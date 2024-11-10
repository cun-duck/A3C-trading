import pandas as pd

def backtest_strategy(df, model, risk_management, initial_balance=10000):
    balance = initial_balance
    position = 0
    total_balance = []

    for idx, row in df.iterrows():
        action = model.predict(row.values)
        if action == 1:  # Long position
            position = balance / row['close']
            balance = 0
        elif action == -1:  # Short position
            position = -balance / row['close']
            balance = 0
        elif action == 0:  # Close position
            balance = position * row['close']
            position = 0

        total_balance.append(balance + position * row['close'])

    return pd.Series(total_balance, name="Total Balance")
