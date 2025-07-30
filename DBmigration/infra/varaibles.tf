# ========================
# EC2 Variables
# ========================
variable "ec2_ami" {
  description = "Ubuntu AMI ID"
  default     = "ami-0f58b397bc5c1f2e8" # Ubuntu 22.04 LTS (Mumbai region)
}

variable "key_name" {
  description = "EC2 Key pair name"
}

# ========================
# RDS MySQL Variables
# ========================
variable "db_name" {
  description = "Name of the MySQL database"
}

variable "db_user" {
  description = "Username for the MySQL DB"
}

variable "db_password" {
  description = "Password for the MySQL DB"
}

