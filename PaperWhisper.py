import streamlit as st
import arxiv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from constants import groq_key
import matplotlib.pyplot as plt
import io
import base64
import re

# === Setup ===
st.set_page_config(page_title="PaperWhisper.ai", layout="centered")
st.title("🧠 PaperWhisper.ai — GenAI Research Assistant")

# === Chat Memory ===
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# === Sidebar Settings ===
mode = st.sidebar.radio("Choose Interaction Mode", ["📰 Article", "🧑‍🏫 Round Table Conference", "🧠 DeepResearch"])
query = st.sidebar.text_input("Enter your research topic", placeholder="e.g., Multimodal RAG in GenAI", value="Agentic AI")
max_papers = st.sidebar.slider("How many papers?", 3, 20, 5)

# === LLM ===
llm = ChatGroq(api_key=groq_key, model_name="llama3-8b-8192")

# === Fetch Papers ===
@st.cache_data(show_spinner=True)
def fetch_papers(query, max_papers):
    search = arxiv.Search(query=query, max_results=max_papers, sort_by=arxiv.SortCriterion.Relevance)
    return [{
        "title": result.title.strip(),
        "summary": result.summary.strip(),
        "link": result.entry_id
    } for result in search.results()]

# === Plot Helper ===
def render_plot():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 9, 2])
    ax.set_title("Example Trend")
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    b64 = base64.b64encode(buf.read()).decode()
    return f'<img src="data:image/png;base64,{b64}" width="500"/>'

# === Main Execution ===
if query:
    with st.spinner("🔍 Fetching latest papers..."):
        papers = fetch_papers(query, max_papers)
        titles = "\n".join([f"- {p['title']}" for p in papers])
        summaries = "\n\n".join([f"{i+1}. {p['title']}\n{p['summary']}" for i, p in enumerate(papers)])

    st.markdown("### 🌸 Top Papers")
    for p in papers:
        st.markdown(f"**[{p['title']}]({p['link']})**")
        st.caption(p['summary'][:300] + "...")

    st.divider()

    # === Mode 1: Article ===
    if mode == "📰 Article":
        st.markdown("## 📄 Article Summary")
        prompt = PromptTemplate.from_template("""
        Write an informative, engaging article on the topic "{query}".
        Use the following research paper titles for guidance:
        {paper_titles}

        Structure it like a blog post and summarize the key research insights in plain English.
        """)
        chain = LLMChain(llm=llm, prompt=prompt)
        article = chain.run(query=query, paper_titles=titles)
        st.write(article)

        st.markdown("## ❓ Ask a Follow-Up Question")
        article_qa = st.text_input("Ask something based on the article or research...")
        if article_qa:
            qa_prompt = PromptTemplate.from_template("""
            Based on the article and these papers:
            {summaries}

            Answer the question: {question}
            """)
            chain = LLMChain(llm=llm, prompt=qa_prompt)
            answer = chain.run(question=article_qa, summaries=summaries)
            st.markdown("### 💬 Answer")
            st.write(answer)

    # === Mode 2: Round Table ===
    elif mode == "🧑‍🏫 Round Table Conference":
        st.markdown("## 🗣️ Round Table Discussion")
        roles = ["Researcher", "Engineer", "Investor", "Historian"]
        for role in roles:
            prompt = PromptTemplate.from_template("""
            You're a {role} discussing the topic "{query}" based on these research papers:
            {paper_titles}

            Share your insights and concerns in 5-6 sentences.
            """)
            chain = LLMChain(llm=llm, prompt=prompt)
            msg = chain.run(role=role, query=query, paper_titles=titles)
            with st.chat_message(role):
                st.markdown(f"**{role} says:** {msg}")

        user_comment = st.text_input("🧠 Add your thoughts to the discussion (as Open Book Boss)")
        if user_comment:
            with st.chat_message("Open Book Boss"):
                st.markdown(user_comment)

    # === Mode 3: DeepResearch Chat ===
    elif mode == "🧠 DeepResearch":
        st.markdown("## 🤖 Ask Questions Based on These Papers")
        user_input = st.chat_input("Ask a deep research question (e.g. plot trend of...)\n")

        if user_input:
            st.session_state.chat_history.append({"user": user_input})

            plot_request = re.search(r"plot|graph|trend", user_input, re.IGNORECASE)
            prompt = PromptTemplate.from_template("""
            You are a highly skilled research assistant.
            Answer the following question using ONLY the information from these papers:

            {summaries}

            Question: {question}

            Give a structured, evidence-based answer. Mention paper titles where appropriate.
            """)
            chain = LLMChain(llm=llm, prompt=prompt)
            answer = chain.run(summaries=summaries, question=user_input)
            st.session_state.chat_history.append({"assistant": answer})

            if plot_request:
                st.markdown("### 📊 Generated Plot")
                st.markdown(render_plot(), unsafe_allow_html=True)

        # Display chat history
        for chat in st.session_state.chat_history:
            if "user" in chat:
                with st.chat_message("User"):
                    st.markdown(chat["user"])
            elif "assistant" in chat:
                with st.chat_message("Assistant"):
                    st.markdown(chat["assistant"])

        st.markdown("---")
        st.markdown(f"✅ Fetched and processed {len(papers)} papers.")

