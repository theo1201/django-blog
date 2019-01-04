from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.utils import timezone

from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(
            status='published')
            
class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'),)

    title = models.CharField(max_length=250)
    # URLs 中使用的字段，slug 是只包含字母、数字、下划线、连字符的短标签。
    # 我们将使用 slug 字段为blog 文章创建漂亮、SEO 友好的 URLs 
    # 们为该字段添加了 unique_for_date 参数，这样我们可以使用date 和 slug 为文章创建标签，设置该参数后将不能为相同日期的多篇文章使用相同的 slug 。
    slug = models.SlugField(max_length=250, unique_for_date='publish')

    # 这个字段定义了一个多对一关系。我们告诉 Django 每篇文章有一个作者而一个作者可以写多篇文章。
    # 使用 related_name 属性为指定反向关系（从 User 到 Post ）的名称，
    # author = models.ForeignKey(User, related_name='blog_posts')
    # _delete=models.CASCADE  主外关系键中，级联删除，也就是当删除主表的数据时候从表中的数据也随着一起删除
#     在实际项目中，我们使用最多的还是related_name
# 如果你觉得上面的定义比较麻烦的话，你也可以在定义主表的外键的时候，给这个外键定义好一个名称。要用related_name比如在Book表中：
#   person = models.ForeignKey(Person, )
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')

    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # 表示文章状态的字段。我们使用 choices 参数，该字段只能为给定的 choices 中的一个。
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='draft')
    objects = models.Manager()
    published = PublishedManager()

    # 模型内部的 Meta 类包含 metadata 。通过它告诉 Django 查询数据库时按照 publish 降序的顺序对查询结果进行排序
    class Meta:
        ordering = ('-publish',)    
    # __str__方法是默认表示对象的方法。Django 将在很多地方使用它，比如 administration 网站。
    def __str__(self):
        return self.title
    # 拼接url地址
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.strftime('%Y'),
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])            

# 评论系统
class Comment(models.Model):
    # Comment 中的这个多对一关系表示评论必须针对某篇文章但是一篇文章可以包含多条评论。post  中的 related_name 属性用于通过文章查看评论，
    # 定义完成后我们可以通过 comment.post 获得文章，通过 post.comments.all() 获得文章的所有评论。
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')

    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #  active 字段来屏蔽某些评论
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)