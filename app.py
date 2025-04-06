from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def plagiarism_checker(text1, text2):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([text1, text2])

    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return similarity_score[0][0]


text1 = "This is a sample text."
text2 = "This is another a example text that is similar but not identical, but still has a difference."
score = plagiarism_checker(text1, text2)
print(f"Similarity score: {score}")
