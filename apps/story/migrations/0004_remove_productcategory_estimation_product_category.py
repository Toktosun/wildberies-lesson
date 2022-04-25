# Generated by Django 4.0.3 on 2022-04-11 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_alter_productcategory_estimation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='estimation',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='story.productcategory'),
        ),
    ]
