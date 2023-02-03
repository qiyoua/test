import streamlit as st
import numpy as np
import pandas as pd
from deta import Deta

st.set_page_config(layout='wide')
st.header('性格测试题')
st.text('接下来是性格测试题,都是单选')
answer = []
label = None
with st.form(key='1'):
    
    q1_text = '今天你放学回家，打开信箱看到一封写给你的邀请卡，原来是好朋友要邀请你到他家参加派对！你觉得这张卡片会是什么颜色？ '
    q1_dict = {'红':5,'黄':1,'蓝':2,'绿':3}
    q1 = st.radio(q1_text,list(q1_dict.keys()))
    answer.append(q1_dict[q1])

    q2_text = '拿着邀请卡的你来到了好朋友的家门口，你觉得这入口会是？ '
    q2_dict = {'一部超级大的电脑':4,' 一扇绿色的大门':1,'一个正在发光的洞口':3}
    q2 = st.radio(q2_text,list(q2_dict.keys()))
    answer.append(q2_dict[q2])

    q3_text = '你到了TA的家，TA热情地招待你，在餐桌上放满了食物。你觉得桌上会是什么食物？ '
    q3_dict = {'糖果和饼干':3,' 汉堡和汽水':2,'蛋糕和果汁':1}
    q3 = st.radio(q3_text,list(q3_dict.keys()))
    answer.append(q3_dict[q3])

    q4_text = '接着，好友带你到处玩，因为你的好友是路痴，你们迷路了，这时远方来了一个人正要走过来，你希望会是谁出现？'
    q4_dict = {'不认识的人':1,' 好友的爸爸':2,'在好友家中工作的人':4,'你其他的朋友':3}
    q4 = st.radio(q4_text,list(q4_dict.keys()))
    answer.append(q4_dict[q4])

    q5_text = '走着走着，你们来到一条大河，你最想要做什么？ '
    q5_dict = {'打水战':3,' 游泳':1,'抓鱼':5}
    q5 = st.radio(q5_text,list(q5_dict.keys()))
    answer.append(q5_dict[q5])

    q6_text = '在你离开之前，好友想和你交换一样东西做纪念，你会交换什么？ '
    q6_dict = {'玩偶':2,' 电动':4,'漫画':1}
    q6 = st.radio(q6_text,list(q6_dict.keys()))
    answer.append(q6_dict[q6])

    q7_text = '你会怎样回家? '
    q7_dict = {' 步行':2,' 的士':1,'巴士':3}
    q7 = st.radio(q7_text,list(q7_dict.keys()))
    answer.append(q7_dict[q7])

    q8_text = '你已经玩得很累了，带着快乐又满足的心情回到家后，你首先想做什么？  '
    q8_dict = {'马上告诉家人或好朋友':5,' 先倒头呼呼大睡':2,'继续玩':1}
    q8 = st.radio(q8_text,list(q8_dict.keys()))
    answer.append(q8_dict[q8])
    
    q9_text = '你已睡着了......正在做梦，你在发什么梦? '
    q9_dict = {'大吃大喝的梦':3,' 和喜欢的人一起的梦':2,'没有发梦':1,'春梦':4}
    q9 = st.radio(q9_text,list(q9_dict.keys()))
    answer.append(q9_dict[q9])
    
    q10_text = '你对这次派对有什么感想? '
    q10_dict = {'好开心':3,'没什么特别感觉-':1,'好闷好无聊':2}
    q10 = st.radio(q10_text,list(q10_dict.keys()))
    answer.append(q10_dict[q10])


    button = st.form_submit_button()

if button:
    score = np.sum(answer)
    if score >= 37:
        label = '机智，处变不惊的人'
    elif 33 <= score <=37:
        label = '有温柔的外表，坚强内心的人'
    elif 29 <= score <=32:
        label = '幽默，有鬼点子的人'
    elif 25 <= score <=28:
        label = '打抱不平，勇于表现自我的人'
    elif 21 <= score <=24:
        label = '热情有朝气，有幽默感的人'
    elif 16 <= score <=20:
        label = '积极上进，肯吃苦耐劳的人'
    elif 12 <= score <=15:
        label = '有抱负，不轻言放弃的人'
    elif 10 <= score <=11:
        label = '聪明，理性又内敛的人'

    data = {'label':label}
    key = 'a0o5tgod_m7ABgBnExQ4GjcWNQvvnJ82KpJreg3HD'
    deta = Deta(key)
    base = deta.Base("databasefortest")
    base.insert(data)

    st.success('提交成功')