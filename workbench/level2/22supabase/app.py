from flask import Flask, request, jsonify, render_template
from supabase import create_client
import os

app = Flask(__name__)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Connecter un script Python à Supabase pour lire/écrire des données.  
@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    response = supabase.table("flasktest").insert(data).execute()
    return jsonify(response.data), 201

@app.route("/results", methods=["GET"])
def results():
    response = supabase.table("flasktest").select("*").execute()
    return jsonify(response.data), 200

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
