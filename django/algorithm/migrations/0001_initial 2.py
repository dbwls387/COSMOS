# Generated by Django 3.1.5 on 2023-03-31 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adjective',
            fields=[
                ('adjective_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('contents', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'adjective',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('end_date', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_category', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.CharField(blank=True, max_length=255, null=True)),
                ('orders', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Courseplace',
            fields=[
                ('course_place_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('orders', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'courseplace',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GugunCode',
            fields=[
                ('code', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'gugun_code',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('couple_id', models.BigIntegerField(blank=True, null=True)),
                ('image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('created_time', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'image',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Noun',
            fields=[
                ('noun_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('contents', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'noun',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('dtype', models.CharField(max_length=31)),
                ('place_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('detail', models.CharField(blank=True, max_length=255, null=True)),
                ('img1', models.CharField(blank=True, max_length=255, null=True)),
                ('img2', models.CharField(blank=True, max_length=255, null=True)),
                ('img3', models.CharField(blank=True, max_length=255, null=True)),
                ('img4', models.CharField(blank=True, max_length=255, null=True)),
                ('img5', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('parking_yn', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('thumb_nail_url', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('acceptable_people', models.CharField(blank=True, max_length=255, null=True)),
                ('bbq_yn', models.CharField(blank=True, max_length=255, null=True)),
                ('check_in', models.CharField(blank=True, max_length=255, null=True)),
                ('check_out', models.CharField(blank=True, max_length=255, null=True)),
                ('cook_yn', models.CharField(blank=True, max_length=255, null=True)),
                ('gym_yn', models.CharField(blank=True, max_length=255, null=True)),
                ('karaoke_yn', models.CharField(blank=True, max_length=255, null=True)),
                ('pickup_yn', models.CharField(blank=True, max_length=255, null=True)),
                ('refund', models.CharField(blank=True, max_length=255, null=True)),
                ('reservation_page', models.CharField(blank=True, max_length=255, null=True)),
                ('room_num', models.CharField(blank=True, max_length=255, null=True)),
                ('room_type', models.CharField(blank=True, max_length=255, null=True)),
                ('card_yn', models.CharField(blank=True, max_length=255, null=True)),
                ('day_off', models.CharField(blank=True, max_length=255, null=True)),
                ('open_time', models.CharField(blank=True, max_length=255, null=True)),
                ('playground', models.CharField(blank=True, max_length=255, null=True)),
                ('representative_menu', models.CharField(blank=True, max_length=255, null=True)),
                ('reserve_info', models.CharField(blank=True, max_length=255, null=True)),
                ('smoking_yn', models.CharField(blank=True, max_length=255, null=True)),
                ('takeout_yn', models.CharField(blank=True, max_length=255, null=True)),
                ('total_menu', models.CharField(blank=True, max_length=255, null=True)),
                ('pet_yn', models.CharField(blank=True, max_length=255, null=True)),
                ('end_date', models.CharField(blank=True, max_length=255, null=True)),
                ('introduce', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.CharField(blank=True, max_length=255, null=True)),
                ('taken_time', models.CharField(blank=True, max_length=255, null=True)),
                ('age_range', models.CharField(blank=True, max_length=255, null=True)),
                ('open_period', models.CharField(blank=True, max_length=255, null=True)),
                ('parking_cost', models.CharField(blank=True, max_length=255, null=True)),
                ('open_day', models.CharField(blank=True, max_length=255, null=True)),
                ('shopping_list', models.CharField(blank=True, max_length=255, null=True)),
                ('stroller_yn', models.CharField(blank=True, max_length=255, null=True)),
                ('inside_yn', models.CharField(blank=True, max_length=255, null=True)),
                ('program', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'place',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('plan_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('end_date', models.CharField(blank=True, max_length=255, null=True)),
                ('main_category', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.CharField(blank=True, max_length=255, null=True)),
                ('couple_id', models.BigIntegerField(blank=True, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('plan_name', models.CharField(blank=True, max_length=255, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'plan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RefreshToken',
            fields=[
                ('refresh_token_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('refresh_token', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'refresh_token',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('contents', models.CharField(blank=True, max_length=255, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'review',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reviewcategory',
            fields=[
                ('review_category_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('review_category_code', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'reviewcategory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reviewplace',
            fields=[
                ('review_place_id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'reviewplace',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SidoCode',
            fields=[
                ('code', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'sido_code',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_seq', models.BigAutoField(primary_key=True, serialize=False)),
                ('age_range', models.CharField(blank=True, max_length=255, null=True)),
                ('birthday', models.CharField(blank=True, max_length=255, null=True)),
                ('couple_id', models.BigIntegerField(blank=True, null=True)),
                ('couple_yn', models.CharField(blank=True, max_length=255, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_img_url', models.CharField(blank=True, max_length=255, null=True)),
                ('role', models.CharField(blank=True, max_length=255, null=True)),
                ('type1', models.CharField(blank=True, max_length=255, null=True)),
                ('type2', models.CharField(blank=True, max_length=255, null=True)),
                ('user_id', models.CharField(blank=True, max_length=255, null=True)),
                ('user_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Userplace',
            fields=[
                ('user_place_id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'userplace',
                'managed': False,
            },
        ),
    ]