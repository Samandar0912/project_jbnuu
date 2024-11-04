# Generated by Django 5.1.2 on 2024-11-04 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_post_site_elon'),
    ]

    operations = [
        migrations.CreateModel(
            name='FastLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Sayt nomi')),
                ('photo', models.ImageField(upload_to='media/Foydali_Sayt_rasmi/')),
                ('href', models.CharField(max_length=100, verbose_name='Sayt linki')),
            ],
            options={
                'verbose_name': 'Tezkor havolalar',
                'verbose_name_plural': 'Tezkor havolalar',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='MySites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Sayt nomi')),
                ('photo', models.ImageField(upload_to='media/Foydali_Sayt_rasmi/')),
                ('href', models.CharField(max_length=100, verbose_name='Sayt linki')),
            ],
            options={
                'verbose_name': 'Bizni Tizimlar',
                'verbose_name_plural': 'Bizni Tizimlar',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Statistika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name="Ko'rsatgichlar nomi")),
                ('number', models.IntegerField(verbose_name="Ko'rsatgichlar qiymati")),
            ],
            options={
                'verbose_name': "Asosiy Ko'rsatgichlar",
                'verbose_name_plural': "Asosiy Ko'rsatgichlar",
            },
        ),
        migrations.CreateModel(
            name='UsefulSites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Sayt nomi')),
                ('photo', models.ImageField(upload_to='media/Foydali_Sayt_rasmi/')),
                ('href', models.CharField(max_length=100, verbose_name='Sayt linki')),
            ],
            options={
                'verbose_name': 'Foydali saytlar',
                'verbose_name_plural': 'Foydali saytlar',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterModelOptions(
            name='category_facultet',
            options={'verbose_name': 'Categorya', 'verbose_name_plural': 'Categoryalar'},
        ),
        migrations.AlterModelOptions(
            name='post_site_elon',
            options={'ordering': ['-id'], 'verbose_name': "E'lon", 'verbose_name_plural': 'Elonlar'},
        ),
        migrations.AlterModelOptions(
            name='post_site_news',
            options={'ordering': ['-id'], 'verbose_name': 'Yangilik', 'verbose_name_plural': 'Yangiliklar'},
        ),
    ]