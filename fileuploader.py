#import required libraries
import streamlit as st
import PIL
# setting page layout
st.set_page_config(
    page_title = "Object detection using YOLOv8",
    page_icon = "🤖",
    layout = "wide",
    initial_sidebar_state = "expanded"
)
#creating sidebar
with st.sidebar:
    st.header("Image/Video config")
    # adding file uploader to sidebar for selecting images
    source_img = st.sidebar.file_uploader(
        "choose an image...", type = ("jpg", "jpeg", "png", "bmp", "webp")
    )

# creating main page heading
st.title("Object detection using YOLOv8")

#creating two columns on the main page
col1, col2 = st.columns(2)

#Adding image to the first column if image is uploaded
with col1:
    if source_img:
        # opening the uploaded image
        uploaded_image = PIL.Image.open(source_img)
        #Adding the uploaded image to the page with a caption
        st.image(source_img,
                 caption="Uploaded Image",
                 use_column_width=True
                 )

