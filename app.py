import os
import streamlit as st
import requests  # Use requests to make API calls

# Set page configuration
st.set_page_config(page_title="AI Content Generator", page_icon="📝", layout="wide")

# Display the logo
logo = "logo.png"  # Replace with your logo file name
st.image(logo, width=200)  # Adjust width as necessary

# Page title
st.title("AI Content Generator for Social Media")
st.write("Generate engaging and creative content for social media using AI with Groq Llama.")

# Sidebar
st.sidebar.header("Settings")
content_type = st.sidebar.selectbox("Select Content Type:", ["Tweet", "Instagram Caption", "LinkedIn Post", "Facebook Post"])
max_length = st.sidebar.slider("Max Length of Generated Content", 50, 300, 150)
temperature = st.sidebar.slider("Creativity (Temperature)", 0.0, 1.0, 0.7)

# Input for user prompt
prompt = st.text_area("Enter your content prompt:", help="Type a brief idea for your social media post.")

# Set up the Groq API key
GROQ_API_KEY = "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"
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Function to generate content using Groq Llama
def generate_content_with_groq(prompt):
    url = "https://api.groq.com/v1/chat/completions"  # Update with the correct endpoint
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "llama3-8b-8192"
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# Button to generate content
if st.button("Generate Content"):
    if prompt:
        with st.spinner('Generating content using Groq...'):
            generated_content = generate_content_with_groq(prompt)
            st.success("Generated Content:")
            st.write(generated_content)
    else:
        st.error("Please enter a prompt to generate content.")

# Footer
st.write("© 2024 Echo AI Content Generator | Powered by Groq Llama")
