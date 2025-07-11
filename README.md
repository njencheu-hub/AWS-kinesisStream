# AWS Kinesis Data Stream Sender

A Python script that securely loads AWS credentials from a YAML file, initializes a Boto3 session, and sends a JSON record into an Amazon Kinesis Data Stream. It prints the shard and sequence number upon success.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [AWS Credentials File](#aws-credentials-file)
- [Usage](#usage)
- [Expected Output](#expected-output)
- [IAM Permissions](#iam-permissions)
- [License](#license)

---

## Features

- Loads AWS credentials from a secure YAML file
- Uses Boto3 to create a session and connect to Amazon Kinesis
- Sends a sample JSON record into a named Kinesis stream
- Outputs the shard ID and sequence number after a successful put
- Includes exception handling for Kinesis errors

---

## Requirements

- Python 3.7+
- Packages:
  - `boto3`
  - `pyyaml`

You can install the requirements using:

```bash
pip install boto3 pyyaml

```

## Setup
- Clone this repo or copy the script.
- Create a file named `aws_credentials.yml` in the same directory (see below).
- Ensure your Kinesis stream is created and active.
- Assign the correct IAM permissions (see IAM Permissions).

## AWS Credentials File

Example aws_credentials.yml:

```yaml

aws_access_key_id: YOUR_ACCESS_KEY_ID
aws_secret_access_key: YOUR_SECRET_ACCESS_KEY
aws_region_name: us-east-2
```
Do not commit this file to version control.

## Usage
Run the script:

```bash
python SendRecordToKinesis.py
```
## Expected Output
If the record is successfully sent:

```bash

Record successfully sent to Kinesis Stream!
ShardId: shardId-000000000000
SequenceNumber: 49561092965719283170505432917626474137982880025628094466
```

If an error occurs:

```bash

Error putting record to stream: <ErrorMessage>
```


## IAM Permissions
The IAM user or role must have the following permissions:

```json

{
  "Effect": "Allow",
  "Action": [
    "kinesis:PutRecord"
  ],
  "Resource": "arn:aws:kinesis:<region>:<account-id>:stream/dea_sample_stream"
}
```

## License
MIT License
© 2025 Georgie Mbianda