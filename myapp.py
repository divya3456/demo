import streamlit as st
st.set_page_config(page_title='Flowers')
st.header("Types of Flowers" style="text-align:center")
col1,col2,col3=st.columns(3)
with col1:
  st.subheader("Lotus:")
  st.image("./image1.jpg",caption="Flower1", width="300",use_column_width=True)
  st.write("Flowers  are  Beautiful:")
with col2:
  st.subheader("Sunflower:")
  st.image("./image2.jpg",caption="Flower2", width="300",use_column_width=True)
  st.write("Sunflower rotates towards Sun:")
with col3:
  st.subheader("Rose:")
  st.image("./image3.jpg",caption="Flower3",width="300",use_column_width=True)
  st.write("Roses  are colorful") 
