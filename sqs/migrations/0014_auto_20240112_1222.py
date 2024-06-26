# Generated by Django 3.2.4 on 2024-01-12 04:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sqs', '0013_layerrequestlog_request_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layerrequestlog',
            name='request_type',
            field=models.CharField(choices=[('FULL', 'FULL'), ('PARTIAL', 'PARTIAL'), ('SINGLE', 'SINGLE')], default='FULL', max_length=40),
        ),
        migrations.AlterField(
            model_name='layerrequestlog',
            name='response',
            field=models.JSONField(default=dict, verbose_name='Response from SQS'),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.PositiveIntegerField(verbose_name='Application ID')),
                ('system', models.CharField(max_length=100, verbose_name='System/Application name')),
                ('requester', models.CharField(max_length=100, verbose_name='Prefill Request User')),
                ('script', models.TextField(verbose_name='Script - Dict (script name)')),
                ('data', models.JSONField(verbose_name='Request query from external system')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Task Description')),
                ('parameters', models.TextField(blank=True, null=True, verbose_name='Script Parameters - Dict (script params_list)')),
                ('status', models.CharField(choices=[('failed', 'Failed'), ('created', 'Created'), ('running', 'Running'), ('completed', 'Completed'), ('cancelled', 'Cancelled'), ('error', 'Error')], default='created', max_length=12, verbose_name='Task Status')),
                ('priority', models.PositiveSmallIntegerField(choices=[(1, 'High'), (2, 'Normal'), (3, 'Low')], default=2, verbose_name='Task Priority')),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('stdout', models.TextField(blank=True, null=True)),
                ('stderr', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('request_log', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request_log', to='sqs.layerrequestlog')),
            ],
        ),
    ]
