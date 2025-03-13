import streamlit as st
import random
import time             # provide functionalities releated to time 
import requests         # helps to call the api

st.title("Money Making Machine")

def generate_money():
    return random.randint(1,1000)                   # randint provide random number specially integer 

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting Your Money...")
    time.sleep(1)         # sleep method is used to puase the execution of program for  specific or given time.it take time in sseconds
    amount = generate_money()
    st.success(f"You've earned ${amount}!")

def fetch_side_hustle():
    try:
        response =  requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return("Freelancing,")
    except:
        return("something went wrong")

st.subheader("Side Hustle Ideas")
if st.button("Generate Hustles"):
    idea = fetch_side_hustle()
    st.success(f"Here's a side hustle idea: {idea}")

def fetch_money_quote():
    try:
        reponse = requests.get("http://127.0.0.1:8000/money_quotes")
        if reponse.status_code == 200:
            quotes = reponse.json()
            return quotes["money_quote"]
        else:
            return("Money is the root of all evil")
    except:
        return("something went wrong")

st.subheader("Money Quote")
if st.button("Generate Quote"):
    quote = fetch_money_quote()
    st.success(f"Here's a money quote: {quote}")
