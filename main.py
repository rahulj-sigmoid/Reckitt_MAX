import plotly.graph_objects as go
import pandas as pd
import streamlit as st
import base64

pd.options.display.float_format = "{:.0f}".format
import helper
import time

st.set_page_config(page_title="MAX", layout="wide", initial_sidebar_state='collapsed')


st.sidebar.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{base64.b64encode(open('images/Max_logo.png', 'rb').read()).decode()}" 
        class="sidebar-image" alt="Max Logo" />
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 20% !important; # Set the width to your desired value
        }
        .st-emotion-cache-kgpedg {
            padding-bottom: 0px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
        /* Responsive image sizing */
        .sidebar-image {
            width: 150px;
            max-width: 10px;
            height: auto;
            margin: 0 auto;
            display: block;
            padding: 10px;
        }
        
        /* Viewport-based scaling */
        @media (max-width: 768px) {
            .sidebar-image {
                max-width: 100px;
            }
        }
        
        @media (max-width: 480px) {
            .sidebar-image {
                max-width: 80px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# helper.max()
pg = st.navigation([ st.Page("pages/chat.py", title="Chat with Max", icon=":material/chat:"), st.Page("pages/experts.py", title="Explore Experts", icon=":material/groups:")])
pg.run()

st.markdown("""
        <style> 
        .st-emotion-cache-1c7y2kd{ 
            padding: 10px; 
            background-color: #facfe5 !important;
           
        }
        .st-emotion-cache-4oy321 { 
            padding: 10px; 
            background-color: #ebebeb !important;
           
        }
        </style>
        """, unsafe_allow_html=True)

st.markdown(
    """
    <style>
        /* Apply color to all markdown text */
        .stMarkdown p {
            color: #E31279;
        }
        .stMarkdown h1 {
            color: #E31279;
        }
        .stMarkdown li {
            color: #E31279;
        }
        .st-emotion-cache-1rsyhoq h2 {
            color: #E31279;
        }
        .st-emotion-cache-1ny7cjd p {
            color: #E31279t;
        }
        .stRadio p {
            color: #E31279;
        }
        .st-emotion-cache-6nrhu6 {color: #E31279;}
        .stLinkButton p {color: #E31279;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
        button[kind="secondary"] {
            margin-left:-5px;
            margin-right:-5px;
            background-color: white;
        }
        button[kind="secondary"] p {
            font-size: 14px;
            color:  #E31279;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
        button[kind="primary"]{
            background-color: #E31279;
            max-width: 170px;
        }
        button[kind="primary"] p {
            color:  white;
            max-width: 170px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
        button[kind="tertiary"]{
            font-size: 20px !important;
        }
        button[kind="tertiary"] hover{
            background-color: #ffffff !important;
        }
        button[kind="tertiary"] p {
            color:  #555 !important;
            font-size: 20px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
        /* Change the chat input container */
        .stChatInput {  
            border: 2px solid #E31279; !important;
        }

        /* Target the chat input send button */
        button[data-testid="stChatInputSubmitButton"]::before {
            content: "mic"; /* Change this to any Material Icon name */
            font-family: "Material Icons";
            font-size: 20px;
            color: #33334d; /* Change icon color */
        }

        /* Hide the default SVG icon */
        button[data-testid="stChatInputSubmitButton"] svg {
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)







