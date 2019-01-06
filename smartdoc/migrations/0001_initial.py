# Generated by Django 2.1.5 on 2019-01-06 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smartdoc.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('mod_date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='文档类型名')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '文档分类',
                'ordering': ['-mod_date'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('mod_date', models.DateField(auto_now=True)),
                ('title', models.TextField(max_length=30, verbose_name='文件名')),
                ('version_no', models.IntegerField(blank=True, default=1, verbose_name='版本编号')),
                ('doc_file', models.FileField(blank=True, null=True, upload_to=smartdoc.models.user_directory_path, verbose_name='文件上传')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='smartdoc.Category', verbose_name='分类')),
            ],
            options={
                'verbose_name': '文档',
                'ordering': ['-mod_date'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('mod_date', models.DateField(auto_now=True)),
                ('name', models.TextField(max_length=30, verbose_name='产品名')),
                ('code', models.TextField(blank=True, default='', max_length=30, verbose_name='产品编码')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '产品',
                'ordering': ['-mod_date'],
            },
        ),
        migrations.AddField(
            model_name='document',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='smartdoc.Product', verbose_name='产品'),
        ),
    ]
