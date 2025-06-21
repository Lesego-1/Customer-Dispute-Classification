from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import joblib
import numpy as np
from django.conf import settings
import os
import spacy
import re

def vectorizer(text:str):
    text = text.lower()  # Lowercase the text
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    text = re.sub(r"[\s+]", " ", text)  # Replace multiple spaces with one space
    
    # Vectorize the text
    nlp = spacy.load('en_core_web_lg')
    doc = nlp(text)
    return doc.vector  # Return the vectorized text

# Create your views here.
def index(request):
    return render(request, "index.html")

@api_view(["POST"])
def predict_dispute(request):
    text = request.data.get("text")  # Get text input
    if not text:
        return Response({"error": "Text input is required."}, status=400)
    BASE_DIR = settings.BASE_DIR
    model_text = vectorizer(text)  # Vectorize text
    model_text = model_text.reshape(1, -1)
    
    # Load models
    clf_model_path = os.path.join(BASE_DIR, "disputes", "models", "model.pkl")
    summarization_model_path = os.path.join(BASE_DIR, "disputes", "models", "summarization_model.pkl")
    classification_model = joblib.load(clf_model_path)
    summarization_model = joblib.load(summarization_model_path)

    # Generate results
    confidence = classification_model.predict(model_text)
    result = np.argmax(confidence, axis=1)  # Get the binary classification for the results
    if result[0] == 1:
        result = "Dispute"
    else:
        result = "No Dispute"
            
    confidence = np.max(confidence, axis=1)  # Get the highest confidence
    summary = summarization_model(text, max_length=50, min_length=20, do_sample=False)
    
    # Return JSON response
    print(Response({
        'result':result,
        'summary':summary[0]["summary_text"],
        'confidence':confidence,
        'original_text':text
    }))
    return Response({
        'result':result,
        'summary':summary[0]["summary_text"],
        'confidence':confidence,
        'original_text':text
    })