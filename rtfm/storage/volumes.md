# Docker Storage: Volumes vs Bind Mounts

## Volumes

Docker-managed storage units, perfect for data persistence.

### Data Persistence

> TLDR: Docker volumes are managed by Docker and are not directly accessible from the host, while bind mounts provide direct access to host directories and files from within the container.

1. **Named Volumes**:
   - Created and managed by Docker using commands like `docker volume create`.
   - Stored in a part of the host filesystem managed by Docker (`/var/lib/docker/volumes/` on Linux).
   - Not directly accessible or visible from the host filesystem without using Docker commands.
   - Ideal for data that needs to persist across container restarts and removals, and for sharing data between containers.
2. **Bind Mounts**:
   - Directly map a specific directory or file on the host filesystem to a directory or file inside the container.
   - Specified using the `-v` or `--mount` flag with the full path of the host directory.
   - Changes in the host directory are immediately reflected in the container and vice versa.
   - Useful for development environments where you need direct access to files from both the host and the container.

### Key Commands

```bash
# Create volume
docker volume create my_volume

# List volumes
docker volume ls

# Inspect volume
docker volume inspect my_volume

# Use volume with container
docker run -v my_volume:/container/path image_name
```

## Types of Persistence

### Named Volumes

Docker-managed persistent storage

```bash
# Create volume
docker volume create my_data

# Use volume with container
docker run -v my_data:/container/path my-image

# List volumes
docker volume ls

# Inspect volume
docker volume inspect my_data

# Remove volume
docker volume rm my_data
```

### Bind Mounts

Direct mapping to host filesystem

```bash
# Mount host directory
docker run -v /host/path:/container/path my-image

# Mount current directory
docker run -v $(pwd):/container/path my-image
```

## HedgeDoc Example

```bash
# Create volume for HedgeDoc data
docker volume create hedgedoc_data

# Run HedgeDoc with persistence
docker run -d \
  -v hedgedoc_data:/hedgedoc/public/uploads \
  -p 3000:3000 \
  --name hedgedoc \
  hedgedoc/hedgedoc:latest
```

## Best Practices

- Use named volumes for application data
- Use bind mounts for development
- Always back up important volumes
- Clean up unused volumes regularly
- Set appropriate permissions

## Backup and Restore

```bash
# Backup volume
docker run --rm -v my_volume:/source -v $(pwd):/backup alpine \
  tar czf /backup/my_volume_backup.tar.gz /source

# Restore volume
docker run --rm -v my_volume:/dest -v $(pwd):/backup alpine \
  tar xzf /backup/my_volume_backup.tar.gz -C /dest
```
