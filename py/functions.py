# Imported librarys
import pandas as pd
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split

# Function that will download the penguin dataset givin a file path to where that file is located
def get_data(PATH):  
    df_penguin = pd.read_csv(PATH)
    return df_penguin

# Cleans data 
def augment_data(dataframe_name):
    # Remove feature that isnt needed
    dataframe_name = dataframe_name.drop('year',axis=1);
    # Convert features that contain text into numbers
    dataframe_name.island = dataframe_name.island.replace({'Biscoe':0,'Dream':1,'Torgensen':2})
    dataframe_name.species = dataframe_name.species.replace({'Adelie':0,'Chinstrap':1,'Gentoo':2})
    dataframe_name.sex = dataframe_name.sex.replace({'female':0,'male':1})
    dataframe_name.diet = dataframe_name.diet.replace({'fish':0,'krill':1,'parental':2,'squid':3})
    dataframe_name.life_stage = dataframe_name.life_stage.replace({'adult':0,'juvenile':1,'chick':2})
    dataframe_name.health_metrics = dataframe_name.health_metrics.replace({'overweight':0,'healthy':1,'underweight':2})
    return dataframe_name

# takes Cleaned dataset returns training and test data
def datasplit_train_test(dataframe_name):
    # make feature dataset by removing class collumn
    X = dataframe_name.drop('species',axis=1)
    # Create target dataset containing class collumn
    y = pd.DataFrame(dataframe_name.species)

    # Scale feature dataset using standard scaler
    scaler = StandardScaler()
    X_scale = scaler.fit_transform(X)
    X_scale = pd.DataFrame(X_scale,columns=X.columns)

    # Using target and feature data split into training and test data 
    X_train, X_test, y_train, y_test = train_test_split(X_scale, y, test_size=0.3, random_state=42,shuffle=True)
    return X_train, X_test, y_train, y_test
