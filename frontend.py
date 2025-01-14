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

if 'knowledge_base' not in st.session_state:
  st.session_state.knowledge_base=None
  
## INITIALIZE VARIABLES
# kb_dict={"Arxiv KB":"AWS_KNOWLEDGE_BASE_ID"}
kb_selected=""

## FUNCTION TO CLEAR CHAT HISTORY
# def clear_chat_history():
#   st.session_state.messages = [{"role": "assistant", "response": "How may I assist you today?"}]
#   st.session_state.session_id=None

# def cancel_source():
#   st.session_state.source = {"active":False}

# def source_callback(metadata:List[Dict]):
#   st.session_state.metadata=metadata
#   st.session_state.source = {"active":True}

### SIDEBAR COMPONENTS
with st.sidebar:
  
  category_selected= st.selectbox(
    "Choose The Post Category",
    (list(linkedin_post_categories.keys()))
  )
  st.session_state.knowledge_base = linkedin_post_categories[category_selected]

  st.divider()
  st.sidebar.button('Clear History', on_click=clear_chat_history)

### HEADER COMPONENTS
st.title("QA Agent")
st.subheader(f"AI-Powered Search Assistant")
st.caption(f"Uses the {kb_selected} Knowledge Base")
st.divider()

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
if prompt := st.chat_input("Ask anything..."):
    
  st.session_state.messages.append({"role": "user", "response": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)
  
  response_instance = st.chat_message("assistant")
  with response_instance:
    with st.spinner("Analyzing..."):
      response = responseGenerator(query=prompt,session_id=st.session_state.session_id,knowledge_base_id=st.session_state.knowledge_base)
          
  with response_instance:
    st.markdown(response["summary"])
    
    if response.get("metadata") and len(response["metadata"]) > 0 and response["metadata"][0]["documentContent"]:
      st.button("ℹ️", key=f"{hash(response['summary'])}", on_click=lambda r=response["metadata"]: source_callback(r))
    st.session_state.session_id=response['sessionId']
   
     
    st.session_state.messages.append({"role": "assistant", "response": response})

    ## '{'content':'something'}'
    ## ' hi '