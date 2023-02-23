import streamlit as st
from game import Game

st.set_page_config(page_title='Weiqi Game')

# Define game modes
HUMAN_VS_HUMAN = 'Human vs. Human'
HUMAN_VS_AI = 'Human vs. AI'

# Define default settings
DEFAULT_MODE = HUMAN_VS_AI
DEFAULT_AI_LEVEL = 2

def main():
    st.title('Weiqi Game')
    mode = st.sidebar.radio('Select game mode:', (HUMAN_VS_HUMAN, HUMAN_VS_AI), index=1)

    if mode == HUMAN_VS_HUMAN:
        st.warning('Human vs. Human mode is not yet supported.')
    else:
        ai_level = st.sidebar.slider('Select AI level (1-5):', 1, 5, DEFAULT_AI_LEVEL)
        game = Game(mode=mode, ai_level=ai_level)
        game.run()

if __name__ == '__main__':
    main()
