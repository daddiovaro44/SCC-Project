import json
import argparse
from pathlib import Path
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from joblib import dump
from sklearn.model_selection import GridSearchCV

def _decision_tree(args):

    # Open and reads file "data"
    with open(args.data) as data_file:
        data = json.load(data_file)
    
    # The excted data type is 'dict', however since the file
    # was loaded as a json object, it is first loaded as a string
    # thus we need to load again from such string in order to get 
    # the dict-type object.
    data = json.loads(data)

    x_train = data['x_train']
    y_train = data['y_train']
    x_test = data['x_test']
    y_test = data['y_test']
    
    param_grid = {
        'max_depth': [10, 20, 30],  
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 5, 10],
        'criterion': ['gini', 'entropy']
    }

    # Initialize the DecisionTreeClassifier
    dt_classifier = DecisionTreeClassifier()

    # Initialize GridSearchCV
    grid_search = GridSearchCV(dt_classifier, param_grid, cv=3, scoring='accuracy', verbose=2, n_jobs=-1)

    # Fit the grid search to the data
    grid_search.fit(x_train, y_train)

    # Get the best parameters from the grid search
    best_params = grid_search.best_params_

    # Get predictions using the best model
    y_pred = grid_search.predict(x_test)
    
    # Get accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Save the best model
    dump(grid_search.best_estimator_, args.model)
    
    with open(args.accuracy, 'w') as accuracy_file:
        accuracy_file.write(str(accuracy))
    
    with open(args.best_param, 'w') as accuracy_file:
        accuracy_file.write(str(best_params))  
      
if __name__ == '__main__':

    # Defining and parsing the command-line arguments
    parser = argparse.ArgumentParser(description='Decision Tree training')
    parser.add_argument('--data', type=str)
    parser.add_argument('--accuracy', type=str)
    parser.add_argument('--model', type=str)
    parser.add_argument('--best_param', type=str)
    
    args = parser.parse_args()

    # Creating the directory where the output file will be created (the directory may or may not exist).
    Path(args.model).parent.mkdir(parents=True, exist_ok=True)
    Path(args.accuracy).parent.mkdir(parents=True, exist_ok=True)
    Path(args.best_param).parent.mkdir(parents=True, exist_ok=True)
    
    _decision_tree(args)
