import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Selectbox for operation
operation = st.selectbox("Choose an operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Button to perform the calculation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division by zero is not allowed!")
            result = None

    if result is not None:
        st.success(f"The result of {operation.lower()} is: {result}")

