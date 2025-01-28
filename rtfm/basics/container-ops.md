# Container Operations Guide

## Basic Container Lifecycle

### Pull Images

```bash
# Pull specific image
docker pull python:3.9-slim

# Check available images
docker images
```

> **Note:** [Docker Hub](https://hub.docker.com/) is a public repository where Docker images are stored. Once you find the desired image, you can use its name and tag in the docker pull command.

### Run Containers

```bash
# Basic run
docker run python:3.9-slim

# Run interactively
docker run -it python:3.9-slim

# Run in background (detached)
docker run -d python:3.9-slim

# Run with name
docker run --name my-python -d python:3.9-slim

# Run with port mapping
docker run -p 8080:80 nginx
```

> **Note:** When you use a Docker container to run Python, the container typically shuts down because Docker containers are designed to terminate once the primary process inside the container finishes. For more information, search for `Docker primary process` and `Dockerfile`.

### Container Management

```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop container
docker stop <container_name_or_id>

# Start stopped container
docker start <container_name_or_id>

# Remove container
docker rm <container_name_or_id>

# Remove container even if running
docker rm -f <container_name_or_id>
```

### Container Information

```bash
# View container logs
docker logs <container_name_or_id>

# Follow log output
docker logs -f <container_name_or_id>

# View container details
docker inspect <container_name_or_id>

# See container resource usage
docker stats <container_name_or_id>
```

## Common Options

- `-d`: Run in detached mode (background)
- `-it`: Interactive with terminal
- `-p`: Port mapping (host:container)
- `--name`: Assign container name
- `-v`: Mount volume
- `--rm`: Remove container when it exits

## Best Practices

- Always name your containers for easier reference
- Clean up unused containers regularly
- Check logs when troubleshooting
- Use appropriate base images (e.g., slim versions for smaller footprint)
