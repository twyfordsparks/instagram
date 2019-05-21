from django.db import models
from django.contrib.auth.models import User
# from tinymice.models import HTMLField

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    caption = models.TextField(max_length =120)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def search_by_user(cls,search_term):
        users = cls.objects.filter(title__icontains=search_term)
        return users

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Comment(models.Model):
    image = models.ForeignKey(Image, blank=True, on_delete=models.CASCADE, related_name='comment')
    commenter = models.ForeignKey(User, blank=True)
    comment_itself = models.TextField()

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments_on_image(cls, id):
        the_comments = Comment.objects.filter(image__pk=id)
        return the_comments

    def __str__(self):
        return self.comment_itself
