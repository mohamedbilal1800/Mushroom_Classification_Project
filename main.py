import pickle 
import numpy as np
import streamlit as st


st.set_page_config(page_title="Mushroom Classifier", page_icon="🍄", layout="wide")

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

with open("Mushroom_model_data.pkl", "rb") as obj1:
    dict1 = pickle.load(obj1)

model = dict1['model']
encoders = dict1['encoders']


st.title("Mushroom Classifier 🍄")
st.sidebar.title("About the App")
st.sidebar.markdown(
    """
    This Mushroom Classifier Web Application classifies mushrooms as edible or poisonous
    based on the following features:
    
    - Class
    - Cap Diameter
    - Cap Shape
    - Cap Color
    - Does Bruise or Bleed
    - Gill Color
    - Stem Height
    - Stem Width
    - Stem Color
    - Has Ring
    - Habitat
    - Season
    
    Enter the required values to classify the mushroom accurately.
    """
)


col1, col2, col3 = st.columns(3)

with col1:
    cap_diameter = st.number_input("Enter the diameter of mushroom cap: ", 0.0, 60.0)

    cap_shape = st.selectbox("Select the shape of mushroom cap: ", ['convex', 'flat', 'sunken', 'bell', 'others', 'spherical', 'conical'])
    cap_shape_val = int(encoders['cap_shape'].transform([cap_shape])[0])

    cap_color = st.selectbox("Select the color of mushroom cap: ", ['orange', 'red', 'brown', 'gray', 'green', 'white', 'yellow', 'pink', 'purple', 'buff', 'blue', 'black'])
    cap_color_val = int(encoders['cap_color'].transform([cap_color])[0])

    gill_color = st.selectbox("Select the color of gills in the mushroom: ", ['white', 'brown', 'pink', 'purple', 'buff', 'gray', 'yellow', 'green', 'red', 'orange', 'black', 'none'])
    gill_color_val = int(encoders['gill_color'].transform([gill_color])[0])
    
    
with col2:
    stem_height = st.number_input("Enter the height of stem: ", 0.0, 34.0)

    stem_width = st.number_input("Enter the width of stem: ", 0.0, 103.0)

    stem_color = st.selectbox("Select the color of stem: ", ['white', 'yellow', 'brown', 'purple', 'buff', 'blue', 'green', 'pink', 'red', 'black', 'gray', 'orange', 'none'])
    stem_color_val = int(encoders['stem_color'].transform([stem_color])[0])

    habitat = st.selectbox("Select the habitat of mushroom: ", ['woods', 'meadows', 'grasses', 'heaths', 'leaves', 'paths', 'waste', 'urban'])
    habitat_val = int(encoders['habitat'].transform([habitat])[0])

with col3:
    season = st.selectbox("Select the season: ", ['winter', 'summer', 'autumn', 'spring'])
    season_val = int(encoders['season'].transform([season])[0])

    has_ring = st.radio("Does the mushroom have rings: ", ['yes', 'no'])
    has_ring_val = int(encoders['has_ring'].transform([has_ring])[0])

    does_bruise_or_bleed = st.radio("Does the mushroom have bruises or bleeds: ", ['yes', 'no'])
    does_bruise_or_bleed_val = int(encoders['does_bruise_or_bleed'].transform([does_bruise_or_bleed])[0])


predict_button = st.button("Predict")


if predict_button:

    test = [[cap_diameter, cap_shape_val, cap_color_val, does_bruise_or_bleed_val, gill_color_val, stem_height, stem_width, stem_color_val, has_ring_val, habitat_val, season_val]]

    pred =  round(model.predict(test)[0])

    result = encoders['class'].inverse_transform([pred])[0]

    if result == 'edible':
        st.success("✅ The mushroom is Edible!")
    else:
        st.error("❌ The mushroom is Poisonous!")