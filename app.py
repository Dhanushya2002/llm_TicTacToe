import streamlit as st
import numpy as np

def check_winner(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != "":
            return row[0]
    for col in board.T:
        if len(set(col)) == 1 and col[0] != "":
            return col[0]
    if len(set(board.diagonal())) == 1 and board[0, 0] != "":
        return board[0, 0]
    if len(set(np.fliplr(board).diagonal())) == 1 and board[0, 2] != "":
        return board[0, 2]
    return None

def check_draw(board):
    return not np.any(board == "")

def reset_game():
    st.session_state.board = np.full((3, 3), "", dtype=str)
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.draw = False

def main():
    st.set_page_config(page_title="Tic Tac Toe", layout="centered")
    st.markdown("<h1 style='text-align: center; color: teal;'>🎮 Tic Tac Toe</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Click a cell to make your move. X goes first!</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Initialize session state
    if "board" not in st.session_state:
        reset_game()

    board = st.session_state.board
    current_player = st.session_state.current_player

    # Display board
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            if cols[j].button(board[i][j] if board[i][j] else " ", key=f"{i}-{j}"):
                if board[i][j] == "" and not st.session_state.winner and not st.session_state.draw:
                    board[i][j] = current_player
                    winner = check_winner(board)
                    if winner:
                        st.session_state.winner = winner
                    elif check_draw(board):
                        st.session_state.draw = True
                    else:
                        st.session_state.current_player = "O" if current_player == "X" else "X"

    # Display status
    if st.session_state.winner:
        st.success(f"🏆 Player {st.session_state.winner} wins!")
    elif st.session_state.draw:
        st.info("It's a draw!")

    # Reset button
    if st.button("🔁 Restart Game"):
        reset_game()

if __name__ == "__main__":
    main()
