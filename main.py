import plotly.graph_objects as go
import pandas as pd
import streamlit as st
import base64

pd.options.display.float_format = "{:.0f}".format
import helper
import time

st.set_page_config(page_title="MAX", layout="wide", initial_sidebar_state='collapsed')

#interface
col1, col2 = st.columns([0.5, 13])
with col1:
    st.markdown(
        """
        <style>
            [data-testid="stImage"] > img {
                max-width: 100%;
                width: auto;
                height: auto;
            }
            
            @media (max-width: 768px) {
                [data-testid="stImage"] > img {
                    max-width: 40px;
                }
            }
            
            @media (max-width: 480px) {
                [data-testid="stImage"] > img {
                    max-width: 30px;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.image("images/chat-xxl.png", width=50)
with col2:
    st.markdown(
        "<h1 style='text-align: left; padding-left: 10px;'>Data Companion</h1>", 
        unsafe_allow_html=True
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

st.sidebar.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{base64.b64encode(open('images/Reckitt_logo.png', 'rb').read()).decode()}" 
        class="sidebar-image" alt="Reckitt Logo" />
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
    </style>
    """,
    unsafe_allow_html=True,
)

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
        }
        button[kind="primary"] p {
            color:  white;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style> 
    .stChatInput{  
        border: 2px solid #E31279; !important;
    }  
    </style>
    """,
    unsafe_allow_html=True,
)

# Remove the pages dictionary and radio selection
# Instead directly call the new max() function
helper.max()

