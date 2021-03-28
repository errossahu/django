from django.shortcuts import render

posts = [
    {
        'author':'Yohanes Erros Sahu',
        'title':'Blog Post 1' , 
        'content': 'First post content', 
        'date_posted': 'Augest 25 2021', 
    },
    {
        'author':'Jhon Doe 2',
        'title':'Blog Post 1' , 
        'content': 'First post content', 
        'date_posted': 'Augest 25 2021', 
    },
]
def home(request):
    context = {
        'post': posts,  
    }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html', {'title':'About'})   

