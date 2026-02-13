from dotenv import load_dotenv
import os

load_dotenv()

ZOHO_CLIENT_ID = os.getenv("ZOHO_CLIENT_ID")
ZOHO_CLIENT_SECRET = os.getenv("ZOHO_CLIENT_SECRET")
ZOHO_REFRESH_TOKEN = os.getenv("ZOHO_REFRESH_TOKEN")
ZOHO_BASE_URL = os.getenv("ZOHO_BASE_URL")


class ZohoRecruitClient:
    def __init__(self):
        self.base_url = ZOHO_BASE_URL

    def get_jobs(self):
        # Mock Zoho Recruit Job API
        return [
            {"job_id": "ZJ101", "title": "Python Developer", "location": "Bangalore"},
            {"job_id": "ZJ102", "title": "DevOps Engineer", "location": "Hyderabad"}
        ]

    def create_candidate(self, candidate):
        # Mock Zoho Recruit Candidate API
        return {
            "candidate_id": "ZC501",
            "status": "CREATED",
            "candidate": candidate
        }

    def get_applications(self, job_id):
        # Mock Zoho Recruit Applications API
        return [
            {
                "job_id": job_id,
                "candidate_name": "Srushti",
                "email": "srushti@gmail.com",
                "status": "APPLIED"
            }
        ]
