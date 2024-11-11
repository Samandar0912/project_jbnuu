# Generated by Django 5.1.2 on 2024-11-06 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_fastlinks_mysites_statistika_usefulsites_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniverHistoryCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Sarlovhasi')),
                ('body', models.TextField(verbose_name='texti')),
                ('photo', models.ImageField(upload_to='media/photo/', verbose_name='rasm')),
                ('yil', models.CharField(max_length=9, verbose_name='yilni kiriting')),
            ],
            options={
                'verbose_name': 'Foydali saytlar',
                'verbose_name_plural': 'Foydali saytlar',
            },
        ),
    ]