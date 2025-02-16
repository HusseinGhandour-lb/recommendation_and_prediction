from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestRegressor
import pickle
import pandas as pd

#loads the data to use in ml
def open_data(file, columns_to_drop=None):
    df = pd.read_csv(file)
    if columns_to_drop is None:
        columns_to_drop = []
    df = df.drop(columns_to_drop, axis=1, errors='ignore')
    return df

#encod the needed columns inorder to transform from text to nb
def encod(column, inverse=False):
    global encoder
    encoder = LabelEncoder()
    if not inverse:
        return encoder.fit_transform(column)
    else:
        return encoder.inverse_transform(column)
    
#train the model and scale it to get best result
def train_model(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    xs_train = scaler.fit_transform(x_train)
    xs_test = scaler.transform(x_test)
    return xs_train, xs_test, y_train, y_test, scaler

#use this function in data_app to apply the price prediction
def pred_model(func, input):
    x_train, x_test, y_train, y_test, scaler = func
    model =RandomForestRegressor(n_estimators=100)
    model.fit(x_train, y_train)
    s_input = scaler.transform(input)
    return model.predict(s_input)

#get the score of the model to check errors
def score_model(model, func):
    x_train, x_test, y_train, y_test, scaler = func
    model.fit(x_train, y_train)
    return model.score(x_test, y_test)

#this function is used in the data_app to recommend the user a laptop from the data set
def recommend(df, func, input):
    x_train, x_test, y_train, y_test, scaler = func
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(x_train, y_train)
    s_input = scaler.transform(input)
    recom = model.kneighbors(s_input, n_neighbors=3, return_distance=False)
    recommendations = []
    for index in recom[0]:  
        brand = df.iloc[index]['name']
        price = df.iloc[index]['price']
        recommendations.append((brand, price))  
    return recommendations

df = open_data('csv_files/basic_clean_data_laptop.csv', columns_to_drop=['cpu','Unnamed: 0','discount_price','discount %', 'classification'])
df['brand_name']= encod(df['brand_name'])

x = df.drop(['price', 'name'], axis=1)
y = df['price']
train = train_model(x, y)

#save the model into a pickle file in order to open the train of the model and use in other files
with open('model_laptop.pkl', 'wb') as f:
    pickle.dump({'train':train, 'df':df},f)
