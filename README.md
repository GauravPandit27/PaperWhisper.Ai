
# 📚 PaperWhisper.ai – Your GenAI Research Co-Pilot

**PaperWhisper.ai** is an intelligent, interactive research assistant powered by LLMs. It helps you rapidly explore, understand, and query research papers using natural language.

🚀 Built using **Streamlit**, **LangChain**, **Groq's LLaMA3**, and **Matplotlib**, it’s your go-to tool for turning dense academic content into digestible insights.

---

## 🧠 Core Features

✅ **Ask Research Questions**  
Type your query and get a direct answer based on top research papers (Arxiv/semantic input to be integrated).

✅ **Deep Research Mode**  
Get insights with support for stats, graphs, and plotting via Matplotlib.

✅ **Round Table Mode (Coming Soon)**  
Simulate a multi-agent discussion between research personas (economist, scientist, policy analyst, etc.).

✅ **News + Research Hybrid (Coming Soon)**  
Ask time-sensitive queries and get answers grounded in both research papers and recent news.

---

## 🔧 Tech Stack

- **Frontend/UI:** Streamlit
- **LLM:** Groq’s `llama3-8b-8192` (via LangChain)
- **Orchestration:** LangChain (RAG-style flow)
- **Data Viz:** Matplotlib (can extend to Plotly/Seaborn)
- **Paper Integration:** Arxiv (to be integrated via API or LangChain Tools)

---

## 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/PaperWhisper.ai.git
cd PaperWhisper.ai
````

2. **Create a virtual environment**

```bash
python -m venv Genai
source Genai/bin/activate  # For Linux/macOS
# OR
Genai\Scripts\activate     # For Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set your Groq API key**

Use Streamlit secrets to keep your key safe:

```toml
# .streamlit/secrets.toml
groq_key = "your_groq_api_key"
```

---

## ▶️ Usage

```bash
streamlit run research_agent.py
```

---

## 📊 Screenshots

> *Add here: Graphs, UI of the app, sample query screenshots*
> E.g., Answer to "What's the latest in GenAI for healthcare?" + Matplotlib plot for keyword distribution.

---

## 🛣️ Roadmap

* [ ] Arxiv API integration
* [ ] LangGraph Agent Flow
* [ ] Round Table Mode (multi-agent simulation)
* [ ] PDF paper uploads & chunked context retrieval
* [ ] Export summaries as PDFs/Markdown

---

## 🤖 Built With

* ❤️ by [Gaurav Pandit](https://linkedin.com/in/gauravpandit7)
* 🔥 Groq + LangChain + Streamlit + Python 3.10
* 🧠 Inspired by the future of research automation

---

## 📝 License

MIT License. Free to use, fork, improve. Just give credits like a scholar 😉

```

---

Want a logo, banner, or badge-based version for LinkedIn or DevPost too? Say the word, boss.
```
