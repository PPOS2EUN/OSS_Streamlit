import streamlit as st

print("hello")

# OSS 중간 시험 결과
OSS_Score = [80, 70, 55, 30, 3, 3, 1, 0]

st.write("# OSS 중간 시험 결과")
st.write("## 얘들아 공부 좀 하자 (나 빼고)")
st.write("### 집에도 일찍 가자")

OSS_Score

st.bar_chart(OSS_Score)