class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.RunSQL(
            sql='ALTER TABLE hotels ADD COLUMN IF NOT EXISTS description TEXT;',
            reverse_sql='ALTER TABLE hotels DROP COLUMN IF EXISTS description;'
        ),
        migrations.CreateModel(
            name='PropertySummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('property_id', models.IntegerField()),
            ],
            options={
                'db_table': 'property_summaries',
            },
        ),
        migrations.CreateModel(
            name='PropertyReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('review', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('property_id', models.IntegerField()),
            ],
            options={
                'db_table': 'property_reviews',
            },
        ),
    ]