import boto3

client = boto3.client('eks', region_name="us-west-2")
clusters = client.list_clusters()['clusters']

print('-' * 60)

for cluster in clusters:
    response = client.describe_cluster(
        name=cluster
    )
    cluster_info = response['cluster']
    cluster_status = cluster_info['status']
    cluster_endpoint = cluster_info['endpoint']
    cluster_version = cluster_info['version']


    print(f"Cluster {cluster} status is: {cluster_status}")
    print(f"Cluster endpoint: {cluster_endpoint}")
    print(f"Cluster version: {cluster_version}")
print('-' * 60)
