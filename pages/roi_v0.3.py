import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="CIMON ROI 분석기", layout="wide")

# CSS: 디자인 일관성 및 헤더 스타일 적용
st.markdown("""
    <style>
    /* 사이드바 완전히 제거 */
    [data-testid="stSidebar"], [data-testid="stSidebarNav"] { display: none !important; }
    
    input { color: inherit !important; -webkit-text-fill-color: inherit !important; }
    label p { color: #0077ff !important; font-weight: bold !important; }
    
    /* 헤더 스타일 (Main 페이지와 동일) */
    .cimon-header-box {
        background-color: #004488 !important;
        padding: 25px !important;
        border-radius: 0 0 20px 20px !important;
        margin-bottom: 30px !important;
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

    .result-section { 
        padding: 25px; border-radius: 12px; 
        border: 1px solid rgba(128, 128, 128, 0.3);
        background-color: rgba(128, 128, 128, 0.05);
    }
    .saving-item { 
        border-bottom: 1px solid rgba(128, 128, 128, 0.2); 
        padding: 12px 0; display: flex; justify-content: space-between;
    }
    .val-text { color: #2ea043 !important; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 헤더 추가 (메인과 동일한 디자인)
st.markdown("""
    <div class="cimon-header-box">
        <div style="display: flex; align-items: center; border: none !important;">
            <span class="cimon-company-name">(주)싸이몬</span>
            <div class="vertical-line"></div>
            <span class="cimon-dept-name">Technical Sales Engineer Team</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 상단 내비게이션 바
top_c1, top_c2 = st.columns([8, 2])
with top_c2:
    if st.button("🏠 메인화면으로", use_container_width=True):
        st.switch_page("main_v0.3.py")

st.title("💰 ROI(투자 회수) 분석 시뮬레이터")
st.markdown("---")

# 입력창/결과창 2열 배치
left, right = st.columns([1, 1.2], gap="large")

with left:
    st.subheader("📋 입력 파라미터")
    faults = st.slider("연간 돌발 고장 횟수 (회)", 0, 50, 5)
    
    # 억/만 입력 함수
    def cimon_input(label, default_uk=0, default_man=0, key=""):
        st.markdown(f"**{label}**")
        c1, c2 = st.columns(2)
        with c1: uk = st.number_input("억", min_value=0, value=default_uk, key=f"{key}_u")
        with c2: man = st.number_input("만", min_value=0, value=default_man, key=f"{key}_m")
        return (uk * 1e8) + (man * 1e4)

    loss = cimon_input("고장 1회당 평균 손실", 0, 500, "loss")
    energy = cimon_input("연간 총 에너지 비용", 2, 0, "energy")
    defect = cimon_input("연간 불량품 손실", 0, 1000, "defect")
    staff = st.number_input("인력 효율화 (재배치 가능 인원)", 0, 10, 1)
    salary = st.number_input("인당 평균 연봉 (만원)", 3000, 15000, 4500) * 1e4
    invest = cimon_input("싸이몬 솔루션 도입 비용", 1, 5000, "inv")
    is_redun = st.toggle("솔루션 이중화(Redundancy) 적용", value=True)

# [수정] 계산 로직: 초기(1년차) 절감액 계산
pdm = (faults * loss) * 0.6
redun = (faults * loss * 0.3) if is_redun else 0
ene_save = energy * 0.1
def_save = defect * 0.2
lab_save = staff * salary
base_total_save = pdm + redun + ene_save + def_save + lab_save

# [추가] 지수 성장을 위한 파라미터 (내부 지표)
# 매년 자동화 최적화로 인해 효율이 15%씩 복리로 개선된다고 가정
annual_growth_rate = 0.15 

# [수정] 5개년 누적 현금흐름 계산 (Exponential)
years_list = list(range(6))
cash_flow = []
cumulative_savings = 0

for i in years_list:
    if i == 0:
        # 0년차는 투자비만 지출된 상태
        cash_flow.append(-invest)
    else:
        # 매년 절감액이 annual_growth_rate만큼 지수적으로 증가
        # 당해연도 절감액 = 초기절감액 * (1 + 성장률)^(n-1)
        yearly_benefit = base_total_save * ((1 + annual_growth_rate) ** (i - 1))
        cumulative_savings += yearly_benefit
        cash_flow.append(cumulative_savings - invest)

# 투자 회수 기간 계산 (단순 계산 대신 정밀 계산 가능하지만 UI 유지를 위해 유지)
payback = invest / base_total_save if base_total_save > 0 else 0

with right:
    st.subheader("📊 시뮬레이션 리포트")
    r1, r2 = st.columns(2)
    # 1년차 기준 표시
    with r1: st.metric("1년차 기대 절감액", f"{base_total_save/1e8:.2f} 억")
    with r2: st.metric("예상 투자 회수 기간", f"{payback:.2f} 년")

    # --- 그래프 파트 (Exponential Curve 시각화) ---
    years_label = [f"{i}년" for i in range(6)]
    
    fig = go.Figure()
    
    # 누적 수익 곡선
    fig.add_trace(go.Scatter(
        x=years_label, 
        y=cash_flow, 
        mode='lines+markers+text',
        text=[f"{v/1e8:.1f}억" if abs(v) >= 1e8 else f"{v/1e4:,.0f}만" for v in cash_flow],
        textposition="top center",
        fill='tozeroy', 
        line=dict(color='#0077ff', width=4, shape='spline'), # spline으로 곡선화
        marker=dict(size=10, color='#2ea043')
    ))
    
    # 손익분기점(0원) 라인 추가
    fig.add_hline(y=0, line_dash="dash", line_color="red", opacity=0.5)
    
    fig.update_layout(
        template="none",
        height=380, 
        margin=dict(l=10, r=10, t=30, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        hovermode="x unified",
        title=dict(text="자동화 도입 후 누적 수익 (지수 성장 모델 적용)", font=dict(size=14))
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
    
    st.plotly_chart(fig, use_container_width=True)
    # --- 그래프 수정 끝 ---

    # 세부 절감 항목
    st.markdown(f"""
    <div class="result-section">
        <p style="font-weight:bold; color:#0077ff; border-bottom:2px solid #0077ff; padding-bottom:5px;">📋 세부 절감 항목</p>
        <div class="saving-item"><span>🛠️ 예측 유지보수(PdM) 효과</span> <span class="val-text">{pdm/1e4:,.0f} 만원</span></div>
        <div class="saving-item"><span>🛡️ 이중화 솔루션 안정성</span> <span class="val-text">{redun/1e4:,.0f} 만원</span></div>
        <div class="saving-item"><span>⚡ 에너지 사용 최적화</span> <span class="val-text">{ene_save/1e4:,.0f} 만원</span></div>
        <div class="saving-item"><span>✅ 품질 개선(불량률 감소)</span> <span class="val-text">{def_save/1e4:,.0f} 만원</span></div>
        <div class="saving-item"><span>👤 인적 자원 효율화</span> <span class="val-text">{lab_save/1e4:,.0f} 만원</span></div>
    </div>
    """, unsafe_allow_html=True) 

st.markdown("---")
if st.button("◀ 메인 페이지로 돌아가기", key="bottom_back", use_container_width=True):

    st.switch_page("main_v0.3.py")


