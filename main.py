import streamlit as st
import pandas as pd
from game_automator.game_pipeline import GamePipeline
import plotly.express as px 

st.set_page_config(
    page_title="Games",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://erick-faster.github.io/portfolio/',
        'Report a bug': "https://www.linkedin.com/in/erickfasterra/",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

#@st.cache
def game_data():
    game_pipeline = GamePipeline()
    df = game_pipeline.run()
    return df

df = game_data()

st.title("Erick Faster Gamechart")

with st.container():

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        st.metric(label="Total Games", value=df.shape[0])
    
    with col2:
        st.metric(label="Total 5 :star: Rating", value=df.loc[df['rating'] == '5 ⭐⭐⭐⭐⭐'].shape[0])
    
    with col3:
        st.metric(label="Games in 2022", value=df.loc[df['finished'] >= "2022-01-01"].shape[0])
       
    with col4:
        st.metric(label="Total Hours", value=df['hours'].sum())

    with col5:
        st.metric(label="Favorite Genre", value=df.loc[(df['status'] == 'Finished') & (df['rating'] == '5 ⭐⭐⭐⭐⭐'), 'genre'].value_counts().sort_values(ascending=False).head(1).index.item())

    with col6:
        st.metric(label="Overrated Genre", value=df.loc[(df['genre'] != 'undefined') &(~df['rating'].isin(['5 ⭐⭐⭐⭐⭐', '4 ⭐⭐⭐⭐'])), 'genre'].value_counts().sort_values(ascending=False).head(1).index.item())

with st.container():
    col7, col8, col9 = st.columns(3)

    with col7:
        fig_status=px.bar(df['status'].value_counts(), orientation='h').update_layout(title_text='<b>Games by Status</b>', title_x=0.5, xaxis_title="No. of Games", yaxis_autorange="reversed" , yaxis_title="Status", showlegend=False)
        st.write(fig_status)

    with col8:
        fig_genre=px.bar(df.loc[df['status'] == 'Finished', 'genre'].value_counts(), orientation='h').update_layout(title_text='<b>Games finished by Genre</b>', title_x=0.5, xaxis_title="No. of Games", yaxis_autorange="reversed", yaxis_title="Genre", showlegend=False)
        st.write(fig_genre)

    with col9:
        fig_rating=px.bar(df.loc[df['status'].isin(['Finished', 'Dropped']), 'rating'].value_counts(), orientation='h').update_layout(title_text='<b>Games played by Rating</b>', title_x=0.5, xaxis_title="No. of Games", yaxis_autorange="reversed", yaxis_title="Rating", showlegend=False)
        st.write(fig_rating)

with st.container():
    colempty1, col10, colempty2 = st.columns([4,5,4])

    with colempty1:
        st.write(' ')

    with col10:
        st.write(df)

    with colempty2:
        st.write(' ')



