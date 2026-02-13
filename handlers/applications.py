import json
from zoho_client import ZohoRecruitClient

zoho = ZohoRecruitClient()

def get_applications(event, context):
    try:
        params = event.get("queryStringParameters") or {}
        job_id = params.get("job_id")
        if not job_id:
            return {"statusCode": 400, "body": json.dumps({"error": "job_id query parameter is required"})}
        applications = zoho.get_applications(job_id)
        return {"statusCode": 200, "body": json.dumps(applications)}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
