from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('../Backend/discord_link/link.py', methods=['POST'])
def link_discord():
    data = request.json
    token = data.get('token')
    discord_id = data.get('discord_id')