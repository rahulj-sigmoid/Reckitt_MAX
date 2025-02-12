import streamlit as st
from datetime import datetime
import helper
import base64

# st.set_page_config(page_title="MAX", layout="wide", initial_sidebar_state='collapsed')
welcome_response = {
        "answer": "👋 Hello! I'm MAX (Modern Analytics Xplorer/Xpert). Feel free to ask me anything or check out the Hot Topics in the sidebar for some suggested questions!",
        "dataframe": [],
        "graphs": [],
        "link": "",
        "tab_name": ""
    }
chat_container = st.container()
def handle_save_chat():
    # Update recent chats (limiting to 5 most recent)
    if "messages" in st.session_state and st.session_state.messages:
        messages = st.session_state.messages.copy()
        new_chat = {
            "title": f"{messages[0]['content']if len(messages)%2==0 else messages[1]['content']}",
            "messages": messages,
        }
        if "saved_chats" not in st.session_state:
            st.session_state.saved_chats = []
        st.session_state.saved_chats.append(new_chat)
        if len(st.session_state.saved_chats) > 5:
            st.session_state.saved_chats.pop(0)
        # Clear current messages
        if "messages" in st.session_state:
            st.session_state.messages = []

            

with chat_container:
    header_cols = st.columns([8, 2])   
    with header_cols[0]:
        html_code = f"""
        <style>
            .container_with_border_5 {{
                background-color: white;
                padding: 10px 0; /* Add some padding for spacing */
                color: #1E3D7D;
                display: flex;
                align-items: center;
                justify-content: space-between; /* Align logo to the left and header to center */
            }}
            .header-content {{
                display: flex;
                align-items: center;
                flex-grow: 1;
                justify-content: center;
                position: relative;
            }}
            .header-content img {{
                height: 50px; /* Adjust the logo height as needed */
                margin-bottom: 15px; /* Add some margin to the left if needed */
            }}
            #dashboard_heading {{
                position: relative;
            }}
            #dashboard_heading h5 {{
                font-size: 36px; /* Increase font size */
                font-weight: 400;
                font-family: 'Source Serif 4', serif;
                color: #1A1A1A;
                margin: 0; /* Remove default margin */
                padding-bottom: 10px; /* Add some space between text and border */
            }}
            .single-line {{
                width: 100%;
                height: 2px; /* Height of the bottom border */
                background: linear-gradient(to right, #e9ebed, #e9ebed); /* Gradient from red to yellow */
                position: absolute;
                bottom: 0;
            }}
        </style>
        <div class="container_with_border_5" style="margin-bottom: 15px; margin-top: -50px">
            <div style="text-align: left;">
                 <img src="data:image/png;base64,{base64.b64encode(open('images/Max_logo.png', 'rb').read()).decode()}" 
                    style="max-width: 100px; height: auto;"/> 
                 <p style="margin: 0; font-size: clamp(17px, 1.5vw, 18px);">Modern Analytics Xplorer/Xpert</p>
            </div>
            
        </div>
        <div class="single-line"></div>
        """
    st.markdown(html_code, unsafe_allow_html=True)


if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add welcome message when session starts
   
    st.session_state.messages.append({"role": "assistant", "content": welcome_response})
    # Display welcome message immediately
    helper.display_content(welcome_response, "assistant", streaming=True, chat_container=chat_container)

if "saved_chats" not in st.session_state:
    st.session_state.saved_chats = []
if "recent_chats" not in st.session_state:
    st.session_state.recent_chats = []
if "disabled" not in st.session_state:
    st.session_state.disabled = False
if "chat_session_index" not in st.session_state:
    st.session_state.chat_session_index = 0 # for keeping track of the chat session.


def handle_clear_chat():
    print("Clear chat entered...")
    if st.session_state.messages:
        complete_messages_of_session = st.session_state.messages.copy()
        for chat in st.session_state.recent_chats:
            print("chat_session_index : " ,chat)
            if chat['chat_session_index'] == st.session_state.chat_session_index:
                chat['messages'] = complete_messages_of_session
                break
    
    # Reset the session's chat history to start fresh
    st.session_state.messages = []
    st.session_state.chat_session_index = st.session_state.chat_session_index + 1 
    print("Chat cleared. Starting new session.")

# Create a fixed container for buttons
fixed_buttons = st.container(border=None, key='fixed_buttons')

with fixed_buttons:
    col0, col1 = st.columns([3,6])
    with col0:
        st.button(
            "Clear Conversation",
            help="Click to reset the chat",
            type="primary",
            key="clear_button",
            on_click=handle_clear_chat,
            use_container_width=True,
        )  
    # with col1:
    #     st.button(
    #         ":material/save:",
    #         help="Click to save the chat",
    #         type="primary",
    #         key="save_button",
    #         on_click=handle_save_chat,
    #         use_container_width=True,
    #     )

prompt = st.chat_input("Ask Max......", disabled=st.session_state.disabled)

st.markdown(
    """
    <style>
        [class*="st-key-fixed_buttons"] {
            position: fixed;
            bottom: 117px;
            align-items: left;
            padding-left: 10px
        }
         [data-test-id="stChatInputSubmitButton"] {
         visibility:hidden;
            position: absolute;
            bottom: -10;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
if prompt:
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        helper.display_content(message["content"], message["role"], streaming=False, chat_container=chat_container)
    print("Given Query: ", prompt)
    # Display user message
    helper.display_content(prompt, "user", chat_container=chat_container)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Getting Answers
    response = None
    print("Checking for a Valid Query...")
    valid_q = helper.fuzzy_match.check_closest_match(prompt)
    print("Matched to valid question:", valid_q)
    if valid_q in helper.query_lis:
        idx = helper.query_lis.index(valid_q)
        response = helper.qna[idx]["response"]
    else:
        response = {}   
        response["answer"] = (
            "I don't have exposure to enough data to answer this question."
        )
    # Display Assistant Response
    helper.display_content(response, "assistant", chat_container=chat_container)
    # Add response message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    is_new_chat = True
    for chat in st.session_state.recent_chats:
        print("chat_session_index : " ,chat)
        if chat['chat_session_index'] == st.session_state.chat_session_index:      
            is_new_chat = False

    if is_new_chat:
        messages = st.session_state.messages.copy()
        new_chat = {
            "title": f"{messages[0]['content']if len(messages)%2==0 else messages[1]['content']}",
            "messages": messages,
            "chat_session_index": st.session_state.chat_session_index,
        }
        st.session_state.recent_chats.append(new_chat)

def on_recent_chat_click(chat_object):
    print(f"Recent chat '{chat_object['title']}' clicked!")  # This will print in the terminal/logs
    st.session_state.messages = chat_object['messages']
    st.session_state.chat_session_index = chat_object['chat_session_index']
    for message in st.session_state.messages:
        helper.display_content(message["content"], message["role"], streaming=False, chat_container=chat_container)


# Recent Chats Section
recent_chats_expander = st.sidebar.expander("Recent Chats", icon=":material/schedule:")
for idx, chat in enumerate(reversed(st.session_state.recent_chats), 1):
    if recent_chats_expander.button(
        f"{idx}. {chat['title']}", 
        use_container_width=True, 
        key=f"{chat['title']}-{idx}"
    ):
        on_recent_chat_click(chat)

# Saved Chats Section
saved_chats_expander = st.sidebar.expander("Saved Chats", icon=":material/bookmark:")
for idx, chat in enumerate(reversed(st.session_state.saved_chats), 1):
    saved_chats_expander.button(f"{idx}.{chat['title']}", use_container_width=True)



# Hot Topics Section
hot_topics_expander = st.sidebar.expander("Hot Topics", icon=":material/local_fire_department:")

que1 = "Monthly rolling trend of hospital contracts won by MJN"
if hot_topics_expander.button(que1):
    # st.session_state.messages = []
    prompt = "month hospitals contracts net rolling won lost"
    helper.push_button(que1, prompt, chat_container, st.session_state.chat_session_index)

que3 = "How many births has MJN gained since 2022?"
if hot_topics_expander.button(que3):
    # st.session_state.messages = []
    prompt = "quarter births net won lost"
    helper.push_button(que3, prompt, chat_container, st.session_state.chat_session_index)

que15 = "Which retailers are having the best YOY growth for POS Sales?"
if hot_topics_expander.button(que15):
    # st.session_state.messages = []
    prompt = "retailers yoy growth best"
    helper.push_button(que15, prompt, chat_container, st.session_state.chat_session_index)

que5 = "Show state-wise performance for hospital contracts won"
if hot_topics_expander.button(que5):
    # st.session_state.messages = []
    prompt = "state net hospitals won"
    helper.push_button(que5, prompt, chat_container, st.session_state.chat_session_index)

que11 = "Compare monthly sales trends across top brands"
if hot_topics_expander.button(que11):
    # st.session_state.messages = []
    prompt = "month sales brand trend"
    helper.push_button(que11, prompt, chat_container, st.session_state.chat_session_index)

que6 = "Which hospital contracts are coming up for renewal?"
if hot_topics_expander.button(que6):
    # st.session_state.messages = []
    prompt = "hospitals contracts coming renewal expire"
    helper.push_button(que6, prompt, chat_container, st.session_state.chat_session_index)

que16 = "Which retailers are showing a decline in POS Sales?"
if hot_topics_expander.button(que16):
    # st.session_state.messages = []
    prompt = "retailers yoy growth negative"
    helper.push_button(que16, prompt, chat_container, st.session_state.chat_session_index)

que13 = "Show monthly sales trends for top retailers"
if hot_topics_expander.button(que13):
    # st.session_state.messages = []
    prompt = "month sales retailer trend"
    helper.push_button(que13, prompt, chat_container, st.session_state.chat_session_index)

que9 = "Which are the biggest hospitals that MJN has lost?"
if hot_topics_expander.button(que9):
    # st.session_state.messages = []
    prompt = "biggest hospital lost"
    helper.push_button(que9, prompt, chat_container, st.session_state.chat_session_index)

que12 = "Effect of Net Births Won on POS Sales"
if hot_topics_expander.button(que12):
    # st.session_state.messages = []
    prompt = "trend pos sales net births won comparison"
    helper.push_button(que12, prompt, chat_container, st.session_state.chat_session_index)

que8 = "States with the best / worst birth share for Reckitt"
if hot_topics_expander.button(que8):
    # st.session_state.messages = []
    prompt = "% percentage share birth state"
    helper.push_button(que8, prompt, chat_container, st.session_state.chat_session_index)

que14 = "Monthly POS sales in top performing states"
if hot_topics_expander.button(que14):
    # st.session_state.messages = []
    prompt = "month sales state trend"
    helper.push_button(que14, prompt, chat_container, st.session_state.chat_session_index)

que2 = "Quarterly trend of hospital contracts won by MJN"
if hot_topics_expander.button(que2):
    # st.session_state.messages = []
    prompt = "quarter hospitals net won lost"
    helper.push_button(que2, prompt, chat_container, st.session_state.chat_session_index)

que4 = "Monthly rolling trend of number of births won by MJN"
if hot_topics_expander.button(que4):
    # st.session_state.messages = []
    prompt = "month births net won lost"
    helper.push_button(que4, prompt, chat_container, st.session_state.chat_session_index)

que17 = "Monthly trend of hospital contracts won by MJN in 2024"
if hot_topics_expander.button(que17):
    # st.session_state.messages = []
    prompt = "month hospitals contracts net rolling won lost 2024"
    helper.push_button(que17, prompt, chat_container, st.session_state.chat_session_index)

que18 = "Monthly trend of hospital contracts won by MJN in 2023"
if hot_topics_expander.button(que18):
    # st.session_state.messages = []
    prompt = "month hospitals contracts net rolling won lost 2023"
    helper.push_button(que18, prompt, chat_container, st.session_state.chat_session_index)

que19 = "How many births has MJN gained since 2023?"
if hot_topics_expander.button(que19):
    # st.session_state.messages = []
    prompt = "quarter births net won lost 2023"
    helper.push_button(que19, prompt, chat_container, st.session_state.chat_session_index)

que20 = "How many births has MJN gained since 2024?"
if hot_topics_expander.button(que20):
    # st.session_state.messages = []
    prompt = "quarter births net won lost 2024"
    helper.push_button(que20, prompt, chat_container, st.session_state.chat_session_index)

que10 = "In which states does MJN have the most number of opportunity cities?"
if hot_topics_expander.button(que10):
    # st.session_state.messages = []
    prompt = "highest opportunity state"
    helper.push_button(que10, prompt, chat_container, st.session_state.chat_session_index)
