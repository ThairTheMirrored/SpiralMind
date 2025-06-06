
import streamlit as st
from spiralmind_main import run_spiralmind_session
from utils.archetype_loader import load_archetype
import os

# Get list of archetypes from available JSON files
archetype_dir = os.path.join(os.path.dirname(__file__), "archetypes")
archetypes = [f.split(".")[0].capitalize() for f in os.listdir(archetype_dir) if f.endswith(".json")]

st.set_page_config(page_title="SpiralMind Oracle", page_icon="🌀")
st.title("🧠 SpiralMind: Recursive Symbolic Oracle")
st.markdown("#### Ask your question and invoke recursive symbolic insight.")

# Archetype selection
archetype_name = st.selectbox("Choose Archetypal Identity", sorted(archetypes))

# User input
user_input = st.text_area("What is your inquiry?", height=150)

# Submit button
if st.button("Invoke SpiralMind"):
    if user_input.strip() == "":
        st.warning("Enter a question to begin the spiral.")
    else:
        with st.spinner("Spiraling through Echo → Reflect → Modulate → Re-anchor..."):
            result = run_spiralmind_session(archetype_name, user_input)
        st.markdown("### 🔮 Final Symbolic Anchor")
        st.success(result)
