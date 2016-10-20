# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20161018_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='doc_detconsider',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_deteir',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_detfindings',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_detmitigation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_detnegdec',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_detnotconsider',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_detnotfindings',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_detnotmitigation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_detnotsigeffect',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_detsigeffect',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_excategorical',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_exdeclared',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_exemergency',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_exministerial',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_exstatutory',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_pending',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_review',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_visible',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='leadagencies',
            name='lag_disable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='projects',
            name='prj_pending',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='projects',
            name='prj_visible',
            field=models.BooleanField(default=False),
        ),
    ]
