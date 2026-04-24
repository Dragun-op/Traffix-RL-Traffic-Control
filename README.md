# RL Traffic Control

##  Overview
This project implements a **Reinforcement Learning (RL)** based traffic signal control system using **Q-Learning** in a SUMO simulation environment. The goal is to reduce congestion by learning optimal traffic signal switching policies based on real-time traffic conditions.

---

## Methodology

### Algorithm
- Q-Learning (Tabular Reinforcement Learning)

###  State Space
- Defined as the **maximum queue length** observed in each lane/approach of the junction.

###  Action Space
Discrete actions (4 total):
- `0` → Stay on current green phase  
- `1` → Switch to next green phase  
- `2` → Switch to next-to-next green phase  
- `3` → Switch to next-to-next-to-next green phase    

---

##  Training Details

###  Training Files
- `rl1.ipynb`
- `rl2.ipynb`

Both notebooks are used to train the RL agent on the same environment:

- **Environment:** `jun1.sumocfg`  
- **Algorithm:** Q-Learning  

###  Key Differences:
- Episode size  
- Epsilon decay strategy  

---

##  Exploration Strategy
- **Epsilon decay (ε-decay)** used for balancing exploration and exploitation  
- **n-step bootstrapping** applied to improve learning efficiency and stability  

---

##  Evaluation & Comparison

###  Evaluation Files
- `model_gui.ipynb`
- `model_gui1.ipynb`

These notebooks:
- Compare RL model performance against a **baseline traffic control strategy**
- Provide visual and analytical insights into system performance  

---

##  Models
- Trained models are stored as `.pkl` files:
  - `rl_model_1.pkl`
  - `rl_model_2.pkl`

---

##  Implementation Note
**All reinforcement learning components, including Q-learning formulation, state-action design, training, and evaluation in SUMO, were implemented entirely by me.**

---

##  Project Context
- Developed as part of a **project-based academic initiative (PBL) named Traffix** 
- **The entire reinforcement learning pipeline, SUMO–TraCI integration, and dataset generation were independently designed and implemented by me (Akshat Kumar).**
- Focused on applying RL techniques to real-world traffic optimization problems  

---

##  Setup Notes
- SUMO must be installed and properly configured  
- File paths in code may need adjustment based on your system  
- Ensure SUMO environment variables are correctly set  

---

##  Future Improvements
- Extend to **Deep Q-Networks (DQN)**  
- Multi-intersection traffic coordination  
- Integration with real-world traffic datasets  
- Advanced reward shaping and state representations  

---

##  Objective
To design an intelligent traffic signal controller that minimizes congestion and improves traffic flow using reinforcement learning.

---
