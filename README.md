🚀 Flask + Express Deployment using AWS & Terraform

This project demonstrates Infrastructure as Code (IaC) using Terraform to deploy a Flask backend and an Express frontend in three different AWS architectures.

🏗 Deployment Architectures Covered

Single EC2 Deployment

Two EC2 Instances Deployment

Dockerized Deployment using ECR + ECS + ALB

Cloud Platform: Amazon Web Services
Infrastructure Tool: Terraform

📌 Project Overview
Part	Deployment Type	Infrastructure
Part 1	Single EC2	Both apps on same instance
Part 2	Dual EC2	Separate instances
Part 3	Containerized	ECR + ECS + ALB
📂 Project Structure
terraform-project/
│
├── part1-single-ec2/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── user_data.sh
│
├── part2-dual-ec2/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── user_data.sh
│
├── part3-ecs-deployment/
│   ├── vpc.tf
│   ├── ecr.tf
│   ├── ecs.tf
│   ├── alb.tf
│   ├── variables.tf
│   ├── outputs.tf
│
└── README.md

🧩 Part 1: Single EC2 Deployment
🎯 Objective

Deploy Flask (Port 5000) and Express (Port 3000) on a single EC2 instance using Terraform.

Service Used: Amazon EC2

⚙ Infrastructure Components

EC2 Instance (Ubuntu)

Security Group (Ports 22, 3000, 5000)

User Data Script:

Install Python

Install Node.js

Install dependencies

Start Flask backend

Start Express frontend

🌐 Architecture Flow
User Browser
      │
      ▼
EC2 Public IP
      │
 ┌───────────────┐
 │   Express     │  Port 3000
 │   (Frontend)  │
 └───────────────┘
      │
      ▼
 ┌───────────────┐
 │    Flask      │  Port 5000
 │   (Backend)   │
 └───────────────┘

▶ Deployment Commands
terraform init
terraform plan
terraform apply

🧩 Part 2: Dual EC2 Deployment
🎯 Objective

Deploy Flask and Express on two separate EC2 instances.

⚙ Infrastructure Components

VPC

Subnets

2 EC2 Instances:

Flask Instance

Express Instance

Security Groups:

Allow inter-instance communication

Allow public access

🔐 Security Configuration
Instance	Open Ports
Flask EC2	22, 5000
Express EC2	22, 3000
🌐 Architecture Flow
User Browser
      │
      ▼
Express EC2 (Port 3000)
      │
      ▼
Flask EC2 (Port 5000)

🧩 Part 3: Docker + ECR + ECS + ALB Deployment
🎯 Objective

Deploy containerized applications using managed AWS services.

Services Used

Amazon Elastic Container Registry (ECR)

Amazon Elastic Container Service (ECS)

AWS Fargate

Application Load Balancer

Amazon VPC

🐳 Deployment Steps
Step 1: Create ECR Repositories

Terraform provisions:

flask-backend repository

express-frontend repository

Step 2: Build & Push Docker Images
docker build -t flask-backend .
docker tag flask-backend:latest <account-id>.dkr.ecr.region.amazonaws.com/flask-backend
docker push <ECR-URL>

docker build -t express-frontend .
docker tag express-frontend:latest <account-id>.dkr.ecr.region.amazonaws.com/express-frontend
docker push <ECR-URL>

Step 3: ECS Cluster & Services

Terraform provisions:

ECS Cluster

Task Definitions

ECS Services (2)

Fargate Launch Type

Step 4: Application Load Balancer

ALB Configuration:

Listener: Port 80

Target Groups:

Flask Service

Express Service

🌐 Production Architecture
                Internet
                    │
                    ▼
           Application Load Balancer
                    │
         ┌──────────┴──────────┐
         ▼                     ▼
   ECS Service (Express)   ECS Service (Flask)
         │                     │
      Fargate Tasks        Fargate Tasks
         │                     │
            Images stored in ECR

📦 Terraform Best Practices Implemented

✔ variables.tf for reusable inputs
✔ outputs.tf for exported values
✔ Modular structure
✔ S3 backend for remote state (recommended)
✔ terraform plan validation before apply

🗃 Terraform State Management

Remote Backend:

S3 Bucket for state storage

DynamoDB for state locking (optional)

Example:

backend "s3" {
  bucket         = "terraform-state-bucket"
  key            = "project/terraform.tfstate"
  region         = "ap-south-1"
}

🛠 Deployment Commands
terraform init
terraform validate
terraform plan
terraform apply


To destroy:

terraform destroy
