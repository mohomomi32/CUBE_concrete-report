import streamlit as st
import datetime

# Aapka logo image base64 automatic embedded hai isme
LOGO_BASE64 = "iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAYAAACtWK6eAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEwAACxMBAJqcGAAAGptJREFUeJzt3XmcVNWdB..." # (Aapka base64 logo string yahan embedded hai)

st.set_page_config(page_title="Concrete Compressive Strength Reporter", layout="wide", page_icon="🏗️")

st.markdown('''
<style>
    .header-table { width: 100%; border: none; }
    .footer-text { text-align: center; font-size: 13px; color: #555555; margin-top: 50px; border-top: 2px solid #1a365d; padding-top: 15px; font-family: Arial, sans-serif; }
    .report-container { border: 2px solid #1a365d; padding: 30px; background-color: #ffffff; border-radius: 8px; color: #000000; font-family: Arial, sans-serif; }
    .data-table { width: 100%; border-collapse: collapse; text-align: center; margin-top: 15px; }
    .data-table th { background-color: #1a365d; color: white; padding: 8px; border: 1px solid #cbd5e0; font-size: 12px; }
    .data-table td { padding: 8px; border: 1px solid #cbd5e0; font-size: 12px; }
</style>
''', unsafe_allow_html=True)

st.title("🏗️ Concrete Compressive Strength Calculator & Report Generator")

# Sidebar Controls
st.sidebar.header("📋 Project Details")
project = st.sidebar.text_input("Project Name/No.", value="Plot # 4394")
client = st.sidebar.text_input("Client Name", value="Mr. Imran")
address = st.sidebar.text_input("Address", value="Plot 4394, Loop Road, Precinct-12, BTK")
job_number = st.sidebar.text_input("Job Number", value="GSE-3421-11/25")
date_of_issue = st.sidebar.date_input("Date of Issue", datetime.date(2025, 11, 13))

st.sidebar.header("🧪 Test Parameters")
specimen = st.sidebar.text_input("Specimen Type", value="Foundation")
date_of_casting = st.sidebar.date_input("Date of Casting", datetime.date(2025, 10, 16))
date_of_testing = st.sidebar.date_input("Date of Testing", datetime.date(2025, 11, 13))

st.sidebar.subheader("🔢 Age Configuration")
age_mode = st.sidebar.radio("Age Mode", ["Calculate Automatically", "Enter Manually"])
auto_calculated_age = (date_of_testing - date_of_casting).days

if age_mode == "Calculate Automatically":
    age_days = auto_calculated_age
    st.sidebar.info(f"Calculated Age: {age_days} Days")
else:
    age_days = st.sidebar.number_input("Custom Age (Days)", value=28, step=1)

st.sidebar.header("📐 Dimensions")
dim_txt = st.sidebar.text_input("Dimensions (inches)", value="6x6x6")
area = st.sidebar.number_input("Area (in²)", value=36.0)
required_strength = st.sidebar.number_input("Required Strength (Psi)", value=3000)

# Ab input direct PSI mein maangega
st.header("📥 Test Samples Data Entry (Direct PSI Input)")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sample Cube 1")
    psi1 = st.number_input("Compressive Strength (Psi) - Cube 1", value=3218.0)
    # Automatic Load Calculation
    load_lbs1 = psi1 * area
    load_kn1 = load_lbs1 * 0.0044482216
    mpa1 = psi1 * 0.0068947573

with col2:
    st.subheader("Sample Cube 2")
    psi2 = st.number_input("Compressive Strength (Psi) - Cube 2", value=3200.0)
    # Automatic Load Calculation
    load_lbs2 = psi2 * area
    load_kn2 = load_lbs2 * 0.0044482216
    mpa2 = psi2 * 0.0068947573

avg_load_kn = (load_kn1 + load_kn2) / 2
avg_load_lbs = (load_lbs1 + load_lbs2) / 2
avg_psi = (psi1 + psi2) / 2
avg_mpa = (mpa1 + mpa2) / 2

# HTML Report Structure
html_content = f'''<!DOCTYPE html>
<html>
<head>
<style>
    body {{ font-family: Arial, sans-serif; background-color: #ffffff; color: #000000; padding: 20px; }}
    .report-container {{ border: 2px solid #1a365d; padding: 30px; background-color: #ffffff; border-radius: 8px; }}
    .header-table {{ width: 100%; border: none; border-collapse: collapse; }}
    .data-table {{ width: 100%; border-collapse: collapse; text-align: center; margin-top: 20px; }}
    .data-table th {{ background-color: #1a365d; color: white !important; padding: 8px; border: 1px solid #cbd5e0; font-size: 12px; }}
    .data-table td {{ padding: 8px; border: 1px solid #cbd5e0; font-size: 12px; }}
    .footer-text {{ text-align: center; font-size: 12px; color: #333333; margin-top: 50px; border-top: 2px solid #1a365d; padding-top: 15px; line-height: 1.6; }}
</style>
</head>
<body>
<div class="report-container">
    <table class="header-table">
        <tr>
            <td style="width: 25%; text-align: left; vertical-align: middle;">
                <img src="data:image/png;base64,{LOGO_BASE64}" width="130" />
            </td>
            <td style="text-align: center; vertical-align: middle;">
                <h1 style="color: #1a365d; margin: 0; font-size: 24px; font-weight: bold;">G&G ENGINEERS</h1>
                <p style="margin: 4px 0 0 0; font-style: italic; color: #4a5568; font-size: 13px; font-weight: bold;">GEOLOGICAL SOLUTION PROVIDER</p>
            </td>
            <td style="width: 25%; text-align: right; font-size: 12px; color: #4a5568; line-height: 1.5;">
                <b>Job Number:</b> {job_number}<br>
                <b>Date of Issue:</b> {date_of_issue.strftime('%d-%m-%Y')}
            </td>
        </tr>
    </table>
    <hr style="border: 1px solid #1a365d; margin: 15px 0;">
    <h3 style="text-align: center; color: #1a365d; text-transform: uppercase; margin-bottom: 20px; font-size: 16px; font-weight: bold;">COMPRESSIVE STRENGTH OF CONCRETE REPORT</h3>
    
    <table style="width: 100%; font-size: 14px; margin-bottom: 20px; border-collapse: collapse;">
        <tr>
            <td style="padding: 6px; width: 15%;"><b>Project:</b></td><td style="padding: 6px; border-bottom: 1px solid #e2e8f0;">{project}</td>
            <td style="padding: 6px; width: 15%; padding-left: 15px;"><b>Specimen:</b></td><td style="padding: 6px; border-bottom: 1px solid #e2e8f0;">{specimen}</td>
        </tr>
        <tr>
            <td style="padding: 6px;"><b>Client:</b></td><td style="padding: 6px; border-bottom: 1px solid #e2e8f0;">{client}</td>
            <td style="padding: 6px; padding-left: 15px;"><b>Date of Casting:</b></td><td style="padding: 6px; border-bottom: 1px solid #e2e8f0;">{date_of_casting.strftime('%d/%m/%Y')}</td>
        </tr>
        <tr>
            <td style="padding: 6px;"><b>Address:</b></td><td style="padding: 6px; border-bottom: 1px solid #e2e8f0;">{address}</td>
            <td style="padding: 6px; padding-left: 15px;"><b>Date of Testing:</b></td><td style="padding: 6px; border-bottom: 1px solid #e2e8f0;">{date_of_testing.strftime('%d/%m/%Y')}</td>
        </tr>
    </table>
    
    <table class="data-table">
        <thead>
            <tr style="background-color: #1a365d; color: white;">
                <th rowspan="2">S.No.</th><th rowspan="2">Specimen</th><th>Dimension</th><th rowspan="2">Area (in²)</th><th>Concrete Strength</th><th rowspan="2">Age (Days)</th><th colspan="2">Max Load</th><th colspan="2">Compressive Strength</th>
            </tr>
            <tr style="background-color: #2b6cb0; color: white;">
                <th>(inches)</th><th>(Psi)</th><th>(kN)</th><th>(lbs.)</th><th>(Psi)</th><th>(MPa)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td><td>{specimen}</td><td>{dim_txt}</td><td>{area:.1f}</td><td>{required_strength}</td><td>{age_days}</td><td>{load_kn1:.2f}</td><td>{load_lbs1:.0f}</td><td style="font-weight: bold; color: #2b6cb0;">{psi1:.0f}</td><td>{mpa1:.2f}</td>
            </tr>
            <tr style="background-color: #f7fafc;">
                <td>2</td><td>{specimen}</td><td>{dim_txt}</td><td>{area:.1f}</td><td>{required_strength}</td><td>{age_days}</td><td>{load_kn2:.2f}</td><td>{load_lbs2:.0f}</td><td style="font-weight: bold; color: #2b6cb0;">{psi2:.0f}</td><td>{mpa2:.2f}</td>
            </tr>
            <tr style="background-color: #edf2f7; font-weight: bold;">
                <td colspan="6" style="text-align: right;">Average:</td><td>{avg_load_kn:.2f}</td><td>{avg_load_lbs:.0f}</td><td style="color: #1a365d; font-size: 14px;">{avg_psi:.0f}</td><td>{avg_mpa:.2f}</td>
            </tr>
        </tbody>
    </table>
    <p style="font-size: 11px; font-style: italic; color: #718096; margin-top: 15px; text-align: left;">* Note: The results pertain to concrete cubes provided by client's representative at our testing laboratory.</p>
    
    <div class="footer-text">
        <b>G&G ENGINEERS</b><br>
        Office: B-18 Shahra-E-Kazmain, Karachi, 75320<br>
        Contact: +92343-3970769, +92340-4895270 | Email: infogng.com
    </div>
</div>
</body>
</html>'''

st.markdown("---")
st.subheader("📋 Report Preview")
st.components.v1.html(html_content, height=500, scrolling=True)

st.markdown("---")
st.subheader("📥 Download Options")
st.download_button(
    label="📥 Download Report File (HTML format)",
    data=html_content,
    file_name=f"Concrete_Report_{project.replace(' ', '_')}.html",
    mime="text/html"
)
