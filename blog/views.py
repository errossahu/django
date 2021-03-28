from django.shortcuts import render

posts = [
    {
        'author':'Yohanes Erros Sahu',
    }
]
def home(request):
    return render(request, 'blog/home.html')
def about(request):
    return render(request, 'blog/about.html')   

