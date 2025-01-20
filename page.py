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
        "Age Distribution of Victims (Histogram)",
        "Age Range of Victims (Boxplot)",
        "Yearly Frequency of Harassment Cases",
        "Harassment Cases Over the Years: Histogram and KDE",
        "Duration of Harassment Cases (in Months)",
        "Percentage Distribution of Harassment Types (Pie Chart)",
        "State-Wise Distribution of Harassment Cases",
        "Actions Taken Against Harassment Cases",
        "Victim Age Across Different Education Levels",
        "Victim Age by Type of Harassment",
        "Harassment Type Across Education Levels",
        "Harassment Cases Across Social Media Platforms",
        "State-Wise Harassment Types: A Stacked View",
        "Trends in Harassment Types by Incident Year",
        "Average Harassment Duration by Victim Age",
        "Education Levels and Actions Results",
        "Action Taken and Actions Results",
        "Total Results Across Different States",
        "Average Duration of Harassment by Social Media Platform",
        "Action Results Over the Years",
        "Actions Taken Across Harassment Types",
        "Average Harassment Duration by Action Results",
        "Median Age of Victims Across Social Media Platforms",
        "Education Level vs. Social Media Platform Usage"
    
    ]
    
    selected_graph = st.selectbox("Select a graph to view", graph_options)

    # Graph Implementation
    if selected_graph == "Age Distribution of Victims":
        plt.figure(figsize=(8, 6))
        sns.histplot(df['VICTIM AGE'], kde=True, bins=20, color='#008080', edgecolor='black')
        plt.title('Age Distribution of Victims')
        plt.xlabel('Age of Victims', fontsize=12)
        plt.ylabel('Number of Cases', fontsize=12)
        st.pyplot()
    
    elif selected_graph == "Age Range of Victims":
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

    elif selected_graph == "Harassment Cases Over the Years: Histogram and KDE":
        plt.figure(figsize=(8, 6))
        sns.histplot(
            df['INCIDENT YEAR'], 
            kde=True, 
            bins=20, 
            color='#008080', 
            edgecolor='black', 
            alpha=0.6
        )
        plt.title('Harassment Cases Over the Years: Histogram and KDE', fontsize=14)
        plt.xlabel('Year of Incident', fontsize=12)
        plt.ylabel('Number of Cases', fontsize=12)  
        st.pyplot()
    
    elif selected_graph == "Duration of Harassment Cases (in Months)":
       plt.figure(figsize=(8, 6))
       sns.countplot(x='DURATION (MONTHS)', data=df, palette='husl', edgecolor='black')
       plt.title('Duration of Harassment Cases (in Months)', fontsize=14)
       plt.xlabel('Duration (Months)', fontsize=12)
       plt.ylabel('Number of Cases', fontsize=12)
       st.pyplot()
    
    elif selected_graph == "Percentage Distribution of Harassment Types":
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
    
    elif selected_graph == "Actions Taken Against Harassment Cases":
        plt.figure(figsize=(8, 6))
        sns.countplot(x='ACTION TAKEN', data=df, palette='magma', edgecolor='black')
        plt.title('Actions Taken Against Harassment Cases', fontsize=14)
        plt.xlabel('Type of Action Taken', fontsize=12)
        plt.ylabel('Number of Cases', fontsize=12)
        plt.xticks(rotation=90)
        st.pyplot()
    
    elif selected_graph == "Victim Age Across Different Education Levels":
        plt.figure(figsize=(8, 6))
        sns.lineplot(x='EDUCATION LEVEL', y='VICTIM AGE', data=df, marker='o', color='teal', linewidth=3)
        plt.title('Victim Age Across Different Education Levels', fontsize=14)
        plt.xlabel('Education Level', fontsize=12)
        plt.ylabel('Victim Age', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.xticks(rotation=90)
        st.pyplot()
    
    elif selected_graph == "Victim Age by Type of Harassment":
        plt.figure(figsize=(9, 6))
        sns.boxplot(data=df, x='TYPE OF HARASSMENT', y='VICTIM AGE', color='#9B59B6')
        plt.xticks(rotation=90)
        plt.title('Victim Age by Type of Harassment', fontsize=14)
        plt.xlabel('Type of Harassment', fontsize=12)
        plt.ylabel('Victim Age', fontsize=12)
        st.pyplot()
    
    elif selected_graph == "Harassment Type Across Education Levels":
        education_harassment = pd.crosstab(df['EDUCATION LEVEL'], df['TYPE OF HARASSMENT'])
        education_harassment.plot(kind='bar', stacked=True, figsize=(8, 6), colormap='viridis', edgecolor='black')
        plt.title('Harassment Type Across Education Levels', fontsize=12)
        plt.ylabel('Number of Cases', fontsize=12)
        plt.xlabel('Education Level', fontsize=12)
        plt.xticks(rotation=90)
        plt.legend(title='Type of Harassment', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
        plt.tight_layout()
        st.pyplot()
    
    elif selected_graph == "Harassment Cases Across Social Media Platforms":
        platform_harassment = df.groupby('SOCIAL MEDIA PLATFORM')['TYPE OF HARASSMENT'].count().reset_index()
        platform_harassment = platform_harassment.sort_values(by='TYPE OF HARASSMENT', ascending=False)
        
        plt.figure(figsize=(8, 6))
        sns.barplot(
            x='SOCIAL MEDIA PLATFORM',
            y='TYPE OF HARASSMENT',
            data=platform_harassment,
            palette='inferno',
            edgecolor='black'
        )
        plt.title('Harassment Cases Across Social Media Platforms', fontsize=14)
        plt.xlabel('Social Media Platform', fontsize=12)
        plt.ylabel('Number of Harassment Cases', fontsize=12)
        plt.xticks(rotation=90)
        st.pyplot()
    
    elif selected_graph == "State-Wise Harassment Types":
        state_harassment = pd.crosstab(df['LOCATION (STATE)'], df['TYPE OF HARASSMENT'])
        state_harassment.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='coolwarm', edgecolor='black')
        plt.title('State-Wise Harassment Types: A Stacked View', fontsize=14)
        plt.ylabel('Number of Cases', fontsize=12)
        plt.xlabel('State', fontsize=12)
        plt.xticks(rotation=90)
        plt.legend(title='Type of Harassment', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        st.pyplot()
    
    elif selected_graph == "Trends in Harassment Types by Incident Year":
        stacked_data = df.pivot_table(
            index='INCIDENT YEAR', 
            columns='TYPE OF HARASSMENT', 
            values='VICTIM AGE', 
            aggfunc='count'
        ).fillna(0)
        
        plt.figure(figsize=(8, 6))
        stacked_data.plot(
            kind='bar',
            stacked=True,
            figsize=(8, 6),
            colormap='Spectral',
            edgecolor='black',
            ax=plt.gca()  
        )
        plt.title('Trends in Harassment Types by Incident Year', fontsize=12)
        plt.ylabel('Number of Cases', fontsize=12)
        plt.xlabel('Year of Incident', fontsize=12)
        plt.xticks(rotation=90)
        plt.legend(title='Type of Harassment', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        st.pyplot()
    
    elif selected_graph == "Average Harassment Duration by Victim Age":
        avg_duration = df.groupby('VICTIM AGE')['DURATION (MONTHS)'].mean().reset_index()
        plt.figure(figsize=(10, 6))
        sns.barplot(
            data=avg_duration,
            x='VICTIM AGE',
            y='DURATION (MONTHS)',
            palette='Blues_d',
            edgecolor='black'
        )
        plt.title('Average Harassment Duration by Victim Age', fontsize=14)
        plt.xlabel('Victim Age', fontsize=12)
        plt.ylabel('Average Duration (Months)', fontsize=12)
        plt.xticks(rotation=0)
        plt.grid(axis='y', alpha=0.3)
        st.pyplot()
    
    elif selected_graph == "Education Levels and Actions Results":
        education_outcome = pd.crosstab(df['EDUCATION LEVEL'], df['OUTCOME/RESULTS'])
        education_outcome.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='icefire', edgecolor='black')
        plt.title('Education Levels and Actions Results', fontsize=12)
        plt.ylabel('Actions Results', fontsize=12)
        plt.xlabel('Education Level', fontsize=12)
        plt.xticks(rotation=90)
        plt.legend(title='Actions Results', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        st.pyplot()
    
    elif selected_graph == "Action Taken and Results":
        action_outcome = pd.crosstab(df['ACTION TAKEN'], df['OUTCOME/RESULTS'])
        action_outcome.plot(kind='bar', figsize=(8, 6), colormap='viridis_r', edgecolor='black')
        plt.title('Action Taken and Actions Results', fontsize=14)
        plt.ylabel('Actions Results', fontsize=12)
        plt.xlabel('Action Taken', fontsize=12)
        plt.xticks(rotation=90)
        plt.legend(title='Actions results', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        st.pyplot()
    
    elif selected_graph == "Total Results Across Different States":
        state_outcome_summary = df.groupby('LOCATION (STATE)')['OUTCOME/RESULTS'].value_counts().unstack(fill_value=0)
        state_outcome_summary = state_outcome_summary.sum(axis=1).reset_index()
        state_outcome_summary.columns = ['LOCATION (STATE)', 'TOTAL OUTCOMES']
        
        plt.figure(figsize=(8, 6))
        sns.barplot(
            data=state_outcome_summary,
            x='LOCATION (STATE)',
            y='TOTAL OUTCOMES',
            palette='viridis',
            edgecolor='black'
        )
        plt.title('Total Results Across Different States', fontsize=14)
        plt.xlabel('State', fontsize=12)
        plt.ylabel('Total Results', fontsize=12)
        plt.xticks(rotation=90, ha='right') 
        plt.grid(axis='y', alpha=0.3)
        st.pyplot()
    
    elif selected_graph == "Average Duration by Social Media Platform":
        platform_avg_duration = df.groupby('SOCIAL MEDIA PLATFORM')['DURATION (MONTHS)'].mean().reset_index()
        
        plt.figure(figsize=(8, 6))
        sns.barplot(
            data=platform_avg_duration,
            x='SOCIAL MEDIA PLATFORM',
            y='DURATION (MONTHS)',
            palette='coolwarm',
            edgecolor='black'
        )
        plt.title('Average Duration of Harassment by Social Media Platform', fontsize=14)
        plt.xlabel('Social Media Platform', fontsize=12)
        plt.ylabel('Average Duration (Months)', fontsize=12)
        plt.xticks(rotation=90, ha='right')  
        plt.grid(axis='y', alpha=0.3)
        st.pyplot()
    
    elif selected_graph == "Action Results Over the Years":
        year_outcome = df.groupby(['INCIDENT YEAR', 'OUTCOME/RESULTS']).size().unstack(fill_value=0)
        year_outcome.reset_index(inplace=True)
        year_outcome.plot(
            kind='bar',
            x='INCIDENT YEAR',
            stacked=False,
            figsize=(8, 6),
            colormap='inferno',
            edgecolor='black'
        )
        plt.title('Action Results Over the Years', fontsize=14)
        plt.ylabel('Number of Action Results', fontsize=12)
        plt.xlabel('Year of Incident', fontsize=12)
        plt.legend(title='Action Results', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xticks(rotation=90, ha='right')  
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()  
        st.pyplot()
    
    elif selected_graph == "Actions Taken Across Harassment Types":
        harassment_action = pd.crosstab(df['TYPE OF HARASSMENT'], df['ACTION TAKEN'])
        harassment_action.plot(kind='bar', stacked=True, figsize=(10, 8), colormap='flare', edgecolor='black')
        plt.title('Actions Taken Across Harassment Types', fontsize=14)
        plt.ylabel('Number of Actions Taken', fontsize=12)
        plt.xlabel('Type of Harassment', fontsize=12)
        plt.xticks(rotation=90)
        plt.legend(title='Action Taken', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()  
        st.pyplot()
    
    elif selected_graph == "Average Harassment Duration by Action Results":
        outcome_avg_duration = df.groupby('OUTCOME/RESULTS')['DURATION (MONTHS)'].mean().reset_index()
        
        plt.figure(figsize=(10, 8))
        sns.barplot(
            data=outcome_avg_duration,
            x='OUTCOME/RESULTS',
            y='DURATION (MONTHS)',
            palette='mako',
            edgecolor='black'
        )
        plt.title('Average Harassment Duration by Action Results', fontsize=14)
        plt.xlabel('Action Results', fontsize=12)
        plt.ylabel('Average Duration (Months)', fontsize=12)
        plt.xticks(rotation=90, ha='right')  
        plt.grid(axis='y', alpha=0.3)
        st.pyplot()
    
    elif selected_graph == "Median Age by Social Media Platform":
        platform_median_age = df.groupby('SOCIAL MEDIA PLATFORM')['VICTIM AGE'].median().reset_index()
        
        plt.figure(figsize=(10, 8))
        sns.barplot(
            data=platform_median_age,
            x='SOCIAL MEDIA PLATFORM',
            y='VICTIM AGE',
            palette='rocket',
            edgecolor='black'
        )
        plt.title('Median Age of Victims Across Social Media Platforms', fontsize=14)
        plt.xlabel('Social Media Platform', fontsize=12)
        plt.ylabel('Median Victim Age', fontsize=12)
        plt.xticks(rotation=90, ha='right')  
        plt.grid(axis='y', alpha=0.3)
        st.pyplot()
    
    elif selected_graph == "Education Level vs. Social Media Platform Usage":
        education_platform = pd.crosstab(df['EDUCATION LEVEL'], df['SOCIAL MEDIA PLATFORM'])
        ax = education_platform.plot(kind='bar', width=0.9, figsize=(15, 10), colormap='Paired', edgecolor='black') 
        
        plt.title('Education Level vs. Social Media Platform Usage', fontsize=30)
        plt.ylabel('Number of Cases', fontsize=20)
        plt.xlabel('Education Level', fontsize=20)
        plt.xticks(rotation=60)
        plt.legend(title='Social Media Platform', bbox_to_anchor=(1.01, 1), loc='upper left')
        plt.tight_layout()
        ax.set_xticks(ax.get_xticks() + 0.9)  
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
