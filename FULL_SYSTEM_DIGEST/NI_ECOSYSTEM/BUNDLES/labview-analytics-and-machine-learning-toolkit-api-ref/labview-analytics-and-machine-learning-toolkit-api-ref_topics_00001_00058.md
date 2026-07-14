# NI DOCUMENT BUNDLE: labview-analytics-and-machine-learning-toolkit-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-analytics-and-machine-learning-toolkit-api-ref start=1 end=58 -->
<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_amlpcat2q_prop.html language=enus -->
## TOPIC 00001: AML PCA T2Q Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_amlpcat2q_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_amlpcat2q_prop.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AML PCA T2Q Properties

Wire the **untrained PCA baseline model** output of the [Initialize Anomaly Detection Model (PCA T2Q)](aml_initialize_anomaly_detection_model_pca_t2q.html) VI to the **reference** input of a standard Property Node to get an AML PCA T2Q Property Node. This Property Node has the following properties:

| Property | Access | Data Type | Description |
| --- | --- | --- | --- |
| Eigenvectors | Read Only |  | Returns the eigenvectors to calculate the principal components. The number of rows equals the number of features of the training data. The PCA baseline model uses a subset of the eigenvectors of the covariance matrix to calculate the principal components in the input data. |
| Hyperparameters | Read Only |  | Returns the hyperparameters of the PCA baseline model. |
| Model Initialized? | Read Only |  | Returns whether the model is initialized. |
| Model Trained? | Read Only |  | Returns whether the model is trained. |
| Mean Values | Read Only |  | Returns the mean value of each feature in the training data. |
| Threshold for Q | Read Only |  | Returns the threshold for Q based on confidence level. You can use the threshold for Q to determine whether the Q values of the data for deployment are abnormal. |
| Threshold for T2 | Read Only |  | Returns the threshold for T2 based on confidence level. You can use the threshold for T2 to determine whether the T2 values of the data for deployment are abnormal. |
| Variance | Read Only |  | Returns the variance of the principal components. The number of rows equals the number of principal components. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_analyticsmodel_prop.html language=enus -->
## TOPIC 00002: AML Analytics Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_analyticsmodel_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_analyticsmodel_prop.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AML Analytics Properties

Wire the **model out** output of any Analytics and Machine Learning VI to the **reference** input of a standard Property Node to get an AML Analytics Property Node. This Property Node has the following properties:

| Property | Access | Data Type | Description |
| --- | --- | --- | --- |
| Anomaly Detection Model Type (One Shot) | Read Only |  | Returns the type of a trained anomaly detection model when you perform one shot training. |
| Anomaly Detection Model Type (Batch) | Read Only |  | Returns the type of a trained anomaly detection model when you perform batch training. |
| Classification Model Type | Read Only |  | Returns the type of a trained classification model. |
| Clustering Model Type | Read Only |  | Returns the type of a trained clustering model. |
| Feature Manipulation Model Type | Read Only |  | Returns the type of a trained feature manipulation model. |
| Running Mode of Anomaly Detection | Read Only |  | Returns the running mode of a trained anomaly detection model. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_anomaly_detection.html language=enus -->
## TOPIC 00003: Anomaly Detection VIs

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_anomaly_detection.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_anomaly_detection.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Anomaly Detection VIs

**Owning Palette:** [Analytics and Machine Learning VIs](../lvaml/aml_pal.html)

**Requires:** Analytics and Machine Learning Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Anomaly Detection VIs to initialize, train, and deploy unsupervised anomaly detection models that detect anomalies in unlabeled data.

| Palette Object | Description |
| --- | --- |
| Deploy Anomaly Detection Model | Deploys a trained anomaly detection model and returns the health index of input data. |
| Initialize Anomaly Detection Model (GMM-CV) | Initializes the hyperparameters of the Gaussian mixture model (GMM) algorithm. |
| Initialize Anomaly Detection Model (One-Class SVM) | Initializes the hyperparameters of the one-class support vector machine (SVM) algorithm. This VI uses the nu-SVM algorithm. |
| Initialize Anomaly Detection Model (PCA T2Q) | Initializes the hyperparameters of the principal component analysis (PCA) algorithm. |
| Initialize Anomaly Detection Model (SOM-MQE) | Initializes the hyperparameters of the self-organizing map (SOM) algorithm. |
| Set Anomaly Detection Model | Sets properties for a trained anomaly detection model before deployment. |
| Train Anomaly Detection Model | Trains an anomaly detection model. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_anomalydetectionmodel_prop.html language=enus -->
## TOPIC 00004: AML Anomaly Detection Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_anomalydetectionmodel_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_anomalydetectionmodel_prop.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AML Anomaly Detection Properties

Wire the **anomaly detection model info out** output of the [Train Anomaly Detection Model](aml_train_anomaly_detection_model.html) VI to the **reference** input of a standard Property Node to get an AML Anomaly Detection Property Node. You must ensure that **anomaly detection model info in** is unwired. This Property Node has the following properties:

| Property | Access | Data Type | Description |
| --- | --- | --- | --- |
| Model Initialized? | Read Only |  | Returns whether the model is initialized. |
| Model Trained? | Read Only |  | Returns whether the model is trained. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_classification.html language=enus -->
## TOPIC 00005: Classification VIs

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_classification.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_classification.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Classification VIs

**Owning Palette:** [Analytics and Machine Learning VIs](../lvaml/aml_pal.html)

**Requires:** Analytics and Machine Learning Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Classification VIs to initialize, train, evaluate, and deploy classification models that classify given sets of categories.

| Palette Object | Description |
| --- | --- |
| Deploy Classification Model | Deploys a trained classification model and returns predicted labels of input data. |
| Evaluate Classification Model | Evaluates a trained classification model by using new test data with labels. |
| Initialize Classification Model (LR) | Initializes the hyperparameters of the logistic regression (LR) algorithm. You can either set the hyperparameters or specify multiple values for each hyperparameter. If you specify multiple values for each hyperparameter, the Train Classification Model VI uses grid search to find the optimal set of hyperparameters. |
| Initialize Classification Model (NN) | Initializes the hyperparameters of the neural network (NN) algorithm. You can either directly set the hyperparameters or specify multiple values for each hyperparameter. If you specify multiple values for each hyperparameter, the Train Classification Model VI uses grid search to find the optimal set of hyperparameters. This VI supports single hidden layers only. |
| Initialize Classification Model (SVM) | Initializes the hyperparameters of the support vector machine (SVM) algorithm. You can either directly set the hyperparameters or specify multiple values for each hyperparameter. If you specify multiple values for each hyperparameter, the Train Classification Model VI uses grid search to find the optimal set of hyperparameters. |
| Set Classification Model | Sets properties for a trained classification model before deployment. |
| Train Classification Model | Trains a classification model. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_classificationmodel_prop.html language=enus -->
## TOPIC 00006: AML Classification Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_classificationmodel_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_classificationmodel_prop.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AML Classification Properties

Wire the **classification model info out** output of the [Train Classification Model](aml_train_classification_model.html) VI to the **reference** input of a standard Property Node to get an AML Classification Property Node. You must ensure that **classification model info out** is unwired. This Property Node has the following properties:

| Property | Access | Data Type | Description |
| --- | --- | --- | --- |
| Cross Validation Configuration | Read Only |  | Returns settings for cross validation. |
| Hyperparameter Optimization | Read Only |  | Returns the method of optimization to determine the optimal hyperparameter settings. |
| Label of Each Class | Read Only |  | Returns the label of each class. |
| Model Initialized? | Read Only |  | Returns whether the model is initialized. |
| Model Trained? | Read Only |  | Returns whether the model is trained. |
| Number of Classes | Read Only |  | Returns the number of classes. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_clustering.html language=enus -->
## TOPIC 00007: Clustering VIs

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_clustering.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_clustering.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Clustering VIs

**Owning Palette:** [Analytics and Machine Learning VIs](../lvaml/aml_pal.html)

**Requires:** Analytics and Machine Learning Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Clustering VIs to initialize, train, evaluate, and deploy clustering models that group data items into clusters. Data items in the same cluster share more similarities than those in other clusters.

| Palette Object | Description |
| --- | --- |
| Deploy Clustering Model | Deploys a trained model and returns predicted labels of input data. |
| Evaluate Clustering Model | Evaluates a trained clustering model with training data or new test data. |
| Initialize Clustering Model (DBSCAN) | Initializes the hyperparameters of the density-based spatial clustering of applications with noise (DBSCAN) algorithm. You can either directly set the hyperparameters or specify multiple values for each hyperparameter. If you specify multiple values for each hyperparameter, the Train Clustering Model VI uses grid search to find the optimal set of hyperparameters. |
| Initialize Clustering Model (GMM) | Initializes the hyperparameters of the Gaussian mixture model (GMM) algorithm. You can either directly set the hyperparameters or specify multiple values for each hyperparameter. If you specify multiple values for each hyperparameter, the Train Clustering Model VI uses grid search to find the optimal set of hyperparameters. |
| Initialize Clustering Model (K-Means) | Initializes the hyperparameters of the K-Means algorithm. You can either directly set the hyperparameters or specify multiple values for each hyperparameter. If you specify multiple values for each hyperparameter, the Train Clustering Model VI uses grid search to find the optimal set of hyperparameters. |
| Set Clustering Model | Sets properties for a trained clustering model before deployment. |
| Train Clustering Model | Trains a clustering model. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_clusteringmodel_prop.html language=enus -->
## TOPIC 00008: AML Clustering Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_clusteringmodel_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_clusteringmodel_prop.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AML Clustering Properties

Wire the **clustering model info out** output of the [Train Clustering Model](aml_train_clustering_model.html) VI to the **reference** input of a standard Property Node to get an AML Clustering Property Node. You must ensure that **clustering model info in** is unwired. This Property Node has the following properties:

| Property | Access | Data Type | Description |
| --- | --- | --- | --- |
| Hyperparameter Optimization | Read Only |  | Returns the method of optimization to determine the optimal hyperparameter settings. |
| Model Initialized? | Read Only |  | Returns whether the model is initialized. |
| Model Trained? | Read Only |  | Returns whether the model is trained. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_data.html language=enus -->
## TOPIC 00009: Data VIs

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_data.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Data VIs

**Owning Palette:** [Analytics and Machine Learning VIs](../lvaml/aml_pal.html)

**Requires:** Analytics and Machine Learning Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Data VIs to save data for model training or deployment and view data changes from the Feature Manipulation VIs.

| Palette Object | Description |
| --- | --- |
| Load Data (2D Array) | Loads data and labels for training or deployment. |
| Read Data (2D Array) | Reads data and labels. Use this VI to read and view transformed data from the Feature Manipulation VIs. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_dbscan_prop.html language=enus -->
## TOPIC 00010: AML DBSCAN Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_dbscan_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_dbscan_prop.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AML DBSCAN Properties

Wire the **untrained DBSCAN model** output of the [Initialize Clustering Model (DBSCAN)](aml_initialize_clustering_model_dbscan.html) VI to the **reference** input of a standard Property Node to get an AML DBSCAN Property Node. This Property Node has the following properties:

| Property | Access | Data Type | Description |
| --- | --- | --- | --- |
| Class Labels | Read Only |  | Returns the labels of the data. |
| Core Sample Labels | Read Only |  | Returns the label of each core sample. |
| Core Samples | Read Only |  | Returns the core samples from the trained DBSCAN model. |
| Core Sample Indexes | Read Only |  | Returns the index of each core sample from the trained DBSCAN model. |
| Evaluation Metric | Read Only |  | Returns the criterion to evaluate the trained clustering model. |
| Hyperparameters | Read Only |  | If you select the Set Parameters instance of the Initialize Clustering Model (DBSCAN) VI, this property returns the hyperparameters input of the VI. If you select the Search Parameters instance of the Initialize Clustering Model (DBSCAN) VI, this property returns the optimal hyperparameters after the Train Clustering Model VI completes grid search. |
| Hyperparameter Grids | Read Only |  | Returns multiple values for each hyperparameter. |
| Hyperparameter Optimization | Read Only |  | Returns the method of optimization to determine the optimal hyperparameter settings. |
| Model Initialized? | Read Only |  | Returns whether the model is initialized. |
| Model Trained? | Read Only |  | Returns whether the model is trained. |
| Number of Clusters | Read Only |  | Returns the number of clusters. The Initialize Clustering Model (DBSCAN) VI calculates this value. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_deploy_anomaly_detection_model.html language=enus -->
## TOPIC 00011: Deploy Anomaly Detection Model VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_deploy_anomaly_detection_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_deploy_anomaly_detection_model.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Deploy Anomaly Detection Model VI

**Owning Palette:** [Anomaly Detection VIs](../lvaml/aml_anomaly_detection.html)

**Requires:** Analytics and Machine Learning Toolkit

Deploys a trained anomaly detection model and returns the health index of input data.

[Example](#examples)

[IMAGE alt='image' src='deploy_anomaly_detection_model.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | health index returns anomaly values for the input data. For the GMM baseline model, health index contains only one element for the confidence value, which is in the range [0,1]. The closer the confidence value is to 1, the closer the input data is to normal condition. The closer the confidence value is to 0, the closer the input data is to abnormal condition. For the one-class SVM model, each element in health index is the health index value for each instance. Health index values greater than 0 represent the normal condition. Health index values less than 0 represent the abnormal condition. For the PCA baseline model, health index returns both the T2 value and the Q value in the following pattern: T2, Q, T2, Q, …. The greater the health index value is, the closer the input data is to abnormal condition. For the SOM baseline model, each element of health index is the MQE value for each instance. The greater the MQE value is, the closer the input data is to abnormal condition. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Anomaly Detection (Deployment) VI in the labview\examples\AML\Anomaly Detection directory for an example of using the Deploy Anomaly Detection Model VI.

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_deploy_classification_model.html language=enus -->
## TOPIC 00012: Deploy Classification Model VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_deploy_classification_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_deploy_classification_model.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Deploy Classification Model VI

**Owning Palette:** [Classification VIs](../lvaml/aml_classification.html)

**Requires:** Analytics and Machine Learning Toolkit

Deploys a trained classification model and returns predicted labels of input data.

[Example](#examples)

[IMAGE alt='image' src='deploy_classification_model.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | predicted labels returns the predicted labels of the data for deployment. |
|  | predicted probabilities returns the predicted probability for each class. If you specify different weights for the SVM model using weighted c in the Initialize Classification Model (SVM) VI, this VI does not return predicted probabilities. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Classification (Deployment) VI in the labview\examples\AML\Classification directory for an example of using the Deploy Classification Model VI.

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_deploy_clustering_model.html language=enus -->
## TOPIC 00013: Deploy Clustering Model VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_deploy_clustering_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_deploy_clustering_model.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Deploy Clustering Model VI

**Owning Palette:** [Clustering VIs](../lvaml/aml_clustering.html)

**Requires:** Analytics and Machine Learning Toolkit

Deploys a trained model and returns predicted labels of input data.

[Example](#examples)

[IMAGE alt='image' src='deploy_clustering_model.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | predicted labels returns the predicted labels of input data. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Clustering (Deployment) VI in the labview\examples\AML\Clustering directory for an example of using the Deploy Clustering Model VI.

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_deploy_feature_manipulation_model.html language=enus -->
## TOPIC 00014: Deploy Feature Manipulation Model VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_deploy_feature_manipulation_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_deploy_feature_manipulation_model.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Deploy Feature Manipulation Model VI

**Owning Palette:** [Feature Manipulation VIs](../lvaml/aml_feature_manipulation.html)

**Requires:** Analytics and Machine Learning Toolkit

Deploys a trained feature manipulation model on deployment data.

[Examples](#examples)

[IMAGE alt='image' src='deploy_feature_manipulation_model.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | transformed data returns the data after feature manipulation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Deploy Feature Manipulation Model VI:

- Feature Manipulation (Deployment) VI: labview\examples\AML\Feature Manipulation
- Classification (Deployment) VI: labview\examples\AML\Classification
- Clustering (Deployment) VI: labview\examples\AML\Clustering

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_evaluate_classification_model.html language=enus -->
## TOPIC 00015: Evaluate Classification Model VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_evaluate_classification_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_evaluate_classification_model.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Evaluate Classification Model VI

**Owning Palette:** [Classification VIs](../lvaml/aml_classification.html)

**Requires:** Analytics and Machine Learning Toolkit

Evaluates a trained classification model by using new test data with labels.

You must load the new test data by using the Deployment instance of the [Load Data (2D Array)](../lvaml/aml_load_data.html) VI.

[Example](#examples)

[IMAGE alt='image' src='evaluate_classification_model.gif']

|  | model in specifies the information about the entire workflow of the model. |  |  |
| --- | --- | --- | --- |
|  | evaluation configuration specifies the configuration for the evaluation metric. average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |  |  |
|  | average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. |  |  |
| 0 | Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples. |  |  |
| 1 | Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels. |  |  |
| 2 | Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label. |  |  |
| 3 | Binary—Calculates the metric values for the class that positive label specifies. |  |  |
|  | positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |  |  |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |  |  |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |  |  |
|  | confusion matrix returns the confusion matrix from the evaluation result. A confusion matrix describes the performance of a classification model by reporting the number of true positive cases, true negative cases, false positive cases, and false negative cases. Each row of a confusion matrix represents the actual class and each column represents the predicted class. For example, for 100 samples, there are two possible classes: positive and negative. The following table is a confusion matrix for the two classes. —Predicted Class PositiveNegative Actual ClassPositive655 Negative1911 The confusion matrix contains 65 true positive cases, 5 false negative cases, 19 false positive cases, and 11 true negative cases. |  |  |
| — | Predicted Class |  |  |
| Positive | Negative |  |  |
| Actual Class | Positive | 65 | 5 |
| Negative | 19 | 11 |  |
|  | metrics returns metrics from the evaluation result. accuracy returns the accuracy metric value. The following equation defines the accuracy metric: where TP is the number of true positive cases in the data TN is the number of true negative cases in the data P is the number of real positive cases in the data N is the number of real negative cases in the data precision returns the precision metric value. The following equation defines the precision metric: where TP is the number of true positive cases in the data FP is the number of false positive cases in the data recall returns the recall metric value. The following equation defines the recall metric: where TP is the number of true positive cases in the data FN is the number of false negative cases in the data f1 score returns the f1 score metric value. The following equation defines the f1 score metric: where TP is the number of true positive cases in the data FP is the number of false positive cases in the data FN is the number of false negative cases in the data |  |  |
|  | accuracy returns the accuracy metric value. The following equation defines the accuracy metric: where TP is the number of true positive cases in the data TN is the number of true negative cases in the data P is the number of real positive cases in the data N is the number of real negative cases in the data |  |  |
| where |  |  |  |
|  | TP is the number of true positive cases in the data |  |  |
|  | TN is the number of true negative cases in the data |  |  |
|  | P is the number of real positive cases in the data |  |  |
|  | N is the number of real negative cases in the data |  |  |
|  | precision returns the precision metric value. The following equation defines the precision metric: where TP is the number of true positive cases in the data FP is the number of false positive cases in the data |  |  |
| where |  |  |  |
|  | TP is the number of true positive cases in the data |  |  |
|  | FP is the number of false positive cases in the data |  |  |
|  | recall returns the recall metric value. The following equation defines the recall metric: where TP is the number of true positive cases in the data FN is the number of false negative cases in the data |  |  |
| where |  |  |  |
|  | TP is the number of true positive cases in the data |  |  |
|  | FN is the number of false negative cases in the data |  |  |
|  | f1 score returns the f1 score metric value. The following equation defines the f1 score metric: where TP is the number of true positive cases in the data FP is the number of false positive cases in the data FN is the number of false negative cases in the data |  |  |
| where |  |  |  |
|  | TP is the number of true positive cases in the data |  |  |
|  | FP is the number of false positive cases in the data |  |  |
|  | FN is the number of false negative cases in the data |  |  |
|  | error out contains error information. This output provides standard error out functionality. |  |  |

#### Example

Refer to the Classification (Deployment) VI in the labview\examples\AML\Classification directory for an example of using the Evaluate Classification Model VI.

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_evaluate_clustering_model.html language=enus -->
## TOPIC 00016: Evaluate Clustering Model VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_evaluate_clustering_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_evaluate_clustering_model.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Evaluate Clustering Model VI

**Owning Palette:** [Clustering VIs](../lvaml/aml_clustering.html)

**Requires:** Analytics and Machine Learning Toolkit

Evaluates a trained clustering model with training data or new test data.

[Example](#examples)

[IMAGE alt='image' src='evaluate_clustering_model.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | predicted labels specifies the predicted labels of training data or test data. |
|  | evaluation metric specifies the criterion to evaluate the trained clustering model. 0Davies Bouldin Index—Evaluates the clustering model using the Davies Bouldin Index metric. The lower the value of metric, the better the compactness and separation of the clustering model. If you select this metric, you do not need to specify predicted labels.1Dunn Index (default)—Evaluates the clustering model using the Dunn Index metric. The higher the value of metric, the better the compactness and separation of the clustering model. If you select this metric, you do not need to specify predicted labels.2Jaccard Index—Evaluates the clustering model using the Jaccard Index metric. The lower the value of metric, the better the separation of the clustering model. If you select this metric, you must specify predicted labels.3Rand Index—Evaluates the clustering model using the Rand Index metric. The lower the value of metric, the better the separation of the clustering model. If you select this metric, you must specify predicted labels.4AIC—Evaluates the GMM model using the Akaike Information Criterion (AIC) metric. The lower the value of metric, the better the GMM model is. If you select this metric, you do not need to specify predicted labels. This metric applies to the GMM model only.5BIC—Evaluates the GMM model using the Bayesian Information Criterion (BIC) metric. The lower the value of metric, the better the GMM model is. If you select this metric, you do not need to specify predicted labels. This metric applies to the GMM model only. |
| 0 | Davies Bouldin Index—Evaluates the clustering model using the Davies Bouldin Index metric. The lower the value of metric, the better the compactness and separation of the clustering model. If you select this metric, you do not need to specify predicted labels. |
| 1 | Dunn Index (default)—Evaluates the clustering model using the Dunn Index metric. The higher the value of metric, the better the compactness and separation of the clustering model. If you select this metric, you do not need to specify predicted labels. |
| 2 | Jaccard Index—Evaluates the clustering model using the Jaccard Index metric. The lower the value of metric, the better the separation of the clustering model. If you select this metric, you must specify predicted labels. |
| 3 | Rand Index—Evaluates the clustering model using the Rand Index metric. The lower the value of metric, the better the separation of the clustering model. If you select this metric, you must specify predicted labels. |
| 4 | AIC—Evaluates the GMM model using the Akaike Information Criterion (AIC) metric. The lower the value of metric, the better the GMM model is. If you select this metric, you do not need to specify predicted labels. This metric applies to the GMM model only. |
| 5 | BIC—Evaluates the GMM model using the Bayesian Information Criterion (BIC) metric. The lower the value of metric, the better the GMM model is. If you select this metric, you do not need to specify predicted labels. This metric applies to the GMM model only. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | metric returns the metric you selected in evaluation metric. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Clustering (Set Parameters, Training) VI in the labview\examples\AML\Clustering directory for an example of using the Evaluate Clustering Model VI.

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_feature_manipulation.html language=enus -->
## TOPIC 00017: Feature Manipulation VIs

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_feature_manipulation.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_feature_manipulation.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Feature Manipulation VIs

**Owning Palette:** [Analytics and Machine Learning VIs](../lvaml/aml_pal.html)

**Requires:** Analytics and Machine Learning Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Feature Manipulation VIs to train and deploy feature reduction and normalization models.

Feature reduction reduces the dimension of data so that you can apply machine learning algorithms to the training data. Normalization standardizes the range of features for the training data.

| Palette Object | Description |
| --- | --- |
| Deploy Feature Manipulation Model | Deploys a trained feature manipulation model on deployment data. |
| Fisher | Trains a Fisher's linear discriminant model. You can use the Fisher's linear discriminant model to reduce the dimension of training data. As a supervised model, Fisher's linear discriminant requires both healthy data and abnormal data. |
| KPCA | Trains a kernel principal component analysis (KPCA) model. You can use the KPCA model to reduce the dimension of training data. |
| Normalize | Trains a normalization model. You can use the normalization model to normalize training data with Z-Score or Min-Max method. |
| PCA | Trains a principal component analysis (PCA) model. You can use the PCA model to reduce the dimension of training data. |
| Set Feature Manipulation Model | Sets properties for a trained feature manipulation model before deployment. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_fisher.html language=enus -->
## TOPIC 00018: Fisher VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_fisher.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_fisher.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Fisher VI

**Owning Palette:** [Feature Manipulation VIs](../lvaml/aml_feature_manipulation.html)

**Requires:** Analytics and Machine Learning Toolkit

Trains a Fisher's linear discriminant model. You can use the Fisher's linear discriminant model to reduce the dimension of training data. As a supervised model, Fisher's linear discriminant requires both healthy data and abnormal data.

[Example](#examples)

[IMAGE alt='image' src='fisher.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | number of components specifies the number of features after feature selection. The default is 2. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | Fisher model info returns the information of the Fisher's linear discriminant model. Wire Fisher model info to the reference input of a standard Property Node to get an AML Fisher Property Node. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Feature Manipulation (Training) VI in the labview\examples\AML\Feature Manipulation directory for an example of using the Fisher VI.

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_fisher_prop.html language=enus -->
## TOPIC 00019: AML Fisher Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_fisher_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_fisher_prop.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AML Fisher Properties

Wire the **Fisher model info** output of the [Fisher](aml_fisher.html) VI to the **reference** input of a standard Property Node to get an AML Fisher Property Node. This Property Node has the following properties:

| Property | Access | Data Type | Description |
| --- | --- | --- | --- |
| Fisher Distance | Read Only |  | Returns the descending fisher distance and the corresponding feature index. |
| Number of Components | Read Only |  | Returns the number of features after feature selection. |
| Selected Feature Index | Read Only |  | Returns the indexes of selected features. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_gmm_prop.html language=enus -->
## TOPIC 00020: AML GMM Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_gmm_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_gmm_prop.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AML GMM Properties

Wire the **untrained GMM model** output of the [Initialize Clustering Model (GMM)](aml_initialize_clustering_model_gmm.html) VI to the **reference** input of a standard Property Node to get an AML GMM Property Node. This Property Node has the following properties:

| Property | Access | Data Type | Description |
| --- | --- | --- | --- |
| Class Labels | Read Only |  | Returns the labels of the data. |
| Covariance Values | Read Only |  | Returns the covariance values of all Gaussian distributions in the trained GMM model. The array size equals the number of clusters input of the GMM instance of the Set Clustering Model VI. |
| Evaluation Metric | Read Only |  | Returns the criterion to evaluate the trained clustering model. |
| Hyperparameters | Read Only |  | If you select the Set Parameters instance of the Initialize Clustering Model (GMM) VI, this property returns the hyperparameters input of the VI. If you select the Search Parameters instance of the Initialize Clustering Model (GMM) VI, this property returns the optimal hyperparameters after the Train Clustering Model VI completes grid search. |
| Hyperparameter Grids | Read Only |  | Returns multiple values for each hyperparameter. |
| Hyperparameter Optimization | Read Only |  | Returns the method of optimization to determine the optimal hyperparameter settings. |
| Model Initialized? | Read Only |  | Returns whether the model is initialized. |
| Model Trained? | Read Only |  | Returns whether the model is trained. |
| Mean Values | Read Only |  | Returns the mean values of all Gaussian distributions in the GMM model. The number of rows equals the number of clusters input of the Initialize Clustering Model (GMM) VI. |
| Weights | Read Only |  | Returns the weights of all Gaussian distributions in the GMM model. The number of rows equals the number of clusters input of the Initialize Clustering Model (GMM) VI. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_gmmcv_prop.html language=enus -->
## TOPIC 00021: AML GMM-CV Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_gmmcv_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_gmmcv_prop.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AML GMM-CV Properties

Wire the **untrained GMM baseline model** output of the [Initialize Anomaly Detection Model (GMM-CV)](aml_initialize_anomaly_detection_model_gmm_cv.html) VI to the **reference** input of a standard Property Node to get an AML GMM-CV Property Node. This Property Node has the following properties:

| Property | Access | Data Type | Description |
| --- | --- | --- | --- |
| Covariance Values | Read Only |  | Returns the covariance values of all Gaussian distributions in the trained GMM baseline model. The array size equals the number of clusters input of the Set Anomaly Detection Model (GMM) VI. |
| GMM Initial Parameter | Read Only |  | Returns the initial parameters to train the GMM baseline model when you perform batch training. |
| Hyperparameters | Read Only |  | Returns the hyperparameters to train the GMM baseline model. |
| Model Initialized? | Read Only |  | Returns whether the model is initialized. |
| Model Trained? | Read Only |  | Returns whether the model is trained. |
| Mean Values | Read Only |  | Returns the mean values of all Gaussian distributions in the GMM baseline model. The number of rows equals the number of clusters input of the Initialize Anomaly Detection Model (GMM-CV) VI. |
| Weights | Read Only |  | Returns the weights of all Gaussian distributions in the GMM baseline model. The number of rows equals the number of clusters input of the Initialize Anomaly Detection Model (GMM-CV) VI. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_initialize_anomaly_detection_model_gmm_cv.html language=enus -->
## TOPIC 00022: Initialize Anomaly Detection Model (GMM-CV) VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_initialize_anomaly_detection_model_gmm_cv.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_initialize_anomaly_detection_model_gmm_cv.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Initialize Anomaly Detection Model (GMM-CV) VI

**Owning Palette:** [Anomaly Detection VIs](../lvaml/aml_anomaly_detection.html)

**Requires:** Analytics and Machine Learning Toolkit

Initializes the hyperparameters of the Gaussian mixture model (GMM) algorithm.

Use the [Train Anomaly Detection Model](../lvaml/aml_train_anomaly_detection_model.html) VI to train the GMM baseline model with training data. Use the [Deploy Anomaly Detection Model](../lvaml/aml_deploy_anomaly_detection_model.html) VI to deploy the GMM baseline model and calculate the confidence value (CV) of the data for deployment. The Deploy Anomaly Detection Model VI calculates the CV by computing the overlap between the GMM baseline model and the GMM model. The Deploy Anomaly Detection Model VI uses **health index** to return the CV.

You can initialize a GMM model for [batch training](../lvamlconcepts/aml_gettingstarted.html) with this VI when you have a large training data set. To improve the machine learning model quality and the predictive performance, NI recommends that you shuffle the data set before training so each batch has similar distribution.

[Details](#details)  [Examples](#examples)

#### One Shot

[IMAGE alt='image' src='initialize_anomaly_detection_model__gmm-cv.gif']

|  | initial parameters specifies the initial parameters to train the GMM baseline model. auto initialization specifies whether this VI automatically calculates the values in initial parameters using K-Means algorithm. The default is TRUE, which specifies that this VI automatically sets the values in initial parameters using K-Means algorithm. If you do not specify values for the arrays in initial parameters and auto initialization is FALSE, this VI randomly calculates the values in initial parameters. initial mean values specifies the initial mean values of all Gaussian distributions in the GMM baseline model. initial covariance values specifies the initial covariance values of all Gaussian distributions in the GMM baseline model. initial covariance matrix specifies the initial covariance matrix of each Gaussian distribution in the GMM baseline model. initial weights specifies the initial weights of all Gaussian distributions in the GMM baseline model. |
| --- | --- |
|  | auto initialization specifies whether this VI automatically calculates the values in initial parameters using K-Means algorithm. The default is TRUE, which specifies that this VI automatically sets the values in initial parameters using K-Means algorithm. If you do not specify values for the arrays in initial parameters and auto initialization is FALSE, this VI randomly calculates the values in initial parameters. |
|  | initial mean values specifies the initial mean values of all Gaussian distributions in the GMM baseline model. |
|  | initial covariance values specifies the initial covariance values of all Gaussian distributions in the GMM baseline model. initial covariance matrix specifies the initial covariance matrix of each Gaussian distribution in the GMM baseline model. |
|  | initial covariance matrix specifies the initial covariance matrix of each Gaussian distribution in the GMM baseline model. |
|  | initial weights specifies the initial weights of all Gaussian distributions in the GMM baseline model. |
|  | hyperparameters specifies the hyperparameters to train the GMM baseline model. number of clusters specifies the number of Gaussian distributions in the GMM baseline model. The default is 3. regulator specifies the value that this VI adds to the covariance matrix to prevent the covariance matrix from converging to 0. The default is 0.000001. tolerance specifies the tolerance for the stopping criteria. The default is 0.0001. The model fitting stops if the change of maximum likelihood between two successive optimization iterations is lower than tolerance. max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 100. The model fitting stops if the number of optimization iterations reaches max iteration. |
|  | number of clusters specifies the number of Gaussian distributions in the GMM baseline model. The default is 3. |
|  | regulator specifies the value that this VI adds to the covariance matrix to prevent the covariance matrix from converging to 0. The default is 0.000001. |
|  | tolerance specifies the tolerance for the stopping criteria. The default is 0.0001. The model fitting stops if the change of maximum likelihood between two successive optimization iterations is lower than tolerance. |
|  | max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 100. The model fitting stops if the number of optimization iterations reaches max iteration. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | untrained GMM baseline model returns the initialized GMM baseline model for training. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Batch

[IMAGE alt='image' src='initialize_model_gmm-cv_batch.gif']

|  | initial parameters specifies the initial parameters to train the GMM baseline model. auto initialization specifies whether this VI automatically calculates the values in initial parameters using K-Means algorithm. The default is TRUE, which specifies that this VI automatically sets the values in initial parameters using K-Means algorithm. If you do not specify values for the arrays in initial parameters and auto initialization is FALSE, this VI randomly calculates the values in initial parameters. initial mean values specifies the initial mean values of all Gaussian distributions in the GMM baseline model. initial covariance values specifies the initial covariance values of all Gaussian distributions in the GMM baseline model. initial covariance matrix specifies the initial covariance matrix of each Gaussian distribution in the GMM baseline model. initial weights specifies the initial weights of all Gaussian distributions in the GMM baseline model. |
| --- | --- |
|  | auto initialization specifies whether this VI automatically calculates the values in initial parameters using K-Means algorithm. The default is TRUE, which specifies that this VI automatically sets the values in initial parameters using K-Means algorithm. If you do not specify values for the arrays in initial parameters and auto initialization is FALSE, this VI randomly calculates the values in initial parameters. |
|  | initial mean values specifies the initial mean values of all Gaussian distributions in the GMM baseline model. |
|  | initial covariance values specifies the initial covariance values of all Gaussian distributions in the GMM baseline model. initial covariance matrix specifies the initial covariance matrix of each Gaussian distribution in the GMM baseline model. |
|  | initial covariance matrix specifies the initial covariance matrix of each Gaussian distribution in the GMM baseline model. |
|  | initial weights specifies the initial weights of all Gaussian distributions in the GMM baseline model. |
|  | hyperparameters specifies the hyperparameters to train the GMM baseline model. number of clusters specifies the number of Gaussian distributions in the GMM baseline model. The default is 3. For the first batch data, number of clusters must be less than or equal to the number of samples. regulator specifies the value that this VI adds to the covariance matrix to prevent the covariance matrix from converging to 0. The default is 0.000001. |
|  | number of clusters specifies the number of Gaussian distributions in the GMM baseline model. The default is 3. For the first batch data, number of clusters must be less than or equal to the number of samples. |
|  | regulator specifies the value that this VI adds to the covariance matrix to prevent the covariance matrix from converging to 0. The default is 0.000001. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | untrained GMM baseline model returns the initialized GMM baseline model for training. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Initialize Anomaly Detection Model (GMM-CV) Details

The following equation defines the GMM model:

[IMAGE alt='image' src='eq_gmm.gif']

| where |  |
| --- | --- |
|  | K is the number of Gaussian mixture components. Each Gaussian mixture component represents a Gaussian distribution. |
|  | μi and Σi are the mean value and the covariance value of the ith Gaussian mixture component |
|  | αi is the weight of the ith Gaussian mixture component |

#### Examples

Refer to the following VIs for examples of using the Initialize Anomaly Detection Model (GMM-CV) VI:

- Anomaly Detection (Training) VI: labview\examples\AML\Anomaly Detection
- Anomaly Detection (Training) (Batch) VI: labview\examples\AML\Anomaly Detection

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_initialize_anomaly_detection_model_one_class_svm.html language=enus -->
## TOPIC 00023: Initialize Anomaly Detection Model (One-Class SVM) VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_initialize_anomaly_detection_model_one_class_svm.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_initialize_anomaly_detection_model_one_class_svm.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Initialize Anomaly Detection Model (One-Class SVM) VI

**Owning Palette:** [Anomaly Detection VIs](../lvaml/aml_anomaly_detection.html)

**Requires:** Analytics and Machine Learning Toolkit

Initializes the hyperparameters of the one-class support vector machine (SVM) algorithm. This VI uses the nu-SVM algorithm.

Use the one-class SVM model to estimate the boundary of a high-dimensional distribution. The one-class SVM algorithm trains models on data that has only one class.

[Example](#examples)

[IMAGE alt='image' src='initialize_anomaly_detection_model__one-class_svm.gif']

|  | hyperparameters specifies the hyperparameters of the one-class SVM model. nu specifies the nu parameter for the one-class SVM model. The nu parameter is both a lower bound for the number of samples that are support vectors and an upper bound for the number of samples that are on the wrong side of the hyperplane. The default is 0.1. The nu parameter must be in the range [0,1]. For example, if nu is 0.05, the training samples that are wrongly classified are not allowed to take up more than 5 percent of all training samples. Also, at least 5 percent of the training samples are support vectors. kernel settings specifies settings to configure the kernel function. This VI supports the following kernel functions: Kernel functionDefinitionDescription Linear functionx and y are the input sample vectors. Polynomial functionx and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. Radial basis functionx and y are the input sample vectors. Sigmoid functionx and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. type specifies the type of the kernel function. 0Linear (default)—Linear function 1Polynomial—Polynomial function 2RBF—Radial basis function 3Sigmoid—Sigmoid function degree specifies the degree coefficient of the kernel function. The default is 3. gamma specifies the gamma coefficient of the kernel function. The default is 1. coef0 specifies the coef0 coefficient of the kernel function. The default is 0. tolerance specifies the tolerance for the stopping criteria. The default is 0.001. max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 100000. The model fitting stops if the number of optimization iterations reaches max iteration. |  |
| --- | --- | --- |
|  | nu specifies the nu parameter for the one-class SVM model. The nu parameter is both a lower bound for the number of samples that are support vectors and an upper bound for the number of samples that are on the wrong side of the hyperplane. The default is 0.1. The nu parameter must be in the range [0,1]. For example, if nu is 0.05, the training samples that are wrongly classified are not allowed to take up more than 5 percent of all training samples. Also, at least 5 percent of the training samples are support vectors. |  |
|  | kernel settings specifies settings to configure the kernel function. This VI supports the following kernel functions: Kernel functionDefinitionDescription Linear functionx and y are the input sample vectors. Polynomial functionx and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. Radial basis functionx and y are the input sample vectors. Sigmoid functionx and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. type specifies the type of the kernel function. 0Linear (default)—Linear function 1Polynomial—Polynomial function 2RBF—Radial basis function 3Sigmoid—Sigmoid function degree specifies the degree coefficient of the kernel function. The default is 3. gamma specifies the gamma coefficient of the kernel function. The default is 1. coef0 specifies the coef0 coefficient of the kernel function. The default is 0. |  |
| Kernel function | Definition | Description |
| Linear function |  | x and y are the input sample vectors. |
| Polynomial function |  | x and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. |
| Radial basis function |  | x and y are the input sample vectors. |
| Sigmoid function |  | x and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. |
|  | type specifies the type of the kernel function. 0Linear (default)—Linear function 1Polynomial—Polynomial function 2RBF—Radial basis function 3Sigmoid—Sigmoid function |  |
| 0 | Linear (default)—Linear function |  |
| 1 | Polynomial—Polynomial function |  |
| 2 | RBF—Radial basis function |  |
| 3 | Sigmoid—Sigmoid function |  |
|  | degree specifies the degree coefficient of the kernel function. The default is 3. |  |
|  | gamma specifies the gamma coefficient of the kernel function. The default is 1. |  |
|  | coef0 specifies the coef0 coefficient of the kernel function. The default is 0. |  |
|  | tolerance specifies the tolerance for the stopping criteria. The default is 0.001. |  |
|  | max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 100000. The model fitting stops if the number of optimization iterations reaches max iteration. |  |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |  |
|  | untrained one-class SVM model returns the initialized one-class SVM model for training. |  |
|  | error out contains error information. This output provides standard error out functionality. |  |

#### Example

Refer to the Anomaly Detection (Training) VI in the labview\examples\AML\Anomaly Detection directory for an example of using the Initialize Anomaly Detection Model (One-Class SVM) VI.

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_initialize_anomaly_detection_model_pca_t2q.html language=enus -->
## TOPIC 00024: Initialize Anomaly Detection Model (PCA T2Q) VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_initialize_anomaly_detection_model_pca_t2q.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_initialize_anomaly_detection_model_pca_t2q.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Initialize Anomaly Detection Model (PCA T2Q) VI

**Owning Palette:** [Anomaly Detection VIs](../lvaml/aml_anomaly_detection.html)

**Requires:** Analytics and Machine Learning Toolkit

Initializes the hyperparameters of the principal component analysis (PCA) algorithm.

The T2-statistic measures the variation in each sample and indicates the distance of each sample from the center of the PCA model. The Q-statistic indicates how well each sample conforms to the PCA model by measuring the distance that a data point falls from the PCA model.

The [Deploy Anomaly Detection Model](../lvaml/aml_deploy_anomaly_detection_model.html) VI uses **health index** to return the T2 value and the Q value.

You can initialize a PCA model for [batch training](../lvamlconcepts/aml_gettingstarted.html) with this VI when you have a large training data set.

[Examples](#examples)

#### One Shot

[IMAGE alt='image' src='initialize_anomaly_detection_model__pca_t2q.gif']

|  | hyperparameters specifies the hyperparameters of the PCA baseline model. PCA settings specifies the method and value for this VI to calculate the number of principal components. criteria specifies the method for this VI to calculate the number of principal components. 0number of components (default)—Directly specifies the number of principal components.1ratio of variance—Specifies the ratio of variance for this VI to calculate the number of principal components. number of components specifies the number of principal components. This input is valid only if criteria is number of components. ratio of variance specifies the ratio of the variance in principal components to the total variance. This VI automatically calculates the number of components. The default is 0.95. This input is valid only if criteria is ratio of variance. confidence level specifies the confidence level for calculating the suggested threshold of T2 and Q. You can use the suggested threshold to detect anomalies. The default is 0.95. You can access the suggested threshold by the AML PCA T2Q Property Node. |
| --- | --- |
|  | PCA settings specifies the method and value for this VI to calculate the number of principal components. criteria specifies the method for this VI to calculate the number of principal components. 0number of components (default)—Directly specifies the number of principal components.1ratio of variance—Specifies the ratio of variance for this VI to calculate the number of principal components. number of components specifies the number of principal components. This input is valid only if criteria is number of components. ratio of variance specifies the ratio of the variance in principal components to the total variance. This VI automatically calculates the number of components. The default is 0.95. This input is valid only if criteria is ratio of variance. |
|  | criteria specifies the method for this VI to calculate the number of principal components. 0number of components (default)—Directly specifies the number of principal components.1ratio of variance—Specifies the ratio of variance for this VI to calculate the number of principal components. |
| 0 | number of components (default)—Directly specifies the number of principal components. |
| 1 | ratio of variance—Specifies the ratio of variance for this VI to calculate the number of principal components. |
|  | number of components specifies the number of principal components. This input is valid only if criteria is number of components. |
|  | ratio of variance specifies the ratio of the variance in principal components to the total variance. This VI automatically calculates the number of components. The default is 0.95. This input is valid only if criteria is ratio of variance. |
|  | confidence level specifies the confidence level for calculating the suggested threshold of T2 and Q. You can use the suggested threshold to detect anomalies. The default is 0.95. You can access the suggested threshold by the AML PCA T2Q Property Node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | untrained PCA baseline model returns the initialized PCA baseline model for training. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Batch

[IMAGE alt='image' src='initialize_model_pca_t2q_batch.gif']

|  | hyperparameters specifies the hyperparameters of the PCA baseline model. number of components specifies the number of principal components in the batch. The default is 2. number of components must be reasonable to avoid too much memory usage for a single batch. For the first batch data, number of components must be less than or equal to the number of rows in the training data. Starting from the second batch data, number of components can be 1 or any number that fits in the computation capacity. confidence level specifies the confidence level for calculating the suggested threshold of T2 and Q. You can use the suggested threshold to detect anomalies. The default is 0.95. You can access the suggested threshold by the AML PCA T2Q Property Node. |
| --- | --- |
|  | number of components specifies the number of principal components in the batch. The default is 2. number of components must be reasonable to avoid too much memory usage for a single batch. For the first batch data, number of components must be less than or equal to the number of rows in the training data. Starting from the second batch data, number of components can be 1 or any number that fits in the computation capacity. |
|  | confidence level specifies the confidence level for calculating the suggested threshold of T2 and Q. You can use the suggested threshold to detect anomalies. The default is 0.95. You can access the suggested threshold by the AML PCA T2Q Property Node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | untrained PCA baseline model returns the initialized PCA baseline model for training. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Initialize Anomaly Detection Model (PCA T2Q) VI:

- Anomaly Detection (Training) VI: labview\examples\AML\Anomaly Detection
- Anomaly Detection (Training) (Batch) VI: labview\examples\AML\Anomaly Detection

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_initialize_anomaly_detection_model_som_mqe.html language=enus -->
## TOPIC 00025: Initialize Anomaly Detection Model (SOM-MQE) VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_initialize_anomaly_detection_model_som_mqe.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_initialize_anomaly_detection_model_som_mqe.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Initialize Anomaly Detection Model (SOM-MQE) VI

**Owning Palette:** [Anomaly Detection VIs](../lvaml/aml_anomaly_detection.html)

**Requires:** Analytics and Machine Learning Toolkit

Initializes the hyperparameters of the self-organizing map (SOM) algorithm.

The minimum quantization error (MQE) is the distance between the input data and the best matching unit.

The [Deploy Anomaly Detection Model](../lvaml/aml_deploy_anomaly_detection_model.html) VI uses **health index** to return the MQE value.

You can initialize a SOM model for [batch training](../lvamlconcepts/aml_gettingstarted.html) with this VI when you have a large training data set. To improve the machine learning model quality and the predictive performance, NI recommends that you shuffle the data set before training so each batch has similar distribution.

[Examples](#examples)

#### One Shot

[IMAGE alt='image' src='initialize_anomaly_detection_model__som-mqe.gif']

|  | initial parameters specifies the initial parameters of the SOM baseline model. map structure settings specifies settings to configure the map structure. auto set? specifies whether this VI automatically configures the map structure. The default is TRUE, which specifies that this VI automatically configures the map structure. map structure specifies settings for the map structure. This input is valid only if auto set? is FALSE. row specifies the number of rows of the SOM baseline model. The default is 7. column specifies the number of columns of the SOM baseline model. The default is 7. lattice type specifies the lattice type of the SOM baseline model. 0rectangular (default) 1hexagonal The following figure shows the rectangular lattice: The following figure shows the hexagonal lattice: initial map vectors specifies the initial map vectors. The number of columns is the number of features. The number of rows is the area of map structure and equals row * column. This input is valid only if auto set? is FALSE. If this input is empty, this VI randomly generates the initial map vectors. If the number of rows of initial map vectors is greater than row * column, this VI deletes extra rows from initial map vectors. If the number of rows of initial map vectors is less than row * column, this VI adds new rows with randomly generated elements to initial map vectors so that the number of rows of initial map vectors equals row * column. |
| --- | --- |
|  | map structure settings specifies settings to configure the map structure. auto set? specifies whether this VI automatically configures the map structure. The default is TRUE, which specifies that this VI automatically configures the map structure. map structure specifies settings for the map structure. This input is valid only if auto set? is FALSE. row specifies the number of rows of the SOM baseline model. The default is 7. column specifies the number of columns of the SOM baseline model. The default is 7. lattice type specifies the lattice type of the SOM baseline model. 0rectangular (default) 1hexagonal The following figure shows the rectangular lattice: The following figure shows the hexagonal lattice: |
|  | auto set? specifies whether this VI automatically configures the map structure. The default is TRUE, which specifies that this VI automatically configures the map structure. |
|  | map structure specifies settings for the map structure. This input is valid only if auto set? is FALSE. row specifies the number of rows of the SOM baseline model. The default is 7. column specifies the number of columns of the SOM baseline model. The default is 7. lattice type specifies the lattice type of the SOM baseline model. 0rectangular (default) 1hexagonal The following figure shows the rectangular lattice: The following figure shows the hexagonal lattice: |
|  | row specifies the number of rows of the SOM baseline model. The default is 7. |
|  | column specifies the number of columns of the SOM baseline model. The default is 7. |
|  | lattice type specifies the lattice type of the SOM baseline model. 0rectangular (default) 1hexagonal The following figure shows the rectangular lattice: The following figure shows the hexagonal lattice: |
| 0 | rectangular (default) |
| 1 | hexagonal |
|  | initial map vectors specifies the initial map vectors. The number of columns is the number of features. The number of rows is the area of map structure and equals row * column. This input is valid only if auto set? is FALSE. If this input is empty, this VI randomly generates the initial map vectors. If the number of rows of initial map vectors is greater than row * column, this VI deletes extra rows from initial map vectors. If the number of rows of initial map vectors is less than row * column, this VI adds new rows with randomly generated elements to initial map vectors so that the number of rows of initial map vectors equals row * column. |
|  | hyperparameters specifies the hyperparameters of the SOM baseline model. initial radius specifies the initial radius for finding the neighbor neurons. The default is 3. initial learning rate specifies the initial learning rate for training the map vectors. The default is 0.1. max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 20. The model fitting stops if the number of optimization iterations reaches max iteration. confidence level specifies the confidence level for calculating the suggested threshold. The default is 0.95. For example, if confidence value is 0.95, this VI calculates the suggested threshold that allows 5 percent of the training samples to have health index exceeding the threshold and regarded as anomalies. You can access the suggested threshold using the AML SOM-MQE Property Node. |
|  | initial radius specifies the initial radius for finding the neighbor neurons. The default is 3. |
|  | initial learning rate specifies the initial learning rate for training the map vectors. The default is 0.1. |
|  | max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 20. The model fitting stops if the number of optimization iterations reaches max iteration. |
|  | confidence level specifies the confidence level for calculating the suggested threshold. The default is 0.95. For example, if confidence value is 0.95, this VI calculates the suggested threshold that allows 5 percent of the training samples to have health index exceeding the threshold and regarded as anomalies. You can access the suggested threshold using the AML SOM-MQE Property Node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | untrained SOM baseline model returns the initialized SOM baseline model for training. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Batch

[IMAGE alt='image' src='initialize_model_som_mqe_batch.gif']

|  | initial parameters specifies the initial parameters of the SOM baseline model. map structure specifies settings for the map structure. row specifies the number of rows of the SOM baseline model. The default is 15. column specifies the number of columns of the SOM baseline model. The default is 10. lattice type specifies the lattice type of the SOM baseline model. 0rectangular (default) 1hexagonal The following figure shows the rectangular lattice: The following figure shows the hexagonal lattice: initial map vectors specifies the initial map vectors. The number of columns is the number of features. The number of rows is the area of map structure and equals row * column. This input is valid only if auto set? is FALSE. If this input is empty, this VI randomly generates the initial map vectors. If the number of rows of initial map vectors is greater than row * column, this VI deletes extra rows from initial map vectors. If the number of rows of initial map vectors is less than row * column, this VI adds new rows with randomly generated elements to initial map vectors so that the number of rows of initial map vectors equals row * column. |
| --- | --- |
|  | map structure specifies settings for the map structure. row specifies the number of rows of the SOM baseline model. The default is 15. column specifies the number of columns of the SOM baseline model. The default is 10. lattice type specifies the lattice type of the SOM baseline model. 0rectangular (default) 1hexagonal The following figure shows the rectangular lattice: The following figure shows the hexagonal lattice: |
|  | row specifies the number of rows of the SOM baseline model. The default is 15. |
|  | column specifies the number of columns of the SOM baseline model. The default is 10. |
|  | lattice type specifies the lattice type of the SOM baseline model. 0rectangular (default) 1hexagonal The following figure shows the rectangular lattice: The following figure shows the hexagonal lattice: |
| 0 | rectangular (default) |
| 1 | hexagonal |
|  | initial map vectors specifies the initial map vectors. The number of columns is the number of features. The number of rows is the area of map structure and equals row * column. This input is valid only if auto set? is FALSE. If this input is empty, this VI randomly generates the initial map vectors. If the number of rows of initial map vectors is greater than row * column, this VI deletes extra rows from initial map vectors. If the number of rows of initial map vectors is less than row * column, this VI adds new rows with randomly generated elements to initial map vectors so that the number of rows of initial map vectors equals row * column. |
|  | hyperparameters specifies the hyperparameters of the SOM baseline model. initial radius specifies the initial radius for finding the neighbor neurons. The default is 3. initial learning rate specifies the initial learning rate for training the map vectors. The default is 0.1. max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 20. The model fitting stops if the number of optimization iterations reaches max iteration. confidence level specifies the confidence level for calculating the suggested threshold. The default is 0.95. For example, if confidence value is 0.95, this VI calculates the suggested threshold that allows 5 percent of the training samples to have health index exceeding the threshold and regarded as anomalies. You can access the suggested threshold using the AML SOM-MQE Property Node. |
|  | initial radius specifies the initial radius for finding the neighbor neurons. The default is 3. |
|  | initial learning rate specifies the initial learning rate for training the map vectors. The default is 0.1. |
|  | max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 20. The model fitting stops if the number of optimization iterations reaches max iteration. |
|  | confidence level specifies the confidence level for calculating the suggested threshold. The default is 0.95. For example, if confidence value is 0.95, this VI calculates the suggested threshold that allows 5 percent of the training samples to have health index exceeding the threshold and regarded as anomalies. You can access the suggested threshold using the AML SOM-MQE Property Node. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | untrained SOM baseline model returns the initialized SOM baseline model for training. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Initialize Anomaly Detection Model (SOM-MQE) VI:

- Anomaly Detection (Training) VI: labview\examples\AML\Anomaly Detection
- Anomaly Detection (Training) (Batch) VI: labview\examples\AML\Anomaly Detection

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_initialize_classification_model_lr.html language=enus -->
## TOPIC 00026: Initialize Classification Model (LR) VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_initialize_classification_model_lr.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_initialize_classification_model_lr.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Initialize Classification Model (LR) VI

**Owning Palette:** [Classification VIs](../lvaml/aml_classification.html)

**Requires:** Analytics and Machine Learning Toolkit

Initializes the hyperparameters of the logistic regression (LR) algorithm. You can either set the hyperparameters or specify multiple values for each hyperparameter. If you specify multiple values for each hyperparameter, the [Train Classification Model](../lvaml/aml_train_classification_model.html) VI uses grid search to find the optimal set of hyperparameters.

[Details](#details)  [Examples](#examples)

#### Set Parameters

[IMAGE alt='image' src='initialize_classification_model__lr_set.gif']

|  | hyperparameters specifies the hyperparameters of the logistic regression model. tolerance specifies the tolerance for the stopping criteria. The default is 0.0001. The model fitting stops if the change of training error between two successive optimization iterations is lower than tolerance. max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 1000. The model fitting stops if the number of optimization iterations reaches max iteration. |
| --- | --- |
|  | tolerance specifies the tolerance for the stopping criteria. The default is 0.0001. The model fitting stops if the change of training error between two successive optimization iterations is lower than tolerance. |
|  | max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 1000. The model fitting stops if the number of optimization iterations reaches max iteration. |
|  | cross validation configuration specifies settings for cross validation. enable? specifies whether this VI enables cross validation in model training. The default is FALSE, which specifies that this VI disables cross validation in model training. If enable? is TRUE, the Train Classification Model VI can return confusion matrix and metrics. number of folds specifies the number of sections that this VI divides the training data into. The default is 3. One section is test data, and the remaining sections are training data. The Evaluate Classification Model VI repeats the cross-validation process for n times, where n equals number of folds. metric configuration specifies the configuration for the evaluation metric in cross validation. average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |
|  | enable? specifies whether this VI enables cross validation in model training. The default is FALSE, which specifies that this VI disables cross validation in model training. If enable? is TRUE, the Train Classification Model VI can return confusion matrix and metrics. |
|  | number of folds specifies the number of sections that this VI divides the training data into. The default is 3. One section is test data, and the remaining sections are training data. The Evaluate Classification Model VI repeats the cross-validation process for n times, where n equals number of folds. |
|  | metric configuration specifies the configuration for the evaluation metric in cross validation. average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |
|  | average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. |
| 0 | Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples. |
| 1 | Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels. |
| 2 | Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label. |
| 3 | Binary—Calculates the metric values for the class that positive label specifies. |
|  | positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | untrained logistic regression model returns the initialized logistic regression model for training. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Search Parameters

[IMAGE alt='image' src='initialize_classification_model__lr_search.gif']

|  | hyperparameter grids specifies multiple values for each hyperparameter of the logistic regression model. tolerance specifies the tolerance for the stopping criteria. The model fitting stops if the change of training error between two successive optimization iterations is lower than tolerance. max iteration specifies the maximum number of optimization iterations for the stopping criteria. The model fitting stops if the number of optimization iterations reaches max iteration. |
| --- | --- |
|  | tolerance specifies the tolerance for the stopping criteria. The model fitting stops if the change of training error between two successive optimization iterations is lower than tolerance. |
|  | max iteration specifies the maximum number of optimization iterations for the stopping criteria. The model fitting stops if the number of optimization iterations reaches max iteration. |
|  | hyperparameter optimization specifies the method of optimization to determine the optimal hyperparameter settings. hyperparameter search method specifies the method to search for the optimal set of hyperparameters. 0Exhaustive search (default)—Tests all possible hyperparameter combinations in the training process. This method is reliable but time-consuming.1Random search—Tests a random subset of the hyperparameter combinations in the training process. This method is faster. number of searchings specifies the number of hyperparameter combinations that this VI selects to train the model. The default is 1. This input is valid only if hyperparameter search method is Random search. evaluation metric specifies the metric to evaluate the trained model with different hyperparameter combinations. The Train Classification Model VI finds the optimal hyperparameter set based on evaluation metric. 0Accuracy1Precision2Recall3F1 score |
|  | hyperparameter search method specifies the method to search for the optimal set of hyperparameters. 0Exhaustive search (default)—Tests all possible hyperparameter combinations in the training process. This method is reliable but time-consuming.1Random search—Tests a random subset of the hyperparameter combinations in the training process. This method is faster. |
| 0 | Exhaustive search (default)—Tests all possible hyperparameter combinations in the training process. This method is reliable but time-consuming. |
| 1 | Random search—Tests a random subset of the hyperparameter combinations in the training process. This method is faster. |
|  | number of searchings specifies the number of hyperparameter combinations that this VI selects to train the model. The default is 1. This input is valid only if hyperparameter search method is Random search. |
|  | evaluation metric specifies the metric to evaluate the trained model with different hyperparameter combinations. The Train Classification Model VI finds the optimal hyperparameter set based on evaluation metric. 0Accuracy1Precision2Recall3F1 score |
| 0 | Accuracy |
| 1 | Precision |
| 2 | Recall |
| 3 | F1 score |
|  | cross validation configuration specifies settings for cross validation. number of folds specifies the number of sections that this VI divides the training data into. The default is 3. One section is test data, and the remaining sections are training data. The Evaluate Classification Model VI repeats the cross-validation process for n times, where n equals number of folds. metric configuration specifies the configuration for the evaluation metric in cross validation. average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |
|  | number of folds specifies the number of sections that this VI divides the training data into. The default is 3. One section is test data, and the remaining sections are training data. The Evaluate Classification Model VI repeats the cross-validation process for n times, where n equals number of folds. |
|  | metric configuration specifies the configuration for the evaluation metric in cross validation. average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |
|  | average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. |
| 0 | Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples. |
| 1 | Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels. |
| 2 | Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label. |
| 3 | Binary—Calculates the metric values for the class that positive label specifies. |
|  | positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | untrained logistic regression model returns the initialized logistic regression model for training. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Initialize Classification Model (LR) Details

[IMAGE alt='image' src='eq_lr.gif']

| where |  |
| --- | --- |
|  | x is the input with k + 1 dimensions. x0 is always 1. |
|  | y is the output with a binary value 0 or 1 |
|  | β is the weight vector with k + 1 dimensions |
|  | P (y = 1\|x) is the probability of y = 1 given a known instance of x |

#### Examples

Refer to the following VIs for examples of using the Initialize Classification Model (LR) VI:

- Classification (Set Parameters, Training) VI: labview\examples\AML\Classification
- Classification (Search Parameters, Training) VI: labview\examples\AML\Classification

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_initialize_classification_model_nn.html language=enus -->
## TOPIC 00027: Initialize Classification Model (NN) VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_initialize_classification_model_nn.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_initialize_classification_model_nn.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Initialize Classification Model (NN) VI

**Owning Palette:** [Classification VIs](../lvaml/aml_classification.html)

**Requires:** Analytics and Machine Learning Toolkit

Initializes the hyperparameters of the neural network (NN) algorithm. You can either directly set the hyperparameters or specify multiple values for each hyperparameter. If you specify multiple values for each hyperparameter, the [Train Classification Model](../lvaml/aml_train_classification_model.html) VI uses grid search to find the optimal set of hyperparameters. This VI supports single hidden layers only.

[Examples](#examples)

#### Set Parameters

[IMAGE alt='image' src='initialize_classification_model__nn_set.gif']

|  | hyperparameters specifies the hyperparameters of the neural network model. number of hidden neurons specifies the number of neurons in the hidden layer. The default is 5. hidden layer type specifies the activation function type in the neurons of the hidden layer. This VI supports the following activation functions for the hidden layer: Function typeDefinitionDescription Sigmoid functionx is the activation value of the hidden neuron. Tanh functionx is the activation value of the hidden neuron. Rectified linear unit functionx is the activation value of the hidden neuron. 0Sigmoid (default)—Sigmoid function1Tanh—Tanh function2ReLU—Rectified linear unit function output layer type specifies the activation function type in the neurons of the output layer. This VI supports the following activation functions for the output layer: Function typeDefinitionDescription Sigmoid functionx is the activation value of the output neuron. Softmax functionx is the activation value of the output neuron and n is the number of classes. 0Sigmoid (default)—Sigmoid function1Softmax—Softmax function cost function type specifies the type of the cost function. cost function type is always Cross-entropy if output layer type is Softmax. This VI supports the following cost functions: Function typeDefinitionDescription Quadratic functiont is the target value, y is the output value, and l is the number of training samples. Cross-entropy functiont is the target value, y is the output value, l is the number of training samples, and n is the number of classes. 0Quadratic (default)—Quadratic function1Cross-entropy—Cross-entropy function tolerance specifies the tolerance for the stopping criteria. The default is 0.0001. The model fitting stops if the change of training error between two successive optimization iterations is lower than tolerance. max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 1000. The model fitting stops if the number of optimization iterations reaches max iteration. |  |
| --- | --- | --- |
|  | number of hidden neurons specifies the number of neurons in the hidden layer. The default is 5. |  |
|  | hidden layer type specifies the activation function type in the neurons of the hidden layer. This VI supports the following activation functions for the hidden layer: Function typeDefinitionDescription Sigmoid functionx is the activation value of the hidden neuron. Tanh functionx is the activation value of the hidden neuron. Rectified linear unit functionx is the activation value of the hidden neuron. 0Sigmoid (default)—Sigmoid function1Tanh—Tanh function2ReLU—Rectified linear unit function |  |
| Function type | Definition | Description |
| Sigmoid function |  | x is the activation value of the hidden neuron. |
| Tanh function |  | x is the activation value of the hidden neuron. |
| Rectified linear unit function |  | x is the activation value of the hidden neuron. |
| 0 | Sigmoid (default)—Sigmoid function |  |
| 1 | Tanh—Tanh function |  |
| 2 | ReLU—Rectified linear unit function |  |
|  | output layer type specifies the activation function type in the neurons of the output layer. This VI supports the following activation functions for the output layer: Function typeDefinitionDescription Sigmoid functionx is the activation value of the output neuron. Softmax functionx is the activation value of the output neuron and n is the number of classes. 0Sigmoid (default)—Sigmoid function1Softmax—Softmax function |  |
| Function type | Definition | Description |
| Sigmoid function |  | x is the activation value of the output neuron. |
| Softmax function |  | x is the activation value of the output neuron and n is the number of classes. |
| 0 | Sigmoid (default)—Sigmoid function |  |
| 1 | Softmax—Softmax function |  |
|  | cost function type specifies the type of the cost function. cost function type is always Cross-entropy if output layer type is Softmax. This VI supports the following cost functions: Function typeDefinitionDescription Quadratic functiont is the target value, y is the output value, and l is the number of training samples. Cross-entropy functiont is the target value, y is the output value, l is the number of training samples, and n is the number of classes. 0Quadratic (default)—Quadratic function1Cross-entropy—Cross-entropy function |  |
| Function type | Definition | Description |
| Quadratic function |  | t is the target value, y is the output value, and l is the number of training samples. |
| Cross-entropy function |  | t is the target value, y is the output value, l is the number of training samples, and n is the number of classes. |
| 0 | Quadratic (default)—Quadratic function |  |
| 1 | Cross-entropy—Cross-entropy function |  |
|  | tolerance specifies the tolerance for the stopping criteria. The default is 0.0001. The model fitting stops if the change of training error between two successive optimization iterations is lower than tolerance. |  |
|  | max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 1000. The model fitting stops if the number of optimization iterations reaches max iteration. |  |
|  | cross validation configuration specifies settings for cross validation. enable? specifies whether this VI enables cross validation in model training. The default is FALSE, which specifies that this VI disables cross validation in model training. If enable? is TRUE, the Train Classification Model VI can return confusion matrix and metrics. number of folds specifies the number of sections that this VI divides the training data into. The default is 3. One section is test data, and the remaining sections are training data. The Evaluate Classification Model VI repeats the cross-validation process for n times, where n equals number of folds. metric configuration specifies the configuration for the evaluation metric in cross validation. average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |  |
|  | enable? specifies whether this VI enables cross validation in model training. The default is FALSE, which specifies that this VI disables cross validation in model training. If enable? is TRUE, the Train Classification Model VI can return confusion matrix and metrics. |  |
|  | number of folds specifies the number of sections that this VI divides the training data into. The default is 3. One section is test data, and the remaining sections are training data. The Evaluate Classification Model VI repeats the cross-validation process for n times, where n equals number of folds. |  |
|  | metric configuration specifies the configuration for the evaluation metric in cross validation. average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |  |
|  | average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. |  |
| 0 | Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples. |  |
| 1 | Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels. |  |
| 2 | Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label. |  |
| 3 | Binary—Calculates the metric values for the class that positive label specifies. |  |
|  | positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |  |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |  |
|  | untrained neural network model returns the initialized neural network model for training. |  |
|  | error out contains error information. This output provides standard error out functionality. |  |

#### Search Parameters

[IMAGE alt='image' src='initialize_classification_model__nn_search.gif']

|  | hyperparameter grids specifies multiple values for each hyperparameter of the neural network model. number of hidden neurons specifies the number of neurons in the hidden layer. hidden layer type specifies the activation function type in the neurons of the hidden layer. This VI supports the following activation functions for the hidden layer: Function typeDefinitionDescription Sigmoid functionx is the activation value of the hidden neuron. Tanh functionx is the activation value of the hidden neuron. Rectified linear unit functionx is the activation value of the hidden neuron. 0Sigmoid—Sigmoid function1Tanh—Tanh function2ReLU—Rectified linear unit function output layer type specifies the activation function type in the neurons of the output layer. This VI supports the following activation functions for the output layer: Function typeDefinitionDescription Sigmoid functionx is the activation value of the output neuron. Softmax functionx is the activation value of the output neuron and n is the number of classes. 0Sigmoid—Sigmoid function1Softmax—Softmax function cost function type specifies the type of the cost function. cost function type is always Cross-entropy if output layer type is Softmax. This VI supports the following cost functions: Function typeDefinitionDescription Quadratic functiont is the target value, y is the output value, and l is the number of training samples. Cross-entropy functiont is the target value, y is the output value, l is the number of samples of training samples, and n is the number of classes. 0Quadratic—Quadratic function1Cross-entropy—Cross-entropy function tolerance specifies the tolerance for the stopping criteria. The model fitting stops if the change of training error between two successive optimization iterations is lower than tolerance. max iteration specifies the maximum number of optimization iterations for the stopping criteria. The model fitting stops if the number of optimization iterations reaches max iteration. |  |
| --- | --- | --- |
|  | number of hidden neurons specifies the number of neurons in the hidden layer. |  |
|  | hidden layer type specifies the activation function type in the neurons of the hidden layer. This VI supports the following activation functions for the hidden layer: Function typeDefinitionDescription Sigmoid functionx is the activation value of the hidden neuron. Tanh functionx is the activation value of the hidden neuron. Rectified linear unit functionx is the activation value of the hidden neuron. 0Sigmoid—Sigmoid function1Tanh—Tanh function2ReLU—Rectified linear unit function |  |
| Function type | Definition | Description |
| Sigmoid function |  | x is the activation value of the hidden neuron. |
| Tanh function |  | x is the activation value of the hidden neuron. |
| Rectified linear unit function |  | x is the activation value of the hidden neuron. |
| 0 | Sigmoid—Sigmoid function |  |
| 1 | Tanh—Tanh function |  |
| 2 | ReLU—Rectified linear unit function |  |
|  | output layer type specifies the activation function type in the neurons of the output layer. This VI supports the following activation functions for the output layer: Function typeDefinitionDescription Sigmoid functionx is the activation value of the output neuron. Softmax functionx is the activation value of the output neuron and n is the number of classes. 0Sigmoid—Sigmoid function1Softmax—Softmax function |  |
| Function type | Definition | Description |
| Sigmoid function |  | x is the activation value of the output neuron. |
| Softmax function |  | x is the activation value of the output neuron and n is the number of classes. |
| 0 | Sigmoid—Sigmoid function |  |
| 1 | Softmax—Softmax function |  |
|  | cost function type specifies the type of the cost function. cost function type is always Cross-entropy if output layer type is Softmax. This VI supports the following cost functions: Function typeDefinitionDescription Quadratic functiont is the target value, y is the output value, and l is the number of training samples. Cross-entropy functiont is the target value, y is the output value, l is the number of samples of training samples, and n is the number of classes. 0Quadratic—Quadratic function1Cross-entropy—Cross-entropy function |  |
| Function type | Definition | Description |
| Quadratic function |  | t is the target value, y is the output value, and l is the number of training samples. |
| Cross-entropy function |  | t is the target value, y is the output value, l is the number of samples of training samples, and n is the number of classes. |
| 0 | Quadratic—Quadratic function |  |
| 1 | Cross-entropy—Cross-entropy function |  |
|  | tolerance specifies the tolerance for the stopping criteria. The model fitting stops if the change of training error between two successive optimization iterations is lower than tolerance. |  |
|  | max iteration specifies the maximum number of optimization iterations for the stopping criteria. The model fitting stops if the number of optimization iterations reaches max iteration. |  |
|  | hyperparameter optimization specifies the method of optimization to determine the optimal hyperparameter settings. hyperparameter search method specifies the method to search for the optimal set of hyperparameters. 0Exhaustive search (default)—Tests all possible hyperparameter combinations in the training process. This method is reliable but time-consuming.1Random search—Tests a random subset of the hyperparameter combinations in the training process. This method is faster. number of searchings specifies the number of hyperparameter combinations that this VI selects to train the model. The default is 1. This input is valid only if hyperparameter search method is Random search. evaluation metric specifies the metric to evaluate the trained model with different hyperparameter combinations. The Train Classification Model VI finds the optimal hyperparameter set based on evaluation metric. 0Accuracy1Precision2Recall3F1 score |  |
|  | hyperparameter search method specifies the method to search for the optimal set of hyperparameters. 0Exhaustive search (default)—Tests all possible hyperparameter combinations in the training process. This method is reliable but time-consuming.1Random search—Tests a random subset of the hyperparameter combinations in the training process. This method is faster. |  |
| 0 | Exhaustive search (default)—Tests all possible hyperparameter combinations in the training process. This method is reliable but time-consuming. |  |
| 1 | Random search—Tests a random subset of the hyperparameter combinations in the training process. This method is faster. |  |
|  | number of searchings specifies the number of hyperparameter combinations that this VI selects to train the model. The default is 1. This input is valid only if hyperparameter search method is Random search. |  |
|  | evaluation metric specifies the metric to evaluate the trained model with different hyperparameter combinations. The Train Classification Model VI finds the optimal hyperparameter set based on evaluation metric. 0Accuracy1Precision2Recall3F1 score |  |
| 0 | Accuracy |  |
| 1 | Precision |  |
| 2 | Recall |  |
| 3 | F1 score |  |
|  | cross validation configuration specifies settings for cross validation. number of folds specifies the number of sections that this VI divides the training data into. The default is 3. One section is test data, and the remaining sections are training data. The Evaluate Classification Model VI repeats the cross-validation process for n times, where n equals number of folds. metric configuration specifies the configuration for the evaluation metric in cross validation. average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |  |
|  | number of folds specifies the number of sections that this VI divides the training data into. The default is 3. One section is test data, and the remaining sections are training data. The Evaluate Classification Model VI repeats the cross-validation process for n times, where n equals number of folds. |  |
|  | metric configuration specifies the configuration for the evaluation metric in cross validation. average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |  |
|  | average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. |  |
| 0 | Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples. |  |
| 1 | Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels. |  |
| 2 | Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label. |  |
| 3 | Binary—Calculates the metric values for the class that positive label specifies. |  |
|  | positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |  |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |  |
|  | untrained neural network model returns the initialized neural network model for training. |  |
|  | error out contains error information. This output provides standard error out functionality. |  |

#### Examples

Refer to the following VIs for examples of using the Initialize Classification Model (NN) VI:

- Classification (Set Parameters, Training) VI: labview\examples\AML\Classification
- Classification (Search Parameters, Training) VI: labview\examples\AML\Classification

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_initialize_classification_model_svm.html language=enus -->
## TOPIC 00028: Initialize Classification Model (SVM) VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_initialize_classification_model_svm.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_initialize_classification_model_svm.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Initialize Classification Model (SVM) VI

**Owning Palette:** [Classification VIs](../lvaml/aml_classification.html)

**Requires:** Analytics and Machine Learning Toolkit

Initializes the hyperparameters of the support vector machine (SVM) algorithm. You can either directly set the hyperparameters or specify multiple values for each hyperparameter. If you specify multiple values for each hyperparameter, the [Train Classification Model](../lvaml/aml_train_classification_model.html) VI uses grid search to find the optimal set of hyperparameters.

[Examples](#examples)

#### Set Parameters

[IMAGE alt='image' src='initialize_classification_model__svm_set.gif']

|  | hyperparameters specifies the hyperparameters of the SVM model. SVM type specifies the type of the SVM model. 1C_SVC (default)—Specifies the C-SVM model.2NU_SVC—Specifies the nu-SVM model. c specifies the c parameter for the C-SVM model. The default is 1. The lower the value of c, the more wrongly classified training samples the SVM model allows for. The c parameter must be greater than 0. This input is valid only if SVM type is C_SVC. nu specifies the nu parameter for the nu-SVM model. The nu parameter is both a lower bound for the number of samples that are support vectors and an upper bound for the number of samples that are on the wrong side of the hyperplane. The default is 0.5. The nu parameter must be in the range [0,1]. This input is valid only if SVM type is NU_SVC. For example, if nu is 0.05, the training samples that are wrongly classified are not allowed to take up more than 5 percent of all training samples. Also, at least 5 percent of the training samples are support vectors. kernel settings specifies settings to configure the kernel function. This VI supports the following kernel functions: Kernel functionDefinitionDescription Linear functionx and y are the input sample vectors. Polynomial functionx and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. Radial basis functionx and y are the input sample vectors. Sigmoid functionx and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. type specifies the type of the kernel function. 0Linear (default)—Linear function 1Polynomial—Polynomial function 2RBF—Radial basis function 3Sigmoid—Sigmoid function degree specifies the degree coefficient of the kernel function. The default is 3. gamma specifies the gamma coefficient of the kernel function. The default is 1. coef0 specifies the coef0 coefficient of the kernel function. The default is 0. weighted c specifies different weights of parameter c for different classes in the training data. Use this input when the training data is unbalanced. In unbalanced data, the number of samples for some classes is much greater than that in other classes. If you specify this input, the Deploy Classification Model VI cannot return the predicted probabilities. label specifies the label of the data to assign weight. weight specifies the weight to assign to the label. tolerance specifies the tolerance for the stopping criteria. The default is 0.001. max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 100000. The model fitting stops if the number of optimization iterations reaches max iteration. |  |
| --- | --- | --- |
|  | SVM type specifies the type of the SVM model. 1C_SVC (default)—Specifies the C-SVM model.2NU_SVC—Specifies the nu-SVM model. |  |
| 1 | C_SVC (default)—Specifies the C-SVM model. |  |
| 2 | NU_SVC—Specifies the nu-SVM model. |  |
|  | c specifies the c parameter for the C-SVM model. The default is 1. The lower the value of c, the more wrongly classified training samples the SVM model allows for. The c parameter must be greater than 0. This input is valid only if SVM type is C_SVC. |  |
|  | nu specifies the nu parameter for the nu-SVM model. The nu parameter is both a lower bound for the number of samples that are support vectors and an upper bound for the number of samples that are on the wrong side of the hyperplane. The default is 0.5. The nu parameter must be in the range [0,1]. This input is valid only if SVM type is NU_SVC. For example, if nu is 0.05, the training samples that are wrongly classified are not allowed to take up more than 5 percent of all training samples. Also, at least 5 percent of the training samples are support vectors. |  |
|  | kernel settings specifies settings to configure the kernel function. This VI supports the following kernel functions: Kernel functionDefinitionDescription Linear functionx and y are the input sample vectors. Polynomial functionx and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. Radial basis functionx and y are the input sample vectors. Sigmoid functionx and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. type specifies the type of the kernel function. 0Linear (default)—Linear function 1Polynomial—Polynomial function 2RBF—Radial basis function 3Sigmoid—Sigmoid function degree specifies the degree coefficient of the kernel function. The default is 3. gamma specifies the gamma coefficient of the kernel function. The default is 1. coef0 specifies the coef0 coefficient of the kernel function. The default is 0. |  |
| Kernel function | Definition | Description |
| Linear function |  | x and y are the input sample vectors. |
| Polynomial function |  | x and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. |
| Radial basis function |  | x and y are the input sample vectors. |
| Sigmoid function |  | x and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. |
|  | type specifies the type of the kernel function. 0Linear (default)—Linear function 1Polynomial—Polynomial function 2RBF—Radial basis function 3Sigmoid—Sigmoid function |  |
| 0 | Linear (default)—Linear function |  |
| 1 | Polynomial—Polynomial function |  |
| 2 | RBF—Radial basis function |  |
| 3 | Sigmoid—Sigmoid function |  |
|  | degree specifies the degree coefficient of the kernel function. The default is 3. |  |
|  | gamma specifies the gamma coefficient of the kernel function. The default is 1. |  |
|  | coef0 specifies the coef0 coefficient of the kernel function. The default is 0. |  |
|  | weighted c specifies different weights of parameter c for different classes in the training data. Use this input when the training data is unbalanced. In unbalanced data, the number of samples for some classes is much greater than that in other classes. If you specify this input, the Deploy Classification Model VI cannot return the predicted probabilities. label specifies the label of the data to assign weight. weight specifies the weight to assign to the label. |  |
|  | label specifies the label of the data to assign weight. |  |
|  | weight specifies the weight to assign to the label. |  |
|  | tolerance specifies the tolerance for the stopping criteria. The default is 0.001. |  |
|  | max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 100000. The model fitting stops if the number of optimization iterations reaches max iteration. |  |
|  | cross validation configuration specifies settings for cross validation. enable? specifies whether this VI enables cross validation in model training. The default is FALSE, which specifies that this VI disables cross validation in model training. If enable? is TRUE, the Train Classification Model VI can return confusion matrix and metrics. number of folds specifies the number of sections that this VI divides the training data into. The default is 3. One section is test data, and the remaining sections are training data. The Evaluate Classification Model VI repeats the cross-validation process for n times, where n equals number of folds. metric configuration specifies the configuration for the evaluation metric in cross validation. average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |  |
|  | enable? specifies whether this VI enables cross validation in model training. The default is FALSE, which specifies that this VI disables cross validation in model training. If enable? is TRUE, the Train Classification Model VI can return confusion matrix and metrics. |  |
|  | number of folds specifies the number of sections that this VI divides the training data into. The default is 3. One section is test data, and the remaining sections are training data. The Evaluate Classification Model VI repeats the cross-validation process for n times, where n equals number of folds. |  |
|  | metric configuration specifies the configuration for the evaluation metric in cross validation. average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |  |
|  | average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. |  |
| 0 | Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples. |  |
| 1 | Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels. |  |
| 2 | Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label. |  |
| 3 | Binary—Calculates the metric values for the class that positive label specifies. |  |
|  | positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |  |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |  |
|  | untrained SVM model returns the initialized SVM model for training. |  |
|  | error out contains error information. This output provides standard error out functionality. |  |

#### Search Parameters

[IMAGE alt='image' src='initialize_classification_model__svm_search.gif']

|  | hyperparameter grids specifies multiple values for each hyperparameter of the SVM model. SVM type specifies the type of the SVM model. 1C_SVC (default)—Specifies the C-SVM model.2NU_SVC—Specifies the nu-SVM model. c specifies the c parameter for the C-SVM model. The lower the value of c, the more wrongly classified training samples the SVM model allows for. The c parameter must be greater than 0. This input is valid only if SVM type is C_SVC. nu specifies the nu parameter for the nu-SVM model. The nu parameter is both a lower bound for the number of samples that are support vectors and an upper bound for the number of samples that are on the wrong side of the hyperplane. The nu parameter must be in the range [0,1]. This input is valid only if SVM type is NU_SVC. For example, if nu is 0.05, the training samples that are wrongly classified are not allowed to take up more than 5 percent of all training samples. Also, at least 5 percent of the training samples are support vectors. kernel settings specifies settings to configure the kernel function. This VI supports the following kernel functions: Kernel functionDefinitionDescription Linear functionx and y are the input sample vectors. Polynomial functionx and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. Radial basis functionx and y are the input sample vectors. Sigmoid functionx and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. type specifies the type of the kernel function. 0Linear—Linear function 1Polynomial—Polynomial function 2RBF—Radial basis function 3Sigmoid—Sigmoid function degree specifies the degree coefficient of the kernel function. gamma specifies the gamma coefficient of the kernel function. coef0 specifies the coef0 coefficient of the kernel function. weighted c specifies different weights of parameter c for different classes in the training data. Use this input when the training data is unbalanced. In unbalanced data, the number of samples for some classes is much greater than that in other classes. If you specify this input, the Deploy Classification Model VI cannot return the predicted probabilities. label specifies the label of the data to assign weight. weight specifies the weight to assign to the label. tolerance specifies the tolerance for the stopping criteria. The default is 0.001. max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 100000. The model fitting stops if the number of optimization iterations reaches max iteration. |  |
| --- | --- | --- |
|  | SVM type specifies the type of the SVM model. 1C_SVC (default)—Specifies the C-SVM model.2NU_SVC—Specifies the nu-SVM model. |  |
| 1 | C_SVC (default)—Specifies the C-SVM model. |  |
| 2 | NU_SVC—Specifies the nu-SVM model. |  |
|  | c specifies the c parameter for the C-SVM model. The lower the value of c, the more wrongly classified training samples the SVM model allows for. The c parameter must be greater than 0. This input is valid only if SVM type is C_SVC. |  |
|  | nu specifies the nu parameter for the nu-SVM model. The nu parameter is both a lower bound for the number of samples that are support vectors and an upper bound for the number of samples that are on the wrong side of the hyperplane. The nu parameter must be in the range [0,1]. This input is valid only if SVM type is NU_SVC. For example, if nu is 0.05, the training samples that are wrongly classified are not allowed to take up more than 5 percent of all training samples. Also, at least 5 percent of the training samples are support vectors. |  |
|  | kernel settings specifies settings to configure the kernel function. This VI supports the following kernel functions: Kernel functionDefinitionDescription Linear functionx and y are the input sample vectors. Polynomial functionx and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. Radial basis functionx and y are the input sample vectors. Sigmoid functionx and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. type specifies the type of the kernel function. 0Linear—Linear function 1Polynomial—Polynomial function 2RBF—Radial basis function 3Sigmoid—Sigmoid function degree specifies the degree coefficient of the kernel function. gamma specifies the gamma coefficient of the kernel function. coef0 specifies the coef0 coefficient of the kernel function. |  |
| Kernel function | Definition | Description |
| Linear function |  | x and y are the input sample vectors. |
| Polynomial function |  | x and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. |
| Radial basis function |  | x and y are the input sample vectors. |
| Sigmoid function |  | x and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. |
|  | type specifies the type of the kernel function. 0Linear—Linear function 1Polynomial—Polynomial function 2RBF—Radial basis function 3Sigmoid—Sigmoid function |  |
| 0 | Linear—Linear function |  |
| 1 | Polynomial—Polynomial function |  |
| 2 | RBF—Radial basis function |  |
| 3 | Sigmoid—Sigmoid function |  |
|  | degree specifies the degree coefficient of the kernel function. |  |
|  | gamma specifies the gamma coefficient of the kernel function. |  |
|  | coef0 specifies the coef0 coefficient of the kernel function. |  |
|  | weighted c specifies different weights of parameter c for different classes in the training data. Use this input when the training data is unbalanced. In unbalanced data, the number of samples for some classes is much greater than that in other classes. If you specify this input, the Deploy Classification Model VI cannot return the predicted probabilities. label specifies the label of the data to assign weight. weight specifies the weight to assign to the label. |  |
|  | label specifies the label of the data to assign weight. |  |
|  | weight specifies the weight to assign to the label. |  |
|  | tolerance specifies the tolerance for the stopping criteria. The default is 0.001. |  |
|  | max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 100000. The model fitting stops if the number of optimization iterations reaches max iteration. |  |
|  | hyperparameter optimization specifies the method of optimization to determine the optimal hyperparameter settings. hyperparameter search method specifies the method to search for the optimal set of hyperparameters. 0Exhaustive search (default)—Tests all possible hyperparameter combinations in the training process. This method is reliable but time-consuming.1Random search—Tests a random subset of the hyperparameter combinations in the training process. This method is faster. number of searchings specifies the number of hyperparameter combinations that this VI selects to train the model. The default is 1. This input is valid only if hyperparameter search method is Random search. evaluation metric specifies the metric to evaluate the trained model with different hyperparameter combinations. The Train Classification Model VI finds the optimal hyperparameter set based on evaluation metric. 0Accuracy1Precision2Recall3F1 score |  |
|  | hyperparameter search method specifies the method to search for the optimal set of hyperparameters. 0Exhaustive search (default)—Tests all possible hyperparameter combinations in the training process. This method is reliable but time-consuming.1Random search—Tests a random subset of the hyperparameter combinations in the training process. This method is faster. |  |
| 0 | Exhaustive search (default)—Tests all possible hyperparameter combinations in the training process. This method is reliable but time-consuming. |  |
| 1 | Random search—Tests a random subset of the hyperparameter combinations in the training process. This method is faster. |  |
|  | number of searchings specifies the number of hyperparameter combinations that this VI selects to train the model. The default is 1. This input is valid only if hyperparameter search method is Random search. |  |
|  | evaluation metric specifies the metric to evaluate the trained model with different hyperparameter combinations. The Train Classification Model VI finds the optimal hyperparameter set based on evaluation metric. 0Accuracy1Precision2Recall3F1 score |  |
| 0 | Accuracy |  |
| 1 | Precision |  |
| 2 | Recall |  |
| 3 | F1 score |  |
|  | cross validation configuration specifies settings for cross validation. number of folds specifies the number of sections that this VI divides the training data into. The default is 3. One section is test data, and the remaining sections are training data. The Evaluate Classification Model VI repeats the cross-validation process for n times, where n equals number of folds. metric configuration specifies the configuration for the evaluation metric in cross validation. average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |  |
|  | number of folds specifies the number of sections that this VI divides the training data into. The default is 3. One section is test data, and the remaining sections are training data. The Evaluate Classification Model VI repeats the cross-validation process for n times, where n equals number of folds. |  |
|  | metric configuration specifies the configuration for the evaluation metric in cross validation. average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |  |
|  | average method specifies the averaging method for this VI to calculate metric values for multiclass classification. 0Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples.1Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels.2Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label.3Binary—Calculates the metric values for the class that positive label specifies. |  |
| 0 | Micro (default)—Calculates metric values for each sample and returns the mean of the metric values for all samples. |  |
| 1 | Macro—Calculates the metric values for each label and returns the mean of the metric values for all labels. |  |
| 2 | Weighted—Calculates the metric values for each label and returns the mean of weighted metric values for all labels. The number of true cases in a label determines the weight of the metric value of the label. |  |
| 3 | Binary—Calculates the metric values for the class that positive label specifies. |  |
|  | positive label specifies the label of the class to calculate metric values. The default is 0. This input is valid only if average method is Binary. |  |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |  |
|  | untrained SVM model returns the initialized SVM model for training. |  |
|  | error out contains error information. This output provides standard error out functionality. |  |

#### Examples

Refer to the following VIs for examples of using the Initialize Classification Model (SVM) VI:

- Classification (Set Parameters, Training) VI: labview\examples\AML\Classification
- Classification (Search Parameters, Training) VI: labview\examples\AML\Classification

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_initialize_clustering_model_dbscan.html language=enus -->
## TOPIC 00029: Initialize Clustering Model (DBSCAN) VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_initialize_clustering_model_dbscan.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_initialize_clustering_model_dbscan.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Initialize Clustering Model (DBSCAN) VI

**Owning Palette:** [Clustering VIs](../lvaml/aml_clustering.html)

**Requires:** Analytics and Machine Learning Toolkit

Initializes the hyperparameters of the density-based spatial clustering of applications with noise (DBSCAN) algorithm. You can either directly set the hyperparameters or specify multiple values for each hyperparameter. If you specify multiple values for each hyperparameter, the [Train Clustering Model](../lvaml/aml_train_clustering_model.html) VI uses grid search to find the optimal set of hyperparameters.

[Examples](#examples)

#### Set Parameters

[IMAGE alt='image' src='initialize_clustering_model__dbscan_set.gif']

|  | hyperparameters specifies hyperparameters for the DBSCAN model. max distance specifies the maximum radius for a sample to form a neighborhood. The default is 1. min samples specifies the minimum number of samples that need to be in the neighborhood of a core sample. The default is 5. p specifies the power of the Minkowski metric that this VI uses to calculate distances between points. The default is 2. The following equation defines the Minkowski metric: where [x1, x2, …, xN] is the input feature vector and [core sample1, core sample2, …, core sampleN] is the core sample feature vector. |
| --- | --- |
|  | max distance specifies the maximum radius for a sample to form a neighborhood. The default is 1. |
|  | min samples specifies the minimum number of samples that need to be in the neighborhood of a core sample. The default is 5. |
|  | p specifies the power of the Minkowski metric that this VI uses to calculate distances between points. The default is 2. The following equation defines the Minkowski metric: where [x1, x2, …, xN] is the input feature vector and [core sample1, core sample2, …, core sampleN] is the core sample feature vector. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | untrained DBSCAN model returns the initialized DBSCAN model for training. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Search Parameters

[IMAGE alt='image' src='initialize_clustering_model__dbscan_search.gif']

|  | hyperparameter grids specifies multiple values for each hyperparameter of the DBSCAN model. max distance specifies the maximum distance between two samples for them to share the same neighborhood. min samples specifies the minimum number of samples in a neighborhood for a point to be a core point. p specifies the power of the Minkowski metric that this VI uses to calculate distances between points. The following equation defines the Minkowski metric: where [x1, x2, …, xN] is the input feature vector and [core sample1, core sample2, …, core sampleN] is the core sample feature vector. |
| --- | --- |
|  | max distance specifies the maximum distance between two samples for them to share the same neighborhood. |
|  | min samples specifies the minimum number of samples in a neighborhood for a point to be a core point. |
|  | p specifies the power of the Minkowski metric that this VI uses to calculate distances between points. The following equation defines the Minkowski metric: where [x1, x2, …, xN] is the input feature vector and [core sample1, core sample2, …, core sampleN] is the core sample feature vector. |
|  | hyperparameter optimization specifies the method of optimization to determine the optimal hyperparameter settings. hyperparameter search method specifies the method to search for the optimal set of hyperparameters. 0Exhaustive search (default)—Tests all possible hyperparameter combinations in the training process. This method is reliable but time-consuming.1Random search—Tests a random subset of the hyperparameter combinations in the training process. This method is faster. number of searchings specifies the number of hyperparameter combinations that this VI selects to train the model. The default is 1. This input is valid only if hyperparameter search method is Random search. |
|  | hyperparameter search method specifies the method to search for the optimal set of hyperparameters. 0Exhaustive search (default)—Tests all possible hyperparameter combinations in the training process. This method is reliable but time-consuming.1Random search—Tests a random subset of the hyperparameter combinations in the training process. This method is faster. |
| 0 | Exhaustive search (default)—Tests all possible hyperparameter combinations in the training process. This method is reliable but time-consuming. |
| 1 | Random search—Tests a random subset of the hyperparameter combinations in the training process. This method is faster. |
|  | number of searchings specifies the number of hyperparameter combinations that this VI selects to train the model. The default is 1. This input is valid only if hyperparameter search method is Random search. |
|  | evaluation metric specifies the criterion to evaluate the trained clustering model. 0Davies Bouldin Index—Evaluates the clustering model using the Davies Bouldin Index metric. The lower the value of metric, the better the compactness and separation of the clustering model.1Dunn Index (default)—Evaluates the clustering model using the Dunn Index metric. The higher the value of metric, the better the compactness and separation of the clustering model.2Jaccard Index—Evaluates the clustering model using the Jaccard Index metric. The lower the value of metric, the better the separation of the clustering model.3Rand Index—Evaluates the clustering model using the Rand Index metric. The lower the value of metric, the better the separation of the clustering model. |
| 0 | Davies Bouldin Index—Evaluates the clustering model using the Davies Bouldin Index metric. The lower the value of metric, the better the compactness and separation of the clustering model. |
| 1 | Dunn Index (default)—Evaluates the clustering model using the Dunn Index metric. The higher the value of metric, the better the compactness and separation of the clustering model. |
| 2 | Jaccard Index—Evaluates the clustering model using the Jaccard Index metric. The lower the value of metric, the better the separation of the clustering model. |
| 3 | Rand Index—Evaluates the clustering model using the Rand Index metric. The lower the value of metric, the better the separation of the clustering model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | untrained DBSCAN model returns the initialized DBSCAN model for training. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Initialize Clustering Model (DBSCAN) VI:

- Clustering (Set Parameters, Training) VI: labview\examples\AML\Clustering
- Clustering (Search Parameters, Training) VI: labview\examples\AML\Clustering

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_initialize_clustering_model_gmm.html language=enus -->
## TOPIC 00030: Initialize Clustering Model (GMM) VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_initialize_clustering_model_gmm.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_initialize_clustering_model_gmm.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Initialize Clustering Model (GMM) VI

**Owning Palette:** [Clustering VIs](../lvaml/aml_clustering.html)

**Requires:** Analytics and Machine Learning Toolkit

Initializes the hyperparameters of the Gaussian mixture model (GMM) algorithm. You can either directly set the hyperparameters or specify multiple values for each hyperparameter. If you specify multiple values for each hyperparameter, the [Train Clustering Model](../lvaml/aml_train_clustering_model.html) VI uses grid search to find the optimal set of hyperparameters.

[Details](#details)  [Examples](#examples)

#### Set Parameters

[IMAGE alt='image' src='initialize_clustering_model__gmm_set.gif']

|  | initial parameters specifies the initial parameters to train the GMM model. auto initialization specifies whether this VI automatically calculates the values in initial parameters using K-Means algorithm. The default is TRUE, which specifies that this VI automatically sets the values in initial parameters using K-Means algorithm. If you do not specify values for the arrays in initial parameters and auto initialization is FALSE, this VI randomly calculates the values in initial parameters. initial mean values specifies the initial mean values of all Gaussian distributions in the GMM model. initial covariance values specifies the initial covariance values of all Gaussian distributions in the GMM model. initial covariance matrix specifies the initial covariance matrix of each Gaussian distribution in the GMM model. initial weights specifies the initial weights of all Gaussian distributions in the GMM model. |
| --- | --- |
|  | auto initialization specifies whether this VI automatically calculates the values in initial parameters using K-Means algorithm. The default is TRUE, which specifies that this VI automatically sets the values in initial parameters using K-Means algorithm. If you do not specify values for the arrays in initial parameters and auto initialization is FALSE, this VI randomly calculates the values in initial parameters. |
|  | initial mean values specifies the initial mean values of all Gaussian distributions in the GMM model. |
|  | initial covariance values specifies the initial covariance values of all Gaussian distributions in the GMM model. initial covariance matrix specifies the initial covariance matrix of each Gaussian distribution in the GMM model. |
|  | initial covariance matrix specifies the initial covariance matrix of each Gaussian distribution in the GMM model. |
|  | initial weights specifies the initial weights of all Gaussian distributions in the GMM model. |
|  | hyperparameters specifies the hyperparameters to train the GMM model. number of clusters specifies the number of Gaussian distributions in the GMM model. The default is 3. regulator specifies the value that this VI adds to the covariance matrix to prevent the covariance matrix from converging to 0. The default is 0.000001. tolerance specifies the tolerance for the stopping criteria. The default is 0.0001. The model fitting stops if the change of maximum likelihood between two successive optimization iterations is lower than tolerance. max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 100. The model fitting stops if the number of optimization iterations reaches max iteration. |
|  | number of clusters specifies the number of Gaussian distributions in the GMM model. The default is 3. |
|  | regulator specifies the value that this VI adds to the covariance matrix to prevent the covariance matrix from converging to 0. The default is 0.000001. |
|  | tolerance specifies the tolerance for the stopping criteria. The default is 0.0001. The model fitting stops if the change of maximum likelihood between two successive optimization iterations is lower than tolerance. |
|  | max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 100. The model fitting stops if the number of optimization iterations reaches max iteration. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | untrained GMM model returns the initialized GMM model for training. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Search Parameters

[IMAGE alt='image' src='initialize_clustering_model__gmm_search.gif']

|  | initial parameters specifies the initial parameters to train the GMM model. auto initialization specifies whether this VI automatically calculates the values in initial parameters using K-Means algorithm. The default is TRUE, which specifies that this VI automatically sets the values in initial parameters using K-Means algorithm. If you do not specify values for the arrays in initial parameters and auto initialization is FALSE, this VI randomly calculates the values in initial parameters. initial mean values specifies the initial mean values of all Gaussian distributions in the GMM model. initial covariance values specifies the initial covariance values of all Gaussian distributions in the GMM model. initial covariance matrix specifies the initial covariance matrix of each Gaussian distribution in the GMM model. initial weights specifies the initial weights of all Gaussian distributions in the GMM model. |
| --- | --- |
|  | auto initialization specifies whether this VI automatically calculates the values in initial parameters using K-Means algorithm. The default is TRUE, which specifies that this VI automatically sets the values in initial parameters using K-Means algorithm. If you do not specify values for the arrays in initial parameters and auto initialization is FALSE, this VI randomly calculates the values in initial parameters. |
|  | initial mean values specifies the initial mean values of all Gaussian distributions in the GMM model. |
|  | initial covariance values specifies the initial covariance values of all Gaussian distributions in the GMM model. initial covariance matrix specifies the initial covariance matrix of each Gaussian distribution in the GMM model. |
|  | initial covariance matrix specifies the initial covariance matrix of each Gaussian distribution in the GMM model. |
|  | initial weights specifies the initial weights of all Gaussian distributions in the GMM model. |
|  | hyperparameter grids specifies multiple values for each hyperparameter of the GMM model. number of clusters specifies the number of Gaussian distributions in the trained GMM model. regulator specifies the value that this VI adds to covariance to prevent the covariance matrix from converging to 0. tolerance specifies the tolerance for the stopping criteria. max iteration specifies the maximum number of optimization iterations for the stopping criteria. The model fitting stops if the number of optimization iterations reaches max iteration. attempts specifies the number of times that the Train Clustering Model VI trains the model with different hyperparameter combinations. |
|  | number of clusters specifies the number of Gaussian distributions in the trained GMM model. |
|  | regulator specifies the value that this VI adds to covariance to prevent the covariance matrix from converging to 0. |
|  | tolerance specifies the tolerance for the stopping criteria. |
|  | max iteration specifies the maximum number of optimization iterations for the stopping criteria. The model fitting stops if the number of optimization iterations reaches max iteration. |
|  | attempts specifies the number of times that the Train Clustering Model VI trains the model with different hyperparameter combinations. |
|  | hyperparameter optimization specifies the method of optimization to determine the optimal hyperparameter settings. hyperparameter search method specifies the method to search for the optimal set of hyperparameters. 0Exhaustive search (default)—Tests all possible hyperparameter combinations in the training process. This method is reliable but time-consuming.1Random search—Tests a random subset of the hyperparameter combinations in the training process. This method is faster. number of searchings specifies the number of hyperparameter combinations that this VI selects to train the model. The default is 1. This input is valid only if hyperparameter search method is Random search. |
|  | hyperparameter search method specifies the method to search for the optimal set of hyperparameters. 0Exhaustive search (default)—Tests all possible hyperparameter combinations in the training process. This method is reliable but time-consuming.1Random search—Tests a random subset of the hyperparameter combinations in the training process. This method is faster. |
| 0 | Exhaustive search (default)—Tests all possible hyperparameter combinations in the training process. This method is reliable but time-consuming. |
| 1 | Random search—Tests a random subset of the hyperparameter combinations in the training process. This method is faster. |
|  | number of searchings specifies the number of hyperparameter combinations that this VI selects to train the model. The default is 1. This input is valid only if hyperparameter search method is Random search. |
|  | evaluation metric specifies the criterion to evaluate the trained clustering model. 0Davies Bouldin Index—Evaluates the clustering model using the Davies Bouldin Index metric. The lower the value of metric, the better the compactness and separation of the clustering model.1Dunn Index—Evaluates the clustering model using the Dunn Index metric. The higher the value of metric, the better the compactness and separation of the clustering model.2Jaccard Index—Evaluates the clustering model using the Jaccard Index metric. The lower the value of metric, the better the separation of the clustering model.3Rand Index—Evaluates the clustering model using the Rand Index metric. The lower the value of metric, the better the separation of the clustering model.4AIC (default)—Evaluates the GMM model using the Akaike Information Criterion (AIC) metric. The lower the value of metric, the better the GMM model is.5BIC—Evaluates the GMM model using the Bayesian Information Criterion (BIC) metric. The lower the value of metric, the better the GMM model is. |
| 0 | Davies Bouldin Index—Evaluates the clustering model using the Davies Bouldin Index metric. The lower the value of metric, the better the compactness and separation of the clustering model. |
| 1 | Dunn Index—Evaluates the clustering model using the Dunn Index metric. The higher the value of metric, the better the compactness and separation of the clustering model. |
| 2 | Jaccard Index—Evaluates the clustering model using the Jaccard Index metric. The lower the value of metric, the better the separation of the clustering model. |
| 3 | Rand Index—Evaluates the clustering model using the Rand Index metric. The lower the value of metric, the better the separation of the clustering model. |
| 4 | AIC (default)—Evaluates the GMM model using the Akaike Information Criterion (AIC) metric. The lower the value of metric, the better the GMM model is. |
| 5 | BIC—Evaluates the GMM model using the Bayesian Information Criterion (BIC) metric. The lower the value of metric, the better the GMM model is. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | untrained GMM model returns the initialized GMM model for training. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Initialize Clustering Model (GMM) Details

The following equation defines the GMM model:

[IMAGE alt='image' src='eq_gmm.gif']

| where |  |
| --- | --- |
|  | K is the number of Gaussian mixture components. Each Gaussian mixture component represents a Gaussian distribution. |
|  | μi and Σi are the mean value and the covariance value of the ith Gaussian mixture component |
|  | αi is the weight of the ith Gaussian mixture component |

#### Examples

Refer to the following VIs for examples of using the Initialize Clustering Model (GMM) VI:

- Clustering (Set Parameters, Training) VI: labview\examples\AML\Clustering
- Clustering (Search Parameters, Training) VI: labview\examples\AML\Clustering

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_initialize_clustering_model_kmeans.html language=enus -->
## TOPIC 00031: Initialize Clustering Model (K-Means) VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_initialize_clustering_model_kmeans.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_initialize_clustering_model_kmeans.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Initialize Clustering Model (K-Means) VI

**Owning Palette:** [Clustering VIs](../lvaml/aml_clustering.html)

**Requires:** Analytics and Machine Learning Toolkit

Initializes the hyperparameters of the K-Means algorithm. You can either directly set the hyperparameters or specify multiple values for each hyperparameter. If you specify multiple values for each hyperparameter, the [Train Clustering Model](../lvaml/aml_train_clustering_model.html) VI uses grid search to find the optimal set of hyperparameters.

[Examples](#examples)

#### Set Parameters

[IMAGE alt='image' src='initialize_clustering_model__k-means_set.gif']

|  | initial centroids specifies the initial centroids. This input is valid only if initial method is Custom. |
| --- | --- |
|  | hyperparameters specifies the hyperparameters for the K-Means model. number of clusters specifies the number of clusters in the K-Means model. The default is 3. tolerance specifies the tolerance for the stopping criteria. The default is 0.00001. max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 50. The model fitting stops if the number of optimization iterations reaches max iteration. initial method specifies the method to select initial centroids. 0K-Means++ (default)—Selects initial centroids in a way that can always speed up convergence.1Random—Randomly selects a specific number of observations from the data and uses them as the initial centroids. This method is also called the Forgy method.2Custom—Directly specifies the initial centroids using the initial centroids input. |
|  | number of clusters specifies the number of clusters in the K-Means model. The default is 3. |
|  | tolerance specifies the tolerance for the stopping criteria. The default is 0.00001. |
|  | max iteration specifies the maximum number of optimization iterations for the stopping criteria. The default is 50. The model fitting stops if the number of optimization iterations reaches max iteration. |
|  | initial method specifies the method to select initial centroids. 0K-Means++ (default)—Selects initial centroids in a way that can always speed up convergence.1Random—Randomly selects a specific number of observations from the data and uses them as the initial centroids. This method is also called the Forgy method.2Custom—Directly specifies the initial centroids using the initial centroids input. |
| 0 | K-Means++ (default)—Selects initial centroids in a way that can always speed up convergence. |
| 1 | Random—Randomly selects a specific number of observations from the data and uses them as the initial centroids. This method is also called the Forgy method. |
| 2 | Custom—Directly specifies the initial centroids using the initial centroids input. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | untrained K-Means model returns the initialized K-Means model for training. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Search Parameters

[IMAGE alt='image' src='initialize_clustering_model__k-means_search.gif']

|  | initial centroids specifies the initial centroids. This input is valid only if initial method is Custom. |
| --- | --- |
|  | hyperparameter grids specifies multiple values for each hyperparameter. number of clusters specifies the number of clusters in the K-Means model. attempts specifies the number of times that the Train Clustering Model VI trains the model with different hyperparameter combinations. tolerance specifies the tolerance for the stopping criteria. max iteration specifies the maximum number of optimization iterations for the stopping criteria. The model fitting stops if the number of optimization iterations reaches max iteration. initial method specifies the initial method. 0K-Means++ (default)—Selects initial centroids in a way that can always speed up convergence.1Random—Randomly selects a specific number of observations from the data and uses them as the initial centroids. This method is also called the Forgy method.2Custom—Directly specifies the initial centroids using the initial centroids input. |
|  | number of clusters specifies the number of clusters in the K-Means model. |
|  | attempts specifies the number of times that the Train Clustering Model VI trains the model with different hyperparameter combinations. |
|  | tolerance specifies the tolerance for the stopping criteria. |
|  | max iteration specifies the maximum number of optimization iterations for the stopping criteria. The model fitting stops if the number of optimization iterations reaches max iteration. |
|  | initial method specifies the initial method. 0K-Means++ (default)—Selects initial centroids in a way that can always speed up convergence.1Random—Randomly selects a specific number of observations from the data and uses them as the initial centroids. This method is also called the Forgy method.2Custom—Directly specifies the initial centroids using the initial centroids input. |
| 0 | K-Means++ (default)—Selects initial centroids in a way that can always speed up convergence. |
| 1 | Random—Randomly selects a specific number of observations from the data and uses them as the initial centroids. This method is also called the Forgy method. |
| 2 | Custom—Directly specifies the initial centroids using the initial centroids input. |
|  | hyperparameter optimization specifies the method of optimization to determine the optimal hyperparameter settings. hyperparameter search method specifies the method to search for the optimal set of hyperparameters. 0Exhaustive search (default)—Tests all possible hyperparameter combinations in the training process. This method is reliable but time-consuming.1Random search—Tests a random subset of the hyperparameter combinations in the training process. This method is faster. number of searchings specifies the number of hyperparameter combinations that this VI selects to train the model. The default is 1. This input is valid only if hyperparameter search method is Random search. |
|  | hyperparameter search method specifies the method to search for the optimal set of hyperparameters. 0Exhaustive search (default)—Tests all possible hyperparameter combinations in the training process. This method is reliable but time-consuming.1Random search—Tests a random subset of the hyperparameter combinations in the training process. This method is faster. |
| 0 | Exhaustive search (default)—Tests all possible hyperparameter combinations in the training process. This method is reliable but time-consuming. |
| 1 | Random search—Tests a random subset of the hyperparameter combinations in the training process. This method is faster. |
|  | number of searchings specifies the number of hyperparameter combinations that this VI selects to train the model. The default is 1. This input is valid only if hyperparameter search method is Random search. |
|  | evaluation metric specifies the criterion to evaluate the trained clustering model. 0Davies Bouldin Index (default)—Evaluates the clustering model using the Davies Bouldin Index metric. The lower the value of metric, the better the compactness and separation of the clustering model.1Dunn Index—Evaluates the clustering model using the Dunn Index metric. The higher the value of metric, the better the compactness and separation of the clustering model.2Jaccard Index—Evaluates the clustering model using the Jaccard Index metric. The lower the value of metric, the better the separation of the clustering model.3Rand Index—Evaluates the clustering model using the Rand Index metric. The lower the value of metric, the better the separation of the clustering model. |
| 0 | Davies Bouldin Index (default)—Evaluates the clustering model using the Davies Bouldin Index metric. The lower the value of metric, the better the compactness and separation of the clustering model. |
| 1 | Dunn Index—Evaluates the clustering model using the Dunn Index metric. The higher the value of metric, the better the compactness and separation of the clustering model. |
| 2 | Jaccard Index—Evaluates the clustering model using the Jaccard Index metric. The lower the value of metric, the better the separation of the clustering model. |
| 3 | Rand Index—Evaluates the clustering model using the Rand Index metric. The lower the value of metric, the better the separation of the clustering model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | untrained K-Means model returns the initialized K-Means model for training. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Initialize Clustering Model (K-Means) VI:

- Clustering (Set Parameters, Training) VI: labview\examples\AML\Clustering
- Clustering (Search Parameters, Training) VI: labview\examples\AML\Clustering

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_kmeans_prop.html language=enus -->
## TOPIC 00032: AML K-Means Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_kmeans_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_kmeans_prop.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AML K-Means Properties

Wire the **untrained K-Means model** output of the [Initialize Clustering Model (K-Means)](aml_initialize_clustering_model_kmeans.html) VI to the **reference** input of a standard Property Node to get an AML K-Means Property Node. This Property Node has the following properties:

| Property | Access | Data Type | Description |
| --- | --- | --- | --- |
| Centroids | Read Only |  | Returns the centroids in the trained clustering model. The number of rows equals the number of clusters. |
| Class Labels | Read Only |  | Returns the labels of the data. |
| Evaluation Metric | Read Only |  | Returns the criterion to evaluate the trained clustering model. |
| Hyperparameters | Read Only |  | If you select the Set Parameters instance of the Initialize Clustering Model (K-Means) VI, this property returns the hyperparameters input of the VI. If you select the Search Parameters instance of the Initialize Clustering Model (K-Means) VI , this property returns the optimal hyperparameters after the Train Clustering Model VI completes grid search. |
| Hyperparameter Grids | Read Only |  | Returns multiple values for each hyperparameter. |
| Hyperparameter Optimization | Read Only |  | Returns the method of optimization to determine the optimal hyperparameter settings. |
| Model Initialized? | Read Only |  | Returns whether the model is initialized. |
| Model Trained? | Read Only |  | Returns whether the model is trained. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_kpca.html language=enus -->
## TOPIC 00033: KPCA VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_kpca.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_kpca.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### KPCA VI

**Owning Palette:** [Feature Manipulation VIs](../lvaml/aml_feature_manipulation.html)

**Requires:** Analytics and Machine Learning Toolkit

Trains a kernel principal component analysis (KPCA) model. You can use the KPCA model to reduce the dimension of training data.

[Example](#examples)

[IMAGE alt='image' src='kpca.gif']

|  | model in specifies the information about the entire workflow of the model. |  |
| --- | --- | --- |
|  | PCA settings specifies the method and value for this VI to calculate the number of principal components. criteria specifies the method for this VI to calculate the number of principal components. 0number of components (default)—Directly specifies the number of principal components.1ratio of variance—Specifies the ratio of variance for this VI to calculate the number of principal components. number of components specifies the number of principal components. This input is valid only if criteria is number of components. ratio of variance specifies the ratio of the variance in principal components to the total variance. This VI automatically calculates the number of components. The default is 0.95. This input is valid only if criteria is ratio of variance. |  |
|  | criteria specifies the method for this VI to calculate the number of principal components. 0number of components (default)—Directly specifies the number of principal components.1ratio of variance—Specifies the ratio of variance for this VI to calculate the number of principal components. |  |
| 0 | number of components (default)—Directly specifies the number of principal components. |  |
| 1 | ratio of variance—Specifies the ratio of variance for this VI to calculate the number of principal components. |  |
|  | number of components specifies the number of principal components. This input is valid only if criteria is number of components. |  |
|  | ratio of variance specifies the ratio of the variance in principal components to the total variance. This VI automatically calculates the number of components. The default is 0.95. This input is valid only if criteria is ratio of variance. |  |
|  | kernel settings specifies the settings to configure the kernel function. This VI supports the following kernel functions: Kernel functionDefinitionDescription Polynomial functionx and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. Radial basis functionx and y are the input sample vectors. Sigmoid functionx and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. type specifies type of the kernel function. 0Polynomial (default)—Polynomial function1RBF—Radial basis function2Sigmoid—Sigmoid function degree specifies the degree coefficient of the kernel function. The default is 3. gamma specifies the gamma coefficient of the kernel function. The default is 1. coef0 specifies the coef0 coefficient of the kernel function. The default is 0. |  |
| Kernel function | Definition | Description |
| Polynomial function |  | x and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. |
| Radial basis function |  | x and y are the input sample vectors. |
| Sigmoid function |  | x and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. |
|  | type specifies type of the kernel function. 0Polynomial (default)—Polynomial function1RBF—Radial basis function2Sigmoid—Sigmoid function |  |
| 0 | Polynomial (default)—Polynomial function |  |
| 1 | RBF—Radial basis function |  |
| 2 | Sigmoid—Sigmoid function |  |
|  | degree specifies the degree coefficient of the kernel function. The default is 3. |  |
|  | gamma specifies the gamma coefficient of the kernel function. The default is 1. |  |
|  | coef0 specifies the coef0 coefficient of the kernel function. The default is 0. |  |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |  |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |  |
|  | KPCA model info returns the information of the KPCA model. Wire KPCA model info to the reference input of a standard Property Node to get an AML KPCA Property Node. |  |
|  | error out contains error information. This output provides standard error out functionality. |  |

#### Example

Refer to the Feature Manipulation (Training) VI in the labview\examples\AML\Feature Manipulation directory for an example of using the KPCA VI.

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_kpca_prop.html language=enus -->
## TOPIC 00034: AML KPCA Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_kpca_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_kpca_prop.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AML KPCA Properties

Wire the **KPCA model info** output of the [KPCA](aml_kpca.html) VI to the **reference** input of a standard Property Node to get an AML KPCA Property Node. This Property Node has the following properties:

| Property | Access | Data Type | Description |
| --- | --- | --- | --- |
| Eigenvectors | Read Only |  | Returns the eigenvectors to calculate the principal components. The number of rows equals the number of features of the training data. The KPCA model uses a subset of the eigenvectors of the covariance matrix to calculate the principal components in the input data. |
| Kernel Settings | Read Only |  | Returns the settings to configure the kernel function. |
| Number of Selected Components | Read Only |  | Returns the number of principal components. |
| PCA Settings | Read Only |  | Returns the method and value to calculate the number of principal components. |
| Source Data | Read Only |  | Returns the training data for the KPCA model. |
| Variance | Read Only |  | Returns the variance of the principal components. The number of rows equals the number of principal components. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_load_data.html language=enus -->
## TOPIC 00035: Load Data (2D Array) VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_load_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_load_data.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Load Data (2D Array) VI

**Owning Palette:** [Data VIs](../lvaml/aml_data.html)

**Requires:** Analytics and Machine Learning Toolkit

Loads data and labels for training or deployment.

#### Training

[IMAGE alt='image' src='load_training_data__2d_array.gif']

|  | load data mode specifies how this VI loads data. 0Read Raw Data (default)—Loads raw data.1Apply Feature Manipulation—Applies feature manipulation to raw data while loading data. |
| --- | --- |
| 0 | Read Raw Data (default)—Loads raw data. |
| 1 | Apply Feature Manipulation—Applies feature manipulation to raw data while loading data. |
|  | model in specifies the information about the entire workflow of the model. |
|  | data specifies the training data. |
|  | data labels specifies the labels of the training data. For classification models, this input must not be empty. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Deployment

[IMAGE alt='image' src='load_testing_data__2d_array.gif']

|  | load data mode specifies how this VI loads data. 0Read Raw Data (default)—Loads raw data.1Apply Feature Manipulation—Applies feature manipulation to raw data while loading data. |
| --- | --- |
| 0 | Read Raw Data (default)—Loads raw data. |
| 1 | Apply Feature Manipulation—Applies feature manipulation to raw data while loading data. |
|  | model in specifies the information about the entire workflow of the model. |
|  | data specifies the data for deployment. |
|  | data labels specifies the labels of data for deployment. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_logisticregression.html language=enus -->
## TOPIC 00036: AML Logistic Regression Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_logisticregression.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_logisticregression.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AML Logistic Regression Properties

Wire the **untrained logistic regression model** output of the [Initialize Classification Model (LR)](aml_initialize_classification_model_lr.html) VI to the **reference** input of a standard Property Node to get an AML Logistic Regression Property Node. This Property Node has the following properties:

| Property | Access | Data Type | Description |
| --- | --- | --- | --- |
| Coefficients | Read Only |  | Returns the trained coefficients of the trained logistic regression model. The array size equals the number of classes. |
| Cross Validation Configuration | Read Only |  | Returns settings for cross validation. |
| Hyperparameters | Read Only |  | If you select the Set Parameters instance of the Initialize Classification Model (LR) VI, this property returns the hyperparameters input of the VI. If you select the Search Parameters instance of the Initialize Classification Model (LR) VI, this property returns the optimal hyperparameters after the Train Classification Model VI completes grid search. |
| Hyperparameter Grids | Read Only |  | Returns multiple values for each hyperparameter. |
| Hyperparameter Optimization | Read Only |  | Returns the method of optimization to determine the optimal hyperparameter settings. |
| Label of Each Class | Read Only |  | Returns the label of each class. |
| Model Initialized? | Read Only |  | Returns whether the model is initialized. |
| Model Trained? | Read Only |  | Returns whether the model is trained. |
| Number of Classes | Read Only |  | Returns the number of classes. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_neuralnetwork.html language=enus -->
## TOPIC 00037: AML Neural Network Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_neuralnetwork.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_neuralnetwork.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AML Neural Network Properties

Wire the **untrained neural network model** output of the [Initialize Classification Model (NN)](aml_initialize_classification_model_nn.html) VI to the **reference** input of a standard Property Node to get an AML Neural Network Property Node. This Property Node has the following properties:

| Property | Access | Data Type | Description |
| --- | --- | --- | --- |
| Cross Validation Configuration | Read Only |  | Returns settings for cross validation. |
| H to O Coefficients | Read Only |  | Returns the trained coefficients between the hidden layer and the output layer in the trained neural network model. The number of rows equals the number of output neurons. |
| Hyperparameters | Read Only |  | If you select the Set Parameters instance of the Initialize Classification Model (NN) VI, this property returns the hyperparameters input of the VI. If you select the Search Parameters instance of the Initialize Classification Model (NN) VI, this property returns the optimal hyperparameters after Train Classification Model VI completes grid search. |
| Hyperparameter Grids | Read Only |  | Returns multiple values for each hyperparameter. |
| Hyperparameter Optimization | Read Only |  | Returns the method of optimization to determine the optimal hyperparameter settings. |
| I to H Coefficients | Read Only |  | Returns the trained coefficients between the input layer and the hidden layer. The number of rows equals the number of hidden neurons. |
| Label of Each Class | Read Only |  | Returns the label of each class. |
| Model Initialized? | Read Only |  | Returns whether the model is initialized. |
| Model Trained? | Read Only |  | Returns whether the model is trained. |
| Number of Classes | Read Only |  | Returns the number of classes. |
| Number of Input Neurons | Read Only |  | Returns the number of input neurons. |
| Number of Output Neurons | Read Only |  | Returns the number of output neurons. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_normalize.html language=enus -->
## TOPIC 00038: Normalize VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_normalize.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_normalize.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Normalize VI

**Owning Palette:** [Feature Manipulation VIs](../lvaml/aml_feature_manipulation.html)

**Requires:** Analytics and Machine Learning Toolkit

Trains a normalization model. You can use the normalization model to normalize training data with Z-Score or Min-Max method.

You can perform [batch training](../lvamlconcepts/aml_gettingstarted.html) with this VI when you have a large training data set.

[Examples](#examples)

#### One Shot

[IMAGE alt='image' src='normalize.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | normalization settings specifies the settings of normalization. transformation method specifies the method of normalization. 0ZScore (default)—Normalizes the data so that the data has a mean of 0 and a variance of 1.1MinMax—Normalizes the data so that the data is in the range that range settings defines. range settings specifies the range of normalization for the MinMax method. This input is valid only if transformation method is MinMax. max specifies the maximum value of the normalized data. The default is 1. min specifies the minimum value of the normalized data. The default is 0. |
|  | transformation method specifies the method of normalization. 0ZScore (default)—Normalizes the data so that the data has a mean of 0 and a variance of 1.1MinMax—Normalizes the data so that the data is in the range that range settings defines. |
| 0 | ZScore (default)—Normalizes the data so that the data has a mean of 0 and a variance of 1. |
| 1 | MinMax—Normalizes the data so that the data is in the range that range settings defines. |
|  | range settings specifies the range of normalization for the MinMax method. This input is valid only if transformation method is MinMax. max specifies the maximum value of the normalized data. The default is 1. min specifies the minimum value of the normalized data. The default is 0. |
|  | max specifies the maximum value of the normalized data. The default is 1. |
|  | min specifies the minimum value of the normalized data. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | normalization model info returns the information of the normalization model. Wire normalization model info to the reference input of a standard Property Node to get an AML Normalize Property Node. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Batch

[IMAGE alt='image' src='normalize_batch.gif']

|  | reset specifies whether to reset the trained model programmatically at run time. The default is FALSE. |
| --- | --- |
|  | model in specifies the information about the entire workflow of the model. |
|  | normalization settings specifies the settings of normalization. transformation method specifies the method of normalization. 0ZScore (default)—Normalizes the data so that the data has a mean of 0 and a variance of 1.1MinMax—Normalizes the data so that the data is in the range that range settings defines. range settings specifies the range of normalization for the MinMax method. This input is valid only if transformation method is MinMax. max specifies the maximum value of the normalized data. The default is 1. min specifies the minimum value of the normalized data. The default is 0. |
|  | transformation method specifies the method of normalization. 0ZScore (default)—Normalizes the data so that the data has a mean of 0 and a variance of 1.1MinMax—Normalizes the data so that the data is in the range that range settings defines. |
| 0 | ZScore (default)—Normalizes the data so that the data has a mean of 0 and a variance of 1. |
| 1 | MinMax—Normalizes the data so that the data is in the range that range settings defines. |
|  | range settings specifies the range of normalization for the MinMax method. This input is valid only if transformation method is MinMax. max specifies the maximum value of the normalized data. The default is 1. min specifies the minimum value of the normalized data. The default is 0. |
|  | max specifies the maximum value of the normalized data. The default is 1. |
|  | min specifies the minimum value of the normalized data. The default is 0. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | normalization model info returns the information of the normalization model. Wire normalization model info to the reference input of a standard Property Node to get an AML Normalize Property Node. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Normalize VI:

- Feature Manipulation (Training) VI: labview\examples\AML\Feature Manipulation
- Feature Manipulation (Training) (Batch) VI: labview\examples\AML\Feature Manipulation
- Anomaly Detection (Training) VI: labview\examples\AML\Anomaly Detection
- Anomaly Detection (Training) (Batch) VI: labview\examples\AML\Anomaly Detection
- Classification (Set Parameters, Training) VI: labview\examples\AML\Classification

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_normalize_prop.html language=enus -->
## TOPIC 00039: AML Normalize Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_normalize_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_normalize_prop.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AML Normalize Properties

Wire the **normalization model info** output of the [Normalize](aml_normalize.html) VI to the **reference** input of a standard Property Node to get an AML Normalize Property Node. This Property Node has the following properties:

| Property | Access | Data Type | Description |
| --- | --- | --- | --- |
| Max Values | Read Only |  | Returns the maximum values of all features in the data for the Min-Max method. This property is available only if transformation method is MinMax. The array length is the number of features. Each element is the maximum value of each feature. |
| Mean Values | Read Only |  | Returns the mean values of all features in the data for the Z-Score method, when you perform one shot training. This property is available only if transformation method is ZScore. Returns the mean values of all features in the data, when you perform batch training. The array length is the number of features. Each element is the mean value of each feature. |
| Min Values | Read Only |  | Returns the minimum values of all features in the data for the Min-Max method. This property is available only if transformation method is MinMax. The array length is the number of features. Each element is the minimum value of each feature. |
| Standard Deviation Values | Read Only |  | Returns the standard deviation values of all features in the data for the Z-Score method. This property is available only if transformation method is ZScore. The array length is the number of features. Each element is the standard deviation value of each feature. |
| Normalization Settings | Read Only |  | Returns the settings of normalization. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_oneclasssvm_prop.html language=enus -->
## TOPIC 00040: AML One-Class SVM Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_oneclasssvm_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_oneclasssvm_prop.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AML One-Class SVM Properties

Wire the **untrained one-class SVM model** output of the [Initialize Anomaly Detection Model (One-Class SVM)](aml_initialize_anomaly_detection_model_one_class_svm.html) VI to the **reference** input of a standard Property Node to get an AML One-Class SVM Property Node. This Property Node has the following properties:

| Property | Access | Data Type | Description |
| --- | --- | --- | --- |
| Coefficients of Support Vectors | Read Only |  | Returns the coefficients of support vectors. The number of rows is one less than the number of classes. |
| Decision Function Constants | Read Only |  | Returns the decision function constants. |
| Hyperparameters | Read Only |  | Returns the hyperparameters of the one-class SVM model. |
| Indexes of Support Vectors | Read Only |  | Returns the indexes of support vectors that you can use to find support vectors from the training data. |
| Model Initialized? | Read Only |  | Returns whether the model is initialized. |
| Model Trained? | Read Only |  | Returns whether the model is trained. |
| Number of Support Vectors | Read Only |  | Returns the number of support vectors. |
| Support Vectors | Read Only |  | Returns all the support vectors. The number of rows is the number of vectors and the number of columns is the number of features. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_pal.html language=enus -->
## TOPIC 00041: Analytics and Machine Learning VIs

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_pal.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Analytics and Machine Learning VIs

July 2018, 377060B-01

**Requires:** Analytics and Machine Learning Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Analytics and Machine Learning VIs to create machine learning applications that discover patterns in large amounts of data and generate models that recognize patterns in new data.

You must activate the [LabVIEW Real-Time Module](/csh?topicname=lvrthelp/lv_real_time_help.html) to use the Analytics and Machine Learning VIs on a real-time target.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific Analytics and Machine Learning error codes](../lvamlconcepts/aml_error_codes.html).

| Subpalette | Description |
| --- | --- |
| Anomaly Detection VIs | Use the Anomaly Detection VIs to initialize, train, and deploy unsupervised anomaly detection models that detect anomalies in unlabeled data. |
| Classification VIs | Use the Classification VIs to initialize, train, evaluate, and deploy classification models that classify given sets of categories. |
| Clustering VIs | Use the Clustering VIs to initialize, train, evaluate, and deploy clustering models that group data items into clusters. Data items in the same cluster share more similarities than those in other clusters. |
| Data VIs | Use the Data VIs to save data for model training or deployment and view data changes from the Feature Manipulation VIs. |
| Feature Manipulation VIs | Use the Feature Manipulation VIs to train and deploy feature reduction and normalization models. |

© 2017–2018 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_pca.html language=enus -->
## TOPIC 00042: PCA VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_pca.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_pca.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### PCA VI

**Owning Palette:** [Feature Manipulation VIs](../lvaml/aml_feature_manipulation.html)

**Requires:** Analytics and Machine Learning Toolkit

Trains a principal component analysis (PCA) model. You can use the PCA model to reduce the dimension of training data.

You can perform [batch training](../lvamlconcepts/aml_gettingstarted.html) with this VI when you have a large training data set.

[Examples](#examples)

#### One Shot

[IMAGE alt='image' src='pca.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | PCA settings specifies the method and value for this VI to calculate the number of principal components. criteria specifies the method for this VI to calculate the number of principal components. 0number of components (default)—Directly specifies the number of principal components.1ratio of variance—Specifies the ratio of variance for this VI to calculate the number of principal components. number of components specifies the number of principal components. This input is valid only if criteria is number of components. ratio of variance specifies the ratio of the variance in principal components to the total variance. This VI automatically calculates the number of components. The default is 0.95. This input is valid only if criteria is ratio of variance. |
|  | criteria specifies the method for this VI to calculate the number of principal components. 0number of components (default)—Directly specifies the number of principal components.1ratio of variance—Specifies the ratio of variance for this VI to calculate the number of principal components. |
| 0 | number of components (default)—Directly specifies the number of principal components. |
| 1 | ratio of variance—Specifies the ratio of variance for this VI to calculate the number of principal components. |
|  | number of components specifies the number of principal components. This input is valid only if criteria is number of components. |
|  | ratio of variance specifies the ratio of the variance in principal components to the total variance. This VI automatically calculates the number of components. The default is 0.95. This input is valid only if criteria is ratio of variance. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | PCA model info returns the information about the PCA model. Wire PCA model info to the reference input of a standard Property Node to get an AML PCA Property Node. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Batch

[IMAGE alt='image' src='pca_batch.gif']

|  | reset specifies whether to reset the trained model programmatically at run time. The default is FALSE. |
| --- | --- |
|  | model in specifies the information about the entire workflow of the model. |
|  | number of components specifies the number of principal components. The default is 2. number of components must be reasonable to avoid too much memory usage for a single batch. For the first batch data, number of components must be less than or equal to the number of rows in the training data. Starting from the second batch data, number of components can be 1 or any number that fits in the computation capacity. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | PCA model info returns the information about the PCA model. Wire PCA model info to the reference input of a standard Property Node to get an AML PCA Property Node. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the PCA VI:

- Feature Manipulation (Training) VI: labview\examples\AML\Feature Manipulation
- Feature Manipulation (Training) (Batch) VI: labview\examples\AML\Feature Manipulation
- Clustering (Set Parameters, Training) VI: labview\examples\AML\Clustering
- Clustering (Search Parameters, Training) VI: labview\examples\AML\Clustering
- Clustering (Deployment) VI: labview\examples\AML\Clustering

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_pca_prop.html language=enus -->
## TOPIC 00043: AML PCA Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_pca_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_pca_prop.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AML PCA Properties

Wire the **PCA model info** output of the [PCA](aml_pca.html) VI to the **reference** input of a standard Property Node to get an AML PCA Property Node. This Property Node has the following properties:

| Property | Access | Data Type | Description |
| --- | --- | --- | --- |
| Eigenvectors | Read Only |  | Returns the eigenvectors to calculate the principal components. The number of rows equals the number of features of the training data. The PCA model uses a subset of the eigenvectors of the covariance matrix to calculate the principal components in the input data. |
| Mean Values | Read Only |  | Returns the mean values of all features in the data. |
| Number of Selected Components | Read Only |  | Returns the number of principal components, when you perform one shot training. |
| PCA Settings | Read Only |  | Returns the method and value to calculate the number of principal components, when you perform one shot training. |
| Variance | Read Only |  | Returns the variance of the principal components. The number of rows equals the number of principal components. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_props.html language=enus -->
## TOPIC 00044: Analytics and Machine Learning Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_props.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_props.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Analytics and Machine Learning Properties

Use the following properties with the Property Node to access Analytics and Machine Learning data.

[AML Analytics Properties](aml_analyticsmodel_prop.html)

[AML Anomaly Detection Properties](aml_anomalydetectionmodel_prop.html)

[AML Classification Properties](aml_classificationmodel_prop.html)

[AML Clustering Properties](aml_clusteringmodel_prop.html)

[AML Fisher Properties](aml_fisher_prop.html)

[AML GMM Properties](aml_gmm_prop.html)

[AML GMM-CV Properties](aml_gmmcv_prop.html)

[AML KPCA Properties](aml_kpca_prop.html)

[AML K-Means Properties](aml_kmeans_prop.html)

[AML Logistic Regression Properties](aml_logisticregression.html)

[AML Neural Network Properties](aml_neuralnetwork.html)

[AML Normalize Properties](aml_normalize_prop.html)

[AML DBSCAN Properties](aml_dbscan_prop.html)

[AML One-Class SVM Properties](aml_oneclasssvm_prop.html)

[AML PCA Properties](aml_pca_prop.html)

[AML PCA T2Q Properties](aml_amlpcat2q_prop.html)

[AML SOM-MQE Properties](aml_sommqe_prop.html)

[AML SVM Properties](aml_svm.html)

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_read_data.html language=enus -->
## TOPIC 00045: Read Data (2D Array) VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_read_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_read_data.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Read Data (2D Array) VI

**Owning Palette:** [Data VIs](../lvaml/aml_data.html)

**Requires:** Analytics and Machine Learning Toolkit

Reads data and labels. Use this VI to read and view transformed data from the Feature Manipulation VIs.

[IMAGE alt='image' src='read_data__2d_array.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | data returns data that this VI reads. |
|  | data labels returns data labels. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_set_anomaly_detection_model.html language=enus -->
## TOPIC 00046: Set Anomaly Detection Model VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_set_anomaly_detection_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_set_anomaly_detection_model.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Set Anomaly Detection Model VI

**Owning Palette:** [Anomaly Detection VIs](../lvaml/aml_anomaly_detection.html)

**Requires:** Analytics and Machine Learning Toolkit

Sets properties for a trained anomaly detection model before deployment.

#### GMM-CV

[IMAGE alt='image' src='set_anomaly_detection_model__gmm-cv.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | GMM baseline model specifies the properties of the GMM baseline model. The following equation defines the GMM model: where K is the number of Gaussian mixture components. Each Gaussian mixture component represents a Gaussian distribution. μi and Σi are the mean value and the covariance value of the ith Gaussian mixture component αi is the weight of the ith Gaussian mixture component hyperparameters specifies the hyperparameters to calculate the GMM baseline model from the data. auto initialization specifies whether this VI automatically calculates the values in initial parameters using K-Means algorithm. The default is TRUE, which specifies that this VI automatically sets the values in initial parameters using K-Means algorithm. If you do not specify values for the arrays in initial parameters and auto initialization is FALSE, this VI randomly calculates the values in initial parameters. initial mean values specifies the initial mean values of all Gaussian distributions in the GMM model that this VI calculates. initial covariance values specifies the initial covariance values of all Gaussian distributions in the GMM model that this VI calculates. initial covariance matrix specifies the initial covariance matrix of each Gaussian distribution in the GMM model. initial weights specifies the initial weights of all Gaussian distributions in the GMM model that this VI calculates. number of clusters specifies the number of Gaussian distributions in the GMM model that this VI calculates. regulator specifies the value that this VI adds to covariance to prevent the covariance matrix from converging to 0. tolerance specifies the tolerance for the stopping criteria. max iteration specifies the maximum number of optimization iterations for the stopping criteria. The model fitting stops if the number of optimization iterations reaches max iteration. baseline model specifies the properties of the trained GMM baseline model. weights specifies the weights of all Gaussian distributions in the trained GMM baseline model. The number of rows must equal number of clusters. covariance values specifies the covariance values of all Gaussian distributions in the trained GMM baseline model. The array size must equal number of clusters. covariance matrix specifies the covariance matrix of all Gaussian distributions in the GMM baseline model. mean values specifies the mean values of all Gaussian distributions in the trained GMM baseline model. The number of rows must equal number of clusters. |
| where |  |
|  | K is the number of Gaussian mixture components. Each Gaussian mixture component represents a Gaussian distribution. |
|  | μi and Σi are the mean value and the covariance value of the ith Gaussian mixture component |
|  | αi is the weight of the ith Gaussian mixture component |
|  | hyperparameters specifies the hyperparameters to calculate the GMM baseline model from the data. auto initialization specifies whether this VI automatically calculates the values in initial parameters using K-Means algorithm. The default is TRUE, which specifies that this VI automatically sets the values in initial parameters using K-Means algorithm. If you do not specify values for the arrays in initial parameters and auto initialization is FALSE, this VI randomly calculates the values in initial parameters. initial mean values specifies the initial mean values of all Gaussian distributions in the GMM model that this VI calculates. initial covariance values specifies the initial covariance values of all Gaussian distributions in the GMM model that this VI calculates. initial covariance matrix specifies the initial covariance matrix of each Gaussian distribution in the GMM model. initial weights specifies the initial weights of all Gaussian distributions in the GMM model that this VI calculates. number of clusters specifies the number of Gaussian distributions in the GMM model that this VI calculates. regulator specifies the value that this VI adds to covariance to prevent the covariance matrix from converging to 0. tolerance specifies the tolerance for the stopping criteria. max iteration specifies the maximum number of optimization iterations for the stopping criteria. The model fitting stops if the number of optimization iterations reaches max iteration. |
|  | auto initialization specifies whether this VI automatically calculates the values in initial parameters using K-Means algorithm. The default is TRUE, which specifies that this VI automatically sets the values in initial parameters using K-Means algorithm. If you do not specify values for the arrays in initial parameters and auto initialization is FALSE, this VI randomly calculates the values in initial parameters. |
|  | initial mean values specifies the initial mean values of all Gaussian distributions in the GMM model that this VI calculates. |
|  | initial covariance values specifies the initial covariance values of all Gaussian distributions in the GMM model that this VI calculates. initial covariance matrix specifies the initial covariance matrix of each Gaussian distribution in the GMM model. |
|  | initial covariance matrix specifies the initial covariance matrix of each Gaussian distribution in the GMM model. |
|  | initial weights specifies the initial weights of all Gaussian distributions in the GMM model that this VI calculates. |
|  | number of clusters specifies the number of Gaussian distributions in the GMM model that this VI calculates. |
|  | regulator specifies the value that this VI adds to covariance to prevent the covariance matrix from converging to 0. |
|  | tolerance specifies the tolerance for the stopping criteria. |
|  | max iteration specifies the maximum number of optimization iterations for the stopping criteria. The model fitting stops if the number of optimization iterations reaches max iteration. |
|  | baseline model specifies the properties of the trained GMM baseline model. weights specifies the weights of all Gaussian distributions in the trained GMM baseline model. The number of rows must equal number of clusters. covariance values specifies the covariance values of all Gaussian distributions in the trained GMM baseline model. The array size must equal number of clusters. covariance matrix specifies the covariance matrix of all Gaussian distributions in the GMM baseline model. mean values specifies the mean values of all Gaussian distributions in the trained GMM baseline model. The number of rows must equal number of clusters. |
|  | weights specifies the weights of all Gaussian distributions in the trained GMM baseline model. The number of rows must equal number of clusters. |
|  | covariance values specifies the covariance values of all Gaussian distributions in the trained GMM baseline model. The array size must equal number of clusters. covariance matrix specifies the covariance matrix of all Gaussian distributions in the GMM baseline model. |
|  | covariance matrix specifies the covariance matrix of all Gaussian distributions in the GMM baseline model. |
|  | mean values specifies the mean values of all Gaussian distributions in the trained GMM baseline model. The number of rows must equal number of clusters. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | error out contains error information. This output provides standard error out functionality. |

#### One-Class SVM

[IMAGE alt='image' src='set_anomaly_detection_model__one-class_svm.gif']

|  | model in specifies the information about the entire workflow of the model. |  |
| --- | --- | --- |
|  | one-class SVM model specifies the properties of the one-class SVM model. The following equation defines the one-class SVM model decision function: where sgn is the sign function l is the number of support vectors αi is the coefficient of the support vector xi is the support vector x is the test data K(xi, x) is the kernel function of xi and x. Available kernel function types include linear, polynomial, radial basis, and sigmoid. ρ is the decision function constant kernel settings specifies settings to configure the kernel function. This VI supports the following kernel functions: Kernel functionDefinitionDescription Linear functionx and y are the input sample vectors. Polynomial functionx and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. Radial basis functionx and y are the input sample vectors. Sigmoid functionx and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. type specifies the type of the kernel function. 0Linear—Linear function 1Polynomial—Polynomial function 2RBF—Radial basis function 3Sigmoid—Sigmoid function degree specifies the degree of the kernel. gamma specifies the gamma of the kernel. coef0 specifies the coef0 of the kernel. number of support vectors specifies the number of support vectors. support vectors specifies the support vectors. The number of rows must equal the number of support vectors and the number of columns must equal the number of features. coefficients of support vectors specifies the coefficients of support vectors. The format of coefficients of support vectors is <number of classes - 1, number of support vectors>. decision function constants specifies the decision function constants. |  |
| where |  |  |
|  | sgn is the sign function |  |
|  | l is the number of support vectors |  |
|  | αi is the coefficient of the support vector |  |
|  | xi is the support vector |  |
|  | x is the test data |  |
|  | K(xi, x) is the kernel function of xi and x. Available kernel function types include linear, polynomial, radial basis, and sigmoid. |  |
|  | ρ is the decision function constant |  |
|  | kernel settings specifies settings to configure the kernel function. This VI supports the following kernel functions: Kernel functionDefinitionDescription Linear functionx and y are the input sample vectors. Polynomial functionx and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. Radial basis functionx and y are the input sample vectors. Sigmoid functionx and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. type specifies the type of the kernel function. 0Linear—Linear function 1Polynomial—Polynomial function 2RBF—Radial basis function 3Sigmoid—Sigmoid function degree specifies the degree of the kernel. gamma specifies the gamma of the kernel. coef0 specifies the coef0 of the kernel. |  |
| Kernel function | Definition | Description |
| Linear function |  | x and y are the input sample vectors. |
| Polynomial function |  | x and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. |
| Radial basis function |  | x and y are the input sample vectors. |
| Sigmoid function |  | x and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. |
|  | type specifies the type of the kernel function. 0Linear—Linear function 1Polynomial—Polynomial function 2RBF—Radial basis function 3Sigmoid—Sigmoid function |  |
| 0 | Linear—Linear function |  |
| 1 | Polynomial—Polynomial function |  |
| 2 | RBF—Radial basis function |  |
| 3 | Sigmoid—Sigmoid function |  |
|  | degree specifies the degree of the kernel. |  |
|  | gamma specifies the gamma of the kernel. |  |
|  | coef0 specifies the coef0 of the kernel. |  |
|  | number of support vectors specifies the number of support vectors. |  |
|  | support vectors specifies the support vectors. The number of rows must equal the number of support vectors and the number of columns must equal the number of features. |  |
|  | coefficients of support vectors specifies the coefficients of support vectors. The format of coefficients of support vectors is <number of classes - 1, number of support vectors>. |  |
|  | decision function constants specifies the decision function constants. |  |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |  |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |  |
|  | error out contains error information. This output provides standard error out functionality. |  |

#### PCA T2Q

[IMAGE alt='image' src='set_anomaly_detection_model__pca_t2q.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | PCA baseline model specifies the properties of the PCA baseline model. mean values specifies the mean value of each feature in the training data. eigenvectors specifies the eigenvectors to calculate the principal components. The number of rows must equal the number of features of the training data. variance specifies the variance of the principal components. The number of rows must equal the number of principal components. threshold for T2 specifies the threshold for T2 that you can use to determine whether the T2 values of the data for deployment are abnormal. threshold for Q specifies the threshold for Q that you can use to determine whether the Q values of the data for deployment are abnormal. |
|  | mean values specifies the mean value of each feature in the training data. |
|  | eigenvectors specifies the eigenvectors to calculate the principal components. The number of rows must equal the number of features of the training data. |
|  | variance specifies the variance of the principal components. The number of rows must equal the number of principal components. |
|  | threshold for T2 specifies the threshold for T2 that you can use to determine whether the T2 values of the data for deployment are abnormal. |
|  | threshold for Q specifies the threshold for Q that you can use to determine whether the Q values of the data for deployment are abnormal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | error out contains error information. This output provides standard error out functionality. |

#### SOM-MQE

[IMAGE alt='image' src='set_anomaly_detection_model__som-mqe.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | SOM baseline model specifies the properties of the SOM baseline model. map vectors specifies the map vectors of the trained SOM baseline model. MQE threshold specifies the MQE threshold that you can use to determine whether the MQE values of the data for deployment are abnormal. map structure specifies the structure of the SOM baseline model. row specifies the number of rows of the SOM baseline model. column specifies the number of columns of the SOM baseline model. lattice type specifies the lattice type of the SOM baseline model. 0rectangular (default) 1hexagonal The following figure shows the rectangular lattice: The following figure shows the hexagonal lattice: |
|  | map vectors specifies the map vectors of the trained SOM baseline model. |
|  | MQE threshold specifies the MQE threshold that you can use to determine whether the MQE values of the data for deployment are abnormal. |
|  | map structure specifies the structure of the SOM baseline model. row specifies the number of rows of the SOM baseline model. column specifies the number of columns of the SOM baseline model. lattice type specifies the lattice type of the SOM baseline model. 0rectangular (default) 1hexagonal The following figure shows the rectangular lattice: The following figure shows the hexagonal lattice: |
|  | row specifies the number of rows of the SOM baseline model. |
|  | column specifies the number of columns of the SOM baseline model. |
|  | lattice type specifies the lattice type of the SOM baseline model. 0rectangular (default) 1hexagonal The following figure shows the rectangular lattice: The following figure shows the hexagonal lattice: |
| 0 | rectangular (default) |
| 1 | hexagonal |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_set_classification_model.html language=enus -->
## TOPIC 00047: Set Classification Model VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_set_classification_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_set_classification_model.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Set Classification Model VI

**Owning Palette:** [Classification VIs](../lvaml/aml_classification.html)

**Requires:** Analytics and Machine Learning Toolkit

Sets properties for a trained classification model before deployment.

#### SVM

[IMAGE alt='image' src='set_classification_model__svm.gif']

|  | model in specifies the information about the entire workflow of the model. |  |
| --- | --- | --- |
|  | SVM model specifies the information about the trained SVM model. The following equation defines the SVM model decision function: where sgn is the sign function l is the number of support vectors yi is the label of the support vector αi is the coefficient of the support vector xi is the support vector x is the input data K(xi, x) is the kernel function of xi and x. Available kernel function types include linear, polynomial, radial basis, and sigmoid. ρ is the decision function constant kernel settings specifies settings to configure the kernel function. This VI supports the following kernel functions: Kernel functionDefinitionDescription Linear functionx and y are the input sample vectors. Polynomial functionx and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. Radial basis functionx and y are the input sample vectors. Sigmoid functionx and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. type specifies the type of the kernel function. 0Linear—Linear function 1Polynomial—Polynomial function 2RBF—Radial basis function 3Sigmoid—Sigmoid function degree specifies the degree coefficient of the kernel function. gamma specifies the gamma coefficient of the kernel function. coef0 specifies the coef0 coefficient of the kernel function. number of classes specifies the number of classes. label of each class specifies the label of each class. number of support vectors specifies the number of support vectors. support vectors specifies the support vectors. The number of rows must equal the number of support vectors and the number of columns must equal the number of features. coefficients of support vectors specifies the coefficients of support vectors. The format of coefficients of support vectors is <number of classes - 1, number of support vectors>. decision function constants specifies the decision function constants. pairwise probability specifies the estimated probabilities of the classes in the trained SVM model. probA specifies the estimated probability of a specific class in the trained SVM model. probB specifies the estimated probability of a specific class in the trained SVM model. number of support vectors for each class specifies the number of support vectors for each class. |  |
| where |  |  |
|  | sgn is the sign function |  |
|  | l is the number of support vectors |  |
|  | yi is the label of the support vector |  |
|  | αi is the coefficient of the support vector |  |
|  | xi is the support vector |  |
|  | x is the input data |  |
|  | K(xi, x) is the kernel function of xi and x. Available kernel function types include linear, polynomial, radial basis, and sigmoid. |  |
|  | ρ is the decision function constant |  |
|  | kernel settings specifies settings to configure the kernel function. This VI supports the following kernel functions: Kernel functionDefinitionDescription Linear functionx and y are the input sample vectors. Polynomial functionx and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. Radial basis functionx and y are the input sample vectors. Sigmoid functionx and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. type specifies the type of the kernel function. 0Linear—Linear function 1Polynomial—Polynomial function 2RBF—Radial basis function 3Sigmoid—Sigmoid function degree specifies the degree coefficient of the kernel function. gamma specifies the gamma coefficient of the kernel function. coef0 specifies the coef0 coefficient of the kernel function. |  |
| Kernel function | Definition | Description |
| Linear function |  | x and y are the input sample vectors. |
| Polynomial function |  | x and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. |
| Radial basis function |  | x and y are the input sample vectors. |
| Sigmoid function |  | x and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. |
|  | type specifies the type of the kernel function. 0Linear—Linear function 1Polynomial—Polynomial function 2RBF—Radial basis function 3Sigmoid—Sigmoid function |  |
| 0 | Linear—Linear function |  |
| 1 | Polynomial—Polynomial function |  |
| 2 | RBF—Radial basis function |  |
| 3 | Sigmoid—Sigmoid function |  |
|  | degree specifies the degree coefficient of the kernel function. |  |
|  | gamma specifies the gamma coefficient of the kernel function. |  |
|  | coef0 specifies the coef0 coefficient of the kernel function. |  |
|  | number of classes specifies the number of classes. |  |
|  | label of each class specifies the label of each class. |  |
|  | number of support vectors specifies the number of support vectors. |  |
|  | support vectors specifies the support vectors. The number of rows must equal the number of support vectors and the number of columns must equal the number of features. |  |
|  | coefficients of support vectors specifies the coefficients of support vectors. The format of coefficients of support vectors is <number of classes - 1, number of support vectors>. |  |
|  | decision function constants specifies the decision function constants. |  |
|  | pairwise probability specifies the estimated probabilities of the classes in the trained SVM model. probA specifies the estimated probability of a specific class in the trained SVM model. probB specifies the estimated probability of a specific class in the trained SVM model. |  |
|  | probA specifies the estimated probability of a specific class in the trained SVM model. |  |
|  | probB specifies the estimated probability of a specific class in the trained SVM model. |  |
|  | number of support vectors for each class specifies the number of support vectors for each class. |  |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |  |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |  |
|  | error out contains error information. This output provides standard error out functionality. |  |

#### Neural Network

[IMAGE alt='image' src='set_classification_model__nn.gif']

|  | model in specifies the information about the entire workflow of the model. |  |
| --- | --- | --- |
|  | neural network model specifies the information about the trained neural network model. This VI supports single hidden layers only. number of classes specifies the number of classes. label of each class specifies the label of each class. number of input neurons specifies the number of neurons in the input layer. number of hidden neurons specifies the number of neurons in the hidden layer. number of output neurons specifies the number of neurons in the output layer. hidden layer type specifies the activation function type in the neurons of the hidden layer. This VI supports the following activation functions for the hidden layer: Function typeDefinitionDescription Sigmoid functionx is the activation value of the hidden neuron. Tanh functionx is the activation value of the hidden neuron. Rectified linear unit functionx is the activation value of the hidden neuron. 0Sigmoid (default)—Sigmoid function1Tanh—Tanh function2ReLU—Rectified linear unit function output layer type specifies the activation function type in the neurons of the output layer. This VI supports the following activation functions for the output layer: Function typeDefinitionDescription Sigmoid functionx is the activation value of the output neuron. Softmax functionx is the activation value of the output neuron and n is the number of classes. 0Sigmoid (default)—Sigmoid function1Softmax—Softmax function I to H coefficients specifies the trained coefficients between the input layer and the hidden layer. H to O coefficients specifies the trained coefficients between the hidden layer and the output layer. |  |
|  | number of classes specifies the number of classes. |  |
|  | label of each class specifies the label of each class. |  |
|  | number of input neurons specifies the number of neurons in the input layer. |  |
|  | number of hidden neurons specifies the number of neurons in the hidden layer. |  |
|  | number of output neurons specifies the number of neurons in the output layer. |  |
|  | hidden layer type specifies the activation function type in the neurons of the hidden layer. This VI supports the following activation functions for the hidden layer: Function typeDefinitionDescription Sigmoid functionx is the activation value of the hidden neuron. Tanh functionx is the activation value of the hidden neuron. Rectified linear unit functionx is the activation value of the hidden neuron. 0Sigmoid (default)—Sigmoid function1Tanh—Tanh function2ReLU—Rectified linear unit function |  |
| Function type | Definition | Description |
| Sigmoid function |  | x is the activation value of the hidden neuron. |
| Tanh function |  | x is the activation value of the hidden neuron. |
| Rectified linear unit function |  | x is the activation value of the hidden neuron. |
| 0 | Sigmoid (default)—Sigmoid function |  |
| 1 | Tanh—Tanh function |  |
| 2 | ReLU—Rectified linear unit function |  |
|  | output layer type specifies the activation function type in the neurons of the output layer. This VI supports the following activation functions for the output layer: Function typeDefinitionDescription Sigmoid functionx is the activation value of the output neuron. Softmax functionx is the activation value of the output neuron and n is the number of classes. 0Sigmoid (default)—Sigmoid function1Softmax—Softmax function |  |
| Function type | Definition | Description |
| Sigmoid function |  | x is the activation value of the output neuron. |
| Softmax function |  | x is the activation value of the output neuron and n is the number of classes. |
| 0 | Sigmoid (default)—Sigmoid function |  |
| 1 | Softmax—Softmax function |  |
|  | I to H coefficients specifies the trained coefficients between the input layer and the hidden layer. |  |
|  | H to O coefficients specifies the trained coefficients between the hidden layer and the output layer. |  |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |  |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |  |
|  | error out contains error information. This output provides standard error out functionality. |  |

#### Logistic Regression

[IMAGE alt='image' src='set_classification_model__lr.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | logistic regression model specifies the information about the trained logistic regression model. The following equation defines the logistic regression model: where x is the input with k + 1 dimensions. x0 is always 1. y is the output with a binary value 0 or 1 β is the weight vector with k + 1 dimensions. Specify the value of β by using coefficients P (y = 1\|x) is the probability of y = 1 given a known instance of x number of classes specifies the number of classes. label of each class specifies the label of each class. coefficients specifies the trained coefficients of the trained logistic regression model. |
| where |  |
|  | x is the input with k + 1 dimensions. x0 is always 1. |
|  | y is the output with a binary value 0 or 1 |
|  | β is the weight vector with k + 1 dimensions. Specify the value of β by using coefficients |
|  | P (y = 1\|x) is the probability of y = 1 given a known instance of x |
|  | number of classes specifies the number of classes. |
|  | label of each class specifies the label of each class. |
|  | coefficients specifies the trained coefficients of the trained logistic regression model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_set_clustering_model.html language=enus -->
## TOPIC 00048: Set Clustering Model VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_set_clustering_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_set_clustering_model.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Set Clustering Model VI

**Owning Palette:** [Clustering VIs](../lvaml/aml_clustering.html)

**Requires:** Analytics and Machine Learning Toolkit

Sets properties for a trained clustering model before deployment.

#### K-Means

[IMAGE alt='image' src='set_clustering_model__k-means.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | K-Means model specifies the information about the trained K-Means model. number of clusters specifies the number of clusters in the trained K-Means model. centroids specifies the centroids of all clusters in the trained K-Means model. The number of rows must equal number of clusters and the number of columns must equal the number of features in the training data. |
|  | number of clusters specifies the number of clusters in the trained K-Means model. |
|  | centroids specifies the centroids of all clusters in the trained K-Means model. The number of rows must equal number of clusters and the number of columns must equal the number of features in the training data. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | error out contains error information. This output provides standard error out functionality. |

#### GMM

[IMAGE alt='image' src='set_clustering_model__gmm.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | GMM model specifies the information about the trained GMM model. number of clusters specifies the number of Gaussian distributions in the trained GMM model. mean values specifies the mean values of all Gaussian distributions in the trained GMM model. The number of rows must equal number of clusters. covariance values specifies the covariance values of all Gaussian distributions in the trained GMM model. The array size must equal number of clusters. covariance matrix specifies the covariance matrix for each Gaussian distribution in the GMM model. weights specifies the weights of all Gaussian distributions in the trained GMM model. The number of rows must equal number of clusters. |
|  | number of clusters specifies the number of Gaussian distributions in the trained GMM model. |
|  | mean values specifies the mean values of all Gaussian distributions in the trained GMM model. The number of rows must equal number of clusters. |
|  | covariance values specifies the covariance values of all Gaussian distributions in the trained GMM model. The array size must equal number of clusters. covariance matrix specifies the covariance matrix for each Gaussian distribution in the GMM model. |
|  | covariance matrix specifies the covariance matrix for each Gaussian distribution in the GMM model. |
|  | weights specifies the weights of all Gaussian distributions in the trained GMM model. The number of rows must equal number of clusters. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | error out contains error information. This output provides standard error out functionality. |

#### DBSCAN

[IMAGE alt='image' src='set_clustering_model__dbscan.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | DBSCAN model specifies the information about the trained DBSCAN model. max distance specifies the maximum radius for a sample to form a neighborhood. The default is 1. p specifies the power of the Minkowski metric that this VI uses to calculate distances between points. The default is 2. The following equation defines the Minkowski metric: where [x1, x2, …, xN] is the input feature vector and [core sample1, core sample2, …, core sampleN] is the core sample feature vector. core samples specifies the core samples from the trained DBSCAN model. core samples labels specifies the label of each core sample. |
|  | max distance specifies the maximum radius for a sample to form a neighborhood. The default is 1. |
|  | p specifies the power of the Minkowski metric that this VI uses to calculate distances between points. The default is 2. The following equation defines the Minkowski metric: where [x1, x2, …, xN] is the input feature vector and [core sample1, core sample2, …, core sampleN] is the core sample feature vector. |
|  | core samples specifies the core samples from the trained DBSCAN model. |
|  | core samples labels specifies the label of each core sample. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_set_feature_manipulation_model.html language=enus -->
## TOPIC 00049: Set Feature Manipulation Model VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_set_feature_manipulation_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_set_feature_manipulation_model.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Set Feature Manipulation Model VI

**Owning Palette:** [Feature Manipulation VIs](../lvaml/aml_feature_manipulation.html)

**Requires:** Analytics and Machine Learning Toolkit

Sets properties for a trained feature manipulation model before deployment.

#### Normalize

[IMAGE alt='image' src='set_normalize_model.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | normalization model specifies the properties of the trained normalization model. normalization settings specifies the settings of normalization. transformation method specifies the method of normalization. 0ZScore—Normalizes the data so that the data has a mean of 0 and a variance of 1.1MinMax—Normalizes the data so that the data is in the range that range settings defines. range settings specifies the range of normalization for the MinMax method. This input is valid only if transformation method is MinMax. max specifies the maximum value of the normalized data. min specifies the minimum value of the normalized data. mean values specifies the mean values of all features in the training data for the Z-Score method. This input is valid only if transformation method is ZScore. standard deviation values specifies the standard deviation values of all features in the training data for the ZScore method. This input is valid only if transformation method is ZScore. min values specifies the minimum values of all features in the training data for the Min-Max method. This input is valid only if transformation method is MinMax. max values specifies the maximum values of all features in the training data for the Min-Max method. This input is valid only if transformation method is MinMax. |
|  | normalization settings specifies the settings of normalization. transformation method specifies the method of normalization. 0ZScore—Normalizes the data so that the data has a mean of 0 and a variance of 1.1MinMax—Normalizes the data so that the data is in the range that range settings defines. range settings specifies the range of normalization for the MinMax method. This input is valid only if transformation method is MinMax. max specifies the maximum value of the normalized data. min specifies the minimum value of the normalized data. |
|  | transformation method specifies the method of normalization. 0ZScore—Normalizes the data so that the data has a mean of 0 and a variance of 1.1MinMax—Normalizes the data so that the data is in the range that range settings defines. |
| 0 | ZScore—Normalizes the data so that the data has a mean of 0 and a variance of 1. |
| 1 | MinMax—Normalizes the data so that the data is in the range that range settings defines. |
|  | range settings specifies the range of normalization for the MinMax method. This input is valid only if transformation method is MinMax. max specifies the maximum value of the normalized data. min specifies the minimum value of the normalized data. |
|  | max specifies the maximum value of the normalized data. |
|  | min specifies the minimum value of the normalized data. |
|  | mean values specifies the mean values of all features in the training data for the Z-Score method. This input is valid only if transformation method is ZScore. |
|  | standard deviation values specifies the standard deviation values of all features in the training data for the ZScore method. This input is valid only if transformation method is ZScore. |
|  | min values specifies the minimum values of all features in the training data for the Min-Max method. This input is valid only if transformation method is MinMax. |
|  | max values specifies the maximum values of all features in the training data for the Min-Max method. This input is valid only if transformation method is MinMax. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Fisher

[IMAGE alt='image' src='set_fisher_model.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | selected feature index specifies the indexes of selected features. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | error out contains error information. This output provides standard error out functionality. |

#### PCA

[IMAGE alt='image' src='set_pca_model.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | PCA Model specifies the properties of the trained PCA model. mean values specifies the mean values of all features in the training data. eigenvectors specifies the eigenvectors to calculate the principal components. |
|  | mean values specifies the mean values of all features in the training data. |
|  | eigenvectors specifies the eigenvectors to calculate the principal components. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | error out contains error information. This output provides standard error out functionality. |

#### KPCA

[IMAGE alt='image' src='set_kpca_model.gif']

|  | model in specifies the information about the entire workflow of the model. |  |
| --- | --- | --- |
|  | KPCA Model specifies the properties of the trained KPCA model. kernel settings specifies the settings to configure the kernel function. This VI supports the following kernel functions: Kernel functionDefinitionDescription Polynomial functionx and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. Radial basis functionx and y are the input sample vectors. Sigmoid functionx and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. type specifies the type of the kernel function. 0Polynomial—Polynomial function1RBF—Radial basis function2Sigmoid—Sigmoid function degree specifies the degree coefficient of the kernel function. gamma specifies the gamma coefficient of the kernel function. coef0 specifies the coef0 coefficient of the kernel function. variance specifies the variance of the principal components. source data specifies the training data for the KPCA model. eigenvectors specifies the eigenvectors to calculate the principal components. |  |
|  | kernel settings specifies the settings to configure the kernel function. This VI supports the following kernel functions: Kernel functionDefinitionDescription Polynomial functionx and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. Radial basis functionx and y are the input sample vectors. Sigmoid functionx and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. type specifies the type of the kernel function. 0Polynomial—Polynomial function1RBF—Radial basis function2Sigmoid—Sigmoid function degree specifies the degree coefficient of the kernel function. gamma specifies the gamma coefficient of the kernel function. coef0 specifies the coef0 coefficient of the kernel function. |  |
| Kernel function | Definition | Description |
| Polynomial function |  | x and y are the input sample vectors; gamma, coef0, and degree are the algorithm coefficients. |
| Radial basis function |  | x and y are the input sample vectors. |
| Sigmoid function |  | x and y are the input sample vectors; gamma and coef0 are the algorithm coefficients. |
|  | type specifies the type of the kernel function. 0Polynomial—Polynomial function1RBF—Radial basis function2Sigmoid—Sigmoid function |  |
| 0 | Polynomial—Polynomial function |  |
| 1 | RBF—Radial basis function |  |
| 2 | Sigmoid—Sigmoid function |  |
|  | degree specifies the degree coefficient of the kernel function. |  |
|  | gamma specifies the gamma coefficient of the kernel function. |  |
|  | coef0 specifies the coef0 coefficient of the kernel function. |  |
|  | variance specifies the variance of the principal components. |  |
|  | source data specifies the training data for the KPCA model. |  |
|  | eigenvectors specifies the eigenvectors to calculate the principal components. |  |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |  |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |  |
|  | error out contains error information. This output provides standard error out functionality. |  |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_sommqe_prop.html language=enus -->
## TOPIC 00050: AML SOM-MQE Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_sommqe_prop.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_sommqe_prop.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AML SOM-MQE Properties

Wire the **untrained SOM baseline model** output of the [Initialize Anomaly Detection Model (PCA T2Q)](aml_initialize_anomaly_detection_model_pca_t2q.html) VI to the **reference** input of a standard Property Node to get an AML PCA T2Q Property Node. This Property Node has the following properties:

| Property | Access | Data Type | Description |
| --- | --- | --- | --- |
| Hyperparameters | Read Only |  | Returns the hyperparameters of the SOM baseline model. |
| Model Initialized? | Read Only |  | Returns whether the model is initialized. |
| Model Trained? | Read Only |  | Returns whether the model is trained. |
| MQE Threshold | Read Only |  | Returns the MQE threshold based on confidence level. You can use the MQE threshold to detect whether the MQE values of the data for deployment are abnormal. |
| Trained Map Vectors | Read Only |  | Returns the map vectors of the trained SOM baseline model. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_svm.html language=enus -->
## TOPIC 00051: AML SVM Properties

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_svm.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_svm.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### AML SVM Properties

Wire the **untrained SVM model** output of the [Initialize Classification Model (SVM)](aml_initialize_classification_model_svm.html) VI to the **reference** input of a standard Property Node to get an AML SVM Property Node. This Property Node has the following properties:

| Property | Access | Data Type | Description |
| --- | --- | --- | --- |
| Coefficients of Support Vectors | Read Only |  | Returns the coefficients of support vectors. |
| Cross Validation Configuration | Read Only |  | Returns settings for cross validation. |
| Decision Function Constants | Read Only |  | Returns the decision function constants. |
| Hyperparameters | Read Only |  | If you select the Set Parameters instance the Initialize Classification Model (SVM) VI, this property returns the hyperparameters input of the VI. If you select the Search Parameters instance the Initialize Classification Model (SVM) VI, this property returns the optimal hyperparameters after the Train Classification Model VI completes grid search. |
| Hyperparameter Grids | Read Only |  | Returns multiple values for each hyperparameter. |
| Hyperparameter Optimization | Read Only |  | Returns the method of optimization to determine the optimal hyperparameter settings. |
| Label of Each Class | Read Only |  | Returns the label of each class. |
| Indexes of Support Vectors | Read Only |  | Returns the indexes of support vectors that you can use to find support vectors from the training data. |
| Model Initialized? | Read Only |  | Returns whether the model is initialized. |
| Model Trained? | Read Only |  | Returns whether the model is trained. |
| Number of Classes | Read Only |  | Returns the number of classes. |
| Number of Support Vectors | Read Only |  | Returns the number of support vectors. |
| Number of Support Vectors for Each Class | Read Only |  | Returns the number of support vectors for each class. |
| Pairwise Probability | Read Only |  | Returns the estimated probabilities of the classes in the trained SVM model. |
| Support Vectors | Read Only |  | Returns all the support vectors. The number of rows equals the number of vectors and the number of columns equals the number of features. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_train_anomaly_detection_model.html language=enus -->
## TOPIC 00052: Train Anomaly Detection Model VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_train_anomaly_detection_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_train_anomaly_detection_model.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Train Anomaly Detection Model VI

**Owning Palette:** [Anomaly Detection VIs](../lvaml/aml_anomaly_detection.html)

**Requires:** Analytics and Machine Learning Toolkit

Trains an anomaly detection model.

[Examples](#examples)

[IMAGE alt='image' src='train_anomaly_detection_model.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | anomaly detection model info in specifies the initialized anomaly detection model for training. You can acquire an initialized anomaly detection model from the following VIs: Initialize Anomaly Detection Model (GMM-CV) VI Initialize Anomaly Detection Model (One-class SVM) VI Initialize Anomaly Detection Model (PCA T2Q) VI Initialize Anomaly Detection Model (SOM-MQE) VI |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | anomaly detection model info out returns the trained anomaly detection model. Wire anomaly detection model info out to the reference input of a standard Property Node to get the properties of the trained anomaly detection model. The following table displays the VI you wire to anomaly detection model info in and the corresponding Property Node you get from anomaly detection model info out. VI NameProperty Node Initialize Anomaly Detection Model (GMM-CV) VIAML GMM-CV Initialize Anomaly Detection Model (One-Class SVM) VIAML One-Class SVM Initialize Anomaly Detection Model (PCA T2Q) VIAML PCA T2Q Initialize Anomaly Detection Model (SOM-MQE) VIAML SOM-MQE |
| VI Name | Property Node |
| Initialize Anomaly Detection Model (GMM-CV) VI | AML GMM-CV |
| Initialize Anomaly Detection Model (One-Class SVM) VI | AML One-Class SVM |
| Initialize Anomaly Detection Model (PCA T2Q) VI | AML PCA T2Q |
| Initialize Anomaly Detection Model (SOM-MQE) VI | AML SOM-MQE |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Train Anomaly Detection Model VI:

- Anomaly Detection (Training) VI: labview\examples\AML\Anomaly Detection
- Anomaly Detection (Training) (Batch) VI: labview\examples\AML\Anomaly Detection

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_train_classification_model.html language=enus -->
## TOPIC 00053: Train Classification Model VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_train_classification_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_train_classification_model.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Train Classification Model VI

**Owning Palette:** [Classification VIs](../lvaml/aml_classification.html)

**Requires:** Analytics and Machine Learning Toolkit

Trains a classification model.

[Examples](#examples)

[IMAGE alt='image' src='train_classification_model.gif']

|  | model in specifies the information about the entire workflow of the model. |  |  |
| --- | --- | --- | --- |
|  | classification model info in specifies the initialized classification model for training. You can acquire an initialized classification model from the following VIs: Initialize Classification Model (LR) VI Initialize Classification Model (NN) VI Initialize Classification Model (SVM) VI |  |  |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |  |  |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |  |  |
|  | classification model info out returns the trained classification model. Wire classification model info out to the reference input of a standard Property Node to get the properties of the trained classification model. The following table displays the VI you wire to classification model info in and the corresponding Property Node you get from classification model info out. VI NameProperty Node Initialize Classification Model (LR) VIAML Logistic Regression Initialize Classification Model (NN) VIAML Neural Network Initialize Classification Model (SVM) VIAML SVM |  |  |
| VI Name | Property Node |  |  |
| Initialize Classification Model (LR) VI | AML Logistic Regression |  |  |
| Initialize Classification Model (NN) VI | AML Neural Network |  |  |
| Initialize Classification Model (SVM) VI | AML SVM |  |  |
|  | confusion matrix returns the confusion matrix from the evaluation result. A confusion matrix describes the performance of a classification model by reporting the number of true positive cases, true negative cases, false positive cases, and false negative cases. Each row of a confusion matrix represents the actual class and each column represents the predicted class. For example, for 100 samples, there are two possible classes: positive and negative. The following table is a confusion matrix for the two classes. —Predicted Class PositiveNegative Actual ClassPositive655 Negative1911 The confusion matrix contains 65 true positive cases, 5 false negative cases, 19 false positive cases, and 11 true negative cases. |  |  |
| — | Predicted Class |  |  |
| Positive | Negative |  |  |
| Actual Class | Positive | 65 | 5 |
| Negative | 19 | 11 |  |
|  | metrics returns metrics from the evaluation result. accuracy returns the accuracy metric value. The following equation defines the accuracy metric: where TP is the number of true positive cases in the data TN is the number of true negative cases in the data P is the number of real positive cases in the data N is the number of real negative cases in the data precision returns the precision metric value. The following equation defines the precision metric: where TP is the number of true positive cases in the data FP is the number of false positive cases in the data recall returns the recall metric value. The following equation defines the recall metric: where TP is the number of true positive cases in the data FN is the number of false negative cases in the data f1 score returns the f1 score metric value. The following equation defines the f1 score metric: where TP is the number of true positive cases in the data FP is the number of false positive cases in the data FN is the number of false negative cases in the data |  |  |
|  | accuracy returns the accuracy metric value. The following equation defines the accuracy metric: where TP is the number of true positive cases in the data TN is the number of true negative cases in the data P is the number of real positive cases in the data N is the number of real negative cases in the data |  |  |
| where |  |  |  |
|  | TP is the number of true positive cases in the data |  |  |
|  | TN is the number of true negative cases in the data |  |  |
|  | P is the number of real positive cases in the data |  |  |
|  | N is the number of real negative cases in the data |  |  |
|  | precision returns the precision metric value. The following equation defines the precision metric: where TP is the number of true positive cases in the data FP is the number of false positive cases in the data |  |  |
| where |  |  |  |
|  | TP is the number of true positive cases in the data |  |  |
|  | FP is the number of false positive cases in the data |  |  |
|  | recall returns the recall metric value. The following equation defines the recall metric: where TP is the number of true positive cases in the data FN is the number of false negative cases in the data |  |  |
| where |  |  |  |
|  | TP is the number of true positive cases in the data |  |  |
|  | FN is the number of false negative cases in the data |  |  |
|  | f1 score returns the f1 score metric value. The following equation defines the f1 score metric: where TP is the number of true positive cases in the data FP is the number of false positive cases in the data FN is the number of false negative cases in the data |  |  |
| where |  |  |  |
|  | TP is the number of true positive cases in the data |  |  |
|  | FP is the number of false positive cases in the data |  |  |
|  | FN is the number of false negative cases in the data |  |  |
|  | error out contains error information. This output provides standard error out functionality. |  |  |

#### Examples

Refer to the following VIs for examples of using the Train Classification Model VI:

- Classification (Set Parameters, Training) VI: labview\examples\AML\Classification
- Classification (Search Parameters, Training) VI: labview\examples\AML\Classification

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvaml/aml_train_clustering_model.html language=enus -->
## TOPIC 00054: Train Clustering Model VI

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvaml/aml_train_clustering_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvaml/aml_train_clustering_model.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Train Clustering Model VI

**Owning Palette:** [Clustering VIs](../lvaml/aml_clustering.html)

**Requires:** Analytics and Machine Learning Toolkit

Trains a clustering model.

[Example](#examples)

[IMAGE alt='image' src='train_clustering_model.gif']

|  | model in specifies the information about the entire workflow of the model. |
| --- | --- |
|  | clustering model info in specifies the initialized clustering model for training. You can acquire an initialized clustering model from the following VIs: Initialize Clustering Model (DBSCAN) VI Initialize Clustering Model (GMM) VI Initialize Clustering Model (K-Means) VI |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | model out returns the information about the entire workflow of the model. Wire model out to the reference input of a standard Property Node to get an AML Analytics Property Node. |
|  | clustering model info out returns the trained clustering model. Wire clustering model info out to the reference input of a standard Property Node to get the properties of the trained clustering model. The following table displays the VI you wire to clustering model info in and the corresponding Property Node you get from clustering model info out. VI NameProperty Node Initialize Clustering Model (DBSCAN) VIAML DBSCAN Initialize Clustering Model (GMM) VIAML GMM Initialize Clustering Model (K-Means) VIAML K-Means |
| VI Name | Property Node |
| Initialize Clustering Model (DBSCAN) VI | AML DBSCAN |
| Initialize Clustering Model (GMM) VI | AML GMM |
| Initialize Clustering Model (K-Means) VI | AML K-Means |
|  | predicted labels returns the predicted labels of training data. |
|  | metric returns the evaluation metric for the clustering model. This output is valid only if you used hyperparameter optimization to initialize the clustering model. For the Davies Bouldin Index metric, the lower the value of metric, the better the compactness and separation of the clustering model. For the Dunn Index metric, the higher the value of metric, the better the compactness and separation of the clustering model. For the Jaccard Index metric, the higher the value of metric, the better the separation of the clustering model. For the Rand Index metric, the lower the value of metric, the better the separation of the clustering model. For the Akaike Information Criterion (AIC) metric, the lower the value of metric, the better a GMM model is. For the Bayesian Information Criterion (BIC) metric, the lower the value of metric, the better a GMM model is. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the Clustering (Search Parameters, Training) VI in the labview\examples\AML\Clustering directory for an example of using the Train Clustering Model VI.

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvamlconcepts/aml_error_codes.html language=enus -->
## TOPIC 00055: Error Codes (Analytics and Machine Learning Toolkit)

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvamlconcepts/aml_error_codes.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvamlconcepts/aml_error_codes.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Error Codes (Analytics and Machine Learning Toolkit)

The [Analytics and Machine Learning](../lvaml/aml_pal.html) VIs can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| −388414 | The number of rows in the first batch of data must be greater than or equal to number of components. |
| −388413 | The number of columns of mean values must equal the number of columns in the current batch of input data. |
| −388412 | The length of min values or max values must equal the number of features in the current batch of input data. |
| −388411 | The length of mean values must equal the number of features in the current batch of input data. |
| −388410 | The array size of weights or biases must equal the number of hidden layers. The array size of weight or bias must equal the number of neurons in each layer. |
| −388409 | The array size of hidden layer type must equal the array size of number of hidden neurons. |
| −388408 | The model fitting does not converge before reaching the maximum number of iterations. |
| −388407 | The SVM model training fails. Normalize the training data or change the SVM parameters. |
| −388406 | The GMM model training fails. Increase regulator. |
| −388405 | The number of data samples must be greater than 1. |
| −388404 | There must be at least one cluster in predicted labels that has more than one data samples for the Davies Bouldin Index metric and the Dunn Index metric. |
| −388403 | predicted labels must have more than one clusters for the Davies Bouldin Index metric and the Dunn Index metric. |
| −388402 | The number of predicted labels in predicted labels must equal the number of data samples. |
| −388401 | The number of data samples must be no less than the number of clusters. |
| −388400 | The covariance matrix in covariance matrix must be positive definite. |
| −388399 | The covariance matrix in initial covariance matrix must be positive definite. |
| −388397 | The covariance matrix in initial covariance matrix must be symmetric. |
| −388396 | The number of rows or columns of initial covariance matrix must equal the number of features in the training data. |
| −388395 | initial weights must be between 0 and 1. |
| −388394 | The number of columns of initial mean values must equal the number of features in data. |
| −388393 | threshold for T2 must be greater than or equal to 0. |
| −388392 | The wrong Load Data (2D Array) VI instance is used to load data. |
| −388391 | The array length of number of support vectors for each class must equal number of classes. |
| −388390 | You must perform feature manipulation before training clustering, classification, and anomaly detection models. |
| −388389 | nu is invalid. Reduce the value of nu. |
| −388388 | The array size of variance must equal the number of eigenvectors. |
| −388387 | MQE threshold must be greater than or equal to 0. |
| −388386 | The number of features in the input data must equal the number of columns of support vectors. |
| −388385 | The number of nodes, which equals row * column, must equal the number of columns of map vectors. |
| −388384 | confidence level must be greater than 0 and less than 1. |
| −388383 | initial learning rate must be greater than 0. |
| −388382 | initial radius must be greater than 0. |
| −388381 | The value of row and col must be greater than or equal to 0. |
| −388380 | The number of features in the input data must equal the number of features in map vectors. |
| −388379 | covariance matrix must be symmetric. |
| −388378 | You must not choose the AIC metric or the BIC metric to evaluate the DBSCAN model and the K-Means model. |
| −388377 | threshold for Q must be greater than or equal to 0. |
| −388376 | The number of columns of the input data must equal the number of columns of centroids. |
| −388375 | The number of columns of the input data must equal the number of columns of core samples. |
| −388374 | The number of columns of the input data must equal the number of columns of mean values. |
| −388372 | The size of predicted labels must equal the size of input labels. |
| −388371 | centroids must not be empty and the number of rows of centroids must equal number of clusters. |
| −388370 | The size of covariance values must equal number of clusters and the number of rows/columns of covariance matrix must equal the size of mean values. |
| −388369 | The size of weights must equal number of clusters and the sum of weights must equal 1. |
| −388368 | The number of rows of mean values must equal number of clusters. |
| −388367 | The size of core samples labels must be greater than 0. |
| −388366 | max must be greater than min. |
| −388365 | The size of core sample labels must equal the number of rows of core samples. |
| −388364 | initial method must not be empty. |
| −388362 | attempts must be greater than 0. |
| −388361 | p must be greater than 0. |
| −388360 | min samples must be greater than 0. |
| −388359 | max distance must be greater than 0. |
| −388358 | number of clusters must be greater than 0. |
| −388357 | regulator must be greater than 0. |
| −388356 | Out of memory. |
| −388355 | The sum of number of support vectors for each class must equal number of support vectors. |
| −388354 | output layer type is empty. |
| −388353 | The array size of probB must equal number of classes * (number of classes - 1)/2. |
| −388352 | The array size of probA must equal number of classes * (number of classes - 1)/2. |
| −388351 | The array size of decision function constants must equal number of classes * (number of classes - 1)/2. |
| −388350 | The number of rows of coefficients of support vectors must be one less than number of classes, and the number of columns of coefficients of support vectors must equal number of support vectors. |
| −388349 | The number of rows of support vectors must equal number of support vectors. |
| −388348 | number of support vectors must be greater than 0. |
| −388347 | The number of rows of H to O coefficients must equal number of output neurons, and the number of columns of H to O coefficients must be one greater than number of hidden neurons. |
| −388346 | The number of rows of I to H coefficients must equal number of hidden neurons, and the number of columns of I to H coefficients must be one greater than number of input neurons. |
| −388345 | number of output neurons must equal number of classes. |
| −388344 | The number of features in the input data must equal number of input neurons. |
| −388343 | number of input neurons must be greater than 0. |
| −388342 | For multi-class classification, the number of rows of coefficients of support vectors must equal number of classes. For two-class classification, the number of rows of coefficients of support vectors must equal 1. |
| −388341 | The array size of labels of each class must equal number of classes. |
| −388340 | number of classes must be greater than 1. |
| −388339 | The number of features in the input data must be one less than the number of columns of coefficients of support vectors. |
| −388338 | The model is untrained before deployment. |
| −388337 | cost function type must not be empty. |
| −388336 | You must initialize the model before training. |
| −388335 | coef0 must not be empty. |
| −388334 | kernel type must not be empty. |
| −388333 | SVM type must not be empty. |
| −388332 | hidden layer type must not be empty. |
| −388331 | There are repeated class labels in weighted c. |
| −388330 | class weight of weighted c must be greater than 0. |
| −388329 | label of weighted c cannot be found in the labels of the training data. |
| −388328 | nu must be greater than 0 and less than or equal to 1. |
| −388327 | c must be greater than 0. |
| −388326 | number of hidden neurons must be greater than 0. |
| −388325 | number of searches must be greater than 0 when search method is random search. |
| −388324 | positive label cannot be found in the labels of the input data. |
| −388323 | number of folds must be greater than 1 and equal to or less than the number of samples in the training data. |
| −388322 | tolerance must be greater than 0. |
| −388321 | max iteration must be greater than 0. |
| −388320 | The input data must not be empty. |
| −388319 | ratio of variance must be greater than 0 and no greater than 1. |
| −388318 | The number of classes in the training data must be no greater than 2. |
| −388317 | number of components must be greater than 0 and no greater than the number of features in training data. |
| −388316 | The number of samples in the training data must equal number of labels. |
| −388315 | The number of features in the input data must equal the number of rows of eigenvectors. |
| −388314 | The number of rows of eigenvectors must equal the array size of mean values, and be no less than the number of columns of eigenvectors. |
| −388313 | mean values and eigenvectors must not be empty. |
| −388312 | selected feature index must be less than the number of features in the input data. |
| −388311 | The selected feature indexes in selected feature index must be different from each other. |
| −388310 | selected feature index must not be empty. |
| −388309 | The number of features in the input data must equal the array size of min values or max values. |
| −388308 | The number of features in the input data must equal the array size of mean values. |
| −388307 | min values and max values must not be empty. The size of min values and max values must be the same. |
| −388306 | mean values and standard deviation values must not be empty. The size of mean values and standard deviation values must be the same. |
| −388305 | The number of features in the input data must equal that in the source data. |
| −388304 | gamma must be greater than 0. |
| −388303 | degree must be greater than 0. |
| −388302 | The array sizes of source data, eigenvectors, and variance in the input model are not compatible with each other. |
| −388301 | source data, eigenvectors, and variance in the input model must not be empty. |
| −388300 | The data must be loaded. |
| 388301 | The PCA T2Q model is trained based on the data that is already transformed with PCA feature manipulation. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvamlconcepts/aml_gettingstarted.html language=enus -->
## TOPIC 00056: Getting Started with Machine Learning (Analytics and Machine Learning Toolkit)

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvamlconcepts/aml_gettingstarted.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvamlconcepts/aml_gettingstarted.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Getting Started with Machine Learning (Analytics and Machine Learning Toolkit)

You can create an application to train machine learning models using the Analytics and Machine Learning Toolkit. Depending on the amount of training data, you choose to use the one shot or batch training mode.

#### One Shot Training

Use the one shot training mode when you have a small amount of data and memory allows loading the data all at once for model training.

The following figure shows an example of using the one shot training mode to train a principal component analysis (PCA) model.

[IMAGE alt='image' src='loc_bd_1shot.gif']

The following events occur in the previous figure.

|  | The Load Data (2D Array) VI loads raw data for model training. Wire a 2D array of training data to data and select the Training instance of this VI. |
| --- | --- |
|  | The PCA VI trains the PCA model using the PCA settings you specify. In this example, select the One Shot instance of this VI. |
|  | The Load Data (2D Array) VI loads raw testing data. Wire a 2D array of testing data to data and select the Deployment instance of this VI. |
|  | The Deploy Feature Manipulation Model VI deploys the trained feature manipulation model and returns the transformed data. |

#### Batch Training

Use the batch training mode when you have a large number of data files but you cannot concatenate them into a large data matrix for model training due to memory constraints. Instead of consolidating all data, you can divide the data into several blocks and input one block at a time for model training so that model parameters are updated continuously. You can input as many files as you want to train the model until the model is ready for deployment.

The following figure shows an example of using the batch training mode to train a PCA model. Use a [For Loop](/csh?topicname=glang/for_loop.html) to control data coming in block by block and repeatedly load the training data one block at a time.

[IMAGE alt='image' src='loc_bd_batch.gif']

The following events occur in the previous figure.

|  | The Recursive File List VI lists all the files in the training data folder. |
| --- | --- |
|  | The Read Delimited Spreadsheet VI reads the training data block by block. |
|  | The Load Data (2D Array) VI loads one block of training data at a time. Wire the array of training data to data and select the Training instance of this VI. |
|  | The PCA VI trains and updates the PCA model block by block. In this example, select the Batch instance of this VI and wire number of components to the VI. |
|  | The Load Data (2D Array) VI loads raw testing data. Wire a 2D array of testing data to data and select the Deployment instance of this VI. |
|  | The Deploy Feature Manipulation Model VI deploys the trained feature manipulation model and returns the transformed data. |

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvamlconcepts/aml_overview.html language=enus -->
## TOPIC 00057: Analytics and Machine Learning Toolkit

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvamlconcepts/aml_overview.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvamlconcepts/aml_overview.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Analytics and Machine Learning Toolkit

July 2018, 377059B-01

The LabVIEW Analytics and Machine Learning Toolkit includes VIs for training machine learning models to discover patterns in large amounts of data. You can deploy trained machine learning models to detect anomalies, recognize patterns, or make predictions in new data.

The following figure illustrates the machine learning process.

[IMAGE alt='image' src='noloc_eps_aml_process.gif']

The machine learning process contains the following steps:

- Data Collection —Collects data using data acquisition devices or other sources.
- Feature Extraction —Extracts features based on your domain knowledge using available signal processing tools in LabVIEW, such as the LabVIEW Advanced Signal Processing Toolkit, Electrical Power Toolkit, NI Sound and Vibration Measurement Suite, Vision Development Module, and so on.
- Feature Reduction —Reduces the dimension of data so that you can use simplified data for model training.
- Model Creation —Trains machine learning models using the training data.
- Model Validation —Validates models using model evaluation metrics.
- Deployment —Deploys trained models on deployment data.

|  | Note Among these steps, the Analytics and Machine Learning Toolkit supports feature reduction, model creation, model validation, and deployment. |
| --- | --- |

The Analytics and Machine Learning Toolkit uses some algorithms from the IMS Center Watchdog Agent. Refer to the IMS Center website at www.imscenter.net for more information about the center.

|  | To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

© 2017–2018 National Instruments. All rights reserved.

<!--NI_TOPIC bundle=labview-analytics-and-machine-learning-toolkit-api-ref path=lvamlconcepts/aml_related_documentation.html language=enus -->
## TOPIC 00058: Related Documentation (Analytics and Machine Learning Toolkit)

- bundle_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- source_path: `lvamlconcepts/aml_related_documentation.html`
- source_url: https://docs-be.ni.com/bundle/labview-analytics-and-machine-learning-toolkit-api-ref/raw/resource/enus/lvamlconcepts/aml_related_documentation.html
- document_id: `labview-analytics-and-machine-learning-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Related Documentation (Analytics and Machine Learning Toolkit)

The following documents contain information that might be helpful as you use the LabVIEW Analytics and Machine Learning Toolkit.

- LabVIEW Analytics and Machine Learning Toolkit Readme —Use this file to obtain introductory information about the Analytics and Machine Learning Toolkit, such as product overview, system requirements, installation instructions, and known issues. Open this readme by navigating to the labview\readme directory and opening readme_AML.html .
- LabVIEW Analytics and Machine Learning Toolkit Example VIs—Refer to the labview\examples\AML directory for example VIs that demonstrate common tasks using the Analytics and Machine Learning Toolkit. You also can access these VIs by selecting Help»Find Examples from the pull-down menu and selecting Toolkits and Modules»Analytics and Machine Learning in the NI Example Finder window.
- Additional LabVIEW documentation .
