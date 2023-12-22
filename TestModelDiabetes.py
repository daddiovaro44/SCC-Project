import json
import argparse
import pandas as pd
from pathlib import Path
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def _TestModel():

    # Gets and split dataset
    df = pd.read_csv("./data/merged_results.csv")
    
    df = df.dropna()

    y = df['Compound']
    x = df.drop(['Unnamed: 0', 'Compound'], axis=1)


    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    x_train, x_test, y_train, y_test = x_train.to_numpy(), x_test.to_numpy(), y_train.to_numpy(), y_test.to_numpy()
 
    # Initialize and train the model
    model = DecisionTreeClassifier(max_depth=3)
    # model = RandomForestClassifier(n_estimators=1000)
    # model = LogisticRegression(max_iter=5000)
    model.fit(x_train, y_train)


    # Get predictions
    y_pred = model.predict(x_test)
    
    # Get accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    print(str(accuracy))
    
if __name__ == '__main__':
    
    # This component does not receive any input
    # it only outpus one artifact which is `data`.
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--data', type=str)
    
    #args = parser.parse_args()
    
    # Creating the directory where the output file will be created 
    # (the directory may or may not exist).
    #Path(args.data).parent.mkdir(parents=True, exist_ok=True)
    _TestModel()
    
