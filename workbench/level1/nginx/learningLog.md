## Thought Process for Volume Persistence and Logging

### Initial Setup

Initially, we used the official Nginx image to serve a static HTML file. The Dockerfile looked like this:

```dockerfile
# Use the official Nginx image from the Docker Hub
FROM nginx:latest

# Set the working directory in the container
WORKDIR /usr/share/nginx/html

# Copy the HTML file into the container
COPY index.html .

# Expose the port
EXPOSE 80

# Create a named volume to persist data
VOLUME /usr/share/nginx/html/data

# Set the default command to run when the container starts
CMD ["nginx", "-g", "daemon off;"]
```

### Requirement for Logging

To test the permanence of the volume, we wanted to add an input feature on the `index.html` page, log all entries in a `.log` file, and display the content at the end of the web page. This required server-side scripting to handle form submissions and log entries.

### Switching to Node.js

Nginx is a powerful web server but does not support server-side scripting directly. To handle form submissions and log entries, we needed a server-side language like Node.js. Therefore, we switched from the Nginx image to the Node.js image and created a simple Express.js server to handle the logging functionality.

### Updated Dockerfile

The updated Dockerfile uses the Node.js image, installs dependencies, and sets up the volume for data persistence:

```dockerfile
# Use the official Node.js image as the base image
FROM node:latest

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the application files into the container
COPY . .

# Install dependencies
RUN npm install express

# Expose the port
EXPOSE 3000

# Create a volume to persist data
VOLUME /usr/src/app/data

# Set the default command to run when the container starts
CMD ["node", "server.js"]
```

### Running the Container

To build and run the container with the volume:

```bash
# Build the Docker image
docker build -t nodelog .

# Run the container with the volume
docker run -d -p 3000:3000 -v my_log_data:/usr/src/app/data --name test nodelog
```

### Testing Persistence

1. Access the application
2. Submit log entries using the form
3. Stop the container
4. Start the container again
5. Access the app again, verify that the log entries persist

=== WARNING: without `-v my_log_data:/usr/src/app/data` the last logs will be ignore, and a new volume will be created.

### Bonus step: using log.txt from current directory

```bash
./workbench/level1/nginx$ ls
Dockerfile  index.html  learningLog.md  log.txt  server.js
```

`docker run -d -p 3000:3000 -v $(pwd):/usr/src/app/data --name test2 nodelog`
