import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Shahzaib's Portfolio", page_icon="👨‍💻", layout="wide")

# --- SIDEBAR (Profile Info) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150) # Placeholder Image
    st.title("Shahzaib Sajid")
    st.write("🚀 **Aspiring AI Engineer | Python Developer**")
    
    st.write("---")
    st.write("📍 Renala Khurd / Lahore, Pakistan")
    st.write("📧 shahzaibsajidskl@gmail.com")
    st.write("📞 +92-315-7227740")
    
    st.write("---")
    st.write("**Social Links:**")
    st.link_button("🔗 LinkedIn Profile", "https://www.linkedin.com/in/shahzaib-sajid-78a319247")
    st.link_button("🐙 GitHub Profile", "https://github.com/ShahzaibSajid601") # Yahan apna link check kr lena

    st.write("---")
    # Resume Download Button (Filhal fake button hai)
    with open("requirements.txt", "rb") as file:
        btn = st.download_button(
            label="📄 Download Resume",
            data=file,
            file_name="Shahzaib_Resume.pdf",
            mime="application/pdf"
        )

# --- MAIN PAGE ---
st.title("Hello, I am Shahzaib! 👋")
st.subheader("Computer Science Student (Batch 2026) & AI Enthusiast")

st.write("""
Main ek passionate software developer hoon jo **Python** aur **Artificial Intelligence** ke zariye real-world problems solve karta hai. 
Filhal main **Generative AI** aur **Web Development** par focus kar raha hoon.
""")

st.write("---")

# --- SKILLS SECTION ---
st.header("💻 Technical Skills")
col1, col2 = st.columns(2)

with col1:
    st.write("**Programming Languages**")
    st.slider("Python (Advanced)", 0, 100, 85, disabled=True)
    st.slider("C++ / SQL", 0, 100, 70, disabled=True)
    st.slider("HTML / CSS", 0, 100, 75, disabled=True)

with col2:
    st.write("**Frameworks & Tools**")
    st.slider("Streamlit (Web Apps)", 0, 100, 90, disabled=True)
    st.slider("Pandas (Data Analysis)", 0, 100, 80, disabled=True)
    st.slider("Git & GitHub", 0, 100, 85, disabled=True)

st.write("---")

# --- PROJECTS SECTION ---
st.header("🚀 My Projects")

# Project 1
with st.container():
    st.subheader("1. AI Mood Detector (NLP App)")
    st.write("Developed a real-time Sentiment Analysis tool using **Python** and **TextBlob**. It detects user emotions from text input.")
    st.markdown("**Tech Stack:** Python, Streamlit, NLP, Git")
    # Yahan usi app ka link lagayen jo abhi live ki thi
    st.link_button("🔴 Live Demo", "https://share.streamlit.io/ShahzaibSajid601/my-first-ai-app") 

# Project 2
with st.container():
    st.subheader("2. Sales Data Analysis Dashboard")
    st.write("Cleaned and analyzed raw sales data using **Pandas** to identify top-performing products and regional trends.")
    st.markdown("**Tech Stack:** Python, Excel, Pivot Tables")

# Project 3
with st.container():
    st.subheader("3. Sneaker Store Management System")
    st.write("Built a full inventory and sales management system with Admin & User panels.")
    st.markdown("**Tech Stack:** PHP, SQL, HTML/CSS")

st.write("---")

# --- EXPERIENCE & EDUCATION ---
col3, col4 = st.columns(2)

with col3:
    st.header("🎓 Education")
    st.write("**BS Computer Science**")
    st.write("University of Engineering & Technology (UET), Lahore")
    st.caption("2022 - 2026 | HEC Scholar")
    
    st.write("**Intermediate (ICS)**")
    st.write("ILM Group of Colleges")
    st.caption("2020 - 2022 | Laptop Award Winner")

with col4:
    st.header("💼 Experience")
    st.write("**Career-Prep Fellow**")
    st.write("Amal Academy (Stanford University Funded)")
    st.caption("Jan 2025 - Mar 2025")
    st.write("Developing leadership and business communication skills.")

st.write("---")

# --- CONTACT FORM ---
st.header("📬 Get In Touch")
contact_form = st.form(key='contact_form')
name = contact_form.text_input("Your Name")
email = contact_form.text_input("Your Email")
message = contact_form.text_area("Your Message")
submit_button = contact_form.form_submit_button("Send Message")

if submit_button:
    st.success(f"Thank you {name}! Your message has been sent.")
    st.balloons()