import os
import streamlit as st
from groq import Groq
import openai

# Set page configuration
st.set_page_config(page_title="AI Content Generator", page_icon="📝", layout="wide")

# Display the logo
logo = "logo.png"  # Replace with your logo file name
st.image(logo, width=200)

# Page title
st.title("AI Content Generator for Social Media")
st.write("Generate engaging and creative content for social media using AI with Groq Llama and Brand Voice Integration.")

# Sidebar settings
st.sidebar.header("Settings")
content_type = st.sidebar.selectbox("Select Content Type:", ["Tweet", "Instagram Caption", "LinkedIn Post", "Facebook Post"])
max_length = st.sidebar.slider("Max Length of Generated Content", 50, 300, 150)
temperature = st.sidebar.slider("Creativity (Temperature)", 0.0, 1.0, 0.7)
brand_voice = st.sidebar.selectbox("Select Brand Voice:", ["Professional", "Casual", "Witty", "Formal"])

# Input for user prompt
prompt = st.text_area("Enter your content prompt:", help="Type a brief idea for your social media post.")

# Set up Groq and OpenAI API keys
GROQ_API_KEY = "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"
openai.api_key = 'your-openai-api-key'
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Function to generate content with Groq Llama
def generate_content_with_groq(prompt):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192"
    )
    return chat_completion.choices[0].message.content

# Function to mimic brand voice
def mimic_brand_voice(content, brand_voice):
    prompt = f"Rewrite the following content in a {brand_voice} tone: {content}"
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if you have access
    messages=[{"role": "user", "content": prompt}]
)
    return response.choices[0].text.strip()

# Button to generate content
if st.button("Generate Content"):
    if prompt:
        with st.spinner('Generating content using Groq...'):
            generated_content = generate_content_with_groq(prompt)
            styled_content = mimic_brand_voice(generated_content, brand_voice)
            st.success("Generated Content with Brand Voice:")
            st.write(styled_content)
    else:
        st.error("Please enter a prompt to generate content.")

# Footer
st.write("© 2024 Echo AI Content Generator | Powered by Groq Llama")
