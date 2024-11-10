import streamlit as st
import pandas as pd
from utils.market_data import get_market_data
from models.a3c_model import build_a3c_model, train_a3c
from utils.visualization import plot_performance
from utils.backtest import backtest_strategy
from utils.evaluation import sharpe_ratio, total_return

st.title("Reinforcement Learning for Trading - A3C")

api_key = st.text_input('94d88ac89a694d5bbbc92f49245c19a8')
symbol = st.text_input('Enter Stock Symbol:', 'AAPL')

if api_key:
    df = get_market_data(api_key, symbol)
    st.write(f"Showing data for {symbol}", df.head())

    model = build_a3c_model(state_shape=(df.shape[1],), action_space=3)
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
    train_a3c(df, model, optimizer)

    total_balance = backtest_strategy(df, model)
    plot_performance(total_balance)

    sharpe = sharpe_ratio(total_balance.pct_change())
    st.write(f"Sharpe Ratio: {sharpe}")
