import streamlit as st
from typing import List, Dict

from prompt import categories,socials
from main import response_generator,chat_response_generator
from chat_history import update_linkedin_chat_history,get_linkedin_chat_history,get_twitter_chat_history

### INITIALIZE SESSION STATE
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

if 'social_media' not in st.session_state:
  st.session_state.social_media=None

if 'response' not in st.session_state:
  st.session_state.response=None


### FUNCTIONS
def generate_response_instance(data:str):
  st.session_state.response_state = True

def generate_clear_instance():
  st.session_state.inp1 = st.session_state.inp2 = st.session_state.inp3 = ""

def generate_done_instance(history_type:str,data:str,response:str):
  update_linkedin_chat_history(history_type,data,response)
  generate_clear_instance()
  st.session_state.inp_ws = ""

def generate_cancel_instance():
  generate_clear_instance()
  st.session_state.inp_ws = ""
  st.session_state.response_state = False

### DIALOG
@st.dialog("History Log",width="large")
def view_chat_history(media_type, history_type:str):

  chat_history = None
  if media_type == "linkedin":
    chat_history = get_linkedin_chat_history(history_type)
  elif media_type == "twitter":
    chat_history = get_twitter_chat_history(history_type)

  for chat in chat_history:
    st.chat_message("user" if chat.role=="user" else "assistant").markdown(chat.content)


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

### SIDEBAR
with st.sidebar:
  
  st.header("CONFIG PANEL",divider="orange")
  st.markdown("")
  st.session_state.social_selected= st.selectbox("Pick the Social Media",
    [word.capitalize() for word in socials],help="select the type of the social media")
  st.session_state.category_selected= st.selectbox("Pick the Post Category",
    [word.capitalize() for word in list(categories.keys())],help="select the type of the post")

  st.session_state.post_category = categories[st.session_state.category_selected.lower()]

  st.session_state.writing_style = st.text_input("Writing Style Guidelines",help="eg: professional, friendly, engaging",placeholder="optional",key="inp_ws")
  
  st.markdown("---")

  
  st.markdown("**HISTORY LOGS**")
  left,right = st.columns(2,vertical_alignment ="bottom",gap="small")
  history_category = right.selectbox("history",[word.capitalize() for word in list(categories.keys())],label_visibility="collapsed")
  media_type = left.selectbox("media",[word.capitalize() for word in socials],label_visibility="collapsed")
  if st.button("View History",use_container_width=True):
    view_chat_history(media_type.lower(),history_category.lower())

### CHAT 
inputs = list(st.session_state.post_category.items())

#### USER INPUT
with st.chat_message("user"):
  st.markdown(f"**{st.session_state.social_selected.upper()} - {st.session_state.category_selected.upper()} INFORMATION**")
  key1,value1 = inputs[0]
  key2,value2 = inputs[1]
  key3,value3 = inputs[2]
  inp1 = st.text_input(f"**{key1}**",placeholder=value1,key="inp1")
  inp2 = st.text_area(f"**{key2}**",placeholder=value2,key="inp2",height=150)
  inp3 = st.text_area(f"**{key3}**",placeholder=value3,key="inp3",height=68)
  st.session_state.data=f"{key1}:{inp1},/n{key2}:{inp2},/n{key3}:{inp3}"

  l1,l2,l3,middle,right = st.columns(5)
  middle.button("Clear",type="secondary",use_container_width=True,on_click=generate_clear_instance)
  
  if st.session_state.inp1.split() and st.session_state.inp2.split() and st.session_state.inp3.split():
    right.button("Generate",type="primary",use_container_width=True,on_click=generate_response_instance,args=[st.session_state.data])
  else:
    right.button("Generate",type="primary",use_container_width=True,disabled=True,on_click=generate_response_instance,args=[st.session_state.data])
  

#### DISPLAY Response
if st.session_state.response_state:
  with st.chat_message("assistant"):
    with st.spinner("Writing✏️..."):
      st.session_state.data=st.session_state.data+"/n/n"+response_generator(st.session_state.writing_style) if st.session_state.writing_style.strip() else st.session_state.data
      st.session_state.response = chat_response_generator(st.session_state.social_selected.lower(),st.session_state.category_selected.lower(),st.session_state.data)
    st.markdown(st.session_state.response)

    l1,right = st.columns([5,0.9])
    st.session_state.response_state=False
    right.button("retry",icon=":material/refresh:",use_container_width=True,on_click=generate_response_instance,args=[st.session_state.data])

  left,middle,right = st.columns([0.7,3,0.7],vertical_alignment ="bottom")
  right.button("Done",icon=":material/thumb_up:",type="primary",use_container_width=True,on_click=generate_done_instance,args=[st.session_state.category_selected.lower(),st.session_state.data,st.session_state.response])

  left.button("Cancel",icon=":material/close:",type="secondary",use_container_width=True,on_click=generate_cancel_instance)
