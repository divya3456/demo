import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of Flowers")
col1,col2=str2.columns(2)
with col1:
  st.subheader("Flower Image1:")
  st.image("./image1.jpg",caption="Flower1", width="300",use_column_width=True)
  st.write("Flowers  are  Beautiful:")
with col2:
  st.subheader("Flower Image2:")
  st.image("./image2.jpg",caption="Flower2", width="300",use_column_width=True)
  st.write("Flowers  are  Beautiful:")
