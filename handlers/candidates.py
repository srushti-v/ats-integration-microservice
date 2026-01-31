import json
from zoho_client import ZohoRecruitClient

zoho = ZohoRecruitClient()


def create_candidate(event, context):
    """
    POST /candidates
    Add candidate dynamically and push to Zoho mock API
    """
    try:
        body = json.loads(event.get("body", "{}"))
        response = zoho.create_candidate(body)  # Zoho mock creates candidate
        return {
            "statusCode": 201,
            "body": json.dumps(response)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }


def list_candidates(event, context):
    """
    GET /candidates
    List all candidates from Zoho mock
    """
    try:
        candidates = zoho.get_applications(job_id=None)  # Returns all candidates
        return {
            "statusCode": 200,
            "body": json.dumps(candidates)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
