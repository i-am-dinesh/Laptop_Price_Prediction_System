import streamlit as st
import pickle
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻",
                   layout="wide")

# Background image
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://e0.pxfuel.com/wallpapers/398/350/desktop-wallpaper-nillia-webdesign-web-development-management.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()


# loading the saved model
pipe=pickle.load(open("pipe.pkl","rb"))
df = pd.read_csv("df.csv")



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Laptop Price Prediction System',
                          
                          ['Introduction',
                           'Prediction',
                           'GitHub'],
                          icons=['activity','laptop computer','person'],
                          default_index=0)
    
    
# Introduction
if (selected == 'Introduction'):
    
    # page title
    st.markdown("<h1 style='text-align: center; color: white;'>Introduction 💻📑</h1>", unsafe_allow_html=True)

    st.subheader("Laptop Price Predictor Introduction") 

    st.write('* <span style="font-size: 20px">Welcome to the Laptop Price Predictor, a machine learning-based web application that helps you predict the price of a laptop based on its specifications. With this app, you can get an estimate of how much you should expect to pay for a particular laptop, based on its brand, processor, RAM, storage, and other key features.</span>', unsafe_allow_html=True)
   
    st.write('* <span style="font-size: 20px">Using state-of-the-art machine learning algorithms and deep learning models, this app can analyze large datasets of laptop prices to identify patterns and make accurate predictions. The app is built using the Python programming language and the Streamlit framework, making it easy to use and deploy.</span>', unsafe_allow_html=True)
   
    st.write('* <span style="font-size: 20px">Whether you are a student, professional, or just someone looking to buy a new laptop, the Laptop Price Predictor can help you make informed decisions and find the best deal. Try it out today and see how accurate it can be!</span>', unsafe_allow_html=True)
    
    st.write('* <span style="font-size: 20px">In this project, a supervised machine learning model is built to predict tentative laptop price based on its specifications.</span>', unsafe_allow_html=True)
    
    st.write('* <span style="font-size: 20px">This model is trained on dataset which is taken from Kaggle.</span>', unsafe_allow_html=True)
   
    st.write('* <span style="font-size: 20px">The dataset contains laptop specifications and corresponding prices. </span>', unsafe_allow_html=True)

    st.write('* <span style="font-size: 20px">Scikit-learn library is used to build the machine learning model.</span>', unsafe_allow_html=True)

    st.write('* <span style="font-size: 20px">Streamlit is used to make a web application that allows users to select the laptop specifications and user gets tentative price of the laptop.</span>', unsafe_allow_html=True)
   
    st.write('* <span style="font-size: 20px">The predicted price is displayed back to the user through the user interface.</span>', unsafe_allow_html=True)

    st.write('* <span style="font-size: 20px">This laptop price predictor web app has been successfully deployed to a hosting platform, allowing users to access it online from anywhere in the world.</span>', unsafe_allow_html=True)

    # st.write('<span style="font-size: 20px"></span>', unsafe_allow_html=True)

    st.subheader("Command to run the project.")
    st.write('<span style="font-size: 20px">We can run this command in our terminal or command prompt after navigating to the directory where our Streamlit app is located.</span>', unsafe_allow_html=True) 
    st.code("streamlit run app.py")


# Price Prediction
if (selected == 'Prediction'):
    
    # page title
    st.markdown("<h1 style='text-align: center; color: white;'>Laptop Price Predictor 💻💲</h1>", unsafe_allow_html=True)

    # making 3 cols left_column, middle_column, right_column
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        # brand input
        company = st.selectbox("Brand", df["Company"].unique())

    with middle_column:
        # laptop type
        type = st.selectbox("Type", df["TypeName"].unique())

    with right_column:
        # Ram size
        ram = st.selectbox("Ram (in GB)", df["Ram"].unique())

        # making 3 cols left_column, middle_column, right_column
    left_column, middle_column, right_column = st.columns(3)
    with left_column:

        # Weight input
        weight = st.number_input("Weight of laptop in kg")

    with middle_column:
        # Touchscreen
        touchscreen = st.selectbox("Touchscreen", ["No", "Yes"])

    with right_column:
        # IPS display
        ips = st.selectbox("IPS Display", ["No", "Yes"])

        # making 3 cols left_column, middle_column, right_column
    left_column, middle_column, right_column = st.columns(3)
    with left_column:

        # screen size
        Screen_size = st.number_input("Screen Size (in Inches)")

    with middle_column:
        # resolution
        resolution = st.selectbox('Screen Resolution',['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600','2560x1440', '2304x1440'])

    with right_column:
        # cpu input
        cpu = st.selectbox("Cpu Brand", df["Cpu brand"].unique())

        # making 3 cols left_column, middle_column, right_column
    left_column,  right_column = st.columns(2)
    with left_column:
        # hdd input
        hdd = st.selectbox("HDD(in GB)", [0, 128, 256, 512, 1024, 2048])


    with right_column:
        # ssd input
        ssd = st.selectbox("SSD(in GB)", [0, 8, 128, 256, 512, 1024])

    # making 3 cols left_column, middle_column, right_column
    left_column,  right_column = st.columns(2)

    with left_column:
        #gpu input
        gpu=st.selectbox("Gpu Brand",df["Gpu brand"].unique())

    with right_column:
        #os input
        os=st.selectbox("OS Type",df["os"].unique())

    if st.button("Predict Price"):
        ppi = None
        if touchscreen=="Yes":
            touchscreen=1
        else:
            touchscreen=0

        if ips == "Yes":
            ips=1
        else:
            ips=0

        X_res=int(resolution.split("x")[0])
        Y_res=int(resolution.split('x')[1])
        ppi=((X_res ** 2)+(Y_res ** 2))**0.5/Screen_size
        query=np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])

        query=query.reshape(1, 12)
        st.title("The Predicted Price of Laptop = Rs "+str(int(np.exp(pipe.predict(query)[0]))))     
    
    
# GitHub Introduction
if (selected == "GitHub"):
    
    # page title
    st.markdown("<h1 style='text-align: center; color: white;'>GitHub 🐙🔍</h1>", unsafe_allow_html=True)


    st.write('* <span style="font-size: 20px">A simple Machine learning web app deployed on Render which predict laptop prices according to laptop configuration defined by us. Predict the Price of laptop on the basis of Context A dataset for 1300 laptop models. Content, Company Name, Product Name, Laptop Type, Screen Inches, Screen Resolution, CPU Model, RAM Characteristics, Memory, GPU Characteristics, Operating System, Laptop Weight, Laptop Price.</span>', unsafe_allow_html=True)

    st.write('* <span style="font-size: 20px">The project is a web application called Laptop Price Predictor created using machine learning or deep learning techniques and Pythons Streamlit library.</span>', unsafe_allow_html=True)
             
    st.write('* <span style="font-size: 20px">The application can predict the price of a laptop based on its specifications. </span>', unsafe_allow_html=True)

    st.write('* <span style="font-size: 20px">The code for the project has been uploaded to a GitHub repository for sharing and collaboration.</span>', unsafe_allow_html=True)
     

    url = 'https://github.com/i-am-dinesh/'

    st.markdown(f'👉 [Click here]({url}) To Visit.')

    st.write('* <span style="font-size: 20px">The project has been deployed and is accessible through a given URL. </span>', unsafe_allow_html=True)

    url = 'https://i-am-dinesh-laptop-price-prediction-system-app-9764ps.streamlit.app/'

    st.markdown(f'👉 [Click here]({url}) To Visit.')






ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: center; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><span> by</span><a style='display: inline; text-align: left;' href="https://github.com/i-am-dinesh" target="_blank"> Dinesh</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)

