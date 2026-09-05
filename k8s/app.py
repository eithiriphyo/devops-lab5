from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)
r = redis.Redis(host=os.environ.get("REDIS_HOST", "redis"), port=6379, decode_responses=True)

@app.route("/")
def home():
    count = r.incr("hits")
    return jsonify(message="Hello from Kubernetes!", hits=count)

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
