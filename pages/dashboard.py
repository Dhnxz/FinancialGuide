import streamlit as st
import pandas as pd
import random

# ---------------- AUTH CHECK ---------------- #

if "token" not in st.session_state:

    st.error("Please Login First")

    st.stop()

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Financial Dashboard",
    page_icon="💰",
    layout="wide"
)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("💰 Financial Guide")

st.sidebar.success(
    f"Logged in as {st.session_state['username']}"
)

# Logout

if st.sidebar.button("Logout"):

    del st.session_state["token"]

    del st.session_state["username"]

    st.switch_page("app.py")

# ---------------- HEADER ---------------- #

st.title("💰 Smart Financial Dashboard")

st.subheader(
    f"Welcome back, {st.session_state['username']}"
)

st.markdown(
    "Track your spending, monitor your savings, and improve your financial habits."
)

# ---------------- TOP METRICS ---------------- #

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Monthly Expenses",
    "₹25,000",
    "-5%"
)

col2.metric(
    "Savings",
    "₹15,000",
    "+12%"
)

col3.metric(
    "Budget Left",
    "₹10,000",
    "+8%"
)

col4.metric(
    "Investment Growth",
    "₹8,500",
    "+18%"
)

st.divider()

# ---------------- UNIQUE INSIGHTS ---------------- #

st.subheader("📊 Smart Financial Insights")

insight1, insight2 = st.columns(2)

with insight1:

    st.info(
        """
        🔍 Highest spending category:
        Shopping
        
        You spent 35% more on shopping this month compared to last month.
        """
    )

    st.success(
        """
        💡 Savings Tip
        
        Reducing food delivery by 2 orders/week can save nearly ₹3,000 monthly.
        """
    )

with insight2:

    st.warning(
        """
        ⚠ Budget Alert
        
        You have already used 80% of your entertainment budget.
        """
    )

    st.success(
        """
        📈 Positive Trend
        
        Your savings increased continuously for the last 3 months.
        """
    )

st.divider()

# ---------------- FINANCIAL HEALTH SCORE ---------------- #

st.subheader("💎 Financial Health Score")

score = random.randint(70, 95)

st.progress(score)

st.write(f"Your Financial Score: {score}/100")

if score > 85:

    st.success(
        "Excellent financial management! Keep maintaining your savings habits."
    )

elif score > 70:

    st.warning(
        "Good financial health. Try reducing unnecessary spending."
    )

else:

    st.error(
        "High spending detected. Consider revising your monthly budget."
    )

st.divider()

# ---------------- RECENT TRANSACTIONS ---------------- #

st.subheader("📋 Recent Transactions")

data = pd.DataFrame({

    "Category": [
        "Food",
        "Travel",
        "Shopping",
        "Bills",
        "Entertainment"
    ],

    "Amount": [
        500,
        1200,
        3000,
        2500,
        1500
    ],

    "Status": [
        "Paid",
        "Paid",
        "Pending",
        "Paid",
        "Paid"
    ]
})

st.dataframe(
    data,
    use_container_width=True
)

st.divider()

# ---------------- AI RECOMMENDATIONS ---------------- #

st.subheader("🤖 AI Financial Recommendations")

recommendations = [

    "Avoid impulse shopping during weekends.",

    "Set automatic savings transfers every month.",

    "Track small daily expenses carefully.",

    "Create category-wise spending limits.",

    "Review subscriptions you no longer use."
]

for tip in recommendations:

    st.write(f"✅ {tip}")

st.divider()

# ---------------- MONTHLY GOALS ---------------- #

st.subheader("🎯 Monthly Financial Goals")

goal1, goal2 = st.columns(2)

with goal1:

    st.checkbox(
        "Save ₹20,000 this month"
    )

    st.checkbox(
        "Reduce shopping expenses"
    )

with goal2:

    st.checkbox(
        "Track all expenses daily"
    )

    st.checkbox(
        "Invest 10% of income"
    )

st.divider()

# ---------------- FOOTER ---------------- #

st.caption(
    "Financial Guide Dashboard • Streamlit + JWT Authentication"
)