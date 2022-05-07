from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

# Create your views here.
class PostListView(ListView):       #Class based views
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog_app/post/list.html'

# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 3) # 3 posts in each page
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)
#     context = {'page': page, 'posts': posts}
#     return render(request,'blog_app/post/list.html', context)

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day) 
    context = {'post': post}
    return render(request, 'blog_app/post/detail.html', context)   