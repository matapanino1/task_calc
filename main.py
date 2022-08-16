import streamlit as st
import datetime

st.title("タスクペース計算")

i_d = datetime.date.today()

f_d = st.date_input(
    "完了目標日：",
    i_d
)

page_num = st.number_input('残りページ(問題)数を入力してください：', value=0)
week_pace = st.number_input('１週間のうち勉強する日数：', min_value=1, max_value=7, value=5)
s_d = f_d - i_d

try:
    task_day = page_num / (week_pace*(s_d.days / 7))
    task_week = page_num / (s_d.days / 7)
    st.metric(label=f'週{week_pace}日勉強する時の1日あたりのページ(問題)数：', value=f'{int(task_day)}ページ/日')
    st.metric(label="1週間：", value=f'{int(task_week)}ページ/週')
except ZeroDivisionError:
    st.write("")