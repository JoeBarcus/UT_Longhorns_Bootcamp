

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
```


```python
city_data = pd.read_csv('city_data.csv')
ride_data = pd.read_csv('ride_data.csv')
```


```python
city_data.head()
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
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nguyenbury</td>
      <td>8</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East Douglas</td>
      <td>12</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>West Dawnfurt</td>
      <td>34</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rodriguezburgh</td>
      <td>52</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
ride_data.head()
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
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarabury</td>
      <td>2016-01-16 13:49:27</td>
      <td>38.35</td>
      <td>5403689035038</td>
    </tr>
    <tr>
      <th>1</th>
      <td>South Roy</td>
      <td>2016-01-02 18:42:34</td>
      <td>17.49</td>
      <td>4036272335942</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wiseborough</td>
      <td>2016-01-21 17:35:29</td>
      <td>44.18</td>
      <td>3645042422587</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spencertown</td>
      <td>2016-07-31 14:53:22</td>
      <td>6.87</td>
      <td>2242596575892</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nguyenbury</td>
      <td>2016-07-09 04:42:44</td>
      <td>6.28</td>
      <td>1543057793673</td>
    </tr>
  </tbody>
</table>
</div>




```python
combined_data = pd.merge(ride_data,city_data,how='inner',on='city')
```


```python
combined_data.head()
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
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarabury</td>
      <td>2016-01-16 13:49:27</td>
      <td>38.35</td>
      <td>5403689035038</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Sarabury</td>
      <td>2016-07-23 07:42:44</td>
      <td>21.76</td>
      <td>7546681945283</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Sarabury</td>
      <td>2016-04-02 04:32:25</td>
      <td>38.03</td>
      <td>4932495851866</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Sarabury</td>
      <td>2016-06-23 05:03:41</td>
      <td>26.82</td>
      <td>6711035373406</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Sarabury</td>
      <td>2016-09-30 12:48:34</td>
      <td>30.30</td>
      <td>6388737278232</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
combined_data = combined_data.drop_duplicates('ride_id')
```


```python
avg_city = pd.DataFrame()
avg_city_fare = combined_data.groupby(['city']).mean()['fare'].rename('Average Fare ($) Per City')
total_rides_city = combined_data.groupby(['city']).count()['ride_id'].rename('Total Rides Per City')
total_drivers_city = combined_data.groupby(['city']).count()['driver_count'].rename('Total Drivers Per City')
avg_city['Average Fare ($ Per City)'] = avg_city_fare
avg_city['Total Rides Per City'] = total_rides_city
avg_city['Total Drivers Per City'] = total_drivers_city
avg_city.reset_index(inplace=True)
avg_city = pd.merge(avg_city,city_data[['city','type']],how='right',on='city')
avg_city.head()
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
      <th>city</th>
      <th>Average Fare ($ Per City)</th>
      <th>Total Rides Per City</th>
      <th>Total Drivers Per City</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alvarezhaven</td>
      <td>23.928710</td>
      <td>31</td>
      <td>31</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alyssaberg</td>
      <td>20.609615</td>
      <td>26</td>
      <td>26</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Anitamouth</td>
      <td>37.315556</td>
      <td>9</td>
      <td>9</td>
      <td>Suburban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Antoniomouth</td>
      <td>23.625000</td>
      <td>22</td>
      <td>22</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Aprilchester</td>
      <td>21.981579</td>
      <td>19</td>
      <td>19</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
colors = {'Urban': 'red', 'Suburban': 'green', 'Rural': 'blue'}
city_type_plot = plt.scatter(avg_city['Total Rides Per City'], avg_city['Average Fare ($ Per City)'], 
            s=avg_city['Total Drivers Per City']*11,alpha=0.6,
           c=avg_city['type'].apply(lambda x: colors[x]),
           edgecolor = 'face', linewidths = 2)
plt.xlabel('Total Number of Rides (Per City)')
plt.ylabel('Average Fare ($)')
plt.title('Pyber Ride Sharing Data (2016)')
plt.grid(True)
plt.legend(colors)
plt.show()
```


![png](output_8_0.png)



```python
urban_list = ['Urban']
urban = combined_data[combined_data['type'].isin(urban_list)]
urban_fare = len(urban)*urban['fare'].mean()
suburban_list = ['Suburban']
suburban = combined_data[combined_data['type'].isin(suburban_list)]
suburban_fare = len(suburban)*suburban['fare'].mean()
rural_list = ['Rural']
rural = combined_data[combined_data['type'].isin(rural_list)]
rural_fare = len(rural)*rural['fare'].mean()
city_type_fare = [urban_fare, suburban_fare, rural_fare]
urban_list = ['Urban','Suburban','Rural']
```


```python
plt.pie(city_type_fare, labels=urban_list, 
        startangle=120, shadow=True, explode=(0,0,0.2), autopct=('%1.1f%%'))
plt.title('% of total fares by city type')
plt.legend(['Urban', 'Suburban', 'Rural'])
plt.show()
```


![png](output_10_0.png)



```python
urban_list = ['Urban']
urban = combined_data[combined_data['type'].isin(urban_list)]
urban_count = len(urban)
suburban_list = ['Suburban']
suburban = combined_data[combined_data['type'].isin(suburban_list)]
suburban_count = len(suburban)
rural_list = ['Rural']
rural = combined_data[combined_data['type'].isin(rural_list)]
rural_count = len(rural)
city_type_count = [urban_count, suburban_count, rural_count]
urban_list = ['Urban','Suburban','Rural']
```


```python
plt.pie(city_type_count, labels=urban_list, 
        startangle=120, shadow=True, explode=(0,0,0.2), autopct=('%1.1f%%'))
plt.title('% of total rides by city type')
plt.legend(['Urban', 'Suburban', 'Rural'])
plt.show()
```


![png](output_12_0.png)



```python
urban_list = ['Urban']
urban = combined_data[combined_data['type'].isin(urban_list)]
urban_count_driver = len(urban)*urban['driver_count'].mean()
suburban_list = ['Suburban']
suburban = combined_data[combined_data['type'].isin(suburban_list)]
suburban_count_driver = len(suburban)*suburban['driver_count'].mean()
rural_list = ['Rural']
rural = combined_data[combined_data['type'].isin(rural_list)]
rural_count_driver = len(rural)*rural['driver_count'].mean()
city_type_driver = [urban_count_driver, suburban_count_driver, rural_count_driver]
urban_list = ['Urban','Suburban','Rural']
```


```python
plt.pie(city_type_driver, labels=urban_list, 
        startangle=120, shadow=True, explode=(0,0,0.2), autopct=('%1.1f%%'))
plt.title('% of total drivers by city type')
plt.legend(['Urban', 'Suburban', 'Rural'])
plt.show()
```


![png](output_14_0.png)

