import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import cufflinks as cf
import plotly.graph_objs as go
cf.go_offline()
cf.set_config_file(world_readable=True, theme='pearl')


# Load the cleaned data
df = pd.read_excel("cleaned_data.xlsx")

# Calculate KPIs
df['total_engagement'] = df['likes'] + df['comments'] + df['shares']
df['engagement_rate'] = (df['total_engagement'] / df['reach']) * 100
df['virality_rate'] = (df['shares'] / df['impressions']) * 100

# Page config
st.set_page_config(page_title="Social Media Dashboard", layout="wide")

st.title("📊 Social Media Analytics Dashboard")

# KPI section
col1, col2, col3 = st.columns(3)
col1.metric("Avg Engagement Rate (%)", round(df['engagement_rate'].mean(), 2))
col2.metric("Avg Virality Rate (%)", round(df['virality_rate'].mean(), 2))
col3.metric("Total Posts", len(df))

#Follower Growth Over Time
st.subheader("📈 Follower Growth Over Time")
sorted_df = df.sort_values('post_date')
fig1 = px.line(
    sorted_df,
    x='post_date',
    y='follower_count_at_time_of_post',
    markers=True,
    title='Follower Growth Over Time'
)
st.plotly_chart(fig1, use_container_width=True)

#Engagement Rate by Post Type
st.subheader("🎯 Engagement Rate by Post Type")
engagement_df = df.groupby('post_type')['engagement_rate'].mean().reset_index()
fig2 = px.bar(
    engagement_df,
    x='post_type',
    y='engagement_rate',
    title='Engagement Rate by Post Type',
    color='engagement_rate'
)
st.plotly_chart(fig2, use_container_width=True)



#Average Reach by Platform
st.subheader("📣 Average Reach by Platform")
reach_df = df.groupby('platform')['reach'].mean().reset_index()
fig3 = px.bar(
    reach_df,
    x='platform',
    y='reach',
    title='Average Reach by Platform',
    color='reach'
)
st.plotly_chart(fig3, use_container_width=True)
