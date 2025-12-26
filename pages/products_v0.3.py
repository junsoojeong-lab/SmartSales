import streamlit as st

st.set_page_config(page_title="CIMON 제품 라인업", layout="wide")

# 디자인 일관성을 위한 CSS
st.markdown("""
    <style>
    /* 사이드바 완전히 제거 */
    [data-testid="stSidebar"], [data-testid="stSidebarNav"] { display: none !important; }
    
    /* 헤더 스타일 (Main/ROI 페이지와 동일) */
    .cimon-header-box {
        background-color: #004488 !important;
        padding: 25px !important;
        border-radius: 0 0 20px 20px !important;
        margin-bottom: 20px !important; /* 버튼과의 간격을 위해 약간 조정 */
        box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
    }
    .cimon-company-name { 
        color: #FFFFFF !important; 
        font-size: 1.6rem !important; 
        font-weight: 700 !important; 
        -webkit-text-fill-color: #FFFFFF !important;
    }
    .cimon-dept-name { 
        color: #FFFFFF !important; 
        font-size: 1.0rem !important; 
        font-weight: 400 !important; 
        opacity: 0.9 !important; 
        -webkit-text-fill-color: #FFFFFF !important;
    }
    .vertical-line { 
        margin: 0 15px; 
        border-left: 1px solid rgba(255, 255, 255, 0.4) !important; 
        height: 20px; 
    }
    
    .product-spec-card {
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(128, 128, 128, 0.3);
        background-color: rgba(128, 128, 128, 0.05);
        margin-bottom: 20px;
    }
    .spec-title { color: #0077ff !important; font-weight: bold; font-size: 1.2rem; margin-bottom: 10px; display: block; }
    </style>
""", unsafe_allow_html=True)

# 1. 헤더 (최상단 배치)
st.markdown("""
    <div class="cimon-header-box">
        <div style="display: flex; align-items: center; border: none !important;">
            <span class="cimon-company-name">(주)싸이몬</span>
            <div class="vertical-line"></div>
            <span class="cimon-dept-name">Technical Sales Engineer Team</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 2. 내비게이션 바 (헤더 바로 아래 배치)
top_c1, top_c2 = st.columns([8, 2])
with top_c2:
    if st.button("🏠 메인화면으로", use_container_width=True):
        st.switch_page("main_v0.3.py")

st.title("📦 제품 라인업 요약")
st.markdown("---")

# 3. 제품 탭 구성
tab1, tab2, tab3 = st.tabs(["PLC", "SCADA", "HMI/IPC"])

with tab1:
    st.subheader("CIMON PLC 시리즈")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class="product-spec-card"><span class="spec-title">CP Series</span><ul><li>고속 연산 (0.02us/step)</li><li>이중화 시스템 지원</li><li>최대 128,000점 제어</li></ul></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="product-spec-card"><span class="spec-title">XP Series</span><ul><li>소형 일체형 경제형 PLC</li><li>PID 및 위치결정 내장</li><li>스마트 공정 최적화</li></ul></div>""", unsafe_allow_html=True)

with tab2:
    st.subheader("CIMON SCADA V4.0")
    st.markdown("""
        <div class="product-spec-card">
            <span class="spec-title">국내 시장 점유율 1위 솔루션</span>
            <ul>
                <li>표준 통신 프로토콜(OPC, ODBC, MQTT) 완벽 대응</li>
                <li>Web/Mobile 원격 감시 모듈 제공</li>
                <li>무중단 운영을 위한 서버 이중화</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with tab3:
    st.subheader("HMI (Xpanel) & IPC")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class="product-spec-card"><span class="spec-title">Xpanel</span><ul><li>고해상도 TFT LCD</li><li>수천 종의 통신 드라이버</li><li>강력한 스크립트 엔진</li></ul></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="product-spec-card"><span class="spec-title">Industrial PC</span><ul><li>Fanless 산업용 내구성</li><li>다양한 사이즈 (10"~21")</li><li>커스텀 사양 대응 가능</li></ul></div>""", unsafe_allow_html=True)

st.markdown("---")

# 4. 하단 돌아가기 버튼
if st.button("◀ 메인 페이지로 돌아가기", key="bottom_back", use_container_width=True):
    st.switch_page("main_v0.3.py")
