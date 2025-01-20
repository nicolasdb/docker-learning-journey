 # Level 1: Container Basics 🎮

## Objectives
- Understand basic Docker concepts
- Run and manage single containers
- Handle container networking
- Deploy an AI model in a container

## Tutorial Content

### 1. First Steps
```bash
# Check Docker installation
docker --version
docker info

# Your first container
docker run hello-world
```

### 2. Running Nginx (Practice Run)
```bash
# Pull nginx image
docker pull nginx

# Run nginx with port mapping
docker run -d -p 8080:80 --name my-webserver nginx

# Check if it's running
curl localhost:8080
```

Understanding what happened:
- `-d`: Run in detached mode (background)
- `-p 8080:80`: Map host port 8080 to container port 80
- `--name`: Give your container a friendly name

### 3. Container Management
```bash
# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop container
docker stop my-webserver

# Remove container
docker rm my-webserver
```

### 4. Working with Container Logs
```bash
# View container logs
docker logs my-webserver

# Follow log output
docker logs -f my-webserver
```

### 5. Container Resource Management
```bash
# View container resource usage
docker stats my-webserver

# Set resource limits
docker run -d --memory="2g" --cpus="1.5" nginx
```

## 🗡️ Mini-Boss Challenge: Deploy Ollama with Llama2

Your challenge is to:
1. Pull and run Ollama
2. Install the Llama2 model
3. Test basic model interaction
4. Ensure container restarts automatically
5. Monitor resource usage

### Victory Conditions 🏆

Create a file `solutions/level1/ollama-setup.sh` with your commands:

```bash
#!/bin/bash

# Pull Ollama image
docker pull ollama/ollama

# Run Ollama with appropriate settings
docker run -d \
  --gpus all \  # Optional: if you have GPU
  -v ollama_data:/root/.ollama \
  -p 11434:11434 \
  --restart unless-stopped \
  --name ollama \
  ollama/ollama

# Wait for Ollama to start
sleep 5

# Pull Llama2 model
docker exec ollama ollama pull llama2

# Test the model
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt": "Say hello!"
}'
```

### Acceptance Criteria ✅

Your solution must:
- [ ] Successfully run Ollama container
- [ ] Have Llama2 model installed
- [ ] Be accessible via localhost:11434
- [ ] Persist model data between restarts
- [ ] Auto-restart on failure
- [ ] Handle resource limits appropriately

### Hints 🎯
- Check container logs if things aren't working
- Monitor memory usage during model download
- Test container restart behavior
- Verify model persistence after container recreation

### Need Help? 
Check `patterns/volumes/persistence.md` for data persistence examples.

## Level Completion
Once you've completed the mini-boss challenge:
1. Test your setup thoroughly
2. Document any issues and solutions
3. Commit your solution to your quest branch
4. Move on to Level 2!