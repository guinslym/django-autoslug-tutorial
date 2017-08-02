from django.db import models
from autoslug import AutoSlugField


class ArticleWithDjango(models.Model):
    '''
    The slug will not automatically created
    '''
    title = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=50, allow_unicode=False)

    def __repr__(self):
        return "\nid\t:{}\ntitle\t:{}\nslug\t:{}\n".format(self.id, self.title, self.slug)

"""
In [1]: from learndjangoautoslug.models import ArticleWithDjango, ArticleWithDjangoAutoSlug

In [2]: ArticleWithDjango.objects.create(title="Hello world to my pythonistas")
Out[2]:

id      :1
title   :Hello world
slug    :
"""

class ArticleWithDjangoAutoSlug(models.Model):
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

    def __repr__(self):
        return "\nid\t:{}\ntitle\t:{}\nslug\t:{}\n".format(self.id, self.title, self.slug)

"""

In [6]: articlewithdjangoautoslug
Out[6]:

id      :1
title   :hello world to all my pythonistas
slug    :hello-world-to-all-my-pythonistas

"""



from django.utils.text import slugify
import string
from autoslug.settings import slugify as default_slugify
from django.conf import settings

try:
    #python 3.6 cryptographic random
    from secrets import choice
except:
    from random import choice


def random_string_generator(
        size=10, 
        chars=string.ascii_lowercase + string.digits):
    """
    return a random string
    """
    return ''.join(choice(chars) for _ in range(size))

def custom_slugify(value):
    """
    will return hello_world_my_dear_s4lkj
    """
    return default_slugify(
        value \
        + " " + \
        random_string_generator(size=5)).replace('-', '_'
        )

class ArticleWithDjangoAutoSlugCustomSlugify(models.Model):
    '''An article with title, date and slug. The slug was custom made.
    then the same slug may reappear within a day or within some author’s 
    articles but never within a day for the same author. 
    '''
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now_add=True)
    slug = AutoSlugField(
            slugify=custom_slugify,
            populate_from='title', 
            unique_with=('pub_date', 'author'),
                        )

    def __repr__(self):
        return "\nid\t:{}\ntitle\t:{}\nslug\t:{}\n".format(self.id, self.title, self.slug)

"""
In [7]: articlewithdjangoautoslugcustomslugify
Out[7]:

id      :1
title   :hello world to all my pythonistas
slug    :hello_world_to_all_my_pythonistas_g0ub6

"""









"""

from learndjangoautoslug.models import ArticleWithDjango
from learndjangoautoslug.models import ArticleWithDjangoAutoSlug
from learndjangoautoslug.models import ArticleWithDjangoAutoSlugCustomSlugify
from django.contrib.auth.models import User


articlewithdjango = ArticleWithDjango.objects.create(title="hello world to all my pythonistas")
articlewithdjangoautoslug = ArticleWithDjangoAutoSlug.objects.create(title="hello world to all my pythonistas")

user=User.objects.create_user('foo', password='bar')
user.save()
articlewithdjangoautoslugcustomslugify = ArticleWithDjangoAutoSlugCustomSlugify.objects.create(title="hello world to all my pythonistas", author=user)

articlewithdjango
articlewithdjangoautoslug
articlewithdjangoautoslugcustomslugfy

"""

"""
In [5]: articlewithdjango
Out[5]:

id      :1
title   :hello world to all my pythonistas
slug    :


In [6]: articlewithdjangoautoslug
Out[6]:

id      :1
title   :hello world to all my pythonistas
slug    :hello-world-to-all-my-pythonistas

In [7]: articlewithdjangoautoslugcustomslugify
Out[7]:

id      :1
title   :hello world to all my pythonistas
slug    :hello_world_to_all_my_pythonistas_g0ub6
"""

