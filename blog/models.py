from django.db import models
from django.utils.html import format_html


# Category Model

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    #displaying catergory names in admin(earlier showing as object)
    def __str__(self):
        return self.title

    #for displaying image in admin
    def image_tag(self):
        return format_html('<img src="/media/{}"  style="width:40px; height:40px; border-radius: 50px; "/>'.format(self.image))

#Post Model
class Post(models.Model):
    post_id = models.AutoField(primary_key =True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    # displaying catergory names in admin(earlier showing as object)
    def __str__(self):
        return self.title

    # for displaying image in admin
    def image_tag(self):
        return format_html('<img src="/media/{}"  style="width:40px; height:40px; border-radius: 50px; "/>'.format(self.image))


class Contact(models.Model):
    id = models.AutoField(primary_key =True)
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    subject = models.CharField(max_length=200, blank=False, null=False)
    message = models.TextField(blank=False, null=False)

    def __str__(self):
        return f'{self.name} - {self.subject}'