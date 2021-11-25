# Austin House Prices

## Summary  
The User will be asked to input housing features and click submit, which will send all the data through a machine learning algorithm to get the resulting housing price. The dashboard also includes a tab to display a map where houses can be selected to look at their features and prices. Another tab includes stats where graphs and plots can be viewed.

## Members  
Ajaypal Paneser (Solo)  

## Dataset Used
https://www.kaggle.com/ericpierce/austinhousingprices/tasks?taskId=4044

## Database
I used postgresql/PGAdmin for the database. The Databasae was split into 4 tables: house_features, house_info, house_location, house_school. 
![PGADMIN](Images/PGADMIN.png)

## Machin Learning Algorithm
For the machine learning algorithm

``` python
def predict(hometype, hasgarage, 
yearbuilt, zipcode, lotsizesqft, livingareasqft, 
numofbathrooms, numofbedrooms, numofstories, avgschooldistance):
    # import from database
    connection = psycopg2.connect(user="postgres", password=db_password, host="localhost", port="5432", database="AustinHomes")
    query = "SELECT * FROM house_info INNER JOIN house_location ON house_info.zpid = house_location.zpid INNER JOIN house_school ON house_location.zpid = house_school.zpid"
    a_sales_df = pd.read_sql(query, connection)

    # create copy for use with the machine learning model
    ml_data = a_sales_df.loc[a_sales_df['city'] == "austin"].copy()

    # use only the columns that will be used in the model
    ml_data = ml_data[['hometype', 'hasgarage', 'yearbuilt', 'latestprice', 'zipcode', 
                    'latest_saleyear', 'lotsizesqft', 'livingareasqft', 'numofbathrooms', 
                    'numofbedrooms', 'numofstories', 'avgschooldistance']]

    # Clean unnecessary data
    ml_data = ml_data.loc[ml_data['numofbedrooms'] != 0]
    ml_data = ml_data.loc[ml_data['numofbedrooms'] < 11]
    ml_data = ml_data.loc[ml_data['numofbathrooms'] < 11]
    ml_data = ml_data.loc[ml_data['hometype'] != 'Other']
    ml_data = ml_data.loc[ml_data['hometype'] != 'Vacant Land']
    ml_data = ml_data.loc[ml_data['lotsizesqft'] < (ml_data['lotsizesqft'].max()*.001)]


    X = ml_data.drop("latestprice", axis=1)
    y = ml_data['latestprice']

    # convert home types into numbers
    home_type = {
        'Single Family': 0, 
        'Residential': 1,
        'Mobile / Manufactured': 2,
        'Townhouse': 3,
        'Condo': 4,
        'Vacant Land': 5,
        'Multiple Occupancy': 6,
        'Other': 7,
        'Apartment': 8,
        'MultiFamily': 9
    }

    X['hometype'] = X['hometype'].apply(lambda x: home_type[x])

    # change the rest into numerical datatypes as well
    le = LabelEncoder()
    X['hasgarage'] = le.fit_transform(X['hasgarage'])

    # split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2)

    clf = GradientBoostingRegressor(n_estimators=400, max_depth=5, min_samples_split=2, learning_rate=.1, loss='squared_error')
    clf.fit(X_train, y_train)
    print("Accuracy Score: ", clf.score(X_test, y_test))
    result = clf.predict([[hometype, hasgarage, yearbuilt, zipcode, 2021, lotsizesqft, 
    livingareasqft, numofbathrooms, numofbedrooms, numofstories, avgschooldistance]])

    return result
```
