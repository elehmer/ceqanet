# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestupgrade',
            name='user_id',
            field=models.OneToOneField(db_constraint=False, db_column=b'user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
