# Generated by Django 2.1.4 on 2019-01-11 10:07

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.IntegerField(null=True)),
                ('description', models.CharField(default='BALANCE', max_length=100)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='date')),
                ('time', models.DateField(default=datetime.time, verbose_name='time')),
            ],
        ),
        migrations.CreateModel(
            name='Debit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit', models.IntegerField(null=True)),
                ('description', models.CharField(default='BALANCE', max_length=100)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='date')),
                ('time', models.DateField(default=datetime.time, verbose_name='time')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(500)])),
                ('date', models.DateField(default=datetime.date.today, verbose_name='date')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(150), django.core.validators.MinValueValidator(0)])),
                ('email', models.CharField(default='enter username', max_length=256, null=True, unique=True, validators=[django.core.validators.EmailValidator])),
                ('password', models.CharField(default='enter password', max_length=6)),
                ('mob', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(max_length=100)),
                ('account_type', models.CharField(choices=[('S', 'SAVINGS_ACCOUNT'), ('C', 'CURRENT_ACCOUNT'), ('F', 'FIXED_DEPOSITE'), ('R', 'RECURRING_DEPOSITE')], max_length=1)),
                ('gender', models.CharField(choices=[('F', 'FEMALE'), ('M', 'MALE')], max_length=1)),
                ('balance', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(500)])),
            ],
        ),
        migrations.AddField(
            model_name='transfer',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='main.User'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='main.User'),
        ),
        migrations.AddField(
            model_name='debit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
        migrations.AddField(
            model_name='credit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
    ]
