from django.http import HttpResponseRedirect


def szukajka(request):
    keyword = request.GET['keyword']
    url = "http://www.google.pl/search?q=" + keyword
    return HttpResponseRedirect(url)

