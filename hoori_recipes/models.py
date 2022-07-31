
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)

    instructions = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    cooking_time = models.IntegerField(null=True)

    protein = models.IntegerField(null=True)
    carbs = models.IntegerField(null=True)
    fat = models.IntegerField(null=True)
    servings = models.IntegerField(null=True)


    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


    def save(self, *args, **kwargs):

        now = datetime.datetime.now()
        d_truncated_date = datetime.date(now.year, now.month, now.day)
        d_truncated_time = datetime.time(now.hour, now.minute, now.second)
        self.slug = slugify(
            f'{self.author}-{self.title}-{d_truncated_date}-{d_truncated_time}'
            )
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

        def __str__(self):
            return f"Comment {self.body} by {self.name}"


