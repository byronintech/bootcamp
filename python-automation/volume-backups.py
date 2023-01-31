import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="us-west-2")


def create_volume_snapshots():
    volumes = ec2_client.describe_volumes()
    print("-----" * 15)
    print("EC2 Volume Dictionary:")
    print(volumes['Volumes'])
    print("-----" * 15)

    for volume in volumes['Volumes']:
        # print("-----" * 15)
        ec2_vol_id = volume['VolumeId']
        print(f"EC2 Volume ID: {ec2_vol_id}")
        new_snapshot = ec2_client.create_snapshot(
            VolumeId=volume['VolumeId']
        )
        print(f"Snapshot Info: {new_snapshot}")
        print("-----" * 15)


# Set Scheduler
schedule.every().day.do(create_volume_snapshots)

# Execute Scheduler
while True:
    schedule.run_pending()
