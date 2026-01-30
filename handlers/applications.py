import json
from handlers.candidates import load_candidates  # this will now work

def get_applications(event, context):
    params = event.get("queryStringParameters") or {}
    job_id = params.get("job_id")

    if not job_id:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "job_id query parameter is required",
                "example": "/applications?job_id=123"
            })
        }

    candidates = load_candidates()

    applications = [
        {
            "id": str(index + 1),
            "candidate_name": c["name"],
            "email": c["email"],
            "status": "APPLIED",
            "job_id": c["job_id"]
        }
        for index, c in enumerate(candidates)
        if c["job_id"] == job_id
    ]

    return {"statusCode": 200, "body": json.dumps(applications)}
