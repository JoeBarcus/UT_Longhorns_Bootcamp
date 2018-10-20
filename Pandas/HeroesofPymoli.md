

```python
#Import Libraries
import pandas as pd
import numpy as np
```


```python
#Read the json file
HeroesofPymoli = pd.read_json ('purchase_data2.json')
```


```python
#Check header for format and pertinent info
HeroesofPymoli.head()
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
      <td>Male</td>
      <td>93</td>
      <td>Apocalyptic Battlescythe</td>
      <td>4.49</td>
      <td>Iloni35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>12</td>
      <td>Dawne</td>
      <td>3.36</td>
      <td>Aidaira26</td>
    </tr>
    <tr>
      <th>2</th>
      <td>17</td>
      <td>Male</td>
      <td>5</td>
      <td>Putrid Fan</td>
      <td>2.63</td>
      <td>Irim47</td>
    </tr>
    <tr>
      <th>3</th>
      <td>17</td>
      <td>Male</td>
      <td>123</td>
      <td>Twilight's Carver</td>
      <td>2.55</td>
      <td>Irith83</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22</td>
      <td>Male</td>
      <td>154</td>
      <td>Feral Katana</td>
      <td>4.11</td>
      <td>Philodil43</td>
    </tr>
  </tbody>
</table>
</div>




```python
#unique values in "SN" row to find total players
total_players = HeroesofPymoli['SN'].nunique()
print('Player count: ' + str(total_players))
```

    Player count: 74
    


```python
#Unique Item IDs'
total_items = HeroesofPymoli['Item ID'].nunique()
#Average price of items
average_price = HeroesofPymoli['Price'].mean()
#Total number of purchases, which is the total size of dataframe as each row is a transaction
total_purchases = len(HeroesofPymoli)
#total revenue as a sum of the Price column
total_revenue = HeroesofPymoli['Price'].sum()


print('Total items: ' + str(total_items) + "  Average price: " + '${:,.2f}'.format(average_price) + "  Total Purchases: " + str(total_purchases) + "  Total revenue: " + '${:,.2f}'.format(total_revenue))
```

    Total items: 64  Average price: $2.92  Total Purchases: 78  Total revenue: $228.10
    


```python
#total number of male players
male = (HeroesofPymoli['Gender'] == 'Male').sum()
#total number of female players
female = (HeroesofPymoli['Gender'] == 'Female').sum()
#total number of others by subtracting total dataframe minus male and female to get balance
hermaphodites = total_purchases - male - female

#some basic math here, could also have used .mean() similar to .sum() above
percent_male = male/total_purchases
percent_female = female/total_purchases
percent_hermaphodites = hermaphodites/total_purchases

print('Count of and percentage of male: ' + str(male) + " / " + '{:.2f}%'.format(percent_male * 100) + '.  Count of and percentage of female: ' + str(female) + " / " + '{0:.02f}%'.format(percent_female * 100) + '.  Count of and percentage of other: ' + str(hermaphodites) + " / " + '{0:.02f}%'.format(percent_hermaphodites * 100))
```

    Count of and percentage of male: 64 / 82.05%.  Count of and percentage of female: 13 / 16.67%.  Count of and percentage of other: 1 / 1.28%
    


```python
#count of puchases by male customers
count_purchase_male = HeroesofPymoli.loc[HeroesofPymoli['Gender'] == 'Male', ['Price']].count()
#count purchases by female customers
count_purchase_female = HeroesofPymoli.loc[HeroesofPymoli['Gender'] == 'Female', ['Price']].count()
#count purchases by other customers
count_purchase_hermaphodite = HeroesofPymoli.loc[HeroesofPymoli['Gender'] == 'Other / Non-Disclosed', ['Price']].count()

#average of puchases by male customers
mean_purchase_male = HeroesofPymoli.loc[HeroesofPymoli['Gender'] == 'Male', ['Price']].mean()
#average purchases by female customers
mean_purchase_female = HeroesofPymoli.loc[HeroesofPymoli['Gender'] == 'Female', ['Price']].mean()
#average purchases by other customers
mean_purchase_hermaphodite = HeroesofPymoli.loc[HeroesofPymoli['Gender'] == 'Other / Non-Disclosed', ['Price']].mean()

#total puchases by male customers
total_purchase_value_male = HeroesofPymoli.loc[HeroesofPymoli['Gender'] == 'Male', ['Price']].sum()
#total purchases by female customers
total_purchase_value_female = HeroesofPymoli.loc[HeroesofPymoli['Gender'] == 'Female', ['Price']].sum()
#total purchases by other customers
total_purchase_value_hermaphodite = HeroesofPymoli.loc[HeroesofPymoli['Gender'] == 'Other / Non-Disclosed', ['Price']].sum()

#normalized total for male players
normalized_male = total_purchase_value_male/count_purchase_male
#normalized total for female players
normalized_female = total_purchase_value_female/count_purchase_female
#normalized total for other customers
normalized_hermaphodite = total_purchase_value_hermaphodite/count_purchase_hermaphodite
```


```python
#create age group bins
bins = [0, 10, 14, 18, 22, 26, 30, 34, 100]
#assign the labels to the bins
group_names = ['Under 10', '10 to 14', '15 to 18', '19 to 22', '23 to 26', '27 to 30', '31 to 34', 'Over 34']
```


```python
#use pd.cut to split up the Age column into respective bins
HeroesofPymoli['Age Range'] = pd.cut(HeroesofPymoli['Age'], bins= bins, labels = group_names)
```


```python
#use groupby to perform aggregation based off Age Range bins, and create a new dataframe with the index of the bins
age_groups1 = HeroesofPymoli.groupby('Age Range')
age_groups = HeroesofPymoli.set_index('Age Range')
#use some math based off the groupby df to add to the properly indexed df
age_groups['Purchase Count'] = age_groups1['Price'].count()
age_groups['Average Purchase Price'] = age_groups1['Price'].mean()
age_groups['Total Purchase Value'] = age_groups1['Price'].sum()
age_groups['Normalized Totals'] = (age_groups1['Price'].sum())/(age_groups1['Price'].count())
#get rid of the columns not needed
age_groups.drop(['Age', 'Gender', 'Item ID', 'Item Name', 'Price', 'SN'], axis = 1, inplace = True)
#remove duplicate rows
age_groups = age_groups.drop_duplicates()
#show dataframe
age_groups
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
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Age Range</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>19 to 22</th>
      <td>20</td>
      <td>3.017000</td>
      <td>60.34</td>
      <td>3.017000</td>
    </tr>
    <tr>
      <th>15 to 18</th>
      <td>11</td>
      <td>2.764545</td>
      <td>30.41</td>
      <td>2.764545</td>
    </tr>
    <tr>
      <th>Under 10</th>
      <td>5</td>
      <td>2.764000</td>
      <td>13.82</td>
      <td>2.764000</td>
    </tr>
    <tr>
      <th>Over 34</th>
      <td>7</td>
      <td>3.717143</td>
      <td>26.02</td>
      <td>3.717143</td>
    </tr>
    <tr>
      <th>27 to 30</th>
      <td>4</td>
      <td>2.692500</td>
      <td>10.77</td>
      <td>2.692500</td>
    </tr>
    <tr>
      <th>23 to 26</th>
      <td>23</td>
      <td>2.939565</td>
      <td>67.61</td>
      <td>2.939565</td>
    </tr>
    <tr>
      <th>31 to 34</th>
      <td>5</td>
      <td>2.034000</td>
      <td>10.17</td>
      <td>2.034000</td>
    </tr>
    <tr>
      <th>10 to 14</th>
      <td>3</td>
      <td>2.986667</td>
      <td>8.96</td>
      <td>2.986667</td>
    </tr>
  </tbody>
</table>
</div>




```python
#group by SN to perform aggregation
players = HeroesofPymoli.groupby('SN')
#calculate the sum, count and mean of all players purchases grouped by player, and return 5 largest spenders
top_5_players = players['Price'].sum()
top_5_players_count = players['Price'].count()
top_5_players_mean = players['Price'].mean()
#change series to frame
top_5_players = top_5_players.to_frame()
top_5_players_count = top_5_players_count.to_frame()
top_5_players_mean = top_5_players_mean.to_frame()
#reset index
top_5_players = top_5_players.reset_index()
top_5_players_count = top_5_players_count.reset_index()
top_5_players_mean = top_5_players_mean.reset_index()
#merge the dataframes into one
inner_merge_df_top5_players = pd.merge(pd.merge(top_5_players,top_5_players_count, on='SN'), top_5_players_mean, on='SN')
#rename the columns
inner_merge_df_top5_players = inner_merge_df_top5_players.rename(columns={'Price_x': 'Total Purchase Value', 'Price_y': 'Purchase Count'})
#sort by total purchases and print head of combined dataframe
inner_merge_df_top5_players.sort_values('Total Purchase Value',ascending = False).head(5)
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
      <th>SN</th>
      <th>Total Purchase Value</th>
      <th>Purchase Count</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>63</th>
      <td>Sundaky74</td>
      <td>7.41</td>
      <td>2</td>
      <td>3.705</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Aidaira26</td>
      <td>5.13</td>
      <td>2</td>
      <td>2.565</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Eusty71</td>
      <td>4.81</td>
      <td>1</td>
      <td>4.810</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Chanirra64</td>
      <td>4.78</td>
      <td>1</td>
      <td>4.780</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Alarap40</td>
      <td>4.71</td>
      <td>1</td>
      <td>4.710</td>
    </tr>
  </tbody>
</table>
</div>




```python
#group by Item ID to perform aggregation
items_group = HeroesofPymoli.groupby('Item ID')
#create a new df with the counts of items
items_group_count = items_group.count()
#sort the values from largest to smallest on purchase count
items_group_count.sort_values('SN', ascending=False, inplace=True)
#create the purchase count column based off any other column
items_group_count['Purchase Count'] = items_group_count['Age']
#get rid of excess columns
items_group_count.drop(['Age','Gender','SN','Price','Age Range'], axis=1, inplace=True)
#reset index to use merge below
items_group_count.reset_index(inplace=True)
#merge the main df with the item group df to grab other info
merge_item_group = pd.merge(items_group_count,HeroesofPymoli, on='Item ID')
#get rid of even more garbage columns
merge_item_group.drop(['Item Name_x', 'Age', 'Gender', 'SN', 'Age Range'], axis=1, inplace=True)
#use math for total purchase value
merge_item_group['Total Purchase Value'] = merge_item_group['Price'] * merge_item_group['Purchase Count']
#rename the nasty looking column
merge_item_group = merge_item_group.rename(columns={'Item Name_y': 'Item Name'})
#remove duplicates
merge_item_group = merge_item_group.drop_duplicates()
#voilah!
merge_item_group.head()
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
      <th>Item ID</th>
      <th>Purchase Count</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>94</td>
      <td>3</td>
      <td>Mourning Blade</td>
      <td>3.64</td>
      <td>10.92</td>
    </tr>
    <tr>
      <th>3</th>
      <td>90</td>
      <td>2</td>
      <td>Betrayer</td>
      <td>4.12</td>
      <td>8.24</td>
    </tr>
    <tr>
      <th>5</th>
      <td>111</td>
      <td>2</td>
      <td>Misery's End</td>
      <td>1.79</td>
      <td>3.58</td>
    </tr>
    <tr>
      <th>7</th>
      <td>64</td>
      <td>2</td>
      <td>Fusion Pummel</td>
      <td>2.42</td>
      <td>4.84</td>
    </tr>
    <tr>
      <th>9</th>
      <td>154</td>
      <td>2</td>
      <td>Feral Katana</td>
      <td>4.11</td>
      <td>8.22</td>
    </tr>
  </tbody>
</table>
</div>




```python
#to get largest total purchase value, simply resort the above dataframe by Total Purchase Value...
merge_item_group.sort_values('Total Purchase Value', ascending=False, inplace=True)
merge_item_group.head()
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
      <th>Item ID</th>
      <th>Purchase Count</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>94</td>
      <td>3</td>
      <td>Mourning Blade</td>
      <td>3.64</td>
      <td>10.92</td>
    </tr>
    <tr>
      <th>13</th>
      <td>117</td>
      <td>2</td>
      <td>Heartstriker, Legacy of the Light</td>
      <td>4.71</td>
      <td>9.42</td>
    </tr>
    <tr>
      <th>17</th>
      <td>93</td>
      <td>2</td>
      <td>Apocalyptic Battlescythe</td>
      <td>4.49</td>
      <td>8.98</td>
    </tr>
    <tr>
      <th>3</th>
      <td>90</td>
      <td>2</td>
      <td>Betrayer</td>
      <td>4.12</td>
      <td>8.24</td>
    </tr>
    <tr>
      <th>9</th>
      <td>154</td>
      <td>2</td>
      <td>Feral Katana</td>
      <td>4.11</td>
      <td>8.22</td>
    </tr>
  </tbody>
</table>
</div>


