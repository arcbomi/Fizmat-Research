# Analysis
----

# 1.Import Libraries:
```
import pandas as pd
import matplotlib.pyplot as plt
```
Here, we import the **pandas** library for working with DataFrames
and **matplotlib.pyplot** library for creating plots.
# 2.Load Data from csv file:
```
file_path = 'student.csv'
df_people = pd.read_csv(file_path)
```
We use **pd.read_csv** to load data from a *CSV* file into a DataFrame.
# 3.Create a Chart for Names:
```
plt.figure(figsize=(155, 6))
df_people['Name'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Name distribution')
plt.xlabel('Name')
plt.ylabel('Number')
plt.xticks(rotation=90)
plt.show()
```
Here, we use **value_counts()** to count unique values in the *"Name"* column and create a bar chart using **plot(kind='bar')**. Titles and axis labels are added for better readability.
![Name](../res/Name.png)
# 4.Create a Chart for Birthdays:
```
plt.figure(figsize=(10, 6))
df_people['Month'].apply(lambda x: pd.to_datetime(x, format='%m').month_name()).value_counts().sort_index().plot(kind='bar', color='red')
plt.title('Distribution of dates of birth by month')
plt.xlabel('Month')
plt.ylabel('Number')
plt.xticks(rotation=45)
plt.show()
```
Here, we use **apply** and **pd.to_datetime** to convert numeric months into their names. Then, we create a *bar chart* similar to the first one.
![Month](../res/Month.png)
# 5.Create a Chart for Gender:
```
plt.figure(figsize=(6, 4))
df_people['Gender'].value_counts().plot(kind='bar', color=['lightblue', 'lightcoral'])
plt.title('Gender distribution')
plt.xlabel('Gender')
plt.ylabel('Number')
plt.xticks(rotation=0)
plt.show()
```
Here, we create a *bar chart* for the "Gender" column. Column colors are specified as a list.
![Gender](../res/Gender.png)

# 6.Summary
In summary, the entire code is designed to load data, create three different types of charts (for names, birth months, and gender), and display them. The charts help visualize the distribution of the data and draw insights.
