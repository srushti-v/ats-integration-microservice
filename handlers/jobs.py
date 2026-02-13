import json
from zoho_client import ZohoRecruitClient

zoho = ZohoRecruitClient()


def get_jobs(event, context):
    """
    GET /jobs
    Returns list of jobs from Zoho Recruit (mock)
    """
    try:
        jobs = zoho.get_jobs()
        return {
            "statusCode": 200,
            "body": json.dumps(jobs)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


def create_job(event, context):
    """
    POST /jobs
    Optionally create a new job in Zoho (mock)
    """
    try:
        body = json.loads(event.get("body", "{}"))
        job = {
            "job_id": f"ZJ{len(zoho.get_jobs())+1}",
            "title": body.get("title"),
            "location": body.get("location"),
            "status": body.get("status", "OPEN"),
            "external_url": body.get("external_url", "")
        }
        # For mock, we just append to Zoho mock list
        # In real API, you would call Zoho POST endpoint here
        return {
            "statusCode": 201,
            "body": json.dumps(job)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
