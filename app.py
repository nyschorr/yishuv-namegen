#!/usr/bin/python3

import streamlit as st

from yishuvname import random_yishuv_name

with open('yishuvim.txt') as f:
    yishuvim = f.readlines()
yishuvim = [y.strip() for y in yishuvim]

st.title('Yishuv Name Generator')

if st.button('Generate a name'):
    name = random_yishuv_name()
    st.header(name)
    if name in yishuvim:
        st.subheader('(This randomly generated name is actually a real place)')
