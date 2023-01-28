import streamlit as st
from PIL import Image

st.set_page_config(page_title="Image Merger", page_icon=":guardsman:", layout="wide")

st.title("pooleno watchlist maker")

picture1 = st.file_uploader("Upload First Picture", type=["jpg", "jpeg", "png"])
picture2 = st.file_uploader("Upload Second Picture", type=["jpg", "jpeg", "png"])
picture3 = st.file_uploader("Upload Third Picture", type=["jpg", "jpeg", "png"])
background = Image.open("background.png").convert("RGBA")
foreground = Image.open("forground.png").convert("RGBA")

if st.button("Merge"):
    if picture1 and picture2 and picture3 and background:
        try:
            # Open the images
            picture1 = Image.open(picture1).convert("RGBA")
            picture2 = Image.open(picture2).convert("RGBA")
            picture3 = Image.open(picture3).convert("RGBA")

            # Resize and paste images on background
            #1
            picture1 = picture1.resize((119,119))
            x, y = picture1.size
            background.paste(picture1, (411, 287), picture1)
            #2
            picture2 = picture2.resize((119,119))
            x, y = picture2.size
            background.paste(picture2, (559, 310), picture2)
            #3
            picture3 = picture3.resize((119,119))
            x, y = picture3.size
            background.paste(picture3, (695, 288), picture3)

            background.paste(foreground, (0, 0), foreground)
            # Save the final image
            background.convert("RGB").save('final-watchlist.png', format="PNG")

            # Show the final image
            st.image(background)
            st.success("Image Merged Successfully!")
        except Exception as e:
            st.error(e)
    else:
        st.warning("Please upload all the images")
