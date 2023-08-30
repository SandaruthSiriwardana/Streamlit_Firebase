# Importing the required modules
import streamlit as st
import pyrebase
from datetime import datetime

# Configeration keys
firebaseConfig = {
  'apiKey': "AIzaSyCn7-xVi0NBsRp-LIKiTFLPFXQDHqMJeo0",
  "authDomain": "buildstreamlit.firebaseapp.com",
  "databaseURL": "https://buildstreamlit-default-rtdb.firebaseio.com",
  "projectId": "buildstreamlit",
  "storageBucket": "buildstreamlit.appspot.com",
  "messagingSenderId": "549954845792",
  "appId": "1:549954845792:web:dc443ef9bc66703c949705",
  "measurementId": "G-7RF1X2RXCR"
}

# Firebase Authentication

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db=firebase.database()
storage = firebase.storage()

st.title("Welcome to the Streamlit App")

# Authentication

choice=st.sidebar.selectbox("Select Activity",["Login","SignUp"])
email=st.sidebar.text_input("Email")
password=st.sidebar.text_input("Password",type="password")

if choice=="SignUp":
    handle=st.sidebar.text_input("handle Name (Unique)",value="Default")
    submit=st.sidebar.button("Create Account")

    if submit:
        user=auth.create_user_with_email_and_password(email,password)
        st.success("Account Created")
        st.balloons()

        # Sign in
        user=auth.sign_in_with_email_and_password(email,password)
        db.child(user['localId']).child("handle").set(handle)
        db.child(user['localId']).child("ID").set(user['localId'])
        st.title("Welcome "+handle)
        st.info("Go to Login Menu to Login")

# Login Block
if choice == 'Login':
    login = st.sidebar.checkbox('Login')
    if login:
        user = auth.sign_in_with_email_and_password(email,password)
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        bio = st.radio('Jump to',['Home','Workplace Feeds', 'Settings'])
        
        # SETTINGS PAGE
        if bio == 'Settings':  
            # Change handle name
            nImage = db.child(user['localId']).child("Image").get().val()     
            if nImage is not None:
                # We plan to store all our image under the child image
                Image = db.child(user['localId']).child("Image").get()
                for img in Image.each():
                    img_choice = img.val()
                st.image(img_choice)

                newImgPath = st.text_input('Enter full path of your profile imgae')
                upload_new = st.button('Upload')
                if upload_new:
                    uid = user['localId']
                    fireb_upload = storage.child(uid).put(newImgPath,user['idToken'])
                    a_imgdata_url = storage.child(uid).get_url(fireb_upload['downloadTokens']) 
                    db.child(user['localId']).child("Image").push(a_imgdata_url)
                    st.success('Success!')           
            # IF THERE IS NO IMAGE
            else:    
                st.info("No profile picture yet")
                newImgPath = st.text_input('Enter full path of your profile image')
                upload_new = st.button('Upload')
                if upload_new:
                    uid = user['localId']
                    # Stored Initated Bucket in Firebase
                    fireb_upload = storage.child(uid).put(newImgPath,user['idToken'])
                    # Get the url for easy access
                    a_imgdata_url = storage.child(uid).get_url(fireb_upload['downloadTokens']) 
                    # Put it in our real time database
                    db.child(user['localId']).child("Image").push(a_imgdata_url)

        elif bio == 'Home':
            # Display the handle name
            nImage = db.child(user['localId']).child("Image").get().val()         
            if nImage is not None:
                val = db.child(user['localId']).child("Image").get()
                for img in val.each():
                    img_choice = img.val()
                st.image(img_choice,use_column_width=True)
            else:
                st.info("No profile picture yet. Go to Edit Profile and choose one!")
            
            post = st.text_input("Let's share my current mood as a post!",max_chars = 100)
            add_post = st.button('Share Posts')
            if add_post:   
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")              
                post = {'Post:' : post,
                        'Timestamp' : dt_string}                           
                results = db.child(user['localId']).child("Posts").push(post)
                st.balloons()

            # This coloumn for the post Display
            all_posts = db.child(user['localId']).child("Posts").get()
            if all_posts.val() is not None:    
                for Posts in reversed(all_posts.each()):
                        st.code(Posts.val(),language = '') 
  
   # WORKPLACE FEED PAGE
        else:
            all_users = db.get()
            res = []
            # Store all the users handle name
            for users_handle in all_users.each():
                k = users_handle.val()["handle"]
                res.append(k)
            # Total users
            nl = len(res)
            st.write('Total users here: '+ str(nl)) 
            
            # Allow the user to choose which other user he/she wants to see 
            choice = st.selectbox('My Collegues',res)
            push = st.button('Show Profile')
            
            # Show the choosen Profile
            if push:
                for users_handle in all_users.each():
                    k = users_handle.val()["handle"]
                    # 
                    if k == choice:
                        lid = users_handle.val()["ID"]
                        
                        handlename = db.child(lid).child("handle").get().val()             
                        
                        st.markdown(handlename, unsafe_allow_html=True)
                        
                        nImage = db.child(lid).child("Image").get().val()         
                        if nImage is not None:
                            val = db.child(lid).child("Image").get()
                            for img in val.each():
                                img_choice = img.val()
                                st.image(img_choice)
                        else:
                            st.info("No profile picture yet. Go to Edit Profile and choose one!")
 
                        # All posts
                        all_posts = db.child(lid).child("Posts").get()
                        if all_posts.val() is not None:    
                            for Posts in reversed(all_posts.each()):
                                st.code(Posts.val(),language = '')