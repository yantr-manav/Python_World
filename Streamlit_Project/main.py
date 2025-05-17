import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


3+4

"hello world"


pressed = st.button("Click me!")

st.title("Hello Streamlit")
st.header("This is a header")
st.subheader("This is a subheader")
st.write("This is a simple Streamlit app.")
st.markdown(" ``` This is a markdown header```")
st.markdown("This is a _markdown_ text.")
st.text("This is a text element.")  
st.latex(r'''a^2 + b^2 = c^2''')
# st.code('''import streamlit as st ```)
st.caption("This is a caption")
st.code("import streamlit as st", language="python")
code_example = """"
def greet(name):
    st.write(f"hello{name}")
"""
st.code(code_example,language = "python")

st.divider()

st.write("This is a simple Streamlit app.")


st.image(os.path.join(os.getcwd(),"static", "github_banner.png"), caption="Wanna give up?..Never ever think of it!",use_column_width=True) 