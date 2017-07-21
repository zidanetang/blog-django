from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post, Category, Tag
#from django import forms

class PostAdmin(admin.ModelAdmin):
    #content = forms.CharField(widget=CKEditorWidget())
    list_display = ['title', 'created_time', 'category', 'author', ]
    ordering = ['-created_time']

    #class Meta:
     #   model = Post

    def __unicode__(self):
        return '%s' % self.title


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', ]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)



# Register your models here.
