# Formula 1 Tyre Compound Prediction App


## Data
Data used in this application are collected from [Fast-F1](https://github.com/theOehrly/Fast-F1/tree/master) repository. We decided to use part of this data, information from 2019 to 2023 are retrived, filtered and ready to use. Then are saved in the `./data/` directory.

## Local Execution of the Web App
### Pre
To collect data has to be installed the Fast-F1 library:
```bash
pip install fastf1
```
Then to execute the application are needed:
- pandas
- streamlit
- joblib
- scikit-learn
To execute them:
```bash
pip install -r requirements.txt
```
## Execution
Just open a terminal and run the following command:
```bash
streamlit run web_app.py
```

## Kubernetes
### Docker
The container is already uploaded on [Docker Hub](https://hub.docker.com/repositories/damiov) with the name `formula1`

### Kind
After having installed Kind on your machine, it is needed to create the cluster:
```
kind create cluster --config=multinode-config-with-port-mapping.yaml --name formula1
```
This will create a Kubernetes cluster with one control-plane node and three worker node, with the exposed port on `localhost:30070`.

Then to deploy the Formula1 Compound Web App is needed to run the following command:
```
kubectl create --filename k8s_formula1_deployment.yaml
```
This command will run the actual deployment of the web application on the previous created Kubernetes cluster.

### View web application
At this point the web application can be seen going on:
```
http://localhost:30070
```

## Kubeflow

** manca **
## Authors

- [@daddiovaro44](https://github.com/daddiovaro44)
- [@Gianluca5galasso](https://github.com/Gianluca5galasso)

