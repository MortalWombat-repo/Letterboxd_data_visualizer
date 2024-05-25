#!/bin/bash

# Prompt for project name
echo "Enter the project name (default: core-forklift-412322):"
read -p "> " project_name
if [[ -z "$project_name" ]]; then
    project_name="core-forklift-412322"
fi

# Prompt for credentials path
echo "Enter the path to your credentials file (default: /home/ssh_user/project/keys/my_key.json):"
read -p "> " credentials_path
if [[ -z "$credentials_path" ]]; then
    credentials_path="/home/ssh_user/project/keys/my_key.json"
fi

# Prompt for project location
echo "Enter the project location (default: EU):"
read -p "> " location
if [[ -z "$location" ]]; then
    location="EU"
fi

# Prompt for GCS bucket name
echo "Enter the GCS bucket name (default: bucket_letterboxd_dashboard_visualizer):"
read -p "> " gcs_bucket_name
if [[ -z "$gcs_bucket_name" ]]; then
    gcs_bucket_name="bucket_letterboxd_dashboard_visualizer"
fi

# Prompt for BigQuery dataset name
echo "Enter the BigQuery dataset name (default: bigquery_letterboxd_dashboard_visualizer):"
read -p "> " bigquery_dataset_name
if [[ -z "$bigquery_dataset_name" ]]; then
    bigquery_dataset_name="bigquery_letterboxd_dashboard_visualizer"
fi

# Now you can use these variables in your Terraform commands or other scripts
# Example: terraform init --backend-config=backend.tfvars
