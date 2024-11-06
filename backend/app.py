from flask import Flask, request
from flask_cors import CORS
from RequirementCollection import RequirementCollectionAgent
from ItineraryPlanning import ItineraryPlanAgent

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    chat_history = request.json
    return RequirementCollectionAgent(chat_history)


@app.route("/route", methods=["POST"])
def get_route():
    return ItineraryPlanAgent(request.json)