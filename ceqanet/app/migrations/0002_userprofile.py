# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_squashed_0026_auto_20161017_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('conphone', models.CharField(max_length=32, null=True, blank=True)),
                ('set_lag_fk', models.ForeignKey(db_constraint=False, db_column=b'set_lag_fk', blank=True, to='app.leadagencies', null=True)),
                ('set_rag_fk', models.ForeignKey(db_constraint=False, db_column=b'set_rag_fk', blank=True, to='app.reviewingagencies', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
