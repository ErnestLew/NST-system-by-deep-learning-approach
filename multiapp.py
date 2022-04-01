"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st

class MultiApp:
    """Framework for combining multiple streamlit applications.
    """
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.

        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # app = st.sidebar.radio(
        menu = ['Style Transfer', 'Advanced Features']
        app = st.sidebar.selectbox(
            'Select from the options',
            menu,
            format_func=lambda app: app['title'])
        
        cont = st.beta_container()
        col1 , col2 = st.beta_columns(2)
        with col1:
            style = st.sidebar.selectbox("Select the option of style transfers", self.apps)
        with col2: 
            advanced = st.sidebar.selectbox("Select the advanced features", self.apps)
        
   

        app['function']()
