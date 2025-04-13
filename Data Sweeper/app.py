import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Page Configuration
st.set_page_config(
    page_title="Data Sweeper", 
    page_icon="🧹", 
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get help": "https://www.google.com/search?q=help",
        "Report a bug": "https://github.com/streamlit/streamlit/issues",
        "About": """# SMAASU Corporation©️  
        https://tinyurl.com/smaasu"""}
    )

st.write("# 🧹 DataSet Sweeper")
files = st.file_uploader("Upload", type=["csv", "xlsx"], accept_multiple_files=True)
for file in files:
    # Convert file to pandas dataframe
    file_ext = os.path.splitext(file.name)[-1].lower()
    if file_ext == ".csv":
        df = pd.read_csv(file)
    elif file_ext == ".xlsx":
        df = pd.read_excel(file)
    else:
        st.write(f"Error {file_ext} is not supported 🤪")
    
    
    st.write(f"**Name :** {file.name}")
    st.write(f"**Size :** {file.size/1024:.2f} KB")
    # st.write(f"**Description :** {file.description}")
    # see_df = st.checkbox("Preview DataSet")
    if st.checkbox("Preview DataSet"):
        #df = pd.read_csv(file)
        st.dataframe(df.head())
    st.write("# Data Cleaning")
    if st.checkbox("Clean DataSet"):
        col1, col2, col3 = st.columns([1,1,2])
        with col1:
            if st.checkbox("Clean Duplicates"):
                st.write(f"**Rows Before** {df.size/len(df.columns)}")
                df.drop_duplicates(inplace=True)
                st.write(f"**Rows After** {df.size/len(df.columns)}")
                st.success("All Duplicates were successfully Cleaned up", icon="😇")
        with col2:
            if st.checkbox("Clean Nully Values"):
                st.write(f"**Rows Before** {df.size/len(df.columns)}")
                df.dropna(inplace=True)
                # z  len(df.columns)
                st.write(f"**Rows After** {df.size/len(df.columns)}")
                st.success("All Nully were successfully Dusted up", icon="😎")
        with col3:
            if st.checkbox("Clean Missing Values"):
                col3_1, col3_2 = st.columns(2)
                with col3_1:
                    st.write("**Null Before After**")
                    num_col = df.select_dtypes('number').columns
                    for col in num_col:  # Assuming num_col is a list of numerical column names
                        st.write(f"**{" ".join(word.capitalize() for word in col.split())}**: {df[col].isnull().sum()}")
                with col3_2:
                    st.write("**Null Value After**")
                    df[num_col] = df[num_col].fillna(df[num_col].mean())
                    for col in num_col:  # Assuming num_col is a list of numerical column names
                        st.write(f"**{" ".join(word.capitalize() for word in col.split())}**: {df[col].isnull().sum()}")
                st.success("All Missing Values were successfully Filled up", icon="🎉")

    #Select the Columns to remain  
    st.header("Select Column")
    elect_col = st.multiselect("Select Column :", options=df.columns, default=df.columns)
    df = df[elect_col]  
    st.write(df.head(5))

    #Visualize any columns
    st.header("Select any two columns to visualize")
    if st.checkbox("Select any two columns to visualize"):
        #visual_col = st.multiselect("Select any two columns to visualize", df.columns, default=df.columns)
        st.bar_chart(df.select_dtypes('number').iloc[:,:2] )

    conversion_type = st.radio("Click to convert the file format !", ["csv", "xlsx"])
    if st.button("Just Convert It"):
        buffer = BytesIO()
        if conversion_type == "csv":
            df.to_csv(buffer, index=False)
            file_name = file.name.replace(file_ext,".csv")
            mime_type = "text/csv"
        
        elif conversion_type == "xlsx":
            df.to_excel(buffer, index=False)
            file_name = file.name.replace(file_ext,".xlsx")
            mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml"
        buffer.seek(0)
    
        #Download File
        st.download_button(
            label="Download",
            data=buffer,
            file_name=file_name,
            mime=mime_type
        )


