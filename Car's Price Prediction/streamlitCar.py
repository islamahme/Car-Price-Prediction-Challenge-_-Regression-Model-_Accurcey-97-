import streamlit as st
import pandas as pd
import numpy as np
import pickle

# upload Data 
data=pickle.load(open(r"C:\Users\islam\Downloads\AI Work\Car's Price Prediction\car_price_prediction.csv",'rb'))