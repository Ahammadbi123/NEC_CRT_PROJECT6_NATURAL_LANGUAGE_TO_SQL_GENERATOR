import streamlit as st
import sqlite3
import os
import pandas as pd
from groq import Groq
from dotenv import load_dotenv
import database
if not os.path.exists("retail_data.db"):
    database.create_database()

# 1. Load API Key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# 2. AI SQL Generator Function
def get_sql_from_ai(user_question):
    prompt = f"""
    You are an expert SQL assistant. Convert natural language into a valid SQLite query.
    
    Database Schema:
    - Table: Products (id, name, category, price, stock)
    - Table: Members (id, name, age, city, joins_count)

    Rules:
    - Use 'Members' table if user asks about people, members, or users.
    - Use 'Products' table if user asks about items, stock, or products.
    - Return ONLY the SQL query code. Do not provide explanations or markdown backticks.
    
    Question: {user_question}
    """
    
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# 3. Database Execution Function
def execute_query(sql_query):
    try:
        # Clean SQL code from any AI formatting
        sql_query = sql_query.replace("```sql", "").replace("```", "").strip()
        
        conn = sqlite3.connect("retail_data.db")
        df = pd.read_sql_query(sql_query, conn)
        conn.close()
        return df
    except Exception as e:
        return str(e)

# 4. Streamlit UI (Improved Structure)
st.set_page_config(page_title="AI SQL Analyzer", page_icon="📊", layout="wide")

# Custom CSS for Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button {
        width: 100%;
        background-color: #007bff;
        color: white;
        border-radius: 8px;
        height: 3em;
        font-weight: bold;
    }
    .sql-box {
        background-color: #1e1e1e;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and Header
st.title("🛒 Smart Retail AI SQL Analyzer")
st.info("Transform your natural language into executable SQL queries instantly using Groq AI.")

# User Input Section
st.subheader("Enter your query below:")
user_input = st.text_input("", placeholder="e.g. Show all members from Hyderabad", label_visibility="collapsed")

if st.button("Generate & Search"):
    if user_input:
        with st.spinner('AI is analyzing your request...'):
            generated_sql = get_sql_from_ai(user_input)
            
            if "Error" in generated_sql:
                st.error(generated_sql)
            else:
                # Structure: Two columns for SQL and Data Result
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.success("✅ Generated SQL Query")
                    st.code(generated_sql, language="sql")
                
                with col2:
                    st.success("📊 Query Results")
                    results = execute_query(generated_sql)
                    
                    if isinstance(results, pd.DataFrame):
                        if not results.empty:
                            st.dataframe(results, use_container_width=True, hide_index=True)
                            st.info(f"Total Rows Found: {len(results)}")
                        else:
                            st.warning("No data matches your criteria in the database.")
                    else:
                        st.error(f"Execution Error: {results}")
    else:
        st.warning("Please type a question to get started.")

# Footer
st.markdown("---")
st.caption("Powered by Groq AI (Llama 3.3) | Built with Streamlit Framework")
