# This page is written by Parth

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def read_file(request):
    f = open('C:/Users/parth/PycharmProjects/textutils/textutils/textutils/1.txt', 'r')
    text = f.read()
    f.close()
    return HttpResponse(text)


def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    removeline = request.GET.get('removeline', 'off')
    removespace = request.GET.get('removespace', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_`~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if removeline == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Remove The Extra Line', 'analyzed_text': analyzed}
        djtext = analyzed

    if removespace == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Remove The Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed

    if (removepunc!="on" and fullcaps!="on" and removeline!="on" and removespace!="on"):
        return HttpResponse(djtext)

    return render(request, 'analyze.html', params)







