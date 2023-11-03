"""
    Please write a script to read in the sale results csv file, remove all rows where out is true ('t')
    Using pandas plot method to create the following 4 png files
    - Total sales for the top 10 sires by total sale price
    - Avg sale price for the top 10 buyers by total sale price
    - Avg sale price by book and by sex
    - Avg sale price by month of birth
"""
# Need to install pandas library 
import pandas as pd
import plotly.express as px
import os

if not os.path.exists("/Users/mariola/Desktop"):
    os.mkdir("/Users/mariola/Desktop")

# Need to install plotly library 
pd.options.plotting.backend = "plotly"

# File path
file_path = "/Users/mariola/Downloads/keesep_2023_results.csv"

# Your code here
# 1. Read in the csv file to pandas dataframe
df = pd.read_csv(file_path)

# 2. Remove outs from the data
df = df[df['out'] != 't']

# 3. Total sale for the top 10 sires by gross sale price
top_10_sires = df.groupby('sire_name')['sale_price'].sum().nlargest(10)
print(top_10_sires)
# display data in a bar graph
fig1 = px.bar(top_10_sires.reset_index(), x="sire_name", y="sale_price", labels={'sire_name':'Sire Name', 'sale_price':'Sale Price'}, title="Total sale for the top 10 sires by gross sale price")
fig1.show()
fig1.write_image("/Users/mariola/Desktop/fig1.png")

# 4. Avg sale price for top 10 buyers by gross sale price
top_10_buyers = df.groupby('buyer')['sale_price'].sum().nlargest(10)
# calculates the average sale price for each of the top 10 buyers
avg_sales_price = df[df['buyer'].isin(top_10_buyers.index)].groupby('buyer')['sale_price'].mean()
print(avg_sales_price)
# display data in a bar graph
fig2 = px.bar(top_10_buyers.reset_index(), x="buyer", y="sale_price", labels={'buyer':'Buyer', 'sale_price':'Sale Price'}, title="Average sale price for top 10 buyers by gross sale price")
fig2.show()
fig2.write_image("/Users/mariola/Desktop/fig2.png")

# 5. Avg sale price by book by sex
avg_sales_price_by_book_by_sex = df.groupby(['book', 'sex'])['sale_price'].mean()
print(avg_sales_price_by_book_by_sex)
# display data in a bar graph
fig3 = px.bar(avg_sales_price_by_book_by_sex.reset_index(), x="book", y="sale_price", color="sex", barmode="group", labels={'book':'Book', 'sale_price':'Sale Price'}, title="Average sales price by book by sex")
fig3.show()
fig3.write_image("/Users/mariola/Desktop/fig3.png")

# 6. Avg sale price by month of birth
df['dob'] = pd.to_datetime(df['dob'])
avg_sales_price_by_month_of_birth = df.groupby(df['dob'].dt.month)['sale_price'].mean()
print(avg_sales_price_by_month_of_birth)
# display data in a funnel graph
fig4 = px.funnel(avg_sales_price_by_month_of_birth.reset_index(), x='dob', y='sale_price', color='dob', labels={'dob':'Month of Birth'}, title="Average sales price by month of birth")
fig4.show()
fig4.write_image("/Users/mariola/Desktop/fig4.png")
