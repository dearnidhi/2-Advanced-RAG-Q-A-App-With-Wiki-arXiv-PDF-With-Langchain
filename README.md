# 🧠 LangChain Knowledge Center

LangChain Knowledge Center is an interactive **AI-powered question-answering application** built using **Streamlit**, **LangChain**, and **OpenAI**. It intelligently answers user queries by combining multiple information sources such as **Wikipedia**, **ArXiv research papers**, and **LangChain documentation**.
The application uses an OpenAI tools-based agent to dynamically choose the best source for each question.

---

## 🚀 Features

- AI-powered question answering using OpenAI
- Wikipedia search integration
- ArXiv research paper lookup
- LangChain documentation retrieval using FAISS
- Vector-based semantic search
- Streamlit-based interactive UI
- Multi-tool agent execution with LangChain

---

## 🧠 How It Works

1. **Document Loading**
   - Loads LangChain documentation from the web
   - Splits content into chunks for efficient retrieval

2. **Vector Search**
   - Creates embeddings using OpenAI
   - Stores embeddings in FAISS for similarity search

3. **AI Agent**
   - Uses OpenAI tools agent
   - Automatically selects between:
     - Wikipedia search
     - ArXiv research papers
     - LangChain documentation retriever

4. **User Interaction**
   - User enters a question via Streamlit UI
   - Agent processes the query and returns the best answer

---

## 🖥️ User Interface

- Clean Streamlit layout
- Sidebar explaining LangChain
- Central input box for questions
- Instant AI-generated responses

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>


2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Environment Variables
Create a .env file in the root directory:
OPENAI_API_KEY=your_openai_api_key_here

5️⃣ Run the Application
streamlit run app.py

🛠️ Tech Stack
Python
Streamlit
LangChain
OpenAI API
FAISS
Wikipedia API
ArXiv API

⚠️ Notes
Requires a valid OpenAI API key
Designed for learning and experimentation
Not optimized for production-scale workloads
