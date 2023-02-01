import boto3
from operator import itemgetter
import schedule

ec2_client = boto3.client('ec2', region_name="us-west-2")


def delete_snapshots():
    snapshots = ec2_client.describe_snapshots(
        OwnerIds=['self']
    )

    sorted_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

    for snap in sorted_by_date[2:]:
        response = ec2_client.delete_snapshot(
            SnapshotId=snap['SnapshotId']
        )
        print(response)


delete_snapshots()

# Schedule to Run Every Week
"""schedule.every().saturday.do(delete_snapshots)

while True:
    schedule.run_pending()"""
