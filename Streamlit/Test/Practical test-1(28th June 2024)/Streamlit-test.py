import streamlit as st

st.title("Streamlit-Practical Test")
st.image("pexels-markusspiske-965345.jpg", caption="I love to code", width= 300)
x = st.slider('Choose a number from 1 to 10:', 1.0, 10.0 )



option = st.selectbox("Do you want your chosen number to be displayed?", ("Yes", "No"))

choose = st.button("Submit!")

if choose and option == "Yes":
    "You chose:", x
if choose and option == "No":
    "You chose your number not to be displayed"




