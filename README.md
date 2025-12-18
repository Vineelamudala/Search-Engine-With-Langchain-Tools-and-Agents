**🔍 Search Engine using LangChain Tools & Agents**

A Search Engine powered by LangChain tools and agents that retrieves information from a real dataset and generates context-aware, hallucination-minimized answers using a Retrieval-Augmented Generation (RAG) approach.

This project demonstrates how LLM agents dynamically invoke tools to perform search and reasoning, making it a practical example of agentic GenAI applications.

_________________________________________________________

**🚀 Features**

🔎 Tool-based search using LangChain Agents

🧠 Retrieval-Augmented Generation (RAG) for accurate responses

📚 Answers generated strictly from retrieved context

⚡ Groq-powered LLaMA LLM for fast inference

🖥️ Interactive UI built with Streamlit

_________________________________________________________

**🛠️ Tech Stack**

LangChain – Tools, Agents, and RAG pipeline

Groq LLM – LLaMA models for response generation

Vector Store – For semantic search and retrieval

Streamlit – Frontend UI

Python – Core programming language
__________________________________________________________

**🧠 Architecture Overview**

User Query
   ↓
LangChain Agent
   ↓
Tool Invocation (Search / Retriever)
   ↓
Relevant Context Retrieved
   ↓
LLM (Groq - LLaMA)
   ↓
Final Answer (Context-aware)
