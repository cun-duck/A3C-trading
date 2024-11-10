import streamlit as st
import matplotlib.pyplot as plt

def plot_performance(total_balance):
    plt.plot(total_balance)
    plt.title('Performance over Time')
    plt.xlabel('Time')
    plt.ylabel('Total Balance')
    st.pyplot(plt)

def plot_trading_data(df):
    st.line_chart(df[['close']])
