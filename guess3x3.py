import streamlit as st
from random import *

hide_menu = """
<style>
/* #MainMenu { 
     visibility: hidden; 
} */

footer {
    visibility: visible;
}
footer:after{
    content:"By: Oswaldo Cadenas, 2022";
    display: block;
    position: relative;
    color: tomato;
}
</style>
"""

st.title("Simple guessing game")
st.markdown(hide_menu, unsafe_allow_html=True)

N = 9
guess = randint(1, 9)
if 'guess' not in st.session_state:
    st.session_state['guess'] = guess
st.markdown(f"Guess position with the hidden value of **{st.session_state['guess']}**; you got 4 attempts")

attempts = 0

def play_again():
    for key in st.session_state.keys():
        del st.session_state[key]


if 'attempts' not in st.session_state:
    st.session_state['attempts'] = 0

if 'won' not in st.session_state:
    st.session_state['won'] = False

def f(lkey, m):
    if lkey not in st.session_state:
        return
    else:
        if st.session_state[lkey] == True:
            m[lkey] = True
            st.session_state['attempts'] += 1
        else:
            pass

if 'mask' not in st.session_state:
    mask = {}
    for i in range(1, N+1):
        lkey = 'b' + str(i)
        mask[lkey] = False
    st.session_state['mask'] = mask

numbers = list(range(1, N+1))
shuffle(numbers)

if 'numbers' not in st.session_state:
    st.session_state['numbers'] = numbers

col1, col2, col3 = st.columns((1,1,1))

with col1:
    positions1 = list(range(1, 10, 3)) 
    for i in range(3):
        cell = st.empty()
        pos = positions1[i]
        lkey = 'b' + str(pos)
        lmask = st.session_state['mask']
        with cell:
            cell.button(label = str(pos), key=lkey, on_click=f(lkey, lmask))
            lnumbers = st.session_state['numbers']
            if lmask[lkey] == True:
                cell.markdown(f':red[{lnumbers[pos-1]}]')
                if st.session_state['guess'] == lnumbers[pos-1]:
                    st.session_state['won'] = True
                
        
with col2:
    positions2 = list(range(2, 10, 3)) 
    for i in range(3):
        cell = st.empty()
        pos = positions2[i]
        lkey = 'b' + str(pos)
        lmask = st.session_state['mask']
        with cell:
            cell.button(label=str(pos), key=lkey, on_click=f(lkey, lmask))
            lnumbers = st.session_state['numbers']
            if lmask[lkey] == True:
                cell.markdown(f':red[{lnumbers[pos-1]}]')
                if st.session_state['guess'] == lnumbers[pos-1]:
                    st.session_state['won'] = True
        

with col3:
    positions3 = list(range(3, 10, 3)) 
    for i in range(3):
        cell = st.empty()
        pos = positions3[i]
        lkey = 'b' + str(pos)
        lmask = st.session_state['mask']
        with cell:
            st.button(str(pos), key=lkey, on_click=f(lkey, lmask))
            lnumbers = st.session_state['numbers']
            if lmask[lkey] == True:
                cell.markdown(f':red[{lnumbers[pos-1]}]')
                if st.session_state['guess'] == lnumbers[pos-1]:
                    st.session_state['won'] = True

final_message = st.empty()
with final_message:
    final_message.write(f"Attempts left: {4-st.session_state['attempts']}")
    if st.session_state['won'] == True:
        final_message.write(f'You won, fab!')
    if st.session_state['attempts'] == 4:
        final_message.write(f'Sorry, game over!')

# st.write(f"Winning: {st.session_state['won']}")
# st.write(f"Numbers: {st.session_state['numbers']}")
# st.write(f"Guess: {st.session_state['guess']}")

st.button(label = "Play again", on_click=play_again)

with st.expander("How to play"):
    st.write("Each button at positions 1 to 9 hides a number from 1 to 9")
    st.write("Click on a position to reveal the hidden number")
    st.write("If your choice reveals the number to guess, you win")
    st.write("That is, if you guess in less 4 guesses at most, otherwise you lose")

    # st.metric(label="", value=numbers[0])
# st.write(f'State')
# st.write(st.session_state)
# st.write(f'Mask')
# st.write(st.session_state['mask'])


