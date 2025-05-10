import streamlit as st


st.title("Chai Maker")
if st.button("Make chai"):
    st.success("Chai is ready!")    



add_masala = st.checkbox("Add masala")

if add_masala: 
    st.write("Masala is added!")

    

tea_type = st.radio("Pick your chai base?", ["Milk", "Sugar", "tea powder"])
st.write(f"you selected: { tea_type}")

flavor = st.selectbox("Add flavor?",["Cardamon","Ginger","Lemon","Tulsi","Kesar"])
st.write(f"you selected:{flavor}")

sugar = st.slider("Add sugar level?", 0, 5, 1)
st.write(f"you selected:{sugar}")

num_input = st.number_input("Add water level?", min_value =1,max_value= 10,step= 1)
st.write(f"you selected:{num_input}")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello {name}, your chai is on the way!")
    
dob = st.date_input("Enter your date of birth")
if dob:
    st.write(f"Your date of birth is: {dob}")



