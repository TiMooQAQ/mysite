# Generated by Django 3.1 on 2020-08-17 05:12

from django.db import migrations, models
import django.db.models.deletion
import wangeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, verbose_name='标签')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'db_table': 'Type',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
                ('cookie', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='封面/', verbose_name='封面')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('content', wangeditor.fields.WangRichTextField(verbose_name='内容')),
                ('create_time', models.TimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modify_time', models.TimeField(auto_now=True, verbose_name='修改时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.user', verbose_name='作者')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.type', verbose_name='标签')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'db_table': 'Article',
                'ordering': ['-modify_time'],
            },
        ),
    ]