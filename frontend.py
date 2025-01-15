import streamlit as st
from typing import List, Dict

from prompt import linkedin_post_categories

# load_dotenv()

## INITIALIZE SESSION STATE
# if "messages" not in st.session_state:
#   st.session_state.messages = [{"role": "assistant", "response": "How may I assist you today?"}]

if 'source' not in st.session_state:
  st.session_state.source = {"active":False}

# if 'metadata' not in st.session_state:
#   st.session_state.metadata = [{}]

# if 'session_id' not in st.session_state:
#   st.session_state.session_id=None

if 'post_category' not in st.session_state:
  st.session_state.post_category=None
  
## INITIALIZE VARIABLES
# kb_dict={"Arxiv KB":"AWS_KNOWLEDGE_BASE_ID"}
category_selected=""

## FUNCTION TO CLEAR CHAT HISTORY
# def clear_chat_history():
#   st.session_state.messages = [{"role": "assistant", "response": "How may I assist you today?"}]
#   st.session_state.session_id=None

# def cancel_source():
#   st.session_state.source = {"active":False}

# def source_callback(metadata:List[Dict]):
#   st.session_state.metadata=metadata
#   st.session_state.source = {"active":True}

### HEADER COMPONENTS
st.title("Write-Up Agent")
st.subheader(f"AI-Powered Write-Up Assistant",divider="grey")

### SIDEBAR COMPONENTS
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 20em !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
  
  st.header("CONFIG PANEL")
  st.divider()

  category_selected= st.selectbox(
    "Pick Your Post Category",
    [word.capitalize() for word in list(linkedin_post_categories.keys())],help="select the type of the post"
  )
  st.session_state.post_category = linkedin_post_categories[category_selected.lower()]

  writing_style = st.text_input("Writing Style Guidelines",help="eg: professional, friendly, engaging",placeholder="optional")
  # st.sidebar.button('Clear History', on_click=clear_chat_history)

## DISPLAY CHAT HISTORY
# for message in st.session_state.messages:
    
#   with st.chat_message(message["role"]):

#     if message["role"] != "assistant":
#       st.markdown(message["response"])
#     else:
#       response = message["response"]
#       if isinstance(response, str):
#         try:
#           response = eval(response)
#         except Exception as e:
#           response = {"summary":message["response"]}
#       st.markdown(response["summary"])
#       if response.get("metadata") and len(response["metadata"]) > 0 and response["metadata"][0]["documentContent"]:
#         st.button("ℹ️", key=f"{hash(response['summary'])}", on_click=lambda r=response["metadata"]: source_callback(r))

### CHAT  
categories = list(st.session_state.post_category.items())

with st.chat_message("user"):
  st.markdown(f"**{category_selected.upper()} INFORMATION**")
  key,value = categories[0]
  inp1 = st.text_input(key,placeholder=value)
  key,value = categories[1]
  inp2 = st.text_area(key,placeholder=value,height=150)
  key,value = categories[2]
  inp3 = st.text_area(key,placeholder=value,height=68)

response_instance = st.chat_message("assistant")
with response_instance:
    with st.spinner("Analyzing..."):
      st.write('hello')

# if prompt := st.chat_input("Ask anything..."):
    
#   st.session_state.messages.append({"role": "user", "response": prompt})
#   with st.chat_message("user"):
#     st.markdown(prompt)
  
#   response_instance = st.chat_message("assistant")
#   with response_instance:
#     with st.spinner("Analyzing..."):
#       response = responseGenerator(query=prompt,session_id=st.session_state.session_id,knowledge_base_id=st.session_state.knowledge_base)
          
#   with response_instance:
#     st.markdown(response["summary"])
    
#     if response.get("metadata") and len(response["metadata"]) > 0 and response["metadata"][0]["documentContent"]:
#       st.button("ℹ️", key=f"{hash(response['summary'])}", on_click=lambda r=response["metadata"]: source_callback(r))
#     st.session_state.session_id=response['sessionId']
   
     
#     st.session_state.messages.append({"role": "assistant", "response": response})

    ## '{'content':'something'}'
    ## ' hi '