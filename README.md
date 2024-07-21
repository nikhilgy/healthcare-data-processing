# healthcare-data-processing

## Overview

This repo is for processing clinical data, ranging from unstructured CSV files to structured RedCap tables. The objective is to clean, organize, and transform this data to provide valuable insights. We will implement Kedro pipelines for data ingestion and processing, and dbt for data transformation and standardization.

Take a look at the [Kedro documentation](https://docs.kedro.org) to get started.

### Tech Stack

- Python 3.11
- Kedro
- PostgreSQL

## How to setup development environment

Clone the repo

```
git clone https://github.com/nikhilgy/healthcare-data-processing.git
```

Activate virtual environment
```
python -m venv venv
source venv/Scripts/activate
```

Install dependencies mentioned in `requirements.txt`. To install them, run:
```
pip install -r requirements.txt
```

Setup database connection and add credentials

1. For Kedro project, create credential.yml in `\conf\base\`

```
postgres:
  con: postgresql+psycopg2://username:password@localhost/lupus_staging_raw
```

2. For dbt project, create profiles.yml in `\dbt\lupus_staging_tuva_model`. Refer [profiles.yml](https://docs.getdbt.com/docs/core/connect-data-platform/profiles.yml). Change host, database name,schema as per your requirements, I'm using localhost for practice.

```
lupus_staging_tuva_model:
  outputs:
    dev:
      dbname: lupus_staging_raw
      host: localhost
      pass: <db_password>
      port: 5432
      schema: tuva_data_model
      threads: 1
      type: postgres
      user: postgres
  target: dev

```

You're ready to run Kedro pipelines now🎉

## How to run your Kedro pipeline

This project has 3 pipelines stages:

1. **data_cleaning** : Here we're identifying data issues such as duplicates, noise in values, wrong formats, fixing them and loading into raw database for all datasets: `patients, medications, symptoms, patient_gender, encounters, conditions` . To run data cleaning, 
    
    ```
    kedro run --pipeline data_cleaning
    ```
2. **data_standardization** : Here we're structuring datasets and columns according to Tuva Project Data Model Input Layer all datasets: `patients, medications, observations, encounters, conditions` . To run data standardization, 
    
    ```
    kedro run --pipeline data_standardization
    ```

2. **data_merge** : Here we're merging all datasets `patients, medications, observations, encounters, conditions` into a patient master dataset for analytical purposes. To run data merge, 
    
    ```
    kedro run --pipeline data_merge
    ```

We've successfully loaded data into database and created a denormalized master table to be used ahead.🎉💯 


##### Pro tip: You can run kedro visualization for getting overview of all pipelines and kedro project
```
kedro viz run
```
