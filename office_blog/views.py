from django.shortcuts import render, render_to_response, get_object_or_404
from office_blog.models import Tag, Category, Post
from django.utils.text import slugify
from django.views.generic import ListView
#from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from markdown.extensions.toc import TocExtension
import markdown


'''
#页面分页函数
def pageing(request,post_list,per_num=1):
    paginator = Paginator(post_list, per_num)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return post_list
'''


# 利用django通用视图主页视图
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    #切片的单位数
    paginate_by = 1

    def get_queryset(self):
        return Post.objects.order_by('-created_time')

'''
#主页视图
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    #每页显示的数量
    per_num = 1
    post_list = pageing(request,post_list,per_num)
    return render(request, 'blog/index.html', context={'post_list': post_list})
'''



#文章详情视图
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    md = markdown.Markdown(extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      TocExtension(slugify=slugify),
                                  ])
    post.body = md.convert(post.body)
    return render(request, 'blog/detail.html', context={'post': post,'toc': md.toc})


#利用django通用视图归档视图
class ArchivesViews(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    #切片的单位数
    paginate_by = 10

    def get_queryset(self):
        self.year = self.kwargs['year']
        self.month = self.kwargs['month']
        return Post.objects.filter(created_time__year=self.year, created_time__month=self.month).order_by('-created_time')

'''
#归档视图
def archives(request,year,month):
    post_list = Post.objects.all().filter(created_time__year=year,created_time__month=month).order_by('-created_time')
    #每页显示的数量
    per_num = 10
    post_list = pageing(request,post_list,per_num)
    return render(request, 'blog/index.html', context={'post_list': post_list})
'''


class CategoryViews(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 10

    def get_queryset(self):
        self.cate = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Post.objects.filter(category=self.cate).order_by('-created_time')

'''
#分类视图
def category(request,pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    #每页显示的数量
    per_num = 10
    post_list = pageing(request,post_list,per_num)
    return render(request, 'blog/index.html', context={'post_list': post_list})
'''


#标签视图
def tag(request,pk):
    ta = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=ta).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


#搜索视图
def search(request):
    input_keword = request.GET.get('search')
    error_msg = ''
    if not input_keword:
        error_msg = u'请输入要搜索的关键字'
        return render(request,'blog/error.html',context={'error_msg':error_msg})
    post_list = Post.objects.filter(title__icontains=input_keword)
    return render(request,'blog/result.html',context={'post_list':post_list,'error_msg':error_msg})
# Create your views here.
