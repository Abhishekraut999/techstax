
# 📦 GitHub Webhook Assignment – Submission Notes

## 🔗 Repositories:
- **Action Repo**: [INSERT ACTION-REPO LINK HERE]
- **Webhook Repo**: [INSERT WEBHOOK-REPO LINK HERE]

---

## 👩‍💻 How to Test:

### 1. Clone the webhook repo:
```bash
git clone <webhook-repo-link>
cd <repo-folder>
```

### 2. Ensure MongoDB is running on your machine at:
```
mongodb://localhost:27017/webhook_db
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Start the Flask backend:
```bash
python run.py
```

### 5. Open a new terminal and expose the local server using ngrok:
```bash
ngrok http 5000
```

### 6. Copy the HTTPS forwarding URL (e.g., `https://abc123.ngrok-free.app`)

---

## 7. Setup Webhook in Action Repo:

1. Go to **Settings → Webhooks → Add Webhook**
2. Set:
   - **Payload URL**: `https://abc123.ngrok-free.app/webhook/receiver`
   - **Content type**: `application/json`
3. Select events:
   - ✅ Push  
   - ✅ Pull Requests

---

## 🧪 Test the Functionality

- 🔄 Do a **Push** → should store and display a push event  
- 🔀 Create a **Pull Request** → should store a PR event  
- ✅ **Merge a PR** → should show a merge event (brownie points)

---

## 🖥️ Dashboard UI

Visit your forwarded URL in the browser (e.g.):
```
https://abc123.ngrok-free.app/
```

- Events are pulled from MongoDB every 15 seconds and shown in formatted logs.

---

## 📌 Notes:

- MongoDB must be running locally for event storage.
- This is a local setup using ngrok (no deployment).
- You can replace `<webhook-repo-link>` and URLs as per your test environment.

---


Follow the steps above to test and verify. Everything should work as expected.
