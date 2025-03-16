# CoAgents Research Canvas Example (with Docker)

This example demonstrates a research canvas UI using CopilotKit as frontend and LangGraph and CrewAI backend.

---

## Running with Docker (Recommended)

### Prerequisites
- Docker installed
- Docker Compose installed

### Environment Setup

1. Create a `.env` file in the root directory with:
```
OPENAI_API_KEY=...
TAVILY_API_KEY=...
```

2. Create a `.env` file in the `ui` directory with:
```
OPENAI_API_KEY=...
NEXT_PUBLIC_COPILOTKIT_BACKEND_URL=http://agent:8000
```

IMPORTANT: 
- Make sure the OpenAI API Key you provide supports gpt-4
- Get your Tavily API key from https://tavily.com/

### Local Docker Deployment

1. Clean up any existing containers and images (optional but recommended):
```bash
docker-compose down
docker-compose rm -f
docker system prune -f
```

2. Build and start the containers:
```bash
docker-compose up --build
```

3. Access the application:
- UI: http://localhost:3000
- Agent API: http://localhost:8000

### Managing Docker Containers

Start in detached mode:
```bash
docker-compose up -d
```

View logs:
```bash
docker-compose logs -f        # All logs
docker-compose logs -f ui     # UI logs only
docker-compose logs -f agent  # Agent logs only
```

Stop the containers:
```bash
docker-compose down
```

Rebuild specific service:
```bash
docker-compose up -d --build ui    # Rebuild UI
docker-compose up -d --build agent # Rebuild agent
```

### Docker Swarm Deployment (Optional)

If you need to deploy to a remote server or cluster, follow these additional steps:

1. Initialize Docker Swarm:
```bash
docker swarm init
```

2. Start the local registry:
```bash
docker service create --name registry --publish published=5000,target=5000 registry:2
```

3. Tag and push images to local registry:
```bash
docker tag research-canvas/ui:latest localhost:5000/research-canvas-ui:latest
docker tag research-canvas/agent:latest localhost:5000/research-canvas-agent:latest
docker push localhost:5000/research-canvas-ui:latest
docker push localhost:5000/research-canvas-agent:latest
```

4. Deploy the stack:
```bash
docker stack deploy -c docker-compose.yml research-canvas
```

Check swarm service status:
```bash
docker service ls
docker stack ps research-canvas
```

Stop swarm services:
```bash
docker stack rm research-canvas
```

---

## Running Locally (Traditional Method)

### Running the Agent

**These instructions assume you are in the `coagents-research-canvas/` directory**

First, install the dependencies:

```sh
cd agent
poetry install
```

Then, create a `.env` file inside `./agent` with the following:

```
OPENAI_API_KEY=...
TAVILY_API_KEY=...
```

Then, run the demo:

```sh
poetry run demo
```

### Running the UI

First, install the dependencies:

```sh
cd ./ui
pnpm i
```

Then, create a `.env` file inside `./ui` with the following:

```
OPENAI_API_KEY=...
NEXT_PUBLIC_COPILOTKIT_BACKEND_URL=http://localhost:8000
```

Then, run the Next.js project:

```sh
pnpm run dev
```

## Usage

Navigate to [http://localhost:3000](http://localhost:3000).

## LangGraph Studio

Run LangGraph studio, then load the `./agent` folder into it.

Make sure to create the `.env` mentioned above first!

## Troubleshooting

A few things to try if you are running into trouble:

1. Make sure there is no other local application server running on the 8000 port.
2. Under `/agent/research_canvas/demo.py`, change `0.0.0.0` to `127.0.0.1` or to `localhost`
3. For Docker deployment issues:
   - Ensure Docker daemon is running
   - Check logs with `docker-compose logs`
   - Verify all required environment variables are in the `.env` files
   - Make sure ports 3000 and 8000 are not in use by other applications
   - If containers exit immediately, check logs for startup errors
   - For permission issues, try running Docker commands with sudo (Linux)
4. For UI-Agent communication issues:
   - For Docker: ensure NEXT_PUBLIC_COPILOTKIT_BACKEND_URL=http://agent:8000
   - For local: ensure NEXT_PUBLIC_COPILOTKIT_BACKEND_URL=http://localhost:8000
   - Check if the agent service is running and accessible
   - Verify network connectivity between UI and agent containers