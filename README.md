# Axis-AutoSalesdata
Analysis of car sales data using Python for Data analysis. 



```python
# Introduction
# Axis Auto Sales
# Carlos Hugens is the Sales Manager for Axis Auto Sales a low cost regional chain of Used Car Lots.
# Carlos is getting ready for his annual sales meeting and he is looking for the best way to improve his
# sales group's performance.
# His data includes the gender, years of experience, sales training and hours worked per week. It also
# includes the average cars sold per month by each salesperson.
```


```python
# Import Libraries
import pandas as pd
import numpy as np
```


```python
Location = "C:\\users\\Matthew\\Desktop\\Datasets\\axisdata.csv"
```


```python
df = pd.read_csv(Location)
```


```python
df.head()
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
      <th>Fname</th>
      <th>Lname</th>
      <th>Gender</th>
      <th>Hours Worked</th>
      <th>SalesTraining</th>
      <th>Years Experience</th>
      <th>Cars Sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jada</td>
      <td>Walters</td>
      <td>F</td>
      <td>39</td>
      <td>N</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nicole</td>
      <td>Henderson</td>
      <td>F</td>
      <td>46</td>
      <td>N</td>
      <td>3</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tanya</td>
      <td>Moore</td>
      <td>F</td>
      <td>42</td>
      <td>Y</td>
      <td>4</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ronelle</td>
      <td>Jackson</td>
      <td>F</td>
      <td>38</td>
      <td>Y</td>
      <td>5</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Brad</td>
      <td>Sears</td>
      <td>M</td>
      <td>33</td>
      <td>N</td>
      <td>4</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# To determine average cars sold:
df['Cars Sold'].mean()
```




    3.9229229229229228




```python
# To determine maximum number of cars sold:
df['Cars Sold'].max()
```




    7




```python
# To determine minimum numbber of cars sold:
df['Cars Sold'].min()
```




    1




```python
# To convert Gender value to numeric for easier analysis:
def score_to_numeric(x):
    if x=='F':
        return 1
    if x=='M':
        return 0
```


```python
# To apply numeric value to Gender:
df['gender_val'] = df['Gender'].apply(score_to_numeric) 
```


```python
df.tail()
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
      <th>Fname</th>
      <th>Lname</th>
      <th>Gender</th>
      <th>Hours Worked</th>
      <th>SalesTraining</th>
      <th>Years Experience</th>
      <th>Cars Sold</th>
      <th>gender_val</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>994</th>
      <td>Victor</td>
      <td>Kane</td>
      <td>M</td>
      <td>22</td>
      <td>Y</td>
      <td>5</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>995</th>
      <td>Charles</td>
      <td>Turner</td>
      <td>M</td>
      <td>45</td>
      <td>N</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>996</th>
      <td>August</td>
      <td>Franklin</td>
      <td>F</td>
      <td>34</td>
      <td>Y</td>
      <td>4</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>997</th>
      <td>Victoria</td>
      <td>Rogers</td>
      <td>F</td>
      <td>29</td>
      <td>N</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>998</th>
      <td>Mike</td>
      <td>Gerardo</td>
      <td>M</td>
      <td>20</td>
      <td>N</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# To determine the average numbers of cars sold by men:
df.loc[df['gender_val']==0]['Cars Sold'].mean()
```




    4.078431372549019




```python
# To determine the average number of cars sold by women:
df.loc[df['gender_val']==1]['Cars Sold'].mean()
```




    3.7607361963190185




```python
# To determine the average hours worked by those selling greater than 3 cars:
df.loc[df['Cars Sold']>3]['Hours Worked'].mean()
```




    34.740237691001695




```python
# To determine the average years of experience:
df['Years Experience'].mean()
```




    3.026026026026026




```python
# The average years of experience for those selling more than 3 cars:
df.loc[df['Cars Sold']>3]['Years Experience'].mean()
```




    3.0492359932088284




```python
# To convert Sales Training values to numeric values: 
def score_to_numeric(x):
    if x=='N':
        return 0
    if x=='Y':
        return 1
```


```python
# To apply numeric values to Sales Training:
df['Sales Training_val'] = df['SalesTraining'].apply(score_to_numeric)
```


```python
df.tail()
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
      <th>Fname</th>
      <th>Lname</th>
      <th>Gender</th>
      <th>Hours Worked</th>
      <th>SalesTraining</th>
      <th>Years Experience</th>
      <th>Cars Sold</th>
      <th>gender_val</th>
      <th>Sales Training_val</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>994</th>
      <td>Victor</td>
      <td>Kane</td>
      <td>M</td>
      <td>22</td>
      <td>Y</td>
      <td>5</td>
      <td>4</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>995</th>
      <td>Charles</td>
      <td>Turner</td>
      <td>M</td>
      <td>45</td>
      <td>N</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>996</th>
      <td>August</td>
      <td>Franklin</td>
      <td>F</td>
      <td>34</td>
      <td>Y</td>
      <td>4</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>997</th>
      <td>Victoria</td>
      <td>Rogers</td>
      <td>F</td>
      <td>29</td>
      <td>N</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>998</th>
      <td>Mike</td>
      <td>Gerardo</td>
      <td>M</td>
      <td>20</td>
      <td>N</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# To calculate the average cars sold by those who did not receive sales training:
df.loc[df['Sales Training_val']==0]['Cars Sold'].mean()
```




    3.5738498789346247




```python
# To calculate the average cars sold by those who received sales training:
df.loc[df['Sales Training_val']==1]['Cars Sold'].mean()
```




    4.1689419795221845




```python

import statsmodels.formula.api as sm
```


```python
#To determine best indicators as to whether or not someone is a good salesperson
df.corr()
# A good sales person is defined by the number of cars sold
# Hours worked showed the strongest correlation with Cars Sold and hence the best indicator.
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
      <th>Hours Worked</th>
      <th>Years Experience</th>
      <th>Cars Sold</th>
      <th>gender_val</th>
      <th>Sales Training_val</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Hours Worked</th>
      <td>1.000000</td>
      <td>0.028400</td>
      <td>0.251038</td>
      <td>-0.004107</td>
      <td>0.025857</td>
    </tr>
    <tr>
      <th>Years Experience</th>
      <td>0.028400</td>
      <td>1.000000</td>
      <td>0.062577</td>
      <td>0.016194</td>
      <td>-0.017864</td>
    </tr>
    <tr>
      <th>Cars Sold</th>
      <td>0.251038</td>
      <td>0.062577</td>
      <td>1.000000</td>
      <td>-0.104055</td>
      <td>0.192009</td>
    </tr>
    <tr>
      <th>gender_val</th>
      <td>-0.004107</td>
      <td>0.016194</td>
      <td>-0.104055</td>
      <td>1.000000</td>
      <td>-0.040016</td>
    </tr>
    <tr>
      <th>Sales Training_val</th>
      <td>0.025857</td>
      <td>-0.017864</td>
      <td>0.192009</td>
      <td>-0.040016</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
 # Conclusion
# Axis Auto Sales sold an average of four cars per months. Gender of sales person was in no way related to the # of cars sold
# Sales training and years of sales experience had little value. To increase his sales group performance Mr. Hugens should 
# focus on increasing the number of hours worked by each sales person as there is a 25% correlation. Mr. Hugens should 
# consider doing a feasibility study to determine what other factors he can employ to increase car sales.   
```


```python

```
