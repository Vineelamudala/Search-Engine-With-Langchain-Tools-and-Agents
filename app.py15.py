import streamlit as st
from langchain_community.tools import ArxivQueryRun,DuckDuckGoSearchRun,WikipediaQueryRun
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_classic.agents import AgentExecutor,initialize_agent,AgentType
from langchain_classic.callbacks import StreamlitCallbackHandler
from langchain_groq import ChatGroq
import os


Arxiv_wrapper=ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=200)
Arxiv=ArxivQueryRun(api_wrapper=Arxiv_wrapper)

Wiki_wrapper=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=250)
Wiki=WikipediaQueryRun(api_wrapper=Wiki_wrapper)

search=DuckDuckGoSearchRun(name="search")

st.title("Langchain with tools and Agents")

st.sidebar.title("Settings")
groq_api_key=st.sidebar.text_input("Enter your groq api key",type="password")

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"Assistant","Content":"Hi,I'm a chatbot who can search the web. How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["Content"])
    
if prompt:=st.chat_input(placeholder="What is Machine Learning"):
    st.session_state.messages.append({"role":"user","Content":prompt})
    st.chat_message("user").write(prompt)

    llm=ChatGroq(api_key=groq_api_key,model="llama-3.3-70b-versatile",streaming=True)

    tools=[Arxiv,Wiki,search]

    search_agent=initialize_agent(llm=llm,tools=tools,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,handle_parsing_erros=True)

    with st.chat_message("assistant"):
        st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response=search_agent.run(prompt,callbacks=[st_cb])
        st.session_state.messages.append({"role":"Assistant","Content":response})
        st.write(response)



