import streamlit as st

def apply_styles():
    st.markdown(
        """
        <style>
        /* ─── Google Fonts ─────────────────────────────────── */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;900&family=Rajdhani:wght@500;600;700&display=swap');

        /* ─── CSS Variables / Design Tokens ────────────────── */
        :root {
            --pitch-dark:   #060d06;
            --pitch-green:  #0a1f0a;
            --grass-mid:    #0d2b0d;
            --emerald:      #00c853;
            --emerald-glow: #00ff6a;
            --gold:         #ffd700;
            --gold-light:   #ffe566;
            --white:        #ffffff;
            --grey-200:     #e2e8f0;
            --grey-400:     #94a3b8;
            --glass-bg:     rgba(255,255,255,0.05);
            --glass-border: rgba(255,255,255,0.10);
            --card-bg:      rgba(10,31,10,0.75);
            --card-border:  rgba(0,200,83,0.25);
            --shadow-green: 0 0 30px rgba(0,200,83,0.20);
            --shadow-gold:  0 0 20px rgba(255,215,0,0.30);
            --radius-lg:    16px;
            --radius-md:    10px;
        }

        /* ─── Hide Streamlit Top Header / Toolbar ───────────── */
        header,
        header[data-testid="stHeader"],
        #stDecoration,
        .stDeployButton,
        #MainMenu,
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        [data-testid="stHeader"] {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
            max-height: 0 !important;
            overflow: hidden !important;
            position: fixed !important;
            top: -100px !important;
        }

        /* Extra header/banner selectors for different Streamlit versions */
        div[data-testid="stAppViewContainer"] > header,
        div[role="banner"],
        .reportview-container header,
        .css-1v0mbdj.e1fqkh3o0 {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
            max-height: 0 !important;
            overflow: hidden !important;
            position: fixed !important;
            top: -120px !important;
        }

        /* Push content to very top since header is removed */
        .stApp > .main > .block-container {
            padding-top: 0.5rem !important;
        }

        .stApp {
            margin-top: 0 !important;
        }

        .appview-container {
            padding-top: 0 !important;
        }

        /* ─── Global Reset & Body ───────────────────────────── */
        html, body, [class*="css"] {
            font-family: 'Outfit', sans-serif !important;
        }

        /* Pitch-style background with subtle stripe pattern */
        .stApp {
            background-color: var(--pitch-dark) !important;
            background-image:
                repeating-linear-gradient(
                    90deg,
                    transparent,
                    transparent 60px,
                    rgba(0,200,83,0.025) 60px,
                    rgba(0,200,83,0.025) 120px
                ),
                radial-gradient(ellipse at 50% 0%, rgba(0,200,83,0.12) 0%, transparent 65%);
            min-height: 100vh;
        }

        /* ─── Main Content Area ─────────────────────────────── */
        .main .block-container {
            padding-top: 0.5rem !important;
            padding-bottom: 3rem !important;
            max-width: 1200px !important;
        }

        /* ─── Header / Title ────────────────────────────────── */
        h1 {
            font-family: 'Rajdhani', sans-serif !important;
            font-size: 3rem !important;
            font-weight: 700 !important;
            color: transparent !important;
            background: linear-gradient(135deg, var(--emerald-glow) 0%, var(--gold) 100%) !important;
            -webkit-background-clip: text !important;
            background-clip: text !important;
            text-align: center !important;
            letter-spacing: 2px !important;
            text-transform: uppercase !important;
            margin-bottom: 0.25rem !important;
            filter: drop-shadow(0 0 18px rgba(0,200,83,0.45));
        }

        h2 {
            font-family: 'Rajdhani', sans-serif !important;
            font-size: 1.6rem !important;
            font-weight: 600 !important;
            color: var(--emerald) !important;
            letter-spacing: 1px !important;
            border-left: 3px solid var(--gold);
            padding-left: 10px;
            margin-top: 1.5rem !important;
        }

        h3 {
            font-family: 'Rajdhani', sans-serif !important;
            font-weight: 600 !important;
            color: var(--grey-200) !important;
            letter-spacing: 0.5px !important;
        }

        /* ─── Caption / Subtext ─────────────────────────────── */
        .element-container small,
        .stCaption, [data-testid="stCaptionContainer"] p {
            color: var(--grey-400) !important;
            text-align: center !important;
            font-size: 0.9rem !important;
            letter-spacing: 0.5px !important;
        }

        /* ─── Sidebar ───────────────────────────────────────── */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #061206 0%, #0a1a0a 100%) !important;
            border-right: 1px solid var(--card-border) !important;
        }

        [data-testid="stSidebar"] .stMarkdown p,
        [data-testid="stSidebar"] label {
            color: var(--grey-200) !important;
        }

        /* ─── Divider ───────────────────────────────────────── */
        hr {
            border: none !important;
            border-top: 1px solid var(--card-border) !important;
            margin: 1.5rem 0 !important;
        }

        /* ─── Selectboxes / Dropdowns ───────────────────────── */
        [data-testid="stSelectbox"] label {
            color: var(--grey-200) !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            text-transform: uppercase !important;
            letter-spacing: 0.5px !important;
        }

        /* Selected value text inside the select box */
        [data-testid="stSelectbox"] > div > div {
            background: var(--card-bg) !important;
            border: 1px solid var(--card-border) !important;
            border-radius: var(--radius-md) !important;
            color: var(--grey-200) !important;
            font-weight: 700 !important;
            font-size: 1rem !important;
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
        }

        /* Ensure inner text/span inside select shows matching high-contrast color */
        [data-testid="stSelectbox"] > div > div span,
        [data-testid="stSelectbox"] > div > div div {
            color: var(--grey-200) !important;
            font-weight: 700 !important;
        }

        [data-testid="stSelectbox"] > div > div:focus-within,
        [data-testid="stSelectbox"] > div > div:hover {
            border-color: var(--emerald) !important;
            box-shadow: 0 0 0 2px rgba(0,200,83,0.20) !important;
        }

        /* ─── Dropdown Option List (Streamlit 1.58 portal) ──── */
        /*
         * Streamlit renders dropdowns in a BaseWeb popover portal
         * OUTSIDE the .stApp container. We use the broadest possible
         * selectors with !important to guarantee visibility.
         */

        /* Popover backdrop / wrapper — every nested div */
        [data-baseweb="popover"],
        [data-baseweb="popover"] > div,
        [data-baseweb="popover"] > div > div,
        [data-baseweb="popover"] > div > div > div,
        [data-baseweb="popover"] div[class],
        div[data-baseweb="popover"] * {
            background-color: #0a1a0a !important;
            background: #0a1a0a !important;
        }

        /* The popover container itself */
        [data-baseweb="popover"] {
            border: 1px solid rgba(0,200,83,0.4) !important;
            border-radius: 10px !important;
            box-shadow: 0 12px 48px rgba(0,0,0,0.8), 0 0 24px rgba(0,200,83,0.15) !important;
            overflow: hidden !important;
        }

        /* The listbox and its container */
        ul[role="listbox"],
        [data-baseweb="menu"],
        [data-baseweb="menu"] > div,
        [data-baseweb="menu"] ul {
            background-color: #0a1a0a !important;
            background: #0a1a0a !important;
            padding: 4px !important;
        }

        /* ── Every single option item ─────────────────────────── */
        ul[role="listbox"] li,
        ul[role="listbox"] > li,
        [data-baseweb="menu"] li,
        [role="option"],
        li[role="option"],
        [data-baseweb="menu"] [role="option"] {
            background-color: transparent !important;
            background: transparent !important;
            color: #ffffff !important;
            font-family: 'Outfit', sans-serif !important;
            font-size: 0.95rem !important;
            font-weight: 400 !important;
            border-radius: 6px !important;
            padding: 10px 16px !important;
            cursor: pointer !important;
            transition: background-color 0.12s ease !important;
        }

        /* Hover state — green highlight */
        ul[role="listbox"] li:hover,
        [data-baseweb="menu"] li:hover,
        [role="option"]:hover,
        li[role="option"]:hover {
            background-color: rgba(0,200,83,0.22) !important;
            background: rgba(0,200,83,0.22) !important;
            color: #00ff6a !important;
        }

        /* Focused / keyboard-highlighted option */
        [data-baseweb="menu"] li[aria-selected="true"],
        ul[role="listbox"] li[aria-selected="true"],
        [role="option"][aria-selected="true"],
        li[role="option"][aria-selected="true"],
        [data-baseweb="menu"] li[data-highlighted],
        [data-baseweb="menu"] li[data-highlighted="true"] {
            background-color: rgba(0,200,83,0.30) !important;
            background: rgba(0,200,83,0.30) !important;
            color: #00ff6a !important;
            font-weight: 600 !important;
        }

        /* Also catch the BaseWeb isHighlighted inline-style override */
        ul[role="listbox"] li[style],
        [data-baseweb="menu"] li[style] {
            background-color: transparent !important;
            color: #ffffff !important;
        }

        ul[role="listbox"] li[style]:hover,
        [data-baseweb="menu"] li[style]:hover {
            background-color: rgba(0,200,83,0.22) !important;
            color: #00ff6a !important;
        }

        /* Text/span inside option items */
        ul[role="listbox"] li span,
        ul[role="listbox"] li div,
        [data-baseweb="menu"] li span,
        [data-baseweb="menu"] li div,
        [role="option"] span,
        [role="option"] div {
            color: inherit !important;
        }

        /* Search/filter input inside dropdown */
        [data-baseweb="select"] input,
        [data-baseweb="menu"] input,
        [data-baseweb="popover"] input {
            background: #060d06 !important;
            color: #ffffff !important;
            border: 1px solid rgba(0,200,83,0.35) !important;
            border-radius: 6px !important;
            caret-color: #00c853 !important;
        }

        /* The "no results" text */
        [data-baseweb="menu"] [role="presentation"],
        [data-baseweb="menu"] [data-baseweb="menu-item-empty"] {
            color: #94a3b8 !important;
        }

        /* Scrollbar inside dropdown */
        [data-baseweb="menu"] ::-webkit-scrollbar { width: 5px; }
        [data-baseweb="menu"] ::-webkit-scrollbar-track { background: #0a1a0a; }
        [data-baseweb="menu"] ::-webkit-scrollbar-thumb {
            background: #00c853;
            border-radius: 3px;
        }
        [data-baseweb="popover"] ::-webkit-scrollbar { width: 5px; }
        [data-baseweb="popover"] ::-webkit-scrollbar-track { background: #0a1a0a; }
        [data-baseweb="popover"] ::-webkit-scrollbar-thumb {
            background: #00c853;
            border-radius: 3px;
        }

        /* ─── Multiselect ───────────────────────────────────── */
        [data-testid="stMultiSelect"] label {
            color: var(--grey-200) !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            text-transform: uppercase !important;
        }

        [data-testid="stMultiSelect"] > div {
            background: var(--card-bg) !important;
            border: 1px solid var(--card-border) !important;
            border-radius: var(--radius-md) !important;
            color: var(--white) !important;
        }

        span[data-baseweb="tag"] {
            background-color: rgba(0,200,83,0.20) !important;
            border: 1px solid var(--emerald) !important;
            color: var(--emerald-glow) !important;
            border-radius: 6px !important;
        }

        /* ─── Primary Button ────────────────────────────────── */
        .stButton > button {
            background: linear-gradient(135deg, #00a845 0%, #00c853 50%, #00e676 100%) !important;
            color: #060d06 !important;
            font-family: 'Rajdhani', sans-serif !important;
            font-size: 1.1rem !important;
            font-weight: 700 !important;
            letter-spacing: 2px !important;
            text-transform: uppercase !important;
            border: none !important;
            border-radius: var(--radius-md) !important;
            height: 3.2em !important;
            width: 100% !important;
            cursor: pointer !important;
            transition: transform 0.15s ease, box-shadow 0.15s ease, filter 0.15s ease !important;
            box-shadow: 0 4px 20px rgba(0,200,83,0.40) !important;
            position: relative !important;
            overflow: hidden !important;
        }

        .stButton > button::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -60%;
            width: 30%;
            height: 200%;
            background: rgba(255,255,255,0.25);
            transform: skewX(-20deg);
            transition: left 0.4s ease;
        }

        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 30px rgba(0,200,83,0.60), 0 0 50px rgba(0,200,83,0.20) !important;
            filter: brightness(1.08) !important;
        }

        .stButton > button:hover::before {
            left: 130%;
        }

        .stButton > button:active {
            transform: translateY(0px) !important;
            box-shadow: 0 2px 10px rgba(0,200,83,0.40) !important;
        }

        /* ─── Metric Cards ──────────────────────────────────── */
        [data-testid="stMetric"] {
            background: var(--card-bg) !important;
            border: 1px solid var(--card-border) !important;
            border-radius: var(--radius-lg) !important;
            padding: 1rem 1.25rem !important;
            box-shadow: var(--shadow-green) !important;
            backdrop-filter: blur(10px) !important;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        [data-testid="stMetric"]:hover {
            transform: translateY(-3px);
            box-shadow: 0 0 40px rgba(0,200,83,0.30) !important;
        }

        [data-testid="stMetricLabel"] {
            color: var(--grey-400) !important;
            font-size: 0.8rem !important;
            font-weight: 600 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.8px !important;
        }

        [data-testid="stMetricValue"] {
            color: var(--emerald-glow) !important;
            font-family: 'Rajdhani', sans-serif !important;
            font-size: 1.8rem !important;
            font-weight: 700 !important;
        }

        [data-testid="stMetricDelta"] {
            color: var(--gold) !important;
        }

        /* ─── Success / Info / Warning / Error Alerts ───────── */
        [data-testid="stAlert"] {
            border-radius: var(--radius-md) !important;
            border: none !important;
            backdrop-filter: blur(8px) !important;
        }

        /* Success */
        .stSuccess, [data-baseweb="notification"][kind="positive"] {
            background: rgba(0,200,83,0.15) !important;
            border-left: 4px solid var(--emerald) !important;
            color: var(--emerald-glow) !important;
            border-radius: var(--radius-md) !important;
        }

        /* Warning */
        .stWarning {
            background: rgba(255,215,0,0.10) !important;
            border-left: 4px solid var(--gold) !important;
            color: var(--gold-light) !important;
            border-radius: var(--radius-md) !important;
        }

        /* Error */
        .stError {
            background: rgba(244,67,54,0.10) !important;
            border-left: 4px solid #f44336 !important;
            border-radius: var(--radius-md) !important;
        }

        /* ─── Tabs ──────────────────────────────────────────── */
        [data-testid="stTabs"] [data-baseweb="tab-list"] {
            background: transparent !important;
            border-bottom: 2px solid var(--card-border) !important;
            gap: 0.5rem !important;
        }

        [data-testid="stTabs"] [data-baseweb="tab"] {
            background: transparent !important;
            color: var(--grey-400) !important;
            font-family: 'Rajdhani', sans-serif !important;
            font-weight: 600 !important;
            font-size: 1rem !important;
            letter-spacing: 1px !important;
            border-radius: var(--radius-md) var(--radius-md) 0 0 !important;
            padding: 0.6rem 1.4rem !important;
            transition: color 0.2s, background 0.2s;
        }

        [data-testid="stTabs"] [aria-selected="true"] {
            background: rgba(0,200,83,0.12) !important;
            color: var(--emerald-glow) !important;
            border-bottom: 2px solid var(--emerald) !important;
        }

        /* ─── Expander ──────────────────────────────────────── */
        [data-testid="stExpander"] {
            background: var(--card-bg) !important;
            border: 1px solid var(--card-border) !important;
            border-radius: var(--radius-lg) !important;
            overflow: hidden !important;
        }

        [data-testid="stExpander"] summary {
            color: var(--grey-200) !important;
            font-weight: 600 !important;
        }

        /* ─── DataFrames / Tables ───────────────────────────── */
        [data-testid="stDataFrame"] {
            border: 1px solid var(--card-border) !important;
            border-radius: var(--radius-lg) !important;
            overflow: hidden !important;
        }

        /* ─── Plotly Chart Container ────────────────────────── */
        [data-testid="stPlotlyChart"] {
            border: 1px solid var(--card-border) !important;
            border-radius: var(--radius-lg) !important;
            background: var(--card-bg) !important;
            backdrop-filter: blur(8px) !important;
            padding: 0.5rem !important;
            box-shadow: var(--shadow-green) !important;
        }

        /* ─── Scrollbar ─────────────────────────────────────── */
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: var(--pitch-dark); }
        ::-webkit-scrollbar-thumb {
            background: var(--emerald);
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover { background: var(--emerald-glow); }

        /* ─── Custom Football Banner ────────────────────────── */
        .football-banner {
            text-align: center;
            padding: 0.4rem 0 1.2rem 0;
            font-size: 0.85rem;
            color: var(--grey-400);
            letter-spacing: 3px;
            text-transform: uppercase;
        }

        /* ─── Pitch Divider ─────────────────────────────────── */
        .pitch-divider {
            height: 2px;
            background: linear-gradient(90deg,
                transparent 0%,
                var(--emerald) 30%,
                var(--gold) 50%,
                var(--emerald) 70%,
                transparent 100%);
            margin: 1.5rem 0;
            border-radius: 2px;
        }

        /* ─── Stat Card (custom HTML component) ─────────────── */
        .stat-card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: var(--radius-lg);
            padding: 1.2rem 1.5rem;
            text-align: center;
            backdrop-filter: blur(10px);
            box-shadow: var(--shadow-green);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .stat-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 0 45px rgba(0,200,83,0.30);
        }

        .stat-card .stat-label {
            font-size: 0.75rem;
            font-weight: 600;
            color: var(--grey-400);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 0.4rem;
        }

        .stat-card .stat-value {
            font-family: 'Rajdhani', sans-serif;
            font-size: 2rem;
            font-weight: 700;
            color: var(--emerald-glow);
        }

        /* ─── Winner Highlight Banner ───────────────────────── */
        .winner-banner {
            background: linear-gradient(135deg,
                rgba(255,215,0,0.15) 0%,
                rgba(0,200,83,0.15) 100%);
            border: 1px solid var(--gold);
            border-radius: var(--radius-lg);
            padding: 1.2rem;
            text-align: center;
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.4rem;
            font-weight: 700;
            color: var(--gold);
            letter-spacing: 2px;
            text-transform: uppercase;
            box-shadow: var(--shadow-gold);
            animation: pulse-gold 2.5s ease-in-out infinite;
        }

        @keyframes pulse-gold {
            0%, 100% { box-shadow: 0 0 20px rgba(255,215,0,0.30); }
            50%       { box-shadow: 0 0 40px rgba(255,215,0,0.55); }
        }

        /* ─── VS Badge ──────────────────────────────────────── */
        .vs-badge {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 56px;
            height: 56px;
            background: linear-gradient(135deg, var(--emerald) 0%, var(--gold) 100%);
            border-radius: 50%;
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.1rem;
            font-weight: 900;
            color: #060d06;
            margin: 0 auto 1rem auto;
            box-shadow: var(--shadow-green);
        }

        /* ─── Floating Football Decoration ──────────────────── */
        .football-deco {
            text-align: center;
            font-size: 3rem;
            margin: -0.5rem 0 0.5rem 0;
            filter: drop-shadow(0 0 12px rgba(0,200,83,0.5));
            animation: bounce-ball 2s ease-in-out infinite;
        }

        @keyframes bounce-ball {
            0%, 100% { transform: translateY(0px); }
            50%       { transform: translateY(-8px); }
        }

        /* ─── Column gap fix ────────────────────────────────── */
        [data-testid="column"] {
            padding: 0 0.5rem !important;
        }

        /* ─── General text color ────────────────────────────── */
        p, li, span {
            color: var(--grey-200) !important;
        }

        label {
            color: var(--grey-200) !important;
        }

        /* ─── Team selection badges (visible selected team) ─── */
        .team-badge {
            display: inline-block;
            padding: 8px 12px;
            border-radius: 999px;
            font-weight: 700;
            margin: 0.5rem 0 1rem 0;
            box-shadow: 0 6px 20px rgba(0,0,0,0.6);
            color: #060d06 !important;
            font-family: 'Rajdhani', sans-serif !important;
            letter-spacing: 0.6px;
        }

        .team-badge.home {
            background: linear-gradient(90deg, var(--emerald) 0%, var(--emerald-glow) 100%) !important;
            border: 1px solid rgba(0,200,83,0.25) !important;
        }

        .team-badge.away {
            background: linear-gradient(90deg, var(--gold) 0%, var(--gold-light) 100%) !important;
            border: 1px solid rgba(255,215,0,0.25) !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )