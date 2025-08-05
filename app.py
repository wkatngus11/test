import streamlit as st #as=알리어스
import pandas as pd
#import plotly.figure_factory as ff
#import plotly.express as px
#import matplotlib.pyplot as plt
#global var
url= "https://www.youtube.com/watch?v=XyEOEBsa8I4"

# data app
df = pd.read_csv('./data/data.csv')

st.set_page_config(layout='wide', page_title='My app')

#html variable
html = '''
<html>
    <head>
        <title> This HTML App </title>
    </head>
    <body>
        <h1> This Long Text!!!</h>
        <br>
        <hr>
        <h3> This a small text</h3>
    </body>
</html>
'''

with open('./blood_html.html','r',encoding='utf-8') as f:
    filehtml = f.read()
    f.close()


st.title('This is my world') #가장 위 제목
col1, col2 = st.columns((4,1)) #목록 생성(길이)
with col1:
    with st.expander('Content1'): #드롭다운 메뉴
        st.subheader('Content1')   #그 속 드롭다운 메뉴 하나 더
        st.video(url)
    with st.expander('Content2'): #드롭다운 메뉴
        st.subheader('Content2')   #그 속 드롭다운 메뉴 하나 더
        st.table(df)   #데이터 테이블 가져오기
        #dff = df.groupby(by='name').sum()
        #st.table(dff)
       # st.plotly_chart(df)
    with st.expander('Content3_image'):
        st.subheader('Content3_image')   
        st.image('./image/love.jpg')
        st.write('<h1> This is new title</h1>', unsafe_allow_html=True)
        st.markdown(html, unsafe_allow_html=True)
    with st.expander('Content4_htmlcontent'):
        st.subheader('Content4_htmlcontent')
        import streamlit.components.v1 as htmlviwer
        htmlviwer.html(filehtml, height=800)

with col2:
    with st.expander('Tips'):
        st.subheader('Tips')




