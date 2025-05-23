import streamlit as st

# Initialize tracking if not already present
if "score_x" not in st.session_state:
    st.session_state.score_x = 0
if "score_o" not in st.session_state:
    st.session_state.score_o = 0
if "score_draw" not in st.session_state:
    st.session_state.score_draw = 0

# Read result of the current game
winner = st.session_state.get("winner", None)
draw = st.session_state.get("draw", False)

# Apply animated background and ensure buttons are always visible
st.markdown("""
<style>
@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
.stApp {
    background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a1c4fd);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    min-height: 100vh;
    color: white;
    text-align: center;
}
/* Ensure buttons are always visible */
.stButton > button {
    background-color: white !important;
    color: black !important;
    font-weight: bold;
    padding: 0.75em 2em;
    border-radius: 8px;
    border: 2px solid #333;
    opacity: 1 !important;
    visibility: visible !important;
    transition: none !important;
    z-index: 9999 !important;
}
.stButton > button:hover {
    background-color: #f0f0f0 !important;
    color: black !important;
}
h1 {
    font-size: 3.5em;
    margin-top: 2em;
}
</style>
""", unsafe_allow_html=True)

# Update session stats based on result
if winner == "X":
    st.session_state.score_x += 1
elif winner == "O":
    st.session_state.score_o += 1
elif draw:
    st.session_state.score_draw += 1

# Show result message
if winner:
    st.markdown(f"<h1>🎉 Player {winner} Wins! 🎉</h1>", unsafe_allow_html=True)
elif draw:
    st.markdown("<h1>🤝 It's a Draw! 🤝</h1>", unsafe_allow_html=True)
else:
    st.warning("No game result found. Please play the game first.")

# Show cumulative session score
st.markdown("## 🧮 Session Scoreboard")
st.markdown(f"- Player X Wins: **{st.session_state.score_x}**")
st.markdown(f"- Player O Wins: **{st.session_state.score_o}**")
st.markdown(f"- Draws: **{st.session_state.score_draw}**")

# Play again resets board but keeps score
if st.button("Play Again"):
    for key in ["board", "current_player", "game_over", "winner", "draw"]:
        if key in st.session_state:
            del st.session_state[key]
    st.switch_page("tic_tac_toe_streamlit.py")

# Optionally add a reset button for scores
if st.button("Reset Session Score"):
    st.session_state.score_x = 0
    st.session_state.score_o = 0
    st.session_state.score_draw = 0
    st.success("Scoreboard has been reset!")
