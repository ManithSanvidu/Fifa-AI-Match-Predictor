import streamlit as st
import pandas as pd
import numpy as np

from components import (
    render_header,
    render_match_input,
    render_prediction_panel,
    render_probability_chart,
    render_team_stats
)

from utils import load_models, predict_match, load_data
from styles import apply_styles

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FIFA AI Match Predictor",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed",
)

apply_styles()
render_header()

# ─── Load Resources ───────────────────────────────────────────────────────────
models = load_models()
data = load_data()

if data is None or not hasattr(data, "shape") or data.empty:
    st.error("⚠️  Match data could not be loaded. Please verify the data file exists and is valid.")
else:
    # ─── Two-column layout ────────────────────────────────────────────────────
    col1, col2 = st.columns([1, 1.3], gap="large")

    with col1:
        st.markdown("## ⚙️ Match Setup")
        home_team, away_team, tournament = render_match_input(data)

        st.markdown("<br>", unsafe_allow_html=True)
        predict_clicked = st.button("⚽  Predict Match Outcome")

        st.markdown('<div class="pitch-divider"></div>', unsafe_allow_html=True)
        render_team_stats(data, home_team, away_team)

    with col2:
        if predict_clicked:
            with st.spinner("🔄  Analyzing match data..."):
                result = predict_match(models, data, home_team, away_team, tournament)
            render_prediction_panel(result)
            render_probability_chart(result)
        else:
            # Placeholder state before prediction
            st.markdown(
                """
                <div style="
                    display:flex;
                    flex-direction:column;
                    align-items:center;
                    justify-content:center;
                    height:400px;
                    border:1px dashed rgba(0,200,83,0.30);
                    border-radius:16px;
                    background:rgba(10,31,10,0.40);
                    color:#94a3b8;
                    font-family:'Rajdhani',sans-serif;
                    font-size:1.1rem;
                    letter-spacing:2px;
                    text-transform:uppercase;
                ">
                    <span style="font-size:3.5rem;margin-bottom:1rem;
                        filter:drop-shadow(0 0 12px rgba(0,200,83,0.4));">⚽</span>
                    Select teams &amp; click<br>
                    <strong style="color:#00c853;">Predict Match Outcome</strong>
                </div>
                """,
                unsafe_allow_html=True
            )

# ─── Footer ───────────────────────────────────────────────────────────────────
st.markdown('<div class="pitch-divider"></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align:center;color:#475569;font-size:0.78rem;
        letter-spacing:1.5px;text-transform:uppercase;padding:0.5rem 0 1rem 0;">
        ⚽ &nbsp; FIFA AI Match Predictor &nbsp;•&nbsp; Powered by Machine Learning &nbsp; ⚽
    </div>
    """,
    unsafe_allow_html=True
)