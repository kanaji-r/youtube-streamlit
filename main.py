import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i+1)
  time.sleep(0.05)

'Done!!!!!!!'

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右カラムです')

option = st.selectbox(
  'あなたが好きな数字を教えてください。',
  list(range(1,11))
)
text = st.text_input(
  'テキストを入力してください',
)
condition = st.slider('調子どう？',0,100,50)

'あなたの好きな数字は',option,'です'
'入力：',text,

'コンディション',condition

expander = st.expander('問い合わせ1')
expander.write('問い合わせ1回答')
expander = st.expander('問い合わせ2')
expander.write('問い合わせ2回答')
expander = st.expander('問い合わせ3')
expander.write('問い合わせ3回答')
# if st.checkbox('Show Image'):
#   img = Image.open('sample01.jpg')
#   st.image(img,caption='kanaji',use_column_width=True)
