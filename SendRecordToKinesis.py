# Below is a complete Python script that:
# Loads your AWS credentials from a file (e.g., ~/.aws/credentials)
# Initializes an AWS session with boto3
# Creates a Kinesis client
# Defines a Kinesis stream name
# Prepares a JSON object
# Sends it to the stream using put_record
# Prints the ShardId and SequenceNumber

#  Send a Record to Kinesis

import boto3
import json
import yaml
from botocore.exceptions import ClientError

# ---------------------
# 1. Load AWS Credentials (from YAML file)
# ---------------------

with open('aws_credentials.yml', 'r') as file:
    aws_credentials = yaml.safe_load(file)

# Extract credentials from YAML

aws_access_key_id = aws_credentials['aws_access_key_id']
aws_secret_access_key = aws_credentials['aws_secret_access_key']
aws_region_name = aws_credentials['aws_region_name']

# Initialize a session using AWS credentials
session = boto3.Session(
    aws_access_key_id = aws_access_key_id,
    aws_secret_access_key = aws_secret_access_key,
    region_name = aws_region_name
)

# ---------------------
# 2. Create a Kinesis client
# ---------------------
kinesis_client = session.client('kinesis')

# ---------------------
# 3. Define the Kinesis Stream Name
# ---------------------
stream_name = 'dea_sample_stream'  # Replace with your stream name

# ---------------------
# 4. Create Sample JSON Data to put into the stream
# ---------------------
sample_data = {
    "event_type": "user_signup",
    "user_id": "abc123",
    "timestamp": "2025-07-07T10:45:00Z"
}

# ---------------------
# 5. Convert JSON Object to String
# ---------------------
data_as_string = json.dumps(sample_data)

# ---------------------
# 6. Put Record into Kinesis Stream
# ---------------------

try:
    response = kinesis_client.put_record(
        StreamName=stream_name,
        Data=data_as_string,
        PartitionKey=sample_data['user_id']
    )

    # ---------------------
    # 7. Print Shard ID and Sequence Number
    # ---------------------
    print("Record successfully sent to Kinesis Stream!")
    print("ShardId:", response['ShardId'])
    print("SequenceNumber:", response['SequenceNumber'])

except Exception as e:
    print("Error putting record to stream:", str(e))