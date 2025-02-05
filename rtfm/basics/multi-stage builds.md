# "Multi-stage builds" in Docker

Multi-stage builds are a powerful feature in Docker that allow you to use multiple `FROM` statements in your Dockerfile, each representing a different stage of the build process.

In a multi-stage build, you typically start with a base image that contains all the tools and dependencies needed to build your application. This stage might include compilers, build tools, and other dependencies that are only necessary during the build process. Once the application is built, you can create a new stage that starts from a minimal base image, such as `alpine` or `scratch`, and copy only the necessary artifacts (e.g., the compiled binary or application files) from the previous stage.

By doing this, you can significantly reduce the size of the final Docker image, as it will not include the build tools and dependencies that were only needed during the build process. This results in faster deployment times and reduced attack surface, as the final image contains fewer components.

Here is an example of a multi-stage Dockerfile:

```dockerfile
# Stage 1: Build the application
FROM golang:1.17 AS builder
WORKDIR /app
COPY . .
RUN go build -o myapp

# Stage 2: Create the final image
FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/myapp .
CMD ["./myapp"]
```

In this example, the first stage (`builder`) uses the `golang` image to compile a Go application. The second stage starts from a minimal `alpine` image and copies the compiled binary from the `builder` stage. The final image is much smaller and only contains the necessary runtime dependencies.

---

> There are benefits to using multi-stage builds, even with the same base image. Let’s break it down:

## **Benefits of Multi-Stage Builds with the Same Base Image**

1. **Smaller Final Image**:
   - The final image excludes build-time dependencies (e.g., `build-essential`), which are not needed at runtime.
   - Even though `build-essential` is small, removing it still reduces the final image size slightly.

2. **Cleaner Runtime Environment**:
   - The runtime stage only includes what’s necessary to run the application, making it easier to manage and debug.

3. **Consistency**:
   - Multi-stage builds enforce a clear separation between build and runtime environments, which can help avoid accidental inclusion of unnecessary files or tools.

4. **Future-Proofing**:
   - If you later decide to use a different base image for the runtime stage (e.g., an even smaller image like `alpine`), the multi-stage setup makes it easy to switch.

---

## **When Multi-Stage Builds Shine**

Multi-stage builds are most beneficial when:

1. **Build-Time Dependencies Are Large**:
   - For example, if you need compilers, development headers, or large libraries during the build phase, multi-stage builds can significantly reduce the final image size.

2. **Different Base Images Are Used**:
   - If you use a heavier base image for building (e.g., `python:3.9` with full development tools) and a lighter one for runtime (e.g., `python:3.9-slim` or `alpine`), the optimization gains are substantial.

3. **Artifacts Are Copied Selectively**:
   - For compiled languages (e.g., Go, Rust), you can copy only the compiled binary to the runtime stage, leaving behind all the build tools and source code.

---

## **Optimizing Further**

If you want to maximize optimization, consider the following:

### **1. Use a Smaller Runtime Base Image**

Switch to an even smaller base image for the runtime stage, such as `alpine`:

```Dockerfile
# Stage 1: Build stage
FROM python:3.9-slim as builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --user --no-warn-script-location -r requirements.txt

# Stage 2: Runtime stage
FROM python:3.9-alpine  # Smaller base image

WORKDIR /app

# Copy only the installed Python packages from the builder stage
COPY --from=builder /root/.local /root/.local

# Ensure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

# Copy the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]
```

### **2. Use `pip install --no-cache-dir`**

Avoid caching pip packages to reduce image size:

```Dockerfile
RUN pip install --user --no-warn-script-location --no-cache-dir -r requirements.txt
```

### **3. Minimize Layers**

Combine commands to reduce the number of layers in the final image:

```Dockerfile
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && pip install --user --no-warn-script-location --no-cache-dir -r requirements.txt \
    && apt-get remove -y build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*
```

---

## **Example with Significant Optimization**

Here’s an example where multi-stage builds make a big difference:

### **Stage 1: Build Stage**

```Dockerfile
FROM python:3.9 as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user --no-warn-script-location --no-cache-dir -r requirements.txt
```

### **Stage 2: Runtime Stage**

```Dockerfile
FROM python:3.9-alpine

WORKDIR /app

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
```

---

## **Summary**

- If you’re using the **same base image**, the optimization gains from multi-stage builds are modest but still valuable for cleanliness and future-proofing.
- For **significant optimization**, consider using a smaller runtime base image (e.g., `alpine`) and minimizing layers.
- Multi-stage builds are most impactful when build-time dependencies are large or when you use different base images for build and runtime.
