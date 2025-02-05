# Key Concepts of Docker Compose

**Docker Compose** is a tool used to define and manage multi-container Docker applications. It simplifies running multiple services by using a single configuration file (`docker-compose.yml`).  

---

## **Key Concepts**  

1. **Services**  
   - Each container (e.g., a database, web server, or backend API) is defined as a service in `docker-compose.yml`.  

2. **Networks**  
   - Services can communicate via internal networks without exposing ports to the host.  

3. **Volumes**  
   - Persistent storage can be shared across services.  

4. **Build and Images**  
   - You can either specify an image (`image: postgres:latest`) or build from a `Dockerfile` (`build: .`).  

5. **Environment Variables**  
   - Used to pass configuration values dynamically.  

6. **Scaling**  
   - `docker-compose up --scale service_name=N` allows running multiple instances of a service.  

---

## **Common Commands**  

| Command | Description |
|---------|-------------|
| `docker-compose up` | Starts all services in the `docker-compose.yml` file. |
| `docker-compose up -d` | Starts services in the background (detached mode). |
| `docker-compose down` | Stops and removes all services, networks, and volumes. |
| `docker-compose ps` | Lists running services. |
| `docker-compose logs -f service_name` | Shows real-time logs of a service. |
| `docker-compose exec service_name bash` | Opens an interactive shell inside a running container. |
| `docker-compose restart service_name` | Restarts a specific service. |
| `docker-compose build` | Builds the images defined in the file. |
| `docker-compose pull` | Pulls the latest images from a registry. |
| `docker-compose up --scale service_name=N` | Runs multiple instances of a service. |

---

## **Structure of `docker-compose.yml`**  

```yaml
version: "3.8"

services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
    networks:
      - mynetwork

  db:
    image: postgres:latest
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - mynetwork

volumes:
  db-data:

networks:
  mynetwork:
```

**Explanation:**
- Defines two services: `web` (Nginx) and `db` (PostgreSQL).
- Uses a shared network (`mynetwork`) for internal communication.
- Mounts a volume (`db-data`) for database persistence.
- Maps `localhost:8080` to Nginx’s internal port `80`.

Let me know if you need help configuring a specific setup! 🚀