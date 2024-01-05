# Formula 1 Tyre Compound Prediction App

Prediction application which can be used from any racing team using different tyre compound for their races.

It is called Formula 1 because uses a dataset based on 2019-present kind of compound used for the highest motorsport category: soft, medium, hard, intermediate and wet.

To use it for your kind tyre compound change the dataset and execute the preparation of the data to match with the code of this repository.

## Data

Data used in this application are collected from [Fast-F1](https://github.com/theOehrly/Fast-F1/tree/master) repository. We decided to use part of this data, information from 2019 to 2023 are retrived, filtered and ready to use. Then are saved in the `./data` directory.

In the `prepare_data.ipynb` file data are collected from the Fast-F1 library from 2019 to 2023. Then are selected only Compound, TyreLife, Position and GridPosition informations, instead about wheather are collected AirTemp, Humidity, Pressure, Rainfall, TrackTemp and WindSpeed. In addition are added year and round number, then saved in the `merged_results.csv`. In an other file are saved the round number and corresponding round name of the 2023 year.

About `additional_data.csv` and `initial_training.csv` are the same data that are in the `merged_results.csv`, but from this are removed last 300 lines and inserted in `additional_data.csv`.

## Local Execution of the Web App

### Pre

To collect data, download the Fast-F1 library:

```bash
pip install fastf1
```

Then to execute the application are needed:

- pandas
- streamlit
- joblib
- scikit-learn

To download needed libraries:

```bash
pip install -r requirements.txt
```

## Execution

Just open a terminal in the directory and run the following command:

```bash
streamlit run web_app.py
```

## Kubernetes

### Docker

The container is already uploaded on [Docker Hub](https://hub.docker.com/repositories/damiov) with the name `formula1`

### Kind

After having installed Kind on your machine, it is needed to create the cluster:

```
kind create cluster --config=multinode-config-with-port-mapping.yaml --name=formula1
```

This will create a Kubernetes cluster with one control-plane node and three worker node, with the exposed port on `localhost:30070`.

To install the Kubernetes Dashboard are needed some files and to execute some code. First of all run:

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-beta8/aio/deploy/recommended.yaml
```

Then are needed the `dashboard-adminuser.yaml` file and the `cluster_rolebinding.yaml` file to create an user with necessary permissions. To apply this configurations:

```
kubectl apply -f dashboard-adminuser.yaml
kubectl apply -f cluster_rolebinding.yaml
```

To get the token to have access to the dashboard run:

```
kubectl -n kubernetes-dashboard create token admin-user
```

Keep this token, and to access to the dashboard run:

```
kubectl proxy
```

Now, go to [Dashboard](http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/) and insert the token to get in the dashboard.

Then to deploy the Formula1 Compound Web App is needed to run the following commands:

```
kubectl create --filename=k8s_formula1_deployment.yaml
kubectl create --filename=k8s_formula1_autoscale.yaml
```

These commands will run the actual deployment of the web application on the previous created Kubernetes cluster and the horizontal autoscaling configuration.

Instead, to run the vertical autoscaling is needed to have in the system the kubernetes autoscaler repository, othwerwise:

```
git clone https://github.com/kubernetes/autoscaler.git
cd autoscaler/vertical-pod-autoscaler/
./hack/vpa-up.sh
```

Then to have automatically computed resource requirements execute the command:

```
kubectl create --filename=k8s_formula1_vertical_autoscale.yaml
```

### View Web Application

At this point the web application can be seen at:

```
http://localhost:30070
```

## Kubeflow

Even in this case all the container are uploaded on [Docker Hub](https://hub.docker.com/repositories/gianluca12galasso).

First thing to do, install Kubeflow Pipelines:

```
export PIPELINE_VERSION=2.0.3
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic-pns?ref=$PIPELINE_VERSION"
```

After several minutes, when all the pods are running (check them running `kubectl get pods -A`) try to access to Kubeflow Pipelines UI by port-forwarding:

```
kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80
```

Then open Kubeflow Pipelines UI at:

```
http://localhost:8080
```

After go to `Pipelines` section, click on `Upload pipeline` button and

1. upload `F1pipeline.yaml` to get a full training pipeline:

- Uploads all data
- Training 3 models: Decision Tree, Logistic Regression, Random Forest
- Shows results: accuracy and model dump of each trained model

2. upload `F1pipeline_retraining.yaml` to get a retraining pipeline of Random Forest model:

- Uploads all data
- Training of a Random Forest model on a section of the data
- Retrains of the same model on another section of the data
- Shows results: accuracy and model dump of random forest model

After the upload of a pipeline, to execute it click on the `Create run` button, then press `Start` and wait the end. After to get results click on `Show results` component and in the "Output Artifacts" section you get accuracy and parameters of the best models. Instead, to get the retrained model click on `(Decision tree, Logistic Regression, Random Forest) classifier`, go to "Output Artifacts" to get all data about the best model, including the model dump.

The model you get, renamed as `model.joblib` and put in the `model` directory can be used in the deployment of the web application.

## Notes

Where is required the `scikit-learn` package is used the `1.3.0` version for compatibility reason with the `load` function of `joblib` library.

## Authors

- [@daddiovaro44](https://github.com/daddiovaro44)
- [@Gianluca5galasso](https://github.com/Gianluca5galasso)
