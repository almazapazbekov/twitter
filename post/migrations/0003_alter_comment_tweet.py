# Generated by Django 3.2 on 2022-12-27 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20221227_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='tweet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.tweet'),
        ),
    ]
