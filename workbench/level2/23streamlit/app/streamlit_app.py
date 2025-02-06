import streamlit as st
from supabase import create_client
import os

# Initialize Supabase client
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# Set page title
st.title("Person Data Entry")

# Create input form
with st.form("data_form"):
    # Name input field
    name_input = st.text_input("Enter name:")
    
    # Age input field
    age_input = st.number_input("Enter age:", min_value=0, max_value=150, step=1)
    
    # Submit button
    submit_button = st.form_submit_button("Submit")
    
    if submit_button and name_input:
        # Insert data into Supabase
        try:
            data = {
                "name": name_input,
                "age": int(age_input)
            }
            response = supabase.table("flasktest").insert(data).execute()
            st.success("Data submitted successfully!")
        except Exception as e:
            st.error(f"Error submitting data: {str(e)}")

# Display all entries
st.subheader("All Entries")
try:
    # Fetch only name and age columns from Supabase
    response = supabase.table("flasktest").select("name, age").execute()
    
    # Display the data in a table
    if response.data:
        # Convert data to remove decimal places from age
        formatted_data = [
            {"name": entry["name"], "age": int(entry["age"]) if entry["age"] is not None else 0} 
            for entry in response.data
        ]
        st.table(formatted_data)
    else:
        st.info("No entries found in the database.")
except Exception as e:
    st.error(f"Error fetching data: {str(e)}")

# Add auto-refresh button
if st.button("Refresh Data"):
    st.rerun()
