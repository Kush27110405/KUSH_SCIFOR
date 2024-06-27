import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(layout="wide")



st.title("My first app in Streamlit by Kush")
st.title('_Streamlit_ is :blue[cool] :sunglasses:')
st.write("My first attempt at creating a table:")
df = pd.DataFrame({
    'first column' : [1, 2, 3, 4],
    'second column' : [10, 20, 30, 40]
    
})

st.write(df)

option = st.sidebar.selectbox(
    "Which number do you like best?",
    df['first column']
)

"You selected:", option

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

df = pd.DataFrame(
    np.random.randn(10, 20),
    columns = ('col %d' % i for i in range(20))
)

st.dataframe(df.style.highlight_max(axis = 0))
st.table(df)
if st.checkbox("Show chart:"):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ['a', 'b', 'c']
    )
    st.bar_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns = ['lat', 'lon']
)
st.map(map_data)

x = st.sidebar.slider('x',key="x")
st.write(x, "Squared is", x * x)

st.text_input("Your name",key="name")

st.session_state.x

add_selectbox = st.sidebar.selectbox(
    "How would u like to be contacted?",
    ('Email', 'Home Phone', 'Mobile Phone')
)

"You would like to be contacted by:", add_selectbox

add_slider = st.sidebar.slider(
    "Select a range of values:",
    0.0, 100.0, (25.0, 75.0)
)

"Range: ", add_slider

left_column, right_column = st.columns(2)
left_column.button("Press me!")

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffinndor", "Ravenclaw", "Hufflepuff", "Slytherin")

    )
    st.write(f"You are in {chosen} house")

"Starting a long computation: ......"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i + 1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"..... and now we're done!"

#st.image("superset photo.jpg", caption="Myself", width= 600)
