import streamlit as st
import random

st.title("🎯 Number Guessing Game")
st.write("You have 7 chances to guess the number. Let's start!")

if 'num' not in st.session_state:
    st.session_state.num = None
if 'gc' not in st.session_state:
    st.session_state.gc = 0
if 'chances' not in st.session_state:
    st.session_state.chances = 7
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

low = st.number_input("Enter the Lower Bound:", value=1)
high = st.number_input("Enter the Upper Bound:", value=100)

if st.button("Start Game") or st.session_state.num is None:
    st.session_state.num = random.randint(low, high)
    st.session_state.gc = 0
    st.session_state.game_over = False
    st.success(f"Game started! Guess a number between {low} and {high}.")

if not st.session_state.game_over and st.session_state.num is not None:
    guess = st.number_input("Enter your guess:", value=low, min_value=low, max_value=high, step=1)
    
    if st.button("Submit Guess"):
        st.session_state.gc += 1

        if guess == st.session_state.num:
            st.balloons()
            st.success(f"🎉 Correct! The number is {st.session_state.num}. You guessed it in {st.session_state.gc} attempts.")
            st.session_state.game_over = True
        elif st.session_state.gc >= st.session_state.chances:
            st.error(f"😢 Sorry! The number was {st.session_state.num}. Better luck next time.")
            st.session_state.game_over = True
        elif guess > st.session_state.num:
            st.warning("Too high! Try a lower number.")
        elif guess < st.session_state.num:
            st.warning("Too low! Try a higher number.")

st.write(f"Attempts used: {st.session_state.gc} / {st.session_state.chances}")
