import json
import requests
from zoho_client import ZohoRecruitClient

BASE_URL = "http://localhost:3000/dev"  # Serverless offline URL
zoho = ZohoRecruitClient()

# -----------------------------
# CLI functions using API endpoints

def list_jobs():
    """Fetch jobs from Zoho API"""
    try:
        jobs = zoho.get_jobs()  # You can also call GET /jobs endpoint
        print("\n--- Jobs ---")
        if not jobs:
            print("No jobs available.")
        for job in jobs:
            print(f"{job['job_id']}: {job['title']} ({job['location']})")
    except Exception as e:
        print("Error fetching jobs:", e)

def add_candidate():
    """Add candidate via API (Zoho)"""
    name = input("Enter candidate name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    resume_url = input("Enter resume URL: ")
    job_id = input("Enter Job ID: ")

    candidate = {
        "name": name,
        "email": email,
        "phone": phone,
        "resume_url": resume_url,
        "job_id": job_id
    }

    try:
        # POST to serverless endpoint
        response = requests.post(f"{BASE_URL}/candidates", json=candidate)
        print("Response:", response.json())
    except Exception as e:
        print("Failed to add candidate:", e)

def list_candidates():
    """List all candidates"""
    try:
        response = requests.get(f"{BASE_URL}/candidates")
        candidates = response.json()
        print("\n--- Candidates ---")
        if not candidates:
            print("No candidates found.")
        for c in candidates:
            print(f"{c['name']} - {c['email']} - Job ID: {c['job_id']}")
    except Exception as e:
        print("Error fetching candidates:", e)

def get_applications():
    """Get applications for a job"""
    job_id = input("Enter Job ID: ")
    try:
        response = requests.get(f"{BASE_URL}/applications", params={"job_id": job_id})
        applications = response.json()
        print(f"\nApplications for Job ID {job_id}:")
        if not applications:
            print("No applications found.")
        for a in applications:
            print(f"{a['candidate_name']} - {a['email']} - Status: {a['status']}")
    except Exception as e:
        print("Error fetching applications:", e)

# -----------------------------
# Menu loop

def menu():
    while True:
        print("\n=== ATS Menu ===")
        print("1. List Jobs")
        print("2. Add Candidate")
        print("3. List Candidates")
        print("4. Get Applications")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            list_jobs()
        elif choice == "2":
            add_candidate()
        elif choice == "3":
            list_candidates()
        elif choice == "4":
            get_applications()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
