V# 📰 TF-IDF News Analyzer Dashboard

## Project Description

The TF-IDF News Analyzer Dashboard is a Natural Language Processing (NLP) application that extracts text from any news article URL, preprocesses the content, and identifies the most important keywords using the TF-IDF (Term Frequency-Inverse Document Frequency) algorithm.

The system automatically collects article content from a user-provided URL, removes unnecessary information, cleans the text, and generates keyword importance scores. The results are displayed through an interactive and user-friendly Streamlit dashboard.

---

## Objectives

* Extract textual content from online news articles.
* Preprocess and clean the extracted text.
* Apply TF-IDF feature extraction.
* Identify important keywords from articles.
* Visualize keyword importance using charts and tables.
* Provide an easy-to-use dashboard for text analysis.

---

## Technologies Used

* Python
* Streamlit
* BeautifulSoup
* Requests
* NLTK
* Scikit-Learn
* Pandas
* Plotly

---

## System Workflow

1. User enters a news article URL.
2. The application downloads the webpage content.
3. BeautifulSoup extracts visible text from the webpage.
4. The extracted text is preprocessed:

   * Convert text to lowercase
   * Remove punctuation and special characters
   * Remove numbers
   * Remove stop words
   * Perform lemmatization
5. TF-IDF vectorization is applied.
6. Top keywords and scores are generated.
7. Results are displayed through charts and tables.

---

## Text Preprocessing Steps

### Lowercasing

All text is converted to lowercase to maintain consistency.

Example:

Before:
The Government Announces New Policies

After:
the government announces new policies

### Removing Special Characters

All punctuation marks and special symbols are removed.

Before:
Economy grows by 5% in 2025!

After:
economy grows by in

### Stop Word Removal

Common words that do not contribute significant meaning are removed.

Examples of stop words:

* the
* is
* are
* and
* in
* of
* to
* for

Before:
the government is working on new policies

After:
government working new policies

### Lemmatization

Words are converted to their base form.

Examples:

* running → run
* cars → car
* studies → study

---

## TF-IDF Concept

### Term Frequency (TF)

Term Frequency measures how frequently a term appears in a document.

TF(t,d) = Number of occurrences of term t in document d / Total number of terms in document d

### Inverse Document Frequency (IDF)

Inverse Document Frequency measures how unique a term is across multiple documents.

IDF(t) = log(Total Documents / Documents Containing t)

### TF-IDF Score

TF-IDF Score = TF × IDF

A high TF-IDF score indicates that the term is important in the current document but rare across the collection of documents.

---

## Dashboard Features

### URL Input

Users can enter any valid news article URL.

### Article Extraction

Automatically extracts visible content from webpages.

### Text Preprocessing

Displays cleaned and processed article text.

### TF-IDF Analysis

Generates keyword importance scores.

### Interactive Charts

Visualizes TF-IDF results using Plotly charts.

### Statistics

Displays:

* Total number of words
* Number of unique keywords
* URL processing status

---

## Example Input

[https://www.example.com/news/article](https://www.example.com/news/article)

---

## Example Output

Top Keywords:

government – 0.412

economy – 0.398

inflation – 0.365

market – 0.331

policy – 0.289

---

## Advantages

* Fast keyword extraction
* Automated news analysis
* Interactive dashboard interface
* Easy to use
* Useful for NLP learning and research

---

## Future Enhancements

* Fake News Detection using Machine Learning
* Sentiment Analysis
* News Summarization
* Word Cloud Generation
* PDF Report Export
* Multi-Article Comparison
* Dark Mode Interface
* Source Credibility Analysis

---

## Conclusion

The TF-IDF News Analyzer Dashboard demonstrates the application of Natural Language Processing techniques for extracting and analyzing information from online news articles. By combining web scraping, text preprocessing, and TF-IDF vectorization, the system effectively identifies significant keywords and presents the results through an interactive dashboard. This project serves as a practical implementation of NLP concepts and can be extended further for fake news detection, sentiment analysis, and advanced text analytics.
