import streamlit as st

st.set_page_config(
    page_title="Crop Disease Assistant",
    page_icon="🌱"
)

st.title("🌱 Crop Disease Assistant")

language = st.selectbox(
    "Choose your language / ቋንቋ ይምረጡ",
    ["English", "አማርኛ"]
)

if language == "English":
    st.write("Welcome! Upload a picture of your crop.")
    st.subheader("Crop Disease Detection")
    crop = st.selectbox(
        "Choose your crop",
        ["Tomato", "Potato", "Maize", "Wheat"]
    )
    uploaded_file = st.file_uploader(
        "Upload a crop picture",
        type=["jpg", "jpeg", "png"]
    )
else:
    st.write("እንኳን ደህና መጡ! የእርሻ ምርትዎን ፎቶ ይጫኑ።")
    st.subheader("የእፅዋት በሽታ ምርመራ")
    crop = st.selectbox(
        "ሰብሉን ይምረጡ",
        ["ቲማቲም", "ድንች", "በቆሎ", "ስንዴ"]
    )
    uploaded_file = st.file_uploader(
        "የሰብሉን ፎቶ ይጫኑ",
        type=["jpg", "jpeg", "png"]
    )

if uploaded_file:
    st.image(uploaded_file, caption="Your crop picture")
    st.success("Your picture was uploaded successfully!")

    st.info("AI disease analysis will be added in a later step.")
