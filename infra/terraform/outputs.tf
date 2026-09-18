# SIGMUN Infrastructure - Terraform Outputs

output "vpc_id" {
  description = "ID of the VPC"
  value       = module.vpc.vpc_id
}

output "vpc_cidr" {
  description = "CIDR block of the VPC"
  value       = module.vpc.vpc_cidr_block
}

output "database_endpoint" {
  description = "PostgreSQL database endpoint"
  value       = module.postgres.db_instance_endpoint
  sensitive   = true
}

output "database_port" {
  description = "PostgreSQL database port"
  value       = module.postgres.db_instance_port
}

output "redis_endpoint" {
  description = "Redis endpoint"
  value       = module.redis.cluster_configuration_endpoint_address
  sensitive   = true
}

output "s3_bucket_name" {
  description = "S3 bucket name for document storage"
  value       = module.s3_documents.s3_bucket_id
}

output "s3_bucket_arn" {
  description = "S3 bucket ARN for document storage"
  value       = module.s3_documents.s3_bucket_arn
}
