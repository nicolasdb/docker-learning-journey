
## **Phase 2 - Intégration de Supabase comme backend**

🎯 **Objectif** : Gérer la persistance des données avec Supabase.  

🔹 **Key Results**

- [x] Installer et configurer Supabase avec Docker Compose.
- [x] .env Management for Access key  
- [x] Créer une base de données et un premier modèle de stockage.  
- [x] Connecter un script Python à Supabase pour lire/écrire des données.  
<!-- - [x] Tester une requête REST depuis Postman ou un script Python.  >>> same same as precedent but nerdy. -->

🛠 **Exercice pratique** :  
- Stocker des réponses de test dans la base de données Supabase.  
- Ajouter un endpoint API pour récupérer les résultats.  

---

Collecting workspace information

In Flask, the 

render_template

 function looks for HTML templates in a folder named `templates` by default. This is why you needed to move your 

index.html

 file into a `templates` directory. Flask expects the following structure for templates and static files:

- `templates/`: Contains HTML files.
- 

static/

: Contains static files like CSS, JavaScript, and images.

Given your current setup, let's review and adjust your 

compose.yml

 and 

app.py

 to ensure everything works correctly.

### Updated 

app.py



Ensure your 

index.html

 file is in the `templates` directory:

```python
from flask import Flask, request, jsonify, render_template
from supabase import create_client
import os

app = Flask(__name__)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    response = supabase.table("flasktest").insert(data).execute()
    return jsonify(response.data), 201

@app.route("/results", methods=["GET"])
def results():
    response = supabase.table("flasktest").select("*").execute()
    return jsonify(response.data), 200

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### Updated 

compose.yml



Ensure the `templates` directory is correctly bind-mounted:

```yaml
services:
  flask-app:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./templates:/app/templates
    environment:
      - SUPABASE_URL=${SUPABASE_URL}
      - SUPABASE_KEY=${SUPABASE_KEY}
```

### Folder Structure

Ensure your project directory has the following structure:

```
workbench/level2/22supabase/
├── app.py
├── Dockerfile
├── requirements.txt
├── compose.yml
└── templates/
    └── index.html
```

### Explanation

1. **

app.py

**: The 

render_template

 function looks for HTML files in the `templates` directory by default.
2. **`compose.yml`**: The `volumes` section bind-mounts the `templates` directory from your host to the `/app/templates` directory in the container.
3. **Folder Structure**: The `templates` directory contains your 

index.html

 file, ensuring Flask can find and render it.

With these adjustments, your Flask app should correctly render the 

index.html

 template, and the bind mount in 

compose.yml

 ensures any changes to the `templates` directory on your host are reflected in the container.

---

### REST with Postman

[Postman is a popular API development](https://marketplace.visualstudio.com/items?itemName=Postman.postman-for-vscode) and testing tool that allows you to create, test, and document APIs. It provides a user-friendly interface to send HTTP requests to your API endpoints and view the responses. This makes it easier to test and debug your APIs without writing code.

#### Key Features of Postman

- **Request Building**: Easily create and configure HTTP requests (GET, POST, PUT, DELETE, etc.).
- **Response Viewing**: View and analyze the responses from your API.
- **Environment Management**: Manage different environments (e.g., development, staging, production) with environment variables.
- **Collections**: Organize your API requests into collections for better management and sharing.
- **Automation**: Automate API testing with scripts and integrate with CI/CD pipelines.

#### method

1. **Submit Data**:
   - Method: POST
   - URL: `http://localhost:5000/submit`
   - Body: JSON (e.g., `{"key": "value"}`)
   - Steps:
     1. Open Postman.
     2. Select `POST` method.
     3. Enter `http://localhost:5000/submit` in the URL field.
     4. Go to the `Body` tab, select `raw` and `JSON`.
     5. Enter the JSON data, e.g., `{"key": "value"}`.
     6. Click `Send` and check the response.

2. **Get Results**:
   - Method: GET
   - URL: `http://localhost:5000/results`
   - Steps:
     1. Open Postman.
     2. Select `GET` method.
     3. Enter `http://localhost:5000/results` in the URL field.
     4. Click `Send` and check the response.

### REST with Python Script

Create a Python script to test the endpoints:

```python
# filepath: /home/nicolas/github/docker-learning-journey/workbench/level2/test_api.py

import requests

# Test the submit endpoint
submit_url = "http://localhost:5000/submit"
data = {"key": "value"}
response = requests.post(submit_url, json=data)
print("Submit Response:", response.json())

# Test the results endpoint
results_url = "http://localhost:5000/results"
response = requests.get(results_url)
print("Results Response:", response.json())