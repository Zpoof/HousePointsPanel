import streamlit as st
import requests

# Define correct username and password
CORRECT_USERNAME = "Admin"
CORRECT_PASSWORD = "Shri@123"

# Define login function
def login(username, password):
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        return True
    else:
        return False

# Define function to get data from Firebase
def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.write("Error retrieving data.")
        return None

# Define app layout
def app():
    # Define login page
    def login_page():
        st.title("Login")
        with st.form(key='login_form'):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit_button = st.form_submit_button(label='Login')
            if submit_button and login(username, password):
                st.session_state.logged_in = True
                st.write("Login successful!")
                st.experimental_rerun()
            elif submit_button:
                st.write("Invalid username or password.")

    # Define panel page
    def panel():
        url = "https://housepoints-5d82e-default-rtdb.asia-southeast1.firebasedatabase.app/points.json"
        st.title("Edit House Points")
        data = get_data(url)
        new_data = data
        if data:
            with st.form(key='House Points'):
                new_data[0] = st.number_input(label = "Himgiri", value = data[0])
                new_data[1] = st.number_input(label = "Sagar", value = data[1])
                new_data[2] = st.number_input(label = "Srishti", value = data[2])
                new_data[3] = st.number_input(label = "Vasundhara", value = data[3])
                
                submit_button = st.form_submit_button(label='Save Changes')
                if submit_button:
                    response = requests.put(url, json=new_data)
                    if response.status_code == 200:
                        st.success("Saved", icon="✅")
                    else:
                        print(f"PUT request failed with status code {response.status_code}")
        else:
            st.write("No data available.")
        st.button("Logout", on_click=lambda: setattr(st.session_state, "logged_in", False))

    # Check if user is logged in
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        panel()
    else:
        login_page()

if __name__ == '__main__':
    st.set_page_config(page_title="House Points Aravali", page_icon = "Shri.png")
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    app()
