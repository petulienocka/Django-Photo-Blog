from django.contrib import admin
from blog.models import Post  #Type

#class TypeAdmin(admin.ModelAdmin):
    #list_display = ["category"]
    #class Meta: 
        #model = Type
  #admin.site.register(Type, TypeAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ["__str__", "time", "updated"]
    list_filter = ["updated"]
    search_fields = ["title"] #"category"
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)

