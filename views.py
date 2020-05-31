from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    print(djtext)
    print(removepunc)

    # Check which checkbox is on
    if removepunc == 'on':
        punctuations =  '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change to UpperCase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        er = """<h1> Error! </h1> <br> <h2> Please! Checkbox to click and get an answer yours</h2>
                 <br> <br> <button><a href="http://127.0.0.1:8000/"> <b> Back </b> </a> </button>"""
        return HttpResponse(er)
