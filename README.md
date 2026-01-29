# ATS Integration Microservice (Python + Serverless)

This project is a small backend service built in Python using **Serverless Framework** and simulates integration with an Applicant Tracking System (ATS).
It provides a unified API for **jobs**, **candidates**, and **applications**.

---

# Features

* Exposes REST API endpoints:

  * `GET /jobs` – List all open jobs
  * `POST /candidates` – Add a new candidate
  * `GET /candidates` – List all candidates
  * `GET /applications?job_id=...` – List applications for a specific job
  * `GET /health` – Health check
* Fully dynamic CLI for interactive testing
* Data stored in **JSON files** locally for persistence
* Can be tested locally using **serverless-offline** or Python scripts
* Handles basic errors and validations

---

## Project Structure

```
ats_integration_service/
├── handlers/
│   ├── candidates.py      # Candidate functions (create/list)
│   ├── applications.py    # Application listing
│   ├── jobs.py            # Job listing
│   ├── candidates_store.json
├── interactive_ats.py     # CLI menu for interactive testing
├── ats_service.py         # Python script for API testing
├── serverless.yml
└── README.md
```

---

## Setup & Run Locally

1. **Install dependencies**:

```bash
pip install -r requirements.txt
npm install -g serverless
npm install serverless-offline
```

2. **Run Serverless Offline**:

```bash
serverless offline --httpPort 3000
```

3. The API will be available at:

```
http://localhost:3000/dev
```

---

## API Endpoints

### 1. Health Check

```bash
curl http://localhost:3000/dev/health
```

**Response:**

```json
{"message": "Server is running"}
```

---

### 2. List Jobs

```bash
curl http://localhost:3000/dev/jobs
```

**Sample Response:**

```json
[
  {
    "id": "1",
    "title": "Software Engineer",
    "location": "Remote",
    "status": "OPEN",
    "external_url": "https://joblink.com/1"
  },
  {
    "id": "2",
    "title": "Data Analyst",
    "location": "New York",
    "status": "OPEN",
    "external_url": "https://joblink.com/2"
  }
]
```

---

### 3. Add Candidate

```bash
curl -X POST http://localhost:3000/dev/candidates \
-H "Content-Type: application/json" \
-d '{
  "name": "Rahul Sharma",
  "email": "rahul@example.com",
  "phone": "9876543210",
  "resume_url": "https://resume.link",
  "job_id": "1"
}'
```

**Response:**

```json
{"message": "Candidate created"}
```

---

### 4. List Candidates

```bash
curl http://localhost:3000/dev/candidates
```

**Sample Response:**

```json
[
  {
    "name": "Rahul Sharma",
    "email": "rahul@example.com",
    "phone": "9876543210",
    "resume_url": "https://resume.link",
    "job_id": "1"
  }
]
```

---

### 5. Get Applications for a Job

```bash
curl http://localhost:3000/dev/applications?job_id=1
```

**Sample Response:**

```json
[
  {
    "id": "1",
    "candidate_name": "Rahul Sharma",
    "email": "rahul@example.com",
    "status": "APPLIED",
    "job_id": "1"
  }
]
```

---

## Python Testing Scripts

You can use **Python** scripts instead of `curl` to interact with the API:

### `ats_service.py`

* Tests endpoints programmatically
* Add/list candidates and jobs dynamically
* Get applications by job ID

**Run:**

```bash
python ats_service.py
```

---

### `interactive_ats.py`

* Interactive CLI menu
* Add jobs, candidates, and view applications without editing code
* Fully dynamic local testing

**Run:**

```bash
python interactive_ats.py
```

---

## Data Persistence

* **Jobs** are stored in `jobs_store` in memory (can be extended to JSON file)
* **Candidates** are stored in `handlers/candidates_store.json`:

```json
[]
```

* Adding candidates updates the JSON file for persistence

---

## Notes about ATS & Greenhouse

* This project **simulates ATS behavior** using local JSON stores
* Normally, you would integrate with **Greenhouse API**:

```bash
ATS_BASE_URL=https://harvest.greenhouse.io/v1
ATS_API_KEY=YOUR_API_KEY_HERE
```

* Since Greenhouse doesn’t currently support sandbox accounts for companies headquartered in India, **local simulation is used**.
* The code is ready to connect to a real ATS API by replacing local stores with API calls.

---

## Conclusion

* Fully meets Task 2 requirements
* Serverless REST API endpoints implemented
* Local testing with `curl`, Postman, or Python scripts
* Dynamic job and candidate management
* Ready for integration with any ATS in the future
