📦 GitHub Webhook Assignment – Submission Notes

🔗 Repositories:
- Action Repo: [INSERT ACTION-REPO LINK HERE]
- Webhook Repo: [INSERT WEBHOOK-REPO LINK HERE]

👩‍💻 How to Test:

1. Clone the webhook repo:
   git clone <webhook-repo-link>
   cd <repo-folder>

2. Ensure MongoDB is running on your machine at:
   mongodb://localhost:27017/webhook_db

3. Install dependencies:
   pip install -r requirements.txt

4. Start the Flask backend:
   python run.py

5. Open a new terminal and expose the local server using ngrok:
   - sudo snap install ngrok
   - ngrok config add-authtoken 2xrLswqrQpkUTVsufBXaG0OkpN2_6p1jqM2D6cH3yFhgb6M7Y
   - ngrok http 5000 

6. Copy the HTTPS ngrok forwarding URL (e.g., https://abc123.ngrok-free.app)

7. In the Action Repo:
   - Go to Settings → Webhooks → Add Webhook
   - Set Payload URL: https://abc123.ngrok-free.app/webhook/receiver
   - Content type: application/json
   - Events to trigger: ✅ Push ✅ Pull Requests

🧪 Test the functionality:
- Do a push → should store and display a push event
- Create a pull request → should display PR event
- Merge a PR → should show merge event

🖥️ Dashboard:
Visit https://abc123.ngrok-free.app/ in your browser
- It will update every 15 seconds to show new events

📌 Note:
- MongoDB is expected to run locally.
- No deployment is done; testing is intended through ngrok and local Flask server.

✅ Everything should work out-of-the-box using the steps above.
