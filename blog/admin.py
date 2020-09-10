from django.contrib import admin
from .models import Article,Category,Writer

class CategoryAdmin(admin.ModelAdmin):
    list_display=('position','title','slug','status')
    list_filter=(['status'])
    search_fields=('title','slug')
    prepopulated_fields={'slug':('title',)}

admin.site.register(Category,CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','slug','jpublish','status','category_to_str','Writer_to_str')
    list_filter=('publish','status')
    search_fields=('title','description')
    prepopulated_fields={'slug':('title',)}
    ordering=['publish']

    def category_to_str(self,obj):
        return  " , ".join([category.title for category in obj.category.all()])
    category_to_str.short_description="دسته بندی"

    def Writer_to_str(self,obj):
        return  " , ".join([writer.name for writer in obj.writer.all()])
    Writer_to_str.short_description="نویسنده"
admin.site.register(Article,ArticleAdmin)



class WriterAdmin(admin.ModelAdmin):
    list_display=('name','lastname','position')
    search_fields=('name','lastname')
    
admin.site.register(Writer,WriterAdmin)




