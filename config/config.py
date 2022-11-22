# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:01:49 2022

@author: erick
"""

import streamlit as st

TOKEN = st.secrets['auth_token']

ID_DATABASE = '87301605d49f4b25a0ebb05e6c12148d'

HEADERS = {
    "Authorization": "Bearer " + TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2021-08-16"
}

URL = f'https://api.notion.com/v1/databases/{ID_DATABASE}/query'