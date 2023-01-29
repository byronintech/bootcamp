# Output EC2 Public IP
output "ec2_public_ip" {
    value = module.myapp-webserver.instance.public_ip
}
