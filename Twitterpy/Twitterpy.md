

```python
#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import tweepy
import datetime
```


```python
#save the current date and time as a variable
now = datetime.datetime.now()
```


```python
#import vader
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
```


```python
#import twitter api keys
from config import (consumer_key,
                    consumer_secret,
                    access_token,
                    access_token_secret)
```


```python
#set up tweepy call
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
```


```python
#create target terms and make an empty list to store sentiments
target_terms = ('@BBC', '@CBS', '@CNN', '@FoxNews', '@nytimes')
sentiment_array = []
```


```python
#loop through each target
for target in target_terms:
    #create a counter to store the tweets in order of time posted, and reset the counter for each target
    counter = 1
    #loop through to grab the most recent 100 tweets (20 per page x 5)
    for x in range (5):
        public_tweets = api.user_timeline(target, page = x+1)
        #analyze each group of 20 tweets and store compound sentiment in an array
        for tweet in public_tweets:
            name = tweet['user']['name']
            compound = analyzer.polarity_scores(tweet["text"])["compound"]           
            sentiment_array.append({'Agency': name,
                                    'compound': compound,
                                    'Tweets ago': counter})
            counter+=1
```


```python
#convert sentiments dictionary into dataframe
sentiments_pd = pd.DataFrame.from_dict(sentiment_array)
sentiments_pd.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Agency</th>
      <th>Tweets ago</th>
      <th>compound</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BBC</td>
      <td>1</td>
      <td>0.0000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BBC</td>
      <td>2</td>
      <td>-0.4215</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BBC</td>
      <td>3</td>
      <td>0.4939</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BBC</td>
      <td>4</td>
      <td>-0.1027</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BBC</td>
      <td>5</td>
      <td>0.0000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#export dataframe to a csv file
sentiments_pd.to_csv('tweets.csv')
```


```python
#create a seaborn scatter plot using the sentiments dataframe
g = sns.lmplot(x='Tweets ago', y='compound', size=7, aspect=2, hue='Agency', fit_reg=False, data=sentiments_pd, scatter_kws={"s": 100})
g.set_axis_labels('Tweets Ago', 'Tweet Polarity')
plt.title('Analysis as of ' + now.strftime("%Y-%m-%d %H:%M"))
plt.show()
plt.savefig('image_1.png')
```


    <matplotlib.figure.Figure at 0x179b9172fd0>



![png](output_9_1.png)



```python
#grab the mean for each news agency
bbc_mean = float(sentiments_pd.loc[sentiments_pd['Agency'] == 'BBC',['compound']].mean())
cbs_mean = float(sentiments_pd.loc[sentiments_pd['Agency'] == 'CBS',['compound']].mean())
cnn_mean = float(sentiments_pd.loc[sentiments_pd['Agency'] == 'CNN',['compound']].mean())
fox_mean = float(sentiments_pd.loc[sentiments_pd['Agency'] == 'Fox News',['compound']].mean())
nyt_mean = float(sentiments_pd.loc[sentiments_pd['Agency'] == 'The New York Times',['compound']].mean())
```


```python
#create a list of the name data and the names of the news agencies, create a dataframe with the two
mean_data = [bbc_mean, cbs_mean, cnn_mean, fox_mean, nyt_mean]
name_data = ['BBC', 'CBS', 'CNN', 'FOX', 'NYT']
mean_list = pd.DataFrame(list(zip(name_data, mean_data)), columns=['News Agency', 'Tweet Polarity'])
```


```python
#show the new df
mean_list
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>News Agency</th>
      <th>Tweet Polarity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BBC</td>
      <td>0.174900</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CBS</td>
      <td>0.337100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>CNN</td>
      <td>-0.014224</td>
    </tr>
    <tr>
      <th>3</th>
      <td>FOX</td>
      <td>0.011256</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NYT</td>
      <td>-0.019531</td>
    </tr>
  </tbody>
</table>
</div>




```python
#create a new plot of the mean by news agency
sns.set_style('dark')
h = sns.barplot(x='News Agency', y='Tweet Polarity', data=mean_list)
for p in h.patches:
    height = p.get_height()
    h.text(p.get_x()+p.get_width()/2.,
            height + .013,
            '{:1.2f}'.format(height),
            ha="center") 
plt.title('Analysis as of ' + now.strftime("%Y-%m-%d %H:%M"))
plt.show()
plt.savefig('image_2.png')
```


![png](output_13_0.png)



```python
#The first observable trend is there are quite a bit of tweets that have a zero sentiment.
#I would imagine these are pictures or something with no text to analyze

#The second observable trend is that CBS and BBC are quite positive when running the analysis.

#The third trend is that CNN, Fox News and the New York Times are all hovering around zero 
#or even negative.
```
