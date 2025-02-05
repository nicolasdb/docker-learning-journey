# network

>>> could you explain to me the basics of networking configuration in a docker container? is it something else than port mapping?

---

Certainly! Networking configurations in Docker containers can be broadly categorized into two main types: static and dynamic.

## Static Network Configuration

Static network configuration refers to configuring the Docker daemon to use specific IP addresses for communication within a container. This approach works well when you have predefined networks or volumes already set up, as it allows you to control the IP addresses that will be used by your containers.

### Example 1

1. **Predefined Volumes**: If you have a volume mounted on your host machine, Docker can access this volume directly and use its static IP address.
2. **Static IPs**: You might configure an IP address for each container (e.g., `localhost:8080`) that corresponds to the IP address of the network in which it is located.

## Dynamic Network Configuration

Dynamic network configuration involves configuring the Docker daemon to manage network addresses on a per-container basis. This approach provides more flexibility, especially when working with shared storage or networks that require dynamic allocation of IPs.

### Example 2

1. **Shared Storage**: If you use a shared file system (e.g., `--network=host`) and have static IP addresses for each container, Docker will automatically assign the same IP address to all containers running in the same host.
2. **Network Pools**: You can define network pools using the `--network` option with options like `--subnet=<subnet>` or `--cidr=<network-address>`, which assigns a network segment to a single container.

## Key Differences

- **Static vs Dynamic IP Addresses**:
  - **Dynamic Network Configuration**: This approach uses static addresses to ensure that each container can communicate independently and dynamically.
  - **Static IP Addresses**: This is less common but works well for containers running on the same machine with no network connectivity issues.

- **Network Policies**:
  - **Shared Storage Networks**: These networks are managed by Docker, which assigns specific IP addresses to containers based on their locations in the shared storage.
  - **Network Pools**: Similar to dynamic network configurations, these are used when you have static IPs but want to share or limit access across multiple nodes.

- **Flexibility**:
  - **Dynamic Network Configuration**: More flexible as it can handle changes in IP addresses dynamically.
  - **Static IP Addresses**: More restrictive, especially when using shared storage networks, as containers won't know their own IP address unless they have a static network address.

## Best Practices

1. **Use Predefined Volumes or Shared Storage**:
   - If you use pre-defined volumes or share storage, Docker automatically assigns static IPs to the containers.
   - This is more straightforward and less error-prone but may not be ideal if your shared volume needs dynamic allocation of IP addresses.

2. **Dynamic Network Configuration**:
   - When possible, choose a shared storage solution where static IP addresses can be configured dynamically.
   - If you must use shared storage, ensure that your network infrastructure supports the required dynamic assignment of IPs to containers.

By using either approach, you gain more control over how your containers communicate within a Docker container. The choice between them depends on specific requirements such as shared storage, file system management, or network connectivity needs.

---

> mhe, Tooo advance for me 😵‍💫
