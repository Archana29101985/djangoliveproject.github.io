# Generated by Django 2.0 on 2019-03-05 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0005_remove_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favorite_genre',
            field=models.CharField(choices=[('Action', 'action'), ('Comedy', 'comedy'), ('Romance', 'romance'), ('Thriller', 'thriller'), ('Horror', 'Horror')], default='Comedy', max_length=100),
        ),
    ]