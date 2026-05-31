from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# This allows the React frontend to talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Node(BaseModel):
    id: str

class Edge(BaseModel):
    source: str
    target: str

class Pipeline(BaseModel):
    nodes: List[Node]
    edges: List[Edge]

def is_dag(nodes, edges):
    # Build adjacency list — who connects to who
    graph = {node.id: [] for node in nodes}
    for edge in edges:
        if edge.source in graph:
            graph[edge.source].append(edge.target)

    # Track visit state for each node
    # 0 = unvisited, 1 = currently visiting, 2 = done
    state = {node.id: 0 for node in nodes}

    def has_cycle(node_id):
        if state[node_id] == 1:
            return True  # cycle found
        if state[node_id] == 2:
            return False  # already checked, safe

        state[node_id] = 1  # mark as currently visiting
        for neighbor in graph.get(node_id, []):
            if has_cycle(neighbor):
                return True
        state[node_id] = 2  # mark as done
        return False

    for node in nodes:
        if state[node.id] == 0:
            if has_cycle(node.id):
                return False  # cycle exists, not a DAG

    return True  # no cycles found

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

@app.post('/pipelines/parse')
def parse_pipeline(pipeline: Pipeline):
    num_nodes = len(pipeline.nodes)
    num_edges = len(pipeline.edges)
    dag = is_dag(pipeline.nodes, pipeline.edges)
    return {'num_nodes': num_nodes, 'num_edges': num_edges, 'is_dag': dag}