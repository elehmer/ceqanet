# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    replaces = [(b'app', '0001_initial'), (b'app', '0002_auto_20161015_0546'), (b'app', '0003_auto_20161015_0632'), (b'app', '0004_auto_20161015_0635'), (b'app', '0005_auto_20161015_0636'), (b'app', '0006_auto_20161015_0637'), (b'app', '0007_auto_20161015_0637'), (b'app', '0008_auto_20161015_0638'), (b'app', '0009_auto_20161015_0639'), (b'app', '0010_auto_20161015_0640'), (b'app', '0011_auto_20161016_2203'), (b'app', '0012_auto_20161016_2207'), (b'app', '0013_auto_20161016_2230'), (b'app', '0014_auto_20161016_2246'), (b'app', '0015_auto_20161016_2257'), (b'app', '0016_auto_20161016_2258'), (b'app', '0017_auto_20161016_2300'), (b'app', '0018_auto_20161016_2301'), (b'app', '0019_auto_20161016_2302'), (b'app', '0020_auto_20161016_2304'), (b'app', '0021_auto_20161016_2305'), (b'app', '0022_auto_20161016_2306'), (b'app', '0023_auto_20161016_2306'), (b'app', '0024_auto_20161016_2307'), (b'app', '0025_auto_20161016_2308'), (b'app', '0026_auto_20161017_2029')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='clearinghouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('schnoprefix', models.CharField(max_length=6)),
                ('currentid', models.IntegerField()),
                ('biayear', models.CharField(max_length=4)),
                ('biaid', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Clearinghouse',
                'verbose_name_plural': 'Clearing House Relate?',
            },
        ),
        migrations.CreateModel(
            name='counties',
            fields=[
                ('geow_pk', models.AutoField(serialize=False, primary_key=True)),
                ('geow_shortname', models.CharField(max_length=32)),
                ('geow_longname', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'County',
                'verbose_name_plural': 'Counties',
            },
        ),
        migrations.CreateModel(
            name='docattachments',
            fields=[
                ('datt_pk', models.AutoField(serialize=False, primary_key=True)),
                ('datt_file', models.FileField(null=True, upload_to=b'documents/%Y/%m/%d', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='doccomments',
            fields=[
                ('dcom_pk', models.AutoField(serialize=False, primary_key=True)),
                ('dcom_commentdate', models.DateField(null=True, blank=True)),
                ('dcom_textcomment', models.TextField(null=True, blank=True)),
                ('dcom_filecomment', models.FileField(null=True, upload_to=b'documents/%Y/%m/%d', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='docgeowords',
            fields=[
                ('dgeo_pk', models.AutoField(serialize=False, primary_key=True)),
                ('dgeo_rank', models.IntegerField()),
                ('dgeo_comment', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='dockeywords',
            fields=[
                ('dkey_pk', models.AutoField(serialize=False, primary_key=True)),
                ('dkey_comment', models.CharField(max_length=64, null=True, blank=True)),
                ('dkey_value1', models.CharField(max_length=16, null=True, blank=True)),
                ('dkey_value2', models.CharField(max_length=16, null=True, blank=True)),
                ('dkey_value3', models.CharField(max_length=16, null=True, blank=True)),
                ('dkey_rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='docreviews',
            fields=[
                ('drag_pk', models.AutoField(serialize=False, primary_key=True)),
                ('drag_comment', models.CharField(max_length=64, null=True, blank=True)),
                ('drag_received', models.DateField(null=True, blank=True)),
                ('drag_sentbysch', models.NullBooleanField()),
                ('drag_sentbylag', models.NullBooleanField()),
                ('drag_late', models.NullBooleanField()),
                ('drag_rank', models.IntegerField()),
                ('drag_copies', models.IntegerField()),
                ('sentbycode', models.CharField(max_length=1, null=True, blank=True)),
                ('dsnum', models.CharField(max_length=10, null=True, blank=True)),
                ('dscode', models.CharField(max_length=5, null=True, blank=True)),
                ('dsloc', models.CharField(max_length=30, null=True, blank=True)),
                ('drag_lateletter', models.DateField(null=True, blank=True)),
                ('drag_numcomments', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='doctypes',
            fields=[
                ('keyw_pk', models.AutoField(serialize=False, primary_key=True)),
                ('keyw_shortname', models.CharField(max_length=32)),
                ('keyw_longname', models.CharField(max_length=64)),
                ('inlookup', models.BooleanField(default=True)),
                ('storfed', models.IntegerField()),
                ('ordinal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='documents',
            fields=[
                ('doc_pk', models.AutoField(serialize=False, primary_key=True)),
                ('doc_schno', models.CharField(db_index=True, max_length=12, null=True, blank=True)),
                ('doc_doctype', models.CharField(max_length=32, null=True, blank=True)),
                ('doc_docname', models.CharField(max_length=64, null=True, blank=True)),
                ('doc_title', models.TextField(null=True, blank=True)),
                ('doc_description', models.TextField(null=True, blank=True)),
                ('doc_comments', models.CharField(max_length=64, null=True, blank=True)),
                ('doc_conname', models.CharField(max_length=64, null=True, verbose_name=b'Contact Name:', blank=True)),
                ('doc_conagency', models.CharField(max_length=64, null=True, blank=True)),
                ('doc_conphone', models.CharField(max_length=32, null=True, blank=True)),
                ('doc_conemail', models.EmailField(max_length=64, null=True, blank=True)),
                ('doc_confax', models.CharField(max_length=32, null=True, blank=True)),
                ('doc_conaddress1', models.CharField(max_length=64, null=True, blank=True)),
                ('doc_conaddress2', models.CharField(max_length=64, null=True, blank=True)),
                ('doc_concity', models.CharField(max_length=32, null=True, blank=True)),
                ('doc_constate', models.CharField(max_length=2, null=True, blank=True)),
                ('doc_conzip', models.CharField(max_length=10, null=True, blank=True)),
                ('doc_county', models.CharField(max_length=64, null=True, verbose_name=b'County:', blank=True)),
                ('doc_city', models.CharField(max_length=64, null=True, verbose_name=b'CityL', blank=True)),
                ('doc_region', models.TextField(null=True, verbose_name=b'Region:', blank=True)),
                ('doc_location', models.TextField(null=True, verbose_name=b'Other Location Info:', blank=True)),
                ('doc_notes', models.TextField(null=True, blank=True)),
                ('doc_jobs', models.IntegerField(null=True, blank=True)),
                ('doc_xstreets', models.CharField(max_length=96, null=True, verbose_name=b'Cross Streets:', blank=True)),
                ('doc_zipcode', models.CharField(max_length=10, null=True, blank=True)),
                ('doc_acres', models.CharField(max_length=16, null=True, blank=True)),
                ('doc_parcelno', models.CharField(max_length=96, null=True, verbose_name=b'Parcel No:', blank=True)),
                ('doc_township', models.CharField(max_length=6, null=True, verbose_name=b'Township:', blank=True)),
                ('doc_range', models.CharField(max_length=6, null=True, verbose_name=b'Range:', blank=True)),
                ('doc_section', models.CharField(max_length=6, null=True, verbose_name=b'Section:', blank=True)),
                ('doc_base', models.CharField(max_length=8, null=True, verbose_name=b'Base:', blank=True)),
                ('doc_highways', models.CharField(max_length=32, null=True, blank=True)),
                ('doc_airports', models.CharField(max_length=32, null=True, blank=True)),
                ('doc_railways', models.CharField(max_length=32, null=True, blank=True)),
                ('doc_waterways', models.CharField(max_length=96, null=True, blank=True)),
                ('doc_schools', models.CharField(max_length=64, null=True, blank=True)),
                ('doc_doctypenotes', models.CharField(max_length=32, null=True, blank=True)),
                ('doc_actionnotes', models.CharField(max_length=32, null=True, blank=True)),
                ('doc_devnotes', models.CharField(max_length=32, null=True, blank=True)),
                ('doc_issuesnotes', models.CharField(max_length=32, null=True, blank=True)),
                ('doc_landuse', models.TextField(null=True, blank=True)),
                ('doc_analyst', models.CharField(max_length=5, null=True, blank=True)),
                ('doc_received', models.DateField(null=True, blank=True)),
                ('doc_dept', models.DateField(null=True, blank=True)),
                ('doc_agency', models.DateField(null=True, blank=True)),
                ('doc_signed', models.DateField(null=True, blank=True)),
                ('doc_clear', models.DateField(null=True, blank=True)),
                ('doc_final', models.DateField(null=True, blank=True)),
                ('doc_nod', models.DateField(null=True, blank=True)),
                ('doc_detsigeffect', models.BooleanField()),
                ('doc_detnotsigeffect', models.BooleanField()),
                ('doc_deteir', models.BooleanField()),
                ('doc_detnegdec', models.BooleanField()),
                ('doc_detmitigation', models.BooleanField()),
                ('doc_detnotmitigation', models.BooleanField()),
                ('doc_detconsider', models.BooleanField()),
                ('doc_detnotconsider', models.BooleanField()),
                ('doc_detfindings', models.BooleanField()),
                ('doc_detnotfindings', models.BooleanField()),
                ('doc_eiravailableat', models.TextField(null=True, blank=True)),
                ('doc_exministerial', models.BooleanField()),
                ('doc_exdeclared', models.BooleanField()),
                ('doc_exemergency', models.BooleanField()),
                ('doc_excategorical', models.BooleanField()),
                ('doc_exstatutory', models.BooleanField()),
                ('doc_exnumber', models.CharField(max_length=32, null=True, blank=True)),
                ('doc_exreasons', models.TextField(null=True, verbose_name=b'Reasons why project is exempt:', blank=True)),
                ('doc_srrreasons', models.TextField(null=True, blank=True)),
                ('doc_ssragencies', models.TextField(null=True, blank=True)),
                ('doc_ssrdays', models.IntegerField(null=True, blank=True)),
                ('doc_ssrapproved', models.DateField(null=True, blank=True)),
                ('doc_prncomment', models.DateField(null=True, blank=True)),
                ('doc_prnnocomment', models.DateField(null=True, blank=True)),
                ('doc_prnlatecomment', models.DateField(null=True, blank=True)),
                ('doc_prnearlyconsult', models.DateField(null=True, blank=True)),
                ('doc_prnnopletter', models.DateField(null=True, blank=True)),
                ('doc_prnacknowledgement', models.DateField(null=True, blank=True)),
                ('doc_letternote', models.TextField(null=True, blank=True)),
                ('doc_updated', models.TextField(null=True, blank=True)),
                ('doc_nodbylead', models.BooleanField()),
                ('doc_nodbyresp', models.BooleanField()),
                ('doc_nodagency', models.CharField(max_length=64, null=True, blank=True)),
                ('doc_tribeinfo', models.CharField(max_length=64, null=True, blank=True)),
                ('doc_lat_deg', models.CharField(max_length=12, null=True, blank=True)),
                ('doc_lat_min', models.CharField(max_length=10, null=True, blank=True)),
                ('doc_lat_sec', models.CharField(max_length=10, null=True, blank=True)),
                ('doc_long_deg', models.CharField(max_length=12, null=True, blank=True)),
                ('doc_long_min', models.CharField(max_length=10, null=True, blank=True)),
                ('doc_long_sec', models.CharField(max_length=10, null=True, blank=True)),
                ('doc_pending', models.BooleanField()),
                ('doc_visible', models.BooleanField()),
                ('doc_review', models.BooleanField()),
                ('doc_plannerregion', models.IntegerField(null=True, blank=True)),
                ('doc_plannerreview', models.BooleanField()),
                ('doc_exstatus', models.IntegerField()),
                ('doc_added', models.DateField(null=True, blank=True)),
                ('doc_draft', models.BooleanField()),
                ('doc_clerknotes', models.TextField(null=True, blank=True)),
                ('doc_approve_noe', models.CharField(max_length=64, null=True, blank=True)),
                ('doc_carryout_noe', models.CharField(max_length=64, null=True, blank=True)),
                ('doc_nodfeespaid', models.BooleanField()),
                ('doc_bia', models.BooleanField()),
                ('doc_statewide', models.BooleanField()),
                ('doc_added_userid', models.ForeignKey(related_name='+', db_column=b'doc_added_userid', db_constraint=False, to=settings.AUTH_USER_MODEL)),
                ('doc_assigned_userid', models.ForeignKey(related_name='+', db_column=b'doc_assigned_userid', db_constraint=False, to=settings.AUTH_USER_MODEL)),
                ('doc_cnty_fk', models.ForeignKey(db_constraint=False, db_column=b'doc_cnty_fk', blank=True, to='app.counties', null=True)),
                ('doc_doct_fk', models.ForeignKey(db_constraint=False, db_column=b'doc_doct_fk', blank=True, to='app.doctypes', null=True)),
                ('doc_lastlooked_userid', models.ForeignKey(related_name='+', db_column=b'doc_lastlooked_userid', db_constraint=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
        ),
        migrations.CreateModel(
            name='geowordlists',
            fields=[
                ('geol_pk', models.AutoField(serialize=False, primary_key=True)),
                ('geol_shortname', models.CharField(max_length=32, null=True, blank=True)),
                ('geol_longname', models.CharField(max_length=64, null=True, blank=True)),
                ('geol_description', models.TextField(null=True, blank=True)),
                ('geol_listsource', models.CharField(max_length=10, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='geowords',
            fields=[
                ('geow_pk', models.AutoField(serialize=False, primary_key=True)),
                ('geow_shortname', models.CharField(max_length=32, db_index=True)),
                ('geow_longname', models.CharField(max_length=64)),
                ('geow_description', models.TextField()),
                ('geow_originalcontrolid', models.CharField(max_length=10)),
                ('geow_recordsource', models.CharField(max_length=10)),
                ('inlookup', models.BooleanField(default=True)),
                ('geow_geol_fk', models.ForeignKey(to='app.geowordlists', db_column=b'geow_geol_fk', db_constraint=False)),
                ('geow_parent_fk', models.ForeignKey(to='app.geowords', db_column=b'geow_parent_fk', db_constraint=False)),
            ],
            options={
                'verbose_name': 'Geoword',
                'verbose_name_plural': 'Geowords',
            },
        ),
        migrations.CreateModel(
            name='holidays',
            fields=[
                ('hday_pk', models.AutoField(serialize=False, primary_key=True)),
                ('hday_name', models.CharField(max_length=40)),
                ('hday_date', models.DateField()),
                ('hday_dow', models.CharField(max_length=10)),
                ('hday_note', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='keywordlists',
            fields=[
                ('keyl_pk', models.AutoField(serialize=False, primary_key=True)),
                ('keyl_shortname', models.CharField(max_length=32)),
                ('keyl_longname', models.CharField(max_length=64)),
                ('keyl_description', models.TextField()),
                ('keyl_listsource', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='keywords',
            fields=[
                ('keyw_pk', models.AutoField(serialize=False, primary_key=True)),
                ('keyw_shortname', models.CharField(max_length=32)),
                ('keyw_longname', models.CharField(max_length=64)),
                ('keyw_description', models.TextField()),
                ('keyw_caption1', models.CharField(max_length=10)),
                ('keyw_caption2', models.CharField(max_length=10)),
                ('keyw_caption3', models.CharField(max_length=10)),
                ('keyw_originalcontrolid', models.CharField(max_length=10)),
                ('keyw_recordsource', models.CharField(max_length=10)),
                ('keyw_keyl_fk', models.ForeignKey(to='app.keywordlists', db_column=b'keyw_keyl_fk', db_constraint=False)),
            ],
            options={
                'verbose_name': 'Keyword',
                'verbose_name_plural': 'Keywords',
            },
        ),
        migrations.CreateModel(
            name='latlongs',
            fields=[
                ('doc_pk', models.AutoField(serialize=False, primary_key=True)),
                ('doc_schno', models.CharField(max_length=12, null=True, blank=True)),
                ('doc_doctype', models.CharField(max_length=32)),
                ('doc_lat_deg', models.CharField(max_length=12, null=True, blank=True)),
                ('doc_lat_min', models.CharField(max_length=10, null=True, blank=True)),
                ('doc_lat_sec', models.CharField(max_length=10, null=True, blank=True)),
                ('doc_long_deg', models.CharField(max_length=12, null=True, blank=True)),
                ('doc_long_min', models.CharField(max_length=10, null=True, blank=True)),
                ('doc_long_sec', models.CharField(max_length=10, null=True, blank=True)),
                ('doc_latitude', models.CharField(max_length=30, null=True, blank=True)),
                ('doc_longitude', models.CharField(max_length=30, null=True, blank=True)),
                ('doc_map_link', models.CharField(max_length=240, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='leadagencies',
            fields=[
                ('lag_pk', models.AutoField(serialize=False, primary_key=True)),
                ('lag_domain', models.CharField(max_length=20)),
                ('lag_name', models.CharField(max_length=90, db_index=True)),
                ('lag_title', models.CharField(max_length=90)),
                ('lag_address1', models.CharField(max_length=50)),
                ('lag_address2', models.CharField(max_length=50)),
                ('lag_city', models.CharField(max_length=30)),
                ('lag_county', models.CharField(max_length=20)),
                ('lag_state', models.CharField(max_length=2)),
                ('lag_zip', models.CharField(max_length=10)),
                ('lag_phone', models.CharField(max_length=30)),
                ('lag_fax', models.CharField(max_length=30)),
                ('lag_sch_no', models.CharField(max_length=10)),
                ('lag_updated', models.DateField()),
                ('lag_acronym', models.CharField(max_length=10)),
                ('lag_disable', models.BooleanField()),
                ('lag_prjcnt', models.IntegerField()),
                ('lag_note', models.CharField(max_length=60)),
                ('inlookup', models.BooleanField(default=True)),
                ('lag_geow_fk', models.ForeignKey(to='app.geowords', db_column=b'lag_geow_fk', db_constraint=False)),
            ],
            options={
                'verbose_name': 'Lead Agency',
                'verbose_name_plural': 'Lead Agencies',
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('geom', django.contrib.gis.db.models.fields.GeometryCollectionField(srid=4326)),
                ('document', models.ForeignKey(to='app.documents', db_column=b'doc_pk', db_constraint=False)),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('prj_pk', models.AutoField(serialize=False, primary_key=True)),
                ('prj_schno', models.CharField(max_length=12, null=True, blank=True)),
                ('prj_title', models.CharField(max_length=160, null=True, blank=True)),
                ('prj_comments', models.TextField(null=True, blank=True)),
                ('prj_status', models.CharField(max_length=32, null=True, blank=True)),
                ('prj_description', models.TextField(null=True, blank=True)),
                ('prj_datefirst', models.DateField(null=True, blank=True)),
                ('prj_datelast', models.DateField(null=True, blank=True)),
                ('prj_analyst', models.CharField(max_length=5, null=True, blank=True)),
                ('prj_leadagency', models.CharField(max_length=90, null=True, blank=True)),
                ('prj_otheragency', models.CharField(max_length=90, null=True, blank=True)),
                ('prj_otheraddress1', models.CharField(max_length=90, null=True, blank=True)),
                ('prj_otheraddress2', models.CharField(max_length=90, null=True, blank=True)),
                ('prj_othercity', models.CharField(max_length=30, null=True, blank=True)),
                ('prj_othercounty', models.CharField(max_length=20, null=True, blank=True)),
                ('prj_otherstate', models.CharField(max_length=2, null=True, blank=True)),
                ('prj_otherzip', models.CharField(max_length=10, null=True, blank=True)),
                ('prj_otherphone', models.CharField(max_length=20, null=True, blank=True)),
                ('prj_updated', models.DateField(null=True, blank=True)),
                ('prj_pending', models.BooleanField()),
                ('prj_visible', models.BooleanField()),
                ('prj_plannerreview', models.NullBooleanField()),
                ('prj_applicant', models.CharField(max_length=64, null=True, blank=True)),
                ('prj_doc_fk', models.ForeignKey(to='app.documents', db_column=b'prj_doc_fk', db_constraint=False)),
                ('prj_lag_fk', models.ForeignKey(to='app.leadagencies', db_column=b'prj_lag_fk', db_constraint=False)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='requestupgrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rqst_pending', models.NullBooleanField()),
                ('rqst_type', models.CharField(max_length=10, null=True, blank=True)),
                ('rqst_reason', models.TextField(null=True, blank=True)),
                ('rqst_lag_fk', models.ForeignKey(db_constraint=False, db_column=b'rqst_lag_fk', blank=True, to='app.leadagencies', null=True)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
        migrations.CreateModel(
            name='reviewingagencies',
            fields=[
                ('rag_pk', models.AutoField(serialize=False, primary_key=True)),
                ('rag_name', models.CharField(max_length=90, db_index=True)),
                ('rag_title', models.CharField(max_length=90, null=True, blank=True)),
                ('rag_subtitle', models.CharField(max_length=50, null=True, blank=True)),
                ('rag_address1', models.CharField(max_length=50, null=True, blank=True)),
                ('rag_address2', models.CharField(max_length=50, null=True, blank=True)),
                ('rag_city', models.CharField(max_length=25, null=True, blank=True)),
                ('rag_county', models.CharField(max_length=16, null=True, blank=True)),
                ('rag_state', models.CharField(max_length=2, null=True, blank=True)),
                ('rag_zip', models.CharField(max_length=10, null=True, blank=True)),
                ('rag_phone', models.CharField(max_length=30, null=True, blank=True)),
                ('rag_copies', models.IntegerField(null=True)),
                ('rag_rank', models.IntegerField(null=True)),
                ('rag_default', models.NullBooleanField()),
                ('rag_acronym', models.CharField(max_length=10, null=True)),
                ('rag_disable', models.NullBooleanField()),
                ('inlookup', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Reviewing Agency',
                'verbose_name_plural': 'Reviewing Agencies',
            },
        ),
        migrations.AddField(
            model_name='requestupgrade',
            name='rqst_rag_fk',
            field=models.ForeignKey(db_constraint=False, db_column=b'rqst_rag_fk', blank=True, to='app.reviewingagencies', null=True),
        ),
        migrations.AddField(
            model_name='requestupgrade',
            name='user_id',
            field=models.ForeignKey(db_constraint=False, db_column=b'user_id', to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AddField(
            model_name='latlongs',
            name='doc_prj_fk',
            field=models.ForeignKey(to='app.projects', db_column=b'doc_prj_fk', db_constraint=False),
        ),
        migrations.AddField(
            model_name='documents',
            name='doc_prj_fk',
            field=models.ForeignKey(db_constraint=False, db_column=b'doc_prj_fk', blank=True, to='app.projects', null=True),
        ),
        migrations.AddField(
            model_name='docreviews',
            name='drag_doc_fk',
            field=models.ForeignKey(to='app.documents', db_column=b'drag_doc_fk', db_constraint=False),
        ),
        migrations.AddField(
            model_name='docreviews',
            name='drag_rag_fk',
            field=models.ForeignKey(to='app.reviewingagencies', db_column=b'drag_rag_fk', db_constraint=False),
        ),
        migrations.AddField(
            model_name='dockeywords',
            name='dkey_doc_fk',
            field=models.ForeignKey(to='app.documents', db_column=b'dkey_doc_fk', db_constraint=False),
        ),
        migrations.AddField(
            model_name='dockeywords',
            name='dkey_keyw_fk',
            field=models.ForeignKey(to='app.keywords', db_column=b'dkey_keyw_fk', db_constraint=False),
        ),
        migrations.AddField(
            model_name='docgeowords',
            name='dgeo_doc_fk',
            field=models.ForeignKey(to='app.documents', db_column=b'dgeo_doc_fk', db_constraint=False),
        ),
        migrations.AddField(
            model_name='docgeowords',
            name='dgeo_geow_fk',
            field=models.ForeignKey(to='app.geowords', db_column=b'dgeo_geow_fk', db_constraint=False),
        ),
        migrations.AddField(
            model_name='doccomments',
            name='dcom_doc_fk',
            field=models.ForeignKey(to='app.documents', db_column=b'dcom_doc_fk', db_constraint=False),
        ),
        migrations.AddField(
            model_name='doccomments',
            name='dcom_drag_fk',
            field=models.ForeignKey(to='app.docreviews', db_column=b'dcom_drag_fk', db_constraint=False),
        ),
        migrations.AddField(
            model_name='doccomments',
            name='dcom_reviewer_userid',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'dcom_reviewer_userid', db_constraint=False),
        ),
        migrations.AddField(
            model_name='docattachments',
            name='datt_doc_fk',
            field=models.ForeignKey(to='app.documents', db_column=b'datt_doc_fk', db_constraint=False),
        ),
        migrations.AlterField(
            model_name='doctypes',
            name='ordinal',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_exstatus',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_nodfeespaid',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_bia',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_statewide',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_plannerreview',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_draft',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_nodbylead',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='documents',
            name='doc_nodbyresp',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='geowords',
            name='geow_parent_fk',
            field=models.ForeignKey(db_constraint=False, db_column=b'geow_parent_fk', to='app.geowords', null=True),
        ),
        migrations.AlterField(
            model_name='geowords',
            name='geow_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='leadagencies',
            name='lag_sch_no',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
