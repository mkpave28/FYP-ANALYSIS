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
    graph_options = [
        "Frequency of Harassment by Year",
        "Distribution of Location (State)",
        "Distribution of Action Taken",
        "Victim Age vs. Type of Harassment",
        "Education Level vs. Type of Harassment",
        "Social Media Platform vs. Total Harassment Cases",
        "Location (State) vs. Type of Harassment",
        "Action Taken vs. Outcome/Results",
        "Average Duration (Months) by Social Media Platform",
        "Type of Harassment vs. Action Taken",
        "Median Victim Age by Social Media Platform"
    ]
    selected_graph = st.selectbox("Select a graph to view", graph_options)

    # Graphs
    if selected_graph == "Frequency of Harassment by Year":
        plt.figure(figsize=(10, 6))
        sns.countplot(x='INCIDENT YEAR', data=df, palette='viridis', edgecolor='black')
        plt.title('Frequency of Harassment by Year')
        plt.xlabel('Incident Year')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        st.pyplot()

    elif selected_graph == "Distribution of Location (State)":
        plt.figure(figsize=(10, 6))
        sns.countplot(x='LOCATION (STATE)', data=df, palette='Set2')
        plt.title('Distribution of Location (State)')
        plt.xticks(rotation=45)
        st.pyplot()

    elif selected_graph == "Distribution of Action Taken":
        plt.figure(figsize=(10, 6))
        sns.countplot(x='ACTION TAKEN', data=df, palette='pastel')
        plt.title('Distribution of Action Taken')
        st.pyplot()

    elif selected_graph == "Victim Age vs. Type of Harassment":
        plt.figure(figsize=(15, 10))
        sns.boxplot(data=df, x='TYPE OF HARASSMENT', y='VICTIM AGE')
        plt.xticks(rotation=90)
        plt.title('Victim Age vs. Type of Harassment')
        st.pyplot()

    elif selected_graph == "Education Level vs. Type of Harassment":
        plt.figure(figsize=(10, 6))
        education_harassment = pd.crosstab(df['EDUCATION LEVEL'], df['TYPE OF HARASSMENT'])
        education_harassment.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')
        plt.title('Education Level vs. Type of Harassment')
        plt.ylabel('Frequency')
        plt.xlabel('Education Level')
        plt.xticks(rotation=85)
        plt.legend(title='Type of Harassment', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        st.pyplot()

    elif selected_graph == "Social Media Platform vs. Total Harassment Cases":
        plt.figure(figsize=(12, 6))
        platform_harassment = df.groupby('SOCIAL MEDIA PLATFORM')['TYPE OF HARASSMENT'].count().reset_index()
        platform_harassment = platform_harassment.sort_values(by='TYPE OF HARASSMENT', ascending=False)
        sns.barplot(x='SOCIAL MEDIA PLATFORM', y='TYPE OF HARASSMENT', data=platform_harassment, palette='viridis')
        plt.title('Social Media Platform vs. Total Harassment Cases')
        plt.xlabel('Social Media Platform')
        plt.ylabel('Number of Harassment Cases')
        plt.xticks(rotation=45)
        st.pyplot()

    elif selected_graph == "Location (State) vs. Type of Harassment":
        plt.figure(figsize=(10, 6))
        state_harassment = pd.crosstab(df['LOCATION (STATE)'], df['TYPE OF HARASSMENT'])
        state_harassment.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='coolwarm')
        plt.title('Location (State) vs. Type of Harassment')
        plt.ylabel('Frequency')
        plt.xlabel('State')
        plt.xticks(rotation=45)
        plt.legend(title='Type of Harassment', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        st.pyplot()

    elif selected_graph == "Action Taken vs. Outcome/Results":
        plt.figure(figsize=(10, 6))
        action_outcome = pd.crosstab(df['ACTION TAKEN'], df['OUTCOME/RESULTS'])
        action_outcome.plot(kind='bar', figsize=(10, 6), colormap='cividis')
        plt.title('Action Taken vs. Outcome/Results')
        plt.ylabel('Frequency')
        plt.xlabel('Action Taken')
        plt.xticks(rotation=90)
        plt.legend(title='Outcome/Results', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        st.pyplot()

    elif selected_graph == "Average Duration (Months) by Social Media Platform":
        platform_avg_duration = df.groupby('SOCIAL MEDIA PLATFORM')['DURATION (MONTHS)'].mean().reset_index()
        plt.figure(figsize=(12, 7))
        sns.barplot(data=platform_avg_duration, x='SOCIAL MEDIA PLATFORM', y='DURATION (MONTHS)', palette='coolwarm', edgecolor='black')
        plt.title('Average Duration (Months) by Social Media Platform')
        plt.xlabel('Social Media Platform')
        plt.ylabel('Average Duration (Months)')
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', alpha=0.3)
        st.pyplot()

    elif selected_graph == "Type of Harassment vs. Action Taken":
        plt.figure(figsize=(10, 6))
        harassment_action = pd.crosstab(df['TYPE OF HARASSMENT'], df['ACTION TAKEN'])
        harassment_action.plot(kind='bar', stacked=True, figsize=(10, 8), colormap='tab20c')
        plt.title('Type of Harassment vs. Action Taken')
        plt.ylabel('Frequency')
        plt.xlabel('Type of Harassment')
        plt.xticks(rotation=90)
        plt.legend(title='Action Taken', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        st.pyplot()

    elif selected_graph == "Median Victim Age by Social Media Platform":
        platform_median_age = df.groupby('SOCIAL MEDIA PLATFORM')['VICTIM AGE'].median().reset_index()
        plt.figure(figsize=(12, 7))
        sns.barplot(data=platform_median_age, x='SOCIAL MEDIA PLATFORM', y='VICTIM AGE', palette='Set2', edgecolor='black')
        plt.title('Median Victim Age by Social Media Platform')
        plt.xlabel('Social Media Platform')
        plt.ylabel('Median Victim Age')
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', alpha=0.3)
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
