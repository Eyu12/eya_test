import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, get_top_regions

st.set_page_config(page_title="Solar Insights Dashboard", layout="wide")

st.title("Cross-Country Solar Insights Dashboard")

# Sidebar
st.sidebar.header("Filter Options")
countries = ["Benin", "Sierra Leone", "Togo"]
selected_country = st.sidebar.selectbox("Select Country", countries)

metric = st.sidebar.selectbox(
    "Select Metric",
    ["GHI", "DNI", "DHI", "ModA", "ModB"]
)

# Load Data
data = load_data(selected_country)

# Main Display
st.subheader(f"{selected_country} — {metric} Distribution")
fig = px.box(data, y=metric, title=f"{metric} Distribution in {selected_country}")
st.plotly_chart(fig, use_container_width=True)

# Top Regions (Example)
st.subheader("Top Regions by Average Solar Irradiance")
top_regions = get_top_regions(data, metric)
st.dataframe(top_regions)

# Additional Interaction
if st.checkbox("Show Summary Statistics"):
    st.write(data[metric].describe())
