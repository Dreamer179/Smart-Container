#  Copyright (C) AI Power - All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by AI Power, January 2020

# Generated by Django 2.2.6 on 2019-11-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('container', '0016_delete_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='containerlog',
            name='inout',
            field=models.IntegerField(choices=[(1, 'In'), (2, 'Out')], default=1),
            preserve_default=False,
        ),
    ]
