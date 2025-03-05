FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements first
COPY pyproject.toml ./

# Install poetry and dependencies
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-root

# Copy the rest of the application
COPY . .

# Make sure the application is in the Python path
ENV PYTHONPATH=/app

# Create a .env file if it doesn't exist
RUN touch .env

# Expose the port
EXPOSE 8000

# Run the application with environment variables
CMD ["sh", "-c", "echo \"OPENAI_API_KEY=${OPENAI_API_KEY}\nTAVILY_API_KEY=${TAVILY_API_KEY}\" > .env && poetry run demo"]