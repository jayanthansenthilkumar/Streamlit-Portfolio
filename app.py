import streamlit as st
import numpy as np
from pathlib import Path
import base64
#Main Function
st.set_page_config(page_title='Jayanthan Senthilkumar',
    page_icon='logo.jpg',
    layout="wide",
    initial_sidebar_state="expanded",)
#Image function Start
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
#Image function End
#Sidebar Start
def cs_sidebar():
    st.sidebar.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=225 height=280>'''.format(img_to_bytes("side.jpeg")), unsafe_allow_html=True)
    st.sidebar.title("Jayanthan Senthilkumar")
    st.sidebar.markdown("Date of Birth : 18-11-2004")
    st.sidebar.markdown("Place : Karur")
    st.sidebar.markdown("Age : 19")
    st.sidebar.markdown('''id : [jayanthansenthilkumar18@gmail.com](mailto:jayanthansenthilkumar18@gmail.com)''', unsafe_allow_html=True)
    st.sidebar.markdown('''Phone : [+91 8825756388](tel:+918825756388)''', unsafe_allow_html=True)
    data = "logo.jpg"
    st.sidebar.download_button('My Resume', data)   
#Sidebar End
def body1():
    st.title("Myself")
    st.markdown("Hey Guys,I'm Jayanthan SenthilKumar,Currently pursuing B.Tech in the stream of Artificial Intelligence and Machine Learning. As a passionate learner, I focusing on enhancing my skills in Python with Data Science.I am eager to contribute my creativity skills to build efficient and user-friendly Data manipulations and other AI based applications.Connect with me to collaborate on exciting projects!!!")
def body2():
#A,B Starts
    a,b = st.columns(2)
    a.title("Education")
    a.header("High School & Grade 12")
    a.markdown("2021 - 2022")
    a.markdown("Cheran Matric.Hr.Sec.School")
    a.markdown("I have passed my higher secondary schooling with 89.5% marks with good communication skills")
#College    
    a.header("B.Tech & Artificial Intelligence and Machine Learning")
    a.markdown("2022 - 2026")
    a.markdown("M.Kumarasamy College of Engineering")
    a.markdown("I'm currently pursuing my Bachelor of Technology in great way in this institution")
    a.title("Languages")
    a.markdown("* Tamil      - 100%")
    a.markdown("* Telugu     - 80%")
    a.markdown("* Sourashtra - 40%")
    a.markdown("* Kannada    - 50%")
    a.markdown("* Hindi      - 50%")
    a.markdown("* Japanese   - 25%")
    a.markdown("* English    - 80%")
#Project Translator
    b.title("Projects")
    b.header("Language Translator - Sourashtra")
    b.markdown("Completed Year : 2024")
    b.latex("Translator Application")
    b.markdown("* This is an AI based model and quick responsible")
    b.markdown("* It is a project which is very easy in translation as well as fully controlled by AI Pre-trained model")
    b.markdown("* This Project motive is to translate the other indian or foreign language to this language and it is very useful to the begineers who are intrested to learn this language")
    b.markdown("* Based on my personal thing only I have developed this project")
#Project Cargo
    b.header("Cargo Vehicle Allotment Agent")
    b.markdown("Completed Year : 2023 - 2024")
    b.latex("Vehicle Allotment Software")
    b.markdown("* This is an application based project")
    b.markdown("* It helps the users to get the cargo transportation vehicle in theri near by areas")
    b.markdown("* This is the project based on Artificial Intelligence Models")
    b.markdown("* Based on my survey most of the people asked to make like this by their request I had made this project")
    st.markdown("---")
#A,B End
#C,D Starts
    c,d=st.columns(2)
    c.title("Technical Skills")
    c.markdown("* Python     - 80%")
    c.markdown("* C Programming     - 90%")
    c.markdown("* Java - 60%")
    c.markdown("* HTML    - 50%")
    c.markdown("* CSS   - 25%")
    c.markdown("* Django    - 40%")
    d.title("Soft Skills")
    d.markdown("* Leadership      - 100%")
    d.markdown("* Teamwork    - 80%")
    d.markdown("* Adaptability - 40%")
    d.markdown("* Time Management    - 50%")
    d.markdown("* Team Management   - 25%")
    st.markdown("---")
    st.title("Certificates")
#C,D End
#Certificate Starts
    tab1,tab2,tab3,tab4,tab5 = st.tabs(["Courses", "Symposium","Internship","Workshop","School Achievement"])
    with tab1:
        col1,col2,col3 = st.columns(3)
        col1.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("p5.png")), unsafe_allow_html=True)
        col2.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("p1.png")), unsafe_allow_html=True)
        col3.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("p2.png")), unsafe_allow_html=True)
        st.markdown("---")
        col4,col5,col6 = st.columns(3)
        col4.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("p3.png")), unsafe_allow_html=True)
        col5.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("p4.png")), unsafe_allow_html=True)
        col6.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("w4.png")), unsafe_allow_html=True)
        st.markdown("---")
        col7,col8,col9 = st.columns(3)
        col7.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("w1.png")), unsafe_allow_html=True)
        col8.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("w2.png")), unsafe_allow_html=True)
        col9.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("w3.png")), unsafe_allow_html=True)
        st.markdown("---")
        col10,col11,col12 = st.columns(3)
        col10.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=250 height=300>'''.format(img_to_bytes("p.png")), unsafe_allow_html=True)
        st.markdown("---")
        
    with tab2:
        col1,col2,col3 = st.columns(3)
        col1.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("cs1.jpg")), unsafe_allow_html=True)
        col2.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("cs2.jpg")), unsafe_allow_html=True)
        col3.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("cs3.jpg")), unsafe_allow_html=True)
        st.markdown("---")
        col4,col5,col6 = st.columns(3)
        col4.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("cs4.jpg")), unsafe_allow_html=True)
        col5.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("cs5.jpg")), unsafe_allow_html=True)
        st.markdown("---")
    with tab3:
        col1,col2,col3 = st.columns(3)
        col1.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=250 height=300>'''.format(img_to_bytes("in1.jpg")), unsafe_allow_html=True)
        col2.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=250 height=300>'''.format(img_to_bytes("in2.jpg")), unsafe_allow_html=True)
        st.markdown("---")
    with tab4:
        col1,col2,col3 = st.columns(3)
        col1.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("wk1.png")), unsafe_allow_html=True)
        col2.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("wk2.png")), unsafe_allow_html=True)
        col3.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=250 height=300>'''.format(img_to_bytes("step.png")), unsafe_allow_html=True)
        st.markdown("---")
    with tab5:
        col1,col2,col3 = st.columns(3)
        col1.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("s2.jpg")), unsafe_allow_html=True)
        col2.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("s3.jpg")), unsafe_allow_html=True)
        col3.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("s4.jpg")), unsafe_allow_html=True)
        st.markdown("---")
        col4,col5,col6 = st.columns(3)
        col4.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=180>'''.format(img_to_bytes("s5.jpg")), unsafe_allow_html=True)
        col5.markdown('''<img src='data:image/png;base64,{}' class='img-fluid' width=250 height=300>'''.format(img_to_bytes("s1.jpg")), unsafe_allow_html=True)
        st.markdown("---")
#Certificate Ends
#Contact Starts
    st.title("Contact Me")
    am,pm=st.columns(2)
    am.header("Address")
    am.markdown("1/64/4,MuthukrishnaPuram,")
    am.markdown("Vennaimalai,")
    am.markdown("Karur - 639006")
    pm.header("Social Profiles")
    pm.markdown('''LinkedIn : [Jayanthan Senthilkumar](https://www.linkedin.com/in/jayanthan-s-%E3%82%B8%E3%83%A3%E3%83%A4%E3%83%B3%E3%82%BF%E3%83%B3-bba225259?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)''', unsafe_allow_html=True)
    pm.markdown('''Mail Id : [jayanthansenthilkumar18@gmail.com](mailto:jayanthansenthilkumar18@gmail.com)''', unsafe_allow_html=True)
    pm.markdown('''Twitter : [jayanthan2004](https://twitter.com/jayanthan2004)''', unsafe_allow_html=True)
    pm.markdown('''Github : [jayanthansenthilkumar](https://github.com/jayanthansenthilkumar)''', unsafe_allow_html=True)
    st.markdown("---")
    with st.form(key="submit"):
        na,ma=st.columns(2)
        username = na.text_input('Name')
        password = ma.text_input('E-Mail')
        message = st.text_input('Message')
        st.form_submit_button('Hire Me')
    st.markdown("---")
#Contact Ends
    st.markdown("Developed by")
    st.title("Jayanthan Senthilkumar")
    st.markdown("All Rights & Copyright Received - 2024")
cs_sidebar()
body1()
body2()
