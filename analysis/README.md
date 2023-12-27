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
# 6.Analysis
Our main anaslysis is relationship between month and name.
Using the analysis we wrote, we found that our students' names at school and their months matched each other.

We made two types of graph:
 1. **Diagram**
 2. **Scatter plot**

## Diagram
```
import pandas as pd
import matplotlib.pyplot as plt
```
* **'import pandas as pd'**: Imports the pandas library and assigns it the alias 'pd' for easier reference in the code.

* **'import matplotlib.pyplot as plt'**: Imports the pyplot module from the matplotlib library and assigns it the alias 'plt' for easier reference in the code.
```
df = pd.read_csv('student.csv', encoding='utf-8')
```
* **'df = pd.read_csv('student.csv', encoding='utf-8')'**: Reads a CSV file named 'student.csv' into a pandas DataFrame called 'df'. The **'encoding='utf-8'** parameter is used to handle any non-ASCII characters in the file.
```
df['First_Letter'] = df['Name'].str[0]
```
* **'df['First_Letter'] = df['Name'].str[0]'**: Creates a new column in the DataFrame ('df') named 'First_Letter' by extracting the first letter of each name in the 'Name' column.

```
letter_mouth_count = df.groupby(['First_Letter', 'Month']).size().unstack()
```
* **'letter_mouth_count = df.groupby(['First_Letter','Month']).size().unstack()'**: Groups the DataFrame by 'First_Letter' and 'Month' columns, counts the occurrences in each group, and then unstacks the result to create a new DataFrame where each unique 'First_Letter' is a row index, each unique 'Month' is a column index, and the values represent the count of occurrences.
```
letter_mouth_count.plot(kind='bar', stacked=True)
```
* **'letter_mouth_count.plot(kind='bar', stacked=True)'**: Creates a stacked bar plot using the 'letter_mouth_count' DataFrame. The 'First_Letter' values are on the x-axis, and each bar is divided into segments representing the count of occurrences for each 'Month'.
```
plt.xlabel('First Letter of Name')
plt.ylabel('Count')
plt.title('Relationship between First Letter of Name and Mouth')
plt.show()
```
* **plt.xlabel('First Letter of Name')**: Sets the label for the x-axis.

* **plt.ylabel('Count')**: Sets the label for the y-axis.

* **plt.title('Relationship between First Letter of Name and Mouth')**: Sets the title of the plot.

* **plt.show()**: Displays the stacked bar plot.

In summary, this code reads a CSV file, extracts the first letter of names, aggregates the data by grouping on the first letter and month, and then visualizes the relationship between the first letter of names and the count of occurrences for each month using a stacked bar plot.

## Scatter plot
```
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read data from a CSV file into a Pandas DataFrame
df = pd.read_csv('student.csv')

# Fill missing values in the 'Name' column with '9'
df['Name'].fillna('9', inplace=True)

# Remove rows where the 'Name' column is equal to '9'
df = df[df['Name'] != '9']

# Convert the 'Month' column to numeric values, handling errors with 'coerce'
df['Month'] = pd.to_numeric(df['Month'], errors='coerce')

# Drop rows with missing values in the 'Month' column
df = df.dropna(subset=['Month'])

# Create a new column 'FirstLetter' containing the first letter of each name
df['FirstLetter'] = df['Name'].str[0]

# Create a scatter plot using 'FirstLetter' as the x-axis and 'Month' as the y-axis
plt.scatter(df['FirstLetter'], df['Month'])

# Set plot title, x-axis label, and y-axis label
plt.title('Name_Month')
plt.xlabel('Name')
plt.ylabel('Month')

# Set y-axis ticks to range from 1 to 12
plt.yticks(range(1, 13))

# Display the plot
plt.show()
```
Summary:

1. **Import Libraries:**

The code imports the necessary libraries: Pandas for data manipulation and Matplotlib for creating visualizations.
2. **Read CSV Data:**

Reads data from a CSV file named 'student.csv' into a Pandas DataFrame named 'df'.
3. **Data Cleaning:**

* Fills missing values in the 'Name' column with the string '9'.
* Removes rows where the 'Name' column is equal to '9'.
* Converts the 'Month' column to numeric values, replacing non-numeric values with NaN.
* Drops rows with missing values in the 'Month' column.
Feature Engineering:
* Creates a new column 'FirstLetter' containing the first letter of each name.
3. **Data Visualization:**

* Plots a scatter plot with 'FirstLetter' on the x-axis and 'Month' on the y-axis.
* Sets plot title, x-axis label, y-axis label.
Sets y-axis ticks to range from 1 to 12.
4. **Display Plot:**
* Finally, displays the created scatter plot.

The code seems to visualize the relationship between the first letter of names and the corresponding months, potentially exploring if there is any pattern or trend.



# 7.Summary
In summary, the entire code is designed to load data, create three different types of charts (for names, birth months, and gender), and display them. The charts help visualize the distribution of the data and draw insights.
