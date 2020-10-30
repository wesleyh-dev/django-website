from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Post

# Create your views here.
def indexView(request): 
    posts = Post.objects.all()

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
        
    template = 'blog/index.html'
    context = {
        'page_obj': page_obj,
    }

    return render(
        request, 
        template,
        context,
    )

    ########### TODO: Add search functionality #############

def detailView(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    template = 'blog/detail.html'
    context = {
        'post': post
    }

    return render(
        request,
        template,
        context
    )
