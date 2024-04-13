variable "project" {
  description = "Project"
  default     = "core-forklift-412322"
}

variable "credentials" {
  description = "Credentials"
  default     = "/home/ssh_user/project/keys/my_key.json"
}

variable "location" {
  description = "Project location"
  default     = "EU"
}

variable "gcs_bucket_name" {
  description = "Bucket for project"
  default     = "bucket_letterboxd_dashboard_visualizer"
}

variable "bigquery_dataset_name" {
  description = "BigQuery dataset"
  default     = "bigquery_letterboxd_dashboard_visualizer"
}
