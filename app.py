import streamlit as st

# =========================
# 페이지 설정
# =========================
st.set_page_config(
    page_title="FindYU",
    page_icon="🔎",
    layout="wide"
)

# =========================
# FindYU 디자인
# =========================
st.markdown("""
<style>

/* 전체 폭 */
.block-container {
    max-width: 1150px;
    padding-top: 2rem;
}

/* FindYU 제목 */
.findyu-title {
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 0px;
}

.findyu-title span {
    color: #4F7FFF;
}

/* 부제목 */
.findyu-subtitle {
    color: #777;
    font-size: 18px;
    margin-bottom: 30px;
}

/* 카드 */
.info-card {
    background-color: #F7F9FC;
    border: 1px solid #E6E9EF;
    border-radius: 15px;
    padding: 22px;
    margin-bottom: 15px;
}

/* MATCH 점수 */
.match-score {
    text-align: center;
    padding: 25px;
    background-color: #F7F9FC;
    border-radius: 18px;
}

.score-number {
    font-size: 55px;
    font-weight: 800;
    color: #4F7FFF;
}

.score-text {
    color: #777;
}

</style>
""", unsafe_allow_html=True)


# =========================
# 상단 로고
# =========================
st.markdown("""
<div class="findyu-title">
    🔎 Find<span>YU</span>
</div>

<div class="findyu-subtitle">
    AI 기반 영남대학교 분실물 · 습득물 자동 매칭 서비스
</div>
""", unsafe_allow_html=True)


# =========================
# 메뉴
# =========================
tab1, tab2 = st.tabs([
    "🔍 Match 결과",
    "📊 서비스 통계"
])


# =================================================
# Match Dashboard
# =================================================
with tab1:

    st.subheader("내 분실물과 습득물 비교")

    st.caption(
        "AI가 이미지, 텍스트, 장소와 시간 정보를 분석하여 "
        "가장 유사한 습득물을 비교합니다."
    )

    st.divider()

    # 사진
    left, right = st.columns(2)

    with left:

        st.markdown("### 🔍 내가 잃어버린 물건")

        lost_image = st.file_uploader(
            "분실물 사진 선택",
            type=["jpg", "jpeg", "png"],
            key="lost"
        )

        if lost_image:
            st.image(
                lost_image,
                use_container_width=True
            )
        else:
            st.info("분실물 사진을 등록해주세요.")


    with right:

        st.markdown("### 📦 추천 습득물")

        found_image = st.file_uploader(
            "습득물 사진 선택",
            type=["jpg", "jpeg", "png"],
            key="found"
        )

        if found_image:
            st.image(
                found_image,
                use_container_width=True
            )
        else:
            st.info("테스트할 습득물 사진을 등록해주세요.")


    st.divider()


    # =========================
    # Demo Match 결과
    # =========================

    matching_score = 87
    image_score = 92
    text_score = 85
    location_score = 80
    time_score = 91


    col_score, col_info = st.columns([1, 2])


    with col_score:

        st.markdown(f"""
        <div class="match-score">

            <div class="score-text">
                MATCH SCORE
            </div>

            <div class="score-number">
                {matching_score}%
            </div>

            <div>
                높은 매칭 가능성
            </div>

        </div>
        """, unsafe_allow_html=True)


    with col_info:

        st.markdown("### AI 매칭 분석")

        st.write(
            f"🖼️ 이미지 유사도  **{image_score}%**"
        )
        st.progress(image_score / 100)

        st.write(
            f"📝 텍스트 유사도  **{text_score}%**"
        )
        st.progress(text_score / 100)

        st.write(
            f"📍 위치 적합도  **{location_score}%**"
        )
        st.progress(location_score / 100)

        st.write(
            f"🕒 시간 적합도  **{time_score}%**"
        )
        st.progress(time_score / 100)


    st.divider()


    # =========================
    # 습득 정보
    # =========================

    st.subheader("📦 습득 정보")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "습득 장소",
            "IT관 1층"
        )

    with c2:
        st.metric(
            "습득 날짜",
            "2026.10.04"
        )

    with c3:
        st.metric(
            "매칭 순위",
            "TOP 1"
        )


    st.divider()


    # 추천 이유
    st.subheader("🤖 AI 추천 이유")

    st.success(
        "분실물과 습득물의 색상 및 외형적 특징이 매우 유사합니다. "
        "또한 분실 위치와 습득 위치가 가까우며 "
        "시간 조건도 높은 수준으로 일치합니다."
    )

    st.caption(
        "※ 현재 표시된 Matching Score는 Dashboard 개발용 테스트 데이터입니다."
    )


# =================================================
# 관리자 / 서비스 통계
# =================================================
with tab2:

    st.subheader("📊 FindYU 서비스 통계")

    st.caption(
        "AI 검색 및 매칭 시스템의 성능을 확인합니다."
    )

    st.divider()

    a, b, c, d = st.columns(4)

    with a:
        st.metric(
            "Top-1",
            "72%"
        )

    with b:
        st.metric(
            "Top-5",
            "84%"
        )

    with c:
        st.metric(
            "Top-10",
            "93%"
        )

    with d:
        st.metric(
            "평균 검색시간",
            "1.8초"
        )

    st.divider()

    st.subheader("검색 성능")

    st.write("Image-only")
    st.progress(0.72)

    st.write("Text-only")
    st.progress(0.68)

    st.write("Multimodal")
    st.progress(0.84)

    st.info(
        "현재 표시되는 통계는 Dashboard 화면 개발을 위한 예시 데이터입니다."
    )