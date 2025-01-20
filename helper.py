import time
import streamlit as st
import fuzzy_match
import fuzzy_match_supply
import json

qna = json.load(open("qna.json",'rb'))
qna_supply = json.load(open("qna_supply.json", 'rb'))

states = json.load(open("states.json", 'rb'))
abb = dict(map(reversed, states.items()))

query_lis = [qset['query'].strip().lower() for qset in qna]
query_lis_supply = [qset['query'].strip().lower() for qset in qna_supply]

global count 
count= 0

def response_generator(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.15)

def write_text(text, streaming):
    # Inject custom CSS to set the text color of st.write to black
    if streaming:
        for line in text.split("\n\n"):
            st.write_stream(response_generator(line.strip()))
            time.sleep(0.1)
    else:
        st.write(text)



def display_content(response, user, streaming = True):
    global count
    if user == "assistant":
        with st.chat_message("assistant"):
            # Display any observations/responses
            write_text(response['answer'], streaming)

            # For DataFrames
            if response.get('dataframe', ''):
                dataframe = response['dataframe']
                if dataframe != []:
                    for df in dataframe:
                        if df.get('text1', '') != '':
                            write_text(df['text1'],streaming)
                        if df.get('code_path', '') !='':
                            with open(df['code_path'], 'r') as f:
                                code = f.read()
                            exec(code, globals())
                            if streaming:
                                time.sleep(2)
                                st.dataframe(globals()['xx'], key=count)
                                count = count + 1
                            else:
                                st.dataframe(globals()['xx'], key=count)
                                count = count + 1
                        if df.get('text2','') != '':
                            #st.write_stream(response_generator(topic.get('text2')))
                            write_text(df['text2'],streaming)
            # For Plots
            if response.get('graphs',None):
                graphs = response['graphs']
                if graphs != []:
                    for topic in graphs:
                        if topic.get('text1','') != '':
                            write_text(topic['text1'],streaming)
                            time.sleep(0.1)
                        if topic.get('code_path','') != '':
                            with open(topic['code_path'],'r') as f:
                                code = f.read()
                            exec(code,globals())
                            time.sleep(0.3)
                            if streaming:
                                time.sleep(2)
                                st.plotly_chart(globals()['fig'], key=count)
                                count = count + 1
                            else:
                                st.plotly_chart(globals()['fig'], key=count)
                                count = count + 1
                        if topic.get('path','') != '':
                            st.image(topic['path'])
                            time.sleep(0.1)
                        if topic.get('text2','') != '':
                            #st.write_stream(response_generator(topic.get('text2')))
                            write_text(topic['text2'],streaming)
            # For Links
            if response.get('link','') != '':
                tab_name = response.get('tab_name', '')
                st.write(f"**The information is also available in the 'Sherlock' Dashboard, in the {tab_name}**")
                st.link_button(label="Link To Dashboard", url = response['link'])
            
    elif user=='user':
        with st.chat_message("user"):
            st.markdown(response)


def display_content_supply(response, user, streaming = True):
    global count
    if user == "assistant":
        with st.chat_message("assistant"):
            # Display any observations/responses
            write_text(response['answer'], streaming)
            # For DataFrames
            if response.get('dataframe', ''):
                dataframe = response['dataframe']
                if dataframe != []:
                    for df in dataframe:
                        if df.get('text1', '') != '':
                            write_text(df['text1'],streaming)
                        if df.get('code_path', '') !='':
                            with open(df['code_path'], 'r') as f:
                                code = f.read()
                            exec(code, globals())
                            if streaming:
                                time.sleep(2)
                                st.dataframe(globals()['xx'], key=count, hide_index=True)
                                count = count + 1
                            else:
                                st.dataframe(globals()['xx'], key=count, hide_index=True)
                                count = count + 1
                        if df.get('text2','') != '':
                            #st.write_stream(response_generator(topic.get('text2')))
                            write_text(df['text2'],streaming)

            # For Plots
            if response.get('graphs',None):
                graphs = response['graphs']
                if graphs != []:
                    for topic in graphs:
                        if topic.get('text1','') != '':
                            write_text(topic['text1'],streaming)
                            time.sleep(0.1)
                        if topic.get('code_path','') != '':
                            with open(topic['code_path'],'r') as f:
                                code = f.read()
                            exec(code,globals())
                            time.sleep(0.3)
                            if streaming:
                                time.sleep(2)
                                st.plotly_chart(globals()['fig'], key=count)
                                count = count + 1
                            else:
                                st.plotly_chart(globals()['fig'], key=count)
                                count = count + 1
                        if topic.get('path','') != '':
                            st.image(topic['path'])
                            time.sleep(0.1)
                        if topic.get('text2','') != '':
                            #st.write_stream(response_generator(topic.get('text2')))
                            write_text(topic['text2'],streaming)
            # For Links
            if response.get('link','') != '':
                st.write(f"**The information is also available in the Supply Chain Dashboard**")
                st.link_button(label="Link To Dashboard", url = response['link'])
    elif user=='user':
        with st.chat_message("user"):
            st.markdown(response)




def push_button(label, actual):
    print("Given Query: ", actual)
    for message in st.session_state.messages:
        display_content(message["content"],message["role"], streaming=False)
    # Display user message
    with st.chat_message("user"):
        st.markdown(label)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": label})
    # Getting Answers
    response = None
    valid_q = actual.strip().lower()
    if valid_q in query_lis:
        print("Matched to valid question:", valid_q)
        idx = query_lis.index(valid_q.strip().lower())
        response = qna[idx]['response']
    else:
        response = {}
        response["answer"] = "I don't have exposure to enough data to answer this question."
    # Display Assistant Response
    display_content(response,"assistant")
    # Add response message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    #st.session_state.messages = []


def push_button_supply(label, actual):
    for message in st.session_state.messages_supply:
        display_content(message["content"],message["role"], streaming=False)
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
        response = qna_supply[idx]['response']
    else:
        response = {}
        response["answer"] = "I don't have exposure to enough data to answer this question."
    # Display Assistant Response
    display_content_supply(response,"assistant")
    # Add response message to chat history
    st.session_state.messages_supply.append({"role": "assistant", "content": response})
    #st.session_state.messages = []

def sherlock():
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "disabled" not in st.session_state:
        st.session_state.disabled = False

    col1, col2, col3 = st.columns([2,13,3])
    with col1:
        #st.markdown('\n')
        st.image('images/hosp.jpg', use_column_width='auto')
    with col2:
        st.markdown('\n')
        st.markdown("# Sherlock Agent\n_Built on top of the Sherlock Dashboard and the following datasets - 'hospital_report' and 'pos_inventory_data'_")

    with col3:
        #st.markdown('\n')
        if st.button("Clear Conversation", help="Click to reset the app", type='primary'):
            if "messages" in st.session_state:
                st.session_state.messages = []
            st.rerun()

    prompt = st.chat_input("Enter Your Query Here...", disabled = st.session_state.disabled)
    if prompt:
        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            display_content(message["content"],message["role"], streaming=False)
        print("Given Query: ",prompt)
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Getting Answers
        response = None
        print("Checking for a Valid Query...")
        valid_q = fuzzy_match.check_closest_match(prompt)
        print("Matched to valid question:", valid_q)
        if valid_q in query_lis:
            idx = query_lis.index(valid_q)
            response = qna[idx]['response']
        else:
            response = {}
            response["answer"] = "I don't have exposure to enough data to answer this question."
        # Display Assistant Response
        display_content(response,"assistant")
        # Add response message to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

    st.sidebar.markdown('## Most Popular Questions this Week')

    que1 = 'Monthly rolling trend of hospital contracts won by MJN'
    if st.sidebar.button(que1):
        #st.session_state.messages = []
        prompt = 'month hospitals contracts net rolling won lost'
        push_button(que1, prompt)


    que3 = "How many births has MJN gained since 2022?"
    if st.sidebar.button(que3):
        #st.session_state.messages = []
        prompt = 'quarter births net won lost'
        push_button(que3, prompt)

    que15 = "Which retailers are having the best YOY growth for POS Sales?"
    if st.sidebar.button(que15):
        #st.session_state.messages = []
        prompt = 'retailers yoy growth best'
        push_button(que15, prompt)

    que5 = "Show state-wise performance for hospital contracts won"
    if st.sidebar.button(que5):
        #st.session_state.messages = []
        prompt = 'state net hospitals won'
        push_button(que5, prompt)

    que11 = "Compare monthly sales trends across top brands"
    if st.sidebar.button(que11):
        #st.session_state.messages = []
        prompt = 'month sales brand trend'
        push_button(que11, prompt)

    que6 = "Which hospital contracts are coming up for renewal?"
    if st.sidebar.button(que6):
        #st.session_state.messages = []
        prompt = 'hospitals contracts coming renewal expire'
        push_button(que6, prompt)

    que16 = "Which retailers are showing a decline in POS Sales?"
    if st.sidebar.button(que16):
        #st.session_state.messages = []
        prompt = 'retailers yoy growth negative'
        push_button(que16, prompt)

    que13 = "Show monthly sales trends for top retailers"
    if st.sidebar.button(que13):
        #st.session_state.messages = []
        prompt = 'month sales retailer trend'
        push_button(que13, prompt)

    que9 = "Which are the biggest hospitals that MJN has lost?"
    if st.sidebar.button(que9):
        #st.session_state.messages = []
        prompt = 'biggest hospital lost'
        push_button(que9, prompt)
    

    que12 = "Effect of Net Births Won on POS Sales"
    if st.sidebar.button(que12):
        #st.session_state.messages = []
        prompt = 'trend pos sales net births won comparison'
        push_button(que12, prompt)

    que8 = "States with the best / worst birth share for Reckitt"
    if st.sidebar.button(que8):
        #st.session_state.messages = []
        prompt = '% percentage share birth state'
        push_button(que8, prompt)

    que14 = "Monthly POS sales in top performing states"
    if st.sidebar.button(que14):
        #st.session_state.messages = []
        prompt = 'month sales state trend'
        push_button(que14, prompt)

    que2 = "Quarterly trend of hospital contracts won by MJN"
    if st.sidebar.button(que2):
        #st.session_state.messages = []
        prompt = 'quarter hospitals net won lost'
        push_button(que2, prompt)

    que4 = "Monthly rolling trend of number of births won by MJN"
    if st.sidebar.button(que4):
        #st.session_state.messages = []
        prompt = 'month births net won lost'
        push_button(que4, prompt)

    que17 = 'Monthly trend of hospital contracts won by MJN in 2024'
    if st.sidebar.button(que17):
        #st.session_state.messages = []
        prompt = 'month hospitals contracts net rolling won lost 2024'
        push_button(que17, prompt)
    
    que18 = 'Monthly trend of hospital contracts won by MJN in 2023'
    if st.sidebar.button(que18):
        #st.session_state.messages = []
        prompt = 'month hospitals contracts net rolling won lost 2023'
        push_button(que18, prompt)

    que19 = "How many births has MJN gained since 2023?"
    if st.sidebar.button(que19):
        #st.session_state.messages = []
        prompt = 'quarter births net won lost 2023'
        push_button(que19, prompt)

    que20 = "How many births has MJN gained since 2024?"
    if st.sidebar.button(que20):
        #st.session_state.messages = []
        prompt = 'quarter births net won lost 2024'
        push_button(que20, prompt)

    que10 = "In which states does MJN have the most number of opportunity cities?"
    if st.sidebar.button(que10):
        #st.session_state.messages = []
        prompt = 'highest opportunity state'
        push_button(que10, prompt)

        
        
def supply():
    # Initialize chat history
    if "messages_supply" not in st.session_state:
        st.session_state.messages_supply = []
    if "disabled_supply" not in st.session_state:
        st.session_state.disabled_supply = False

    col1, col2, col3 = st.columns([2,13,3])
    with col1:
        #st.markdown('\n')
        st.image('images/supply.png', use_column_width='auto')
    with col2:
        st.markdown('\n')
        st.markdown("# Supply Chain Agent\n_Built on top of the Supply Chain Dashboard and the following datasets - 'supply_information'_")

    with col3:
        #st.markdown('\n')
        if st.button("Clear Conversation", help="Click to reset the app", type='primary'):
            if "messages_supply" in st.session_state:
                st.session_state.messages_supply = []
            st.rerun()


    prompt = st.chat_input("Enter Your Query Here...", disabled = st.session_state.disabled_supply)
    if prompt:
        # Display chat messages from history on app rerun
        for message in st.session_state.messages_supply:
            display_content(message["content"],message["role"], streaming=False)
        print("Given Query: ",prompt)
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages_supply.append({"role": "user", "content": prompt})
        # Getting Answers
        response = None
        print("Checking for a Valid Query...")
        valid_q = fuzzy_match_supply.check_closest_match(prompt).strip().lower()
        print("Matched to valid question:", valid_q)
        if valid_q in query_lis_supply:
            idx = query_lis_supply.index(valid_q)
            response = qna_supply[idx]['response']
        else:
            response = {}
            response["answer"] = "I don't have exposure to enough data to answer this question."
        # Display Assistant Response
        display_content(response,"assistant")
        # Add response message to chat history
        st.session_state.messages_supply.append({"role": "assistant", "content": response})

    st.sidebar.markdown('## Most Popular Questions this Week')

    que1 = 'What was the total cost to serve the German market in 2023'
    if st.sidebar.button(que1):
        #st.session_state.messages = []
        prompt = 'What was the total cost to serve the German market in 2023'
        push_button_supply(que1, prompt)

    que2 = "How has the cost to serve evolved from 2022?"
    if st.sidebar.button(que2):
        #st.session_state.messages = []
        prompt = 'How has the cost to serve evolved from 2022?'
        push_button_supply(que2, prompt)

    que3 = "What are the drivers of increase in transport costs?"
    if st.sidebar.button(que3):
        #st.session_state.messages = []
        prompt = 'What are the drivers of increase in transport costs?'
        push_button_supply(que3, prompt)

    que6 = "Explore reduction of SLA of top 40 customers and generate scenarios to identify cost savings."
    if st.sidebar.button(que6):
        #st.session_state.messages = []
        prompt = 'Explore reduction of SLA of top 40 customers and generate scenarios to identify cost savings.'
        push_button_supply(que6, prompt)
        
    que8 = "Specify cost savings for Customer ID Dir_239"
    if st.sidebar.button(que8):
        #st.session_state.messages = []
        prompt = 'Specify cost savings for Customer ID Dir_239'
        push_button_supply(que8, prompt)

    que5 = "How can the average pallets per trip be controlled / improved"
    if st.sidebar.button(que5):
        #st.session_state.messages = []
        prompt = 'How can the average pallets per trip be controlled / improved'
        push_button_supply(que5, prompt)

    que7 = "Explore reduction of SLA of top 20 customers and generate scenarios to identify cost savings."
    if st.sidebar.button(que7):
        #st.session_state.messages = []
        prompt = 'Explore reduction of SLA of top 20 customers and generate scenarios to identify cost savings.'
        push_button_supply(que7, prompt)

    que9 = "Specify cost savings for Customer ID Dir_121"
    if st.sidebar.button(que9):
        #st.session_state.messages = []
        prompt = 'Specify cost savings for Customer ID Dir_121'
        push_button_supply(que9, prompt)



