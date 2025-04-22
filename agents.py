# from crewai import Agent
# from tools import yt_tools
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# import os
# from crewai.llm import LLM

# load_dotenv()

# # Make sure GOOGLE_API_KEY is properly set
# os.environ["GOOGLE_API_KEY"] = "AIzaSyA0exSSxpU6_Yll7mrwRZXrj6vq6mWyJpM"

# # Call the gemini models
# # llm = ChatGoogleGenerativeAI(
# #     model="gemini/gemini-1.5-flash",
# #     verbose=True,
# #     temperature=0.5,
# #     google_api_key=os.environ["GOOGLE_API_KEY"]
# # )
# llm = LLM(
#     model="gemini/gemini-1.5-flash",
#     provider="google",  # ✅ Specify the provider
#     api_key="AIzaSyA0exSSxpU6_Yll7mrwRZXrj6vq6mWyJpM"
# )

# # Create a senior blog content researcher
# blog_researcher = Agent(
#     role='Blog Researcher from Youtube Videos',
#     goal='get the relevant video transcription for the topic {topic} from the provided Yt channel',
#     verbose=True,  # Fixed typo from "verboe"
#     memory=True,
#     backstory=(
#        "Expert in understanding videos in AI Data Science, Machine Learning And GEN AI and providing suggestion" 
#     ),
#     tools=[yt_tools],
#     llm=llm,
#     allow_delegation=True
# )

# # Creating a senior blog writer agent with YT tool
# blog_writer = Agent(
#     role='Blog Writer',
#     goal='Narrate compelling tech stories about the video {topic} from YT video',
#     verbose=True,
#     memory=True,
#     backstory=(
#         "With a flair for simplifying complex topics, you craft "
#         "engaging narratives that captivate and educate, bringing new "
#         "discoveries to light in an accessible manner."
#     ),
#     tools=[yt_tools],
#     llm=llm,
#     allow_delegation=False
# )
from crewai import Agent
from crewai.llm import LLM
import os

def get_agents(yt_tool):
    llm = LLM(
        model="gemini/gemini-1.5-flash",
        provider="google",
        api_key=os.getenv("GOOGLE_API_KEY")
    )

    blog_researcher = Agent(
        role='Blog Researcher from Youtube Videos',
        goal='Get video transcripts related to {topic}',
        verbose=True,
        memory=True,
        backstory="Expert in AI/Data Science video analysis",
        tools=[yt_tool],
        llm=llm,
        allow_delegation=True
    )

    blog_writer = Agent(
        role='Blog Writer',
        goal='Write engaging blog post from YouTube content',
        verbose=True,
        memory=True,
        backstory="Skilled at writing simple, educational tech blogs",
        tools=[yt_tool],
        llm=llm,
        allow_delegation=False
    )

    return blog_researcher, blog_writer
