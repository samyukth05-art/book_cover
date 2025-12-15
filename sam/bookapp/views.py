from django.shortcuts import render

def book_func(request):
    return render(request, 'bookcover.html')

