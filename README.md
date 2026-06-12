# 🛒 Smart Retail AI SQL Analyzer

An advanced **Natural Language to SQL (NL-to-SQL)** generator built using **Python**, **Streamlit**, and the **Groq AI (Llama 3.3)** model. This application allows users to interact with a database using plain English, automatically converting their questions into executable SQL queries and displaying the results in a professional dashboard.


##  LIVE LINK :
https://nec-crt-project6-natural-language-to-sql.onrender.com

---

## 🚀 Features
- **Natural Language Processing:** Converts complex English questions into valid SQLite queries.
- **Lightning Fast AI:** Powered by **Groq Cloud** (Llama 3.3 70B model) for near-instant responses.
- **Dynamic Data Analysis:** Seamlessly queries multiple tables like `Products` and `Members`.
- **Interactive UI:** A clean, professional dashboard built with **Streamlit**.
- **Live Preview:** Displays both the generated SQL code and the data results side-by-side.

---

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **AI Engine:** Groq API (Llama 3.3 70B Versatile)
- **Database:** SQLite3
- **Language:** Python 3.x
- **Data Handling:** Pandas

---

## 📁 Project Structure
```text
NEC_CRT_PROJECT6_NATURAL_LANGUAGE_TO_SQL_GENERATOR/
├── app.py              # Main Streamlit application
├── database.py         # Script to initialize the SQLite database and sample data
├── .env                # API Key storage (Hidden/Ignored by Git)
├── .gitignore          # Files to ignore (e.g., .env, .db)
├── requirements.txt    # List of required Python packages
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Ahammadbi123/NEC_CRT_PROJECT6_NATURAL_LANGUAGE_TO_SQL_GENERATOR.git
cd NEC_CRT_PROJECT6_NATURAL_LANGUAGE_TO_SQL_GENERATOR
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Groq API Key
Create a `.env` file in the root directory and add your Groq API Key:
```text
GROQ_API_KEY=your_actual_api_key_here
```

### 4. Initialize the Database
Run this script once to create the `retail_data.db` file with sample tables and data:
```bash
python database.py
```

### 5. Run the Application
```bash
streamlit run app.py
```

---

## 🖥️ How to Use
1. Open the application in your browser (usually at `http://localhost:8501`).
2. Type a natural language question in the input box.
   - *Example:* "Show all members from Hyderabad"
   - *Example:* "List products with price greater than 1000"
3. Click **"Generate & Search"**.
4. View the **Generated SQL** and the **Query Results** instantly.

---

## ☁️ Deployment
This project is ready to be deployed on **Streamlit Cloud**:
1. Push your code to GitHub (ensure `.env` is ignored).
2. Connect your repo to Streamlit Cloud.
3. Add your `GROQ_API_KEY` in the **Advanced Settings -> Secrets** section of the Streamlit dashboard.

---

## 👤**Developed By** : SHAIK AHMMAD BI

---
