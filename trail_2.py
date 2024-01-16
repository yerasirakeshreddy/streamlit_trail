#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

def main():
    st.title("Basic Streamlit App Example")

    # Sidebar for user input
    number = st.sidebar.number_input("Select a number", value=1, step=1)

    # Calculate square and cube
    square = number ** 2
    cube = number ** 3

    # Display the results
    st.write(f"Square of {number}: {square}")
    st.write(f"Cube of {number}: {cube}")

    # Additional text
    st.markdown("### Additional Information")
    st.write("This is a simple Streamlit app example.")

if __name__ == "__main__":
    main()

