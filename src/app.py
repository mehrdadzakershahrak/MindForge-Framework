import streamlit as st
from loop_2 import main  
# Streamlit app title
st.title('MindForge Framework Interface')

# User input
user_query = st.text_input("Enter your query:")

# Button to trigger processing
if st.button('Process Query'):
    if user_query:  # Only process if user has entered a query
        with st.spinner('Processing...'):
            # Call the main function with the user query and capture the output
            output = main(user_query)

            # Display the output
            st.write(output)
    else:
        st.warning('Please enter a query to process.')
