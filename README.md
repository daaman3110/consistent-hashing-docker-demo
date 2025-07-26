# 🔁 Consistent Hashing Simulation with Docker

This project demonstrates the concept of **Consistent Hashing** using Python, Flask, and Docker. It's designed to help visualize how data is distributed across multiple backend nodes in a distributed system and how failures impact routing.

## 📌 What is Consistent Hashing?

Consistent Hashing is a distributed hashing technique used to **evenly distribute keys across multiple servers or nodes**. It's especially useful in systems like:
- Distributed caching (e.g. Memcached, Redis)
- Load balancing
- Partitioning in databases (e.g. DynamoDB, Cassandra)

The goal is to minimize disruption when a node is added or removed.

---

## 🧠 What this project shows

- Each node is placed at a fixed position on a circular hash ring (e.g. node1 at 100, node2 at 200, etc.).
- When you hit the router with a key (like `key=Alice`), it:
  1. Computes the MD5 hash of the key
  2. Converts it to a ring position
  3. Finds the nearest node in clockwise direction
  4. Forwards the request to that node
- You can **simulate node failures** by stopping one container and watching how the system breaks.

---

## ⚙️ Project Structure

```
consistent-hashing-docker-demo/
│
├── docker-compose.yml
│
├── node/
│   ├── app.py                 # Node server code
│   └── Dockerfile             # Container for each node
│
├── router/
│   ├── app.py                 # Router logic (does hashing + routing)
│   └── Dockerfile             # Container for router
```

---

## 🚀 How to Run

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/consistent-hashing-docker-demo.git
   cd consistent-hashing-docker-demo
   ```

2. **Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **Send some test requests**  
   Open your browser or use curl:
   ```bash
   http://localhost:8080/route?key=Alice
   http://localhost:8080/route?key=Bob
   http://localhost:8080/route?key=Carol
   ```
   You'll see which node handled the key based on its position on the ring.

---

## 🧪 Simulate Node Failure

Try stopping a node:
```bash
docker stop consistent-hashing-docker-node1-1
```

Now refresh the previous URLs that were hitting node1 — you'll see **500 Internal Server Errors**. This shows how failure without virtual nodes causes routing breakdown.

---

## 🧰 Tech Stack

- **Python 3.11**
- **Flask**
- **Docker**
- **Hashing** using MD5 from Python's hashlib

---

## 🧠 Learnings

- You'll understand the core of how systems like DynamoDB or distributed caches distribute and route data.
- You'll get hands-on with Docker containers working as individual nodes.
- You'll visually see the hash ring routing in action.

---

## 🚧 Future Improvements

- ✅ Add virtual nodes to improve data balancing and fault tolerance
- ⚠️ Implement node join/leave dynamically  
- 📈 Add a UI to visualize the hash ring
- 💾 Persist key-value pairs across nodes
