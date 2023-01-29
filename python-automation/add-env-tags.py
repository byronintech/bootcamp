import boto3

ec2_client_cali = boto3.client('ec2', region_name="us-west-1")
ec2_resource_cali = boto3.resource('ec2', region_name="us-west-1")

ec2_client_ohio = boto3.client('ec2', region_name="us-east-2")
ec2_resource_ohio = boto3.resource('ec2', region_name="us-east-2")

instance_ids_cali = []
instance_ids_ohio = []

# Prod Environment - Cali - US-WEST-1
reservations_cali = ec2_client_cali.describe_instances()['Reservations']
for res in reservations_cali:
    instances = res['Instances']
    for ins in instances:
        instance_ids_cali.append(ins['InstanceId'])

response = ec2_resource_cali.create_tags(
    Resources=instance_ids_cali,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'prod'
        },
    ]
)

# Dev Environment - Ohio - US-EAST-2
reservations_ohio = ec2_client_ohio.describe_instances()['Reservations']
for res in reservations_ohio:
    instances = res['Instances']
    for ins in instances:
        instance_ids_ohio.append(ins['InstanceId'])

response = ec2_resource_ohio.create_tags(
    Resources=instance_ids_ohio,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'dev'
        },
    ]
)
