# Generated by Django 3.1.6 on 2021-02-05 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallary_app', '0002_auto_20210205_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='id',
        ),
        migrations.AddField(
            model_name='image',
            name='image_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='category_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='gallary_app.imagecategory'),
        ),
        migrations.AlterField(
            model_name='imagecategory',
            name='category',
            field=models.CharField(default='Other', max_length=200),
        ),
    ]
