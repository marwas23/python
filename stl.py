import streamlit as st
import random
import time
st.title("Zgadnij liczbę")
st.write("Komputer losuje liczbę od 1 do 10.")
st.write("Spróbuj ją odgadnąć!")

liczba = st.number_input(
    "Twój wybór:",
    min_value=1,
    max_value=10,
    value=5,
)
if st.button("Sprawdź"):
    wynik = st.empty()

    for i in range(3, 0,-1):
        wynik.write(f"Losowanie za {i}...")
        time.sleep(1)

    los = random.randint(1,10)

    wynik.write(f"Wylosowano: {los}")
    if liczba == los:
        st.success("Brawo! Wygrałeś!")
        st.balloons()
    else:
        st.error("Niestety, nie trafiłeś!")