import pandas as pd
import matplotlib.pyplot as plt

# Loading the CSV file with the selection of data from 2016 to 2019
data = pd.read_csv('finance_liquor_16to19.csv')

# Convert the 'date' column to a datetime format (because otherwise there was an error in the data type)
data['date'] = pd.to_datetime(data['date'])

# Filter for years between 2016 and 2019
filtered_data = data.loc[(data['date'].dt.year >= 2016) & (data['date'].dt.year <= 2019)]

# Group the data by zip code and calculate the total bottles sold
total_bottles_sold = filtered_data.groupby('zip_code')['bottles_sold'].sum()

# Create a scatter chart of the number of bottles sold per zip code
plt.scatter(total_bottles_sold.index, total_bottles_sold.values, c=total_bottles_sold.values, cmap='coolwarm')

# Set the title and axis labels
plt.title('Number of Bottles Sold per Zip Code during 2016 to 2019')
plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')

# Display the plot
plt.show()