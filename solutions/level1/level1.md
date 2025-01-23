# Level 1: Getting Started with Docker 🎮

## Step 1: Docker Setup Verification

### Permissions Check

After installing Docker Desktop (or Docker Engine), ensure proper permissions:

```bash
# Add your user to docker group
sudo usermod -aG docker $USER

# Apply new group membership (or logout/login)
newgrp docker

# Verify setup
docker run hello-world
```

## Step 2: Basic Container Operations

Let's master the basic container lifecycle using hello-world and nginx:

### Container Lifecycle

```bash
# Pull and run hello-world
docker run hello-world

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Notice the random name assigned to hello-world container
CONTAINER ID   IMAGE                            COMMAND                  CREATED          STATUS                      PORTS     NAMES
6a239f534287   hello-world                      "/hello"                 14 seconds ago   Exited (0) 12 seconds ago             admiring_raman
# Remove it using the name or ID
docker rm <container id or name>
```

### Practice with Nginx

```bash
# Pull nginx image
docker pull nginx

# Run with specific port mapping and name 
docker run -d -p 8080:80 --name test-nginx nginx
```

Understanding what happened:

- `-d`: Run in detached mode (background)
- `-p 8080:80`: Map host port 8080 to container port 80
- `--name`: Give your container a friendly name

```bash
# Verify it's running
curl localhost:8080  # Or check http://localhost:8080 in browser
```

## Step 3: Container Management and Monitoring

### Logs and Resource Monitoring

```bash
# View container logs
docker logs test-nginx

# Follow log output
docker logs -f test-nginx

# Check container resource usage
docker stats test-nginx
```

### Data Persistence

TLDR: Docker volumes are managed by Docker and are not directly accessible from the host, while bind mounts provide direct access to host directories and files from within the container.

1. **Docker Volumes**:
   - Created and managed by Docker using commands like `docker volume create`.
   - Stored in a part of the host filesystem managed by Docker (`/var/lib/docker/volumes/` on Linux).
   - Not directly accessible or visible from the host filesystem without using Docker commands.
   - Ideal for data that needs to persist across container restarts and removals, and for sharing data between containers.
2. **Bind Mounts**:
   - Directly map a specific directory or file on the host filesystem to a directory or file inside the container.
   - Specified using the `-v` or `--mount` flag with the full path of the host directory.
   - Changes in the host directory are immediately reflected in the container and vice versa.
   - Useful for development environments where you need direct access to files from both the host and the container.

```bash
# Create a docker volume
docker volume create nginx-data

# Run container with volume
docker run -d \
  -p 8080:80 \
  -v nginx-data:/usr/share/nginx/html \
  --name test-nginx-persistent \
  nginx
```

The command `docker run -d -p 8080:80 -v nginx-data:/usr/share/nginx/html --name test-nginx-persistent nginx` is used to start a new Docker container running the Nginx web server with specific configurations.

Here's a breakdown of the command:

1. `docker run -d`: This is the base command to create and start a new Docker container in detached mode.

2. `-p 8080:80`: This option maps port 8080 on your host machine to port 80 in the container. Port 80 is the default port for HTTP traffic in the Nginx server.

3. `-v nginx-data:/usr/share/nginx/html`: This flag mounts a Docker volume named `nginx-data` to the directory `/usr/share/nginx/html` inside the container. This setup ensures that any data stored in the Nginx HTML directory persists even if the container is stopped or removed, as the data is stored in the named volume `nginx-data`.

4. `--name test-nginx-persistent`: This option assigns a name, `test-nginx-persistent`, to the container.

5. `nginx`: This is the name of the Docker image to use for the container.

## Step 4: Container Updates and Cleanup

### Updating Containers

```bash
# Pull latest version of an image
docker pull nginx:latest

# Stop and remove old container
docker stop test-nginx
docker rm test-nginx

# Create new container with latest image
docker run -d -p 8080:80 --name test-nginx nginx:latest
```

### Cleanup Operations

```bash
# Remove a specific container
docker rm <container_id_or_name>

# Remove a specific image
docker rmi <image_id_or_name>

# Remove all stopped containers
docker container prune

# Remove unused images
docker image prune

# Remove all unused volumes
docker volume prune

# Remove all unused networks
docker network prune

# Remove everything unused (containers, images, volumes, networks)
docker system prune

```

## Mini-Boss Challenges

### Challenge 1: Container Mastery

Complete these tasks:

- [ ] Pull and Run 3 different docker images
- [ ] Monitor their resource usage
- [ ] Clean up all containers and images properly
- [ ] Use both CLI and Docker Desktop GUI to manage containers

#### Rewards

1. Basic Container Operations
   - [x] Can run/stop/remove containers confidently
   - [x] Understand container naming and identification
   - [x] Comfortable with both CLI and GUI operations

2. Resource Management
   - [x] Can monitor container logs
   - [x] Understand basic volume management
   - [ ] Can update containers safely

### Challenge 2: Deploy Ollama

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
- [ ] Get responses from the model

### Hints 🎯

- Check container logs if things aren't working
- Monitor memory usage during model download
- Test container restart behavior
- Verify model persistence after container recreation

## Bonus Knowledge

- Check `patterns/` directory for common command patterns
- Understand the difference between:
  - Container removal (`docker rm`)
  - Image removal (`docker rmi`)
  - Volume management (`docker volume`)

## Level Completion

Once you've completed the mini-boss challenge:

1. Test your setup thoroughly
2. Document any issues and solutions
3. Commit your solution to your quest branch

## Next Level Preview

In Level 2, we'll explore Docker Compose to manage multiple containers together!
