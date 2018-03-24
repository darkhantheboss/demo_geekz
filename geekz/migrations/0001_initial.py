# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pair',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=16, verbose_name=b'\xd0\xa1\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe')),
                ('synonym', models.CharField(max_length=16, verbose_name=b'\xd0\xa1\xd0\xb8\xd0\xbd\xd0\xbe\xd0\xbd\xd0\xb8\xd0\xbc')),
            ],
            options={
                'verbose_name': '\u041f\u0430\u0440\u0430',
                'verbose_name_plural': '\u041f\u0430\u0440\u044b \u0441\u043b\u043e\u0432',
            },
        ),
    ]
