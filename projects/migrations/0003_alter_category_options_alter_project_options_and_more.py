# Generated by Django 5.0.2 on 2024-05-13 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'التصنيف', 'verbose_name_plural': 'التصنيف'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'المشروع', 'verbose_name_plural': 'المشروع'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'المهمة', 'verbose_name_plural': 'المهمة'},
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(choices=[(1, 'قيد التنفيذ'), (2, 'مكتمل'), (3, 'معلق'), (4, 'ملغي')], default=1),
        ),
    ]
