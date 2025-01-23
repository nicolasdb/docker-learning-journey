# Dockerfile Basics

## What is a Dockerfile?

A Dockerfile is a text file containing instructions for building a Docker image. It automates the process of creating consistent and reproducible container images by defining:

- Base image to use
- Files to include
- Commands to run
- Environment setup
- Runtime behavior

## Basic Dockerfile Instructions

```dockerfile
# Use a base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files from host to container
COPY requirements.txt .
COPY app.py .

# Run commands during build
RUN pip install -r requirements.txt

# Set environment variables
ENV PORT=8080

# Command to run when container starts
CMD ["python", "app.py"]
```

### Common Instructions

- `FROM`: Specifies the base image
- `WORKDIR`: Sets the working directory for subsequent instructions
- `COPY`: Copies files from host to container
- `ADD`: Similar to COPY but can also handle URLs and tar files
- `RUN`: Executes commands during image build
- `ENV`: Sets environment variables
- `EXPOSE`: Documents which ports the container listens on
- `CMD`: Default command to run when container starts
- `ENTRYPOINT`: Makes container behave like an executable

## Docker Build Command

```bash
# Basic build
docker build -t myapp:1.0 .

# Build with different Dockerfile
docker build -f Dockerfile.dev -t myapp:dev .

# Build with build arguments
docker build --build-arg VERSION=1.0 -t myapp .

# Build without using cache
docker build --no-cache -t myapp .
```

### Common Build Options

- `-t`: Tag the image
- `-f`: Specify Dockerfile path
- `--build-arg`: Pass build-time variables
- `--no-cache`: Build without using cache
- `--pull`: Always pull newer version of base image

## Container Lifecycle and Python

### Understanding Auto-Stop Behavior

Python containers often stop immediately because:

1. The container's main process (defined by CMD/ENTRYPOINT) completes
2. Python scripts exit after execution
3. No foreground process keeps the container running

### Solutions for Keeping Containers Running

1. Interactive Mode:

    ```bash
    # Run with terminal
    docker run -it python:3.9-slim

    # Run with bash shell
    docker run -it python:3.9-slim bash
    ```

2. Long-Running Service:

    ```dockerfile
    # Example Dockerfile for a web service
    FROM python:3.9-slim
    WORKDIR /app
    COPY app.py .
    CMD ["python", "-m", "http.server"]
    ```

3. Infinite Loop:

    ```python
    # Example for a background service
    import time
    while True:
        # Do work
        time.sleep(60)
    ```

## Best Practices

1. **Base Images**
   - Use official images
   - Prefer slim/alpine variants for smaller size
   - Specify exact version tags
2. **Layer Optimization**
   - Group related RUN commands
   - Place infrequently changing layers first
   - Use .dockerignore for unnecessary files
3. **Security**
   - Don't run as root
   - Remove unnecessary tools
   - Keep base images updated
4. **Multi-stage Builds**

    ```dockerfile
    # Build stage
    FROM python:3.9 AS builder
    COPY . .
    RUN pip install --user -r requirements.txt

    # Runtime stage
    FROM python:3.9-slim
    COPY --from=builder /root/.local /root/.local
    COPY app.py .
    CMD ["python", "app.py"]
    ```

    > **note:** The multi-stage build helps to keep the final image size small by separating the build dependencies from the runtime environment.
   - The build stage installs the necessary dependencies.
   - The runtime stage copies only the necessary files and dependencies, resulting in a leaner image.

## Troubleshooting

1. **Container Stops Immediately**
   - Check logs: `docker logs <container>`
   - Verify CMD/ENTRYPOINT configuration
   - Ensure main process doesn't exit
2. **Build Fails**
   - Review build logs
   - Check file paths and permissions
   - Verify base image compatibility
3. **Container Won't Start**
   - Check port conflicts
   - Verify environment variables
   - Inspect resource constraints
4. **Performance Issues**
   - Use multi-stage builds
   - Optimize layer caching
   - Clean up unnecessary files
