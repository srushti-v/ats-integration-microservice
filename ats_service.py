import requests
import json

BASE_URL = "http://localhost:3000/dev"  # Change port if needed


# 1️⃣ Health check
def test_health():
    url = f"{BASE_URL}/health"
    response = requests.get(url)
    print("Health Endpoint:", response.json())


# 2️⃣ List all jobs
def list_jobs():
    url = f"{BASE_URL}/jobs"
    response = requests.get(url)
    jobs = response.json()
    print("Jobs:")
    for job in jobs:
        print(f"  {job['id']}: {job['title']} ({job['location']}) - {job['status']}")
    return jobs


# 3️⃣ Add a candidate
def add_candidate(name, email, phone, resume_url, job_id):
    url = f"{BASE_URL}/candidates"
    payload = {
        "name": name,
        "email": email,
        "phone": phone,
        "resume_url": resume_url,
        "job_id": job_id
    }
    response = requests.post(url, json=payload)
    print(f"Add Candidate Response ({name}):", response.json())


# 4️⃣ List all candidates
def list_candidates():
    url = f"{BASE_URL}/candidates"
    response = requests.get(url)
    candidates = response.json()
    print("Candidates:")
    for cand in candidates:
        print(f"  {cand.get('name')} ({cand.get('email')}) - Job ID: {cand.get('job_id')}")
    return candidates


# 5️⃣ Get applications for a job
def get_applications(job_id):
    url = f"{BASE_URL}/applications"
    params = {"job_id": job_id}
    response = requests.get(url, params=params)
    apps = response.json()
    print(f"Applications for Job ID {job_id}:")
    for app in apps:
        print(f"  {app['candidate_name']} ({app['email']}) - Status: {app['status']}")
    return apps


# ✅ Main workflow
if __name__ == "__main__":
    test_health()

    jobs = list_jobs()

    # Add multiple candidates
    add_candidate("Rahul Sharma", "rahul@example.com", "9876543210", "https://resume.link", "3")
    add_candidate("Sheela Venkaraddi", "sheela@gmail.com", "7483665969", "https://resume.link", "4")

    candidates = list_candidates()

    # Show applications grouped by job
    print("\n=== Applications by Job ===")
    for job in jobs:
        get_applications(job['id'])
