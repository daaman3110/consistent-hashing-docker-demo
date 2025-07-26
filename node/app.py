from flask import Flask, request
import os

app = Flask(__name__)
node_id = os.getenv("NODE_ID", "unknown")

@app.route("/handle")
def handle():
    key = request.args.get("key", "?")
    return f"Node {node_id} handled key: {key}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

