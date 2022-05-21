import streamlit as st
from calling import caller
from run import RUN

obj1 = caller()
obj2 = RUN()

if 'score' not in st.session_state:
    st.session_state['score'] = 0 

if 'verify_button' not in st.session_state:
    st.session_state['verify_button'] = 1

if 'train_button' not in st.session_state:
    st.session_state['train_button'] = 0

if 'predict_button' not in st.session_state:
    st.session_state['predict_button'] = 0

app_mode = st.sidebar.selectbox('Choose the App mode',
['About App','Face Verification'])
if app_mode =='About App':
    pass

elif app_mode == "Face Verification" and st.session_state.score == 0:
    st.title("WEBCAM")
    WINDOW = st.image([])  ## How to render this in frontend need to discuss
    if st.session_state.verify_button == 1: 
        take = st.button("Verify")
        if take:
            data = {"mode":"verify","image_area":WINDOW}
            # data = {"mode":"verify"}
            status = obj2.controller(data)
            if status == "Verified":
                st.session_state.score = 1
                st.success("User Verified")
            else:
                st.success("User Not Verified")
                st.session_state.train_button = 1
                st.session_state.verify_button = 0
    if st.session_state.train_button == 1:
        train = st.button("Take images")
        if train:
            data = {"mode":"train","image_area":WINDOW}
            # data = {"mode":"train"}
            status = obj2.controller(data)
            if status == "success":
                st.success("Image Trained Successfully")
                st.session_state.predict_button = 1
                st.session_state.train_button = 0
                st.session_state.verify_button = 0
                
    if st.session_state.predict_button == 1:
        predp = st.button("Predict")
        if predp:
            data = {"mode":"predict","image_area":WINDOW}
            # data = {"mode":"predict"}
            status = obj2.controller(data)
            if status == "Verified":
                st.session_state.score = 1
                st.success("User Verified")

if st.session_state.score != 0:
    app_mode2 = st.sidebar.selectbox('Data',
    ["Choose","Add","View","Delete"]
    )

    if app_mode2 == "Add":
        with st.form(key="userdata",clear_on_submit=True):
            category = st.text_input("what data you want to store")
            username = st.text_input("Username")
            password = st.text_input("Password",type="password")
            data = {"mode":app_mode2,"category":category,"username":username,"password":password}
            st.form_submit_button("save",on_click=obj1.database_controller(data=data))


    elif app_mode2 == "View":
        options = ['choose','microsoft','ineuron','hdfc','View all']
        category = st.selectbox("Enter the category to fetch",options)
        data = {"mode":app_mode2,"category": category}
        st.button("View",on_click=obj1.database_controller(data=data))
        

    elif app_mode2 == "Delete":
        options = ['choose','microsoft','ineuron','hdfc','Delete all'] ##Need to fetch keys from datbase to show it in frontend
        category = st.selectbox("Enter the category to fetch",options)
        data = {"mode":app_mode2,"category": category}
        st.button("Delete",on_click=obj1.database_controller(data=data))

