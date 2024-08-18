import streamlit as st
from storyrecommender import recommendStories

st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFEB3B; /* Bright yellow background */
    }
    .main-title {
        color: #FF4500; /* Orange red color for the title */
        font-size: 50px;
        font-family: 'Comic Sans MS', cursive, sans-serif; /* Fun and playful font */
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px #000000; /* Shadow effect for better visibility */
    }
    .sidebar .sidebar-content {
        background-color: #FF69B4; /* Hot pink for the sidebar */
        color: #FFFFFF; /* White text color */
        font-family: 'Comic Sans MS', cursive, sans-serif; /* Consistent font */
        padding: 10px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #FFD700; /* Bright yellow color for the button */
        color: white;
        font-size: 20px;
        border-radius: 10px;
        padding: 10px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #FFC107; /* Slightly darker yellow when hovered */
    }
    .stDataFrame {
        font-family: 'Comic Sans MS', cursive, sans-serif; /* Fun font for the data frame */
        background-color: #FFFFE0; /* Light yellow background for the table */
        color: #FF6347; /* Tomato color for text */
        border-radius: 10px;
        padding: 10px;
    }
    .stDataFrame thead {
        background-color: #FF69B4; /* Hot pink header background */
        color: white;
    }
    .stDataFrame tbody {
        background-color: #FFFFFF; /* White background for rows */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='main-title'>🎉 Story Recommendation System for Kids 📚</h1>", unsafe_allow_html=True)

st.sidebar.header("👦👧 User Input")

# User input fields with playful placeholders
user_interest_age = st.sidebar.number_input("What's your favorite age to read about? (e.g., 10, 12, 14)", min_value=0, step=1)
user_reading_age = st.sidebar.number_input("What age do you read at? (e.g., 10, 12, 14)", min_value=0, step=1)

if st.sidebar.button("🎈 Get Recommendations 🎈", key="recommend_button"):
    if user_interest_age >= 0 and user_reading_age >= 0:
        recommended = recommendStories(user_interest_age, user_reading_age)
        if not recommended.empty:
            st.markdown("<h2 style='color:#FF4500;'>Here are some stories you might love:</h2>", unsafe_allow_html=True)
            st.dataframe(recommended)
        else:
            st.markdown("<h2 style='color:#FF4500;'>Oops! No recommendations found for the given inputs.</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='color:#FF4500;'>Please enter valid ages! 😊</h2>", unsafe_allow_html=True)
