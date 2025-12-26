import streamlit as st

st.set_page_config(page_title="CIMON 제품 라인업", layout="wide")

# 디자인 일관성을 위한 CSS
st.markdown("""
    <style>
    [data-testid="stSidebar"], [data-testid="stSidebarNav"] { display: none !important; }
    
    .cimon-header-box {
        background-color: #004488 !important;
        padding: 25px !important;
        border-radius: 0 0 20px 20px !important;
        margin-bottom: 30px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
    }
    .cimon-company-name { color: #FFFFFF !important; font-size: 1.6rem !important; font-weight: 700 !important; }
    .cimon-dept-name { color: #FFFFFF !important; font-size: 1.0rem !important; font-weight: 400 !important; opacity: 0.9 !important; }
    .vertical-line { margin: 0 15px; border-left: 1px solid rgba(255, 255, 255, 0.4) !important; height: 20px; }
    
    .product-spec-card {
        padding: 20px;
        border-radius: 10px;
        border: 1px solid rgba(128, 128, 128, 0.2);
        background-color: rgba(128, 128, 128, 0.05);
        margin-bottom: 20px;
    }
    .spec-title { color: #0077ff; font-weight: bold; font-size: 1.2rem; margin-bottom: 10px; display: block; }
    </style>
""", unsafe_allow_html=True)

# 헤더 (메인과 동일)
st.markdown("""
    <div class="cimon-header-box">
        <div style="display: flex; align-items: center; border: none !important;">
            <span class="cimon-company-name">(주)싸이몬</span>
            <div class="vertical-line"></div>
            <span class="cimon-dept-name">Technical Sales Engineer Team</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 상단 내비게이션
if st.button("🏠 메인화면으로 돌아가기", use_container_width=True):
    st.switch_page("main_v0.2.py")

st.title("📦 제품 라인업 요약")
st.write("CIMON의 핵심 솔루션 라인업 사양입니다.")
st.markdown("---")

tab1, tab2, tab3 = st.tabs(["PLC", "SCADA", "HMI/IPC"])

with tab1:
    st.subheader("PLC (Programmable Logic Controller)")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
            <div class="product-spec-card">
                <span class="spec-title">CP Series (High Performance)</span>
                <ul>
                    <li>고속 연산 처리 (0.02us/step)</li>
                    <li>최대 128,000점 입출력 제어</li>
                    <li>Ethernet, Serial 내장 포트 제공</li>
                    <li>이중화 시스템 완벽 지원</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
            <div class="product-spec-card">
                <span class="spec-title">XP Series (Compact)</span>
                <ul>
                    <li>경제적인 소형 일체형 PLC</li>
                    <li>PID 제어 및 위치결정 모듈 내장</li>
                    <li>스마트 팩토리 기초 공정 최적화</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

with tab2:
    st.subheader("CIMON SCADA")
    st.info("💡 싸이몬 스카다는 국내 시장 점유율 1위의 통합 관제 소프트웨어입니다.")
    st.markdown("""
        <div class="product-spec-card">
            <span class="spec-title">핵심 특장점</span>
            <table style="width:100%; border-collapse: collapse;">
                <tr style="border-bottom: 1px solid #ddd;"> <td style="padding:10px;"><b>개방성</b></td> <td>표준 통신 프로토콜(OPC, ODBC 등) 완벽 대응</td> </tr>
                <tr style="border-bottom: 1px solid #ddd;"> <td style="padding:10px;"><b>확장성</b></td> <td>Web/Mobile 원격 감시 및 제어 지원</td> </tr>
                <tr style="border-bottom: 1px solid #ddd;"> <td style="padding:10px;"><b>안정성</b></td> <td>서버 이중화 기능을 통한 무중단 운영</td> </tr>
            </table>
        </div>
    """, unsafe_allow_html=True)

with tab3:
    st.subheader("HMI & Industrial PC")
    col_a, col_b = st.columns(2)
    with col_a:
        st.image("https://via.placeholder.com/400x250.png?text=CIMON+Xpanel", caption="Xpanel Series")
    with col_b:
        st.markdown("""
            **Xpanel (HMI)**
            - 고해상도 TFT LCD 채용
            - 다양한 드라이버 제공 (수천종의 장비 연결)
            - 강력한 스크립트 기능 지원
            
            **Industrial PC**
            - Fanless 저전력 고성능 설계
            - 열악한 산업 환경을 고려한 내구성
            - 10" ~ 21" 다양한 라인업
        """)