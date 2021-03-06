# Generated by Django 4.0.2 on 2022-03-09 20:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0005_remove_projetos_created_remove_projetos_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetos',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 3, 9, 20, 22, 16, 610678, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projetos',
            name='description',
            field=models.TextField(default=datetime.datetime(2022, 3, 9, 20, 22, 23, 170897, tzinfo=utc), verbose_name='Descrição'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projetos',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projetos',
            name='id_user_group',
            field=models.CharField(max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projetos',
            name='se_ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='projetos',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
