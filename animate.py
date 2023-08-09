from azure.batch import BatchServiceClient
from azure.batch.batch_auth import SharedKeyCredentials
from azure.batch.models import JobAddParameter, PoolInformation, OnAllTasksComplete
import azure.batch.models as batchmodels
from azure.storage.blob import BlobServiceClient
import os, sys, pandas as pd
from io import StringIO
import argparse

parser = argparse.ArgumentParser(description='Get topic ID.')
parser.add_argument('projectname', type=str, help='An integer argument.')

# Parse the command-line arguments
args = parser.parse_args()

# Access the argument value
project = args.projectname

batch_service_client.job.add(job)




resource_files = []

tasks = []
container_name = "code"
blob_name = "info.csv"
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
downloaded_blob = blob_client.download_blob()
blob_content = downloaded_blob.content_as_text()
df = pd.read_csv(StringIO(blob_content))

selected = [*range(len(df))]

for i in selected:
    command = f"python3 run.py {i} {project}"
    tasks.append(batchmodels.TaskAddParameter(
        id=f'{i}',
        command_line=command,
        resource_files = resource_files
    ))

batch_service_client.task.add_collection(project, tasks)