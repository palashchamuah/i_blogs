from django.contrib import admin

from .models import Category, Post, Contact

# Register your models here.


#configuration of category at admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url', 'add_date',)
    search_fields = ('title','add_date',)

#configuration of Post at admin

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title','content','url',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 10


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Contact)
