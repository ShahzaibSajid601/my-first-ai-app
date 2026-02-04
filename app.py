import streamlit as st
from PIL import Image

# --- PAGE CONFIG (Tab ka naam aur icon) ---
st.set_page_config(page_title="Shahzaib's Portfolio", page_icon="👨‍💻", layout="wide")

# --- CUSTOM CSS (Styling ke liye) ---
# Yeh code website ko sundar banata hai aur faltu branding hatata hai
st.markdown("""
<style>
    /* Main Content Padding kam karein */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    /* Sidebar ka background color */
    [data-testid="stSidebar"] {
        background-color: #f0f2f6;
    }
    /* Buttons ko thoda stylish banayein */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #FF4B4B; 
        color: white;
    }
    /* Footer hide karein */
    footer {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR (Profile Card) ---
with st.sidebar:
    # Profile Picture (Placeholder)
    st.image("https://cdn-icons-png.flaticon.com/512/4140/4140048.png", width=120)
    
    st.markdown("## Shahzaib Sajid")
    st.markdown("** AI & Python Developer**")
    
    st.info("📍 Renala Khurd, Pakistan")
    
    # Social Links buttons
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("LinkedIn", "https://www.linkedin.com/in/shahzaib-sajid-78a319247")
    with col2:
        st.link_button("GitHub", "https://github.com/ShahzaibSajid601")

    st.divider()
    
    # Skills Progress
    st.write("### 🛠 Core Skills")
    st.caption("Python Programming")
    st.progress(85)
    st.caption("AI & NLP")
    st.progress(70)
    st.caption("Web Dev (Streamlit)")
    st.progress(90)
    
    st.divider()
    # Resume Download
    with open("requirements.txt", "rb") as file:
        st.download_button("📄 Download CV", file, file_name="Shahzaib_Resume.pdf")

# --- MAIN CONTENT (TABS SYSTEM) ---
# Tabs se website clean lagti hai
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "🚀 Projects", "🎓 Resume", "📬 Contact"])

# --- TAB 1: HOME / ABOUT ---
with tab1:
    st.title("Hi, I'm Shahzaib! ")
    st.subheader("Building the future with Artificial Intelligence.")
    
    st.write("""
    Main ek **Computer Science Student (Batch 2026)** hoon jo real-world problems ko code ke zariye solve karta hai.
    Mera focus **Generative AI**, **Automation**, aur **Data Science** par hai.
    """)
    
    st.divider()
    
    # Stats (Quick Info)
    col_a, col_b, col_c = st.columns(3)
    col_a.metric(label="Projects Completed", value="5+", delta="Latest: AI App")
    col_b.metric(label="Experience", value="Fresh Grad", delta="Amal Fellow")
    col_c.metric(label="Focus", value="Gen-AI", delta="Python")

# --- TAB 2: PROJECTS (Cards Layout) ---
with tab2:
    st.header("My Technical Projects")
    
    # Project 1
    with st.container():
        st.write("### 🤖 1. AI Mood Detector")
        st.write("An NLP-based web app that detects human emotions from text.")
        st.code("pip install textblob streamlit", language="python")
        col_x, col_y = st.columns([1, 4])
        with col_x:
            st.link_button("Live Demo 🔴", "https://share.streamlit.io/ShahzaibSajid601/my-first-ai-app")
        with col_y:
            st.caption("Tech Stack: Python, Streamlit, Git, TextBlob")
    
    st.divider()
    
    # Project 2
    with st.container():
        st.write("### 📊 2. Sales Data Dashboard")
        st.write("Automated data cleaning and visualization dashboard for business insights.")
        st.info("Used Pandas for cleaning 10,000+ rows of data.")
    
    st.divider()

    # Project 3
    with st.container():
        st.write("### 👟 3. Sneaker Store Manager")
        st.write("Full-stack PHP application for inventory management.")

# --- TAB 3: RESUME / EDUCATION ---
with tab3:
    st.header("Education & Experience")
    
    st.markdown("""
    #### 🎓 Education
    * **BS Computer Science** | UET Lahore (2022-2026)
        * *HEC Scholar, 3.5+ GPA (Expected)*
    * **ICS (Computer Science)** | ILM College (2020-2022)
    
    ---
    #### 💼 Experience
    * **Career-Prep Fellow** | Amal Academy (2025)
        * Developed leadership and business communication skills (Stanford funded).
    * **Freelance Developer** | Upwork (2024-Present)
        * Python scripting and automation tasks.
    """)

# --- TAB 4: CONTACT ---
with tab4:
    st.header("Get In Touch")
    
    col_form, col_img = st.columns([2, 1])
    
    with col_form:
        contact_form = st.form(key='contact_form_2')
        name = contact_form.text_input("Name")
        email = contact_form.text_input("Email")
        msg = contact_form.text_area("Message")
        submit = contact_form.form_submit_button("Send Message")
        
        if submit:
            st.success("Message Sent! I will reply shortly.")
            
    with col_img:
        st.image("https://cdn-icons-png.flaticon.com/512/2504/2504957.png", width=150)
        st.write("📧 shahzaibsajidskl@gmail.com")
        st.write("📞 +92-315-7227740")