# Generated by Django 3.1.7 on 2021-03-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0004_user_mood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='style',
        ),
        migrations.AddField(
            model_name='user',
            name='style1',
            field=models.CharField(choices=[('', ''), ('acoustic', 'Acoustic'), ('afrobeat', 'Afrobeat'), ('ambient', 'Ambient'), ('anime', 'Anime'), ('blues', 'Blues'), ('chill', 'Chill'), ('classical', 'Classical'), ('club', 'Club'), ('country', 'Country'), ('dance', 'Dance'), ('disco', 'Disco'), ('disney', 'Disney'), ('dubstep', 'Dubstep'), ('edm', 'Edm'), ('electro', 'Electro'), ('electronic', 'Electronic'), ('emo', 'Emo'), ('french', 'French'), ('funk', 'Funk'), ('groove', 'Groove'), ('guitar', 'Guitar'), ('happy', 'Happy'), ('hard-rock', 'Hard-rock'), ('hardcore', 'Hardcore'), ('heavy-metal', 'Heavy-metal'), ('hip-hop', 'Hip-hop'), ('holidays', 'Holidays'), ('house', 'House'), ('j-pop', 'J-pop'), ('jazz', 'Jazz'), ('k-pop', 'K-pop'), ('kids', 'Kids'), ('latin', 'Latin'), ('latino', 'Latino'), ('metal', 'Metal'), ('movies', 'Movies'), ('new-release', 'New-release'), ('opera', 'Opera'), ('party', 'Party'), ('piano', 'Piano'), ('pop', 'Pop'), ('rainy-day', 'Rainy-day'), ('reggaeton', 'Reggaeton'), ('road-trip', 'Road-trip'), ('rock', 'Rock'), ('rock-n-roll', 'Rock-n-roll'), ('romance', 'Romance'), ('sad', 'Sad'), ('salsa', 'Salsa'), ('samba', 'Samba'), ('sleep', 'Sleep'), ('spanish', 'Spanish'), ('study', 'Study'), ('summer', 'Summer'), ('techno', 'Techno'), ('work-out', 'Work-out'), ('world-music', 'World-music')], default=('', ''), max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='style2',
            field=models.CharField(choices=[('', ''), ('acoustic', 'Acoustic'), ('afrobeat', 'Afrobeat'), ('ambient', 'Ambient'), ('anime', 'Anime'), ('blues', 'Blues'), ('chill', 'Chill'), ('classical', 'Classical'), ('club', 'Club'), ('country', 'Country'), ('dance', 'Dance'), ('disco', 'Disco'), ('disney', 'Disney'), ('dubstep', 'Dubstep'), ('edm', 'Edm'), ('electro', 'Electro'), ('electronic', 'Electronic'), ('emo', 'Emo'), ('french', 'French'), ('funk', 'Funk'), ('groove', 'Groove'), ('guitar', 'Guitar'), ('happy', 'Happy'), ('hard-rock', 'Hard-rock'), ('hardcore', 'Hardcore'), ('heavy-metal', 'Heavy-metal'), ('hip-hop', 'Hip-hop'), ('holidays', 'Holidays'), ('house', 'House'), ('j-pop', 'J-pop'), ('jazz', 'Jazz'), ('k-pop', 'K-pop'), ('kids', 'Kids'), ('latin', 'Latin'), ('latino', 'Latino'), ('metal', 'Metal'), ('movies', 'Movies'), ('new-release', 'New-release'), ('opera', 'Opera'), ('party', 'Party'), ('piano', 'Piano'), ('pop', 'Pop'), ('rainy-day', 'Rainy-day'), ('reggaeton', 'Reggaeton'), ('road-trip', 'Road-trip'), ('rock', 'Rock'), ('rock-n-roll', 'Rock-n-roll'), ('romance', 'Romance'), ('sad', 'Sad'), ('salsa', 'Salsa'), ('samba', 'Samba'), ('sleep', 'Sleep'), ('spanish', 'Spanish'), ('study', 'Study'), ('summer', 'Summer'), ('techno', 'Techno'), ('work-out', 'Work-out'), ('world-music', 'World-music')], default=('', ''), max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='style3',
            field=models.CharField(choices=[('', ''), ('acoustic', 'Acoustic'), ('afrobeat', 'Afrobeat'), ('ambient', 'Ambient'), ('anime', 'Anime'), ('blues', 'Blues'), ('chill', 'Chill'), ('classical', 'Classical'), ('club', 'Club'), ('country', 'Country'), ('dance', 'Dance'), ('disco', 'Disco'), ('disney', 'Disney'), ('dubstep', 'Dubstep'), ('edm', 'Edm'), ('electro', 'Electro'), ('electronic', 'Electronic'), ('emo', 'Emo'), ('french', 'French'), ('funk', 'Funk'), ('groove', 'Groove'), ('guitar', 'Guitar'), ('happy', 'Happy'), ('hard-rock', 'Hard-rock'), ('hardcore', 'Hardcore'), ('heavy-metal', 'Heavy-metal'), ('hip-hop', 'Hip-hop'), ('holidays', 'Holidays'), ('house', 'House'), ('j-pop', 'J-pop'), ('jazz', 'Jazz'), ('k-pop', 'K-pop'), ('kids', 'Kids'), ('latin', 'Latin'), ('latino', 'Latino'), ('metal', 'Metal'), ('movies', 'Movies'), ('new-release', 'New-release'), ('opera', 'Opera'), ('party', 'Party'), ('piano', 'Piano'), ('pop', 'Pop'), ('rainy-day', 'Rainy-day'), ('reggaeton', 'Reggaeton'), ('road-trip', 'Road-trip'), ('rock', 'Rock'), ('rock-n-roll', 'Rock-n-roll'), ('romance', 'Romance'), ('sad', 'Sad'), ('salsa', 'Salsa'), ('samba', 'Samba'), ('sleep', 'Sleep'), ('spanish', 'Spanish'), ('study', 'Study'), ('summer', 'Summer'), ('techno', 'Techno'), ('work-out', 'Work-out'), ('world-music', 'World-music')], default=('', ''), max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='mood',
            field=models.FloatField(choices=[(0.3, 'Turn Up'), (0.5, 'Chill'), (0.8, 'Study')], default=(0.3, 'Turn Up'), max_length=1000),
        ),
    ]
