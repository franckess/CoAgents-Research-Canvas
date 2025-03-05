"""Demo"""

import os
from dotenv import load_dotenv

# Load environment variables at the very beginning
load_dotenv()

# Verify API keys are present
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is not set")
if not os.getenv("TAVILY_API_KEY"):
    raise ValueError("TAVILY_API_KEY environment variable is not set")

# pylint: disable=wrong-import-position
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from copilotkit.integrations.fastapi import add_fastapi_endpoint
from copilotkit import CopilotKitRemoteEndpoint, LangGraphAgent
from research_canvas.crewai.crewai_agent import CrewAIAgent
from research_canvas.crewai.agent import ResearchCanvasFlow
from research_canvas.langgraph.agent import graph

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

sdk = CopilotKitRemoteEndpoint(
    agents=[
        CrewAIAgent(
            name="research_agent_crewai",
            description="Research agent.",
            flow=ResearchCanvasFlow(),
        ),
        LangGraphAgent(
            name="research_agent",
            description="Research agent.",
            graph=graph,
        ),
        LangGraphAgent(
            name="research_agent_google_genai",
            description="Research agent.",
            graph=graph
        ),
    ],
)

# Add the CopilotKit endpoint
add_fastapi_endpoint(app, sdk, "/copilotkit")

@app.get("/health")
def health():
    """Health check."""
    return {"status": "ok"}

@app.get("/")
def root():
    """Root endpoint."""
    return {"message": "Research Canvas API is running"}

def main():
    """Run the uvicorn server."""
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(
        "research_canvas.demo:app",
        host="0.0.0.0",
        port=port,
        reload=False  # Disable reload in production
    )