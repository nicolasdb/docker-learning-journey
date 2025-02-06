# Dockerizing Streamlit Apps

This document provides a comprehensive guide to containerizing Streamlit applications using Docker and Docker Compose, covering both CSV file and Supabase table data sources.

## Folder Structure

```plaintext
my_streamlit_app/
├── app/             # Streamlit application code
│   ├── your_streamlit_app.py  # Your Streamlit app
│   └── requirements.txt         # Python dependencies
├── data/            # Optional: CSV data files
│   └── questions_customer_a.csv
│   └── questions_customer_b.csv
├── compose.yml         # Docker Compose configuration
└── .env                 # Environment variables (secrets)
```

## 1. Streamlit App (`app/your_streamlit_app.py`)

```python
import streamlit as st
import os
import pandas as pd
import supabase

# Access environment variables
customer_id = os.environ.get("CUSTOMER_ID")
questions_table = os.environ.get("QUESTIONS_TABLE")
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
data_source = os.environ.get("DATA_SOURCE")
csv_file_path = os.environ.get("CSV_FILE_PATH")

# Error handling for missing environment variables
if not all([customer_id, questions_table, supabase_url, supabase_key, data_source]):
    st.error("Missing required environment variables. Check your .env file and compose.yml.")
    st.stop()

# Initialize Supabase client
supabase = supabase.create_client(supabase_url, supabase_key)

# Data Loading Logic (Choose one method)

if data_source == "supabase":
    try:
        questions = supabase.table(questions_table).select("*").execute().data
        df_questions = pd.DataFrame(questions)
    except Exception as e:
        st.error(f"Error fetching data from Supabase: {e}")
        st.stop()

elif data_source == "csv":
    try:
        df_questions = pd.read_csv(csv_file_path)
    except FileNotFoundError:
        st.error(f"CSV file not found: {csv_file_path}")
        st.stop()
    except Exception as e:
        st.error(f"Error reading CSV file: {e}")
        st.stop()

else:
    st.error("Invalid data source specified. Must be 'supabase' or 'csv'.")
    st.stop()

# ... (Rest of your Streamlit application logic using df_questions) ...
st.write(f"Customer ID: {customer_id}")
st.write(df_questions)

# Example of dynamic Supabase results table
results_table = f"results_{customer_id}"
# ... your Supabase interaction code using results_table ...

```

## 2. Requirements (`app/requirements.txt`)

```plaintext
streamlit
supabase
pandas  # Or any other dependencies
```

## 3. Docker Compose (`compose.yml`)

```yaml
version: "3.9"

services:
  streamlit_app:
    build: ./app  # Build from the app directory
    ports:
      - "8501:8501"
    env_file: .env
    environment:
      - CUSTOMER_ID=${CUSTOMER_ID}
      - QUESTIONS_TABLE=${QUESTIONS_TABLE}
      - SUPABASE_URL=${SUPABASE_URL}
      - SUPABASE_KEY=${SUPABASE_KEY}
      - DATA_SOURCE=${DATA_SOURCE}
      - CSV_FILE_PATH=${CSV_FILE_PATH} # Only if DATA_SOURCE is csv
    volumes:
      - ./data:/app/data # Mount data directory for CSV files
    restart: always
```

## 4. Environment Variables (`.env`)

```yaml
CUSTOMER_ID=customer_a  # Or customer_b, etc.
QUESTIONS_TABLE=questions_customer_a # Or questions_customer_b, etc.
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
DATA_SOURCE=supabase # Or csv
CSV_FILE_PATH=/app/data/questions_customer_a.csv # Only if DATA_SOURCE is csv
```

## Build and Run

1. Place all files in the correct directory structure.
2. Fill in the `.env` file with your actual values.
3. Navigate to the directory containing `compose.yml` in your terminal.
4. Run: `docker compose up -d`

## Key Considerations

* **Data Source:** Choose either `supabase` or `csv` for `DATA_SOURCE` in your `.env` file.  Ensure the corresponding data (Supabase tables or CSV files) exists.
* **Customer-Specific Configuration:** Change the environment variables in the `.env` file (e.g., `CUSTOMER_ID`, `QUESTIONS_TABLE`, `CSV_FILE_PATH`) to deploy for different customers.
* **Security:**  **Never** commit your `.env` file containing secrets to version control.
* **Error Handling:** The provided Python code includes basic error handling for missing environment variables and file operations.  Enhance this as needed for your application.
* **Supabase Setup:** If using Supabase, ensure you have created the necessary tables (e.g., `questions_customer_a`, `results_customer_a`) in your Supabase project.
* **CSV Setup:** If using CSV, place the CSV files in the `data` directory.  The file path in `.env` must match.

This reference guide should provide a solid foundation for containerizing your Streamlit applications with different data source options.  Remember to adapt the code and configuration to your specific requirements.
