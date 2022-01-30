from django.db import models
from django.utils.html import format_html
# Create your models here.
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    description = models.TextField()
    url = models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'catogery/')
    #add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title
    
    def imgtagcat(self):
        return format_html("<img src='/media/{}' style = 'width:40px; height : 40px;'>".format(self.img))


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)

    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    img = models.ImageField(upload_to = 'post/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.CharField(max_length=50,null=True)
    
    
    def __str__(self):
        return self.title
    def imgtagpost(self):
        return format_html("<img src='/media/{}' style = 'width:40px; height : 40px;'>".format(self.img))
    
    
class PostComments(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    comments = models.TextField()
    
    
class register(models.Model):
    username = models.CharField(max_length = 50)
    email = models.EmailField()
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    password = models.CharField(max_length = 32)
    confirm_password = models.CharField(max_length = 32)