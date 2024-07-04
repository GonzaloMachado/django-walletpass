# Generated by Django 3.2.14 on 2023-07-09 18:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_walletpass.storage


class Migration(migrations.Migration):

    dependencies = [
        ('django_walletpass', '0008_alter_pass_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='log',
            name='device_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='msg',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='pass_type_identifier',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='pazz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='django_walletpass.pass'),
        ),
        migrations.AddField(
            model_name='log',
            name='serial_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='task_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='web_service_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pass',
            name='data',
            field=models.FileField(storage=django_walletpass.storage.WalletPassStorage(), upload_to='passes'),
        ),
    ]