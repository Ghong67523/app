import streamlit as st

OPENAI_API_KEY = st.secrets['API_KEY']

st.set_page_config(
    page_title="AI Career Finder",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------
# 1. 화면 제목
# --------------------------------

st.title("🚀 AI CAREER FINDER")
st.subheader("나의 가능성을 발견하는 맞춤형 진로 탐색 시스템")
st.write(
    "관심 분야, 선호 활동, 강점과 직업 가치관을 종합적으로 분석하여 "
    "나에게 어울리는 진로를 탐색합니다."
)

st.divider()

# --------------------------------
# 2. 사용자 입력
# --------------------------------

st.header("01. 나의 정보")

name = st.text_input("이름을 입력하세요.")

grade = st.selectbox(
    "현재 학년",
    ["고등학교 1학년", "고등학교 2학년", "고등학교 3학년"]
)

st.divider()

st.header("02. 관심 분야")

interests = st.multiselect(
    "관심 있는 분야를 선택하세요.",
    [
        "인공지능(AI)", "소프트웨어 개발", "정보보안",
        "로봇공학", "게임 개발", "데이터 분석",
        "생명과학", "경영·경제", "디자인", "환경·에너지"
    ]
)

st.header("03. 선호하는 활동")

activities = st.multiselect(
    "어떤 활동을 좋아하나요?",
    [
        "문제를 분석하고 해결하기",
        "새로운 프로그램 만들기",
        "데이터를 분석하기",
        "창의적인 아이디어 구상하기",
        "기계를 설계하고 제작하기",
        "사람들과 소통하고 협력하기",
        "연구하고 실험하기"
    ]
)

st.header("04. 나의 역량")

strengths = st.multiselect(
    "자신이 가지고 있다고 생각하는 강점은?",
    [
        "논리적 사고력", "창의력", "문제 해결 능력",
        "수학적 사고력", "의사소통 능력",
        "분석 능력", "끈기와 집중력"
    ]
)

st.header("05. 직업 선택 기준")

values = st.multiselect(
    "미래 직업에서 중요하게 생각하는 요소는?",
    [
        "높은 경제적 보상", "직업의 안정성",
        "사회적 기여", "자율적인 업무 환경",
        "지속적인 성장 가능성", "창의적인 업무"
    ]
)

st.divider()

# --------------------------------
# 3. 직업별 전문 분야 데이터
# --------------------------------

careers = [
    {
        "name": "AI 엔지니어",
        "description": "인공지능 모델을 설계하고 학습시켜 실제 서비스에 적용합니다.",
        "interests": ["인공지능(AI)", "소프트웨어 개발", "데이터 분석"],
        "activities": ["새로운 프로그램 만들기", "데이터를 분석하기", "문제를 분석하고 해결하기", "연구하고 실험하기"],
        "strengths": ["논리적 사고력", "수학적 사고력", "분석 능력", "문제 해결 능력"],
        "values": ["높은 경제적 보상", "지속적인 성장 가능성", "창의적인 업무"],
        "majors": "인공지능학과, 소프트웨어융합학과, 데이터사이언스학과",
        "skills": "Python, 수학, 알고리즘, 머신러닝, 데이터 분석",
        "roadmap": [
            "Python과 수학 기초 학습하기",
            "데이터 분석 프로젝트 진행하기",
            "간단한 인공지능 모델 제작하기",
            "대학에서 머신러닝과 AI 기술 심화하기"
        ]
    },
    {
        "name": "소프트웨어 개발자",
        "description": "웹사이트, 앱, 프로그램 등 사용자의 문제를 해결하는 소프트웨어를 개발합니다.",
        "interests": ["소프트웨어 개발", "인공지능(AI)", "게임 개발"],
        "activities": ["새로운 프로그램 만들기", "문제를 분석하고 해결하기"],
        "strengths": ["논리적 사고력", "창의력", "문제 해결 능력", "끈기와 집중력"],
        "values": ["높은 경제적 보상", "직업의 안정성", "자율적인 업무 환경", "지속적인 성장 가능성"],
        "majors": "소프트웨어융합학과, 응용소프트웨어학과, 소프트웨어학과",
        "skills": "Python, Java, JavaScript, 자료구조, 알고리즘",
        "roadmap": [
            "Python 또는 JavaScript 기초 학습하기",
            "웹사이트나 간단한 프로그램 제작하기",
            "프로젝트 결과물을 포트폴리오로 정리하기",
            "대학에서 소프트웨어 설계와 개발 심화하기"
        ]
    },
    {
        "name": "정보보안 전문가",
        "description": "컴퓨터 시스템과 네트워크의 보안 문제를 분석하고 정보 유출과 사이버 위협을 예방합니다.",
        "interests": ["정보보안", "소프트웨어 개발", "인공지능(AI)"],
        "activities": ["문제를 분석하고 해결하기", "데이터를 분석하기", "연구하고 실험하기"],
        "strengths": ["논리적 사고력", "문제 해결 능력", "분석 능력", "끈기와 집중력"],
        "values": ["직업의 안정성", "사회적 기여", "지속적인 성장 가능성"],
        "majors": "정보보호학과, 사이버보안학과, 소프트웨어융합학과",
        "skills": "네트워크, 운영체제, Python, 보안 기초",
        "roadmap": [
            "컴퓨터와 네트워크의 기본 원리 학습하기",
            "Python 프로그래밍 연습하기",
            "정보보안의 기본 개념과 윤리 이해하기",
            "대학에서 시스템 및 네트워크 보안 심화하기"
        ]
    },
    {
        "name": "로봇 소프트웨어 개발자",
        "description": "로봇이 주변 환경을 인식하고 스스로 움직이도록 제어하는 소프트웨어를 개발합니다.",
        "interests": ["로봇공학", "인공지능(AI)", "소프트웨어 개발"],
        "activities": ["새로운 프로그램 만들기", "기계를 설계하고 제작하기", "연구하고 실험하기"],
        "strengths": ["논리적 사고력", "수학적 사고력", "창의력", "문제 해결 능력"],
        "values": ["높은 경제적 보상", "지속적인 성장 가능성", "창의적인 업무"],
        "majors": "로봇공학과, 지능형로봇학과, 소프트웨어융합학과",
        "skills": "Python, C++, 센서, 알고리즘, 로봇 제어",
        "roadmap": [
            "Python과 수학 기초 학습하기",
            "센서와 로봇의 작동 원리 이해하기",
            "간단한 로봇 제어 프로젝트 제작하기",
            "대학에서 로봇 소프트웨어와 인공지능 심화하기"
        ]
    },
    {
        "name": "임베디드 소프트웨어 개발자",
        "description": "자동차, 가전제품, 로봇 등의 기기 안에서 작동하는 소프트웨어를 개발합니다.",
        "interests": ["소프트웨어 개발", "로봇공학", "인공지능(AI)"],
        "activities": ["새로운 프로그램 만들기", "기계를 설계하고 제작하기", "문제를 분석하고 해결하기"],
        "strengths": ["논리적 사고력", "수학적 사고력", "문제 해결 능력", "끈기와 집중력"],
        "values": ["직업의 안정성", "높은 경제적 보상", "지속적인 성장 가능성"],
        "majors": "전자공학과, 임베디드시스템학과, 소프트웨어융합학과",
        "skills": "C, C++, 마이크로컨트롤러, 운영체제, 회로 기초",
        "roadmap": [
            "프로그래밍 기초 학습하기",
            "전자기기와 센서의 작동 원리 이해하기",
            "간단한 기기 제어 프로젝트 진행하기",
            "대학에서 임베디드 시스템과 제어 기술 심화하기"
        ]
    },
    {
        "name": "데이터 분석가",
        "description": "다양한 데이터를 수집하고 분석하여 의미 있는 정보와 의사결정 근거를 찾습니다.",
        "interests": ["데이터 분석", "인공지능(AI)", "경영·경제"],
        "activities": ["데이터를 분석하기", "문제를 분석하고 해결하기"],
        "strengths": ["분석 능력", "수학적 사고력", "논리적 사고력"],
        "values": ["높은 경제적 보상", "직업의 안정성", "지속적인 성장 가능성"],
        "majors": "데이터사이언스학과, 통계학과, 소프트웨어융합학과",
        "skills": "Python, SQL, 통계, 데이터 시각화",
        "roadmap": [
            "기초 통계와 수학 학습하기",
            "Python으로 데이터 분석 연습하기",
            "실제 데이터를 활용한 분석 프로젝트 진행하기",
            "대학에서 통계와 데이터 처리 기술 심화하기"
        ]
    },
    {
        "name": "생물정보학 전문가",
        "description": "생명과학 연구에서 발생하는 유전자와 생물학적 데이터를 컴퓨터 기술로 분석합니다.",
        "interests": ["생명과학", "데이터 분석", "인공지능(AI)", "소프트웨어 개발"],
        "activities": ["데이터를 분석하기", "연구하고 실험하기", "문제를 분석하고 해결하기"],
        "strengths": ["분석 능력", "수학적 사고력", "논리적 사고력", "끈기와 집중력"],
        "values": ["사회적 기여", "지속적인 성장 가능성", "높은 경제적 보상"],
        "majors": "생명정보학과, 생명과학과, 바이오융합학과, 데이터사이언스학과",
        "skills": "Python, 통계, 생명과학 기초, 유전체 데이터 분석",
        "roadmap": [
            "생명과학과 유전의 기본 개념 학습하기",
            "Python과 데이터 분석 기초 익히기",
            "생물학 관련 데이터를 활용한 분석 탐구하기",
            "대학에서 생명정보학과 데이터 분석 심화하기"
        ]
    },
    {
        "name": "생명공학 연구원",
        "description": "생물의 특성을 연구하고 이를 의약품, 식품, 바이오 기술 등에 활용하는 연구를 수행합니다.",
        "interests": ["생명과학"],
        "activities": ["연구하고 실험하기", "문제를 분석하고 해결하기"],
        "strengths": ["분석 능력", "끈기와 집중력", "논리적 사고력"],
        "values": ["사회적 기여", "지속적인 성장 가능성"],
        "majors": "생명공학과, 생명과학과, 바이오시스템공학과",
        "skills": "생물학, 화학, 실험 설계, 데이터 해석",
        "roadmap": [
            "생명과학과 화학 기초 학습하기",
            "생명과학 실험과 탐구 활동 경험하기",
            "바이오 기술과 연구 분야 조사하기",
            "대학에서 생명공학 및 실험 연구 심화하기"
        ]
    },
    {
        "name": "환경 데이터 분석 전문가",
        "description": "기후, 대기, 수질 등의 환경 데이터를 분석하여 환경 변화와 문제 해결 방안을 연구합니다.",
        "interests": ["환경·에너지", "데이터 분석", "인공지능(AI)"],
        "activities": ["데이터를 분석하기", "연구하고 실험하기", "문제를 분석하고 해결하기"],
        "strengths": ["분석 능력", "논리적 사고력", "문제 해결 능력"],
        "values": ["사회적 기여", "지속적인 성장 가능성"],
        "majors": "환경공학과, 환경과학과, 데이터사이언스학과",
        "skills": "Python, 통계, 환경과학, 데이터 시각화",
        "roadmap": [
            "기후와 환경 문제의 원인 조사하기",
            "환경 관련 공공 데이터 찾아보기",
            "데이터를 분석하고 그래프로 표현하기",
            "대학에서 환경과 데이터 분석 기술 심화하기"
        ]
    },
    {
        "name": "게임 개발자",
        "description": "게임의 규칙과 기능을 설계하고 실제로 작동하는 게임 프로그램을 제작합니다.",
        "interests": ["게임 개발", "소프트웨어 개발", "디자인"],
        "activities": ["새로운 프로그램 만들기", "창의적인 아이디어 구상하기"],
        "strengths": ["창의력", "논리적 사고력", "끈기와 집중력"],
        "values": ["자율적인 업무 환경", "창의적인 업무", "지속적인 성장 가능성"],
        "majors": "게임공학과, 게임소프트웨어학과, 소프트웨어융합학과",
        "skills": "C#, C++, 게임 엔진, 알고리즘",
        "roadmap": [
            "프로그래밍 기초 학습하기",
            "게임 엔진의 기본 기능 익히기",
            "간단한 게임 직접 제작하기",
            "대학에서 게임 프로그래밍과 설계 심화하기"
        ]
    },
    {
        "name": "UX/UI 디자이너",
        "description": "사용자가 웹사이트와 앱을 편리하게 이용할 수 있도록 화면과 사용 경험을 설계합니다.",
        "interests": ["디자인", "소프트웨어 개발"],
        "activities": ["창의적인 아이디어 구상하기", "사람들과 소통하고 협력하기"],
        "strengths": ["창의력", "의사소통 능력", "문제 해결 능력"],
        "values": ["창의적인 업무", "자율적인 업무 환경", "사회적 기여"],
        "majors": "디지털디자인학과, 산업디자인학과, 시각디자인학과",
        "skills": "UI 설계, 사용자 조사, 디자인 도구, 프로토타이핑",
        "roadmap": [
            "좋은 앱과 웹사이트의 디자인 분석하기",
            "사용자 입장에서 불편한 점 찾아보기",
            "간단한 앱 화면과 웹 화면 설계하기",
            "대학에서 사용자 경험과 인터페이스 디자인 심화하기"
        ]
    },
    {
        "name": "금융 데이터 분석가",
        "description": "금융과 경제 데이터를 분석하여 시장 흐름과 기업의 의사결정에 필요한 정보를 제공합니다.",
        "interests": ["경영·경제", "데이터 분석", "인공지능(AI)"],
        "activities": ["데이터를 분석하기", "문제를 분석하고 해결하기"],
        "strengths": ["수학적 사고력", "분석 능력", "논리적 사고력"],
        "values": ["높은 경제적 보상", "직업의 안정성", "지속적인 성장 가능성"],
        "majors": "경제학과, 금융공학과, 통계학과, 데이터사이언스학과",
        "skills": "통계, Python, 금융 기초, 데이터 분석",
        "roadmap": [
            "경제와 금융의 기본 개념 학습하기",
            "기초 통계와 데이터 분석 연습하기",
            "경제 데이터를 활용한 분석 프로젝트 진행하기",
            "대학에서 금융과 데이터 분석 지식 심화하기"
        ]
    },
    {
        "name": "클라우드 엔지니어",
        "description": "기업의 서버와 데이터를 클라우드 환경에서 안정적으로 운영하고 관리하는 기술을 개발합니다.",
        "interests": ["소프트웨어 개발", "정보보안", "데이터 분석"],
        "activities": ["문제를 분석하고 해결하기", "새로운 프로그램 만들기", "연구하고 실험하기"],
        "strengths": ["논리적 사고력", "문제 해결 능력", "끈기와 집중력"],
        "values": ["직업의 안정성", "높은 경제적 보상", "지속적인 성장 가능성"],
        "majors": "소프트웨어학과, 컴퓨터공학과, 정보보호학과",
        "skills": "네트워크, Linux, 서버, 클라우드 기초, Python",
        "roadmap": [
            "컴퓨터와 네트워크 기초 학습하기",
            "운영체제와 서버의 기본 원리 이해하기",
            "간단한 웹 서비스 운영 경험하기",
            "대학에서 클라우드와 시스템 운영 기술 심화하기"
        ]
    }
]

# --------------------------------
# 4. 점수 계산 알고리즘
# --------------------------------

WEIGHTS = {
    "interests": 45,
    "activities": 25,
    "strengths": 20,
    "values": 10
}


def calculate_score(user_data, career):
    total_score = 0
    used_weight = 0
    matched = {}

    for category, weight in WEIGHTS.items():
        selected = user_data[category]
        targets = career[category]

        # 선택하지 않은 분야는 점수 계산에서 제외
        if not selected:
            continue

        matches = sorted(set(selected) & set(targets))
        match_ratio = len(matches) / len(selected)

        total_score += match_ratio * weight
        used_weight += weight

        matched[category] = matches

    if used_weight == 0:
        return 0, matched

    final_score = round(total_score / used_weight * 100)

    return final_score, matched


# --------------------------------
# 5. 분석 실행
# --------------------------------

if st.button("🔍 나의 진로 분석하기", use_container_width=True):

    if not name.strip():
        st.warning("이름을 입력해 주세요.")

    elif not interests or not activities or not strengths:
        st.warning("관심 분야, 선호 활동, 강점을 모두 선택해 주세요.")

    else:
        user_data = {
            "interests": interests,
            "activities": activities,
            "strengths": strengths,
            "values": values
        }

        results = []

        for career in careers:
            score, matched = calculate_score(user_data, career)

            results.append({
                "name": career["name"],
                "score": score,
                "matched": matched,
                "info": career
            })

        results.sort(
            key=lambda result: result["score"],
            reverse=True
        )

        st.session_state["results"] = results[:3]
        st.session_state["user_name"] = name
        st.session_state["grade"] = grade
        st.session_state["user_data"] = user_data


# --------------------------------
# 6. 개인별 분석 보고서
# --------------------------------

if "results" in st.session_state:

    results = st.session_state["results"]

    st.divider()
    st.header(f"📊 {st.session_state['user_name']}님의 진로 분석 보고서")

    st.write(f"분석 대상: {st.session_state['grade']}")

    st.info(
        "관심 분야, 선호 활동, 강점, 직업 가치관을 "
        "직업별 특성과 비교하여 연관 점수를 계산했습니다."
    )

    # 성향 분석
    user_data = st.session_state["user_data"]

    st.subheader("1. 나의 진로 성향")

    st.write(
        f"관심 분야: {', '.join(user_data['interests'])}"
    )
    st.write(
        f"선호 활동: {', '.join(user_data['activities'])}"
    )
    st.write(
        f"강점: {', '.join(user_data['strengths'])}"
    )

    if user_data["values"]:
        st.write(
            f"직업 선택 기준: {', '.join(user_data['values'])}"
        )

    # TOP 3 추천
    st.subheader("2. 추천 진로 TOP 3")

    for i, result in enumerate(results):

        info = result["info"]
        matched = result["matched"]

        with st.expander(
            f"{i + 1}위. {result['name']} - 연관 점수 {result['score']}점",
            expanded=(i == 0)
        ):
            st.progress(result["score"] / 100)

            st.write(info["description"])

            st.markdown("**추천된 이유**")

            labels = {
                "interests": "관심 분야",
                "activities": "선호 활동",
                "strengths": "강점",
                "values": "직업 선택 기준"
            }

            has_reason = False

            for category, label in labels.items():
                if matched.get(category):
                    st.write(
                        f"- {label}: {', '.join(matched[category])}"
                    )
                    has_reason = True

            if not has_reason:
                st.write("선택한 항목과 직접 일치하는 특성이 적습니다.")

            st.write(f"**관련 학과:** {info['majors']}")
            st.write(f"**필요 역량:** {info['skills']}")

    # 점수 비교
    st.subheader("3. 진로별 연관 점수 비교")

    chart_data = {
        "진로": [r["name"] for r in results],
        "연관 점수": [r["score"] for r in results]
    }

    st.bar_chart(
        chart_data,
        x="진로",
        y="연관 점수"
    )

    # 1순위 직업 상세 분석
    best = results[0]
    best_info = best["info"]

    st.subheader("4. 가장 추천하는 진로")

    st.markdown(f"### 🎯 {best['name']}")

    st.write(best_info["description"])

    st.write(f"**관련 학과:** {best_info['majors']}")
    st.write(f"**핵심 역량:** {best_info['skills']}")

    # 개인별 조언
    st.subheader("5. 개인별 진로 조언")

    matched_interests = best["matched"].get("interests", [])
    matched_activities = best["matched"].get("activities", [])
    matched_strengths = best["matched"].get("strengths", [])

    if matched_interests:
        st.write(
            f"관심 분야 중 {', '.join(matched_interests)}이(가) "
            f"{best['name']} 분야와 연결됩니다."
        )

    if matched_activities:
        st.write(
            f"특히 {', '.join(matched_activities)} 활동을 선호한다는 점에서 "
            "관련 분야의 프로젝트를 직접 경험해 보는 것이 좋습니다."
        )

    if matched_strengths:
        st.write(
            f"선택한 강점인 {', '.join(matched_strengths)}을(를) "
            "관련 학습과 프로젝트에서 발전시켜 보세요."
        )

    st.write(
        "현재 결과만으로 진로를 확정하기보다는 실제 직업의 업무와 "
        "대학 교육과정을 조사하고, 관련 프로젝트를 경험하면서 "
        "자신에게 맞는 분야인지 확인하는 것이 중요합니다."
    )

    # 성장 로드맵
    st.subheader("6. 나만의 성장 로드맵")

    roadmap = best_info["roadmap"]

    for i, step in enumerate(roadmap, start=1):
        st.write(f"**STEP {i}.** {step}")

    st.success("개인별 진로 분석 보고서가 완성되었습니다!")

    st.caption(
        "※ 연관 점수는 입력한 선택 항목과 직업별 특성의 일치 정도를 나타냅니다. "
        "실제 적성, 성적, 취업 가능성을 측정하거나 보장하는 수치는 아닙니다."
    )

    if st.button("🔄 다른 조건으로 다시 분석하기"):
        del st.session_state["results"]
        del st.session_state["user_name"]
        del st.session_state["grade"]
        del st.session_state["user_data"]
        st.rerun()