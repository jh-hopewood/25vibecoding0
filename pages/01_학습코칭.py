import streamlit as st

# MBTI 유형별 간단한 특성 정의
type_descriptions = {
    "INTJ": "🧠 전략적 사고를 잘하며, 독립적인 사고를 선호하는 유형입니다.",
    "INTP": "💡 아이디어를 깊이 탐구하고 분석하는 것을 좋아하는 유형입니다.",
    "ENTJ": "🚀 목표를 명확히 설정하고 리더십을 발휘하는 유형입니다.",
    "ENTP": "🗣️ 호기심이 많고 새로운 아이디어를 즐기는 유형입니다.",
    "INFJ": "🔮 깊은 통찰력과 공감을 중요시하는 유형입니다.",
    "INFP": "🎨 창의적이고 감정에 민감한 유형입니다.",
    "ENFJ": "🌱 타인의 성장을 돕고 협력하는 것을 좋아하는 유형입니다.",
    "ENFP": "🔥 열정적이고 창의적인 성향을 가진 유형입니다.",
    "ISTJ": "🗂️ 체계적이고 현실적인 접근을 중시하는 유형입니다.",
    "ISFJ": "🛡️ 타인을 돕고 책임감을 중시하는 유형입니다.",
    "ESTJ": "📊 실용적이고 결과 지향적인 유형입니다.",
    "ESFJ": "🤝 타인과의 협력과 조화를 중시하는 유형입니다.",
    "ISTP": "🔧 논리적이며 실용적인 문제 해결을 선호하는 유형입니다.",
    "ISFP": "🌸 자유롭고 개방적인 성향을 가진 유형입니다.",
    "ESTP": "⚡ 즉각적인 결과와 행동을 중시하는 유형입니다.",
    "ESFP": "🎉 사교적이고 활발한 성향을 가진 유형입니다."
}

# MBTI 유형별 학습 방법 정의
learning_tips = {
    "INTJ": [
        ("📅 목표를 세우고 계획적으로 학습하기", "큰 그림을 그리고 장기적인 목표를 설정하세요. 예를 들어, 시험 점수보다 학기말 프로젝트나 대학 진학을 목표로 학습 계획을 세워보세요."),
        ("📝 논리적이고 구조화된 학습 자료 활용하기", "복잡한 개념을 명확히 정리하고 체계적인 자료를 활용하세요. 구조화된 노트와 요약을 추천합니다."),
        ("📊 분석적 사고를 바탕으로 복잡한 문제 해결하기", "데이터와 정보를 활용하여 문제를 깊이 분석하고 해결하는 연습을 하세요.")
    ],
    "INTP": [
        ("🔍 자유로운 탐구와 실험을 통한 학습", "새로운 아이디어와 이론을 자유롭게 탐구하세요. 실험과 가설을 세워보는 것도 좋습니다."),
        ("🗒️ 개념을 깊이 파고드는 독서와 토론", "단순한 지식 암기가 아닌 개념의 본질을 이해하는 데 집중하세요."),
        ("🛠️ 직접 문제를 해결하며 논리적 사고 연습", "복잡한 문제를 직접 풀어보며 논리적 사고를 키워보세요.")
    ]
}

# MBTI 유형별 주의할 점 정의
learning_cautions = {
    "INTJ": ["😅 지나치게 완벽을 추구하지 않기", "🤔 감정 표현에 소홀하지 않기", "📅 계획에 너무 얽매이지 않기"],
    "INTP": ["📝 과도한 분석에 빠지지 않기", "🤷 다른 사람의 의견을 무시하지 않기", "🔄 계획 없이 무작정 시작하지 않기"]
}

# 앱 제목 설정
st.title("MBTI 학습 코치")
st.write("자신의 MBTI를 선택하면 학습 스타일에 맞는 팁과 주의할 점을 알려드립니다.")

# MBTI 선택 드롭다운
selected_mbti = st.selectbox("자신의 MBTI 유형을 선택하세요:", list(type_descriptions.keys()))

# 선택한 MBTI 설명, 학습 팁, 주의할 점 출력
description = type_descriptions[selected_mbti]
learning_tips_list = learning_tips[selected_mbti]
learning_cautions_list = learning_cautions[selected_mbti]

st.header(f"{selected_mbti} 유형의 특성")
st.write(description)

st.header(f"{selected_mbti} 유형을 위한 학습 팁")
for title, detail in learning_tips_list:
    with st.expander(title):
        st.write(detail)

st.header(f"{selected_mbti} 유형의 학습 시 주의할 점")
for caution in learning_cautions_list:
    st.write(caution)
