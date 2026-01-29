import json
import os

DATA_FILE = "handlers/candidates_store.json"  # your JSON file

# ✅ Load candidates from JSON
def load_candidates():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# ✅ Save candidates to JSON
def save_candidates(candidates):
    with open(DATA_FILE, "w") as f:
        json.dump(candidates, f)

# Create a candidate
def create_candidate(event, context):
    body = json.loads(event["body"])
    candidates = load_candidates()
    candidates.append(body)
    save_candidates(candidates)
    return {
        "statusCode": 201,
        "body": json.dumps({"message": "Candidate created"})
    }

# List all candidates
def list_candidates(event, context):
    candidates = load_candidates()
    return {
        "statusCode": 200,
        "body": json.dumps(candidates)
    }
