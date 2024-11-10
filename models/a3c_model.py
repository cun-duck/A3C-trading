import gym
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from gym_anytrading.envs import TradingEnv

def build_a3c_model(state_shape, action_space):
    model = tf.keras.Sequential([
        layers.Input(shape=state_shape),
        layers.Dense(64, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(action_space, activation='linear')  # Output layer
    ])
    return model

def train_a3c(env, model, optimizer, gamma=0.99, num_episodes=1000):
    for episode in range(num_episodes):
        state = env.reset()
        done = False
        total_reward = 0

        while not done:
            action = model(state).numpy().argmax()
            next_state, reward, done, _ = env.step(action)
            total_reward += reward

            with tf.GradientTape() as tape:
                q_value = model(state)[action]
                loss = -q_value

            grads = tape.gradient(loss, model.trainable_variables)
            optimizer.apply_gradients(zip(grads, model.trainable_variables))

            state = next_state

        print(f"Episode {episode}, Total Reward: {total_reward}")
