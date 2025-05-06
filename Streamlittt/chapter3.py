import streamlit as st

st.title("Chai Taste Poll")
left_col,right_col = st.columns(2)

with left_col:
    st.header("Masala Chai")
    st.image("https://render.fineartamerica.com/images/rendered/search/canvas-print/8/8/mirror/break/images/artworkimages/medium/1/cup-of-chai-art-by-linda-woods-linda-woods-canvas-print.jpg", width=200)
    vote1 = st.button("Vote Masala chai")

with right_col:
    st.header("Adrak Chai")
    st.image("https://render.fineartamerica.com/images/rendered/search/framed-print/images-medium-5/antique-teacup-in-the-woods-edward-fielding.jpg?imgWI=7&imgHI=10&sku=CRQ13&mat1=PM918&mat2=&t=2&b=2&l=2&r=2&off=0.5&frameW=0.875", width=175)
    vote2 = st.button("Vote Adrak chai")
    
    
if vote1:
        st.success("Thanks for voting for Masala chai!")
elif vote2:
        st.success("Thanks for voting for Adrak chai!")
        
        
        
name = st.sidebar.text_input("Enter your name :")
tea = st.sidebar.selectbox("choose your chai",["Masala chai","Adrak chai","Kesar chai"])

st.write(f"Welcome {name}, you have selected {tea} as your chai")

with st.expander("Show Chai Recepie"):
    st.write("""
             1.Boil water with tea leaves.\n
             2.Add milk and sugar to taste.\n
             3.Add spices like cardamom, ginger, or cloves.\n
             4.Simmer for a few minutes.\n
             5.Strain and serve hot.
             """)
    
    
st.markdown('## Chai Ingredients')
st.markdown("""
             > # Blockquote: Chai Ingredients\n
             - Tea powder\n
             - Water\n
             - Tea leaves\n
             - Milk\n
             - Sugar\n
             - Spices (optional)\n
             """)