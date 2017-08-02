# Django Autoslug tutorial

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