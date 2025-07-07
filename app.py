import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("book.csv")
    df['description'] = df['description'].fillna('')
    df['combined'] = df['title'] + ' ' + df['author'] + ' ' + df['genre'] + ' ' + df['description']
    return df

df = load_data()

# Compute similarity matrix
@st.cache_data
def compute_similarity(df):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['combined'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

cosine_sim = compute_similarity(df)
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

# Recommendation function
def recommend(title, num_recommendations=5):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    book_indices = [i[0] for i in sim_scores]
    return df.iloc[book_indices]

# Streamlit UI
st.title("📚 Book Recommendation System")
st.write("Find books similar to your favorite.")

# Language filter
language_option = st.selectbox("Choose language", ["All", "English", "Hindi"])

if language_option != "All":
    filtered_df = df[df['language'] == language_option]
else:
    filtered_df = df

# Search bar & matches
search_input = st.text_input("Search for a book title")
matches = filtered_df[filtered_df['title'].str.contains(search_input, case=False, na=False)] if search_input else pd.DataFrame()

if not matches.empty:
    selected_book = st.selectbox("Select from matching titles", matches['title'].unique())
    if st.button("Recommend"):
        recommendations = recommend(selected_book)
        st.subheader(f"Because you like '{selected_book}', you might also like:")
        for _, row in recommendations.iterrows():
            col1, col2 = st.columns([1,3])
            with col1:
                st.image(row['cover_url'], width=100)
            with col2:
                st.markdown(f"### {row['title']} by {row['author']}")
                st.markdown(f"⭐ **Rating:** {row['rating']}/5")
                st.markdown(f"{row['description']}")
else:
    if search_input:
        st.info("No matches found. Try another title or language.")
