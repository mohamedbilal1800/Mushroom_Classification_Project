# 🍄 Mushroom Classification Project

This repository contains the **Mushroom Classification Project**, a machine learning-based web application that classifies mushrooms as **edible** or **poisonous** based on various features. The project includes a **Jupyter Notebook** for data analysis and model development, as well as a **Streamlit web app** for user interaction.

---

## 📋 **Project Overview**
Mushrooms are fascinating fungi that can be both a delicacy and a danger. Some mushrooms are edible, while others are highly toxic. The **Mushroom Classification Project** aims to build a machine learning model that accurately classifies mushrooms as either **edible** or **poisonous** based on specific features such as:
- Cap diameter
- Cap shape
- Cap color
- Gill color
- Stem height and width
- Habitat
- Season
- Presence of rings

The project leverages data analysis, preprocessing, and model selection to achieve an accurate classification model. The web app provides an intuitive interface for users to input mushroom features and receive predictions in real-time.

---

## 📊 **Dataset Description**
The dataset used for this project contains detailed information about mushrooms, including:
- **Class**: Edible or poisonous
- **Cap shape**: Convex, flat, sunken, etc.
- **Cap color**: Red, brown, yellow, etc.
- **Gill color**: White, pink, purple, etc.
- **Stem properties**: Height, width, color
- **Habitat**: Woods, meadows, grasses, etc.
- **Season**: Spring, summer, autumn, winter

The dataset has been preprocessed to handle categorical variables using label encoding.

---

## 📚 **Tech Stack**
- **Python**
- **Pandas** for data manipulation
- **Scikit-learn** for model building
- **Streamlit** for creating the web application
- **Pickle** for saving the trained model

---

## 🛠 **Project Structure**
```
├── main.py                 # Streamlit app
├── ML_008_Classification_Task.ipynb  # Jupyter Notebook for data analysis
├── Mushroom_model_data.pkl  # Serialized model and encoders
├── License
└── README.md               # Project documentation
```

---

## ⚙️ **Setup Instructions**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mushroom-classification.git
   cd mushroom-classification
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

---

## 🚀 **Usage Guidelines**
1. Open the Streamlit web app in your browser.
2. Enter the required mushroom features such as cap diameter, shape, color, etc.
3. Click the **Predict** button.
4. The app will display whether the mushroom is **Edible** or **Poisonous**.

---

## ✅ **Results**
The models - KNeighborsClassifier, DecisionTreeClassifier, and RandomForestClassifier achieved high accuracy results of 98.77%, 98.52%, and 99.57% respectively in classifying mushrooms, effectively distinguishing between edible and poisonous varieties. RandomForestClassifier was chosen as the best model. The prediction is displayed with a friendly UI, making it easy for users to interact with the model.

---
