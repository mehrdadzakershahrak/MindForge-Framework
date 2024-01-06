import streamlit as st
from web_decision_making import main

st.title('MindForge Framework Interface')

user_query = st.text_input("What would you like to discuss? ")

if st.button('Process Query'):
    if user_query:
        with st.spinner('Processing...'):
            outputs = main(user_query)

            # Display each step's output
            for step, output in outputs:
                st.subheader(f"Output from {step.capitalize()}:")
                st.write(output)
    else:
        st.warning('Please enter a query to process.')
