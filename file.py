import streamlit as st

# 웹 페이지 제목
st.title("나의 Streamlit 웹 어플리케이션")

# 사이드바에 설명 추가
st.sidebar.header("사이드바")
st.sidebar.text("여기서 설정을 변경할 수 있습니다.")

# 사용자 입력을 위한 텍스트 박스
user_input = st.text_input("텍스트 입력:", "기본 텍스트")

# 버튼 클릭 시 입력된 텍스트 표시
if st.button("제출"):
    st.write("입력한 텍스트:", user_input)

# 간단한 차트 추가
st.subheader("차트 예시")
data = [1, 2, 3, 4, 5]
st.line_chart(data)

# 페이징 및 이미지 업로드 기능 추가
uploaded_file = st.file_uploader("이미지 업로드", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    st.image(uploaded_file, caption="업로드한 이미지", use_column_width=True)

# 유용한 링크 추가
st.sidebar.subheader("링크")
st.sidebar.markdown("[Streamlit Documentation](https://docs.streamlit.io/)")

# 하단에 크레딧 추가
st.write("제작자: 당신의 이름")
