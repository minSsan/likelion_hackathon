# Generated by Django 3.2.5 on 2021-08-12 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('team_build', '0008_alter_recruit_locate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_username',
        ),
        migrations.RemoveField(
            model_name='commentanswer',
            name='user_username',
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='commentanswer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
