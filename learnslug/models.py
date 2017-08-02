
class Article(models.Model):
    '''An article with title, date and slug. The slug is not totally
    unique but there will be no two articles with the same slug within
    any month.
    '''
    title = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=50, allow_unicode=False)



from django.db import models
from autoslug import AutoSlugField
class Article(models.Model):
    '''An article with title, date and slug. The slug is not totally
    unique but there will be no two articles with the same slug within
    any month.
    '''
    title = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now_add=True)
    slug = AutoSlugField(
            populate_from='title', 
            unique_with='pub_date__month'
                        )




"""
from learnslug.models import Article, NewsArticle
from mixer.backend.django import mixer

Article.objects.all().delete()
NewsArticle.objects.all().delete()
mixer.cycle(10).blend(Article, title=mixer.sequence(lambda c: "title_%s" % c))
"""


from django.db import models
from autoslug import AutoSlugField
class Article(models.Model):
    '''Custom slugify
    '''
    title = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now_add=True)
    slug = AutoSlugField(
            slugify=custom_slugify,
            populate_from='title', 
            unique_with='pub_date__month'
                        )



from django.utils.text import slugify
import string
from faker import Factory
fake = Factory.create()


try:
    #python 3.6 cryptographic random
    from secrets import choice
except:
    from random import choice

def random_string_generator(
        size=10, 
        chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Create your models here.
from autoslug.settings import slugify as default_slugify
def custom_slugify(value):
    return default_slugify(
        value \
        + " " + fake.name() + " " +\
        random_string_generator(size=3)).replace('-', '_'
        )
    #slug = AutoSlugField(slugify=custom_slugify)



articles = Article.objects.all()
for i in articles:
    print("article.slug1\t{}".format(i.slug))
    i.save()
    print("article.slug2\t{}\n".format(i.slug))