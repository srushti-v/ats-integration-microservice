def health(event, context):
    return {
        "statusCode": 200,
        "body": '{"message": "Server is running"}'
    }
