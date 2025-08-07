🛠️ Project: Migrating Local SQLite-Based App to AWS RDS MySQL on EC2
This project demonstrates manual migration of a local Flask application that originally used SQLite or local JSON data, to a production-ready environment using:

✅ AWS EC2 for hosting the Flask app
✅ AWS RDS (MySQL) as the database backend
✅ Python virtual environment (venv)
✅ Manual file copy (no Ansible, no pipeline — focused on learning migration steps)
🧱 Project Structure

EC2Files/                         # Final working app files on EC2
 app.py                        # Flask app (connects to RDS)
 products.sql                  # MySQL insert statements (generated from JSON)
 requirements.txt              # Flask + PyMySQL
 templates/
 index.html                # Jinja2 product display template

before_migration_on_AWS/         # Original local version
 app.py                        # Flask app using JSON
 requirements.txt              # No DB required locally
 sample_data/
 products.json             # Source data
 products.sql              # Generated MySQL data
 └── transform_to_sql.py      # Python script to convert JSON → SQL
│   ├── static/
│   │   └── style.css
│   └── templates/
│       └── index.html

└── infra/
    ├── ec2.tf                        # EC2 Instance (Terraform)
    ├── network.tf                    # VPC, Subnet, Security Group
    ├── rds.tf                        # AWS RDS MySQL setup
    ├── outputs.tf
    └── variables.tf & terrafrom.tfvars

📦 Step-by-Step Setup (Manual Deployment on EC2)
🚫 No CI/CD or Ansible used — steps done manually for learning clarity.

✅ 1. Launch and SSH into EC2 Instance
Provision EC2 and RDS using terraform apply. Then SSH into the instance:
ssh -i your-key.pem ec2-user@<public-ip>

✅ 2. Install Required Packages
sudo apt update
sudo apt install python3-pip python3-venv -y

✅ 3. Set Up Python Virtual Environment
python3 -m venv venv
source venv/bin/activate

✅ 4. Transfer Files from Local to EC2
From your local machine:
scp -i your-key.pem -r EC2Files/* ec2-user@<public-ip>:/home/ec2-user/myapp/

✅ 5. Install Python Dependencies
pip install -r requirements.txt
Your requirements.txt should include:
flask
pymysql

✅ 6. Verify RDS Connectivity
Check port access to RDS MySQL:
telnet <rds-endpoint> 3306
If successful, proceed.

✅ 7. Import Data into RDS
Run the products.sql file on RDS:
mysql -h <rds-endpoint> -u admin -p mydatabase < products.sql

✅ 8. Run the Flask App
nohup python3 app.py &
The app will start on port 8008 (configured in app.py):
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)

Access it via:
http://<EC2-public-ip>:8008

🔄 Data Migration: JSON ➜ SQL
We used a custom script to transform the existing products.json into MySQL-compatible insert statements:

python3 transform_to_sql.py
This generated products.sql, which we later imported to RDS.

🚫 What This Project Does Not Use

❌ No Docker / containers

❌ No Ansible / automation

❌ No CI/CD pipelines

❌ No Kubernetes

📌 Purpose

This project is primarily to understand:

✅ Manual migration of app from local to cloud

✅ Understanding RDS, EC2, VPC manually

✅ Importance of connectivity, security groups

✅ Basics of Flask + MySQL app deployment

👷 Future Scope

You can extend this project by:

Automating using Ansible

CI/CD via GitHub Actions or Jenkins

Dockerizing the app

Deploying on Kubernetes (EKS)

🙋 Need Help?
If you face any issues during setup or migration, ensure:

RDS is publicly accessible

Security groups allow port 3306 (RDS) and 8008 (EC2)

EC2 has IAM role if needed (for SSM, if automating)
