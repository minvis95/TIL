from django.db import models

# Create your models here.
# models모듈의 Model 클레스를 상속 받아. 즉 프레임워크 이용해
class Article(models.Model):
    # PK는 알아서 작성된다.
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# article = Article()
# article.title = ''
# article.content = ''
# article.save()

# article = Article(title='', content='')
# article.save()

# Article.objects.create(title='', content='')
