# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20161018_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docattachments',
            name='datt_doc_fk',
            field=models.ForeignKey(to='app.documents', db_column=b'datt_doc_fk'),
        ),
        migrations.AlterField(
            model_name='doccomments',
            name='dcom_doc_fk',
            field=models.ForeignKey(to='app.documents', db_column=b'dcom_doc_fk'),
        ),
        migrations.AlterField(
            model_name='doccomments',
            name='dcom_drag_fk',
            field=models.ForeignKey(to='app.docreviews', db_column=b'dcom_drag_fk'),
        ),
        migrations.AlterField(
            model_name='doccomments',
            name='dcom_reviewer_userid',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'dcom_reviewer_userid'),
        ),
        migrations.AlterField(
            model_name='docgeowords',
            name='dgeo_doc_fk',
            field=models.ForeignKey(to='app.documents', db_column=b'dgeo_doc_fk'),
        ),
        migrations.AlterField(
            model_name='docgeowords',
            name='dgeo_geow_fk',
            field=models.ForeignKey(to='app.geowords', db_column=b'dgeo_geow_fk'),
        ),
        migrations.AlterField(
            model_name='dockeywords',
            name='dkey_doc_fk',
            field=models.ForeignKey(to='app.documents', db_column=b'dkey_doc_fk'),
        ),
        migrations.AlterField(
            model_name='dockeywords',
            name='dkey_keyw_fk',
            field=models.ForeignKey(to='app.keywords', db_column=b'dkey_keyw_fk'),
        ),
        migrations.AlterField(
            model_name='docreviews',
            name='drag_doc_fk',
            field=models.ForeignKey(to='app.documents', db_column=b'drag_doc_fk'),
        ),
        migrations.AlterField(
            model_name='docreviews',
            name='drag_rag_fk',
            field=models.ForeignKey(to='app.reviewingagencies', db_column=b'drag_rag_fk'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_added_userid',
            field=models.ForeignKey(related_name='+', db_column=b'doc_added_userid', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_assigned_userid',
            field=models.ForeignKey(related_name='+', db_column=b'doc_assigned_userid', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_cnty_fk',
            field=models.ForeignKey(db_column=b'doc_cnty_fk', blank=True, to='app.counties', null=True),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_doct_fk',
            field=models.ForeignKey(db_column=b'doc_doct_fk', blank=True, to='app.doctypes', null=True),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_lastlooked_userid',
            field=models.ForeignKey(related_name='+', db_column=b'doc_lastlooked_userid', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_prj_fk',
            field=models.ForeignKey(db_column=b'doc_prj_fk', blank=True, to='app.projects', null=True),
        ),
        migrations.AlterField(
            model_name='geowords',
            name='geow_geol_fk',
            field=models.ForeignKey(to='app.geowordlists', db_column=b'geow_geol_fk'),
        ),
        migrations.AlterField(
            model_name='geowords',
            name='geow_parent_fk',
            field=models.ForeignKey(db_column=b'geow_parent_fk', to='app.geowords', null=True),
        ),
        migrations.AlterField(
            model_name='keywords',
            name='keyw_keyl_fk',
            field=models.ForeignKey(to='app.keywordlists', db_column=b'keyw_keyl_fk'),
        ),
        migrations.AlterField(
            model_name='latlongs',
            name='doc_prj_fk',
            field=models.ForeignKey(to='app.projects', db_column=b'doc_prj_fk'),
        ),
        migrations.AlterField(
            model_name='leadagencies',
            name='lag_geow_fk',
            field=models.ForeignKey(to='app.geowords', db_column=b'lag_geow_fk'),
        ),
        migrations.AlterField(
            model_name='locations',
            name='document',
            field=models.ForeignKey(to='app.documents', db_column=b'doc_pk'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='prj_doc_fk',
            field=models.ForeignKey(to='app.documents', db_column=b'prj_doc_fk'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='prj_lag_fk',
            field=models.ForeignKey(to='app.leadagencies', db_column=b'prj_lag_fk'),
        ),
        migrations.AlterField(
            model_name='requestupgrade',
            name='rqst_lag_fk',
            field=models.ForeignKey(db_column=b'rqst_lag_fk', blank=True, to='app.leadagencies', null=True),
        ),
        migrations.AlterField(
            model_name='requestupgrade',
            name='rqst_rag_fk',
            field=models.ForeignKey(db_column=b'rqst_rag_fk', blank=True, to='app.reviewingagencies', null=True),
        ),
        migrations.AlterField(
            model_name='requestupgrade',
            name='user_id',
            field=models.OneToOneField(db_column=b'user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='set_lag_fk',
            field=models.ForeignKey(db_column=b'set_lag_fk', blank=True, to='app.leadagencies', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='set_rag_fk',
            field=models.ForeignKey(db_column=b'set_rag_fk', blank=True, to='app.reviewingagencies', null=True),
        ),
    ]
