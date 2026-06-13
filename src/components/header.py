import streamlit as st
import base64


def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def header_home():

    logo_base64 = get_base64_image("src/logo/attendexa_icon.png")

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='data:image/png;base64,{logo_base64}' style='height:100px;' />
            <h1 style='text-align:center; color:#E0E3FF'>Attendexa</h1>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():

    logo_base64 = get_base64_image("src/logo/attendexa_icon.png")

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='data:image/png;base64,{logo_base64}' style='height:75px;' />
            <h2 style='text-align:left; color:#5865F2'>Attendexa</h2>
        </div>   
                
                """, unsafe_allow_html=True)