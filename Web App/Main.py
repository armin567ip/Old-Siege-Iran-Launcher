import streamlit as st
from streamlit_option_menu import option_menu
import json
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title="OldSiege.ir", page_icon=":video_game:", layout="wide")


#Hide Menu
hide_menu = """
<style>
#MainMenu {
    visibility:hidden;
}

footer{
    visibility:hidden;
}
</style>
"""

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

Discord_anime = load_lottiefile("discord.json")
controller = load_lottiefile("controller.json")

selected = option_menu(
        menu_title=None , 
        options=["Home", "Download" , "Contact" ],
        icons=["house","download","envelope"],
        default_index=0,
        orientation=("horizontal"),
        )

if selected == "Home":
    st.markdown(
        """
        <style>
    @font-face {
    font-family: 'segoe ui';
    font-style: normal;
    src: url(https://fonts.gstatic.com/s/segoe ui/v12/IurY6Y5j_oScZZow4VOxCZZM.woff2) format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
    }

    html, body, [class*="css"]  {
    font-family: 'segoe ui';
    font-size: 93.84%;
    text-align: right;
    }
    </style>

    """,
        unsafe_allow_html=True,
    )
    with st.container():
        st.write("---")
        left_column,right_column = st.columns(2)
        with left_column:
            st.markdown(hide_menu,unsafe_allow_html=True)
            st_lottie(controller,height=350,key="hello")
    with right_column:
        st.header ("درباره ما")
        st.write("##")
        st.subheader("""
            ما یک انجمن اصلاح کننده برای رینبو سیکس سیج هستیم
        
              ما ابزار هایی داریم که پلیر ها را قادر به بازی کردن سیزن های قبلی بازی و یک سری گیم مود های خاص میکنند  ⦿   
              این ابزار ها را به صورت کاملا رایگان در اختیار همه میگذاریم  ⦿   
              در حال تشکیل کامیونیتی هستیم که همه کنار هم جمع شیم و از بازی کردن سیزن های قبلی بازی لذت ببریم   ⦿       
            """
            ) 
                   
if selected == "Download":
    st.markdown(hide_menu,unsafe_allow_html=True)
    st.subheader("Rainbow Six Siege Operation: Whitenoise")
    st.title("10 Parts/Each is 5GB")
    st.write("All : 45.5 GB")
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Links")
            st.write("[Download Part 1 >](https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part01.rar)")
            st.write("[Download Part 2 >](https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part02.rar)")
            st.write("[Download Part 3 >](https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part03.rar)")
            st.write("[Download Part 4 >](https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part04.rar)")
            st.write("[Download Part 5 >](https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part05.rar)")
            st.write("[Download Part 6 >](https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part06.rar)")
            st.write("[Download Part 7 >](https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part07.rar)")
            st.write("[Download Part 8 >](https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part08.rar)")
            st.write("[Download Part 9 >](https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part09.rar)")
            st.write("[Download Part 10 >](https://s5.uupload.ir/files/oldsiege23/Y2S4_WhiteNoise.part10.rar)")  
            st.write("---")   
            st.subheader("Rainbow Six Siege Operation: VelvetShell")  
            st.title("7 Parts/Each is 4GB") 
            st.write("All : 27.6 GB") 
            st.write("[Download Part 1 >](https://s3.uupload.ir/files/oldsiege23/Y2S1_VelvetShell.part01.rar)")
            st.write("[Download Part 2 >](https://s3.uupload.ir/files/oldsiege23/Y2S1_VelvetShell.part02.rar)")
            st.write("[Download Part 3 >](https://s3.uupload.ir/files/oldsiege23/Y2S1_VelvetShell.part03.rar)")
            st.write("[Download Part 4 >](https://s3.uupload.ir/files/oldsiege23/Y2S1_VelvetShell.part04.rar)")
            st.write("[Download Part 5 >](https://s3.uupload.ir/files/oldsiege23/Y2S1_VelvetShell.part05.rar)")
            st.write("[Download Part 6 >](https://s3.uupload.ir/files/oldsiege23/Y2S1_VelvetShell.part06.rar)")
            st.write("[Download Part 7 >](https://s3.uupload.ir/files/oldsiege23/Y2S1_VelvetShell.part07.rar)")         

contact_form = """
<form action="https://formsubmit.co/armin7890ip@gmail.com" method="POST">
     <input type="text" name="name" placeholder="نام  شما" required>
     <input type="hidden" name="_captcha" value="false">
     <input type="email" name="email" placeholder="آدرس  ایمیل  شما" required>
     <input type="hidden" name="_next" value="http://teststreamlit.runflare.run/">
     <textarea name="message" placeholder="پیام  شما"></textarea>
     <button type="submit">ارسال</button>
</form>
"""

if selected == "Contact":
    st.markdown(
        """
        <style>
    @font-face {
    font-family: 'segoe ui';
    font-style: normal;
    src: url(https://fonts.gstatic.com/s/segoe ui/v12/IurY6Y5j_oScZZow4VOxCZZM.woff2) format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
    }

    html, body, [class*="css"]  {
    font-family: 'segoe ui';
    font-size: 20;
    }
    </style>

    """,
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(hide_menu,unsafe_allow_html=True)
        st_lottie(Discord_anime,height=120)
        st.write(" ")
    with col2:
        st.title("در دیسکورد به ما ملحق شوید" )
        st.subheader("[Discord >](https://discord.gg/62bmu2ZNXN)")
    st.write("---")
    st.header(":email: پیغام خود را برای ما ارسال کنید" )
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
        def local_css(file_name):
           with open(file_name) as f:
               st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



        local_css("style.css")