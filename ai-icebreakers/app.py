import os
import streamlit as st
from google import genai
from google.genai import types
import random

st.set_page_config(page_title="AI Icebreakers!", layout="centered", page_icon="🧊")

# Load custom CSS
def local_css(file_name: str):
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Style file '{file_name}' not found.")

local_css("style.css")

# Initialise Gemini API client
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("Environment variable 'GEMINI_API_KEY' not set.")
    st.stop()
client = genai.Client(api_key=api_key)

# Display logo in the centre column
top_cols = st.columns(3)
with top_cols[1]:
    st.image("Logo2.png", use_container_width=True)

# Retrieve URL parameters
params = st.query_params
param_keys = ["event", "event_subject", "audience", "additional_notes"]
values = { key: params.get(key, [None])[0] if isinstance(params.get(key), list) else params.get(key) for key in param_keys }

# List of 30 adjectives for icebreakers
adjectives = [
    "fun", "creative", "poignant", "random", "smart",
    "witty", "thoughtful", "quirky", "clever", "friendly",
    "lighthearted", "engaging", "unexpected", "memorable", "insightful",
    "humorous", "energetic", "intriguing", "warm", "bold",
    "spontaneous", "sharp", "playful", "charming", "original",
    "stimulating", "imaginative", "dynamic", "refreshing", "captivating"
]

# Pick one adjective at random
random_adjective = random.choice(adjectives)

# Function to build and send prompt
def generate_icebreaker():
    prompt = f"Generate a short and {random_adjective} icebreaker to get to know someone"
    if values.get("event") and random.random() < 0.8:
        prompt += f" at a {values['event']}"
    if values.get("event_subject") and random.random() < 0.5:
        prompt += f" about {values['event_subject']}"
    if values.get("audience") and random.random() < 0.5:
        prompt += f" who may be {values['audience']}"
    if values.get("additional_notes") and random.random() < 0.3:
        prompt += f". {values['additional_notes']}"
    prompt += ". The response must be less than 20 words."
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            temperature=random.uniform(0,2)
        )
    )
    return response.text

# Ensure one-time generation
if 'icebreaker' not in st.session_state:
    st.session_state['icebreaker'] = generate_icebreaker()

# Display icebreaker as subtitle
st.subheader(st.session_state['icebreaker'])

# Regenerate button only
if st.button("Regenerate Icebreaker", width="stretch"):
    st.session_state['icebreaker'] = generate_icebreaker()
    st.rerun()
