# from crewai import Task
# from tools import yt_tools
# from agents import blog_researcher, blog_writer

# # Research Task
# research_task = Task(
#     description=(
#         "Identify the video about {topic}. "
#         "Get detailed information about the video from the channel video."
#     ),
#     expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content.',
#     tools=[yt_tools],
#     agent=blog_researcher,
# )

# # Writing task with language model configuration
# write_task = Task(
#     description=(
#         "Get the info from the youtube channel on the topic {topic}."
#     ),
#     expected_output='Summarize the info from the youtube channel video on the topic {topic} and create the content for the blog',
#     tools=[yt_tools],
#     agent=blog_writer,
#     async_execution=False,
#     output_file='new-blog-post.md'  # Example of output customization
# )
from crewai import Task

def get_tasks(blog_researcher, blog_writer, yt_tool):
    research_task = Task(
        description="Find video about {topic} and extract relevant insights.",
        expected_output="A 3-paragraph detailed report on {topic}.",
        tools=[yt_tool],
        agent=blog_researcher,
    )

    write_task = Task(
        description="Summarize the info from the video on {topic}.",
        expected_output="Complete blog post written for the topic {topic}.",
        tools=[yt_tool],
        agent=blog_writer,
        async_execution=False
    )

    return research_task, write_task
