import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# -------------------------------
# TITLE & INTRO
# -------------------------------
# st.title() makes a large title at the top of the page
st.title("Affordable Housing Analysis")
st.subheader("An analysis of the stuff that I analyzed")
st.write("This app displays many interactive elements that give insight into the data I analyzed.")


df = pd.read_csv('Affordable_Housing_by_Town_2011-2022.csv', encoding='latin-1')
df2=pd.read_csv("housing_price_dataset.csv", encoding='latin1')
st.header("3. Charts and Plots")
sns.set_style("darkgrid")
sns.set_palette(["#4d217a"])
fig, ax = plt.subplots()
sns.histplot(df["Percent Affordable"], bins=20, color="#4d217a", alpha=0.8, ax=ax)
ax.set_title("Distribution of Housing Affordability", fontsize=14, color="#1b1534")
ax.set_xlabel("Percent Affordable (%)", fontsize=12, color="#312e34")
ax.set_ylabel("Frequency", fontsize=12, color="#312e34")
ax.grid(True, color="#e6e6e6")
st.pyplot(fig)


sqft_min, sqft_max = int(df2["SquareFeet"].min()), int(df2["SquareFeet"].max())
price_min, price_max = int(df2["Price"].min()), int(df2["Price"].max())

sqft_range = st.slider("Square Feet", sqft_min, sqft_max, (sqft_min, sqft_max))
price_range = st.slider("Price ($)", price_min, price_max, (price_min, price_max))

# Filter the data
filtered = df2[
    df2["SquareFeet"].between(*sqft_range) &
    df2["Price"].between(*price_range)
]

# Plot
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(filtered["SquareFeet"], filtered["Price"], alpha=0.6)
ax.set_title("Home Size vs Price")
ax.set_xlabel("Square Feet")
ax.set_ylabel("Price ($)")
ax.grid(True)

st.pyplot(fig)

st.title("Average Price by Number of Bedrooms")

# Group and compute average price
bedroom_avg = df2.groupby("Bedrooms")["Price"].mean()

# Create figure
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(bedroom_avg.index, bedroom_avg.values, color="#4d217a", alpha=0.8)
ax.set_title("Average Price by Number of Bedrooms")
ax.set_xlabel("Number of Bedrooms")
ax.set_ylabel("Average Price ($)")
ax.grid(axis='y')
st.pyplot(fig)