import steamlit as st

x = st.slider("select a value")
st.write(x, 'is a square ', x * x)