"""
========================================================================================
PROFESSIONAL CV & PORTFOLIO WEB APPLICATION
DINH CAO HUAN – Manager, Credit Card Portfolio Management | ACB Bank
Positioning: Credit Risk | Portfolio Management | Data Analytics | BI | Strategy
========================================================================================
Designed for Streamlit Community Cloud deployment.
Written in clean, modular Python with full responsive styling and embedded risk analytics.
========================================================================================
"""

from __future__ import annotations
import base64
import io
import os
from typing import Any, Dict, List, Optional
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
import streamlit as st

# ======================================================================================
# 1. CENTRALIZED DATA CONFIGURATION (EASY TO CUSTOMIZE WITHOUT TOUCHING UI CODE)
# ======================================================================================

CONFIG: Dict[str, Any] = {
    # ----------------------------- Personal Information -----------------------------
    "personal": {
        "full_name": "DINH CAO HUAN",
        "current_title": "Credit Card Portfolio Management Manager",
        "current_company": "ACB Bank",
        "positioning": "Credit Risk | Portfolio Management | Data Analytics | Business Intelligence | Strategy",
        "tagline": (
            "Senior Banking Professional driving profitable portfolio growth and risk governance "
            "through advanced data analytics, predictive early-warning frameworks, and strategic underwriting."
        ),
        "summary": (
            "Banking and portfolio management professional with over 8 years of retail finance experience, "
            "specializing in Credit Card Portfolio Management, Credit Risk Analytics, and Business Intelligence. "
            "Currently serving as Manager, Credit Card Portfolio Management at ACB Bank, focusing on optimizing portfolio "
            "profitability, risk-return trade-offs, and underwriting strategies. Proven expertise in building end-to-end "
            "automated risk monitoring systems, early warning indicators (FPD/SPD), and regulatory CIC frameworks using "
            "Python, SQL, and advanced BI dashboards. Highly skilled in translating complex portfolio data into proactive credit "
            "policies, controlling delinquency, and driving sustainable retail balance sheet growth."
        ),
        "phone": "0786.29.9683",
        "email": "dinhcaohuan117@gmail.com",
        "location": "Ho Chi Minh City, Vietnam",
        "dob": "1992",
        "gender": "Male",
        "linkedin_url": "https://www.linkedin.com/",  # Replace with direct profile if available
        "drive_cv_url": "https://drive.google.com/uc?export=download&id=1FVs7HDqZzMmCj-ncfDC-l9RoZaHPAXiR",
        "default_photo_url": "https://i.postimg.cc/h4VrcD4x/profile-1a.jpg",
    },

    # ----------------------------- Core Competencies --------------------------------
    "competencies": [
        {
            "category": "Credit Risk",
            "icon": "🛡️",
            "skills": [
                "Credit Risk Management",
                "Credit Risk Analytics",
                "Portfolio Monitoring",
                "Credit Policy",
                "Risk Segmentation",
                "Early Warning (FPD/SPD)",
            ],
        },
        {
            "category": "Portfolio Management",
            "icon": "💳",
            "skills": [
                "Credit Card Portfolio Management",
                "Portfolio Strategy",
                "Customer Segmentation",
                "Portfolio Performance",
                "Campaign Targeting",
                "Limit Management",
            ],
        },
        {
            "category": "Data & BI",
            "icon": "📊",
            "skills": [
                "Data Analytics",
                "Business Intelligence",
                "Dashboard Engineering",
                "Advanced SQL",
                "Python (Pandas, Plotly)",
                "Data Visualization",
            ],
        },
        {
            "category": "Strategy & Governance",
            "icon": "🎯",
            "skills": [
                "Data-driven Strategy",
                "Business Analysis",
                "Customer Targeting",
                "Performance Optimization",
                "Circular 15 CIC Compliance",
                "RCSA / KRI Governance",
            ],
        },
    ],

    # ----------------------------- Work Experience ----------------------------------
    "experience": [
        {
            "position": "Manager, Credit Card Portfolio Management",
            "company": "ACB Bank",
            "period": "Current Role",
            "is_current": True,
            "badge": "Current Position",
            "responsibilities": [
                "Direct the end-to-end portfolio management strategies for ACB's credit card division, aligning risk tolerance with retail asset growth objectives.",
                "Formulate data-driven customer segmentation, limit management, and activation frameworks to optimize portfolio yield and customer lifetime value.",
                "Build dynamic early delinquency surveillance mechanisms and vintage roll-rate monitors to safeguard portfolio asset quality.",
                "Partner with Product Development, Underwriting, and Data Analytics units to drive automated pre-approval policies and risk-based pricing.",
            ],
            "key_achievements": [
                "Spearheaded card portfolio optimization initiatives balancing risk-adjusted return and customer retention.",
                "Strengthened portfolio early warning indicators, maintaining delinquent metrics well within target risk appetite.",
            ],
        },
        {
            "position": "Assistant Manager – Retail Risk, Risk Management",
            "company": "CIMB Bank Vietnam",
            "period": "09/2023 – 06/2025",
            "is_current": False,
            "badge": "Retail Risk",
            "responsibilities": [
                "Automated and enhanced end-to-end credit portfolio and performance reports across multiple consumer lending products.",
                "Developed early warning indicators (First Payment Default - FPD, Second Payment Default - SPD) to strengthen risk detection.",
                "Built and maintained regulatory CIC reporting infrastructure using SQL and Python on Google BigQuery and RStudio in compliance with Circular 15.",
                "Prepared group-level portfolio performance and risk appetite monitoring reports for Senior Management and Board committees.",
                "Partnered closely with Underwriting, Fraud, and Collections departments to execute proactive risk mitigation strategies.",
                "Monitored Key Risk Indicators (KRIs) and ensured operational risk compliance as Departmental Compliance & Operational Risk Officer (DCORO).",
            ],
            "key_achievements": [
                "Automated critical reporting cycles, cutting risk data preparation turnaround time significantly.",
                "Formulated compliant Circular 15 reporting pipelines and robust multi-product early warning tracking.",
            ],
        },
        {
            "position": "Senior Credit Risk Policy Specialist",
            "company": "MOVI VIET NAM",
            "period": "11/2022 – 08/2023",
            "is_current": False,
            "badge": "Risk Policy",
            "responsibilities": [
                "Built automated BI dashboards for real-time risk monitoring across customer segments and financing channels.",
                "Provided data-driven insights and quantitative analyses for continuous credit policy enhancements.",
                "Integrated predictive analytics into automated underwriting rules and fraud detection algorithms.",
            ],
            "key_achievements": [
                "Successfully launched executive risk dashboards enabling daily delinquency monitoring.",
                "Enhanced underwriting cutoff scores to reduce default rates without sacrificing origination volume.",
            ],
        },
        {
            "position": "Senior Credit Risk Policy & Process Specialist",
            "company": "FE CREDIT",
            "period": "05/2022 – 11/2022",
            "is_current": False,
            "badge": "Policy & Process",
            "responsibilities": [
                "Developed and calibrated credit risk policies utilizing data analytics for Point-of-Sale (POS) and E-Commerce lending portfolios.",
                "Monitored portfolio trends and vintage performance curves to trigger timely corrective risk actions.",
                "Collaborated with IT and Operations to embed policy revisions into the core loan origination workflow.",
            ],
            "key_achievements": [
                "Streamlined policy rules for digital e-commerce financing, accelerating approval turnaround.",
                "Established vintage tracking models to detect cohort deterioration at early Month on Book (MOB).",
            ],
        },
        {
            "position": "Senior Credit Card Underwriter",
            "company": "Nam A Bank",
            "period": "05/2017 – 05/2022",
            "is_current": False,
            "badge": "Underwriting",
            "responsibilities": [
                "Managed retail credit card underwriting operations, balancing approval efficiency with stringent risk standards.",
                "Collaborated with Risk and Fraud Prevention teams for early delinquency identification and suspicious file investigations.",
                "Mentored and trained junior underwriters on credit appraisal standards and financial verification.",
                "Contributed front-line operational insights to risk management for continuous credit card policy refinements.",
            ],
            "key_achievements": [
                "Consistently maintained superior underwriting turnaround time while keeping portfolio loss rates below departmental limits.",
                "Coached a team of underwriters in financial statement analysis and credit bureau (CIC) interpretation.",
            ],
        },
    ],

    # ----------------------------- Skill Matrix -------------------------------------
    "skills": {
        "Analytics & Modeling": [
            "Python (Pandas, Plotly, Scikit-learn)",
            "SQL (Advanced Complex Queries & CTEs)",
            "Excel (VBA, Power Query, Advanced Modeling)",
            "Data Analysis & Statistical Modeling",
            "Google BigQuery & Cloud Data Marts",
            "RStudio",
        ],
        "Credit Risk & Governance": [
            "Credit Risk Management & Analytics",
            "Portfolio Risk Monitoring & Early Warning (FPD/SPD)",
            "Credit Policy Design & Cut-off Calibration",
            "Circular 15 CIC Regulatory Compliance",
            "Operational Risk Frameworks (RCSA, LED, KRI)",
            "Vintage & Roll-Rate Cohort Analytics",
        ],
        "Business Intelligence & Reporting": [
            "Automated BI Dashboard Engineering",
            "Interactive Data Visualization",
            "Power BI & Visual Analytics",
            "Executive Reporting & Risk Appetite Metrics",
            "Cohort Delinquency Tracking",
            "ETL Pipeline Conception",
        ],
        "Banking & Portfolio Domain": [
            "Credit Card Portfolio Management",
            "Retail Banking Credit Operations",
            "Credit Card Underwriting & Risk-Based Limits",
            "Unsecured Consumer Loans & POS Financing",
            "Buy Now Pay Later (BNPL) Portfolio Surveillance",
            "Delinquency & NPL Governance",
        ],
    },

    # ----------------------------- Education ----------------------------------------
    "education": [
        {
            "degree": "Bachelor’s Degree in Finance – Banking",
            "institution": "Ho Chi Minh City Open University",
            "period": "09/2022 – 11/2024",
            "details": "Graduated with High Distinction | GPA: 3.49 / 4.00",
        },
        {
            "degree": "Associate’s Degree in Finance – Banking",
            "institution": "HCMC Institute of Applied Science & Technology",
            "period": "10/2010 – 10/2013",
            "details": "Core Foundation in Commercial Banking, Financial Markets & Corporate Credit",
        },
        {
            "degree": "English Proficiency – TOEIC 800 / 990",
            "institution": "IIG Viet Nam",
            "period": "Certified",
            "details": "Professional working proficiency in banking, technical documentation & cross-functional presentations",
        },
    ],

    # ----------------------------- Certifications -----------------------------------
    "certifications": [
        {"year": "2025", "title": "SQL (Advanced)", "issuer": "HackerRank"},
        {"year": "2024", "title": "Human Skills for Managers Professional Certificate", "issuer": "LinkedIn Learning"},
        {"year": "2023", "title": "Credit Risk Management", "issuer": "New York Institute of Finance (NYIF)"},
        {"year": "2023", "title": "Google Data Analytics Professional Certificate", "issuer": "Google"},
        {"year": "2023", "title": "Data Analysis with Python", "issuer": "IBM"},
        {"year": "2022", "title": "Practical Data Analytics with Python", "issuer": "CyberSoft"},
    ],

    # ----------------------------- Professional References --------------------------
    "references": [
        {
            "name": "Chu Nguyên Tú",
            "title": "Vice President – Credit Risk",
            "organization": "CIMB Bank Vietnam",
            "note": "Contact phone/email available upon request",
        },
        {
            "name": "Nguyễn Văn Quỳnh",
            "title": "Senior Underwriting Strategy Manager",
            "organization": "MOVI Vietnam",
            "note": "Contact phone/email available upon request",
        },
        {
            "name": "Đinh Văn Hiệu",
            "title": "Assistant Manager – Risk Management",
            "organization": "CIMB Bank Vietnam",
            "note": "Contact phone/email available upon request",
        },
    ],

    # ----------------------------- Portfolio Projects -------------------------------
    "projects": [
        {
            "id": "credit_risk_dashboard",
            "title": "Interactive Credit Risk Analytics & Portfolio Monitoring Dashboard",
            "category": "Credit Risk & BI Analytics",
            "featured": True,
            "business_problem": (
                "Expanding retail loan portfolios across multi-product lines (Credit Cards, Unsecured Personal Loans, BNPL) "
                "creates operational complexity. Without real-time, cohort-level surveillance, early signs of delinquency roll rates "
                "and underwriting bottlenecks go unnoticed, jeopardizing NPL targets and regulatory capital adequacy."
            ),
            "objective": (
                "Build an interactive executive risk monitoring system that synthesizes $1.25B in portfolio exposures, "
                "delivers automated early warning indicators (FPD/SPD), tracks 12-month NPL trends, and conducts vintage cohort "
                "roll-rate analysis (DPD 30+) to steer underwriting policy refinements."
            ),
            "approach": (
                "1. Data Integration: Unified origination, repayment, and credit bureau (CIC) data into a structured risk mart.\n"
                "2. Dynamic Risk Segmentation: Segmented exposures into 4 risk tiers (Low, Medium, High, Very High) and 3 product categories.\n"
                "3. Diagnostic Diagnostics: Implemented real-time rejection driver decomposition and multi-product credit score distributions.\n"
                "4. Longitudinal Tracking: Modeled vintage curves across disbursement months (M1–M4) over Months on Book (MOB 1–8)."
            ),
            "tools": ["Python", "SQL", "Streamlit", "Plotly", "Google BigQuery"],
            "key_output": (
                "Full-featured interactive risk dashboard tracking portfolio KPIs ($1.25B Outstanding Balance, 3.15% NPL Rate, "
                "642 Avg Score, 42.5% Approval Rate), rejection distributions, and multi-cohort vintage roll-rate curves."
            ),
            "business_impact": (
                "Accelerated credit risk reporting from days to instantaneous monitoring. Enabled risk committees to pinpoint "
                "deteriorating cohorts by MOB 3, prompting timely cut-off tightening on high-risk segments that curbed bad debt formation."
            ),
        },
        {
            "id": "card_limit_strategy",
            "title": "Credit Card Limit Management & Risk-Reward Customer Segmentation",
            "category": "Portfolio Management & Strategy",
            "featured": False,
            "business_problem": (
                "Uniform credit limits lead to under-utilization among affluent low-risk cardholders and heightened exposure among "
                "volatile revolving borrowers, curbing interchange revenue and inflating credit loss provisions."
            ),
            "objective": (
                "Formulate an analytical segmentation model categorizing credit cardholders by risk band and transactional behavior "
                "to execute proactive credit limit adjustments (Line Increases & Decreases)."
            ),
            "approach": (
                "1. Extracted behavioral data on utilization rate, payment-to-balance ratio, and external CIC status.\n"
                "2. Clustered accounts into transactors, revolvers, and dormant segments across risk score deciles.\n"
                "3. Designed automated credit limit increase (CLI) rules for prime revolvers and proactive line decrease triggers."
            ),
            "tools": ["Python", "SQL", "Excel Power Query", "Statistical Clustering"],
            "key_output": (
                "Strategic framework and automated rules engine for ongoing credit card limit management and risk-reward optimization."
            ),
            "business_impact": (
                "Optimized cardholder lifecycle profitability while safeguarding the balance sheet from unexpected credit shocks."
            ),
        },
    ],
}


# ======================================================================================
# 2. STREAMLIT APP CONFIGURATION & EXECUTIVE THEME CSS
# ======================================================================================

st.set_page_config(
    page_title="Dinh Cao Huan | Credit Card Portfolio Management Manager",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def inject_custom_css() -> None:
    """Injects high-end, modern banking and fintech responsive CSS."""
    st.markdown(
        """
        <style>
        /* Import clean modern sans-serif typography */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        /* Root color palette - Executive Banking (Navy, ACB Blue, Slate, Pure Light) */
        :root {
            --bg-primary: #0A192F;
            --bg-surface: #0F2744;
            --bg-card: #132E52;
            --bg-card-hover: #1A3C6B;
            --accent-blue: #2563EB;
            --accent-cyan: #38BDF8;
            --accent-gold: #F59E0B;
            --accent-green: #10B981;
            --accent-red: #EF4444;
            --text-primary: #F8FAFC;
            --text-secondary: #CBD5E1;
            --text-muted: #94A3B8;
            --border-subtle: rgba(148, 163, 184, 0.2);
            --border-glow: rgba(37, 99, 235, 0.4);
            --shadow-card: 0 10px 25px -5px rgba(0, 0, 0, 0.4), 0 8px 10px -6px rgba(0, 0, 0, 0.3);
        }

        /* Base body and canvas styling */
        html, body, [data-testid="stAppViewContainer"] {
            background-color: var(--bg-primary) !important;
            color: var(--text-primary) !important;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
            -webkit-font-smoothing: antialiased;
        }

        /* Top header bar styling */
        [data-testid="stHeader"] {
            background-color: rgba(10, 25, 47, 0.85) !important;
            backdrop-filter: blur(10px) !important;
        }

        /* Streamlit main block container */
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 4rem !important;
            max-width: 1200px !important;
        }

        /* Typography overrides */
        h1, h2, h3, h4, h5, h6 {
            color: var(--text-primary) !important;
            font-weight: 700 !important;
            letter-spacing: -0.02em !important;
        }

        p, li {
            color: var(--text-secondary);
            font-size: 0.95rem;
            line-height: 1.65;
        }

        /* Executive Section Header */
        .section-header-container {
            margin-top: 2.5rem;
            margin-bottom: 1.5rem;
            border-bottom: 1px solid var(--border-subtle);
            padding-bottom: 0.75rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .section-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: #FFFFFF !important;
            display: flex;
            align-items: center;
            gap: 0.6rem;
            margin: 0;
        }
        .section-subtitle {
            font-size: 0.85rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-weight: 600;
        }

        /* Hero Container & Profile Portrait */
        .hero-container {
            background: linear-gradient(135deg, rgba(15, 39, 68, 0.95) 0%, rgba(10, 25, 47, 0.98) 100%);
            border: 1px solid var(--border-subtle);
            border-radius: 20px;
            padding: 2.2rem;
            box-shadow: var(--shadow-card);
            margin-bottom: 2rem;
        }

        .profile-img-styled {
            width: 170px;
            height: 170px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid var(--accent-blue);
            box-shadow: 0 0 25px rgba(37, 99, 235, 0.35);
            display: block;
            margin: 0 auto;
        }

        .badge-current-role {
            display: inline-block;
            background: rgba(37, 99, 235, 0.2);
            color: #60A5FA;
            border: 1px solid rgba(96, 165, 250, 0.4);
            border-radius: 9999px;
            padding: 0.3rem 0.85rem;
            font-size: 0.8rem;
            font-weight: 600;
            letter-spacing: 0.04em;
            margin-bottom: 0.6rem;
        }

        .hero-name {
            font-size: 2.25rem;
            font-weight: 800;
            color: #FFFFFF !important;
            letter-spacing: -0.01em;
            margin: 0.2rem 0;
            line-height: 1.2;
        }

        .hero-title {
            font-size: 1.15rem;
            font-weight: 600;
            color: #93C5FD;
            margin-bottom: 0.4rem;
        }

        .hero-positioning {
            font-size: 0.9rem;
            font-weight: 500;
            color: var(--accent-cyan);
            letter-spacing: 0.03em;
            margin-bottom: 1rem;
        }

        .hero-meta-row {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-bottom: 1.2rem;
        }

        .hero-meta-item {
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }

        /* Executive Cards */
        .exec-card {
            background-color: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: 14px;
            padding: 1.4rem;
            box-shadow: var(--shadow-card);
            transition: transform 0.2s ease, border-color 0.2s ease;
            height: 100%;
        }
        .exec-card:hover {
            transform: translateY(-3px);
            border-color: var(--border-glow);
        }

        /* Core Competency Tag */
        .skill-tag {
            display: inline-block;
            background: rgba(30, 58, 102, 0.7);
            color: #E2E8F0;
            border: 1px solid rgba(148, 163, 184, 0.25);
            border-radius: 8px;
            padding: 0.35rem 0.65rem;
            font-size: 0.82rem;
            font-weight: 500;
            margin: 0.25rem 0.25rem 0.25rem 0;
            transition: all 0.2s ease;
        }
        .skill-tag:hover {
            background: rgba(37, 99, 235, 0.4);
            border-color: #60A5FA;
            color: #FFFFFF;
        }

        /* Work Experience Timeline Card */
        .timeline-card {
            background-color: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-left: 4px solid var(--accent-blue);
            border-radius: 12px;
            padding: 1.4rem;
            margin-bottom: 1.25rem;
            box-shadow: var(--shadow-card);
        }
        .timeline-card.current {
            border-left: 4px solid #38BDF8;
            background: linear-gradient(90deg, rgba(26, 60, 107, 0.35) 0%, rgba(15, 39, 68, 0.8) 100%);
        }
        .timeline-role {
            font-size: 1.1rem;
            font-weight: 700;
            color: #FFFFFF;
            margin: 0;
        }
        .timeline-company {
            font-size: 0.95rem;
            font-weight: 600;
            color: #60A5FA;
            margin-bottom: 0.2rem;
        }
        .timeline-period {
            font-size: 0.8rem;
            color: var(--text-muted);
            font-weight: 500;
            margin-bottom: 0.8rem;
        }

        /* Metric KPI Card */
        .kpi-card {
            background: linear-gradient(135deg, rgba(19, 46, 82, 0.8) 0%, rgba(15, 39, 68, 0.9) 100%);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            padding: 1.2rem;
            text-align: left;
            box-shadow: var(--shadow-card);
        }
        .kpi-title {
            font-size: 0.75rem;
            font-weight: 600;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.06em;
            margin: 0;
        }
        .kpi-value {
            font-size: 1.85rem;
            font-weight: 800;
            color: #FFFFFF;
            margin: 0.25rem 0;
        }
        .kpi-delta {
            font-size: 0.8rem;
            font-weight: 600;
        }
        .delta-positive { color: var(--accent-green); }
        .delta-negative { color: var(--accent-red); }
        .delta-neutral { color: var(--text-muted); }

        /* Project Structured Card */
        .project-card {
            background-color: var(--bg-surface);
            border: 1px solid var(--border-subtle);
            border-radius: 14px;
            padding: 1.6rem;
            margin-bottom: 1.5rem;
            box-shadow: var(--shadow-card);
        }
        .project-badge {
            display: inline-block;
            background: rgba(56, 189, 248, 0.15);
            color: #38BDF8;
            border: 1px solid rgba(56, 189, 248, 0.3);
            border-radius: 6px;
            padding: 0.2rem 0.5rem;
            font-size: 0.75rem;
            font-weight: 600;
            margin-bottom: 0.6rem;
        }

        /* Streamlit Button Tweaks */
        .stButton > button {
            background: #173D7A !important;
            color: #FFFFFF !important;
            border: 1px solid #2E69C4 !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            padding: 0.55rem 1.25rem !important;
            transition: all 0.2s ease !important;
        }
        .stButton > button:hover {
            background: #2563EB !important;
            border-color: #60A5FA !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4) !important;
        }

        /* Streamlit Download Button */
        .stDownloadButton > button {
            background: #10B981 !important;
            color: #FFFFFF !important;
            border: 1px solid #34D399 !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            padding: 0.55rem 1.25rem !important;
            transition: all 0.2s ease !important;
        }
        .stDownloadButton > button:hover {
            background: #059669 !important;
            border-color: #6EE7B7 !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4) !important;
        }

        /* Responsive Mobile Tuning */
        @media (max-width: 768px) {
            .hero-container {
                padding: 1.4rem;
            }
            .profile-img-styled {
                width: 120px;
                height: 120px;
            }
            .hero-name {
                font-size: 1.75rem;
            }
            .hero-title {
                font-size: 1rem;
            }
            .kpi-value {
                font-size: 1.5rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

inject_custom_css()


# ======================================================================================
# 3. HELPER FUNCTIONS (STATE MANAGEMENT, PHOTO & PDF HANDLING)
# ======================================================================================

def init_session_state() -> None:
    """Initializes session state for active navigation, uploaded photo, and uploaded CV."""
    if "nav_page" not in st.session_state:
        st.session_state["nav_page"] = "Overview"
    if "custom_photo_bytes" not in st.session_state:
        st.session_state["custom_photo_bytes"] = None
    if "custom_cv_bytes" not in st.session_state:
        st.session_state["custom_cv_bytes"] = None
    if "custom_cv_name" not in st.session_state:
        st.session_state["custom_cv_name"] = "DinhCaoHuan_CV.pdf"

init_session_state()


def get_profile_photo_data_uri() -> str:
    """Returns a Data URI or URL for the profile photo."""
    # 1. Check if user uploaded a photo in current session
    if st.session_state.get("custom_photo_bytes") is not None:
        b64 = base64.b64encode(st.session_state["custom_photo_bytes"]).decode()
        return f"data:image/jpeg;base64,{b64}"
    
    # 2. Check if a local avatar file exists in repo (e.g., avatar.jpg or profile.jpg)
    for local_name in ["avatar.jpg", "avatar.png", "profile.jpg", "profile.png"]:
        if os.path.exists(local_name):
            try:
                with open(local_name, "rb") as f:
                    b64 = base64.b64encode(f.read()).decode()
                    ext = "png" if local_name.endswith(".png") else "jpeg"
                    return f"data:image/{ext};base64,{b64}"
            except Exception:
                pass
    
    # 3. Fallback to default high-res URL
    return CONFIG["personal"]["default_photo_url"]


def get_cv_pdf_bytes() -> tuple[Optional[bytes], str]:
    """Retrieves CV bytes from session state, local repo, or None (to trigger Drive fallback)."""
    # 1. Session state upload
    if st.session_state.get("custom_cv_bytes") is not None:
        return st.session_state["custom_cv_bytes"], st.session_state.get("custom_cv_name", "DinhCaoHuan_CV.pdf")
    
    # 2. Local repo file cv.pdf or DinhCaoHuan_CV.pdf
    for fname in ["cv.pdf", "DinhCaoHuan_CV.pdf", "CV.pdf"]:
        if os.path.exists(fname):
            try:
                with open(fname, "rb") as f:
                    return f.read(), fname
            except Exception:
                pass
    
    return None, "DinhCaoHuan_CV.pdf"


# ======================================================================================
# 4. TOP EXECUTIVE NAVIGATION BAR
# ======================================================================================

def render_navigation() -> None:
    """Renders a sleek top navigation switcher with clean responsive layout."""
    pages = [
        "Overview",
        "Experience",
        "Competencies & Skills",
        "Portfolio Dashboard",
        "Education & Certs",
        "Contact",
    ]
    
    cols = st.columns([2.5, 5, 2.5])
    with cols[0]:
        st.markdown(
            f"<div style='font-size:1.15rem; font-weight:700; color:#FFFFFF; padding-top:0.4rem;'>"
            f"🏛️ {CONFIG['personal']['full_name']}</div>",
            unsafe_allow_html=True,
        )
    with cols[1]:
        selected = st.radio(
            label="Main Navigation",
            options=pages,
            index=pages.index(st.session_state["nav_page"]) if st.session_state["nav_page"] in pages else 0,
            horizontal=True,
            label_visibility="collapsed",
            key="top_navbar_radio",
        )
        if selected != st.session_state["nav_page"]:
            st.session_state["nav_page"] = selected
            st.rerun()
            
    with cols[2]:
        # Quick access to Drive CV or Direct Download
        cv_bytes, cv_fname = get_cv_pdf_bytes()
        if cv_bytes is not None:
            st.download_button(
                label="📄 Download CV (PDF)",
                data=cv_bytes,
                file_name=cv_fname,
                mime="application/pdf",
                use_container_width=True,
            )
        else:
            st.link_button(
                label="⬇️ Download CV",
                url=CONFIG["personal"]["drive_cv_url"],
                use_container_width=True,
            )

    st.markdown("<div style='margin-bottom: 1.5rem;'></div>", unsafe_allow_html=True)


# ======================================================================================
# 5. SECTION: HERO / EXECUTIVE SUMMARY
# ======================================================================================

def render_hero_section() -> None:
    """Renders the executive Hero section with portrait, current title, positioning, and action buttons."""
    p = CONFIG["personal"]
    photo_uri = get_profile_photo_data_uri()
    
    col_photo, col_info = st.columns([1, 2.8], gap="large")
    
    with col_photo:
        st.markdown(
            f"""
            <div style="text-align: center; padding: 1rem 0;">
                <img src="{photo_uri}" alt="{p['full_name']}" class="profile-img-styled" />
            </div>
            """,
            unsafe_allow_html=True,
        )
        
    with col_info:
        st.markdown(
            f"""
            <div>
                <span class="badge-current-role">⭐ {p['current_company']} • {p['current_title']}</span>
                <h1 class="hero-name">{p['full_name']}</h1>
                <div class="hero-title">{p['current_title']} | {p['current_company']}</div>
                <div class="hero-positioning">{p['positioning']}</div>
                <p style="font-size: 0.95rem; line-height: 1.6; color: #E2E8F0; margin-bottom: 1.2rem;">
                    {p['tagline']}
                </p>
                <div class="hero-meta-row">
                    <div class="hero-meta-item">📞 {p['phone']}</div>
                    <div class="hero-meta-item">📧 {p['email']}</div>
                    <div class="hero-meta-item">📍 {p['location']}</div>
                    <div class="hero-meta-item">👤 {p['gender']} • DOB: {p['dob']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        btn_c1, btn_c2, btn_c3 = st.columns(3)
        with btn_c1:
            cv_bytes, cv_fname = get_cv_pdf_bytes()
            if cv_bytes is not None:
                st.download_button(
                    label="⬇️ Download CV",
                    data=cv_bytes,
                    file_name=cv_fname,
                    mime="application/pdf",
                    use_container_width=True,
                )
            else:
                st.link_button(
                    label="⬇️ Download CV",
                    url=p["drive_cv_url"],
                    use_container_width=True,
                )
        with btn_c2:
            if st.button("📊 View Portfolio", use_container_width=True):
                st.session_state["nav_page"] = "Portfolio Dashboard"
                st.rerun()
        with btn_c3:
            if st.button("✉️ Contact Me", use_container_width=True):
                st.session_state["nav_page"] = "Contact"
                st.rerun()


def render_professional_summary() -> None:
    """Renders the concise 80-120 word executive summary."""
    p = CONFIG["personal"]
    st.markdown(
        """
        <div class="section-header-container">
            <h2 class="section-title">📌 Professional Summary</h2>
            <span class="section-subtitle">Executive Overview</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        f"""
        <div class="exec-card" style="background: rgba(15, 39, 68, 0.85); border-left: 4px solid var(--accent-blue);">
            <p style="font-size: 1.02rem; line-height: 1.75; color: #F1F5F9; margin: 0;">
                {p['summary']}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ======================================================================================
# 6. SECTION: CORE COMPETENCIES
# ======================================================================================

def render_core_competencies() -> None:
    """Renders the 4 core competency pillar cards with structured badges."""
    st.markdown(
        """
        <div class="section-header-container">
            <h2 class="section-title">⚡ Core Competencies</h2>
            <span class="section-subtitle">Pillars of Expertise</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    cols = st.columns(4)
    for i, comp in enumerate(CONFIG["competencies"]):
        with cols[i]:
            tags_html = "".join([f"<span class='skill-tag'>{s}</span>" for s in comp["skills"]])
            st.markdown(
                f"""
                <div class="exec-card">
                    <div style="font-size: 1.6rem; margin-bottom: 0.5rem;">{comp['icon']}</div>
                    <h3 style="font-size: 1.05rem; font-weight: 700; color: #FFFFFF; margin-bottom: 0.8rem;">
                        {comp['category']}
                    </h3>
                    <div>{tags_html}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ======================================================================================
# 7. SECTION: WORK EXPERIENCE
# ======================================================================================

def render_work_experience() -> None:
    """Renders an executive banking timeline highlighting ACB Bank as current role."""
    st.markdown(
        """
        <div class="section-header-container">
            <h2 class="section-title">💼 Professional Experience</h2>
            <span class="section-subtitle">Banking & Risk Management Timeline</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    for exp in CONFIG["experience"]:
        is_cur = exp["is_current"]
        card_class = "timeline-card current" if is_cur else "timeline-card"
        badge_style = "background: #2563EB; color: #FFFFFF;" if is_cur else "background: rgba(148, 163, 184, 0.2); color: #94A3B8;"
        
        resp_list = "".join([f"<li>{r}</li>" for r in exp["responsibilities"]])
        achiev_list = "".join([f"<li>{a}</li>" for a in exp["key_achievements"]])
        
        st.markdown(
            f"""
            <div class="{card_class}">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
                    <div>
                        <h3 class="timeline-role">{exp['position']}</h3>
                        <div class="timeline-company">{exp['company']}</div>
                        <div class="timeline-period">🗓️ {exp['period']}</div>
                    </div>
                    <span style="{badge_style} border-radius: 9999px; padding: 0.25rem 0.75rem; font-size: 0.78rem; font-weight: 600;">
                        {exp['badge']}
                    </span>
                </div>
                <div style="margin-top: 0.8rem;">
                    <div style="font-size: 0.85rem; font-weight: 600; color: #CBD5E1; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.4rem;">
                        Core Responsibilities:
                    </div>
                    <ul style="margin: 0 0 0.8rem 1.2rem; padding: 0;">
                        {resp_list}
                    </ul>
                    <div style="font-size: 0.85rem; font-weight: 600; color: #38BDF8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.4rem;">
                        Key Contributions:
                    </div>
                    <ul style="margin: 0 0 0 1.2rem; padding: 0; color: #94A3B8;">
                        {achiev_list}
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ======================================================================================
# 8. SECTION: SKILLS MATRIX
# ======================================================================================

def render_skills_matrix() -> None:
    """Renders categorized skill cards without subjective progress bars."""
    st.markdown(
        """
        <div class="section-header-container">
            <h2 class="section-title">🧠 Technical & Domain Competencies</h2>
            <span class="section-subtitle">Skill Matrix</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    cols = st.columns(2)
    categories = list(CONFIG["skills"].items())
    
    for idx, (cat_name, skill_items) in enumerate(categories):
        with cols[idx % 2]:
            tags_html = "".join([f"<span class='skill-tag'>{s}</span>" for s in skill_items])
            st.markdown(
                f"""
                <div class="exec-card" style="margin-bottom: 1.2rem;">
                    <h3 style="font-size: 1.05rem; font-weight: 700; color: #60A5FA; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.4rem;">
                        <span>🔹</span> {cat_name}
                    </h3>
                    <div style="line-height: 1.9;">
                        {tags_html}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ======================================================================================
# 9. SECTION: INTERACTIVE PORTFOLIO & CREDIT RISK ANALYTICS DASHBOARD
# ======================================================================================

def render_portfolio_section() -> None:
    """Renders the comprehensive portfolio with the live interactive Credit Risk Analytics Dashboard."""
    st.markdown(
        """
        <div class="section-header-container">
            <h2 class="section-title">📊 Portfolio Projects & Analytical Case Studies</h2>
            <span class="section-subtitle">Real-World Banking Impact</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Showcase Project 1: Credit Risk Analytics Dashboard (Interactive)
    proj1 = CONFIG["projects"][0]
    st.markdown(
        f"""
        <div class="project-card">
            <span class="project-badge">FEATURED CASE STUDY • {proj1['category']}</span>
            <h2 style="font-size: 1.45rem; font-weight: 800; color: #FFFFFF; margin: 0.3rem 0 0.8rem 0;">
                {proj1['title']}
            </h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-bottom: 1.2rem;">
                <div style="background: rgba(10, 25, 47, 0.6); padding: 1rem; border-radius: 10px; border-left: 3px solid #EF4444;">
                    <div style="font-size: 0.8rem; font-weight: 700; color: #FCA5A5; text-transform: uppercase;">1. Business Problem</div>
                    <p style="font-size: 0.88rem; margin: 0.4rem 0 0 0; color: #E2E8F0;">{proj1['business_problem']}</p>
                </div>
                <div style="background: rgba(10, 25, 47, 0.6); padding: 1rem; border-radius: 10px; border-left: 3px solid #38BDF8;">
                    <div style="font-size: 0.8rem; font-weight: 700; color: #BAE6FD; text-transform: uppercase;">2. Objective</div>
                    <p style="font-size: 0.88rem; margin: 0.4rem 0 0 0; color: #E2E8F0;">{proj1['objective']}</p>
                </div>
            </div>
            <div style="background: rgba(10, 25, 47, 0.6); padding: 1rem; border-radius: 10px; border-left: 3px solid #10B981; margin-bottom: 1rem;">
                <div style="font-size: 0.8rem; font-weight: 700; color: #6EE7B7; text-transform: uppercase;">3. Approach & Analytical Methodology</div>
                <p style="font-size: 0.88rem; margin: 0.4rem 0 0 0; white-space: pre-line; color: #E2E8F0;">{proj1['approach']}</p>
            </div>
            <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.2rem;">
                <span style="font-size: 0.8rem; color: #94A3B8; font-weight: 600; align-self: center;">Tools Applied:</span>
                {"".join([f"<span class='skill-tag'>{t}</span>" for t in proj1['tools']])}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ----------------------------- LIVE DASHBOARD TABS -----------------------------
    st.markdown("### 📈 Live Interactive Credit Risk Analytics Dashboard")
    st.caption("Recreated with Plotly & Streamlit based on live portfolio metrics from the original project.")

    tab_overview, tab_segmentation, tab_trends = st.tabs([
        "📊 Portfolio Overview",
        "🔍 Segmentation & Underwriting",
        "📉 Performance & Vintage Trends",
    ])

    # TAB 1: OVERVIEW
    with tab_overview:
        k1, k2, k3, k4 = st.columns(4)
        with k1:
            st.markdown(
                """
                <div class="kpi-card">
                    <div class="kpi-title">Total Outstanding Balance</div>
                    <div class="kpi-value">$1.25 B</div>
                    <div class="kpi-delta delta-positive">▲ +2.5% vs. previous month</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with k2:
            st.markdown(
                """
                <div class="kpi-card">
                    <div class="kpi-title">NPL Rate</div>
                    <div class="kpi-value" style="color: #EF4444;">3.15%</div>
                    <div class="kpi-delta delta-negative">▲ +0.12% vs. previous month</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with k3:
            st.markdown(
                """
                <div class="kpi-card">
                    <div class="kpi-title">Avg. Risk Score</div>
                    <div class="kpi-value">642</div>
                    <div class="kpi-delta delta-positive">▼ -5 points (improved quality)</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with k4:
            st.markdown(
                """
                <div class="kpi-card">
                    <div class="kpi-title">New Loans (Disbursed)</div>
                    <div class="kpi-value">1,820</div>
                    <div class="kpi-delta delta-neutral">Current Month Originations</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("<div style='margin-bottom: 1.5rem;'></div>", unsafe_allow_html=True)
        c_chart1, c_chart2 = st.columns([1.6, 1.2])

        with c_chart1:
            # Bar Chart: Outstanding Balance by Risk Level
            risk_labels = ["Low Risk", "Medium Risk", "High Risk", "Very High Risk"]
            risk_balances = [500, 450, 200, 100]  # USD Millions
            colors = ["#10B981", "#F59E0B", "#F97316", "#EF4444"]
            
            fig_bar = go.Figure(
                data=[
                    go.Bar(
                        x=risk_labels,
                        y=risk_balances,
                        marker_color=colors,
                        text=[f"${v}M" for v in risk_balances],
                        textposition="auto",
                    )
                ]
            )
            fig_bar.update_layout(
                title=dict(text="Outstanding Balance by Risk Level (USD Millions)", font=dict(color="#FFFFFF", size=14)),
                paper_bgcolor="rgba(15, 39, 68, 0.8)",
                plot_bgcolor="rgba(15, 39, 68, 0.8)",
                font=dict(color="#94A3B8"),
                height=340,
                margin=dict(l=20, r=20, t=50, b=20),
                yaxis=dict(gridcolor="rgba(255, 255, 255, 0.1)", title="Balance (USD M)"),
                xaxis=dict(gridcolor="rgba(0, 0, 0, 0)"),
            )
            st.plotly_chart(fig_bar, use_container_width=True)

        with c_chart2:
            # Donut Chart: Risk Distribution
            donut_labels = ["Low Risk", "Medium Risk", "High / Very High"]
            donut_values = [45, 35, 20]
            donut_colors = ["#10B981", "#F59E0B", "#EF4444"]

            fig_donut = go.Figure(
                data=[
                    go.Pie(
                        labels=donut_labels,
                        values=donut_values,
                        hole=0.6,
                        marker=dict(colors=donut_colors),
                        textinfo="label+percent",
                        textfont=dict(color="#FFFFFF"),
                    )
                ]
            )
            fig_donut.update_layout(
                title=dict(text="Portfolio Risk Share (%)", font=dict(color="#FFFFFF", size=14)),
                paper_bgcolor="rgba(15, 39, 68, 0.8)",
                plot_bgcolor="rgba(15, 39, 68, 0.8)",
                font=dict(color="#94A3B8"),
                height=340,
                margin=dict(l=20, r=20, t=50, b=20),
                showlegend=False,
            )
            st.plotly_chart(fig_donut, use_container_width=True)

    # TAB 2: SEGMENTATION & UNDERWRITING
    with tab_segmentation:
        s1, s2 = st.columns(2)
        with s1:
            st.markdown(
                """
                <div class="kpi-card">
                    <div class="kpi-title">Approval Rate</div>
                    <div class="kpi-value">42.5%</div>
                    <div class="kpi-delta delta-positive">▲ +1.2% vs. previous month</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with s2:
            st.markdown(
                """
                <div class="kpi-card">
                    <div class="kpi-title">Payment Default Rate</div>
                    <div class="kpi-value" style="color: #EF4444;">4.8%</div>
                    <div class="kpi-delta delta-negative">Target: &lt; 4.5% (Requires Policy Attention)</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("<div style='margin-bottom: 1rem;'></div>", unsafe_allow_html=True)
        
        # Product filter
        prod_filter = st.radio(
            "Filter Analysis by Lending Product:",
            ["All Products", "Unsecured Loan", "Credit Card", "BNPL"],
            horizontal=True,
        )

        reject_data_dict = {
            "All Products": {
                "labels": ["Low Credit Score", "Insufficient Income", "Incomplete Application", "CIC Bad Debt", "Other"],
                "data": [40, 25, 15, 10, 10],
            },
            "Unsecured Loan": {
                "labels": ["Insufficient Income", "Low Credit Score", "CIC Bad Debt", "Application", "Other"],
                "data": [50, 20, 15, 10, 5],
            },
            "Credit Card": {
                "labels": ["Low Credit Score", "High Limit Request", "Existing Debt Threshold", "Income", "Other"],
                "data": [40, 20, 20, 15, 5],
            },
            "BNPL": {
                "labels": ["Incomplete Application", "Low Credit Score", "Unable to Verify Identity", "Other"],
                "data": [50, 30, 15, 5],
            },
        }

        col_rej, col_score = st.columns(2)

        with col_rej:
            cur_rej = reject_data_dict[prod_filter]
            fig_rej = go.Figure(
                data=[
                    go.Pie(
                        labels=cur_rej["labels"],
                        values=cur_rej["data"],
                        hole=0.55,
                        textinfo="label+percent",
                        marker=dict(colors=["#EF4444", "#F97316", "#F59E0B", "#8B5CF6", "#64748B"]),
                    )
                ]
            )
            fig_rej.update_layout(
                title=dict(text=f"Reject Reason Analysis ({prod_filter})", font=dict(color="#FFFFFF", size=14)),
                paper_bgcolor="rgba(15, 39, 68, 0.8)",
                plot_bgcolor="rgba(15, 39, 68, 0.8)",
                font=dict(color="#94A3B8"),
                height=350,
                margin=dict(l=20, r=20, t=50, b=20),
                legend=dict(orientation="h", y=-0.2),
            )
            st.plotly_chart(fig_rej, use_container_width=True)

        with col_score:
            score_bins = ["<500", "500-550", "550-600", "600-650", "650-700", "700-750", ">750"]
            fig_score = go.Figure()

            if prod_filter in ["All Products", "Unsecured Loan"]:
                fig_score.add_trace(
                    go.Scatter(
                        x=score_bins,
                        y=[10, 20, 40, 80, 50, 20, 10],
                        mode="lines+markers",
                        name="Unsecured Loan",
                        line=dict(color="#3B82F6", width=2.5),
                        fill="tozeroy",
                        fillcolor="rgba(59, 130, 246, 0.1)",
                    )
                )
            if prod_filter in ["All Products", "Credit Card"]:
                fig_score.add_trace(
                    go.Scatter(
                        x=score_bins,
                        y=[5, 15, 30, 60, 70, 40, 20],
                        mode="lines+markers",
                        name="Credit Card",
                        line=dict(color="#10B981", width=2.5),
                        fill="tozeroy",
                        fillcolor="rgba(16, 185, 129, 0.1)",
                    )
                )
            if prod_filter in ["All Products", "BNPL"]:
                fig_score.add_trace(
                    go.Scatter(
                        x=score_bins,
                        y=[30, 50, 60, 40, 20, 10, 5],
                        mode="lines+markers",
                        name="BNPL",
                        line=dict(color="#F59E0B", width=2.5),
                        fill="tozeroy",
                        fillcolor="rgba(245, 158, 11, 0.1)",
                    )
                )

            fig_score.update_layout(
                title=dict(text=f"Score Distribution ({prod_filter})", font=dict(color="#FFFFFF", size=14)),
                paper_bgcolor="rgba(15, 39, 68, 0.8)",
                plot_bgcolor="rgba(15, 39, 68, 0.8)",
                font=dict(color="#94A3B8"),
                height=350,
                margin=dict(l=20, r=20, t=50, b=20),
                yaxis=dict(gridcolor="rgba(255, 255, 255, 0.1)", title="Volume of Applications"),
                xaxis=dict(gridcolor="rgba(0, 0, 0, 0)", title="Credit Score Deciles"),
                legend=dict(orientation="h", y=-0.2),
            )
            st.plotly_chart(fig_score, use_container_width=True)

    # TAB 3: TRENDS & VINTAGE
    with tab_trends:
        months = [f"M{i}" for i in range(1, 13)]
        npl_vals = [2.8, 2.9, 3.0, 2.8, 3.1, 3.3, 3.4, 3.2, 3.0, 3.1, 3.2, 3.15]

        col_t1, col_t2 = st.columns(2)

        with col_t1:
            fig_npl = go.Figure()
            fig_npl.add_trace(
                go.Scatter(
                    x=months,
                    y=npl_vals,
                    mode="lines+markers",
                    name="NPL Rate (%)",
                    line=dict(color="#EF4444", width=3),
                    fill="tozeroy",
                    fillcolor="rgba(239, 68, 68, 0.12)",
                )
            )
            fig_npl.add_hline(y=3.0, line_dash="dash", line_color="#F59E0B", annotation_text="Internal Threshold 3.0%")
            fig_npl.update_layout(
                title=dict(text="12-Month Historical NPL Rate (%)", font=dict(color="#FFFFFF", size=14)),
                paper_bgcolor="rgba(15, 39, 68, 0.8)",
                plot_bgcolor="rgba(15, 39, 68, 0.8)",
                font=dict(color="#94A3B8"),
                height=360,
                margin=dict(l=20, r=20, t=50, b=20),
                yaxis=dict(gridcolor="rgba(255, 255, 255, 0.1)", title="NPL %"),
                xaxis=dict(gridcolor="rgba(0, 0, 0, 0)"),
            )
            st.plotly_chart(fig_npl, use_container_width=True)

        with col_t2:
            mobs = [f"MOB {i}" for i in range(1, 9)]
            fig_vint = go.Figure()
            fig_vint.add_trace(go.Scatter(x=mobs, y=[0.5, 0.8, 1.2, 1.5, 1.9, 2.1, 2.2, 2.3], name="Cohort M1/2024", line=dict(color="#EF4444", width=2)))
            fig_vint.add_trace(go.Scatter(x=mobs[:7], y=[0.4, 0.7, 1.1, 1.4, 1.8, 2.0, 2.1], name="Cohort M2/2024", line=dict(color="#F97316", width=2)))
            fig_vint.add_trace(go.Scatter(x=mobs[:6], y=[0.6, 0.9, 1.3, 1.7, 2.0, 2.2], name="Cohort M3/2024", line=dict(color="#F59E0B", width=2)))
            fig_vint.add_trace(go.Scatter(x=mobs[:5], y=[0.5, 0.8, 1.2, 1.6, 1.9], name="Cohort M4/2024", line=dict(color="#3B82F6", width=2)))

            fig_vint.update_layout(
                title=dict(text="Vintage Analysis: Roll Rate by DPD 30+ (% by MOB)", font=dict(color="#FFFFFF", size=14)),
                paper_bgcolor="rgba(15, 39, 68, 0.8)",
                plot_bgcolor="rgba(15, 39, 68, 0.8)",
                font=dict(color="#94A3B8"),
                height=360,
                margin=dict(l=20, r=20, t=50, b=20),
                yaxis=dict(gridcolor="rgba(255, 255, 255, 0.1)", title="DPD 30+ Rate (%)"),
                xaxis=dict(gridcolor="rgba(0, 0, 0, 0)", title="Month on Book (MOB)"),
                legend=dict(orientation="h", y=-0.25),
            )
            st.plotly_chart(fig_vint, use_container_width=True)

    # Key Output & Business Impact of Project 1
    st.markdown(
        f"""
        <div style="background: rgba(15, 39, 68, 0.8); border: 1px solid var(--border-subtle); border-radius: 12px; padding: 1.2rem; margin-top: 1.2rem;">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;">
                <div>
                    <span style="font-size: 0.8rem; font-weight: 700; color: #60A5FA; text-transform: uppercase;">Key Output</span>
                    <p style="font-size: 0.88rem; color: #E2E8F0; margin: 0.3rem 0 0 0;">{proj1['key_output']}</p>
                </div>
                <div>
                    <span style="font-size: 0.8rem; font-weight: 700; color: #10B981; text-transform: uppercase;">Strategic Business Impact</span>
                    <p style="font-size: 0.88rem; color: #E2E8F0; margin: 0.3rem 0 0 0;">{proj1['business_impact']}</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)

    # Showcase Project 2: Card Limit Optimization & Customer Segmentation
    proj2 = CONFIG["projects"][1]
    st.markdown(
        f"""
        <div class="project-card">
            <span class="project-badge">STRATEGIC MODEL • {proj2['category']}</span>
            <h2 style="font-size: 1.45rem; font-weight: 800; color: #FFFFFF; margin: 0.3rem 0 0.8rem 0;">
                {proj2['title']}
            </h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-bottom: 1.2rem;">
                <div style="background: rgba(10, 25, 47, 0.6); padding: 1rem; border-radius: 10px; border-left: 3px solid #EF4444;">
                    <div style="font-size: 0.8rem; font-weight: 700; color: #FCA5A5; text-transform: uppercase;">1. Business Problem</div>
                    <p style="font-size: 0.88rem; margin: 0.4rem 0 0 0; color: #E2E8F0;">{proj2['business_problem']}</p>
                </div>
                <div style="background: rgba(10, 25, 47, 0.6); padding: 1rem; border-radius: 10px; border-left: 3px solid #38BDF8;">
                    <div style="font-size: 0.8rem; font-weight: 700; color: #BAE6FD; text-transform: uppercase;">2. Objective</div>
                    <p style="font-size: 0.88rem; margin: 0.4rem 0 0 0; color: #E2E8F0;">{proj2['objective']}</p>
                </div>
            </div>
            <div style="background: rgba(10, 25, 47, 0.6); padding: 1rem; border-radius: 10px; border-left: 3px solid #10B981; margin-bottom: 1rem;">
                <div style="font-size: 0.8rem; font-weight: 700; color: #6EE7B7; text-transform: uppercase;">3. Strategic Approach</div>
                <p style="font-size: 0.88rem; margin: 0.4rem 0 0 0; white-space: pre-line; color: #E2E8F0;">{proj2['approach']}</p>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem;">
                <div>
                    <span style="font-size: 0.8rem; font-weight: 700; color: #60A5FA; text-transform: uppercase;">Key Output</span>
                    <p style="font-size: 0.88rem; color: #E2E8F0; margin: 0.3rem 0 0 0;">{proj2['key_output']}</p>
                </div>
                <div>
                    <span style="font-size: 0.8rem; font-weight: 700; color: #10B981; text-transform: uppercase;">Business Impact</span>
                    <p style="font-size: 0.88rem; color: #E2E8F0; margin: 0.3rem 0 0 0;">{proj2['business_impact']}</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ======================================================================================
# 10. SECTION: EDUCATION, CERTIFICATIONS & REFERENCES
# ======================================================================================

def render_education_and_certifications() -> None:
    """Renders education credentials, professional certifications, and references."""
    col_edu, col_cert = st.columns(2, gap="large")

    with col_edu:
        st.markdown(
            """
            <div class="section-header-container" style="margin-top: 0;">
                <h2 class="section-title">🎓 Education</h2>
                <span class="section-subtitle">Academic Credentials</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        for edu in CONFIG["education"]:
            st.markdown(
                f"""
                <div class="exec-card" style="margin-bottom: 1rem;">
                    <div style="font-size: 0.78rem; font-weight: 600; color: #38BDF8; text-transform: uppercase;">{edu['period']}</div>
                    <h3 style="font-size: 1.05rem; font-weight: 700; color: #FFFFFF; margin: 0.2rem 0;">{edu['degree']}</h3>
                    <div style="font-size: 0.9rem; font-weight: 600; color: #60A5FA; margin-bottom: 0.4rem;">{edu['institution']}</div>
                    <p style="font-size: 0.85rem; color: #CBD5E1; margin: 0;">{edu['details']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with col_cert:
        st.markdown(
            """
            <div class="section-header-container" style="margin-top: 0;">
                <h2 class="section-title">📜 Certifications</h2>
                <span class="section-subtitle">Accreditations</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        for cert in CONFIG["certifications"]:
            st.markdown(
                f"""
                <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 0.75rem 1rem; margin-bottom: 0.6rem; display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <div style="font-weight: 600; color: #FFFFFF; font-size: 0.92rem;">{cert['title']}</div>
                        <div style="font-size: 0.8rem; color: #94A3B8;">{cert['issuer']}</div>
                    </div>
                    <span style="background: rgba(37, 99, 235, 0.2); color: #60A5FA; border: 1px solid rgba(37, 99, 235, 0.4); border-radius: 6px; padding: 0.2rem 0.5rem; font-size: 0.75rem; font-weight: 700;">
                        {cert['year']}
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # Professional References section
    st.markdown(
        """
        <div class="section-header-container">
            <h2 class="section-title">🤝 Professional References</h2>
            <span class="section-subtitle">Direct Endorsements</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    r_cols = st.columns(3)
    for i, ref in enumerate(CONFIG["references"]):
        with r_cols[i]:
            st.markdown(
                f"""
                <div class="exec-card">
                    <h3 style="font-size: 1.05rem; font-weight: 700; color: #FFFFFF; margin-bottom: 0.2rem;">{ref['name']}</h3>
                    <div style="font-size: 0.88rem; font-weight: 600; color: #60A5FA;">{ref['title']}</div>
                    <div style="font-size: 0.82rem; color: #94A3B8; margin-bottom: 0.5rem;">{ref['organization']}</div>
                    <p style="font-size: 0.78rem; color: var(--accent-cyan); margin: 0;">📞 {ref['note']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ======================================================================================
# 11. SECTION: CONTACT & ADMIN CONFIGURATION PANEL
# ======================================================================================

def render_contact_and_admin() -> None:
    """Renders contact details, CV download options, and an isolated administrative panel for uploads."""
    p = CONFIG["personal"]
    
    st.markdown(
        """
        <div class="section-header-container">
            <h2 class="section-title">📬 Contact & Professional Inquiries</h2>
            <span class="section-subtitle">Get in Touch</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    c_info, c_action = st.columns([1.5, 1.2], gap="large")
    with c_info:
        st.markdown(
            f"""
            <div class="exec-card">
                <h3 style="font-size: 1.15rem; font-weight: 700; color: #FFFFFF; margin-bottom: 1rem;">
                    Let's Connect
                </h3>
                <p style="color: #CBD5E1; margin-bottom: 1.2rem;">
                    Open to professional discussions on retail portfolio strategy, credit card risk policy, 
                    and advanced risk analytics leadership.
                </p>
                <div style="display: flex; flex-direction: column; gap: 0.85rem; font-size: 0.95rem;">
                    <div><strong>👤 Name:</strong> {p['full_name']}</div>
                    <div><strong>💼 Current Role:</strong> {p['current_title']} ({p['current_company']})</div>
                    <div><strong>📧 Email:</strong> <a href="mailto:{p['email']}" style="color: #60A5FA; text-decoration: none;">{p['email']}</a></div>
                    <div><strong>📞 Phone:</strong> <a href="tel:{p['phone'].replace('.', '')}" style="color: #60A5FA; text-decoration: none;">{p['phone']}</a></div>
                    <div><strong>📍 Location:</strong> {p['location']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c_action:
        st.markdown(
            """
            <div class="exec-card">
                <h3 style="font-size: 1.15rem; font-weight: 700; color: #FFFFFF; margin-bottom: 0.8rem;">
                    Curriculum Vitae
                </h3>
                <p style="font-size: 0.88rem; color: #94A3B8; margin-bottom: 1.2rem;">
                    Download a comprehensive offline copy of my professional banking CV in PDF format.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        cv_bytes, cv_fname = get_cv_pdf_bytes()
        if cv_bytes is not None:
            st.download_button(
                label=f"⬇️ Download {cv_fname}",
                data=cv_bytes,
                file_name=cv_fname,
                mime="application/pdf",
                use_container_width=True,
            )
        else:
            st.link_button(
                label="⬇️ Download CV (Google Drive Direct)",
                url=p["drive_cv_url"],
                use_container_width=True,
            )

    # ----------------------------- ADMIN CONFIGURATION AREA -----------------------------
    st.markdown("<div style='margin-top: 3rem;'></div>", unsafe_allow_html=True)
    with st.expander("⚙️ Admin Settings: Upload Profile Photo & Custom CV PDF", expanded=False):
        st.info(
            "💡 **Streamlit Cloud Persistence Notice:** File uploads in this panel are held in session memory for live preview. "
            "To make your photo or CV permanent on Streamlit Community Cloud without re-uploading, place `avatar.jpg` and `cv.pdf` "
            "directly in your GitHub repository root, or edit the `CONFIG` dictionary at the top of `app.py`."
        )

        col_up_photo, col_up_cv = st.columns(2, gap="large")

        with col_up_photo:
            st.markdown("#### 1. Upload Profile Photo")
            uploaded_img = st.file_uploader(
                "Choose portrait image (JPG, PNG, WEBP):",
                type=["jpg", "jpeg", "png", "webp"],
                key="admin_photo_uploader",
            )
            if uploaded_img is not None:
                try:
                    img_bytes = uploaded_img.read()
                    # Validate image with Pillow
                    Image.open(io.BytesIO(img_bytes)).verify()
                    st.session_state["custom_photo_bytes"] = img_bytes
                    st.success("✅ Profile photo successfully updated for this session!")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Invalid image file: {e}")

            if st.session_state.get("custom_photo_bytes") is not None:
                if st.button("Reset to Default Photo"):
                    st.session_state["custom_photo_bytes"] = None
                    st.rerun()

        with col_up_cv:
            st.markdown("#### 2. Upload Custom CV (PDF Only)")
            uploaded_pdf = st.file_uploader(
                "Choose CV file (.pdf only):",
                type=["pdf"],
                key="admin_cv_uploader",
            )
            if uploaded_pdf is not None:
                if not uploaded_pdf.name.lower().endswith(".pdf"):
                    st.error("❌ Only PDF files (.pdf) are permitted.")
                else:
                    pdf_bytes = uploaded_pdf.read()
                    st.session_state["custom_cv_bytes"] = pdf_bytes
                    st.session_state["custom_cv_name"] = uploaded_pdf.name
                    st.success(f"✅ CV '{uploaded_pdf.name}' loaded successfully!")
                    st.rerun()

            if st.session_state.get("custom_cv_bytes") is not None:
                if st.button("Reset to Default CV"):
                    st.session_state["custom_cv_bytes"] = None
                    st.session_state["custom_cv_name"] = "DinhCaoHuan_CV.pdf"
                    st.rerun()

        # PDF Live Preview if available
        current_cv_bytes, current_cv_name = get_cv_pdf_bytes()
        if current_cv_bytes is not None:
            st.markdown(f"#### 📄 PDF Preview: {current_cv_name}")
            try:
                base64_pdf = base64.b64encode(current_cv_bytes).decode("utf-8")
                pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf" style="border-radius:12px; border:1px solid rgba(148, 163, 184, 0.3);"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)
            except Exception as e:
                st.warning(f"Could not render inline PDF preview: {e}")


# ======================================================================================
# 12. MAIN APP ROUTER & ORCHESTRATION
# ======================================================================================

def main() -> None:
    """Main application orchestrator."""
    # Top navigation
    render_navigation()

    # Hero & Core Info (always visible at top of page or overview)
    render_hero_section()

    current_page = st.session_state.get("nav_page", "Overview")

    if current_page == "Overview":
        render_professional_summary()
        render_core_competencies()
        st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)
        render_work_experience()
        st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)
        render_skills_matrix()
        st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)
        render_portfolio_section()
        st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)
        render_education_and_certifications()
        st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)
        render_contact_and_admin()

    elif current_page == "Experience":
        render_work_experience()

    elif current_page == "Competencies & Skills":
        render_core_competencies()
        st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)
        render_skills_matrix()

    elif current_page == "Portfolio Dashboard":
        render_portfolio_section()

    elif current_page == "Education & Certs":
        render_education_and_certifications()

    elif current_page == "Contact":
        render_contact_and_admin()

    # Footer
    st.markdown(
        f"""
        <div style="text-align: center; color: var(--text-muted); font-size: 0.8rem; margin-top: 4rem; padding-top: 1.5rem; border-top: 1px solid var(--border-subtle);">
            © 2026 {CONFIG['personal']['full_name']} • {CONFIG['personal']['current_title']} • {CONFIG['personal']['current_company']}<br>
            Professional CV & Portfolio built with Python & Streamlit
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
