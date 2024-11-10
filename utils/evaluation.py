import numpy as np

def sharpe_ratio(returns, risk_free_rate=0.0):
    excess_returns = returns - risk_free_rate
    return np.mean(excess_returns) / np.std(excess_returns)

def total_return(balance, initial_balance=10000):
    return (balance[-1] - initial_balance) / initial_balance
