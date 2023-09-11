import streamlit as st
from streamlit_chat import message
from streamlit.components.v1 import html
from chat import chater

api_key=st.secrets["api_key"]


def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)
    bot_response = chater(user_input,api_key)
    st.session_state.generated.append({'type': 'normal', 'data': bot_response})
    st.session_state.user_input = ""

def on_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]

st.session_state.setdefault(
    'past', 
    []
)

st.session_state.setdefault(
    'generated', 
    []
)

st.title("MR.MAVELI")


chat_placeholder = st.empty()

with chat_placeholder.container():    
    for i in range(len(st.session_state['generated'])):
        message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
        message(
            st.session_state['generated'][i]['data'], 
            avatar_style="circle",logo="https://w7.pngwing.com/pngs/666/476/png-transparent-man-holding-red-umbrella-illustration-onam-vallam-kali-kerala-kerala-miscellaneous-wish-fictional-character.png",
            key=f"{i}", 
            allow_html=True,
            is_table=True if st.session_state['generated'][i]['type']=='table' else False,
        )
    
    st.button("Clear Chat", on_click=on_btn_click)

with st.container():
    
    st.text_input("User Input:", on_change=on_input_change, key="user_input")
