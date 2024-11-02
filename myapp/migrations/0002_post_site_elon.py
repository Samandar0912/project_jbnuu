# Generated by Django 5.1.2 on 2024-11-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='post_site_elon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name="E'lon sarlovhasi")),
                ('body', models.TextField(verbose_name="E'lon tanasi")),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Kiritilgan sanasi')),
                ('photo', models.ImageField(upload_to='media/elon_photo/')),
            ],
        ),
    ]