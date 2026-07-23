import requests
from django.shortcuts import redirect, render
from .forms import SearchForm
from .models import SearchHistory

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def fetch_word_data(word):
    response = requests.get(f"{API_URL}{word}", timeout=10)
    if response.status_code != 200:
        return None
    return response.json()


def home_view(request):
    form = SearchForm()
    recent = SearchHistory.objects.all()[:6]
    return render(request, "dictionary/home.html", {"form": form, "recent_searches": recent})


def search_view(request):
    form = SearchForm(request.GET or None)
    if form.is_valid():
        word = form.cleaned_data["word"].strip().lower()
        SearchHistory.objects.create(word=word)
        return redirect("dictionary:detail", word=word)
    recent = SearchHistory.objects.all()[:6]
    return render(request, "dictionary/home.html", {"form": form, "recent_searches": recent})


def word_detail_view(request, word):
    data = fetch_word_data(word)
    if not data:
        return render(request, "dictionary/error.html", {"word": word})

    definitions = []
    for entry in data:
        for meaning in entry.get("meanings", []):
            part_of_speech = meaning.get("partOfSpeech")
            for definition in meaning.get("definitions", []):
                definitions.append({
                    "part_of_speech": part_of_speech,
                    "definition": definition.get("definition"),
                    "example": definition.get("example"),
                    "synonyms": definition.get("synonyms", []),
                    "antonyms": definition.get("antonyms", []),
                })

    return render(request, "dictionary/detail.html", {
        "word": word,
        "definitions": definitions,
    })
