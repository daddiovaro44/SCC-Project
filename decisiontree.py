import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from joblib import dump


def train_model():

    df = pd.read_csv("./data/merged_results.csv")
    df = df.dropna()

    y = df['Compound']
    x = df.drop(['Unnamed: 0', 'Compound'], axis=1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    x_train, x_test, y_train, y_test = x_train.to_numpy(), x_test.to_numpy(), y_train.to_numpy(), y_test.to_numpy()
 
    model = DecisionTreeClassifier(max_depth=3)
    model.fit(x_train, y_train)
    
    dump(model, './models/decisiontree.joblib')

    return model, x_test, y_test

def test_model(model, x, y):
    y_pred = model.predict(x)
    accuracy = accuracy_score(y, y_pred)
    
    return accuracy
    
if __name__ == '__main__':
    
    trained_model, x, y = train_model()
    acc = test_model(trained_model, x, y)

    print(str(acc))


    
