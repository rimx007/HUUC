import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu
import numpy as np
import json

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="HUUH", page_icon=":person in lotus position:", layout="wide")   


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")
image = Image.open('Untitled-2.png')

selected = option_menu(
            menu_title=None,  # required
            options=["HOME", "ABOUT US", "CONTACT"],  # required
            icons=["house", "info-circle", "person-lines-fill"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            
        )
           
    

if selected == "HOME":

    # ---- HEADER SECTION ----
    with st.container():
       
        st.title("Henan University Of Urban Construction")
        explination = '<p style="font-size: 20px;">Henan University of Urban Construction (河南城市建设大学) is the only provincial undergraduate university in Henan Province that focuses on engineering and features “urban construction” as a multi-disciplinary coordinated development. It is also one of the only two undergraduate universities in the country named after “urban construction”.The predecessor of Henan University of Urban Construction (河南城市建设大学) was the Pingdingshan Urban Construction Environmental Protection School founded in 1983 and the Henan Branch of Wuhan Urban Construction College in 1985. It has gone through historical periods such as Henan Urban Construction College and Pingdingshan Institute of Technology. In 2002, it was approved by the Ministry of Education and was upgraded to an undergraduate college. The school was renamed Henan Urban Construction College in 2008</p>' 


        st.markdown(explination, unsafe_allow_html=True)
        
        
        st.write("[Learn More >](https://www.hncj.edu.cn/)")

    # ---- WHAT WE DO ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("WHAT WE DO")
            st.write("##")
            st.write(
                """
                Our school is known and recognized for:
                - being on of the best engineering schools in China.
                - Having best and respected students.
                - Having a good oversea students program.
                - creating smart and overachiving students.
                - being open and understanding of students.
            
                """
            )
            st.write("[Watch short video>](https://haokan.baidu.com/v?pd=wisenatural&vid=15448485800867417635)")
        with right_column:
            st.image('https://i.ibb.co/yBW6Hqp/Untitled-3.png',width=500, caption='henan university of urban construction')
            
                
       
            
     # ---- WHAT WE ARE LOOKING FOR ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("WHAT WE ARE LOOKING FOR")
            st.write("##")
            st.write(
                """
                we are looking for someone who:
                - is trying to achive big things.
                - works hard and tries his best.
                - at least have a universty entery exam score of 80 or higher.
                - who will respect and obey the laws and regulations of our school.
                So if you think you got what it takes you can apply and submit you're files and after carfully checking it we will get back to you. 
            
                """
            )
    with st.container():
        st.write("---")
        st.write("##")
        st.markdown("<h1 style='text-align: center; background-color: #00cc00;height:3em;width:60em;margin: auto;font-size: 22px;display: block;'>If you want to apply pleace check the box below</h1>", unsafe_allow_html=True)
        st.write("##")
    
    
              
    # ---- CONTACT ----
    with st.container():
        m = st.markdown("""
<style>
div.stcheckbox > checkbox:first-child {
background-color: #00cc00;
        color: white;
        height: 3em;
        width: 12em;
        border-radius:10px;
        border:3px solid #000000;
        font-size:20px;
        font-weight: bold;
        margin: auto;
        display: block;
}</style>""", unsafe_allow_html=True)
        selected = st.checkbox ("I WANT TO APPLY")
        if selected:
            
            stra ='<p style="font-size: 22px;">Great!!!please go ahead and apply</p>'
            st.markdown(stra, unsafe_allow_html=True)
            with st.container():
                option = st.selectbox('What major do you want to study?',
     ('Computer Science','civil engineering', 'Design','Architecture', 'Management', 'Business Administration', 'Philology'))

                st.write('You selected:', option)
                st.radio("which program will you be taking?",
                         key="visibility",
                         options=["bachelor-program", "Masters-program", "Doctoral-program"],
    )
        
            m = st.markdown("""
<style>
div.stButton > button:first-child {
        background-color: #00cc00;
        color: white;
        height: 3em;
        width: 12em;
        border-radius:10px;
        border:3px solid #000000;
        font-size:20px;
        font-weight: bold;
        margin: auto;
        display: block;
}

div.stButton > button:hover {
	background:linear-gradient(to bottom, #ffffff 5%, #A7A5A4 100%);
	background-color:#ffffff;
}

div.stButton > button:active {
	position:relative;
	top:3px;
}</style>""", unsafe_allow_html=True)
            b = st.button("APPLY")
            if b:
                 with st.container():
                     st.header("APPLY!")
                     st.markdown("<h1 style='background-color: #FF0000; width: 32em; font-size: 18px;'>when you upload all the file needed to apply, make sure its pdf format.</h1>", unsafe_allow_html=True)
                     contact_form = """
        <form action="https://formsubmit.co/rimon.adey@gmail.com"enctype="multipart/form-data" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <input type="file" name="attachment" accept="image/png, image/pdf">
            <textarea name="message" placeholder="why Henan University of Urban Construction?" required></textarea>
            <button type="submit">Submit</button>
        </form>
        """ 
                     left_column, right_column = st.columns(2)
                     with left_column:
                         st.markdown(contact_form, unsafe_allow_html=True)
                     with right_column:
                         st.empty()
                         st.write("##")             


                    
                    
if selected == "ABOUT US":
    
    st.markdown("<h1 style='text-align: center; font-size: 30px;'>About Henan University Of Urban Construction</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 18px;'> Henan University of Urban Construction (河南城市建设大学) is the only provincial undergraduate university in Henan Province that focuses on engineering and features “urban construction” as a multi-disciplinary coordinated development. It is also one of the only two undergraduate universities in the country named after “urban construction”. The predecessor of Henan University of Urban Construction (河南城市建设大学) was the Pingdingshan Urban Construction Environmental Protection School founded in 1983 and the Henan Branch of Wuhan Urban Construction College in 1985. It has gone through historical periods such as Henan Urban Construction College and Pingdingshan Institute of Technology. In 2002, it was approved by the Ministry of Education and was upgraded to an undergraduate college. The school was renamed Henan Urban Construction College in 2008.The school is located in China’s outstanding tourist city-Pingdingshan City, Henan Province. The natural scenery here is beautiful, and there are many places of interest and historical sites. Not only the primitive society Neolithic Peiligang Culture, Yangshao Culture, and Longshan Cultural Sites, but also the Yaoshan Scenic Area with heavy mountains and tall peaks, as well as the cemetery of the great writer Su Shi and his son in the Song Dynasty, the best-preserved Yexian County Office of Ming Dynasty and so on. The main campus of the school faces the thousand-year-old ancient temple Xiangshan Temple and is close to the rippling Baigui Lake. The campus buildings are scattered and beautiful and the environment is beautiful and pleasant. In 2008, it was named as the garden unit of Henan Province.</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.image('https://i.ibb.co/R0VyrV7/Untitled-2.png', width= 1300, caption='henan university of urban construction') 

    with col3:
        st.write("")
    st.markdown("<h1 style='font-size: 18px;'>The school covers an area of   1,730 acres, with a construction area of   more than 610,000 square meters, a total value of 114 million yuan in teaching and scientific research equipment, more than 1.3 million documents in the library, 16 databases of various Chinese and foreign documents, and more than 85,000 various sports fields and gymnasiums. Square meters.Henan University of Urban Construction (河南城市建设大学) has a strong team of teachers. There are more than 1,100 faculty members and more than 800 full-time teachers, including more than 530 teachers with doctoral and master’s degrees, 65 professors, and 238 teachers with associate titles. There are 43 outstanding provincial experts, provincial academic and technical leaders, and provincial top-notch talents in professional technology. More than 40 famous international and domestic scholars, academicians and experts are also employed as part-time or visiting professors.The school has always attached great importance to scientific research, has long adhered to the main battlefield of the national economy, focused on serving the construction industry and local economic construction, and focused on scientific and technological innovation. In recent years, it has undertaken more than 530 national, provincial and municipal longitudinal scientific research projects, won more than 300 awards of various levels, and published more than 3,600 academic papers, including core journals and publications of important international search institutions such as SCI, EI, and ISTP Collected more than 1,400 articles, published more than 700 textbooks and monographs, and obtained 8 national patents.Henan University of Urban Construction (河南城市建设大学) insists on opening schools, continuously expands and deepens foreign exchanges, actively carries out education for international students in China, and conducts teaching and scientific research cooperation with well-known foreign universities such as the United States, Britain, Germany, Russia, Australia, and Malaysia. Since 2011, it has successfully carried out undergraduate and junior college Chinese-foreign cooperative education projects with the University of the Highland Islands in the United Kingdom, the St. the Petersburg State University of Architectural Engineering in Russia, and the Lyndon University in Malaysia. There are currently 1,227 students in the school.Looking forward to the future, Henan University of Urban Construction (河南城市建设大学) will continue to firmly grasp the socialist direction of running a school, focusing on the overall improvement of the quality of talent training; running through the two main lines of reform and innovation, transformation and upgrading; and striving to achieve the three goals of raising the level of running a school, transforming and developing, and building a civilized and harmonious campus , Focus on shaping the four characteristics of application, urban construction, locality, and internationalization; continue to focus on the construction of majors and professional groups, faculty, practical teaching bases and platforms for integration of production and education, scientific and technological services and collaborative innovation platforms, cultural inheritance and innovation The university system and other five constructions, closely following the pace of “double first-class” construction, actively promote the construction of new engineering, actively integrate into the “100-city construction quality improvement project”, and strive to build the school into a high-level applied technology-based urban construction university.</h1>", unsafe_allow_html=True)
    m = st.markdown("""
<style>
div.stButton > button:first-child {
        background-color: #00cc00;
        color: white;
        height: 3em;
        width: 12em;
        border-radius:10px;
        border:3px solid #000000;
        font-size:20px;
        font-weight: bold;
        margin: auto;
        display: block;
}

div.stButton > button:hover {
	background:linear-gradient(to bottom, #ffffff 5%, #A7A5A4 100%);
	background-color:#ffffff;
}

div.stButton > button:active {
	position:relative;
	top:3px;
}</style>""", unsafe_allow_html=True)
    b = st.button("learn more")
    if b:
        col1, col2, col3 = st.columns([1,6,1])
        with col1:
            st.write("")
        with col1:
            st.write("[check website >](https://www.hncj.edu.cn/)")
            st.write("[watch video >](https://haokan.baidu.com/v?pd=wisenatural&vid=1985089589719155429)")
        with col3:
            st.write("")
            
              
    
if selected == "CONTACT":
    st.markdown("<h1 style='text-align: center; font-size: 30px;'>Contact us</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 18px;'>Adress: Longxiang Street, New City District, Pingdingshan City, Henan Province, China</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 18px;'>Phone: 0375-2089581 0375-2089583</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 18px;'>Email: admission@cuecc.com</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 18px;'>Home Page: http://www.hncj.edu.cn/</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 18px;'>Zip: 467036</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 18px;'>Welcome</h1>", unsafe_allow_html=True)
    
    







   

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://i.ibb.co/XSP7r47/Untitled-1.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
