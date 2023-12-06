from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Category, Post, PostImage, PostLink

admin.site.site_header = "Публикация новостей"
admin.site.site_title = "Панель администратора"
admin.site.index_title = "Публикация новостей"

admin.site.site_icon = 'img/favicon.png'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class PostImageInline(admin.TabularInline):
    model = PostImage

class PostLinkInline(admin.TabularInline):
    model = PostLink
    extra = 2  # Количество дополнительных полей для заполнения

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_date', 'updated')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PostImageInline, PostLinkInline] 

    #ordering = ('name',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj is None:  # Если объект еще не сохранен в базе данных (т.е. создается новый пост)
            return []
        else:
            return ['pub_date', 'updated']  # В противном случае скрываем только поле updated

admin.site.register(Category, CategoryAdmin)
admin.site.register(PostImage)
admin.site.register(PostLink)

admin.site.unregister(PostImage)
admin.site.unregister(PostLink)

admin.site.unregister(User)
admin.site.unregister(Group)