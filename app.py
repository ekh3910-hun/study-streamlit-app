import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

APP_TITLE = os.getenv('APP_TITLE', '스터디 관리 앱')
APP_GREETING = os.getenv('APP_GREETING', '오늘도 화이팅!')

st.set_page_config(
    page_title=APP_TITLE,
    page_icon='📚'
)

st.title(APP_TITLE)
st.write(APP_GREETING)

if 'studies' not in st.session_state:
    st.session_state.studies = []

with st.form('study_form'):
    subject = st.text_input('공부할 주제')
    hours = st.number_input('공부 시간', min_value=1, max_value=24)
    submitted = st.form_submit_button('등록')

if submitted:
    if not subject.strip():
        st.warning('공부할 주제를 입력해주세요.')
    else:
        st.session_state.studies.append({
            '학습 주제': subject.strip(),
            '공부 시간': hours
        })
        st.success('등록되었습니다.')

st.subheader('나의 공부 목록')

if st.session_state.studies:
    df = pd.DataFrame(st.session_state.studies)
    st.dataframe(df, use_container_width=True)

    total = df['공부 시간'].sum()
    st.metric('총 공부 시간', f'{total}시간')
else:
    st.info('등록된 공부가 없습니다.')