import time
import streamlit as st
import fuzzy_match
import fuzzy_match_supply
import json
from datetime import datetime

qna = json.load(open("qna.json", "rb"))
qna_supply = json.load(open("qna_supply.json", "rb"))

states = json.load(open("states.json", "rb"))
abb = dict(map(reversed, states.items()))

query_lis = [qset["query"].strip().lower() for qset in qna]
query_lis_supply = [qset["query"].strip().lower() for qset in qna_supply]

global count
count = 0


def response_generator(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.075)


def write_text(text, streaming):
    # Inject custom CSS to set the text color of st.write to black
    if streaming:
        for line in text.split("\n\n"):
            st.write_stream(response_generator(line.strip()))
            time.sleep(0.1)
    else:
        st.write(text)


def display_content(response, user, streaming=True, chat_container=None):
    # Add Material Icons CSS
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <style>
            .material-icons {
                font-size: 20px !important;
                vertical-align: middle !important;
                color: #555 !important;
                border: none !important;
                border-radius: 5px !important;
                padding: 5px 7.5px !important;
            }
            .material-icons:hover {
                background-color: #ffffff !important;
            }
            .button-container {
                display: flex;
                flex-wrap: nowrap; /* Prevents wrapping */
                gap: 2px; /* Space between buttons */
                justify-content: left; /* Center align */
                align-items: center;
                overflow-x: auto; /* Horizontal scrolling if needed */
                padding: 0px 0px 10px 0px;
                max-width: 100%;
            }
        </style>
    """,
        unsafe_allow_html=True,
    )

    global count
    col1, col2 = st.columns([8, 2])
    col3, col4 = st.columns([4, 6])
    
    with chat_container:
        if user == "assistant":
            with col1:
                with st.chat_message("assistant"):
                    # Display any observations/responses
                    write_text(response["answer"], streaming)

                    # For DataFrames
                    if response.get("dataframe", ""):
                        dataframe = response["dataframe"]
                        if dataframe != []:
                            for df in dataframe:
                                if df.get("text1", "") != "":
                                    write_text(df["text1"], streaming)
                                if df.get("code_path", "") != "":
                                    with open(df["code_path"], "r") as f:
                                        code = f.read()
                                    exec(code, globals())
                                    if streaming:
                                        time.sleep(2)
                                        st.dataframe(globals()["xx"], key=count)
                                        count = count + 1
                                    else:
                                        st.dataframe(globals()["xx"], key=count)
                                        count = count + 1
                                if df.get("text2", "") != "":
                                    # st.write_stream(response_generator(topic.get('text2')))
                                    write_text(df["text2"], streaming)
                    # For Plots
                    if response.get("graphs", None):
                        graphs = response["graphs"]
                        if graphs != []:
                            for topic in graphs:
                                if topic.get("text1", "") != "":
                                    write_text(topic["text1"], streaming)
                                    time.sleep(0.1)
                                if topic.get("code_path", "") != "":
                                    with open(topic["code_path"], "r") as f:
                                        code = f.read()
                                    exec(code, globals())
                                    time.sleep(0.3)
                                    if streaming:
                                        time.sleep(2)
                                        st.plotly_chart(globals()["fig"], key=count)
                                        count = count + 1
                                    else:
                                        st.plotly_chart(globals()["fig"], key=count)
                                        count = count + 1
                                if topic.get("path", "") != "":
                                    st.image(topic["path"])
                                    time.sleep(0.1)
                                if topic.get("text2", "") != "":
                                    # st.write_stream(response_generator(topic.get('text2')))
                                    write_text(topic["text2"], streaming)
                    # For Links
                    if response.get("link", "") != "":
                        tab_name = response.get("tab_name", "")
                        st.write(
                            f"**The information is also available in the 'Sherlock' Dashboard, in the {tab_name}**"
                        )
                        st.link_button(label="Link To Dashboard", url=response["link"])
                    st.markdown(
                    """
                    <div class="button-container">
                        <button class="material-icons" onclick='alert(hello)'>thumb_up</button>
                        <button class="material-icons">thumb_down</button>
                        <button class="material-icons">refresh</button>
                        <button class="material-icons">share</button>
                        <button class="material-icons">more_vert</button>
                    </div>
                    """,
                    unsafe_allow_html=True,
                    )
                    # Add interaction buttons in a horizontal layout
                    # button_cols = st.columns([1, 1, 1, 1, 1, 15])  # 4 buttons + spacing
                    # with button_cols[0]:
                    #     st.markdown('<button class="material-icons">thumb_up</button>', unsafe_allow_html=True)
                    # with button_cols[1]:
                    #     st.markdown('<button class="material-icons">thumb_down</button>', unsafe_allow_html=True)
                    # with button_cols[2]:
                    #     st.markdown('<button class="material-icons">refresh</button>', unsafe_allow_html=True)
                    # with button_cols[3]:
                    #     st.markdown('<button class="material-icons">share</button>', unsafe_allow_html=True)
                    # with button_cols[4]:
                    #     st.markdown('<button class="material-icons">more_vert</button>', unsafe_allow_html=True)    
                    count += 1

            with col2:
                st.markdown("")
        elif user == "user":
            with col3:
                st.markdown(" ")        
            with col4:
                with st.chat_message("user"):
                    st.markdown(response)
                


def display_content_supply(response, user, streaming=True):
    global count
    if user == "assistant":
        with st.chat_message("assistant"):
            # Display any observations/responses
            write_text(response["answer"], streaming)
            # For DataFrames
            if response.get("dataframe", ""):
                dataframe = response["dataframe"]
                if dataframe != []:
                    for df in dataframe:
                        if df.get("text1", "") != "":
                            write_text(df["text1"], streaming)
                        if df.get("code_path", "") != "":
                            with open(df["code_path"], "r") as f:
                                code = f.read()
                            exec(code, globals())
                            if streaming:
                                time.sleep(2)
                                st.dataframe(
                                    globals()["xx"], key=count, hide_index=True
                                )
                                count = count + 1
                            else:
                                st.dataframe(
                                    globals()["xx"], key=count, hide_index=True
                                )
                                count = count + 1
                        if df.get("text2", "") != "":
                            # st.write_stream(response_generator(topic.get('text2')))
                            write_text(df["text2"], streaming)

            # For Plots
            if response.get("graphs", None):
                graphs = response["graphs"]
                if graphs != []:
                    for topic in graphs:
                        if topic.get("text1", "") != "":
                            write_text(topic["text1"], streaming)
                            time.sleep(0.1)
                        if topic.get("code_path", "") != "":
                            with open(topic["code_path"], "r") as f:
                                code = f.read()
                            exec(code, globals())
                            time.sleep(0.3)
                            if streaming:
                                time.sleep(2)
                                st.plotly_chart(globals()["fig"], key=count)
                                count = count + 1
                            else:
                                st.plotly_chart(globals()["fig"], key=count)
                                count = count + 1
                        if topic.get("path", "") != "":
                            st.image(topic["path"])
                            time.sleep(0.1)
                        if topic.get("text2", "") != "":
                            # st.write_stream(response_generator(topic.get('text2')))
                            write_text(topic["text2"], streaming)
            # For Links
            if response.get("link", "") != "":
                st.write(
                    f"**The information is also available in the Supply Chain Dashboard**"
                )
                st.link_button(label="Link To Dashboard", url=response["link"])
    elif user == "user":
        with st.chat_message("user"):
            st.markdown(response)


def push_button(label, actual, chat_container, chat_session_index = 0):
    print("Given Query: ", actual)
    for message in st.session_state.messages:
        display_content(message["content"], message["role"], streaming=False, chat_container=chat_container)
        
    # Display user message
    display_content(label, "user", chat_container=chat_container)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": label})
    # Getting Answers
    response = None
    valid_q = actual.strip().lower()
    if valid_q in query_lis:
        print("Matched to valid question:", valid_q)
        idx = query_lis.index(valid_q.strip().lower())
        response = qna[idx]["response"]
    else:
        response = {}
        response["answer"] = (
            "I don't have exposure to enough data to answer this question."
        )
    # Display Assistant Response
    display_content(response, "assistant", chat_container=chat_container)
    # Add response message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    # st.session_state.messages = []
    if "recent_chats" not in st.session_state:
        st.session_state.recent_chats = []
    
    is_new_chat = True
    for chat in st.session_state.recent_chats:
        print("chat_session_index : " ,chat['chat_session_index'])
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
    # Force a rerun to update the UI
    # st.rerun()


def push_button_supply(label, actual):
    for message in st.session_state.messages_supply:
        display_content(message["content"], message["role"], streaming=False)
    print("Given Query: ", actual)
    # Display user message
    with st.chat_message("user"):
        st.markdown(label)
    # Add user message to chat history
    st.session_state.messages_supply.append({"role": "user", "content": label})
    # Getting Answers
    response = None
    valid_q = actual.strip().lower()
    print("Matched to valid question:", valid_q)
    if valid_q.strip().lower() in query_lis_supply:
        idx = query_lis_supply.index(valid_q.strip().lower())
        response = qna_supply[idx]["response"]
    else:
        response = {}
        response["answer"] = (
            "I don't have exposure to enough data to answer this question."
        )
    # Display Assistant Response
    display_content_supply(response, "assistant",)
    # Add response message to chat history
    st.session_state.messages_supply.append({"role": "assistant", "content": response})
    # st.session_state.messages = []


def max():
    chat_container = st.container()
    def handle_save_chat():
        # Update recent chats (limiting to 5 most recent)
        if "messages" in st.session_state and st.session_state.messages:
            new_chat = {
                "title": f"Chat on {datetime.now().strftime('%Y-%m-%d %H:%M')}",
                "messages": st.session_state.messages.copy(),
            }
            if "recent_chats" not in st.session_state:
                st.session_state.recent_chats = []
            st.session_state.recent_chats.append(new_chat)
            if len(st.session_state.recent_chats) > 5:
                st.session_state.recent_chats.pop(0)
            # Clear current messages
            if "messages" in st.session_state:
                st.session_state.messages = []
   

    with chat_container:
            header_cols = st.columns([8, 2])   
            with header_cols[0]:
                st.markdown(
                        """
                        <div style="text-align: left;">
                            <h1 style="margin: 0; font-size: clamp(20px, 3vw, 32px); padding: 0;">MAX</h1>
                            <p style="margin: 0; font-size: clamp(12px, 1.5vw, 18px);">Modern Analytics Xplorer/Xpert</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                
            with header_cols[1]:
                    # Create columns for buttons with equal width
                button_cols = st.columns(2)
                with button_cols[0]:
                        st.button(
                            "Save",
                            help="Click to save the chat",
                            type="primary",
                            key="save_button",
                            on_click=handle_save_chat,
                            use_container_width=True,
                        )
                with button_cols[1]:
                    st.button(
                            "Clear",
                            help="Click to reset the app",
                            type="primary",
                            key="clear_button",
                            on_click=lambda: (
                                st.session_state.update({"messages": []})
                                if "messages" in st.session_state
                                else None
                            ),
                            use_container_width=True,
                        )
    

        
        # Initialize chat history
        
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Add welcome message when session starts
        welcome_response = {
            "answer": "👋 Hello! I'm MAX (Modern Analytics Xplorer/Xpert). Feel free to ask me anything or check out the Hot Topics in the sidebar for some suggested questions!",
            "dataframe": [],
            "graphs": [],
            "link": "",
            "tab_name": ""
        }
        st.session_state.messages.append({"role": "assistant", "content": welcome_response})
        # Display welcome message immediately
        display_content(welcome_response, "assistant", streaming=True, chat_container=chat_container)
    
    if "recent_chats" not in st.session_state:
        st.session_state.recent_chats = []
    if "disabled" not in st.session_state:
        st.session_state.disabled = False


    prompt = st.chat_input("Ask Max......", disabled=st.session_state.disabled)

    if prompt:
        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            display_content(message["content"], message["role"], streaming=False, chat_container=chat_container)
        print("Given Query: ", prompt)
        # Display user message
        display_content(prompt, "user", chat_container=chat_container)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Getting Answers
        response = None
        print("Checking for a Valid Query...")
        valid_q = fuzzy_match.check_closest_match(prompt)
        print("Matched to valid question:", valid_q)
        if valid_q in query_lis:
            idx = query_lis.index(valid_q)
            response = qna[idx]["response"]
        else:
            response = {}
            response["answer"] = (
                "I don't have exposure to enough data to answer this question."
            )
        # Display Assistant Response
        display_content(response, "assistant", chat_container=chat_container)
        # Add response message to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    # Recent Chats Section
    saved_chats_expander = st.sidebar.expander("Saved Chats", icon=":material/bookmark:")
    for idx, chat in enumerate(reversed(st.session_state.recent_chats), 1):
        saved_chats_expander.write(f"{idx}. {chat['title']}")


    # Hot Topics Section
    hot_topics_expander = st.sidebar.expander("Hot Topics", icon=":material/local_fire_department:")

    que1 = "Monthly rolling trend of hospital contracts won by MJN"
    if hot_topics_expander.button(que1):
        # st.session_state.messages = []
        prompt = "month hospitals contracts net rolling won lost"
        push_button(que1, prompt, chat_container)

    que3 = "How many births has MJN gained since 2022?"
    if hot_topics_expander.button(que3):
        # st.session_state.messages = []
        prompt = "quarter births net won lost"
        push_button(que3, prompt, chat_container)

    que15 = "Which retailers are having the best YOY growth for POS Sales?"
    if hot_topics_expander.button(que15):
        # st.session_state.messages = []
        prompt = "retailers yoy growth best"
        push_button(que15, prompt, chat_container)

    que5 = "Show state-wise performance for hospital contracts won"
    if hot_topics_expander.button(que5):
        # st.session_state.messages = []
        prompt = "state net hospitals won"
        push_button(que5, prompt, chat_container)

    que11 = "Compare monthly sales trends across top brands"
    if hot_topics_expander.button(que11):
        # st.session_state.messages = []
        prompt = "month sales brand trend"
        push_button(que11, prompt, chat_container)

    que6 = "Which hospital contracts are coming up for renewal?"
    if hot_topics_expander.button(que6):
        # st.session_state.messages = []
        prompt = "hospitals contracts coming renewal expire"
        push_button(que6, prompt, chat_container)

    que16 = "Which retailers are showing a decline in POS Sales?"
    if hot_topics_expander.button(que16):
        # st.session_state.messages = []
        prompt = "retailers yoy growth negative"
        push_button(que16, prompt, chat_container)

    que13 = "Show monthly sales trends for top retailers"
    if hot_topics_expander.button(que13):
        # st.session_state.messages = []
        prompt = "month sales retailer trend"
        push_button(que13, prompt, chat_container)

    que9 = "Which are the biggest hospitals that MJN has lost?"
    if hot_topics_expander.button(que9):
        # st.session_state.messages = []
        prompt = "biggest hospital lost"
        push_button(que9, prompt, chat_container)

    que12 = "Effect of Net Births Won on POS Sales"
    if hot_topics_expander.button(que12):
        # st.session_state.messages = []
        prompt = "trend pos sales net births won comparison"
        push_button(que12, prompt, chat_container)

    que8 = "States with the best / worst birth share for Reckitt"
    if hot_topics_expander.button(que8):
        # st.session_state.messages = []
        prompt = "% percentage share birth state"
        push_button(que8, prompt, chat_container)

    que14 = "Monthly POS sales in top performing states"
    if hot_topics_expander.button(que14):
        # st.session_state.messages = []
        prompt = "month sales state trend"
        push_button(que14, prompt, chat_container)

    que2 = "Quarterly trend of hospital contracts won by MJN"
    if hot_topics_expander.button(que2):
        # st.session_state.messages = []
        prompt = "quarter hospitals net won lost"
        push_button(que2, prompt, chat_container)

    que4 = "Monthly rolling trend of number of births won by MJN"
    if hot_topics_expander.button(que4):
        # st.session_state.messages = []
        prompt = "month births net won lost"
        push_button(que4, prompt, chat_container)

    que17 = "Monthly trend of hospital contracts won by MJN in 2024"
    if hot_topics_expander.button(que17):
        # st.session_state.messages = []
        prompt = "month hospitals contracts net rolling won lost 2024"
        push_button(que17, prompt, chat_container)

    que18 = "Monthly trend of hospital contracts won by MJN in 2023"
    if hot_topics_expander.button(que18):
        # st.session_state.messages = []
        prompt = "month hospitals contracts net rolling won lost 2023"
        push_button(que18, prompt, chat_container)

    que19 = "How many births has MJN gained since 2023?"
    if hot_topics_expander.button(que19):
        # st.session_state.messages = []
        prompt = "quarter births net won lost 2023"
        push_button(que19, prompt, chat_container)

    que20 = "How many births has MJN gained since 2024?"
    if hot_topics_expander.button(que20):
        # st.session_state.messages = []
        prompt = "quarter births net won lost 2024"
        push_button(que20, prompt, chat_container)

    que10 = "In which states does MJN have the most number of opportunity cities?"
    if hot_topics_expander.button(que10):
        # st.session_state.messages = []
        prompt = "highest opportunity state"
        push_button(que10, prompt, chat_container)

