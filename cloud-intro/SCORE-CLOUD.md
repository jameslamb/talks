# Cloud scoring

## Lambda Test Events

## From anywhere

```python
import base64
import boto3
import json
import os
from scripts.create_random_tickets import _get_one_record

os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

payload = {
    "data": [
        _get_one_record()
        for i in range(10)
    ]
}

client = boto3.client("lambda")
response = client.invoke(
    FunctionName="ticket-closure-scoring",
    InvocationType='RequestResponse',
    LogType='Tail',
    Payload=json.dumps(payload).encode('utf-8')
)

# see the logs
for line in base64.b64decode(response["LogResult"]).decode('utf-8').split('\n'):
    print(line)

# see the predictions
result = json.loads(response["Payload"].read().decode('utf-8'))
print(result)
```
