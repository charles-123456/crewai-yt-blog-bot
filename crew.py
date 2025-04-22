from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task
import os
from dotenv import load_dotenv

load_dotenv()

# Set the Google API key environment variable
os.environ["GOOGLE_API_KEY"] = "AIzaSyA0exSSxpU6_Yll7mrwRZXrj6vq6mWyJpM"

# Forming the tech-focused crew with explicit LLM configuration
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential
   
)

# Start the task execution process
result = crew.kickoff(inputs={'topic': 'AI VS ML VS DL vs Data Science'})
print(result)