from django.db import models
from wangeditor.fields import WangRichTextField


# Create your models here.
class Type(models.Model):
    type = models.CharField(max_length=20,verbose_name='标签')

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'Type'
        verbose_name = '标签'
        verbose_name_plural = verbose_name

class User(models.Model):
    username = models.CharField( max_length=10,verbose_name='用户名',unique=True)
    password = models.CharField(max_length=255,verbose_name='密码')
    cookie = models.CharField(max_length=30,null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'User'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

class Article(models.Model):
    cover = models.ImageField(verbose_name='封面',upload_to='封面/%Y%m%d',null=True,blank=True)
    title = models.CharField(max_length=20,verbose_name='标题')
    content = WangRichTextField(verbose_name='内容')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,verbose_name='作者')
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING,verbose_name='标签')
    create_time = models.TimeField(auto_now_add=True,verbose_name='创建时间')
    modify_time = models.TimeField(auto_now=True,verbose_name='修改时间')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-modify_time']
        db_table = 'Article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name
