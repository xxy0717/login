import streamlit as st
from game import Game

# Set page title
st.set_page_config(page_title="围棋游戏", page_icon=":memo:", layout="wide")

# Create a new game
game = Game()

# Title
st.title("围棋游戏")

# Sidebar
st.sidebar.title("游戏设置")
difficulty = st.sidebar.slider("请选择机器的围棋水平", 1, 10, 5)

# Main content
if st.button("开始新游戏"):
    game.start_game(difficulty)

if game.started:
    # Draw the board
    st.write("当前棋局：")
    st.image(game.draw_board(), use_column_width=True)

    # Check if game is over
    if game.check_game_over():
        st.write("游戏结束！")
        if game.winner is None:
            st.write("平局！")
        else:
            st.write(f"{game.winner} 获胜！")

    # Check if it's the machine's turn
    elif game.turn == Game.MACHINE:
        st.write("机器正在思考中...")
        game.make_move()

    # Let the user make a move
    else:
        col, row = st.number_input("请输入你的落子位置（例如：3,4）", value=(0, 0), step=1)
        if st.button("下子"):
            game.make_move((col, row))
