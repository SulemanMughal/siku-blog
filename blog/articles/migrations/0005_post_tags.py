# Generated by Django 3.1.4 on 2022-03-24 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_post_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, help_text='Keywords for a post', max_length=100, null=True, verbose_name='Tags'),
        ),
    ]
