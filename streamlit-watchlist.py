import streamlit as st
from PIL import Image

st.set_page_config(page_title="Image Merger", page_icon=":guardsman:", layout="wide")

st.title("Image Merger")

picture1 = st.file_uploader("Upload First Picture", type=["jpg", "jpeg", "png"])
picture2 = st.file_uploader("Upload Second Picture", type=["jpg", "jpeg", "png"])
picture3 = st.file_uploader("Upload Third Picture", type=["jpg", "jpeg", "png"])
background = st.file_uploader("Upload Background Picture", type=["jpg", "jpeg", "png"])

if st.button("Merge"):
    if picture1 and picture2 and picture3 and background:
        try:
            # Open the images
            picture1 = Image.open(picture1).convert("RGBA")
            picture2 = Image.open(picture2).convert("RGBA")
            picture3 = Image.open(picture3).convert("RGBA")
            background = Image.open(background).convert("RGBA")

            # Resize and paste images on background
            picture1 = picture1.resize((130,130))
            x, y = picture1.size
            background.paste(picture1, (405, 284), picture1)

            picture2 = picture2.resize((130,130))
            x, y = picture2.size
            background.paste(picture2, (535, 307), picture2)

            picture3 = picture3.resize((130,130))
            x, y = picture3.size
            background.paste(picture3, (670, 279), picture3)

            # Save the final image
            background.convert("RGB").save('final-watchlist.png', format="PNG")

            # Show the final image
            st.image(background)
            st.success("Image Merged Successfully!")
        except Exception as e:
            st.error(e)
    else:
        st.warning("Please upload all the images")
