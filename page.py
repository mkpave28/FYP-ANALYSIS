import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('https://raw.githubusercontent.com/mkpave28/FYP-ANALYSIS/refs/heads/main/SEXUAL%20HARASSMENT%20IN%20SOCIAL%20MEDIA%20FROM%202018%20UNTIL%202022%20BY%20WAO.csv')

# Display the first 5 rows
st.write(df.head())

# Display DataFrame info as text
buffer = []
df.info(buf=buffer)
info_str = "\n".join(buffer)
st.text(info_str)  # Use st.text instead of st.write for df.info()

# Display summary statistics
st.write(df.describe())
# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(x='INCIDENT YEAR', data=df, palette='viridis', edgecolor='black', ax=ax)
ax.set_title('Frequency of Harassment by Year')
ax.set_xlabel('Incident Year')
ax.set_ylabel('Count')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)
