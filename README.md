# 🚀 Offline Customer Support Knowledge Base using LangChain & FAISS

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.45-FF4B4B?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Semantic_Search-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Database-orange)
![Sentence Transformers](https://img.shields.io/badge/SentenceTransformers-MiniLM-purple)
![Offline](https://img.shields.io/badge/Mode-Offline-success)

An offline customer support knowledge base built using **LangChain**, **Sentence Transformers**, **FAISS**, and **Streamlit**.

The application indexes customer support documents (**FAQs, Troubleshooting Guides, and Support Tickets**) into a local vector database, allowing users to perform **fast semantic search** without requiring an internet connection or external APIs.

> ✅ 100% Offline • No API Key Required • Fast Semantic Search

---

# 🌟 Features

- 📄 Search answers from multiple PDF documents
- 🧠 Semantic Search using Sentence Transformers
- ⚡ Fast Retrieval using FAISS Vector Database
- 💻 Interactive Streamlit User Interface
- 🔒 Works Completely Offline
- 📚 Local PDF Knowledge Base
- 🚀 Fast Document Search Pipeline

---

# 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Sentence Transformers (MiniLM)
- FAISS
- PyPDF
- NumPy
- Git
- GitHub

---

# 📁 Project Structure

```text
RAG-customer-support-knowledge-base/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── customer_FAQ.pdf
│   ├── Support_Tickets.pdf
│   └── Troubleshooting_Guide.pdf
│
├── images/
│   ├── ui.png
│   └── output.png
│
├── models/
│   └── vector_store/
│       ├── index.faiss
│       └── index.pkl
│
├── rag_pipeline.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ How It Works

```text
PDF Documents
      │
      ▼
PyPDFLoader
      │
      ▼
Text Splitter
      │
      ▼
Sentence Transformer
      │
      ▼
FAISS Vector Store
      │
      ▼
Semantic Similarity Search
      │
      ▼
Top Matching Results
      │
      ▼
Streamlit User Interface
```

---

# 🚀 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/srinivas-kandimalla/Rag-customer-support-knowledge-base.git
cd Rag-customer-support-knowledge-base
```

---

## 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Build the Vector Database

Run this command once to process all PDF files and generate the FAISS vector database.

```bash
python rag_pipeline.py
```

---

## 5️⃣ Launch the Streamlit Application

```bash
streamlit run app/streamlit_app.py
```

Open your browser:

```
http://localhost:8501
```

---

# 💡 Example Queries

Try asking questions like:

- How do I reset my password?
- How can I contact customer support?
- What should I do if the application is not opening?
- How can I resolve payment issues?
- Login failed. What are the troubleshooting steps?

---

# 📸 Screenshots

## 🖥️ Application Interface

<img src="images/ui.png" width="900">

---

## 🔍 Search Results

<img src="images/output.png" width="900">

---

# 🚀 Future Improvements

- 🤖 OpenAI / Ollama Integration
- 💬 Conversational Chat Interface
- 📄 Source Citation with Page Numbers
- 📊 Confidence Score
- 📂 Upload Custom PDF Documents
- 🐳 Docker Support
- ☁️ Cloud Deployment
- 📈 Analytics Dashboard

---

# 👨‍💻 Developer

**Srinivas Kandimalla**

🎓 B.Tech – Computer Science Engineering (AI & ML)

### GitHub

https://github.com/srinivas-kandimalla

### LinkedIn

https://www.linkedin.com/in/srinivas-kandimalla/

---

# 📄 License

This project is developed for educational and learning purposes.

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Your support helps improve future projects and motivates further development.