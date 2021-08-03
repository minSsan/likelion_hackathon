# Generated by Django 3.2.5 on 2021-08-03 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team_build', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeRecruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=200)),
                ('recruit_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team_build.recruit')),
            ],
        ),
    ]
