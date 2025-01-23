# hedgedoc container

pull from https://hub.docker.com/r/linuxserver/hedgedoc

- postgres environment secret?
- bindmount volumes link with obsidian
- run recommanded command:

```bash
docker run -d \
  --name=hedgedoc \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -e DB_HOST="<hostname or ip>" \
  -e DB_PORT=3306 \
  -e DB_USER=hedgedoc \
  -e DB_PASS="<secret password>" \
  -e DB_NAME=hedgedoc \
  -e CMD_DOMAIN=localhost \
  -e CMD_URL_ADDPORT=false `#optional` \
  -e CMD_PROTOCOL_USESSL=false `#optional` \
  -e CMD_PORT=3000 `#optional` \
  -e CMD_ALLOW_ORIGIN=['localhost'] `#optional` \
  -e CMD_DB_DIALECT= `#optional` \
  -p 3000:3000 \
  -v /home/nicolas/github/docker-learning-journey/solutions/level1/hedgedoc/config/:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/hedgedoc:latest
```

Error in log, cannot connect to database
Well, make sense. The image from docker hub is published by "linuxserver" and on the main hedgedoc documentation, they point somewhere else for the image and they suggest a docker-compose.yml where postgres is downloaded as a service to hedgedoc, so 2 images to download. There is no trace of that from "linuxserver" version.

```yaml
version: '3'
services:
  database:
    image: postgres:13.4-alpine
    environment:
      - POSTGRES_USER=hedgedoc
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=hedgedoc
    volumes:
      - database:/var/lib/postgresql/data
    restart: always
  app:
    # Make sure to use the latest release from https://hedgedoc.org/latest-release
    image: quay.io/hedgedoc/hedgedoc:1.9.9
    environment:
      - CMD_DB_URL=postgres://hedgedoc:password@database:5432/hedgedoc
      - CMD_DOMAIN=localhost
      - CMD_URL_ADDPORT=true
    volumes:
      - uploads:/hedgedoc/public/uploads
    ports:
      - "3000:3000"
    restart: always
    depends_on:
      - database
volumes:
  database:
  uploads:
```

next: docker-compose is not yet the focus on this level but I'll exercice to connect postgresDB from my supabase account.

## Steps to Connect HedgeDoc to Supabase

Supabase Postgres Docker Connect

When setting up Supabase with Docker, you may encounter issues connecting to the PostgreSQL database. Here are some steps and tips to ensure a successful connection:

1. **Ensure Docker and Docker Compose are Installed**: Make sure Docker and Docker Compose are installed and running on your system. You can install Docker Compose using your distribution's package manager. For Debian and Ubuntu, you can use:

   ```bash
   sudo apt install docker-compose-plugin
   ```

2. **Clone the Supabase Repository**: Clone the Supabase repository from GitHub to your local machine:

   ```bash
   git clone --depth 1 https://github.com/supabase/supabase
   ```

3. **Copy the .env File**: Copy the `.env.example` file to `.env` and customize it with your own keys and passwords:

   ```bash
   cp .env.example .env
   ```

4. **Edit the docker-compose.yml File**: Ensure your `docker-compose.yml` file is correctly configured. You should have a `db` service defined, which includes the PostgreSQL container. Here is an example configuration:

   ```bash
   version: '3'
   services:
     db:
       container_name: supabase-db
       image: supabase/postgres:14.1.0.89
       healthcheck:
         test: pg_isready -U postgres -h localhost
         interval: 5s
         timeout: 5s
         retries: 10
       command:
         - postgres
         - -c
         - config_file=/etc/postgresql/postgresql.conf
         - -c
         - log_min_messages=fatal
       restart: unless-stopped
       ports:
         - ${POSTGRES_PORT}:5432
       environment:
         POSTGRES_HOST: /var/run/postgresql
         POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
       volumes:
         - ./volumes/db/roles.sql:/docker-entrypoint-initdb.d/roles.sql
         - ./postgres-data:/var/lib/postgresql/data
   ```

5. **Start Docker Compose**: Run the following command to start the Supabase services:

   ```bash
   sudo docker compose up -d
   ```

6. **Check Docker Logs**: If you encounter issues, check the logs for the `supabase-auth` container:

   ```bash
   docker logs supabase-auth
   ```

7. **Special Characters in .env File**: Ensure there are no special characters in your `.env` file, especially for the `POSTGRES_PASSWORD` variable. If there are any, remove them and restart Docker Compose.

8. **External Connection**: If containers cannot connect through Docker's network but an external connection is accepted, ensure your firewall allows connections to the PostgreSQL port.

If you follow these steps and still face issues, consider checking the [GitHub issue thread for similar problems and solutions](https://github.com/supabase/supabase/issues/10541)

---

## Taking a step back

That’s a great approach! Starting small and focusing on learning Docker fundamentals like **volumes** and **persistent storage** is an excellent idea. To meet your goals without introducing a database yet, you can use simpler containerized applications that don’t require complex setups but still let you explore key Docker concepts.

Here are some suggestions for containerized software you can use to achieve your objectives:

---

### Option 1: Code Server (VS Code in the Browser)

A lightweight and interactive app that lets you create and edit files directly in the browser.

#### Why it's great:
- No database required.
- Allows you to work with files directly in a volume.
- Changes persist after container restarts.

#### How to Set It Up:
```bash
docker run -d \
  --name=code-server \
  -e PASSWORD="yourpassword" \
  -p 8080:8080 \
  -v /path/to/your/data:/home/coder/project \
  --restart unless-stopped \
  codercom/code-server:latest
```

#### Objectives:
- Persistent storage: Files created in `/path/to/your/data` will persist after container restarts.
- Explore and edit files in a browser-based VS Code editor.
- A simple and engaging way to test volumes.

---

### **Option 2: Nginx + Custom HTML Files**  
Run an Nginx web server to serve custom files you save in a volume.

#### Why it's great:
- Simple to understand and configure.
- No app interface to worry about—just edit the files in the volume and see changes instantly in your browser.
- Great for understanding how Docker serves content from volumes.

#### How to Set It Up:
1. Create a folder for your HTML files, e.g., `/path/to/website`.
2. Run the Nginx container:
   ```bash
   docker run -d \
     --name=nginx-server \
     -p 8080:80 \
     -v /path/to/website:/usr/share/nginx/html \
     --restart unless-stopped \
     nginx:latest
   ```
3. Edit or add files to `/path/to/website` and refresh your browser at `http://localhost:8080`.

#### Objectives:
- Learn how to bind a volume to a container.
- See how changes to the volume reflect instantly in the container.

---

### **Option 3: Joplin Server (Markdown Notes)**  
Joplin is a self-hosted markdown note-taking app, like HedgeDoc but simpler. The official image allows running the app without an external database.

#### Why it's great:
- Focuses on creating and editing documents.
- Persistent storage via volumes.
- Documents persist after restarts.

#### How to Set It Up:
```bash
docker run -d \
  --name=joplin-server \
  -p 22300:22300 \
  -v /path/to/joplin:/var/lib/joplin \
  --restart unless-stopped \
  florider89/joplin-server:latest
```

#### Objectives:
- Create and edit markdown notes.
- Notes are saved in `/path/to/joplin`.
- Restart the container and confirm notes persist.

---

### **Option 4: Static Markdown Viewer**
If you're just learning Docker and want something simple, try a markdown viewer like `dillinger`:

#### Why it's great:
- No database required.
- Lets you upload markdown files and see them rendered.

#### How to Set It Up:
```bash
docker run -d \
  --name=dillinger \
  -p 8080:8080 \
  --restart unless-stopped \
  joemccann/dillinger
```

#### Objectives:
- Learn to manage a containerized app with persistent settings.
- Use the Dillinger web app to create and edit markdown files.

---

### **Key Docker Commands to Practice**
- **Inspect running containers**:

  ```bash
  docker ps
  ```

- **Inspect volumes**:

  ```bash
  docker volume ls
  docker volume inspect <volume-name>
  ```

- **Stop and restart containers**:

  ```bash
  docker stop <container-name>
  docker start <container-name>
  ```

- **Remove containers**:

  ```bash
  docker rm <container-name>
  ```

- **Remove images**:

  ```bash
  docker rmi <image-name>
  ```

---

### Recommended Next Steps:
- Start with **Nginx** or **Code Server** for simple volume testing.
- Experiment with creating and editing files.
- Restart the container and confirm your content persists.
- Once you're comfortable, transition to Docker Compose to manage multi-container setups like databases or more complex apps.

Let me know which one catches your interest, and I’ll guide you through it step by step! 🚀