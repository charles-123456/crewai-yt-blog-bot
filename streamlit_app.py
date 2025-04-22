# streamlit_app.py

import streamlit as st
from crewai import Crew, Process
from agents import get_agents
from tasks import get_tasks
from tools import create_yt_tool
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")  # For safety

st.set_page_config(page_title="YT Blog Bot", layout="centered")
st.title("📽️ YouTube Blog Writer 🤖")

# --- Step 1: Inputs ---
with st.form("yt_blog_form"):
    youtube_handle = st.text_input("Enter YouTube Channel Handle (e.g., @krishnaik06)", value="@krishnaik06")
    topic = st.text_input("Enter Topic to Research (e.g., AI vs ML vs DL)", value="AI vs ML vs DL vs Data Science")
    submitted = st.form_submit_button("Generate Blog")

# --- Step 2: Kickoff Crew ---
if submitted:
    with st.spinner("Generating blog post from YouTube channel..."):
        yt_tools = create_yt_tool(youtube_handle)
        blog_researcher, blog_writer = get_agents(yt_tools)
        research_task, write_task = get_tasks(blog_researcher, blog_writer, yt_tools)

        crew = Crew(
            agents=[blog_researcher, blog_writer],
            tasks=[research_task, write_task],
            process=Process.sequential
        )

        result = crew.kickoff(inputs={"topic": topic})
        st.success("✅ Blog generated!")
        st.markdown("### ✍️ Generated Blog Post")
        st.markdown(result)
