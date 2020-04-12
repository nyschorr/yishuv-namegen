#!/usr/bin/python3

import streamlit as st

from yishuvname import random_yishuv_name

st.title('Yishuv Name Generator')

if st.button('Generate a name'):
    st.header(random_yishuv_name())
