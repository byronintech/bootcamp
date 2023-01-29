import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="us-west-2")
ec2_resource = boto3.resource('ec2', region_name="us-west-2")

# Scheduler Function
def check_instance_status():
# EC2 Status Check
        statuses = ec2_client.describe_instance_status(IncludeAllInstances=True)
        for status in statuses['InstanceStatuses']:
                ins_status = status['InstanceStatus']['Status']
                sys_status = status['SystemStatus']['Status']
                state = status['InstanceState']['Name']
                print(f"Instance {status['InstanceId']} is {state} with instance status {ins_status} and system status is {sys_status}")
        print('-' * 60)
# Set Scheduler
schedule.every(15).seconds.do(check_instance_status)

# Execute Scheduler
while True:
        schedule.run_pending()
