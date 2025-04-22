# from crewai_tools import YoutubeChannelSearchTool

# # Initialize the tool with a specific Youtube channel handle to target your search

# yt_tools = YoutubeChannelSearchTool(
#     youtube_channel_handle='@krishnaik06',  # Required param
#     config=dict(
#         llm=dict(
#             provider="google",
#             config=dict(
#                 model="gemini-1.5-flash-002",  # Gemini LLM
#                 # Optional: temperature, top_p, etc.
#             ),
#         ),
#         embedder=dict(
#             provider="google",
#             config=dict(
#                 model="models/embedding-001",  # Gemini embedding model
#                 task_type="retrieval_document",
#                 # Optional: title="Embeddings",
#             ),
#         ),
#     )
# )
from crewai_tools import YoutubeChannelSearchTool

def create_yt_tool(channel_handle):
    return YoutubeChannelSearchTool(
        youtube_channel_handle=channel_handle,
        config=dict(
            llm=dict(
                provider="google",
                config=dict(
                    model="gemini-1.5-flash-002",
                ),
            ),
            embedder=dict(
                provider="google",
                config=dict(
                    model="models/embedding-001",
                    task_type="retrieval_document",
                ),
            ),
        )
    )
