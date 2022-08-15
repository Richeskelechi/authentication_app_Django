# Generated by Django 4.0.6 on 2022-08-08 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('librarys', '0003_librarypage_library_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentreaction',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentreaction',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='commentreaction',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarys.librarypage'),
        ),
    ]