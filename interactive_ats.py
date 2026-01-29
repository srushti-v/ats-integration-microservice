import json
import os
import requests

BASE_URL = "http://localhost:3000/dev"  # Serverless offline URL

# -----------------------------
# JSON file paths
JOBS_FILE = "handlers/jobs_store.json"
CANDIDATES_FILE = "handlers/candidates_store.json"

# -----------------------------
# Helper functions to persist jobs and candidates
def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return []

def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)

def load_jobs():
    return load_json(JOBS_FILE)

def save_jobs(jobs):
    save_json(JOBS_FILE, jobs)

def load_candidates():
    return load_json(CANDIDATES_FILE)

def save_candidates(candidates):
    save_json(CANDIDATES_FILE, candidates)

# -----------------------------
# Interactive API functions
def test_health():
    url = f"{BASE_URL}/health"
    try:
        response = requests.get(url)
        print("Health Endpoint:", response.json())
    except Exception as e:
        print("Error:", e)

def list_jobs():
    jobs_store = load_jobs()
    print("\n--- Jobs ---")
    if not jobs_store:
        print("No jobs available.")
    for job in jobs_store:
        print(f"{job['id']}: {job['title']} ({job['location']}) [{job['status']}]")

def add_job():
    jobs_store = load_jobs()
    job_id = str(len(jobs_store) + 1)
    title = input("Enter Job Title: ")
    location = input("Enter Job Location: ")
    status = input("Enter Status (OPEN/CLOSED/DRAFT): ").upper()
    external_url = input("Enter Job URL: ")
    job = {
        "id": job_id,
        "title": title,
        "location": location,
        "status": status,
        "external_url": external_url
    }
    jobs_store.append(job)
    save_jobs(jobs_store)
    print("Job added successfully.")

def add_candidate():
    name = input("Enter candidate name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    resume_url = input("Enter resume URL: ")
    job_id = input("Enter Job ID: ")

    # Validate job exists
    jobs_store = load_jobs()
    if not any(j["id"] == job_id for j in jobs_store):
        print("Invalid Job ID! Candidate not added.")
        return

    candidate = {
        "name": name,
        "email": email,
        "phone": phone,
        "resume_url": resume_url,
        "job_id": job_id
    }

    candidates_store = load_candidates()
    candidates_store.append(candidate)
    save_candidates(candidates_store)

    # Optionally, POST to your serverless backend
    try:
        response = requests.post(f"{BASE_URL}/candidates", json=candidate)
        print(response.json())
    except Exception as e:
        print("Candidate added locally, but failed to POST to server:", e)

def list_candidates():
    candidates_store = load_candidates()
    jobs_store = load_jobs()
    print("\n--- Candidates ---")
    if not candidates_store:
        print("No candidates found.")
    for c in candidates_store:
        job = next((j for j in jobs_store if j["id"] == c["job_id"]), None)
        job_title = job["title"] if job else "Unknown Job"
        print(f"{c['name']} - {c['email']} - Job: {job_title}")

def get_applications():
    job_id = input("Enter Job ID: ")
    candidates_store = load_candidates()
    apps = [c for c in candidates_store if c["job_id"] == job_id]
    print(f"\nApplications for Job ID {job_id}:")
    if not apps:
        print("No applications found.")
    for a in apps:
        print(f"{a['name']} - {a['email']} - Status: APPLIED")

# -----------------------------
# Menu loop
def menu():
    while True:
        print("\n=== ATS Menu ===")
        print("1. Test Health")
        print("2. List Jobs")
        print("3. Add Job")
        print("4. Add Candidate")
        print("5. List Candidates")
        print("6. Get Applications")
        print("7. Exit")
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            test_health()
        elif choice == "2":
            list_jobs()
        elif choice == "3":
            add_job()
        elif choice == "4":
            add_candidate()
        elif choice == "5":
            list_candidates()
        elif choice == "6":
            get_applications()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
