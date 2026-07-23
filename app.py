import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="AI Study Quiz Generator", page_icon="🧠", layout="centered")

# App Header
st.title("🧠 AI Study Quiz & Flashcard Generator")
st.write("Turn your lecture notes or textbook chapters into instant practice quizzes using AI!")

# Sidebar for API Key Configuration
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter your Google Gemini API Key", type="password")

# Main Input Section
st.subheader("1. Paste Your Study Material")
study_text = st.text_area("Paste notes, article text, or a chapter summary here:", height=200, placeholder="Paste your text here...")

num_questions = st.sidebar.slider("Number of Questions", min_value=3, max_value=10, value=5)

# Generate Button
if st.button("🚀 Generate Quiz", type="primary"):
    if not api_key:
        st.error("Please enter your Google Gemini API key in the sidebar.")
    elif not study_text.strip():
        st.error("Please paste some study text first!")
    else:
        try:
            # Configure Gemini
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            # System prompt / instructions
            prompt = f"""
            You are an expert tutor. Based on the following study material, generate {num_questions} multiple-choice quiz questions. 
            For each question, provide:
            1. The Question
            2. Four options (A, B, C, D)
            3. The correct answer
            4. A brief explanation of why it is correct.
            
            Study Material:
            {study_text}
            """
            
            with st.spinner("Generating your custom quiz... Please wait."):
                response = model.generate_content(prompt)
                
            st.success("Quiz Generated Successfully!")
            st.markdown("---")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
