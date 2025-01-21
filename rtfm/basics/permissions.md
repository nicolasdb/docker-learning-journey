# Docker Permissions Guide

## Story Context → Technical Reality
- "Connection established" → Docker daemon accessible
- "Proper access rights" → Docker group membership
- "First contact" → Initial container test


### Test Container Access
```bash
# Run test container
docker run hello-world
```

Success looks like:
```
Hello from Docker!
This message shows that your installation appears to be working correctly...
```

## Troubleshooting Tips
- Always log out and back in after group changes
- Use `groups` command to verify docker group membership
- Check Docker daemon status if containers won't start

### Permission Denied Error
If you see:
```bash
docker: permission denied while trying to connect to the Docker daemon socket
```

This means your user needs access to the Docker daemon. Fix it with:
```bash
# Add your user to docker group
sudo usermod -aG docker $USER

# Apply new group membership
newgrp docker
```

### Verify Installation

Basic checkup:
```bash
# Check Docker version
docker --version

# Check Docker service status
sudo systemctl status docker

# Start Docker if needed
sudo systemctl start docker
```