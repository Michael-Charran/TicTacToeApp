import streamlit as st
import numpy as np
from collections import defaultdict
import random

# ============================
# Game + RL Logic
# ============================

def empty_board():
    return " " * 9

def get_available_actions(state):
    return [i for i, s in enumerate(state) if s == " "]

def make_move(state, action, player):
    return state[:action] + player + state[action+1:]

def check_winner(state):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in wins:
        if state[a] == state[b] == state[c] != " ":
            return state[a]
    if " " not in state:
        return "cat"
    return None

# Q-learning tables
Q = defaultdict(lambda: np.zeros(9))

alpha = 0.8
gamma = 0.95
epsilon = 0.1


def choose_action(state):
    """ Choose an action during training """
    if random.random() < epsilon:
        return random.choice(get_available_actions(state))
    qvals = Q[state]
    valid = get_available_actions(state)
    return max(valid, key=lambda a: qvals[a])


def choose_best_action(state):
    """ Choose the optimal action (no randomness) for gameplay """
    valid = get_available_actions(state)
    qvals = Q[state]
    return max(valid, key=lambda a: qvals[a])


def train(games=20000):
    for g in range(games):
        state = empty_board()
        player = "X"
        visited = []

        while True:
            # Agent = X
            if player == "X":
                action = choose_action(state)
                visited.append((state, action))
            else:
                # Opponent = random
                action = random.choice(get_available_actions(state))

            next_state = make_move(state, action, player)
            winner = check_winner(next_state)

            # If game is over, backprop rewards
            if winner:
                if winner == "X": r = 1
                elif winner == "O": r = -1
                else: r = 0.5

                for s, a in reversed(visited):
                    Q[s][a] = Q[s][a] + alpha * (r - Q[s][a])
                    r *= gamma
                break

            state = next_state
            player = "O" if player == "X" else "X"

        # Streamlit progress display
        if g % 1000 == 0:
            st.session_state['train_progress'] = g

# ============================
# Streamlit UI
# ============================

st.set_page_config(page_title="RL Tic-Tac-Toe", layout="centered")

st.title("🤖 Reinforcement Learning Tic-Tac-Toe")
st.write("AI trains with Q-learning and you play against it — all locally.")

# Initialize session variables
if "trained" not in st.session_state:
    st.session_state.trained = False

if "board" not in st.session_state:
    st.session_state.board = empty_board()

if "status" not in st.session_state:
    st.session_state.status = "Your Turn"

# -------------------------
# Training Section
# -------------------------

st.header("🔧 Train the AI")

train_games = st.number_input("Number of training games:", 1000, 100000, 20000, 1000)

if st.button("Train"):
    st.write("Training, please wait...")
    progress = st.progress(0)

    for i in range(train_games):
        train(1)
        if i % (train_games // 100) == 0:
            progress.progress(int(i / train_games * 100))

    progress.progress(100)
    st.success(f"Training complete! AI trained on {train_games} games.")
    st.session_state.trained = True

# -------------------------
# Gameplay Section
# -------------------------

st.header("🎮 Play Against the AI")

def reset_board():
    st.session_state.board = empty_board()
    st.session_state.status = "Your Turn"


# Draw board
cols = st.columns(3)

def draw_button(pos, col):
    mark = st.session_state.board[pos]
    disabled = (mark != " " or st.session_state.status != "Your Turn")

    if col.button(mark if mark != " " else " ", key=f"btn{pos}", disabled=disabled):
        human_move(pos)

def human_move(pos):
    # Player = O
    st.session_state.board = make_move(st.session_state.board, pos, "O")

    winner = check_winner(st.session_state.board)
    if winner:
        st.session_state.status = "You win!" if winner == "O" else "Tie!"
        return

    ai_move()

def ai_move():
    state = st.session_state.board
    action = choose_best_action(state)
    st.session_state.board = make_move(state, action, "X")

    winner = check_winner(st.session_state.board)
    if winner:
        if winner == "X":
            st.session_state.status = "AI wins!"
        else:
            st.session_state.status = "Tie!"
    else:
        st.session_state.status = "Your Turn"


# Render buttons in 3x3 grid
draw_button(0, cols[0])
draw_button(1, cols[1])
draw_button(2, cols[2])

cols = st.columns(3)
draw_button(3, cols[0])
draw_button(4, cols[1])
draw_button(5, cols[2])

cols = st.columns(3)
draw_button(6, cols[0])
draw_button(7, cols[1])
draw_button(8, cols[2])

st.subheader(st.session_state.status)

if st.button("Reset Game"):
    reset_board()
