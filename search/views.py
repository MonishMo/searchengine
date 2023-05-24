from django.shortcuts import render
from .search_service import load_documents,find_similarity


def home(request):
    return render(request, 'index.html')

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q', '').strip()

        dir = r"C:\Users\Windows\Documents\Python Scripts\Q&A using GPT-3\training-data\\"
        documents = load_documents(dir)

        response = find_similarity(documents,query)

        top_response = response[response['similarity'] > 0.8].sort_values(by='similarity', ascending=False)

        context = {'query': query, 'results': top_response['QnA'].to_list()}
        return render(request, 'search.html', context)
    else:
        return render(request, 'index.html')