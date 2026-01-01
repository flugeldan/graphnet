# GraphNet - Social Network Analysis Platform / universal backend for creating any social-connecting platform with analysis
Universal graph analysis engine for community detection and social matching.

## Project vision
Building a reusable platform for analyzing social networks using advanced graph algorithms. Not just another social network clone - a **platform** that can power any community-based application.

## Features

### Implemented (Stage 1 - In Progress)

- ✅ **Community Detection** - Find connected groups using BFS
- ✅ **Best Match Algorithm** - Compatibility scoring with exponential age decay
- ✅ **Common Analysis** - Find common friends and hobbies
- ✅ **Data Generator** - Create 100+ realistic test users
- ✅ **Separation Degree** - Shortest path between users
- ⬜ **Mutual Friend Suggestions** - "People you may know"
- ⬜ **Bridge Detection** - Critical connections (Tarjan's algorithm)

### Planned (Stage 2-3)

- 🎯 **PageRank** - Influence scoring (Google's algorithm)
- 🎯 **Louvain Algorithm** - Advanced community detection
- 🎯 **Graph Neural Networks** - ML-based link prediction
- 🎯 **Node2Vec** - Graph embeddings
















## 🧮 Algorithms

### Community Detection (BFS)
- **Complexity:** O(V + E)
- **Use Case:** Find isolated groups in network
- **Implementation:** Breadth-First Search
- **Quick note: community every member of community does not necessarily need to know each other, being connected through node is enough. Might add for small graphs condition that new person should know everyone before in community to be part of community, in order to prevent clique problem on a big data**

- **Also for now, one member can be only in one community (done that for optimization), but will add for small graphs either filter for biggest user community or every community that user in, right now you can tell how many unconnected groups of people there, or if everyone knows each other, possibly good for advertisiment (how to connect 2 independent groups of people by their interests)**

- ### Separation Degree (BFS)
- **Feature**s:
- **BFS-based shortest path finding**
- **Full path reconstruction from start to end**
- **Handles edge cases (same user, direct friends, disconnected)**
- **O(V+E) time complexity**
Implementation:
- **Queue stores (path, current_node) tuples**
- **Path built incrementally during BFS**
- **Returns (distance, path) or (None, None)**

### Best Match Scoring
- **Factors:** Common hobbies (×5), Mutual friends (×5), Age similarity
- **Age Decay:** Exponential penalty for age difference >10 years
- **Formula:** `score = base × (1 / (1 + (age_diff - 10) × 0.2))` 
- **Const 0.2 is changeable, put 0.05 if u want for example tax 5% for each year**

## 📈 Development Progress

### Stage 1: Classical Graph Algorithms
- [x] Project structure
- [x] Data generator (120 users)
- [x] Community detection (BFS)
- [x] Separation degree (BFS path finding)
- [ ] Mutual friend suggestions
- [ ] Bridge detection (Tarjan's)
- [ ] Friend-adding system by request rather than just adding
- [ ] After every operation of removing/adding friend, checking changes in community graph

**Target:** End of Q1 2026


### Stage 2: Advanced Algorithms
- [ ] PageRank implementation
- [ ] Louvain community detection
- [ ] Performance optimization (10k+ nodes)

**Target:** Q2 2026

### Stage 3: Machine Learning
- [ ] Graph Neural Networks
- [ ] Node2Vec embeddings
- [ ] Link prediction

**Target:** Q3 2026







## 🛠️ Tech Stack

**Language:** Python 3.8+  
**Architecture:** Modular, object-oriented  
**Data Structure:** Adjacency list (dict-based)  
**Storage:** JSON  
**Dependencies:** None (pure Python!)

**Algorithms Implemented (please check out algorithms section above aswell):**
- BFS (Breadth-First Search)
- DFS (Depth-First Search)
- Exponential decay scoring
- Bidirectional graph normalization

**Planned:**
- Tarjan's algorithm
- PageRank (power iteration)
- Louvain (modularity optimization)
- GNN (PyTorch Geometric)




## 👨‍💻 Author

**Flugel**  
First-year Software Engineering @ AITU, Kazakhstan

**Background:**
- Competitive Programming (Codeforces ~1400, targeting 1800+)
- Leetcode problem solver
- Focus: Graph algorithms, backend development, system design

## 📝 License

Personal educational project - 2025

---

*Built in December 2025. Learning by doing. Aiming for research-level implementation.*
