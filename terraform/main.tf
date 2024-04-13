terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.21.0"
    }
  }
}

provider "google" {
  project     = var.project
  credentials = file(var.credentials)
  region      = "europe-west1"
}

resource "google_storage_bucket" "bucket" {
  name                     = var.gcs_bucket_name
  location                 = var.location
  force_destroy            = true
  public_access_prevention = "enforced"

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "bigquery" {
  dataset_id = var.bigquery_dataset_name
  location   = var.location
}