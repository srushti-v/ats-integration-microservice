import json

def health(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Server is running"})
    }
