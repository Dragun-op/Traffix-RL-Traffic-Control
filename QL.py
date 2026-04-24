import numpy as np
import random
from collections import defaultdict
def default_q():
    return np.zeros(4)
class QLearningAgent:
    def __init__(self, state_size, action_size, alpha, gamma, epsilon, epsilon_decay, epsilon_min):
        
        self.state_size = state_size
        self.action_size = action_size
        self.alpha = alpha    
        self.gamma = gamma        
        self.epsilon = epsilon    
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.q_table = defaultdict(default_q)
    
    def to_tuple(self, state):
        return tuple(state)

    def choose_action(self, state):
        state = self.to_tuple(state)
        if random.random() < self.epsilon:
            return random.randint(0, self.action_size - 1)
        else:
            q_values = self.q_table[state]
            max_q = np.max(q_values)
            actions = np.where(q_values == max_q)[0]
            return random.choice(actions)

    def update(self, state, action, reward, next_state, done,power=1):
        state = self.to_tuple(state)  
        next_state = self.to_tuple(next_state)
        old_q = self.q_table[state][action]                           #added done for termial
        target = reward
        if not done:
            target += (self.gamma**power)* np.max(self.q_table[next_state])
        self.q_table[state][action] += self.alpha * (target - self.q_table[state][action])
        new_q = self.q_table[state][action]
        return abs(new_q - old_q)

    def decay_epsilon(self):
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)