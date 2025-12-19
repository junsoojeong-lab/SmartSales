import streamlit as st

st.set_page_config(page_title="(주)싸이몬 스마트 세일즈", layout="wide")

# CSS: 사이드바 제거 및 테마 대응 디자인
st.markdown("""
    <style>
    /* 1. 사이드바 메뉴 완전히 숨기기 */
    [data-testid="stSidebar"], [data-testid="stSidebarNav"] { display: none !important; }
    
    /* 카드 디자인 */
    .module-card {
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(128, 128, 128, 0.2);
        min-height: 250px;
        margin-bottom: 10px;
        transition: transform 0.2s;
    }
    .module-card:hover { transform: translateY(-5px); }
    .card-title { color: #0077ff !important; font-size: 1.5rem; font-weight: bold; margin-bottom: 12px; display: block; }
    
    /* 버튼 스타일 */
    div[data-testid="stButton"] button[kind="primary"] {
        background-color: #004488 !important; color: white !important; border: none; height: 45px;
    }
    </style>
""", unsafe_allow_html=True)

# 헤더
st.markdown("""
    <div style="background-color: #004488 !important; padding: 25px; border-radius: 0 0 20px 20px; margin-bottom: 30px; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
        <h2 style="margin:0; display: flex; align-items: center; border: none !important;">
            <span style="color: #ffffff !important; font-size: 1.6rem !important; font-weight: 700 !important; text-decoration: none !important;">
                (주)싸이몬
            </span>
            <span style="margin: 0 15px; border-left: 2px solid #ffffff !important; height: 20px; opacity: 0.5;"></span>
            <span style="color: #ffffff !important; font-size: 1.1rem !important; font-weight: 400 !important; text-decoration: none !important;">
                Technical Sales Engineer Team
            </span>
        </h2>
    </div>
""", unsafe_allow_html=True)

st.title("💼 스마트 세일즈")
st.markdown("---")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
        <div class="module-card" style="border-left: 6px solid #2ea043;">
            <div style="font-size: 2.8rem; margin-bottom: 15px;">💰</div>
            <span class="card-title">ROI 계산기 (Investment)</span>
            <p>솔루션 도입에 따른 비용 절감액과 투자 회수 기간을 시뮬레이션합니다.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("ROI 분석 실행하기", key="go_roi", use_container_width=True, type="primary"):
        st.switch_page("pages/roi_v0.2.py")

with col2:
    st.markdown("""
        <div class="module-card">
            <div style="font-size: 2.8rem; margin-bottom: 15px;">🏆</div>
            <span class="card-title">성공 사례 (References)</span>
            <p>국내외 주요 산업군의 CIMON 솔루션 적용 사례와 핵심 성과를 확인합니다.</p>
        </div>
    """, unsafe_allow_html=True)
    st.button("준비 중", disabled=True, use_container_width=True)

col3, col4 = st.columns(2, gap="large")

with col3:
    st.markdown("""
        <div class="module-card">
            <div style="font-size: 2.8rem; margin-bottom: 15px;">⚙️</div>
            <span class="card-title">솔루션 아키텍처</span>
            <p>SCADA, PLC, HMI 기반의 통합 제어 시스템 아키텍처 가이드를 제공합니다.</p>
        </div>
    """, unsafe_allow_html=True)
    st.button("준비 중", key="c3", disabled=True, use_container_width=True)

with col4:
    st.markdown("""
        <div class="module-card">
            <div style="font-size: 2.8rem; margin-bottom: 15px;">📦</div>
            <span class="card-title">제품 라인업 요약</span>
            <p>CIMON 전 제품군의 사양 비교와 핵심 특장점을 한눈에 보여줍니다.</p>
        </div>
    """, unsafe_allow_html=True)
    st.button("준비 중", key="c4", disabled=True, use_container_width=True)