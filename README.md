# Credit_Decisions: Explaining Credit Decisions with Amazon SageMaker

This project aims to use machine learning to classify credit applications and predict whether the credit would be paid back or not. The main goal is to provide explanations for each prediction, giving insight into the factors that contributed to the decision. This can be beneficial for both the credit providers to understand risk factors and for customers to understand the reasons for credit approval or denial.

This project leverages Amazon SageMaker and other AWS services, along with the tree-based LightGBM model and SHAP (SHapley Additive exPlanations) for predictions and their explanations respectively.

### Project Structure

The project is divided into the following stages, each represented by a Jupyter notebook:

1. **Introduction (0_introduction.ipynb)**: Provides a high-level overview of the project.
2. **Datasets (1_datasets.ipynb)**: Covers the preparation of a dataset for machine learning using AWS Glue.
3. **Training (2_training.ipynb)**: Trains a LightGBM model using Amazon SageMaker.
4. **Endpoint (3_endpoint.ipynb)**: Deploys the model explainer to a HTTP endpoint using Amazon SageMaker and visualizes the explanations.
5. **Batch Transform (4_batch_transform.ipynb)**: Uses Amazon SageMaker Batch Transform to obtain explanations for the complete dataset.
6. **Conclusion (5_conclusion.ipynb)**: Wraps things up and discusses how to clean up the solution.

### Technologies Used

- **[Amazon SageMaker](https://aws.amazon.com/sagemaker/)**: Used for training the LightGBM model, deploying the model explainer, and obtaining explanations for the complete dataset.
- **[AWS Lambda](https://aws.amazon.com/lambda/)**: Used to generate a synthetic credits dataset and upload to Amazon S3.
- **[AWS Glue](https://aws.amazon.com/glue/)**: Used to crawl datasets and transform the credits dataset using Apache Spark.
- **[Amazon S3](https://aws.amazon.com/s3/)**: Used to store datasets and the outputs of the AWS Glue Job.
- **[Amazon ECR](https://aws.amazon.com/ecr/)**: Used to store the custom Scikit-learn + LightGBM training environment.
- **[Amazon SageMaker Batch Transform](https://aws.amazon.com/sagemaker/)**: Used to compute explanations in batch.

## Datasets Preparation and AWS Glue

The `1_datasets.ipynb` notebook is responsible for preparing datasets for machine learning using AWS Glue and creating schemas to enforce the validity of the data in later stages. 

This notebook involves the following steps:

- Interacting with AWS services to retrieve information about a provisioned product and writing the retrieved information to a JSON file.
- Using AWS Glue to infer data schemas and perform extract, transform, and load (ETL) jobs in Spark. This is done through the AWS Glue workflow, which crawls the datasets stored in Amazon S3 and executes a job for data ETL.
- Waiting for the AWS Glue workflow to complete. Once completed, four additional datasets are available in the Amazon S3 bucket: `data_train`, `label_train`, `data_test`, and `label_test`.
- Retrieving the table schema for `data_train` from the AWS Glue catalog, adding additional information such as feature descriptions, and doing the same for the `label_train` schema.
- Saving these updated schemas to disk in preparation for uploading to Amazon S3.
- Using a SageMaker Session to upload these schemas to Amazon S3.

There are three datasets involved in this notebook:

1. `credits`: Contains features directly related to the credit application.
2. `people`: Contains features related to the people making the credit applications (i.e., the applicants).
3. `contacts`: Contains contact information for the applicants.

These datasets are used in AWS Glue to infer data schemas and perform ETL jobs in Spark. The AWS Glue workflow crawls these datasets, infers the schema, performs ETL tasks, and then uploads the processed datasets to Amazon S3.

The processed datasets (`data_train`, `label_train`, `data_test`, and `label_test`) are used in subsequent notebooks for model training and deployment. The schema of these datasets, stored in `jsonschema` format, is used to keep track of feature names, descriptions, and types, and to validate the input to the trained model and deployed endpoints.

Please refer to the `1_datasets.ipynb` notebook for more detailed instructions and explanations. 

### Getting Started

Please follow the instructions in the Jupyter notebooks, starting with `0_introduction.ipynb`. 

Make sure to configure your AWS environment and ensure that you have the necessary permissions to access the required AWS services.

### Contributing

Contributions are welcome! Please fork this repository and open a pull request to propose changes.

### License

This project is licensed under the terms of the [MIT license](https://opensource.org/licenses/MIT).
