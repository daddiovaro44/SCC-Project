import kfp
from kfp import dsl


@dsl.pipeline(name='F1 Pipeline', description='Applies Decision Tree, Logistic Regression and Random Forest for F1 classification problem.')
def F1pipeline():

    # Loads the yaml manifest for each component
    load = kfp.components.load_component_from_file('load_data/load_data.yaml')
    decision_tree = kfp.components.load_component_from_file('decision_tree/decision_tree.yaml')
    logistic_regression = kfp.components.load_component_from_file('logistic_regression/logistic_regression.yaml')
    random_forest = kfp.components.load_component_from_file('random_forest/random_forest.yaml')
    
    # Run load_data task
    load_task = load()

    decision_tree_task = decision_tree(load_task.output)
    logistic_regression_task = logistic_regression(load_task.output)
    random_forest_task = random_forest(load_task.output)


if __name__ == '__main__':
    kfp.compiler.Compiler().compile(F1pipeline, 'F1Pipeline_grid.yaml')
