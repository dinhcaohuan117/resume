# Professional Banking & Risk Management CV Portfolio
### DINH CAO HUAN — Credit Card Portfolio Management Manager | ACB Bank
**Positioning:** Credit Risk | Portfolio Management | Data Analytics | Business Intelligence | Strategy

---

## 1. Project Overview

This repository contains the production-ready code for the executive CV & Portfolio website of **Dinh Cao Huan**, Manager of Credit Card Portfolio Management at **ACB Bank**.

The application is tailored for Senior/Middle-Senior Banking, Risk Management, and Analytics professionals. Designed with a modern, high-contrast Banking/FinTech design system, it showcases:
- **Professional Positioning:** Highlighting the intersection of Credit Risk Governance, Credit Card Portfolio Management, and Advanced Data Analytics.
- **Career Trajectory:** Complete, unembellished banking experience across ACB Bank, CIMB Bank Vietnam, MOVI, FE CREDIT, and Nam A Bank.
- **Embedded Interactive Portfolio:** A full live simulation of the *Credit Risk Analytics Dashboard*, complete with multi-product filtering, KPI metric cards, reject reason analysis, and vintage cohort roll-rate curves (DPD 30+).
- **Recruiter Experience:** One-click CV downloading (PDF), responsive desktop/mobile layouts, and clean executive summaries.

Built natively in **Python** using **Streamlit** and **Plotly**, the application runs seamlessly on **Streamlit Community Cloud** with zero external server dependencies.

---

## 2. Features & Recent Upgrades

- **Executive Hero & Branding:**
  - High-resolution executive portrait embedded directly into the application with calibrated framing and centering (`object-position: center 15%`).
  - Clean layout without redundant text banners or upload popovers.
  - Prominent positioning badges for current role at ACB Bank.
- **Streamlined Action Buttons (No Redundancy):**
  - **⬇️ Tải CV (PDF):** Downloads active CV (uploaded, local repository file, or Google Drive direct fallback).
  - **📤 Cập nhật CV (PDF):** Dedicated button opening an instant uploader to replace the CV file (.pdf only) with automatic validation and preview.
  - **📊 Xem Portfolio:** Fully functional reactive button that jumps directly to the Portfolio Dashboard.
  - **✉️ Liên hệ:** Fully functional reactive button that jumps directly to the Contact section.
- **100% Modern Button Navigation (No Radio Buttons):**
  - Main top navigation has been upgraded from `st.radio` to modern, responsive buttons (`primary` active highlight).
  - Portfolio Dashboard product filter (`All Products`, `Unsecured Loan`, `Credit Card`, `BNPL`) now uses styled button toggles.
- **Structured Experience Timeline:**
  - Features current position at ACB Bank with a distinct visual badge.
  - Details historical roles with bulleted responsibilities and key quantitative contributions.
- **Interactive Credit Risk Analytics Dashboard:**
  - **Portfolio Overview:** Real-time KPI cards ($1.25B Outstanding Balance, 3.15% NPL, 642 Avg Score, 1,820 New Loans), Outstanding Balance by Risk Grade (Bar Chart), and Risk Share Donut.
  - **Segmentation & Underwriting:** Dynamic Product Filter (`All Products`, `Unsecured Loan`, `Credit Card`, `BNPL`), Approval Rate (42.5%), Default Rate (4.8%), Dynamic Reject Reason Donut, and Credit Score Distribution Curves.
  - **Performance & Trends:** 12-Month NPL Rate curve with 3.0% internal appetite threshold, and Vintage Analysis tracking DPD 30+ roll rates across Cohorts M1–M4 over MOB 1–8.
  - **Strategic Portfolio Case Study 2:** Credit Card Limit Management & Risk-Reward Customer Segmentation.
- **Skill Matrix:** Categorized competencies (Analytics & Modeling, Credit Risk & Governance, BI & Reporting, Banking Domain) without subjective progress bars.
- **Education, Certifications & References:**
  - Bachelor’s Degree in Finance–Banking (GPA 3.49/4.00, HCMC Open University), Associate's Degree, TOEIC 800/990.
  - Professional certifications from HackerRank (SQL Advanced), NYIF, Google, IBM, CyberSoft, and LinkedIn Learning.
  - Direct banking executive references.

---

## 3. Project Structure

The project strictly follows the minimalist 3-file structure for straightforward deployment:

```text
/
├── app.py             # Complete application code (Data Configuration, Theme CSS, UI & Analytics)
├── requirements.txt   # Minimal, production-stable Python dependencies
└── README.md          # Full setup, customization, and deployment documentation
```

---

## 4. Local Installation

Ensure you have **Python 3.10+** installed on your system.

1. Clone or download the repository to your local machine:
   ```bash
   git clone <YOUR_REPOSITORY_URL>
   cd <REPOSITORY_FOLDER>
   ```

2. (Recommended) Create and activate a virtual environment:
   - On Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 5. Run Locally

Launch the Streamlit app with:

```bash
streamlit run app.py
```

Streamlit will start the local server and open your default browser at:
`http://localhost:8501`

---

## 6. Deploy to GitHub

To push your project to a new GitHub repository:

```bash
# 1. Initialize git
git init

# 2. Add all 3 files
git add .

# 3. Create initial commit
git commit -m "Initial CV Portfolio for Dinh Cao Huan"

# 4. Set main branch
git branch -M main

# 5. Link remote repository (replace with your actual GitHub URL)
git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY_NAME>.git

# 6. Push to GitHub
git push -u origin main
```

---

## 7. Deploy to Streamlit Community Cloud

Deploying your portfolio to Streamlit Community Cloud is 100% free and takes less than 2 minutes:

1. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
2. Click **New app**.
3. Select your repository: `<YOUR_USERNAME>/<YOUR_REPOSITORY_NAME>`.
4. Select branch: `main`.
5. Specify Main file path: `app.py`.
6. Click **Deploy!**

Your live executive portfolio will be active worldwide at `https://<YOUR_CUSTOM_SUBDOMAIN>.streamlit.app`.

---

## 8. How to Replace Profile Photo

You have two methods to update your profile photo:

### Method A: Permanent Update via GitHub Repository (Recommended)
1. Name your desired professional photo `avatar.jpg` (or `avatar.png`).
2. Place this image in the root directory of your project (alongside `app.py`).
3. Commit and push to GitHub:
   ```bash
   git add avatar.jpg
   git commit -m "Update profile portrait"
   git push
   ```
   The app automatically detects local avatar files first and renders them in high resolution!

### Method B: In-App Direct Button
Click the **"📷 Thay đổi ảnh profile"** button located directly beneath your photo in the Hero section. Select your new image (`.jpg`, `.png`, `.webp`) and the app will update it immediately for the current session.

### Method C: Update via Hosted Image URL
Open `app.py`, locate the `CONFIG["personal"]["default_photo_url"]` entry (around line 53), and paste your direct image link.

---

## 9. How to Replace CV PDF

### Method A: Permanent CV in Repository (Recommended)
1. Save your CV file as `cv.pdf` (or `DinhCaoHuan_CV.pdf`).
2. Place `cv.pdf` in the root folder of your project.
3. Commit and push:
   ```bash
   git add cv.pdf
   git commit -m "Update official CV PDF"
   git push
   ```
   The "Tải CV (PDF)" buttons will immediately serve this local PDF file directly.

### Method B: In-App Direct Button
Click the **"📤 Cập nhật CV (PDF)"** button in the Hero section action bar or Contact page, upload your new `.pdf` file, and download or preview it immediately.

### Method C: Update Google Drive Direct Download Link
Open `app.py` and modify `CONFIG["personal"]["drive_cv_url"]` (around line 52) with your Google Drive download link.

---

## 10. Customization Guide

All data and content are isolated inside the `CONFIG` dictionary at the top of `app.py` (lines 26–347). You do not need to touch any HTML, CSS, or Streamlit rendering logic to update your portfolio:

| Item | Location in `app.py` | Description |
| :--- | :--- | :--- |
| **Personal Info & Title** | `CONFIG["personal"]` | Full name, current position, company, positioning tagline, phone, email, location. |
| **Executive Summary** | `CONFIG["personal"]["summary"]` | The 80–120 word banking executive summary. |
| **Core Competencies** | `CONFIG["competencies"]` | The 4 competency pillars (Credit Risk, Portfolio Management, Data & BI, Strategy). |
| **Work Experience** | `CONFIG["experience"]` | Ordered list of roles, companies, dates, responsibilities, and achievements. ACB Bank is set with `"is_current": True`. |
| **Skills Matrix** | `CONFIG["skills"]` | Grouped skill sets (Analytics, Credit Risk, BI, Banking Domain). |
| **Portfolio Projects** | `CONFIG["projects"]` | Problem, Objective, Approach, Tools, Output, and Impact for each case study. |
| **Education** | `CONFIG["education"]` | Degrees, universities, GPAs, and English proficiency certifications. |
| **Certifications** | `CONFIG["certifications"]` | Years, certification titles, and issuing bodies. |
| **References** | `CONFIG["references"]` | Names, titles, organizations, and contact notes. |

---

## 11. Important Limitation on Streamlit Cloud Persistence

> [!WARNING]
> **Ephemeral File System on Streamlit Community Cloud:**
> Files uploaded via the browser popovers are stored in the temporary container's **session memory**. If the Streamlit application restarts, reboots, or deploys a new commit, any browser-uploaded files will be cleared.
>
> **Best Practice for Permanent Updates:**
> To ensure your CV and Photo persist permanently across server restarts and for all external recruiters, always add `cv.pdf` and `avatar.jpg` directly into your GitHub repository or configure their direct URLs inside `CONFIG` in `app.py`.
