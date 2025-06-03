from flask import Blueprint, request, jsonify, render_template
from app.extensions import mongo
from bson.json_util import dumps

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/')
def index():
    return render_template("index.html")

@webhook_bp.route('/events', methods=['GET'])
def get_events():
    events = mongo.db.events.find().sort("timestamp", -1).limit(10)
    return dumps(events), 200, {'Content-Type': 'application/json'}

@webhook_bp.route('/webhook/receiver', methods=['POST'])
def webhook_receiver():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')
    print(f"Received event: {event_type}")
    print(f"Payload: {data}")

    event_data = {}

    if event_type == 'push':
        event_data = {
            "author": data['pusher']['name'],
            "action_type": "push",
            "to_branch": data['ref'].split('/')[-1],
            "timestamp": data['head_commit']['timestamp']
        }

    elif event_type == 'pull_request':
        pr = data['pull_request']
        if data['action'] == 'closed' and pr.get('merged'):
            # MERGE event
            event_data = {
                "author": pr['merged_by']['login'],
                "action_type": "merge",
                "from_branch": pr['head']['ref'],
                "to_branch": pr['base']['ref'],
                "timestamp": pr['merged_at']
            }
        else:
            # PULL REQUEST event
            event_data = {
                "author": pr['user']['login'],
                "action_type": "pull_request",
                "from_branch": pr['head']['ref'],
                "to_branch": pr['base']['ref'],
                "timestamp": pr['created_at']
            }

    else:
        return jsonify({"message": "Event type ignored"}), 200

    mongo.db.events.insert_one(event_data)
    return jsonify({"message": "Event stored"}), 200
