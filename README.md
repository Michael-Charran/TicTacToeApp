Tic-Tac-Toe Reinforcement Learning with Streamlit
Overview

This project implements a Reinforcement Learning (Q-Learning) agent that learns to play Tic-Tac-Toe.
It features an interactive web interface built with Streamlit allowing you to:

Train the AI by simulating thousands of games locally

Play against the trained AI in your browser

See game status and reset anytime

Everything runs locally on your machine—no external APIs or internet connection needed.



Features


Q-Learning algorithm for training the Tic-Tac-Toe AI


Configurable number of training games via Streamlit UI


Clickable 3x3 grid to play against AI


AI plays as "X", user plays as "O"


Real-time game status updates (win, lose, tie)


Reset board to start new games easily


Fully self-contained with no dependencies beyond standard Python libraries and Streamlit



Getting Started
Prerequisites


Python 3.10 or 3.11 (recommended for compatibility)


Streamlit library installed (pip install streamlit)


Installation


Clone or download this repository.


(Optional) Create and activate a virtual environment:


python -m venv venv
# On Windows (PowerShell):
venv\Scripts\Activate.ps1
# On Linux/macOS:
source venv/bin/activate



Install required packages:


pip install streamlit numpy

Running the App
Run the Streamlit app with:
streamlit run app.py

Your default web browser will open the interface at:
http://localhost:8501


Usage


Train the AI:
Use the "Train the AI" section to run simulations. More training games generally improve AI skill.


Play the Game:
Click on empty squares to make your move. The AI will respond automatically.


Reset:
Use the "Reset Game" button to clear the board and start a new game.



How It Works
The AI uses Q-learning, a reinforcement learning technique, to learn optimal moves by simulating games against a random opponent.


Each state (board configuration) maps to Q-values for each possible move.


The AI updates its knowledge with rewards for winning (+1), losing (-1), or drawing (+0.5).


Over many simulated games, the AI converges towards optimal play.



Project Structure


app.py: Main Streamlit application with RL logic and UI


Dependencies: streamlit, numpy



Future Improvements


Visualize Q-values and training progress graphs


Add AI vs AI mode to watch games play out


Improve UI/UX with colors and animations


Save/load trained models for persistent AI learning



License
This project is open source and free to use under the MIT License.

Contact
For questions or suggestions, feel free to reach out!

If you want me to generate a version with markdown formatting, badges, or for GitHub specifically, just ask!
