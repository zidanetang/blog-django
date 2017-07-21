from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


#类别
class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name=u'类别')

    def __str__(self):
        return '%s' % self.name


#标签
class Tag(models.Model):
    name = models.CharField(max_length=100,verbose_name=u'标签')

    def __str__(self):
        return '%s' % self.name


#博客文章
@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name=u'文章标题')
    #body = models.TextField(verbose_name=u'文章内容')
    #body = RichTextField(u'文章内容')
    body = RichTextUploadingField(u'文章内容')
    created_time = models.DateField(verbose_name=u'创建日期',auto_now_add=True)
    excerpt = models.CharField(max_length=200, blank=True,verbose_name=u'简介')
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    views = models.PositiveIntegerField(default=0,verbose_name=u'阅读量')

#文章阅读量函数
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('office_blog:detail', kwargs={'pk': self.pk})

    #重写save函数，用于获取博客内容的前60个字符作为简介保存
    def save(self,*args,**kwargs):
        self.excerpt = self.body[:60]
        super(Post, self).save(*args,**kwargs)

# Create your models here.
