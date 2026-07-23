import google.generativeai as genai
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Study Quiz & Flashcard Generator",
    page_icon="🧠",
    layout="centered",
)

# App Header
st.title("🧠 AI Study Quiz & Flashcard Generator")
st.write(
    "Turn your lecture notes or textbook chapters into instant practice"
    " quizzes using AI!"
)

# Sidebar for API Key Configuration
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input(
    "Enter your Google Gemini API Key", type="password"
)

# Main Input Section
st.subheader("1. Paste Your Study Material")
study_text = st.text_area(
    "Paste notes, article text, or a chapter summary here:", height=200
)

num_questions = st.sidebar.slider(
    "Number of Questions", min_value=3, max_value=10, value=5
)

# Generate Button Logic
if st.button("Generate Quiz"):
  if not api_key:
    st.error("Please enter your Google Gemini API Key in the sidebar.")
  elif not study_text.strip():
    st.error("Please paste some study material to generate a quiz.")
  else:
    try:
      # Configure Gemini API
      genai.configure(api_key=api_key)
      model = genai.GenerativeModel("gemini-2.5-flash")

      prompt = f"""
            Based on the following text, generate a practice quiz with {num_questions} multiple-choice questions (with 4 options each and the correct answer indicated) and 5 flashcards with key concepts and definitions.
            
            Text:
            {study_text}
            """

      with st.spinner("Generating your quiz and flashcards..."):
        response = model.generate_content(prompt)
        st.subheader("Generated Quiz & Flashcards")
        st.write(response.text)

    except Exception as e:
      st.error(f"An error occurred: {e}")
