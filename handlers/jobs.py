import json

jobs = [
    {
        "id": "1",
        "title": "Software Engineer",
        "location": "Remote",
        "status": "OPEN",
        "external_url": "https://joblink.com/1"
    }
]

def get_jobs(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(jobs)
    }

def add_job(event, context):
    body = json.loads(event["body"])

    job = {
        "id": str(len(jobs) + 1),
        "title": body["title"],
        "location": body["location"],
        "status": body["status"],
        "external_url": body["external_url"]
    }

    jobs.append(job)

    return {
        "statusCode": 201,
        "body": json.dumps(job)
    }
