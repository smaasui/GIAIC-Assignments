import streamlit as st
import pandas as pd

st.set_page_config(page_title="Personal Library", layout="centered", initial_sidebar_state="expanded", page_icon="📚")

# Initialize session state for book list
if "library" not in st.session_state:
    st.session_state.library = []

st.title("📚 My Simple Personal Library")

st.header("➕ Add a New Book")
with st.form("book_form"):
    isbn = st.text_input("ISBN")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=0, max_value=2100, step=1)
    submit = st.form_submit_button("Add Book")

    if submit:
        if isbn and title and author:
            st.session_state.library.append({
                "ISBN": isbn,
                "Title": title,
                "Author": author,
                "Year": int(year)
            })
            st.success("Book added!")
        else:
            st.warning("Please fill in ISBN, Title, and Author")

st.header("📖 My Book List")
if len(st.session_state.library) > 0:
    df = pd.DataFrame(st.session_state.library)
    st.table(df)
else:
    st.info("No books added yet.")
