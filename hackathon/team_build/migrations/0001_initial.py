# Generated by Django 3.2.5 on 2021-07-31 10:36

from django.db import migrations, models
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(default='', max_length=200)),
                ('title', models.CharField(default='', max_length=300)),
                ('team_name', models.CharField(default='', max_length=200)),
                ('service', models.CharField(default='', max_length=200)),
                ('team_members', models.CharField(blank=True, choices=[('1', '1명'), ('2', '2명'), ('3', '3명'), ('4', '4명'), ('5', '5명 이상')], default='1', max_length=10)),
                ('service_level', models.CharField(blank=True, choices=[('0', '아이디어 구상 단계'), ('1', '초기 개발 단계'), ('2', '프로토타입 완성 단계'), ('3', '배포 및 상용화 단계'), ('4', '서비스 확장 단계')], default='0', max_length=10)),
                ('founding_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('locate', models.CharField(blank=True, choices=[('', '미정'), ('서울', '서울특별시'), ('부산', '부산광역시'), ('인천', '인천광역시'), ('대구', '대구광역시'), ('광주', '광주광역시'), ('대전', '대전광역시'), ('울산', '울산광역시'), ('세종', '세종시'), ('경기', '경기도'), ('강원', '강원도'), ('충남', '충청남도'), ('충북', '충청북도'), ('경북', '경상북도'), ('경남', '경상남도'), ('전북', '전라북도'), ('전남', '전라남도'), ('제주', '제주도')], default='', max_length=2)),
                ('image', models.ImageField(blank=True, default='', upload_to='')),
                ('role', multiselectfield.db.fields.MultiSelectField(choices=[('Developer', '개발자'), ('Designer', '디자이너'), ('Planner', '기획자'), ('Editor', '편집자')], default='', max_length=100)),
                ('detail', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
