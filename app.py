import streamlit as st

# Define correct username and password
CORRECT_USERNAME = "myusername"
CORRECT_PASSWORD = "mypassword"

# Define login function
def login(username, password):
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        return True
    else:
        return False

# Define app layout
def app():
    st.title("Login Page")
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        st.write("You are logged in!")
        st.button("Logout", on_click=lambda: setattr(st.session_state, "logged_in", False))
    else:
        st.write("Please log in to continue.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if login(username, password):
                st.session_state.logged_in = True
                st.write("Login successful!")
            else:
                st.write("Invalid username or password.")

if __name__ == '__main__':
    app()
