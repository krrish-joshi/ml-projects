# 👤 @krrish-joshi  

# 📄 Chat with PDFs – Powered by LangChain & Google Generative AI  

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)  
[![LangChain](https://img.shields.io/badge/LangChain-AI%20Framework-green)](https://www.langchain.com/)  
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20DB-orange)](https://faiss.ai/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Made by krrish-joshi](https://img.shields.io/badge/Made%20by-krrish--joshi-blueviolet)](https://github.com/krrish-joshi)  

---

## 🚀 Overview  
This project is an **AI-powered PDF chatbot** that allows you to:  
- Upload one or multiple PDF documents 📚  
- Extract and chunk text for efficient processing ⚡  
- Convert text into embeddings using **Google Generative AI** 🤖  
- Store embeddings in a **FAISS vector database** 🗂️  
- Ask natural language questions about your documents 💬  
- Get context-aware answers instantly! 🎯  

All of this runs on a clean **Streamlit web interface**.  

---

## 🛠️ Tech Stack  
- **Python** 🐍  
- **Streamlit** – Web UI  
- **LangChain** – Text splitting, embeddings, and QA pipeline  
- **FAISS** – Vector database for similarity search  
- **Google Generative AI (Gemini API)** – Embeddings + Chat model  
- **PyPDF2** – Extract text from PDFs  
- **dotenv** – API key management  

---

## 📂 Project Structure  
├── pdf_bot.py # Main Streamlit app

├── requirement.txt # Dependencies

├── .env # Store your GOOGLE_API_KEY

└── faiss_index/ # Local FAISS vector store

---

## ⚙️ Installation  

1. **Clone the repository**  
```bash
git clone https://github.com/krrish-joshi/pdf-bot.git
cd pdf-bot
Create virtual environment & install dependencies


pip install -r requirement.txt
Setup API key
Create a .env file in the project root:


GOOGLE_API_KEY=your_google_api_key_here
▶️ Run the App


streamlit run pdf_bot.py
Now open http://localhost:8501 in your browser. 🌐

💡 Features in Action
✅ Upload multiple PDFs at once
✅ Process & chunk documents for efficient search
✅ Store embeddings locally in FAISS
✅ Ask contextual questions and get detailed answers
✅ Powered by Gemini 1.5 Flash


📌 Example Use Cases
Upload your research papers and ask questions

Summarize long PDFs into short answers

Use it as a study assistant for notes & books

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📜 License
This project is licensed under the MIT License.

✨ Made with ❤️ by @krrish-joshi
