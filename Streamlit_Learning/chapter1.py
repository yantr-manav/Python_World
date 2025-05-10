import streamlit as st

st.title("Hello World!")
st.subheader("This is   a sample Streamlit App")
st.text("This is simple text")
st.write("This is a write function")

chai = st.selectbox("Select a Chai for yourself:",["Masala chai","Garam chai","lemon chai","Kesar chai"])
st.write("you selected: ",chai)
st.success("Your selected chai is on the way!")
 