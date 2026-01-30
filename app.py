import streamlit as st
import pickle
import numpy as np
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Book Buddy", page_icon="📚", layout="wide")

@st.cache_resource 
def load_data():
    model = pickle.load(open('model.pkl', 'rb'))
    pivot_table = pickle.load(open('pivot_table.pkl', 'rb'))
    books_metadata = pickle.load(open('books_metadata.pkl', 'rb'))
    pivot_table.fillna(0, inplace=True)
    popular = pickle.load(open('popular.pkl', 'rb'))
    return model, pivot_table, books_metadata, popular

try:
    model, pivot_table, books_metadata, popular = load_data()
except Exception as e:
    st.error(f"Error loading files: {e}")

# 3. Custom CSS
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
    .book-title { font-size: 14px; font-weight: bold; margin-top: 10px; height: 3em; overflow: hidden; }
    </style>
    """, unsafe_allow_html=True)
st.title("📚 Book Recommendation System")

# 5. The "Smart" Search Bar
book_list = pivot_table.index.tolist()

# We use a selectbox but we allow it to be empty
# Streamlit's selectbox has a built-in search/autocomplete
selected_book = st.selectbox(
    "Search for a book:", 
    options=book_list, 
    index=None, 
    placeholder="Start typing (e.g., Harry Potter)..."
)

def display_books(book_identifiers, is_title_list=False):
    cols = st.columns(5)
    for i in range(5):
        title = book_identifiers[i] if is_title_list else pivot_table.index[book_identifiers[i]]
        with cols[i]:
            try:
                img_url = books_metadata[books_metadata['Book-Title'] == title]['Image-URL-M'].values[0]
            except:
                img_url = "https://via.placeholder.com/150"
            st.image(img_url, use_container_width=True)
            st.markdown(f"<p class='book-title'>{title}</p>", unsafe_allow_html=True)

# 6. Button Logic
if st.button('Get Recommendations'):
    if selected_book in pivot_table.index:
        # CASE: Book Found
        idx = np.where(pivot_table.index == selected_book)[0][0]
        distances, indices = model.kneighbors(pivot_table.iloc[idx, :].values.reshape(1, -1), n_neighbors=6)
        
        st.subheader(f"Because you liked '{selected_book}':")
        display_books(indices.flatten()[1:])
    else:
        # CASE: Book Not Found or Empty
        st.warning("We couldn't find that exact title in our 'Famous Books' collection.")
        st.subheader("But you might enjoy these all-time favorites:")
        display_books(popular, is_title_list=True)