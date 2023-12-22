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
    df = pd.read_csv("C:/Users/gianl/Desktop/ApplicazioneF1/KubeFlowPipeline/load_data/diabetes.csv")
    y = df['Outcome']
    x = df.drop('Outcome', axis=1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    x_train, x_test, y_train, y_test = x_train.to_numpy(), x_test.to_numpy(), y_train.to_numpy(), y_test.to_numpy()

    # Creates `data` structure to save and 
    # share train and test datasets.
    #data = {'x_train': x_train.tolist(), 'y_train': y_train.tolist(), 'x_test': x_test.tolist(), 'y_test': y_test.tolist()}

    # Creates a json object based on `data`
    # data_json = json.dumps(data)

    # Saves the json object into a file
    # with open(args.data, 'w') as out_file:
    #    json.dump(data_json, out_file)
    
    '''x_train = data['x_train']
    y_train = data['y_train']
    x_test = data['x_test']
    y_test = data['y_test']'''
 
    # Initialize and train the model
    #model = DecisionTreeClassifier(max_depth=3)
    #model = RandomForestClassifier(n_estimators=1000)
    model = LogisticRegression(max_iter=5000)
    i=0
    while i<10000:
        model.fit(x_train, y_train)
        i+=1

    # Get predictions
    y_pred = model.predict(x_test)
    
    # Get accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    print(str(accuracy))
    '''num_folds = 10
    skf = StratifiedKFold(n_splits=num_folds, shuffle=True, random_state=42)

    # Perform K-fold cross validation
    accuracies = []

    for train_index, test_index in skf.split(x, y):
        x_train, x_test = x[train_index], x[test_index]
        y_train, y_test = y[train_index], y[test_index]

        # Train the model on the training set
        model.fit(x_train, y_train)

        # Get predictions on the test set
        y_pred = model.predict(x_test)

        # Calculate accuracy and store it
        accuracy = accuracy_score(y_test, y_pred)
        accuracies.append(accuracy)

    # Calculate and print the average accuracy across all folds
    average_accuracy = sum(accuracies) / num_folds
    print(f"Average Accuracy: {average_accuracy}")'''
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
    
