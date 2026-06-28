import streamlit as st
import pandas as pd
import plotly.graph_objects as go


# ─── Header ──────────────────────────────────────────────────────────────────

def render_header():
    st.markdown('<div class="football-deco">⚽</div>', unsafe_allow_html=True)
    st.title("FIFA AI Match Predictor")
    st.markdown(
        '<div class="football-banner">🏟️ &nbsp; ML-Powered Football Match Outcome Prediction &nbsp; 🏟️</div>',
        unsafe_allow_html=True
    )
    st.markdown('<div class="pitch-divider"></div>', unsafe_allow_html=True)


# ─── Match Input ──────────────────────────────────────────────────────────────

def render_match_input(data):
    teams = sorted(
        set(data["home_team"].dropna().unique()) |
        set(data["away_team"].dropna().unique())
    )
    tournaments = (
        sorted(set(data["tournament"].dropna()))
        if "tournament" in data else ["Friendly"]
    )

    st.markdown("#### 🏠 &nbsp; Home Team")
    home_team = st.selectbox("Home Team", teams, index=0, label_visibility="collapsed")
    # Visible badge for selected home team (improves visibility)
    st.markdown(f'<div class="team-badge home">🏠 &nbsp; {home_team}</div>', unsafe_allow_html=True)

    # VS badge
    st.markdown('<div class="vs-badge">VS</div>', unsafe_allow_html=True)

    st.markdown("#### ✈️ &nbsp; Away Team")
    away_team_options = [t for t in teams if t != home_team] or teams
    away_team = st.selectbox("Away Team", away_team_options, index=0,
                             key="away_team", label_visibility="collapsed")
    # Visible badge for selected away team (improves visibility)
    st.markdown(f'<div class="team-badge away">✈️ &nbsp; {away_team}</div>', unsafe_allow_html=True)

    st.markdown("#### 🏆 &nbsp; Tournament")
    tournament = st.selectbox("Tournament", tournaments, index=0,
                              label_visibility="collapsed")

    return home_team, away_team, tournament


# ─── Prediction Panel ─────────────────────────────────────────────────────────

def render_prediction_panel(result):
    st.markdown("## 📊 Prediction Result")
    st.markdown('<div class="pitch-divider"></div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("🏠 Home Win", f"{result['home_win']:.1%}")
    with c2:
        st.metric("🤝 Draw", f"{result['draw']:.1%}")
    with c3:
        st.metric("✈️ Away Win", f"{result['away_win']:.1%}")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f'<div class="winner-banner">🏆 &nbsp; Predicted Winner: {result["winner"]} &nbsp; 🏆</div>',
        unsafe_allow_html=True
    )


# ─── Probability Chart ────────────────────────────────────────────────────────

def render_probability_chart(result):
    labels = ["Home Win", "Draw", "Away Win"]
    values = [result["home_win"], result["draw"], result["away_win"]]
    colors = ["#00c853", "#ffd700", "#0d47a1"]
    bar_colors_hover = ["#00ff6a", "#ffe566", "#1565c0"]

    fig = go.Figure(data=[
        go.Bar(
            x=labels,
            y=values,
            marker=dict(
                color=colors,
                line=dict(color="rgba(255,255,255,0.1)", width=1),
                cornerradius=8,
            ),
            text=[f"{v:.1%}" for v in values],
            textposition="outside",
            textfont=dict(color="#e2e8f0", size=14, family="Rajdhani"),
            hovertemplate="<b>%{x}</b><br>Probability: %{text}<extra></extra>",
        )
    ])

    fig.update_layout(
        title=dict(
            text="⚽  Match Probability Breakdown",
            font=dict(color="#e2e8f0", size=18, family="Rajdhani"),
            x=0.5,
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#94a3b8", family="Outfit"),
        yaxis=dict(
            tickformat=".0%",
            gridcolor="rgba(255,255,255,0.06)",
            range=[0, max(values) * 1.3],
            showline=False,
            zeroline=False,
        ),
        xaxis=dict(showline=False),
        margin=dict(l=20, r=20, t=55, b=20),
        height=320,
        bargap=0.35,
    )

    st.plotly_chart(fig, use_container_width=True)


# ─── Team Stats ───────────────────────────────────────────────────────────────

def render_team_stats(data, home_team, away_team):
    st.markdown("## 📈 Team Comparison")
    st.markdown('<div class="pitch-divider"></div>', unsafe_allow_html=True)

    home_mask = data["home_team"] == home_team
    away_mask = data["away_team"] == away_team

    # ── Avg ratings ──────────────────────────────────────────
    home_rating_vals, away_rating_vals = [], []
    if "home_player_rating" in data.columns:
        home_rating_vals += list(data.loc[home_mask, "home_player_rating"].dropna())
        away_rating_vals += list(data.loc[data["home_team"] == away_team, "home_player_rating"].dropna())
    if "away_player_rating" in data.columns:
        home_rating_vals += list(data.loc[data["away_team"] == home_team, "away_player_rating"].dropna())
        away_rating_vals += list(data.loc[away_mask, "away_player_rating"].dropna())

    home_rating = round(sum(home_rating_vals) / len(home_rating_vals), 2) if home_rating_vals else "N/A"
    away_rating = round(sum(away_rating_vals) / len(away_rating_vals), 2) if away_rating_vals else "N/A"

    # ── Win stats ─────────────────────────────────────────────
    home_wins_as_home = int(
        ((data["home_team"] == home_team) & (data.get("result", pd.Series(dtype=str)) == "H")).sum()
    ) if "result" in data.columns else "—"

    away_wins_as_away = int(
        ((data["away_team"] == away_team) & (data.get("result", pd.Series(dtype=str)) == "A")).sum()
    ) if "result" in data.columns else "—"

    # ── Goals scored ──────────────────────────────────────────
    home_goals = "—"
    away_goals = "—"
    if "home_score" in data.columns:
        home_goals = round(data.loc[home_mask, "home_score"].dropna().mean(), 1) if home_mask.any() else "—"
    if "away_score" in data.columns:
        away_goals = round(data.loc[away_mask, "away_score"].dropna().mean(), 1) if away_mask.any() else "—"

    # ── Render ────────────────────────────────────────────────
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"### 🏠 {home_team}")
        st.metric("⭐ Avg Player Rating", home_rating)
        st.metric("🥅 Avg Goals (Home)", home_goals)
        if home_wins_as_home != "—":
            st.metric("🏆 Home Wins", home_wins_as_home)

    with col2:
        st.markdown(f"### ✈️ {away_team}")
        st.metric("⭐ Avg Player Rating", away_rating)
        st.metric("🥅 Avg Goals (Away)", away_goals)
        if away_wins_as_away != "—":
            st.metric("🏆 Away Wins", away_wins_as_away)

    # ── Radar chart for head-to-head feel ─────────────────────
    if all(isinstance(v, float) for v in [home_rating, away_rating]):
        _render_rating_gauge(home_team, away_team, float(home_rating), float(away_rating))


def _render_rating_gauge(home_team, away_team, home_val, away_val):
    """Side-by-side horizontal bar comparison."""
    fig = go.Figure()

    fig.add_trace(go.Bar(
        name=home_team,
        y=["Player Rating"],
        x=[home_val],
        orientation="h",
        marker_color="#00c853",
        text=[f"{home_val}"],
        textposition="auto",
        textfont=dict(color="#060d06", size=13, family="Rajdhani"),
    ))

    fig.add_trace(go.Bar(
        name=away_team,
        y=["Player Rating"],
        x=[away_val],
        orientation="h",
        marker_color="#ffd700",
        text=[f"{away_val}"],
        textposition="auto",
        textfont=dict(color="#060d06", size=13, family="Rajdhani"),
    ))

    fig.update_layout(
        barmode="group",
        title=dict(
            text="⚽  Rating Head-to-Head",
            font=dict(color="#e2e8f0", size=16, family="Rajdhani"),
            x=0.5,
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#94a3b8", family="Outfit"),
        legend=dict(
            font=dict(color="#e2e8f0"),
            bgcolor="rgba(0,0,0,0)",
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        ),
        margin=dict(l=10, r=10, t=55, b=10),
        height=200,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False),
    )

    st.plotly_chart(fig, use_container_width=True)