import streamlit as st
from textblob import TextBlob  # <--- NLP ki library

st.title("AI Mood Detector 🤖")
st.write("Kuch bhi likhein, main bataunga ke aapka mood kaisa hai!")

# User se input lein
user_input = st.text_area("Yahan likhein (English mein):")

if st.button("Analyze Mood"):
    if user_input:
        # AI Dimagh (NLP)
        blob = TextBlob(user_input)
        result = blob.sentiment.polarity  # -1 (Negative) se +1 (Positive)

        # Logic
        if result > 0:
            st.success("Result: POSITIVE (Khushi/Achi baat) 😊")
            st.balloons()
        elif result < 0:
            st.error("Result: NEGATIVE (Gussa/Buri baat) 😡")
        else:
            st.info("Result: NEUTRAL (Normal baat) 😐")
            
        # Score bhi dikhayen
        st.write(f"Confidence Score: {result}")
    else:
        st.warning("Pehle kuch likhein toh sahi!")