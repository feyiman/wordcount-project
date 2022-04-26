# In order to generate a webpage, we need a http response
from operator import itemgetter
from django.http import HttpResponse
# In order to allow access to HTML files, use render
from django.shortcuts import render
import re
import string


def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']

    worddictionary = {}
    # To eliminate all punctuation marks, we use the regex function
    wordlist = re.sub('['+string.punctuation+']', ' ', fulltext).split()

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    # worddictionary.item returns a list which can be sorted thus:
    Sortedwords = sorted(worddictionary.items(),
                         key=itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'Sortedwords': Sortedwords})
