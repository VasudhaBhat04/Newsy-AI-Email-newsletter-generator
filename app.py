import streamlit as st
import google.generativeai as genai  
from apikey import google_gemini_api_key  

genai.configure(api_key=google_gemini_api_key)

st.set_page_config(layout="wide")
st.title("Newsy: Your assistant for crafting email newsletters 🤖")
st.subheader("I'm here to assist 🤝")

with st.sidebar:
    st.title("Input Your Email-Newsletter Details:")
    st.subheader("Main Idea and Focus of the Email")

    email_title = st.text_input("Title")
    keywords = st.text_area("Keywords (comma-separated)")
    tone = st.selectbox(
    "Select the tone of your newsletter:",
    ["Promotional", "Educational", "Community-Focused"]
)
                       
    num_words = st.slider("Number of words", min_value=250, max_value=5000, step=250, value=500)
    submit_button = st.button("Generate")

def generate_newsletter(title, keywords, word_count,tone):
    prompt = f"""
Convert the blog post titled '{title}' into a professional and engaging email newsletter for my subscribers.
The newsletter should be concise yet informative, highlighting the key insights or tips from the blog.
It should include a compelling introduction, a bulleted or sectioned format for easy readability, and a clear call-to-action (CTA) at the end.
Make sure to naturally incorporate the following keywords: '{keywords}'.

Choose the tone of the newsletter:

1 = Promotional (focus on offers, benefits, CTA-driven)

2 = Educational (focus on tips, insights, value-driven)

3 = Community-Focused (focus on updates, stories, engagement)

The tone of the newsletter should align with the selected choice and be suitable for an online audience. Use the tone input as: '{tone}'.
"""
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

if submit_button:
    with st.spinner("Generating your newsletter..."):
        newsletter = generate_newsletter(email_title, keywords, num_words,tone)
        st.markdown(newsletter)  

 # st.download_button(" Download Newsletter", newsletter, file_name="generated_content.md")  
