# Run the migration function via manage.py remote shell (or manage.py shell
# for local development DB)

from datetime import datetime
from blog.models import Blog, Post
from minicms.models import Page
from django.db import models

def migrate_v2():
    # Run this *before* deployment
    Page._meta.get_field('last_update').default = lambda: datetime.now()
    for page in Page.objects.all():
        page.save()

def migrate_v3():
    # Run this quickly before or after deployment
    Blog.add_to_class('base_url', models.CharField('Base URL', max_length=200))
    for blog in Blog.objects.all():
        blog.url = '/blog/' + blog.base_url
        blog.save()

    Post._meta.get_field('last_update').auto_now = False
    for post in Post.objects.all():
        if post.url and post.published_on and '/' not in post.url:
            post.url = post.blog.url_prefix + '%04d/%02d/' % (post.published_on.year, post.published_on.month) + post.url
        post.save()

    Page._meta.get_field('last_update').auto_now = False
    for page in Page.objects.all():
        page.save()