## Terraform

### backend config: tf.conf

```shell
bucket="<<bucket>>"
region="<<region>"
```

### To run:

#### Terraform init:
```shell
terraform init -backend-config=tf.conf
```

#### Terraform apply:
```shell
terraform apply -var-file="variables.tfvars"
```