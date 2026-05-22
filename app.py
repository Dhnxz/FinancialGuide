import streamlit as st

from database import conn, cursor

from auth import (
    hash_password,
    verify_password
)

from jwt_handler import create_token

# Page Config

st.set_page_config(
    page_title="Financial Guide",
    page_icon="💰"
)

# Title

st.title("💰 Financial Guide")

# Sidebar Menu

menu = st.sidebar.selectbox(
    "Menu",
    ["Register", "Login"]
)

# ---------------- REGISTER ---------------- #

if menu == "Register":

    st.subheader("Create Account")

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Register"):

        hashed = hash_password(password)

        try:

            cursor.execute(
                """
                INSERT INTO users
                (username,password)

                VALUES (?,?)
                """,

                (username, hashed)
            )

            conn.commit()

            st.success(
                "Registration Successful"
            )

        except:

            st.error(
                "Username already exists"
            )

# ---------------- LOGIN ---------------- #

if menu == "Login":

    st.subheader("Login")

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        cursor.execute(
            """
            SELECT password
            FROM users
            WHERE username=?
            """,

            (username,)
        )

        data = cursor.fetchone()

        if data:

            stored_password = data[0]

            try:
                verified = verify_password(
                    password,
                    stored_password
                )
            except Exception as exc:
                print(
                    "Login verify_password exception:",
                    repr(exc),
                    type(stored_password),
                    repr(stored_password)[:120]
                )
                st.error("Unexpected login error. Check app logs.")
                verified = False

            if verified:

                token = create_token(
                    username
                )

                st.session_state[
                    "token"
                ] = token

                st.session_state[
                    "username"
                ] = username

                # AUTO REDIRECT

                st.switch_page(
                    "pages/dashboard.py"
                )

            else:

                st.error(
                    "Wrong Password"
                )

        else:

            st.error(
                "User Not Found"
            )