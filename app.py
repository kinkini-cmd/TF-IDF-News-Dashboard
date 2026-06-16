import streamlit as st
import requests
import re
import nltk
import pandas as pd
import plotly.express as px

from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# ==========================
# NLTK Downloads
# ==========================
nltk.download('stopwords')
nltk.download('wordnet')

# ==========================
# Page Config
# ==========================
st.set_page_config(
    page_title="TF-IDF News Analyzer",
    page_icon="📰",
    layout="wide"
)

# ==========================
# Custom CSS
# ==========================
st.markdown("""
<style>

.main {
    background-color:#f5f7ff;
}

.title {
    text-align:center;
    color:#6C63FF;
    font-size:42px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:gray;
}

.stButton>button{
    background: linear-gradient(90deg,#6C63FF,#FF4B91);
    color:white;
    border:none;
    border-radius:10px;
    height:50px;
    width:100%;
    font-size:18px;
}

.metric-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# ==========================
# NLP Setup
# ==========================
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# ==========================
# Preprocessing Function
# ==========================
def preprocess(text):

    text = text.lower()

    text = re.sub(r"http\\S+", "", text)

    text = re.sub(r"[^a-zA-Z ]", " ", text)

    words = text.split()

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words and len(word) > 2
    ]

    return " ".join(words)

# ==========================
# Extract Text From URL
# ==========================
def extract_text(url):

    response = requests.get(url, timeout=15)

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    for tag in soup(
        ["script","style","nav","footer","header"]
    ):
        tag.decompose()

    text = soup.get_text(
        separator=" ",
        strip=True
    )

    return text

# ==========================
# Dashboard Header
# ==========================
st.markdown(
    "<h1 class='title'>TF-IDF News Analyzer</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Analyze any article URL using TF-IDF</p>",
    unsafe_allow_html=True
)

st.divider()

# ==========================
# URL Input
# ==========================
url = st.text_input(
    "Enter News URL",
    placeholder="https://example.com/article"
)

# ==========================
# Analyze Button
# ==========================
if st.button("Analyze Article"):

    if url == "":
        st.warning("Please enter a URL")

    else:

        try:

            # Extract article
            raw_text = extract_text(url)

            # Preprocess
            clean_text = preprocess(raw_text)

            # TF-IDF
            vectorizer = TfidfVectorizer(
                max_features=20
            )

            tfidf_matrix = vectorizer.fit_transform(
                [clean_text]
            )

            features = vectorizer.get_feature_names_out()

            scores = tfidf_matrix.toarray()[0]

            df = pd.DataFrame({
                "Keyword":features,
                "Score":scores
            })

            df = df.sort_values(
                by="Score",
                ascending=False
            )

            # =====================
            # Metrics
            # =====================
            col1,col2,col3 = st.columns(3)

            col1.metric(
                "Total Words",
                len(clean_text.split())
            )

            col2.metric(
                "Unique Keywords",
                len(features)
            )

            col3.metric(
                "URL Status",
                "Success"
            )

            st.divider()

            # =====================
            # Text Display
            # =====================
            st.subheader("🧹 Preprocessed Text")

            st.text_area(
                "",
                clean_text[:5000],
                height=250
            )

            st.divider()

            # =====================
            # TF-IDF Table
            # =====================
            st.subheader(
                "TF-IDF Keywords"
            )

            st.dataframe(
                df,
                use_container_width=True
            )

            # =====================
            # Plotly Chart
            # =====================
            fig = px.bar(
                df,
                x="Score",
                y="Keyword",
                orientation="h",
                color="Score",
                text="Score"
            )

            fig.update_layout(
                height=500
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            # =====================
            # Top Keywords
            # =====================
            st.subheader(
                "Top 10 Keywords"
            )

            top10 = df.head(10)

            for _,row in top10.iterrows():

                st.success(
                    f"{row['Keyword']}  →  {row['Score']:.4f}"
                )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )