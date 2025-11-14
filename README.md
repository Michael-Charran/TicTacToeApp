# Tic-Tac-Toe Reinforcement Learning with Streamlit

## Overview

This project implements a **Reinforcement Learning (Q-Learning) agent** that learns to play Tic-Tac-Toe.  
It features an interactive web interface built with **Streamlit** allowing you to:

- Train the AI by simulating thousands of games locally  
- Play against the trained AI in your browser  
- See game status and reset anytime  

Everything runs **locally on your machine**—no external APIs or internet connection needed.

## Features

- **Q-Learning algorithm** for training the Tic-Tac-Toe AI  
- Configurable number of training games via Streamlit UI  
- Clickable 3x3 grid to play against AI  
- AI plays as "X", user plays as "O"  
- Real-time game status updates (win, lose, tie)  
- Reset board to start new games easily  
- Fully self-contained with no dependencies beyond standard Python libraries and Streamlit  

## Getting Started

### Prerequisites

- Python 3.10 or 3.11 (recommended for compatibility)  
- Streamlit library installed (`pip install streamlit numpy`)

### Installation

1. Clone or download this repository.

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
# On Windows (PowerShell):
venv\Scripts\Activate.ps1
# On Linux/macOS:
source venv/bin/activate
