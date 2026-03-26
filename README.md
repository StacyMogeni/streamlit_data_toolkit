# 📊 Streamlit Data Science Toolkit

An interactive web application built with **Streamlit**, created as part of my learning journey using AI tools. This project demonstrates how to leverage Python and AI-assisted guidance to build data-driven dashboards, explore CSV datasets, and generate actionable insights without requiring front-end development skills.

---

## 🎯 Project Objective
The goal of this toolkit is to provide a seamless interface for data exploration:
* **User-Driven:** Allows users to upload any CSV dataset.
* **Automated Insights:** Instantly generates summary statistics and dataset shapes.
* **Interactive Visualizations:** Enables dynamic bar charts based on user-selected columns.

---

## 🚀 Quick Start

### 1. System Requirements
* **OS:** Windows / Mac / Linux
* **Language:** Python 3.7+
* **Editor:** VS Code (Recommended)

### 2. Installation
Install the necessary dependencies using pip:

```bash
pip install -r requirements.txt
``` 

### 3. Run the Application

Navigate to your project folder and execute:

```bash
streamlit run app.py

```

---

## 🛠️ Key Features

The application is structured into a multi-page experience to separate learning from utility:

* **Home Page:** An introductory welcome screen explaining the project's purpose.

* **Learn Page:** A concise overview of Streamlit’s core strengths, such as rapid deployment.

* **Data App Page (Before CSV Upload):** Prompts the user to upload a CSV file.

* **Dataset Preview:** Displays the first few rows of the uploaded CSV file.

* **Summary Statistics & Shape:** Shows dataset shape and basic statistics.

* **Visualization:** Dynamic bar chart for a user-selected column (e.g., “Industry”).

---

## 🧠 Technical Overview: Client-Server Architecture

Understanding how this app runs is crucial for deployment:

* **The Server (Backend):** The Python script runs on the host machine, performing all data computations.
* **The Client (Frontend):** Users view the app via a web browser.
* **Data Privacy:** The app only processes files explicitly provided via the `st.file_uploader` widget; it cannot access a user's local OS files directly.

---

## 📋 Common Troubleshooting

| Issue | Explanation | Fix |
| --- | --- | --- |
| **ModuleNotFoundError** | Streamlit is not installed in the current environment. | Run `pip install streamlit`. |
| **App won't open** | Browser didn't trigger or wrong directory. | Copy the Local URL from the terminal into your browser. |
| **CSV Load Error** | Incorrect format or upload failure. | Ensure the file is a standard CSV and read using `pd.read_csv()`. |

---

## 📚 References & AI Attribution

* **Documentation:** [Streamlit](https://docs.streamlit.io), [Pandas](https://pandas.pydata.org), [Python](https://docs.python.org/3/).
* **AI Mentorship:** Concepts and troubleshooting were refined using ChatGPT, Claude, and Gemini Pro.

---

This toolkit demonstrates how beginner-friendly tools like Streamlit can be used to create interactive data applications, explore datasets, and visualize insights without requiring advanced front-end skills.