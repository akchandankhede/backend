# Generated by Django 3.1.2 on 2020-10-21 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kenmark', models.SlugField(default='', editable=False, max_length=6)),
                ('text', models.CharField(max_length=1000)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('coordinates', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, choices=[('m', 'Gemeld'), ('i', 'In afwachting van behandeling'), ('h', 'On hold'), ('o', 'Afgehandeld'), ('s', 'Gesplitst'), ('reopened', 'Heropend'), ('b', 'In behandeling'), ('ingepland', 'Ingepland'), ('ready to send', 'Te verzenden naar extern systeem'), ('a', 'Geannuleerd'), ('closure requested', 'Verzoek tot afhandeling'), ('sent', 'Verzonden naar extern systeem'), ('send failed', 'Verzending naar extern systeem mislukt'), ('done external', 'Melding is afgehandeld in extern systeem'), ('reopen requested', 'Verzoek tot heropenen')], default='m', max_length=20)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('file', models.FileField(blank=True, max_length=255, null=True, upload_to='attachments/%Y/%m/%d/')),
                ('file1', models.FileField(blank=True, null=True, upload_to='attachments/%Y/%m/%d/')),
                ('file2', models.FileField(blank=True, null=True, upload_to='attachments/%Y/%m/%d/')),
                ('file3', models.FileField(blank=True, null=True, upload_to='attachments/%Y/%m/%d/')),
                ('priority', models.CharField(choices=[('low', 'Low'), ('normal', 'Normal'), ('high', 'High')], default='normal', max_length=255)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
