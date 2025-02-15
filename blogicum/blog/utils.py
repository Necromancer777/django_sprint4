from django.utils import timezone
from .models import Post


def post_filter():
    return Post.objects.filter(pub_date__lt=timezone.now(), is_published=True,
                               category__is_published=True)
