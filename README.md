# DevOps Project – Scotia Bank (CI/CD on Azure with AKS & OpenShift)

This project reflects a real-world DevOps setup for Scotia Bank, focusing on secure, scalable deployments in Azure using AKS, OpenShift, and CI/CD via Azure DevOps Pipelines.

## 🔧 Key Features

- Microservices deployed through Azure DevOps Pipelines with Nexus artifact storage
- Container orchestration with AKS and OpenShift
- Infrastructure as Code with Terraform + Terragrunt
- Multi-environment architecture (DEV, UAT, PROD) with secure subnets in Azure VNet
- Configuration management with Chef and Ansible
- Monitoring/logging via ELK stack and scripting with Bash + Python

## 🛠️ Tech Stack

- **CI/CD**: Azure DevOps, Nexus, Docker, OpenShift
- **Orchestration**: AKS, ACS, OpenShift
- **IaC**: Terraform, Terragrunt
- **Monitoring**: ELK (Elasticsearch, Logstash, Kibana)
- **Messaging**: RabbitMQ
- **Config Management**: Chef, Ansible
- **Scripting**: Bash, Python
- **App Stack**: Java, Spring Boot, Node.js, .NET
- **Database**: MariaDB
- **Cloud**: Azure (VNet, Load Balancers, NSGs)

## 📦 Project Highlights

- Used Terraform modules and Terragrunt for DRY infrastructure definitions
- Created AKS clusters and managed networking with private/public subnets and NSGs
- Wrote custom Dockerfiles for each microservice and deployed with OpenShift
- Built CI/CD pipelines in Azure DevOps for controlled, 2-week release cycles
- Managed RabbitMQ for messaging, ELK for logs, and secured infra with Azure Firewall
- Automated environment setup with Chef and Ansible
- Wrote shell scripts for secure SSH key distribution

## 📂 Folder Structure

```bash
.
├── terraform/
│   └── main.tf
├── k8s/
│   └── deployment.yaml
├── chef/
│   └── cookbook.rb
├── ansible/
│   └── playbook.yml
├── scripts/
│   ├── ssh-key-share.sh
│   └── configure-logging.py
├── README.md
```

## 👨‍💻 Your Role

- CI/CD automation with Azure DevOps Pipelines
- Infrastructure provisioning using Terraform and Terragrunt
- Secure container deployment with Docker, AKS, and OpenShift
- Scripting for automation, security, and environment configuration
- Release coordination and monitoring/logging integration

> **Note:** This project reflects real enterprise DevOps workflows and tools. Code is illustrative.
