#!/bin/bash

# Run Terraform apply
terraform apply -auto-approve

# Run Terraform destroy
function cleanup {
    terraform destroy -auto-approve
}

trap cleanup EXIT

# Keep the container running
while true; do sleep 1; done
