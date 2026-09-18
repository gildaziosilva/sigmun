# SIGMUN Infrastructure as Code
# Based on Arquitetura de Implantação - AWS

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# VPC
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"

  name = "sigmun-${var.environment}"
  cidr = "10.0.0.0/16"

  azs             = ["${var.aws_region}a", "${var.aws_region}b"]
  public_subnets  = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets = ["10.0.10.0/24", "10.0.11.0/24"]

  enable_nat_gateway = true
  single_nat_gateway = true

  tags = {
    Project = "SIGMUN"
    Environment = var.environment
  }
}

# RDS PostgreSQL
module "postgres" {
  source  = "terraform-aws-modules/rds/aws"
  version = "~> 6.0"

  identifier = "sigmun-${var.environment}-postgres"

  engine               = "postgres"
  engine_version       = "16"
  family               = "postgres16"
  major_engine_version = "16"

  instance_class = var.db_instance_class
  allocated_storage     = 20
  max_allocated_storage = 100

  db_name  = var.db_name
  username = var.db_username
  port     = var.db_port

  db_subnet_group_name   = module.vpc.database_subnet_group_name
  vpc_security_group_ids = [module.vpc.default_security_group_id]

  backup_retention_period = 7
  backup_window           = "02:00-03:00"
  maintenance_window      = "sun:03:00-sun:04:00"

  tags = {
    Project = "SIGMUN"
    Environment = var.environment
  }
}

# ElastiCache Redis
module "redis" {
  source  = "terraform-aws-modules/elasticache/aws"
  version = "~> 9.0"

  cluster_id = "sigmun-${var.environment}-redis"

  engine         = "redis"
  engine_version = "7.0"
  node_type      = var.redis_node_type
  num_cache_nodes = 1
  port            = 6379

  subnet_group_name = module.vpc.elasticache_subnet_group_name
  security_group_ids = [module.vpc.default_security_group_id]

  apply_immediately = true

  tags = {
    Project = "SIGMUN"
    Environment = var.environment
  }
}

# S3 Bucket for documents
module "s3_documents" {
  source  = "terraform-aws-modules/s3-bucket/aws"
  version = "~> 4.0"

  bucket = "sigmun-${var.environment}-documentos"

  versioning = {
    status = true
  }

  server_side_encryption_configuration = {
    rule = {
      apply_server_side_encryption_by_default = {
        sse_algorithm = "AES256"
      }
    }
  }

  tags = {
    Project = "SIGMUN"
    Environment = var.environment
  }
}
