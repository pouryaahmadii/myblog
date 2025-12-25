from django.shortcuts import render, HttpResponse

def user_list(request):
    return render(request, 'account/user_list.html')

# Create your views here.
