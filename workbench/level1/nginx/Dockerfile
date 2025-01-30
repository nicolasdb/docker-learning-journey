# Using Node.js alpine as the base image is a good practice because it is lightweight and secure (around 90% smaller than the standard Node.js image)
FROM node:alpine3.20

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the application files into the container
COPY . .

# Install dependencies
RUN npm install express

# Expose the port
EXPOSE 3000

# Create a named volume to persist data
VOLUME /usr/src/app/data

# Set the default command to run when the container starts
CMD ["node", "server.js"]


# In this case, the command is `nginx`, which is a popular web server. The `-g` flag is used to pass a global directive to Nginx. The directive `daemon off;` tells Nginx to run in the foreground rather than as a background daemon. This is important in the context of Docker because Docker containers are designed to run a single process in the foreground. If Nginx were to run as a daemon, the container would exit immediately after starting, as Docker would think the main process has finished.
# This setup is common in Dockerized applications that use Nginx as a web server or reverse proxy.