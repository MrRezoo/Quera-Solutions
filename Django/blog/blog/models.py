from django.db import models


# TODO write all of your code here...
class Author(models.Model):
    name = models.CharField(max_length=50)


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def copy(self):
        new_post = BlogPost(title=self.title, body=self.body, author=self.author)
        new_post.save()
        for comment in self.comment_set.values('text'):
            Comment(**comment, blog_post=new_post).save()
        return new_post.id


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
