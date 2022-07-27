import matplotlib.colors as mcolors
import gensim
import gensim.corpora as corpora
from operator import index
from wordcloud import WordCloud
from pandas._config.config import options
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import Similar
from PIL import Image
import time
# import sys


image = Image.open('Images//unnamed.png')

st.title("Resume Scoring extension")
dataset = pd.read_csv('parsed_data.csv')
st.markdown("---")