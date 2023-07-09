# 📚 Credit_Decisions: Explaining Credit Decisions 🎛️

This project 💼 aims to use machine learning 🤖 to classify credit applications 💳 and predict whether the credit would be paid back or not. The main goal is to provide explanations for each prediction, giving insight into the factors that contributed to the decision. This can be beneficial for both the credit providers to understand risk factors and for customers to understand the reasons for credit approval or denial.

This project leverages Amazon SageMaker and other AWS services 🌐, along with the tree-based LightGBM model and SHAP (SHapley Additive exPlanations) for predictions and their explanations, respectively.

## 🤔 What is explainability?
Model explainability is the degree to which humans 👥 can understand the cause of decisions made by a machine learning model. Many methods now exist for formulating explanations from complex models that are interpretable and faithful.

## ❓ Why is explainability useful?
An explanation gives stakeholders a way to understand the relationships and patterns learned by a machine learning model. As an example, an explanation can be used to verify that meaningful relationships are being used by the model instead of spurious relationships. Such checks can give stakeholders more confidence in the reliability and robustness of the model for real-world deployments. It’s critical for building trust 💙 in the system. When issues are found, explanations often give scientists a strong indication of what needs to be fixed in the dataset or model training procedure: saving significant time ⏰ and money 💵. Other serious issues, such a social discrimination and bias, can be clearly flagged by an explanation.

## 👩‍💼 Why is credit default prediction useful? And how does explainability help?
Given a credit application from a bank customer, the aim of the bank is to predict whether or not the customer will pay back the credit in accordance with their repayment plan. When a customer can't pay back their credit, often called a 'default', the bank loses money 💸 and the customer's credit score will be impacted. On the other hand, denying trustworthy customers credit also has a set of negative impacts.

Using accurate machine learning models to classify the risk of a credit application can help find a good balance between these two scenarios, but this provides no comfort to those customers who have been denied credit. Using explainability methods, it's possible to determine actionable factors that had a negative impact on the application. Customers can then take action to increase their chance of obtaining credit in subsequent applications.

## 💭 What is SHAP?
SHAP (Lundberg et al. 2017) stands for SHapley Additive exPlanations. 'Shapley' relates to a game theoretic concept called Shapley values that is used to create the explanations. A Shapley value describes the marginal contribution of each 'player' when considering all possible 'coalitions'. Using this in a machine learning context, a Shapley value describes the marginal contribution of each feature when considering all possible sets of features. 'Additive' relates to the fact that these Shapley values can be summed together to give the final model prediction.

As an example, we might start off with a baseline credit default risk of 10%. Given a set of features, we can calculate the Shapley value for each feature. Summing together all the Shapley values, we might obtain a cumulative value of +30%. Given the same set of features, we therefore expect our model to return a credit default risk of 40% (i.e. 10% + 30%).

![SHAP Values Image Placeholder](https://github.com/vivek7208/Credit-Decisions/assets/65945306/7f684e57-3dbc-4d63-b02f-62230fdd5b32)

### 📂 Project Structure

The project is divided into the following stages, each represented by a Jupyter notebook 📓:

1. **Introduction (0_introduction.ipynb)**: [![Open In Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vivek7208/Credit-Decisions/blob/main/notebooks/0_introduction.ipynb) Provides a high-level overview of the project.
2. **Datasets (1_datasets.ipynb)**: [![Open In Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vivek7208/Credit-Decisions/blob/main/notebooks/1_datasets.ipynb) Covers the preparation of a dataset for machine learning using AWS Glue.
3. **Training (2_training.ipynb)**: [![Open In Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vivek7208/Credit-Decisions/blob/main/notebooks/2_training.ipynb) Trains a LightGBM model using Amazon SageMaker.
4. **Endpoint (3_endpoint.ipynb)**: [![Open In Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vivek7208/Credit-Decisions/blob/main/notebooks/3_endpoint.ipynb) Deploys the model explainer to a HTTP endpoint using Amazon SageMaker and visualizes the explanations.
5. **Batch Transform (4_batch_transform.ipynb)**: [![Open In Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vivek7208/Credit-Decisions/blob/main/notebooks/4_batch_transform.ipynb) Uses Amazon SageMaker Batch Transform to obtain explanations for the complete dataset.
6. **Conclusion (5_conclusion.ipynb)**: [![Open In Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/vivek7208/Credit-Decisions/blob/main/notebooks/5_conclusion.ipynb) Wraps things up and discusses how to clean up the solution.

### 🛠️ Technologies Used

- **[Amazon SageMaker](https://aws.amazon.com/sagemaker/)**: Used for training the LightGBM model, deploying the model explainer, and obtaining explanations for the complete dataset.
- **[AWS Lambda](https://aws.amazon.com/lambda/)**: Used to generate a synthetic credits dataset and upload to Amazon S3.
- **[AWS Glue](https://aws.amazon.com/glue/)**: Used to crawl datasets and transform the credits dataset using Apache Spark.
- **[Amazon S3](https://aws.amazon.com/s3/)**: Used to store datasets and the outputs of the AWS Glue Job.
- **[Amazon ECR](https://aws.amazon.com/ecr/)**: Used to store the custom Scikit-learn + LightGBM training environment.
- **[Amazon SageMaker Batch Transform](https://aws.amazon.com/sagemaker/)**: Used to compute explanations in batch.

## 📚 Datasets Preparation and AWS Glue

The `1_datasets.ipynb` notebook 📖 is responsible for preparing datasets for machine learning using AWS Glue and creating schemas to enforce the validity of the data in later stages. 

Please refer to the `1_datasets.ipynb` notebook for detailed steps on how the datasets are processed.

## 🏋️‍♀️ Model Training with Amazon SageMaker

In the `2_training.ipynb` notebook 📖, we train a LightGBM model using Amazon SageMaker. 

For more details on model training, please refer to the `2_training.ipynb` notebook.

## 🚀 Model Deployment with Amazon SageMaker

The `3_endpoint.ipynb` notebook 📖 is used to deploy the trained model to a SageMaker endpoint for real-time inference.

Please refer to the `3_endpoint.ipynb` notebook for detailed steps on how the model is deployed and the explanations are obtained.

## 📊 Obtaining Explanations with Amazon SageMaker Batch Transform

In the `4_batch_transform.ipynb` notebook 📖, we use Amazon SageMaker Batch Transform to obtain explanations for the complete dataset.

Please refer to the `4_batch_transform.ipynb` notebook for detailed steps on how to compute explanations in batch.

## 🏁 Conclusion

In the final `5_conclusion.ipynb` notebook 📖, we discuss how to clean up the solution and offer some closing thoughts on the project.

## 👏 Datasets

The datasets (i.e. credits, people, and contacts) were synthetically created from features contained in the German Credit Dataset (UCI Machine Learning Repository). All personal information was generated using Faker. 

### Getting Started

Please follow the instructions in the Jupyter notebooks, starting with `0_introduction.ipynb`. 

Make sure to configure your AWS environment and ensure that you have the necessary permissions to access the required AWS services.

### Contributing

Contributions are welcome! Please fork this repository and open a pull request to propose changes.

### License

This project is licensed under the terms of the [MIT license](https://opensource.org/licenses/MIT).
