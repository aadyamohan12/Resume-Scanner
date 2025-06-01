import torch
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from sklearn.metrics.pairwise import cosine_similarity

# Load once and cache
embed_model = SentenceTransformer("all-MiniLM-L6-v2")
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def get_embedding(text):
    return embed_model.encode([text])[0]

def match_keywords(resume_text, skills_list):
    matches = []
    text = resume_text.lower()
    for skill in skills_list:
        if skill.lower() in text:
            matches.append(skill)
    return matches

def calculate_weighted_score(must, nice, resume_text):
    must_matches = match_keywords(resume_text, must)
    nice_matches = match_keywords(resume_text, nice)
    total_score = (2 * len(must_matches)) + (1 * len(nice_matches))
    max_possible = (2 * len(must)) + (1 * len(nice)) or 1
    return total_score / max_possible, must_matches, nice_matches

def summarize_resume(text):
    return summarizer(text[:1024], max_length=100, min_length=30, do_sample=False)[0]["summary_text"]
