from flask import Flask, request
import hashlib
import requests

app = Flask(__name__)

# Map of node hash -> URL
nodes = {
    100: "http://node1:5000",
    200: "http://node2:5000",
    300: "http://node3:5000"
}

sorted_hashes = sorted(nodes.keys())

def get_node_for_key(key):
    h = int(hashlib.md5(key.encode()).hexdigest(), 16) % 360
    for nh in sorted_hashes:
        if h <= nh:
            return nodes[nh]
    return nodes[sorted_hashes[0]]

@app.route("/route")
def route():
    key = request.args.get("key")
    if not key:
        return "Missing key parameter", 400

    node_url = get_node_for_key(key)
    res = requests.get(f"{node_url}/handle", params={"key": key})
    return f"[Ring Position: {int(hashlib.md5(key.encode()).hexdigest(), 16) % 360}] {res.text}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

