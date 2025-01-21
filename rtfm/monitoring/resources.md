# Docker Monitoring Guide

## Resource Management

### View Resource Usage
```bash
# Monitor all containers
docker stats

# Monitor specific container
docker stats <container_name>

# Get one-time stats
docker stats --no-stream
```

### Set Resource Limits
```bash
# Limit memory
docker run -m 512m my-image

# Limit CPU
docker run --cpus=".5" my-image

# Both memory and CPU
docker run -m 512m --cpus=".5" my-image
```

## Container Health

### Logs
```bash
# View logs
docker logs <container_name>

# Follow logs
docker logs -f <container_name>

# Show timestamps
docker logs -t <container_name>

# Show last n lines
docker logs --tail 100 <container_name>
```

### Container Status
```bash
# View container details
docker inspect <container_name>

# Format specific info
docker inspect -f '{{.State.Status}}' <container_name>
```

## Auto-Restart Policies

```bash
# Always restart
docker run --restart always my-image

# Restart on failure
docker run --restart on-failure my-image

# Restart unless stopped
docker run --restart unless-stopped my-image
```

## Ollama Specific

### Resource Requirements
- Minimum 8GB RAM recommended
- CPU with AVX2 support
- Storage for models (varies by model)

### Monitoring Example
```bash
# Run Ollama with resource limits
docker run -d \
  --name ollama \
  -p 11434:11434 \
  -v ollama_data:/root/.ollama \
  --restart unless-stopped \
  -m 8g \
  --cpus="2.0" \
  ollama/ollama

# Monitor usage
docker stats ollama
```

## Best Practices
- Monitor resource usage regularly
- Set appropriate limits based on application needs
- Use restart policies for stability
- Check logs for troubleshooting
- Keep system resources in mind when running AI models