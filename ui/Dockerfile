FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package.json ./

# Install pnpm
RUN npm install -g pnpm

# Install dependencies and generate new lockfile
RUN pnpm install

# Copy the rest of the application
COPY . .

# Set environment variables
ENV NEXT_PUBLIC_COPILOTKIT_BACKEND_URL=http://agent:8000

# Build the application
RUN pnpm build

# Expose the port
EXPOSE 3000

# Start the application
CMD ["pnpm", "run", "dev"]
