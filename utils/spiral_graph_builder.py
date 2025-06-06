
import json
import networkx as nx
from pathlib import Path

TRANSCRIPT_DIR = Path(__file__).parent.parent / "transcripts"

def build_spiral_graph(session_file: str) -> nx.DiGraph:
    path = TRANSCRIPT_DIR / session_file
    with open(path, "r") as f:
        dialogue = json.load(f)

    G = nx.DiGraph()
    last_node = None

    for idx, entry in enumerate(dialogue):
        node_id = f"{entry['from']}_{idx}"
        G.add_node(node_id, label=entry['from'], output=entry['output'], ethics=entry['ethics_rating'])

        if last_node:
            G.add_edge(last_node, node_id)

        last_node = node_id

    return G
