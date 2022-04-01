import streamlit as st

st.title('Hello world')


st.metric('My metric', 50,  2)

clicked = st.button('Cluck button')



date = st.date_input("Pick a date")
st.title(date)

time = st.time_input('Meeting time')



profesion = st.radio(
     "Нравится ли вам наш курс",
     ('Да', 'Конечно', 'Естественно'))


if st.button('Result'):
     st.write('Вы дошли до конца сайта')

