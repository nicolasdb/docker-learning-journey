# 🐇 Follow the white rabbit 
Welcome, brave adventurer! 
You're about to embark on a journey into the world of containers. Each level will teach you new skills and bring you closer to Docker container mastery.

## Your Quest Log 📜
This quest will lead you to build an automated system for processing and analyzing audio recordings using containerized services.

### 🎯 Level 1: Container basics
**Status: Ready to Start**
- Learn to handle single containers
- Master basic Docker commands
- Run and manage services
- Mini-boss: Get Ollama running with Llama2

Key Skills:
- [ ] Docker installation and setup
- [ ] Basic container operations
- [ ] Port mapping and networking basics
- [ ] Running AI models in containers

[Begin Your Journey](levels/level1-basics.md)

### 🎯 Level 2: Multi-container magic
**Status: Locked 🔒**
- Set up n8n workflow engine
- Connect containers together
- Create basic automation flows
- Mini-boss: Connect n8n to Ollama

Prerequisites:
- Complete Level 1
- Working Ollama installation

### 🎯 Level 3: Service integration
**Status: Locked 🔒**
- Add external services (Supabase)
- Set up audio transcription
- Handle sensitive data
- Mini-boss: Complete file processing pipeline

Prerequisites:
- Complete Level 2
- Working n8n + Ollama setup

### 🎯 Level 4: BOSS LEVEL
**Status: Locked 🔒**
Final Challenge: Build complete meeting assistant
- Automated transcription pipeline
- Multi-step AI processing
- Template-based output generation
- Web interface integration

Prerequisites:
- Complete Level 3
- Working pipeline setup

---

### 🎯 Level 2: Multi-container Magic

**Overview:**
In this level, you will learn how to manage and orchestrate multiple containers using Docker Compose. You will set up a workflow engine (n8n) and connect it with other services to create basic automation flows. This level will also introduce you to more advanced container networking and environment management.

**Key Skills:**
- Docker Compose basics
- Multi-container orchestration
- Container networking
- Environment variables and secrets management
- Basic automation with n8n

**Topics Covered:**

1. **Docker Compose Basics:**
   - Introduction to Docker Compose
   - Writing a `docker-compose.yml` file
   - Starting and stopping multi-container applications

2. **Multi-container Orchestration:**
   - Defining services in Docker Compose
   - Managing dependencies between containers
   - Scaling services

3. **Container Networking:**
   - Creating and managing Docker networks
   - Connecting containers using Docker Compose
   - Exposing and mapping ports

4. **Environment Variables and Secrets Management:**
   - Using environment variables in Docker Compose
   - Managing secrets securely

5. **Basic Automation with n8n:**
   - Setting up n8n workflow engine
   - Creating basic automation flows
   - Connecting n8n to other containers

**Mini-Boss Challenge:**
- Connect n8n to Ollama and create a basic automation flow.

**Prerequisites:**
- Complete Level 1
- Working Ollama installation

### 🎯 Level 3: Service Integration

**Overview:**
In this level, you will integrate n8n and Python containers with external APIs and services like Supabase for database management and user login. You will also handle local data using bind mounts and integrate with local applications like Obsidian.

**Key Skills:**
- API integration
- Database management with Supabase
- User authentication
- Local data handling with bind mounts
- Integration with local applications

**Topics Covered:**

1. **API Integration:**
   - Connecting to external APIs from containers
   - Handling API authentication and requests

2. **Database Management with Supabase:**
   - Setting up Supabase
   - Managing databases and user authentication
   - Connecting containers to Supabase

3. **Local Data Handling with Bind Mounts:**
   - Using bind mounts for local data persistence
   - Synchronizing data between containers and local applications

4. **Integration with Local Applications:**
   - Connecting containers to local applications like Obsidian
   - Automating workflows between containers and local apps

**Mini-Boss Challenge:**
- Complete a file processing pipeline using n8n and Python containers, integrated with Supabase and local data.

**Prerequisites:**
- Complete Level 2
- Working n8n + Ollama setup

### 🎯 Level 4: BOSS LEVEL

**Overview:**
In this final level, you will build a complete meeting assistant application. This will involve creating an automated transcription pipeline, multi-step AI processing, template-based output generation, and publishing the application as a web app on platforms like Hugging Face Spaces or Streamlit.

**Key Skills:**
- Automated transcription
- Multi-step AI processing
- Template-based output generation
- Web app deployment

**Topics Covered:**

1. **Automated Transcription Pipeline:**
   - Setting up transcription services
   - Automating transcription workflows

2. **Multi-step AI Processing:**
   - Creating complex AI processing pipelines
   - Integrating multiple AI models

3. **Template-based Output Generation:**
   - Generating outputs based on templates
   - Customizing output formats

4. **Web App Deployment:**
   - Deploying applications on Hugging Face Spaces or Streamlit
   - Managing web app hosting and scaling

**Final Challenge:**
- Build a complete meeting assistant with automated transcription, multi-step AI processing, and a web interface.

**Prerequisites:**
- Complete Level 3
- Working pipeline setup


---


## Progress Tracking 📊
Mark your progress by editing this file in your `myQuest` branch:
```bash
git checkout -b myQuest
```
> to create or switch to, a new branch

Then commit your victories
```bash
git add .
git commit -m "Level X Progress: Completed Y challenge"
```

## Need Help? 
- Check the `patterns/` directory for reference implementations
- Each level includes detailed explanations and examples
- Remember: The journey is as important as the destination! 🌟

Ready to begin? Head to [Level 1](levels/level1-basics.md) and start your adventure!


