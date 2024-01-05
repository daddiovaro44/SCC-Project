import kfp
from kfp import dsl
from kfp.components import func_to_container_op


@func_to_container_op
def show_results(random_forest_accuracy: float, random_forest_best_param: str) -> None:

    # Given the outputs from random_forest components the results are shown.
    print(f"Random forest (best_param): {random_forest_best_param}")
    print(f"Random forest (accuracy): {random_forest_accuracy}")

@dsl.pipeline(name='F1 Pipeline retraining', description='Pipeline for retraing best model of F1 classification problem.')
def F1pipeline_retraining():

    # Loads the yaml manifest for each component
    load = kfp.components.load_component_from_file('load_data/load_data_retraining.yaml')
    random_forest = kfp.components.load_component_from_file('random_forest/random_forest_retraining.yaml')
    
    # Run load_data task
    load_task = load()
   
    # the output generated by "load_task".
    random_forest_task = random_forest(load_task.output)
    
    # Given the outputs from "random_forest"
    # the component "show_results" is called to print the results.
    show_results(random_forest_task.outputs['Accuracy'],random_forest_task.outputs['Best_param'])

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(F1pipeline_retraining, 'F1Pipeline_retraining.yaml')
