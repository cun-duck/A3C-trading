def run_experiment(model, env, episodes=100):
    rewards = []
    for _ in range(episodes):
        state = env.reset()
        done = False
        total_reward = 0
        while not done:
            action = model.predict(state)
            next_state, reward, done, _ = env.step(action)
            total_reward += reward
            state = next_state
        rewards.append(total_reward)
    return np.mean(rewards)
