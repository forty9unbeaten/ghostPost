# Generated by Django 3.0.6 on 2020-05-15 02:05

from django.db import migrations, models
import django.utils.timezone
import ghost_post.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_roast', models.BooleanField()),
                ('content', models.CharField(max_length=280)),
                ('up_votes', models.IntegerField(default=0)),
                ('down_votes', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('secret_id', models.CharField(default=ghost_post.utils.generate_secret_id, max_length=6)),
            ],
        ),
    ]
