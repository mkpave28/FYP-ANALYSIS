import pandas as pd
import streamlit as st
df = pd.read_csv('https://github.com/mkpave28/FYP-ANALYSIS/blob/main/SEXUAL%20HARASSMENT%20IN%20SOCIAL%20MEDIA%20FROM%202018%20UNTIL%202022%20BY%20WAO.csv')
# Display the first 5 rows of the dataset
st.write(df.head())

# Information about columns, data types, and non-null counts
st.write(df.info())

# Summary statistics for numerical columns
st.write(df.describe())
import matplotlib as plt
import seaborn as sns
# Histogram of age
plt.figure(figsize=(10, 6))
sns.histplot(df['VICTIM AGE'], kde=True, bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
st.pyplot(plt.gcf())
