import streamlit as st
import numpy as np
import pandas as pd
from deta import Deta

st.set_page_config(layout='wide')
st.header('手机收集数据的尝试')

with st.form(key='1'):
    name = st.text_input('你的名字是')

    gender = st.selectbox(options=['男','女'],label='你的性别是')

    button = st.form_submit_button()

if button:
    data = {'name':name,'gender':gender}
    key = 'c0kd2hv8_r8eJSEiZjnna6Po9EoeiEgGYAwXA15QZ'
    deta = Deta(key)
    base = deta.Base("databasefortest")
    base.insert(data)
    # users = deta.Base("test")

    # users.insert(data)
    st.success('提交成功')