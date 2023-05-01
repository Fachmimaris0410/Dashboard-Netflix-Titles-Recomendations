import pandas as pd
import pickle
from PIL import Image
import streamlit as st
import plotly.express as px


data = pd.read_csv('netflix_titles.csv')

def recommend(type, release_year):
    recommendations = data[(data['type'] == type) & (data['release_year'] == release_year)]['title'].tolist()
    if recommendations:
        return recommendations
    else:
        return ['No recommendations found.']
    
def app():
    # Set the title and layout (must be the first Streamlit command in your script)
    st.set_page_config(page_title='Title Recommender', layout='wide')

    st.title('Title Recommender')
    px.defaults.template = "plotly_dark"
    px.defaults.color_continuous_scale = "reds"

    img = Image.open("D:\PIP HackerRank\PIP dashboard streamlit\logo.png")
    st.sidebar.image(img)

    # Add input widgets for type and release year
    type = st.selectbox('Select type:', data['type'].unique())
    release_year = st.selectbox('Select release year:', data['release_year'].unique())
    
    # Call the recommend function and display the recommendations
    recommendations = recommend(type, release_year)
    st.write('Recommended titles:')
    df = pd.DataFrame({'Recommended titles': recommendations})
    st.write(df)

# Run the app
if __name__ == '__main__':
    app()
