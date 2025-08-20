import streamlit as st
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Alidar Kuchukov | Visionary Entrepreneur & Web3 Pioneer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'easter_egg_unlocked' not in st.session_state:
    st.session_state.easter_egg_unlocked = False
# Show Easter Egg if unlocked
    if st.session_state.easter_egg_unlocked:
        st.markdown('<div class="glass-card" style="margin-top: 30px;">', unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: center; padding: 20px;">
            <h2 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.8rem; 
                       font-weight: 600; background: linear-gradient(135deg, #EF4444 0%, #F87171 50%, #FCA5A5 100%);
                       -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
                       margin-bottom: 20px;">
                🎉 Happy Birthday, Brother! 🎉
            </h2>
            <p style="color: rgba(255, 255, 255, 0.9); font-size: 1.2rem; margin: 20px 0;">
                From your brother Alisher Beisembekov
            </p>
            <p style="color: rgba(255, 255, 255, 0.9); line-height: 1.8; margin: 20px 0;">
                Alidar, my brother! This website is my birthday gift to you. 
                You've always been more than a friend - you're family to me. 
                Your vision, passion, and unstoppable drive inspire everyone around you.
                <br><br>
                From dropping out of high school to pursue your dreams, to building 
                incredible companies and changing lives through your work - you've 
                shown what true leadership looks like.
                <br><br>
                Keep building the future, brother. The world needs more visionaries like you! 🚀
            </p>
            <p style="background: linear-gradient(135deg, #EF4444 0%, #F87171 100%);
                      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                      font-weight: 600; margin-top: 20px;">
                With love and respect,<br>
                Alisher ❤️
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1,1,1])
        with col2:
            if st.button("Close", key="close_easter_egg"):
                st.session_state.easter_egg_unlocked = False
        
        st.markdown('</div>', unsafe_allow_html=True)
# Advanced Red-themed CSS Design
def load_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700;800;900&display=swap');

        /* Global Styles */
        * {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background: linear-gradient(135deg, #4A1515 0%, #7A2525 50%, #5A1A1A 100%);
            background-attachment: fixed;
        }

        /* Hide Streamlit Branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background: rgba(74, 21, 21, 0.8);
            backdrop-filter: blur(20px);
            border-right: 1px solid rgba(255, 150, 150, 0.2);
        }

        section[data-testid="stSidebar"] .stButton > button {
            background: rgba(255, 150, 150, 0.08);
            color: rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(255, 150, 150, 0.2);
            border-radius: 15px;
            padding: 15px;
            width: 100%;
            transition: all 0.3s ease;
            font-weight: 500;
            margin-bottom: 10px;
        }

        section[data-testid="stSidebar"] .stButton > button:hover {
            background: linear-gradient(135deg, rgba(248, 113, 113, 0.4) 0%, rgba(239, 68, 68, 0.4) 100%);
            border: 1px solid rgba(255, 150, 150, 0.4);
            transform: translateX(5px);
            box-shadow: 0 5px 15px rgba(248, 113, 113, 0.4);
        }

        /* Animated Background */
        .animated-bg {
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: -1;
            background: linear-gradient(270deg, #4A1515, #7A2525, #5A1A1A, #4A1515);
            background-size: 800% 800%;
            animation: gradientShift 20s ease infinite;
        }

        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Glassmorphism Cards */
        .glass-card {
            background: rgba(255, 150, 150, 0.08);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 20px;
            border: 1px solid rgba(255, 150, 150, 0.15);
            padding: 30px;
            margin: 20px 0;
            box-shadow: 0 8px 32px 0 rgba(248, 113, 113, 0.4);
            transition: all 0.3s ease;
        }

        .glass-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px 0 rgba(248, 113, 113, 0.6);
            border: 1px solid rgba(255, 150, 150, 0.25);
        }

        /* Hero Section */
        .hero-name {
            font-family: 'Space Grotesk', sans-serif;
            font-size: clamp(3rem, 8vw, 6rem);
            font-weight: 700;
            background: linear-gradient(135deg, #EF4444 0%, #F87171 20%, #FCA5A5 40%, #FECACA 60%, #FEE2E2 80%, #EF4444 100%);
            background-size: 200% 200%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            animation: gradientText 5s ease infinite;
            letter-spacing: -0.02em;
            line-height: 1.1;
            margin-bottom: 0;
        }

        @keyframes gradientText {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .hero-title {
            font-family: 'Space Grotesk', sans-serif;
            font-size: clamp(1.2rem, 3vw, 1.8rem);
            color: rgba(255, 255, 255, 0.9);
            text-align: center;
            margin-top: 10px;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            font-weight: 300;
        }

        /* Metric Cards */
        .metric-card {
            background: linear-gradient(135deg, rgba(255,150,150,0.12) 0%, rgba(255,150,150,0.08) 100%);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 25px;
            text-align: center;
            border: 1px solid rgba(255, 150, 150, 0.15);
            transition: all 0.3s ease;
        }

        .metric-card:hover {
            transform: translateY(-5px) scale(1.02);
            border: 1px solid rgba(255, 150, 150, 0.3);
            box-shadow: 0 10px 30px rgba(248, 113, 113, 0.4);
        }

        .metric-number {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #EF4444 0%, #F87171 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 5px;
        }

        .metric-label {
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }

        /* Section Headers */
        .section-header {
            font-family: 'Space Grotesk', sans-serif;
            font-size: clamp(2rem, 4vw, 3rem);
            font-weight: 600;
            background: linear-gradient(135deg, #fff 0%, rgba(255,255,255,0.7) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 40px 0 30px 0;
            position: relative;
            padding-bottom: 15px;
        }

        .section-header:after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100px;
            height: 3px;
            background: linear-gradient(90deg, #EF4444 0%, #F87171 100%);
            border-radius: 2px;
        }

        /* Achievement Cards */
        .achievement-card {
            background: rgba(255, 150, 150, 0.06);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 25px;
            margin-bottom: 20px;
            border: 1px solid rgba(255, 150, 150, 0.12);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .achievement-card:before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,150,150,0.15), transparent);
            transition: left 0.5s ease;
        }

        .achievement-card:hover:before {
            left: 100%;
        }

        .achievement-card:hover {
            transform: translateX(5px);
            border: 1px solid rgba(255, 150, 150, 0.25);
            box-shadow: 0 5px 20px rgba(248, 113, 113, 0.4);
        }

        /* Skills Grid */
        .skill-tag {
            background: rgba(255, 150, 150, 0.08);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 150, 150, 0.15);
            color: rgba(255, 255, 255, 0.9);
            padding: 12px 20px;
            border-radius: 25px;
            text-align: center;
            font-weight: 500;
            transition: all 0.3s ease;
            cursor: default;
            display: inline-block;
            margin: 5px;
        }

        .skill-tag:hover {
            background: linear-gradient(135deg, rgba(248, 113, 113, 0.25) 0%, rgba(239, 68, 68, 0.25) 100%);
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(248, 113, 113, 0.4);
            border: 1px solid rgba(255, 150, 150, 0.3);
        }

        /* Floating Elements */
        .floating {
            animation: float 6s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }

        /* Glow Effect */
        .glow {
            box-shadow: 0 0 30px rgba(248, 113, 113, 0.6),
                        0 0 60px rgba(248, 113, 113, 0.4),
                        0 0 90px rgba(248, 113, 113, 0.2);
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
        }

        ::-webkit-scrollbar-track {
            background: rgba(255, 150, 150, 0.08);
        }

        ::-webkit-scrollbar-thumb {
            background: linear-gradient(135deg, #EF4444 0%, #F87171 100%);
            border-radius: 5px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: linear-gradient(135deg, #F87171 0%, #EF4444 100%);
        }

        /* Company Links */
        .company-link {
            color: inherit;
            text-decoration: none;
            transition: all 0.3s ease;
            position: relative;
        }

        .company-link:hover {
            text-shadow: 0 0 10px rgba(248, 113, 113, 0.8);
            transform: translateX(3px);
        }

        .company-link:after {
            content: ' 🔗';
            opacity: 0;
            transition: opacity 0.3s ease;
            font-size: 0.8em;
        }

        .company-link:hover:after {
            opacity: 0.7;
        }

        /* Text Styles */
        .text-gradient {
            background: linear-gradient(135deg, #EF4444 0%, #F87171 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .text-white {
            color: rgba(255, 255, 255, 0.9);
        }

        .text-muted {
            color: rgba(255, 255, 255, 0.6);
        }

        /* Sidebar Header */
        .sidebar-header {
            color: white;
            text-align: center;
            padding: 20px 0;
            border-bottom: 1px solid rgba(255, 150, 150, 0.15);
            margin-bottom: 20px;
        }

        .sidebar-name {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.5rem;
            font-weight: 600;
            background: linear-gradient(135deg, #EF4444 0%, #F87171 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 5px;
        }

        .sidebar-title {
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9rem;
            letter-spacing: 0.1em;
        }

        /* Easter Egg Styles */
        .easter-egg-trigger {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 50px;
            height: 50px;
            background: rgba(248, 113, 113, 0.15);
            border-radius: 50%;
            border: 1px solid rgba(248, 113, 113, 0.25);
            cursor: pointer;
            transition: all 0.3s ease;
            z-index: 1000;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
        }

        .easter-egg-trigger:hover {
            background: rgba(248, 113, 113, 0.25);
            transform: scale(1.1);
            box-shadow: 0 0 20px rgba(248, 113, 113, 0.6);
        }

        .easter-egg-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            z-index: 2000;
            display: flex;
            align-items: center;
            justify-content: center;
            animation: fadeIn 0.5s ease;
        }

        .easter-egg-content {
            background: linear-gradient(135deg, rgba(74, 21, 21, 0.9) 0%, rgba(122, 37, 37, 0.9) 100%);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            border: 2px solid rgba(248, 113, 113, 0.4);
            padding: 40px;
            text-align: center;
            max-width: 500px;
            margin: 20px;
            box-shadow: 0 20px 40px rgba(248, 113, 113, 0.4);
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .birthday-message {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            background: linear-gradient(135deg, #EF4444 0%, #F87171 50%, #FCA5A5 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
            animation: gradientText 3s ease infinite;
        }

        .close-button {
            background: rgba(248, 113, 113, 0.25);
            border: 1px solid rgba(248, 113, 113, 0.4);
            color: white;
            padding: 10px 20px;
            border-radius: 10px;
            cursor: pointer;
            margin-top: 20px;
            transition: all 0.3s ease;
        }

        .close-button:hover {
            background: rgba(248, 113, 113, 0.35);
            transform: scale(1.05);
        }
    </style>

    <div class="animated-bg"></div>
    """, unsafe_allow_html=True)

# Load CSS
load_css()

# Easter Egg Handler
def show_easter_egg():
    # Create a hidden button in the sidebar
    with st.sidebar:
        st.markdown("---")
        if st.button("🎁", help="Special surprise from a brother!", key="easter_egg_btn"):
            st.session_state.easter_egg_unlocked = True

# Sidebar Navigation
with st.sidebar:
    st.markdown("""
    <div class="sidebar-header">
        <div class="sidebar-name">Alidar Kuchukov</div>
        <div class="sidebar-title">Portfolio Navigation</div>
    </div>
    """, unsafe_allow_html=True)

    # Navigation buttons
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.current_page = 'home'
    if st.button("💼 Career", use_container_width=True):
        st.session_state.current_page = 'career'
    if st.button("🚀 Ventures", use_container_width=True):
        st.session_state.current_page = 'ventures'
    if st.button("🌐 Web3 Journey", use_container_width=True):
        st.session_state.current_page = 'web3'
    if st.button("🏆 Achievements", use_container_width=True):
        st.session_state.current_page = 'achievements'
    if st.button("📊 Analytics", use_container_width=True):
        st.session_state.current_page = 'analytics'

    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <p style="color: rgba(255, 255, 255, 0.6); margin-bottom: 15px;">Connect</p>
        <div style="display: flex; justify-content: center; gap: 15px;">
            <a href="https://www.linkedin.com/in/alidar-kuchukov-9bb253207/" style="color: rgba(255, 255, 255, 0.7); text-decoration: none;">💼</a>
            <a href="https://t.me/Alidar01" style="color: rgba(255, 255, 255, 0.7); text-decoration: none;">📱</a>
            <a href="#" style="color: rgba(255, 255, 255, 0.7); text-decoration: none;">🌐</a>
        </div>
        <p style="color: rgba(255, 255, 255, 0.4); font-size: 0.8rem; margin-top: 15px;">
            Look for something special below...
        </p>
    </div>
    """, unsafe_allow_html=True)

# Show Easter Egg
show_easter_egg()

# Show Easter Egg if unlocked
if st.session_state.easter_egg_unlocked:
    st.markdown('<div class="glass-card" style="margin-top: 30px;">', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h2 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.8rem; 
                   font-weight: 600; background: linear-gradient(135deg, #EF4444 0%, #F87171 50%, #FCA5A5 100%);
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
                   margin-bottom: 20px;">
            🎉 Happy Birthday, Brother! 🎉
        </h2>
        <p style="color: rgba(255, 255, 255, 0.9); font-size: 1.2rem; margin: 20px 0;">
            From your brother Alisher Beisembekov
        </p>
        <p style="color: rgba(255, 255, 255, 0.9); line-height: 1.8; margin: 20px 0;">
            Alidar, my brother! This website is my birthday gift to you. 
            You've always been more than a friend - you're family to me. 
            Your vision, passion, and unstoppable drive inspire everyone around you.
            <br><br>
            From dropping out of high school to pursue your dreams, to building 
            incredible companies and changing lives through your work - you've 
            shown what true leadership looks like.
            <br><br>
            Keep building the future, brother. The world needs more visionaries like you! 🚀
        </p>
        <p style="background: linear-gradient(135deg, #EF4444 0%, #F87171 100%);
                  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                  font-weight: 600; margin-top: 20px;">
            With love and respect,<br>
            Alisher ❤️
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("Close", key="close_easter_egg"):
            st.session_state.easter_egg_unlocked = False
    
    st.markdown('</div>', unsafe_allow_html=True)

# Page content based on selection
if st.session_state.current_page == 'home':
    # Hero Section
    st.markdown('<h1 class="hero-name floating">Alidar Kuchukov</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-title">Visionary Entrepreneur • Web3 Pioneer • Serial Founder</p>', unsafe_allow_html=True)

    # Quick Stats
    st.markdown("---")
    cols = st.columns(4)
    metrics = [
        ("Years in USA", "7", "🇺🇸"),
        ("Web3 Experience", "6", "🌐"),
        ("Funding Raised", "$1M+", "💰"),
        ("Countries Served", "35+", "🌍")
    ]

    for col, (label, value, icon) in zip(cols, metrics):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 2rem; margin-bottom: 10px;">{icon}</div>
                <div class="metric-number">{value}</div>
                <div class="metric-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    # Main Content
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Building the Future</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <p class="text-white" style="font-size: 1.1rem; line-height: 1.8;">
        Visionary entrepreneur who dropped out of one of California's best public high schools to fully dedicate 
        himself to business and startups. Mission-driven founder creating startups and products that solve 
        massive problems for people at scale. Currently pioneering the intersection of AI and Web3 in 
        language learning while building the next generation of digital experiences.
        </p>
        """, unsafe_allow_html=True)

        # Current Positions
        st.markdown('<h3 class="text-gradient" style="margin-top: 30px;">Current Leadership Roles</h3>',
                    unsafe_allow_html=True)

        positions = [
            {
                "title": "Co-Founder",
                "company": "Aleem",
                "period": "Mar 2025 - Present",
                "location": "New York, United States (Remote)",
                "description": "Revolutionary AI-powered language learning platform with Web3 tokenomics, serving 35+ countries"
            },
            {
                "title": "Serial Entrepreneur",
                "company": "Multiple Ventures",
                "period": "2022 - Present",
                "location": "Washington DC",
                "description": "Building and scaling innovative startups across Web3, EdTech, and charitable platforms"
            }
        ]

        for position in positions:
            st.markdown(f"""
            <div class="achievement-card">
                <h4 class="text-white">{position["title"]}</h4>
                <p class="text-gradient" style="font-weight: 600;">{position["company"]}</p>
                <p class="text-muted">{position["period"]} • {position["location"]}</p>
                <p class="text-white" style="margin-top: 10px;">{position["description"]}</p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        # Core Expertise
        st.markdown('<h3 class="text-gradient">Core Expertise</h3>', unsafe_allow_html=True)

        expertise = {
            "Entrepreneurship": ["Startup Founding", "Scaling", "Fundraising", "Strategic Vision"],
            "Web3 & Blockchain": ["6 Years Experience", "Private Sales", "NFT Platforms", "Tokenomics"],
            "Business Development": ["Growth Hacking", "International Expansion", "Partnerships", "Innovation"]
        }

        for category, skills in expertise.items():
            st.markdown(f'<p class="text-white" style="font-weight: 600; margin-top: 20px;">{category}</p>',
                        unsafe_allow_html=True)
            for skill in skills:
                st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

        # Background
        st.markdown('<h3 class="text-gradient" style="margin-top: 30px;">Background</h3>', unsafe_allow_html=True)
        st.markdown("""
        <div class="achievement-card">
            <h4 class="text-white">Location</h4>
            <p class="text-white">Washington DC</p>
            <p class="text-muted">7 years in USA</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="achievement-card">
            <h4 class="text-white">Education Path</h4>
            <p class="text-white">Self-Directed Learning</p>
            <p class="text-muted">Dropped out of top CA high school to pursue entrepreneurship</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'career':
    st.markdown('<h1 class="hero-name">Career Journey</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-title">From Actor to Serial Entrepreneur</p>', unsafe_allow_html=True)

    positions = [
        {
            "title": "Co-Founder",
            "company": "Aleem",
            "period": "Mar 2025 - Present (6 mos)",
            "location": "New York, United States • Remote",
            "description": "Co-founding revolutionary AI & Web3 language learning platform",
            "achievements": ["$5M valuation achieved", "MVP launched with 300 beta users", "Investments from USA and UAE secured", "35+ countries market reach"]
        },
        {
            "title": "Chief Executive Officer",
            "company": "GETENG",
            "period": "Jul 2023 - Feb 2024 (8 mos)",
            "location": "Remote",
            "description": "Leading GET ENGLISH to massive social media success",
            "achievements": ["320K Instagram followers in 1 year", "300M+ views generated", "700K+ free guide downloads", "3,000+ clients from 35 countries"]
        },
        {
            "title": "CEO",
            "company": "INIP",
            "period": "Jan 2022 - Jun 2023 (1 yr 6 mos)",
            "location": "Washington DC-Baltimore Area • Remote",
            "description": "Founded first charitable NFT marketplace",
            "achievements": ["$100K pre-seed funding raised", "First charitable NFT platform", "Innovative Web3 solution", "Social impact focus"]
        },
        {
            "title": "Actor",
            "company": "Central Casting",
            "period": "Aug 2018 - Nov 2020 (2 yrs 4 mos)",
            "location": "Los Angeles, California, United States • On-site",
            "description": "Professional acting career with major studios",
            "achievements": ["60OUT Escape Rooms commercials", "Family Jurassic World commercials", "ABC network projects", "Disney Studios TV shows", "Nickelodeon appearances"]
        }
    ]

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Professional Timeline</h2>', unsafe_allow_html=True)

    for i, position in enumerate(positions):
        color = "#EF4444" if i < 2 else "#F87171"
        
        st.markdown(f'''
        <div class="achievement-card">
            <div style="display: flex; align-items: start; gap: 20px;">
                <div style="min-width: 60px; height: 60px; background: linear-gradient(135deg, {color} 0%, #F87171 100%); 
                            border-radius: 15px; display: flex; align-items: center; justify-content: center; color: white; 
                            font-weight: bold; font-size: 1.5rem;">
                    {i + 1}
                </div>
                <div style="flex: 1;">
                    <h3 class="text-white">{position["title"]}</h3>
                    <p class="text-gradient" style="font-weight: 600; font-size: 1.1rem;">{position["company"]}</p>
                    <p class="text-muted">{position["period"]}</p>
                    <p class="text-muted" style="font-size: 0.9rem;">{position["location"]}</p>
                    <p class="text-white" style="margin: 15px 0;">{position["description"]}</p>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Achievement tags
        st.markdown('<div style="display: flex; flex-wrap: wrap; gap: 10px; margin: 15px 0;">', unsafe_allow_html=True)
        for achievement in position["achievements"]:
            st.markdown(f'<span class="skill-tag">{achievement}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'ventures':
    st.markdown('<h1 class="hero-name">Venture Portfolio</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-title">Building Impactful Companies</p>', unsafe_allow_html=True)

    # Current Ventures
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Current Ventures</h2>', unsafe_allow_html=True)

    ventures = [
        {
            "name": "Aleem",
            "category": "AI & Web3 EdTech",
            "status": "Active",
            "funding": "$5M Valuation",
            "description": "Revolutionary language learning platform combining AI personalization with Web3 tokenomics",
            "metrics": {"Beta Users": "300", "Countries": "35+", "Funding": "USA & UAE"},
            "highlights": ["MVP in beta testing", "International investment", "AI-powered learning", "Web3 integration"]
        },
        {
            "name": "GET ENGLISH (Pre-Startup)",
            "category": "EdTech & Social Media",
            "status": "Evolved",
            "funding": "Bootstrapped",
            "description": "Massive English learning community that grew to 320K followers and 300M views",
            "metrics": {"Followers": "320K", "Views": "300M", "Downloads": "700K", "Clients": "3,000+"},
            "highlights": ["Viral growth", "Global reach", "Free education", "Community building"]
        }
    ]

    for venture in ventures:
        status_color = "#00ff88" if venture["status"] == "Active" else "#ffa500"
        
        st.markdown(f'''
        <div class="achievement-card">
            <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 20px;">
                <div>
                    <h3 class="text-white">{venture["name"]}</h3>
                    <p class="text-gradient" style="font-weight: 600;">{venture["category"]}</p>
                </div>
                <div style="text-align: right;">
                    <span style="background: {status_color}; color: #000; padding: 5px 15px; 
                                border-radius: 20px; font-weight: 600; font-size: 0.9rem;">
                        {venture["status"]}
                    </span>
                    <p class="text-muted" style="margin-top: 5px;">{venture["funding"]}</p>
                </div>
            </div>
            <div style="text-align: center;">
                <p class="text-white" style="margin: 15px 0; line-height: 1.6;">{venture["description"]}</p>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Metrics section
        st.markdown('<div style="display: flex; gap: 30px; margin: 20px 0;">', unsafe_allow_html=True)
        cols = st.columns(len(venture["metrics"]))
        for i, (key, value) in enumerate(venture["metrics"].items()):
            with cols[i]:
                st.markdown(f'''
                <div style="text-align: center;">
                    <p class="text-gradient" style="font-weight: 700; font-size: 1.2rem; margin: 0;">{value}</p>
                    <p class="text-muted" style="font-size: 0.9rem; margin: 0;">{key}</p>
                </div>
                ''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Highlights section  
        st.markdown('<div style="display: flex; flex-wrap: wrap; gap: 10px; margin: 20px 0;">', unsafe_allow_html=True)
        for highlight in venture["highlights"]:
            st.markdown(f'<span class="skill-tag">{highlight}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Past Ventures
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Previous Ventures</h2>', unsafe_allow_html=True)

    past_ventures = [
        {
            "name": "INIP",
            "category": "Charitable NFT Marketplace",
            "period": "Jan 2022 - Jun 2023",
            "funding": "$100K Pre-seed",
            "description": "World's first charitable NFT marketplace combining blockchain technology with social impact",
            "impact": ["First of its kind", "Charitable focus", "Web3 innovation", "Social impact"],
            "status": "Completed"
        }
    ]

    for venture in past_ventures:
        st.markdown(f'''
        <div class="achievement-card">
            <h3 class="text-white">{venture["name"]}</h3>
            <p class="text-gradient" style="font-weight: 600; margin: 10px 0;">{venture["category"]}</p>
            <p class="text-muted">{venture["period"]} • {venture["funding"]}</p>
            <p class="text-white" style="margin: 15px 0;">{venture["description"]}</p>
        </div>
        ''', unsafe_allow_html=True)
        
        # Impact tags
        st.markdown('<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 15px;">', unsafe_allow_html=True)
        for impact in venture["impact"]:
            st.markdown(f'<span class="skill-tag">{impact}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'web3':
    st.markdown('<h1 class="hero-name">Web3 Journey</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-title">6 Years of Blockchain Innovation</p>', unsafe_allow_html=True)

    # Web3 Experience Overview
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Web3 Expertise</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="achievement-card">
            <h3 class="text-gradient">6 Years of Practical Experience</h3>
            <p class="text-white" style="margin: 15px 0;">
            Deep hands-on experience across almost all Web3 directions, from DeFi and NFTs 
            to tokenomics and blockchain development. Proven track record in private sales 
            and fundraising within the Web3 ecosystem.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="achievement-card">
            <h3 class="text-gradient">$1M+ Raised in Private Sales</h3>
            <p class="text-white" style="margin: 15px 0;">
            Successfully attracted over $1,000,000 for Web3 startups at the private-sales stage, 
            demonstrating deep understanding of crypto fundraising and investor relations.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="achievement-card">
            <h3 class="text-gradient">First Charitable NFT Marketplace</h3>
            <p class="text-white" style="margin: 15px 0;">
            Founded INIP, the world's first charitable NFT marketplace, combining blockchain 
            innovation with social impact. Raised $100K in pre-seed funding for this 
            groundbreaking platform.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="achievement-card">
            <h3 class="text-gradient">Web3 + AI Integration</h3>
            <p class="text-white" style="margin: 15px 0;">
            Currently pioneering the intersection of AI and Web3 with Aleem, creating 
            innovative tokenomics for language learning that rewards user progress 
            and engagement.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Web3 Skills
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Blockchain Competencies</h2>', unsafe_allow_html=True)

    skills_categories = [
        {
            "category": "Fundraising & Investment",
            "skills": ["Private Sales", "Tokenomics Design", "Investor Relations", "Pitch Development"],
            "icon": "💰"
        },
        {
            "category": "Platform Development",
            "skills": ["NFT Marketplaces", "DeFi Protocols", "Smart Contracts", "Web3 Integration"],
            "icon": "🔧"
        },
        {
            "category": "Business Strategy",
            "skills": ["Go-to-Market", "Community Building", "Partnership Development", "Regulatory Navigation"],
            "icon": "📈"
        },
        {
            "category": "Innovation",
            "skills": ["AI + Web3", "Social Impact", "Charitable Platforms", "EdTech Integration"],
            "icon": "🚀"
        }
    ]

    cols = st.columns(2)
    for i, category in enumerate(skills_categories):
        with cols[i % 2]:
            st.markdown(f'''
            <div class="achievement-card">
                <div style="text-align: center; margin-bottom: 20px;">
                    <div style="font-size: 3rem;">{category["icon"]}</div>
                    <h3 class="text-gradient">{category["category"]}</h3>
                </div>
            </div>
            ''', unsafe_allow_html=True)
            
            # Skills tags
            for skill in category["skills"]:
                st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'achievements':
    st.markdown('<h1 class="hero-name">Achievements & Impact</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-title">Transforming Ideas into Reality</p>', unsafe_allow_html=True)

    # Key Achievements
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Major Milestones</h2>', unsafe_allow_html=True)

    achievements = [
        {
            "title": "Pioneered First Charitable NFT Marketplace",
            "description": "Created INIP, the world's first NFT marketplace dedicated to charitable causes",
            "impact": "$100K Pre-seed Funding",
            "icon": "🌟"
        },
        {
            "title": "Built Viral EdTech Community",
            "description": "Grew GET ENGLISH to 320K followers with 300M+ views in just one year",
            "impact": "700K+ Downloads",
            "icon": "📈"
        },
        {
            "title": "Secured $1M+ in Web3 Funding",
            "description": "Successfully raised over $1M for Web3 startups in private sales rounds",
            "impact": "Multiple Successful Rounds",
            "icon": "💎"
        },
        {
            "title": "International Business Expansion",
            "description": "Scaled operations across 35+ countries with diverse global client base",
            "impact": "3,000+ Global Clients",
            "icon": "🌍"
        },
        {
            "title": "AI + Web3 Innovation",
            "description": "Pioneering the intersection of AI and blockchain with Aleem platform",
            "impact": "$5M Valuation",
            "icon": "🤖"
        },
        {
            "title": "Entertainment Industry Success",
            "description": "Professional acting career with major studios including Disney and Nickelodeon",
            "impact": "2+ Years Experience",
            "icon": "🎬"
        }
    ]

    cols = st.columns(2)
    for i, achievement in enumerate(achievements):
        with cols[i % 2]:
            st.markdown(f'''
            <div class="achievement-card">
                <div style="display: flex; align-items: start; gap: 20px;">
                    <div style="font-size: 3rem;">{achievement["icon"]}</div>
                    <div style="flex: 1;">
                        <h3 class="text-white">{achievement["title"]}</h3>
                        <p class="text-white" style="margin: 15px 0;">{achievement["description"]}</p>
                        <p class="text-gradient" style="font-weight: 600;">{achievement["impact"]}</p>
                    </div>
                </div>
            </div>
            ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Impact Metrics
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Impact by Numbers</h2>', unsafe_allow_html=True)

    cols = st.columns(4)
    metrics = [
        ("Total Funding", "$1M+", "💰"),
        ("Global Reach", "35+", "🌍"),
        ("Social Impact", "700K+", "👥"),
        ("Years Building", "7", "⏰")
    ]

    for col, (label, value, icon) in zip(cols, metrics):
        with col:
            st.markdown(f'''
            <div class="metric-card glow">
                <div style="font-size: 2.5rem;">{icon}</div>
                <div class="metric-number">{value}</div>
                <div class="metric-label">{label}</div>
            </div>
            ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'analytics':
    st.markdown('<h1 class="hero-name">Growth Analytics</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-title">Data-Driven Success Metrics</p>', unsafe_allow_html=True)

    # Career Growth Chart
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Career Growth Trajectory</h2>', unsafe_allow_html=True)

    # Create timeline data
    years = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    ventures = [0, 0, 0, 0, 1, 1, 2, 2]
    funding = [0, 0, 0, 0, 100, 100, 500, 1000]  # in thousands
    followers = [0, 10, 20, 50, 100, 200, 320, 320]  # in thousands

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=years, y=ventures,
        name='Ventures Founded',
        line=dict(color='#EF4444', width=3),
        marker=dict(size=10)
    ))

    fig.add_trace(go.Scatter(
        x=years, y=funding,
        name='Funding Raised (K$)',
        line=dict(color='#F87171', width=3),
        marker=dict(size=10),
        yaxis='y2'
    ))

    fig.add_trace(go.Scatter(
        x=years, y=followers,
        name='Social Followers (K)',
        line=dict(color='#FCA5A5', width=3),
        marker=dict(size=10),
        yaxis='y3'
    ))

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        height=400,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        yaxis=dict(
            title="Ventures",
            gridcolor='rgba(255,150,150,0.15)'
        ),
        yaxis2=dict(
            title="Funding (K$)",
            overlaying='y',
            side='right',
            gridcolor='rgba(255,150,150,0.15)'
        ),
        yaxis3=dict(
            title="Followers (K)",
            overlaying='y',
            side='right',
            position=0.95,
            gridcolor='rgba(255,150,150,0.15)'
        ),
        xaxis=dict(
            title="Year",
            gridcolor='rgba(255,150,150,0.15)'
        )
    )

    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Business Impact
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Business Impact Distribution</h2>', unsafe_allow_html=True)

    impact_data = pd.DataFrame({
        'Category': ['EdTech', 'Web3/Blockchain', 'Entertainment', 'Social Impact'],
        'Impact Score': [95, 90, 75, 85]
    })

    fig2 = px.bar(impact_data, x='Impact Score', y='Category', orientation='h',
                  color='Impact Score', color_continuous_scale=['#F87171', '#EF4444', '#FCA5A5'])

    fig2.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        height=300,
        showlegend=False,
        xaxis=dict(gridcolor='rgba(255,150,150,0.15)'),
        yaxis=dict(gridcolor='rgba(255,150,150,0.15)')
    )

    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="margin-top: 60px; padding: 30px 0; text-align: center; border-top: 1px solid rgba(255,150,150,0.15);">
    <p class="text-muted">© 2025 Alidar Kuchukov. Building tomorrow's solutions, one startup at a time.</p>
    <div style="margin-top: 15px;">
        <p class="text-muted" style="font-size: 0.9rem;">
            "Mission-driven to create startups and products that solve massive problems for people at scale"
        </p>
    </div>
</div>
""", unsafe_allow_html=True)
