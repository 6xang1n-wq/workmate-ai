import streamlit as st

st.set_page_config(page_title="WorkMate AI", page_icon="💼")

st.title("💼 WorkMate AI")
st.subheader("직장인을 위한 하루 업무 정리 및 성장 도우미")

st.write(
    "오늘의 업무와 상태를 입력하면 하루를 정리하고, "
    "내일 해야 할 일을 추천해주는 AI Agent입니다."
)

work_log = st.text_area(
    "오늘 어떤 일을 했나요?",
    placeholder="예: 회의 2개 참석, 보고서 초안 작성, 고객사 메일 답변 못 함"
)

mood = st.selectbox(
    "오늘의 상태는 어땠나요?",
    ["좋음", "보통", "피곤함", "스트레스 많음", "집중 잘 됨"]
)

if st.button("AI 분석하기"):
    if work_log.strip() == "":
        st.warning("오늘의 업무 내용을 입력해주세요.")
    else:
        st.markdown("## 📌 오늘의 업무 요약")
        st.write(work_log)

        st.markdown("## 😊 현재 상태 분석")
        st.write(f"오늘의 상태는 **{mood}**으로 기록되었습니다.")

        st.markdown("## 👍 잘한 점")
        st.write("- 오늘의 업무를 기록하며 하루를 돌아본 점이 좋습니다.")
        st.write("- 완료한 일과 미완료한 일을 구분하려는 태도가 업무 성장에 도움이 됩니다.")

        st.markdown("## 🔧 개선할 점")
        st.write("- 미완료 업무가 있다면 내일 가장 먼저 처리하는 것이 좋습니다.")
        st.write("- 업무를 크게 잡기보다 작은 단위로 나누면 실행 가능성이 높아집니다.")

        st.markdown("## ✅ 내일 추천 할 일")
        st.write("1. 오늘 미완료한 업무 먼저 처리하기")
        st.write("2. 회의나 업무 내용을 5분 안에 간단히 정리하기")
        st.write("3. 내일 가장 중요한 업무 1개를 정해서 먼저 시작하기")
