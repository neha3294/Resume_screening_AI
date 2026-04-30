import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

def preprocess(text):
    return text.lower()

def get_similarity(resume, job_desc):
    texts = [resume, job_desc]
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    return round(similarity[0][0] * 100, 2)

def extract_skills(text):
    skills_list = ["python", "sql", "excel", "power bi", "tableau", "c#", "asp.net"]
    
    found_skills = []
    for skill in skills_list:
        if skill in text.lower():
            found_skills.append(skill)
    
    return found_skills