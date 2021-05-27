from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post



def post_list(request):
    # template = loader.get_template('blog/post_list.html')
    # context = {
    # }
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
    # return HttpResponse(template.render(context, request))

def uikit(request):
    template = loader.get_template('blog/uikit.html')
    context = {
    }
    return HttpResponse(template.render(context, request))