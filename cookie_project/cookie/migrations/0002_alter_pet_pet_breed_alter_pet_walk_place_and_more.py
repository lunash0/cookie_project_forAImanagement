# Generated by Django 4.0 on 2023-08-20 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='PET_BREED',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookie.breed'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='WALK_PLACE',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookie.walk'),
        ),
        migrations.AlterField(
            model_name='skininfo',
            name='PET_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cookie.pet'),
        ),
        migrations.AlterField(
            model_name='user',
            name='PET_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookie.pet', unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='USER_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cookie.accounts'),
        ),
    ]
