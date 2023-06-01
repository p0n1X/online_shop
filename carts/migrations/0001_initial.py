# Generated by Django 4.2 on 2023-06-01 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('token', models.CharField(blank=True, max_length=256, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.product')),
            ],
        ),
    ]