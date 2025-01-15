import streamlit as st
from typing import List, Dict

from prompt import linkedin_post_categories
from main import response_generator,chat_response_generator
from chat_history import update_linkedin_chat_history

# load_dotenv()

## INITIALIZE SESSION STATE
# if "messages" not in st.session_state:
#   st.session_state.messages = [{"role": "assistant", "response": "How may I assist you today?"}]

if 'response_state' not in st.session_state:
  st.session_state.response_state = False

if 'category_selected' not in st.session_state:
  st.session_state.category_selected = None

if 'writing_style' not in st.session_state:
  st.session_state.writing_style = ""

if 'data' not in st.session_state:
  st.session_state.data = None

if 'post_category' not in st.session_state:
  st.session_state.post_category=None

## INITIALIZE VARIABLES
# kb_dict={"Arxiv KB":"AWS_KNOWLEDGE_BASE_ID"}

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
st.subheader(f"AI-Powered Write-Up Assistant",divider="orange")

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
  
  st.header("CONFIG PANEL",divider="orange")

  st.session_state.category_selected= st.selectbox(
    "Pick Your Post Category",
    [word.capitalize() for word in list(linkedin_post_categories.keys())],help="select the type of the post"
  )
  st.session_state.post_category = linkedin_post_categories[st.session_state.category_selected.lower()]

  st.session_state.writing_style = st.text_input("Writing Style Guidelines",help="eg: professional, friendly, engaging",placeholder="optional",key="inp_ws")
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
def generate_response_instance(data:str):
  st.session_state.response_state = True

categories = list(st.session_state.post_category.items())

def generate_done_instance(history_type:str,data:str,response:str):
  update_linkedin_chat_history(history_type,data,response)
  generate_clear_instance()
  st.session_state.inp_ws = ""

def generate_clear_instance():
  st.session_state.inp1 = st.session_state.inp2 = st.session_state.inp3 = ""

with st.chat_message("user"):
  st.markdown(f"**{st.session_state.category_selected.upper()} INFORMATION**")
  key1,value1 = categories[0]
  key2,value2 = categories[1]
  key3,value3 = categories[2]
  inp1 = st.text_input(key1,placeholder=value1,key="inp1")
  inp2 = st.text_area(key2,placeholder=value2,key="inp2",height=150)
  inp3 = st.text_area(key3,placeholder=value3,key="inp3",height=68)
  st.session_state.data=f"{key1}:{inp1},/n{key2}:{inp2},/n{key3}:{inp3}"

  l1,l2,l3,middle,right = st.columns(5)
  middle.button("Clear",type="secondary",use_container_width=True,on_click=generate_clear_instance)
  
  if st.session_state.inp1.split() and st.session_state.inp2.split() and st.session_state.inp3.split():
    right.button("Generate",type="primary",use_container_width=True,on_click=generate_response_instance,args=[st.session_state.data])
  else:
    right.button("Generate",type="primary",use_container_width=True,disabled=True,on_click=generate_response_instance,args=[st.session_state.data])
  
if st.session_state.response_state:
  with st.chat_message("assistant"):
    with st.spinner("Writing✏️..."):
      st.session_state.data=st.session_state.data+"/n/n"+response_generator(st.session_state.writing_style) if st.session_state.writing_style.strip() else st.session_state.data
      response = chat_response_generator(st.session_state.category_selected.lower(),st.session_state.data)
    st.markdown(response)

    l1,l2,l3,l4,middle,right = st.columns(6)
    st.session_state.response_state=False
    middle.button("retry",icon=":material/refresh:",use_container_width=True,on_click=generate_response_instance,args=[st.session_state.data])
    
    right.button("Done",icon=":material/check:",type="primary",on_click=generate_done_instance,args=[st.session_state.category_selected.lower(),st.session_state.data,response])
    
# # Check the rerun flag and trigger rerun
# if st.session_state.should_rerun:
#   st.session_state.response_state=False
#   st.session_state.should_rerun = False  # Reset the flag
#   st.rerun(scope="app")
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