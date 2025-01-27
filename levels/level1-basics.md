# Stage 1: First Contact Protocol

## Mission 1: First Contact

```plaintext
TERMINAL INITIALIZED...
CONNECTING...
=======================

>_ Hello? Is anyone there?
>_ We detected Docker technology on your system...
>_ But something's not quite right...

STATUS CHECK:
- Docker Service: ❓
- User Permissions: ❌
- Container Access: ❌

WARNING: PERMISSION DENIED
Container operations require proper access rights.
=======================
```

### 🎯 Mission 1 Victory Conditions

- [ ] Docker service is running on your system
- [ ] Your user has proper Docker access (no sudo needed)
- [ ] You can run the hello-world container

*Need help? Check `rtfm/basics/permissions.md` for user setup.*

## Mission 2: Container Explorer

```plaintext
INCOMING TRANSMISSION...
=======================
>_ Excellent! Connection established! This is Commander Chen 
   from Container Labs. We've been monitoring systems worldwide
   for potential allies.

>_ Listen carefully: We need to test your container skills
   with a simple application first. Python will be perfect
   for this test - it's stable and widely used.

>_ Can you help us set up a test environment? We need to
   ensure you can control containers effectively before
   we proceed with more complex missions.

SCANNING DOCKER HUB...
>_ Found the Python container? Perfect! Now let's test your
   container control abilities. Remember, mastery over
   basic operations is crucial for what lies ahead.
=======================
```

### 🎯 Mission 2 Victory Conditions

- [ ] Found and pulled official Python container
- [ ] Successfully running Python container
- [ ] Can start, stop, and remove container
- [ ] Understand container lifecycle management
- [ ] Create a Dockerfile for a custom Python application
- [ ] Successfully build and run your custom container

*Need help? Check `rtfm/basics/container-ops.md` and `rtfm/basics/dockerfile-basics.md` for guidance.*

## Mission 3: Data Persistence

```plaintext
URGENT UPDATE...
=======================
>_ Commander Chen here again. Your container skills are
   improving, but there's one crucial aspect we need
   to test: data persistence.

>_ In the field, data loss is not an option. We need
   to ensure your containers can maintain their state
   even through restarts and updates.

>_ Your mission: Set up a containerized web application
   that can persist data. This will simulate real-world
   scenarios where data preservation is critical.

CRITICAL NOTE:
>_ Whatever you do, make sure the data survives container
   restarts. We can't afford to lose valuable information!
=======================
```

### 🎯 Mission 3 Victory Conditions

- [ ] Container running with persistent storage
- [ ] Data survives container restarts
- [ ] Proper volume configuration
- [ ] Can modify and persist content
- [ ] Understand different storage options

*Study `rtfm/storage/volumes.md` for persistence setup.*

## 🗡️ BOSS BATTLE: The Integration Challenge

```plaintext
EMERGENCY BROADCAST...
=======================
>_ *static*... Commander Chen here... *static*... 
   This is the moment of truth!

>_ We need you to combine everything you've learned:
   - Container management
   - Custom images
   - Data persistence
   - Resource monitoring

>_ Your final challenge: Create a complete containerized
   application environment that demonstrates mastery of
   these fundamental skills.

CRITICAL PARAMETERS:
>_ Storage must be persistent
>_ Ports must be properly mapped
>_ Resources must be monitored
>_ Container must auto-restart on failure

The success of future missions depends on mastering
these fundamentals. Are you ready?
=======================
```

### 🏆 Boss Battle Victory Conditions

- [ ] Custom application container running stably
- [ ] Persistent storage properly configured
- [ ] Port mapping working correctly
- [ ] Container auto-restart enabled
- [ ] Resource monitoring in place
- [ ] Setup survives system restart

*Master `rtfm/monitoring/resources.md` before attempting this challenge.*

```plaintext
LEVEL STATUS: IN PROGRESS
>_ Your journey into container mastery has begun.
>_ Each challenge builds your expertise.
>_ Level 2 will reveal more advanced concepts...
=======================
