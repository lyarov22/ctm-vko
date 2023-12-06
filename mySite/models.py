from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя категории(рус)')
    name2 = models.CharField(max_length=200, db_index=True, default='', verbose_name='Санат атауы(каз)')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Ссылка')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория / Санат'
        verbose_name_plural = 'Категории / Санаттар'

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория / Санат')
    title = models.CharField(max_length=200, verbose_name='Заголовок (рус)')
    title2 = models.CharField(max_length=200, default='', verbose_name='Тақырып (каз)')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='post/%Y/%m/%d', blank=True, verbose_name='Главное фото / Негізгі сурет')
    content = models.TextField(verbose_name='Текст(рус)')
    content2 = models.TextField(default='', verbose_name='Текст (каз)')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации / Жарияланған күні')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления / Жаңарту күні')

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

        verbose_name = 'Новость / Жаңалықтар'
        verbose_name_plural = 'Новости / Жаңалықтар'

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post/%Y/%m/%d/', verbose_name='Дополнительное фото / Қосымша фотосурет')

    def __str__(self):
        return f"{self.post.title} Image"
    
    class Meta:
        verbose_name = 'Изображение / Сурет'
        verbose_name_plural = 'Изображения / Суреттер'


class PostLink(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='links')
    url = models.URLField(verbose_name='Ссылки')
    text = models.CharField(max_length=200, verbose_name='Текст(рус)')
    text2 = models.CharField(max_length=200, verbose_name='Текст(каз)')

    def __str__(self):
        return f"{self.post.title} - {self.text}"
    
    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'