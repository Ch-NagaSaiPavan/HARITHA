import streamlit as st
from fluent.runtime import FluentBundle, FluentResource
import page1
import page2
import page3
import page4

# Set up the Streamlit page title
st.title("Fluent Translator System Testing Interface")
st.write("An interactive interface to run system tests on the Fluent Translator")

# Initialize the FluentBundle with a default locale
st.subheader("1. Initialize Fluent Bundle")
locale = st.text_input("Enter locale (e.g., en-US):", "en-US")
bundle = page1.create_bundle(locale)

# Load translation text
st.subheader("2. Load Translation Text")
translation_text = st.text_area(
    "Enter translation text in Fluent format (e.g., 'hello = Hello, { $name }!'):",
    "hello = Hello, { $name }!\nbye = Goodbye, { $name }!"
)
if st.button("Load Translation"):
    try:
        page2.load_translation(bundle, translation_text)
        st.success("Translation loaded successfully!")
    except Exception as e:
        st.error(f"Failed to load translation: {e}")

# Set up test cases
st.subheader("3. Define and Run Test Cases")

# Test Case 1: Translation with variable
st.write("**Test Case 1**: Translation with a variable")
name = st.text_input("Enter name for Test Case 1:", "Alice")
test_variables_1 = {"name": name}
message_id_1 = "hello"

if st.button("Run Test Case 1"):
    output_1 = page4.format_output(bundle, message_id_1, test_variables_1)
    st.write("Expected Output: Hello, Alice!")
    st.write(f"Actual Output: {output_1}")
    if output_1 == f"Hello, {name}!":
        st.success("Test Case 1 Passed")
    else:
        st.error("Test Case 1 Failed")

# Test Case 2: Translation without variable
st.write("**Test Case 2**: Translation with a missing variable")
message_id_2 = "hello"

if st.button("Run Test Case 2"):
    output_2 = page4.format_output(bundle, message_id_2, {})
    st.write("Expected Output: (Should handle missing variable gracefully)")
    st.write(f"Actual Output: {output_2}")
    if "Hello," in output_2:
        st.success("Test Case 2 Passed")
    else:
        st.error("Test Case 2 Failed")

# Test Case 3: Invalid message ID
st.write("**Test Case 3**: Request translation with an invalid message ID")
message_id_3 = "invalid_id"

if st.button("Run Test Case 3"):
    output_3 = page4.format_output(bundle, message_id_3, test_variables_1)
    st.write("Expected Output: Message not found.")
    st.write(f"Actual Output: {output_3}")
    if output_3 == "Message not found.":
        st.success("Test Case 3 Passed")
    else:
        st.error("Test Case 3 Failed")

# Test Case 4: Translation with extra variable
st.write("**Test Case 4**: Translation with an extra, unused variable")
test_variables_4 = {"name": name, "extra": "extra_value"}
message_id_4 = "hello"

if st.button("Run Test Case 4"):
    output_4 = page4.format_output(bundle, message_id_4, test_variables_4)
    st.write("Expected Output: Hello, Alice!")
    st.write(f"Actual Output: {output_4}")
    if output_4 == f"Hello, {name}!":
        st.success("Test Case 4 Passed")
    else:
        st.error("Test Case 4 Failed")

st.write("System testing for Fluent Translator completed. Modify inputs above to test additional cases.")
