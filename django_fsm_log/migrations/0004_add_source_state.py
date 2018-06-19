# Generated by Django 2.1.1 on 2018-09-08 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_fsm_log', '0003_statelog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='statelog',
            name='source_state',
            field=models.CharField(blank=True, db_index=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='statelog',
            name='state',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Target state'),
        ),
    ]
