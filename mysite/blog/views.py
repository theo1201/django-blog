from django.shortcuts import render,get_object_or_404
from .models import Post

# 类视图
from django.views.generic import ListView

# 引入分页
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# 该文件实现应用逻辑。每个 view 接收一个 HTTP请求，对其进行处理并返回一个响应。

# Create your views here.
# def post_list(request):
#     posts = Post.published.all()
#     return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='published',
                             publish__year=year, publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})

def post_list(request):
    object_list = Post.published.all()
    # 使用每页想要显示的文章数量创建 Paginator 实例；
    paginator = Paginator(object_list, 3)  # 3 post in each page
    # 从 request 的 GET 参数中获取请求的页码；
    page = request.GET.get('page')
    # 如果得到的页码不是整数，则取第一页的文章进行展示，如果得到的页码大于最大分页数，那么取最后一页的文章进行展示。
    try:
        # 从 Paginator 的 page() 方法获取文章列表的 queryset ，并设为posts；
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
        # 使用模板渲染步骤 2 中的 page 和步骤 3 中的 posts ，返回 httpResponse。
    return render(request, 'blog/post/list.html',
                  {'page': page, 'posts': posts})

# 视图是一个输入 web请求输出 web响应的函数，我们也可以使用类方法定义视图。Django 提供视图类，这些视图类解决了 HTTP 匹配和其它功能。

class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'