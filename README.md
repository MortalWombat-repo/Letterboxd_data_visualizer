# Letterboxd_data_visualizer

## Problem description
This project ingests a dataset from kaggle in hope of gaining insight into the movie trends from the letterboxd database.

Everything is orchestrated through Mage.

The data is first downloaded through kaggle api and then sent to google bucket in a parquet format to take as little space possible.

After that the data is ingested through bigquery after which the data is visualized in Google Looker Studio.

## Cloud
Everything is in Google Cloud with Terraform provisioning resources.

## Data ingestion
No manual steps, end to end pipeline

## Data warehouse
Tables are created in DWH, but not optimized.
That is because i had missing NaN values in the dataset and the nature of the Nan is to behave as a float which makes conversion very hard and if just one Nan is not taken care of all integers get converted to float because of the data integrity.

It is not without the lack of trying but I almost didn't complete it trying to fix that.
The dataset is just not meant for it it seems.

Even if I did fix it and I came close it would be particulary difficult to explain why i clustered the bunch of 0 to not display in my charts.

## Transformations
No transformations with dbt. I also had problems there.

## Dashboard
A dashboard with more than 2 tiles

## Reproducibility
First the runner needs to download the kaggle.json and google cloud.json to the keys folder.
after that run docker-compose up.

### Kaggle
https://www.kaggle.com/docs/api
"In order to use the Kaggle’s public API, you must first authenticate using an API token. Go to the 'Account' tab of your user profile and select 'Create New Token'. This will trigger the download of kaggle.json, a file containing your API credentials."

### Google
https://console.cloud.google.com/iam-admin/serviceaccounts

From google cloud documentation
Create a service account key
In the Google Cloud console, go to the Service accounts page.
Go to Service accounts
Select a project. 
Click the email address of the service account that you want to create a key for.
Click the Keys tab.
Click the Add key drop-down menu, then select Create new key.
Select JSON as the Key type and click Create.
Clicking Create downloads a service account key file. After you download the key file, you cannot download it again.

## Dashboard
![image](https://github.com/MortalWombat-repo/Letterboxd_data_visualizer/assets/69204832/177573a0-1f0f-44df-9430-d9df620e25eb)

## Tree

```bash
Letterboxd_data_visualizer/
├── LICENSE
├── README.md
├── dbt
│   └── dbt_readme
├── docker
│   ├── DOCKERFILE
│   └── docker-compose.yaml
├── keys
│   └── INSTRUCTION.MD
├── mage
│   ├── DOCKERFILE
│   ├── docker-compose.yml
│   ├── letterboxd
│   │   ├── data_exporters
│   │   │   ├── kaggle_to_bucket.py
│   │   │   └── movies_to_bigquery.py
│   │   ├── data_loaders
│   │   │   ├── choose_kaggle_project.py
│   │   │   └── lad_movies_from_gcsbucket.py
│   │   ├── pipelines
│   │   │   └── letterboxd
│   │   │       └── metadata.yaml
│   │   └── transformers
│   │       └── fil_nan_values.py
│   └── requirements.txt
└── terraform
    ├── README
    ├── entrypoint.sh
    ├── main.tf
    └── variables.tf
```

## Note:
This was a very frustrating project and ultimatively I need to do it again with a different dataset as I had many different tables I planned the project around but did not understand the consequences of Nan values.
I counted it too late to find out that maybe 10% of rows had entire rows unaffected.
I thought about downloading many datasets and substituting values on this dataset but ultimatively that would be pointless as I found out that bigquery does not allow droping columns only creating new tables.
Had I done that and substituted values I would negate the point of bigquery and i sure wouldn't look good for me wasting the most expensive resource in this project like that.

Who ever takes a deeper dive into it. I'm very sorry many ad-hoc were made and i continue to make this a bit more manageble.

