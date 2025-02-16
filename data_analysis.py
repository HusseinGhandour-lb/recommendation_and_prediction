import pandas as pd

df = pd.read_csv('csv_files/store_laptop_info.csv')

#transform some columns by removing excess characters and changing it datatype 
df['discount_price'] = df['discount_price'].str.replace('$','')
df['discount_price'] = df['discount_price'].str.replace(',','')
df['discount_price'] = pd.to_numeric(df['discount_price'])

df['price'] = df['price'].str.replace('$','')
df['price'] = df['price'].str.replace(',','')
df['price'] = pd.to_numeric(df['price'])

df['discount %'] = df['discount %'].str.replace('%','')
df['discount %'] = df['discount %'].str.replace('New','')
df['discount %'] = pd.to_numeric(df['discount %'])
df = df.dropna()

#create new columns by etracting data from the description column and setting new features
df['cpu'] = df['description'].str.extract(r'Processor: (.*?)™')
df['ram'] = df['description'].str.extract(r'Memory: (.*?)GB')
df['storage'] = df['description'].str.extract(r'Storage: (.*?)B')
df['classification'] = df['price'].apply(lambda x: 'Hight End' if x>1800 else 'Mid End' if x<=1800 and x>=900 else 'Budget')

#reclean the new features and transforming their datatypes
df['cpu'] = df['cpu'].str.split(" ").str[0]

df['storage'] = df['storage'].str.replace('T', '000').str.replace('G', '').str.strip()
df['storage'] = pd.to_numeric(df['storage'], errors='coerce')

df['ram'] = df['ram'].str.replace(r'[x1x2]', '', regex=True).str.strip()
df['ram'] = pd.to_numeric(df['ram'], errors='coerce')

# drop rows that have uncomplete data and exxtract the brand name from name column to foucs our data
df = df.dropna()
df['brand_name'] = df['name'].str.split(' ').str[0:1].astype(str).str.lower().str.replace(r"[\[\]',]", "", regex=True)

#create a new data set in order to extract the relation of data columns with each other 
brands = df.groupby('brand_name')['brand_name'].count()
brands_price = df.groupby('brand_name')['price'].mean()
brands_dis_price = df.groupby('brand_name')['discount_price'].mean()
brands_dis_per = df.groupby('brand_name')['discount %'].mean()

brand_data= {'count_nb': brands, 'price': brands_price, 'discouunt price' : brands_dis_price, 'discount%' : brands_dis_per}
df_brand = pd.DataFrame(brand_data)

#remove any columns and rows that we will not use 
df = df.drop(columns=['description'])
df = df.dropna()

# save the new cleaned and extracted data to new files to use in ml or chart plot
df.to_csv('csv_files/basic_clean_data_laptop.csv')
df_brand.to_csv('csv_files/group_name_laptop.csv')

print('Done! :)')