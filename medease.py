import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
# Set up the page configuration
st.set_page_config(page_title="MedEase", page_icon=":tada:", layout="wide")
image_medease = Image.open('images/logo.png')
st.image(image_medease)
# Function to load Lottie animation from a URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load the Lottie animation using your URL
lottie_url = "https://lottie.host/dab65fbe-1149-434f-accf-bf8282f399c4/g3iUF5gfdf.json"
lottie_json = load_lottieurl(lottie_url)

# Set up the layout with two columns
left_column, right_column = st.columns(2)

# Display content in the left column
with left_column:
    st.title("Hi, welcome to the official MedEase website! Here is a short overview on what we are building")
    st.write('---')

# Display the Lottie animation in the right column
with right_column:
    if lottie_json:
        st_lottie(lottie_json, speed=1, width=200, height=200, key="medanim")
    else:
        st.write("Lottie animation failed to load.")

# Add the container for features
with st.container():
    st.title("Core Features of the App:")

    st.subheader("1. Symptoms-Based Disease Recognition")
    st.write("1. Users input symptoms.")
    st.write("2. AI analyzes the symptoms and identifies the most probable disease.")
    st.write('---')

    st.subheader("2. Medicine Suggestions and Delivery")
    st.write("1. AI provides a list of appropriate medicines for the diagnosed condition.")
    st.write("2. Users can directly order these medicines through the app, and they are delivered to their doorstep.")
    st.write('---')

    st.subheader("3. Doctor Consultation")
    st.write("1. The app offers a feature to consult with certified doctors through chat, video calls, or appointments.")
    st.write('---')

    st.subheader("4. Diet Plans")
    st.write("1. AI suggests personalized diet plans tailored to the specific disease or condition.")
    st.write("2. The plans focus on nutritional needs and the recovery process.")
    st.write('---')

    st.subheader("5. Healthy Food Ordering")
    st.write("1. Users can order pre-made healthy meals directly through the app.")
    st.write("2. The food options align with the recommended diet plan for the diagnosed condition.")
    st.write('---')

    st.title("Benefits of the MedEase App:")
    st.write("1. **Convenience:** Combines diagnosis, treatment, and dietary management in one app.")
    st.write("2. **Accessibility:** Allows easy access to medical advice and products, reducing the need for in-person visits.")
    st.write("3. **Personalization:** Offers tailored solutions for individual health conditions.")
    st.write('---')

    st.title("Additional Considerations for Development:")
    st.write("1. **Regulatory Compliance:** Ensure adherence to medical regulations and data privacy laws in target regions.")
    st.write("2. **Accuracy of Diagnosis:** Integrate a robust medical database and validation system for the AI's recommendations.")
    st.write("3. **User Trust:** Collaborate with certified doctors and pharmacists to validate AI suggestions.")
    st.write("4. **User-Friendly Design:** Ensure the app is intuitive and accessible for all age groups.")

with st.container():
    st.write('---')
    st.header("Our Achievements:")
    st.write('Well, uhh, no achievements yet, but hey, we have a website, thats an achievement right!, butt anyway, here`s a video just for youu')
    st.markdown('[Watch Video...](https://youtu.be/dQw4w9WgXcQ?si=MpgZCcfx3X9qRFwN)')
