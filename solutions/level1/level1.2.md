# What is "Dockerfile"

To containerize a simple Python service that prints "Hello World" using Docker, follow these steps:

## Prerequisites

- Ensure you have **Docker** installed on your machine. You can download it from the official Docker website.

## Step-by-Step Guide

### 1. Create Project Directory

Start by creating a new directory for your project:

```bash
mkdir python-hello-world
cd python-hello-world
```

### 2. Create Python Script

Inside the `python-hello-world` directory, create a file named `hello-world.py` and add the following code:

```python
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
```

### 3. Create Dockerfile

Next, create a file named `Dockerfile` in the same directory. This file will contain instructions for building your Docker image. Add the following content to the `Dockerfile`:

```dockerfile
# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Python script into the container
COPY hello-world.py .

# Command to run the Python script
CMD ["python", "./hello-world.py"]
```

### 4. Build the Docker Image

Open your terminal and navigate to your project directory (`python-hello-world`). Run the following command to build your Docker image:

```bash
docker build -t python-hello-world .
```

This command tells Docker to build an image with the tag `python-hello-world` using the current directory (`.`) as context.

### 5. Run the Docker Container

Now that you have built your image, you can run it with:

```bash
docker run python-hello-world
```

Upon running this command, you should see "Hello World!" printed in your terminal.

## Summary of Commands

Here’s a quick summary of all commands used:

```bash
mkdir python-hello-world
cd python-hello-world
# Create hello-world.py and add Python code here...
# Create Dockerfile and add Docker instructions here...
docker build -t python-hello-world .
docker run python-hello-world
```

By following these steps, you have successfully containerized a simple Python service using Docker! This process can be adapted for more complex applications by adding dependencies and additional configurations as needed.
