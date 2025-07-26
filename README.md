🔁 Consistent Hashing Simulation with Docker
This project demonstrates the concept of Consistent Hashing using Python, Flask, and Docker. It's designed to help visualize how data is distributed across multiple backend nodes in a distributed system and how failures impact routing.
📌 What is Consistent Hashing?
Consistent Hashing is a distributed hashing technique used to evenly distribute keys across multiple servers or nodes. It's especially useful in systems like:

Distributed caching (e.g., Memcached, Redis)
Load balancing
Partitioning in databases (e.g., DynamoDB, Cassandra)

The goal is to minimize disruption when a node is added or removed from the system.
🧠 What This Project Demonstrates

Each node is placed at a fixed position on a circular hash ring (e.g., node1 at 100, node2 at 200, etc.)
When you hit the router with a key (like key=Alice), it:

Computes the MD5 hash of the key
Converts it to a ring position
Finds the nearest node in the clockwise direction
Forwards the request to that node


You can simulate node failures by stopping one container and watching how the system responds

⚙️ Project Structure
consistent-hashing-docker-demo/
│
├── docker-compose.yml          # Orchestrates all containers
│
├── node/                       # Backend node implementation
│   ├── app.py                 # Node server code
│   └── Dockerfile             # Container for each node
│
├── router/                     # Hash ring router
│   ├── app.py                 # Router logic (hashing + routing)
│   └── Dockerfile             # Container for router
│
└── README.md                   # This file
🚀 How to Run
1. Clone the Repository
bashgit clone https://github.com/your-username/consistent-hashing-docker-demo.git
cd consistent-hashing-docker-demo
2. Run with Docker Compose
bashdocker-compose up --build
This will start:

Router service on port 8080
Multiple node services on internal Docker network

3. Send Test Requests
Open your browser or use curl to test the routing:
bash# Test different keys to see routing distribution
curl "http://localhost:8080/route?key=Alice"
curl "http://localhost:8080/route?key=Bob" 
curl "http://localhost:8080/route?key=Carol"
curl "http://localhost:8080/route?key=David"
You'll see which node handled each key based on its position on the hash ring.
🧪 Simulate Node Failure
Test Fault Tolerance
bash# Stop a specific node
docker stop consistent-hashing-docker-node1-1

# Or view running containers first
docker ps
Now refresh the previous URLs that were hitting the stopped node. You'll observe:

500 Internal Server Errors for keys that mapped to the failed node
Other keys continue working normally
This demonstrates how failure without virtual nodes causes routing breakdown

Restart Failed Node
bashdocker-compose up node1
🧰 Tech Stack

Python 3.11 - Runtime environment
Flask - Web framework for API endpoints
Docker - Containerization platform
MD5 Hashing - Using Python's hashlib for key distribution

🧠 Learning Outcomes
After running this simulation, you'll understand:

How distributed systems like DynamoDB or Redis distribute data
The concept of hash rings and clockwise key mapping
Impact of node failures on data availability
Why virtual nodes are important for better distribution
Docker container orchestration for distributed systems

Troubleshooting
Common Issues
Port Already in Use
bash# Kill processes using port 8080
sudo lsof -ti:8080 | xargs kill -9
Container Build Failures
bash# Clean rebuild all containers
docker-compose down
docker-compose build --no-cache
docker-compose up
Node Communication Errors

Ensure all containers are on the same Docker network
Check docker-compose.yml service names match router configuration

