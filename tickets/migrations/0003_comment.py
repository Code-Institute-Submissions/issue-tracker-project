# Generated by Django 3.0.8 on 2020-07-12 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20200711_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=60)),
                ('comment_text', models.TextField()),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tickets.Ticket')),
            ],
        ),
    ]