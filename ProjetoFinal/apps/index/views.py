from django.shortcuts import render
from apps.post.models import Post
from django.core.paginator import Paginator

def pagination(request):
    post_list = Post.objects.all().order_by('date_posted')
    paginator = Paginator(post_list, 3)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    
    return render(request, 'pagination.html', {'posts': posts})
