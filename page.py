import pandas as pd
import streamlit as st
df = pd.read_csv('https://raw.githubusercontent.com/mkpave28/FYP-ANALYSIS/refs/heads/main/SEXUAL%20HARASSMENT%20IN%20SOCIAL%20MEDIA%20FROM%202018%20UNTIL%202022%20BY%20WAO.csv')
# Display the first 5 rows of the dataset
st.write(df.head())

# Information about columns, data types, and non-null counts
st.write(df.info())

# Summary statistics for numerical columns
st.write(df.describe())
import matplotlib as plt
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.countplot(x='INCIDENT YEAR', data=df, palette='viridis', edgecolor='black')
plt.title('Frequency of Harassment by Year')
plt.xlabel('Incident Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
