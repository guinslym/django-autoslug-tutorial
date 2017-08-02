# Django Autoslug tutorial


### Creating some models
please see the models.py file
```python
class ArticleWithDjango(models.Model):
    '''
    The slug will not automatically created
    '''
    title = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=50, allow_unicode=False)

    def __repr__(self):
        return "\nid\t:{}\ntitle\t:{}\nslug\t:{}\n".format(self.id, self.title, self.slug)

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
```

```python
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
```


Output

```shell
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
```