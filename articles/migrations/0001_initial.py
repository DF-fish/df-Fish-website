# Generated by Django 3.0.6 on 2020-05-18 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('published_date', models.DateTimeField(blank=True)),
                ('jupyter_playground', models.FileField(upload_to='')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('type', models.CharField(choices=[('T', 'Tutorial'), ('S', 'Story')], default='T', max_length=1)),
            ],
        ),
    ]
