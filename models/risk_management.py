def risk_management(balance, position_size, max_drawdown=0.1):
    risk = balance * max_drawdown
    max_position_size = risk / position_size
    return max_position_size
