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

def main():
    st.title("Tic-Tac-Toe")
    st.markdown("""
    <style>
    .stApp {
        background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRe-kCkXLA2vSiNElExHdLe3OVkYMZPKjjNgw&s');
        background-attachment: fixed;
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        min-height: 100vh;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    /* Set sidebar background color to teal */
    section[data-testid="stSidebar"] {
        background-color: teal;
    }
    section[data-testid="stSidebar"] * {
    color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    if "board" not in st.session_state:
        st.session_state.board = np.array([["" for _ in range(3)] for _ in range(3)])
        st.session_state.current_player = "X"
        st.session_state.game_over = False
        st.session_state.winner = None
        st.session_state.draw = False

    board = st.session_state.board
    current_player = st.session_state.current_player
    winner = check_winner(board)

    if winner is not None:
        st.session_state.winner = winner
        st.session_state.game_over = True
        st.switch_page("pages/Results.py")

    elif check_draw(board):
        st.session_state.draw = True
        st.session_state.game_over = True
        st.switch_page("pages/Results.py")

    # else:
    #     for row in range(3):
    #         cols = st.columns(3)
    #         for col in range(3):
    #             if board[row, col] == "":
    #                 if cols[col].button(" ", key=f"button_{row}_{col}"):
    #                     board[row, col] = current_player
    #                     st.session_state.board = board
    #                     st.session_state.current_player = "O" if current_player == "X" else "X"
    #                     st.rerun()
    #             else:
    #                 cols[col].write(board[row, col], key=f"button_{row}_{col}")

    # if st.button("Reset game"):
    #     st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    #     st.session_state.current_player = "X"
    #     st.rerun()

    if st.button("Reset Game"):
        st.session_state.board = np.array([["" for _ in range(3)] for _ in range(3)])
        st.session_state.current_player = "X"
        st.session_state.game_over = False
        st.session_state.winner = None
        st.session_state.draw = False
        st.rerun()

    st.write("### Current Player:", current_player)

    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            if cols[j].button(board[i][j] if board[i][j] != "" else " ", key=f"{i}-{j}", disabled=(board[i][j] != "" or st.session_state.game_over)):
                if not st.session_state.game_over and board[i][j] == "":
                    board[i][j] = current_player
                    st.session_state.current_player = "O" if current_player == "X" else "X"
                    st.session_state.board = board
                    st.rerun()

if __name__ == "__main__":
    main()
