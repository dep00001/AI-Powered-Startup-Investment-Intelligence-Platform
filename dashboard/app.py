import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Startup Investment Intelligence",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------
# Load Dataset
# ---------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(BASE_DIR, "data", "unicorn_companies.csv")

df = pd.read_csv(csv_path)

# ---------------------------
# Title
# ---------------------------
st.title("🚀 AI-Powered Startup Investment Intelligence Platform")

st.markdown(
    "### Advanced Unicorn Analytics, Market Intelligence & Investment Insights"
)

# ---------------------------
# Sidebar Filters
# ---------------------------
st.sidebar.header("🔍 Filters")

selected_country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + sorted(df["Country"].dropna().unique().tolist())
)

selected_industry = st.sidebar.selectbox(
    "Select Industry",
    ["All"] + sorted(df["Industry"].dropna().unique().tolist())
)

# Filtered Data
filtered_df = df.copy()

if selected_country != "All":
    filtered_df = filtered_df[
        filtered_df["Country"] == selected_country
    ]

if selected_industry != "All":
    filtered_df = filtered_df[
        filtered_df["Industry"] == selected_industry
    ]

# ---------------------------
# KPI Cards
# ---------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Unicorns", len(filtered_df))

with col2:
    st.metric("Countries", filtered_df["Country"].nunique())

with col3:
    st.metric("Industries", filtered_df["Industry"].nunique())

st.divider()

# ---------------------------
# Top Countries
# ---------------------------
st.subheader("🌍 Top 10 Countries by Unicorn Count")

country_counts = (
    filtered_df["Country"]
    .value_counts()
    .head(10)
)

fig_country = px.bar(
    x=country_counts.index,
    y=country_counts.values,
    labels={
        "x": "Country",
        "y": "Number of Unicorns"
    },
    title="Top Countries"
)

st.plotly_chart(fig_country, use_container_width=True)

# ---------------------------
# Top Industries
# ---------------------------
st.subheader("🏭 Top Industries")

industry_counts = (
    filtered_df["Industry"]
    .value_counts()
    .head(10)
)

fig_industry = px.bar(
    x=industry_counts.index,
    y=industry_counts.values,
    labels={
        "x": "Industry",
        "y": "Number of Unicorns"
    },
    title="Top Industries"
)

st.plotly_chart(fig_industry, use_container_width=True)

# ---------------------------
# Industry Share Pie Chart
# ---------------------------
st.subheader("🥧 Industry Share")

industry_share = (
    filtered_df["Industry"]
    .value_counts()
    .head(10)
)

fig_pie = px.pie(
    values=industry_share.values,
    names=industry_share.index,
    title="Industry Distribution"
)

st.plotly_chart(fig_pie, use_container_width=True)

# ---------------------------
# Top Companies
# ---------------------------
st.subheader("🏆 Top Unicorn Companies")

top_companies = (
    filtered_df["Company"]
    .value_counts()
    .head(10)
)

fig_company = px.bar(
    x=top_companies.index,
    y=top_companies.values,
    title="Top Unicorn Companies"
)

st.plotly_chart(fig_company, use_container_width=True)

# ---------------------------
# Dataset Preview
# ---------------------------
st.subheader("📄 Dataset Preview")

st.dataframe(filtered_df.head(20))

# ---------------------------
# Missing Values
# ---------------------------
st.subheader("⚠ Missing Values")

missing_values = filtered_df.isnull().sum()

missing_df = pd.DataFrame({
    "Column": missing_values.index,
    "Missing Values": missing_values.values
})

st.dataframe(missing_df)

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")

st.markdown(
    "Developed as part of the AI-Powered Startup Investment Intelligence Platform"
)