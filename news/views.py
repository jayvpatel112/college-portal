from django.shortcuts import render, HttpResponse
from news.models import Post

# Create your views here.
def newsHome(request):
    allPosts = Post.objects.all()
    # print(allPosts)
    context = {'allPosts': allPosts}

    return render(request, 'news/newsHome.html', context)
    

def newsPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "news/newsPost.html", context)
