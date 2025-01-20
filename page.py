import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# Set page title and layout
st.set_page_config(
    page_title="Women Harassment Analysis Dashboard",
    layout="wide"
)

# Dashboard Title
st.title("Women Harassment Analysis in Social Media (2018-2022)")

# Sidebar for navigation
st.sidebar.title("Navigation")
sections = ["Dataset Overview", "Visualizations", "Insights"]
selected_section = st.sidebar.radio("Go to", sections)

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv(
        'https://raw.githubusercontent.com/mkpave28/FYP-ANALYSIS/refs/heads/main/SEXUAL%20HARASSMENT%20IN%20SOCIAL%20MEDIA%20FROM%202018%20UNTIL%202022%20BY%20WAO.csv'
    )

df = load_data()

# Dataset Overview Section
if selected_section == "Dataset Overview":
    st.header("Dataset Overview")
    st.write("### First Five Rows of the Dataset")
    st.dataframe(df.head())
    st.write("### Dataset Info")
    buffer = StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()
    st.text(info_str)
    st.write("### Summary Statistics")
    st.dataframe(df.describe())

# Visualizations Section
elif selected_section == "Visualizations":
    st.header("Visualizations")
    
    # List of all graphs
    graph_options = [
        "Frequency of Harassment by Year (Histogram & KDE)",
        "Age Distribution of Victims (Histogram)",
        "Age Range of Victims (Boxplot)",
        "Yearly Frequency of Harassment Cases",
        "Percentage Distribution of Harassment Types (Pie Chart)",
        "State-Wise Distribution of Harassment Cases",
        "Duration of Harassment Cases (in Months)",
        "Action Taken Distribution",
        "Monthly Harassment Trend (Line Chart)",
        "Year-Month Analysis of Cases (Heatmap)",
        "Relation Between Age and Harassment Type (Scatter Plot)",
        "Monthly Harassment Cases by State (Stacked Bar Chart)",
        "Day-of-Week Frequency of Incidents (Bar Chart)",
        "Number of Cases by Time of Day (Bar Chart)",
        "Severity of Cases by Time of Day (Boxplot)",
        "Location of Cases (Geographical Distribution)",
        "Number of Cases by Location Type (Bar Chart)",
        "Age and Duration Correlation (Scatter Plot with Regression)",
        "Harassment Types and Severity Comparison (Bar Chart)",
        "Monthly Victim Counts for Key States (Line Chart)",
        "Comparison of Action Taken Across States (Grouped Bar Chart)",
        "Year-on-Year Growth Rate of Harassment Cases (Line Chart)",
        "Severity Analysis for Key Harassment Types (Boxplot)",
        "Relationship Between Victim Age and Incident Duration (Scatter Plot)"
    ]
    
    selected_graph = st.selectbox("Select a graph to view", graph_options)

    # Graph Implementation
    if selected_graph == "Frequency of Harassment by Year (Histogram & KDE)":
        plt.figure(figsize=(8, 6))
        sns.histplot(df['INCIDENT YEAR'], kde=True, bins=20, color='#008080', edgecolor='black', alpha=0.6)
        plt.title('Harassment Cases Over the Years: Histogram and KDE', fontsize=14)
        plt.xlabel('Year of Incident', fontsize=12)
        plt.ylabel('Number of Cases', fontsize=12)
        st.pyplot()
        
    elif selected_graph == "Age Distribution of Victims (Histogram)":
        plt.figure(figsize=(8, 6))
        sns.histplot(df['VICTIM AGE'], kde=True, bins=20, color='#008080', edgecolor='black')
        plt.title('Age Distribution of Victims', fontsize=14)
        plt.xlabel('Age of Victims', fontsize=12)
        plt.ylabel('Number of Cases', fontsize=12)
        st.pyplot()
        
    elif selected_graph == "Age Range of Victims (Boxplot)":
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=df['VICTIM AGE'], color='#FF6347')
        plt.title('Age Range of Victims', fontsize=14)
        plt.xlabel('Age of Victims', fontsize=12)
        st.pyplot()
    
    elif selected_graph == "Yearly Frequency of Harassment Cases":
        plt.figure(figsize=(8, 6))
        sns.countplot(x='INCIDENT YEAR', data=df, palette='Dark2', edgecolor='black')
        plt.title('Yearly Frequency of Harassment Cases', fontsize=14)
        plt.xlabel('Year of Incident', fontsize=12)
        plt.ylabel('Number of Cases', fontsize=12)
        plt.xticks(rotation=90)
        st.pyplot()
        
    elif selected_graph == "Percentage Distribution of Harassment Types (Pie Chart)":
        harassment_counts = df['TYPE OF HARASSMENT'].value_counts()
        labels = harassment_counts.index.str.replace('count', '', regex=False).str.strip()

        plt.figure(figsize=(8, 6))
        plt.pie(
            harassment_counts,
            labels=labels,
            autopct='%1.1f%%',
            startangle=90,
            colors=['#4DB6AC', '#FFC107', '#7E57C2'],
            wedgeprops={'linewidth': 3, 'edgecolor': 'white'},
            labeldistance=1.1
        )
        plt.title('Percentage Distribution of Harassment Types', fontsize=14)
        st.pyplot()
    
    elif selected_graph == "State-Wise Distribution of Harassment Cases":
        plt.figure(figsize=(8, 6))
        sns.countplot(x='LOCATION (STATE)', data=df, palette='Spectral', edgecolor='black')
        plt.title('State-Wise Distribution of Harassment Cases', fontsize=14)
        plt.xlabel('State', fontsize=12)
        plt.ylabel('Number of Cases', fontsize=12)
        plt.xticks(rotation=90)
        st.pyplot()
    
    elif selected_graph == "Duration of Harassment Cases (in Months)":
        plt.figure(figsize=(8, 6))
        sns.countplot(x='DURATION (MONTHS)', data=df, palette='husl', edgecolor='black')
        plt.title('Duration of Harassment Cases (in Months)', fontsize=14)
        plt.xlabel('Duration (Months)', fontsize=12)
        plt.ylabel('Number of Cases', fontsize=12)
        st.pyplot()
    
    elif selected_graph == "Monthly Harassment Trend (Line Chart)":
    monthly_trend = df.groupby('MONTH')['CASE ID'].count()
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=monthly_trend, marker="o", color="#FF6F61")
    plt.title("Monthly Harassment Trend", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Number of Cases", fontsize=12)
    st.pyplot()

# Year-Month Analysis of Cases (Heatmap)
elif selected_graph == "Year-Month Analysis of Cases (Heatmap)":
    heatmap_data = df.pivot_table(index='MONTH', columns='INCIDENT YEAR', values='CASE ID', aggfunc='count')
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap="YlGnBu", annot=True, fmt=".0f", linewidths=0.5)
    plt.title("Year-Month Analysis of Cases", fontsize=14)
    st.pyplot()

# Relation Between Age and Harassment Type (Scatter Plot)
elif selected_graph == "Relation Between Age and Harassment Type (Scatter Plot)":
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="VICTIM AGE", y="TYPE OF HARASSMENT", data=df, alpha=0.7, hue="ACTION TAKEN")
    plt.title("Relation Between Age and Harassment Type", fontsize=14)
    plt.xlabel("Victim Age", fontsize=12)
    plt.ylabel("Harassment Type", fontsize=12)
    st.pyplot()

# Monthly Harassment Cases by State (Stacked Bar Chart)
elif selected_graph == "Monthly Harassment Cases by State (Stacked Bar Chart)":
    state_month_data = df.groupby(['LOCATION (STATE)', 'MONTH'])['CASE ID'].count().unstack()
    state_month_data.plot(kind="bar", stacked=True, figsize=(12, 8), colormap="tab20c")
    plt.title("Monthly Harassment Cases by State", fontsize=14)
    plt.xlabel("State", fontsize=12)
    plt.ylabel("Number of Cases", fontsize=12)
    plt.legend(title="Month", bbox_to_anchor=(1.05, 1), loc="upper left")
    st.pyplot()

# Day-of-Week Frequency of Incidents (Bar Chart)
elif selected_graph == "Day-of-Week Frequency of Incidents (Bar Chart)":
    plt.figure(figsize=(10, 6))
    sns.countplot(x="DAY OF WEEK", data=df, palette="cubehelix", order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    plt.title("Day-of-Week Frequency of Incidents", fontsize=14)
    plt.xlabel("Day of the Week", fontsize=12)
    plt.ylabel("Number of Cases", fontsize=12)
    st.pyplot()

# Number of Cases by Time of Day (Bar Chart)
elif selected_graph == "Number of Cases by Time of Day (Bar Chart)":
    plt.figure(figsize=(10, 6))
    sns.countplot(x="TIME OF DAY", data=df, palette="Set2", order=["Morning", "Afternoon", "Evening", "Night"])
    plt.title("Number of Cases by Time of Day", fontsize=14)
    plt.xlabel("Time of Day", fontsize=12)
    plt.ylabel("Number of Cases", fontsize=12)
    st.pyplot()

# Severity of Cases by Time of Day (Boxplot)
elif selected_graph == "Severity of Cases by Time of Day (Boxplot)":
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="TIME OF DAY", y="SEVERITY SCORE", data=df, palette="pastel")
    plt.title("Severity of Cases by Time of Day", fontsize=14)
    plt.xlabel("Time of Day", fontsize=12)
    plt.ylabel("Severity Score", fontsize=12)
    st.pyplot()

# Location of Cases (Geographical Distribution)
elif selected_graph == "Location of Cases (Geographical Distribution)":
    st.map(df[["LATITUDE", "LONGITUDE"]].dropna())

# Number of Cases by Location Type (Bar Chart)
elif selected_graph == "Number of Cases by Location Type (Bar Chart)":
    plt.figure(figsize=(10, 6))
    sns.countplot(x="LOCATION TYPE", data=df, palette="coolwarm", order=df["LOCATION TYPE"].value_counts().index)
    plt.title("Number of Cases by Location Type", fontsize=14)
    plt.xlabel("Location Type", fontsize=12)
    plt.ylabel("Number of Cases", fontsize=12)
    st.pyplot()

# Age and Duration Correlation (Scatter Plot with Regression)
elif selected_graph == "Age and Duration Correlation (Scatter Plot with Regression)":
    plt.figure(figsize=(10, 6))
    sns.regplot(x="VICTIM AGE", y="DURATION (MONTHS)", data=df, scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})
    plt.title("Correlation Between Age and Duration of Harassment", fontsize=14)
    plt.xlabel("Victim Age", fontsize=12)
    plt.ylabel("Duration (Months)", fontsize=12)
    st.pyplot()

# Harassment Types and Severity Comparison (Bar Chart)
elif selected_graph == "Harassment Types and Severity Comparison (Bar Chart)":
    plt.figure(figsize=(12, 6))
    sns.barplot(x="TYPE OF HARASSMENT", y="SEVERITY SCORE", data=df, ci=None, palette="viridis")
    plt.title("Comparison of Harassment Types and Severity", fontsize=14)
    plt.xlabel("Harassment Type", fontsize=12)
    plt.ylabel("Severity Score", fontsize=12)
    plt.xticks(rotation=45, ha="right")
    st.pyplot()

# Monthly Victim Counts for Key States (Line Chart)
elif selected_graph == "Monthly Victim Counts for Key States (Line Chart)":
    key_states = ["Selangor", "Kuala Lumpur", "Johor"]
    filtered_df = df[df["LOCATION (STATE)"].isin(key_states)]
    monthly_data = filtered_df.groupby(["LOCATION (STATE)", "MONTH"])["CASE ID"].count().unstack()
    plt.figure(figsize=(12, 6))
    monthly_data.T.plot(marker="o", figsize=(12, 6))
    plt.title("Monthly Victim Counts for Key States", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Number of Cases", fontsize=12)
    plt.legend(title="State")
    st.pyplot()

# Comparison of Action Taken Across States (Grouped Bar Chart)
elif selected_graph == "Comparison of Action Taken Across States (Grouped Bar Chart)":
    state_action_data = df.groupby(["LOCATION (STATE)", "ACTION TAKEN"])["CASE ID"].count().unstack()
    state_action_data.plot(kind="bar", figsize=(12, 6), colormap="tab10")
    plt.title("Comparison of Action Taken Across States", fontsize=14)
    plt.xlabel("State", fontsize=12)
    plt.ylabel("Number of Actions", fontsize=12)
    plt.legend(title="Action Taken", bbox_to_anchor=(1.05, 1), loc="upper left")
    st.pyplot()

# Year-on-Year Growth Rate of Harassment Cases (Line Chart)
elif selected_graph == "Year-on-Year Growth Rate of Harassment Cases (Line Chart)":
    yearly_cases = df.groupby("INCIDENT YEAR")["CASE ID"].count()
    growth_rate = yearly_cases.pct_change() * 100
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=yearly_cases.index, y=growth_rate, marker="o", color="#D81B60")
    plt.axhline(0, color="gray", linestyle="--", linewidth=1)
    plt.title("Year-on-Year Growth Rate of Harassment Cases", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Growth Rate (%)", fontsize=12)
    st.pyplot()

# Severity Analysis for Key Harassment Types (Boxplot)
elif selected_graph == "Severity Analysis for Key Harassment Types (Boxplot)":
    key_types = ["Verbal", "Physical", "Cyber"]
    filtered_df = df[df["TYPE OF HARASSMENT"].isin(key_types)]
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="TYPE OF HARASSMENT", y="SEVERITY SCORE", data=filtered_df, palette="coolwarm")
    plt.title("Severity Analysis for Key Harassment Types", fontsize=14)
    plt.xlabel("Harassment Type", fontsize=12)
    plt.ylabel("Severity Score", fontsize=12)
    st.pyplot()

# Relationship Between Victim Age and Incident Duration (Scatter Plot)
elif selected_graph == "Relationship Between Victim Age and Incident Duration (Scatter Plot)":
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="VICTIM AGE", y="DURATION (MONTHS)", data=df, hue="TYPE OF HARASSMENT", alpha=0.7, palette="Dark2")
    plt.title("Relationship Between Victim Age and Incident Duration", fontsize=14)
    plt.xlabel("Victim Age", fontsize=12)
    plt.ylabel("Incident Duration (Months)", fontsize=12)
    st.pyplot() 


# Insights Section
elif selected_section == "Insights":
    st.header("Insights")
    st.write("### Key Findings and Observations")
    st.markdown("""
    - The dataset covers incidents of harassment reported from 2018 to 2022.
    - Visualizations reveal trends in incident frequency over the years.
    - Insights will be added here as we analyze more data.
    """)

# Footer
st.markdown("---")
st.markdown("Created by PAVETHRAN BATMANATHEN as part of Final Year Project")
