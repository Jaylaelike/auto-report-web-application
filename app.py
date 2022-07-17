from turtle import up
from webbrowser import get
import streamlit as st
import pandas as pd
import os
import os.path
from time import process_time

from io import BytesIO, IOBase
import plotly.express as px  # pip install plotly-express

import subprocess
import sys




st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
st.title('🚀 Auto Diary Report Chumphon 📊 ☕')


def upload_file_process():
    
    try:
            uploaded_file = st.file_uploader("Choose a file")

            if uploaded_file is not None:
                df = pd.read_excel(
                        io=uploaded_file,
                        engine="openpyxl",
                        sheet_name="CHP",
                        skiprows=3,
                        usecols="A:AJ",
                        nrows=1000,
                    )  
            fileContent = df.astype(str)
            st.dataframe(fileContent)
            
            if (uploaded_file != ''):
                with open(os.path.join("tempDir","data.xlsx"),"wb") as f: 
                    f.write(uploaded_file.getbuffer())         
                    st.success("Saved File")

    except:
        pass   
   


def download_file():
 with open('รายงานประจำวันฝ่ายระบบส่งสัญญาณชุมพร.xlsx', 'rb') as my_file:
  st.download_button(label = 'Download', data = my_file, file_name = 'รายงานประจำวัน_success.xlsx', mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')   


def button_run_app():
    button1 = st.button("Click to run")
    if button1:
        subprocess.run([f"{sys.executable}", "api.py"])
        st.write("finished")



upload_file_process()
button_run_app()
download_file()



