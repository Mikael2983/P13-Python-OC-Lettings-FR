from django.db import migrations


def delete_old_data(apps, schema_editor):

    OldProfile = apps.get_model('oc_lettings_site', 'profile')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    OldAddress = apps.get_model('oc_lettings_site', 'Address')

    OldProfile.objects.all().delete()
    OldLetting.objects.all().delete()
    OldAddress.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_copy_data_from_old_table'),
        ('profiles', '0002_copy_data_from_old_table'),
    ]

    operations = [
        migrations.RunPython(delete_old_data, migrations.RunPython.noop),
    ]
