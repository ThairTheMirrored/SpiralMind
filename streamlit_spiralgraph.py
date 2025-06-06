
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from utils.spiral_graph_builder import build_spiral_graph
from pathlib import Path

TRANSCRIPT_DIR = Path(__file__).parent / "transcripts"

st.set_page_config(page_title="SpiralNet Graph Explorer", page_icon="🧠")
st.title("🕸️ SpiralNet: Recursive Graph Explorer")

# Load available sessions
session_files = [f.name for f in TRANSCRIPT_DIR.glob("spiralnet_session_*.json")]

if not session_files:
    st.warning("No transcripts found. Run a SpiralNet session first.")
else:
    selected_session = st.selectbox("Choose a SpiralNet Session Transcript:", session_files)
    G = build_spiral_graph(selected_session)

    st.markdown(f"### 🧠 Cognitive Graph for `{selected_session}`")

    pos = nx.spring_layout(G, seed=42)
    node_labels = {n: G.nodes[n]['label'] for n in G.nodes}
    node_colors = [G.nodes[n].get('ethics', 0.5) for n in G.nodes]

    fig, ax = plt.subplots(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, labels=node_labels, node_color=node_colors,
            cmap=plt.cm.viridis, node_size=1500, font_size=10, edge_color='gray', ax=ax)

    st.pyplot(fig)

    st.markdown("### 🔍 Node Details:")
    for node in G.nodes:
        data = G.nodes[node]
        st.write(f"**{node}**")
        st.json({
            "Archetype": data['label'],
            "Symbolic Output": data['output'],
            "Ethics Rating": data['ethics']
        })
