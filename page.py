import pandas as pd
import streamlit as st
df = pd.read_excel('SEXUAL HARASSMENT IN SOCIAL MEDIA FROM 2018 UNTIL 2022 BY WAO.xlsx')
# Display the first 5 rows of the dataset
st.write(df.head())

# Information about columns, data types, and non-null counts
st.write(df.info())

# Summary statistics for numerical columns
st.write(df.describe())
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Histogram of age
plt.figure(figsize=(10, 6))
sns.histplot(df['VICTIM AGE'], kde=True, bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
st.pyplot(plt.gcf())
