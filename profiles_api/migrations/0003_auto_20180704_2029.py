# Generated by Django 2.0.5 on 2018-07-04 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_auto_20180704_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='nfclistofusers',
            name='listOfDoorGroups',
            field=models.ManyToManyField(related_name='DoorGroup_NfcListOfUsers', to='profiles_api.NfcDoorGroup'),
        ),
        migrations.AddField(
            model_name='nfclistofusers',
            name='listOfDoors',
            field=models.ManyToManyField(related_name='ListOfDoors_NfcListOfUsers', to='profiles_api.NfcDoor'),
        ),
        migrations.AlterField(
            model_name='nfckey',
            name='AESEncryptKey',
            field=models.BinaryField(default=b'\xc4:UV&\xab\xbad\xdb\x03{\x86\xd6\x0c\xddD\xe1i2"\xa3\xf1\xea\rT\xfa\xbf\xe2\xdc\x894w\xf0\xfe\xf6l.\xcb6^\xc3@~^1`3\x08I\x8d\xb1\xf8j\x8dsn\xees\xf1\xb7@\x89\xd1\x8b\xd0\xa0\xa9\x11\xa6\xb3\xc1\x83$\x133!\x0c\xe1\xb9D,\xdc\xc1ZS\'\x92\xa4\xb7\x9d&\xd0>4\xfd\x1fR\x0eP\xf7\xd4\x83\x94\xbf\x18\x10\x11h\xd2\x1fb@He\x9e@\x02\x95\x86N\x8b]\x88\xd1\xeb\x1bl\x9e', max_length=128),
        ),
        migrations.AlterField(
            model_name='nfclistofusers',
            name='TDAT',
            field=models.TextField(default='Q59NqnAiNRRQ77FoGvDJykDy4tMkyvnQSMoBjOwUTBCO3DaPdvGXsPc0Ohyp4sq2Y8mrHgDFP1lgl0hHygNpWOlqbw4kNVZiXbNJnoM9QvqvgKaBVdlfgkAuGmzyYdlN2UTywKkXrxTg2TzFs9mFrpbEX1PjScjTUwpoLSHFq8GxlSoGis2IuL8y1ySMwpdFOaDQLvT0GqfRMER6uc56CE5pcRFfPGM7Q5uh8pvx8cQhrSkBV0tKfL8aJakastQX', editable=False, max_length=256),
        ),
        migrations.AlterField(
            model_name='nfclistofusers',
            name='accesingUDID',
            field=models.TextField(default='64PS7pF8rpN5dL1fPyXrJjN60fDHNgIiLyL1ANmxkqMBqPrgXtKGoTtNEiOsuC6k5b19AFmmlwMF3NULaoB0Us1Ix80rZmyNB4KR06AjvhPC7Zi1iZqbkIJ5mZHfAHiixYysl9FZza8Hd180j63otB9ElOlBDXr1VaSC5Pov06lTMwqM5MLBOCj40oL0og0COJyikWo98jKBQC52o8MvW7pKD6ZTj8gPnLbkAGidQA0vnRJTqHt6QPBM3PQVWPkM', editable=False, max_length=256),
        ),
        migrations.AlterField(
            model_name='nfclistofusers',
            name='encryptionKey',
            field=models.TextField(default='XXxJKd6bCtPHNtqggSXKanlV8BH4hABv7s6df1h0ABCML7X3SbbehTZtiz7M1jPgbDHiOdxN1IxvnF9MLNRtWn1spVQdFYIplgLspsj89xq7CpjFcrflwzZN8WJ4kLIvkkFF74b3Lo88fU8D5F6h2ZgxMbommvxaaNUi5kfaPt6JairUYBus9u3yyCL6qxU4TFPpNmGZOTJZCaVvuTuJduG7wD4hQeRf3UhVJjotPa61jBZW7XaNaUYlIpt1DudZ', editable=False, max_length=256),
        ),
    ]
