import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.data_loader import load_local_csv, preprocess

st.title("📦 Inventory Dashboard")

uploaded_file = st.file_uploader("Upload inventory CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df = preprocess(df)

    st.subheader("Product Quantities by Category")
    fig1, ax1 = plt.subplots()
    sns.barplot(data=df, x="Category", y="Quantity", ax=ax1, estimator=sum, ci=None)
    ax1.set_title("Total Quantity per Category")
    st.pyplot(fig1)

    st.subheader("Restocking Schedule Over Time")
    restock_trend = df.groupby("RestockDate").size().reset_index(name='RestockCount')
    fig2, ax2 = plt.subplots()
    sns.lineplot(data=restock_trend, x="RestockDate", y="RestockCount", marker="o", ax=ax2)
    ax2.set_title("Restocking Trend")
    st.pyplot(fig2)

    st.subheader("Stock Heatmap by Warehouse Zone")
    pivot_table = df.pivot_table(values='Quantity', index='WarehouseZone', columns='Category', aggfunc='sum', fill_value=0)
    fig3, ax3 = plt.subplots()
    sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", ax=ax3)
    ax3.set_title("Warehouse Zone Stock Levels")
    st.pyplot(fig3)
else:
    st.info("Please upload a CSV file to continue.")
