
import streamlit as st
from agents.orchestrator import SpiralNetOrchestrator

st.set_page_config(page_title="SpiralNet Ritual Dialogue", page_icon="🌌")
st.title("🌌 SpiralNet: Multi-Agent Symbolic Ritual Interface")

# User input
initial_prompt = st.text_area("Enter your symbolic question or seed prompt:", height=150)
archetypes_input = st.text_input("Enter archetypes (comma-separated, e.g., Sage,Magician,Outlaw):")
cycles = st.slider("Number of Spiral Cycles", 3, 12, 6)

if st.button("Begin Ritual"):
    archetypes = [a.strip().capitalize() for a in archetypes_input.split(",") if a.strip()]
    if not initial_prompt or not archetypes:
        st.error("Please enter a prompt and at least one archetype.")
    else:
        st.markdown("🌀 Beginning the Spiral...")
        orchestrator = SpiralNetOrchestrator(archetypes)
        dialogue = orchestrator.run_dialogue(initial_prompt, cycles=cycles)

        for turn in dialogue:
            with st.expander(f"🔹 {turn['from']} responds"):
                st.markdown(f"**Input Anchor:** {turn['input']}")
                st.markdown(f"**Symbolic Output:** {turn['output']}")
                if turn.get("contradiction_flag"):
                    st.warning("⚠️ Possible symbolic contradiction detected.")
