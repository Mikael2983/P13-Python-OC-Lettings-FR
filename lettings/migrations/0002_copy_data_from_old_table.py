from django.db import migrations


def copy_data(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')

    for old_addr in OldAddress.objects.all():
        NewAddress.objects.create(
            id=old_addr.id,
            number=old_addr.number,
            street=old_addr.street,
            city=old_addr.city,
            state=old_addr.state,
            zip_code=old_addr.zip_code,
            country_iso_code=old_addr.country_iso_code,
        )

    for old_let in OldLetting.objects.all():
        NewLetting.objects.create(
            id=old_let.id,
            title=old_let.title,
            address_id=old_let.address_id,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_data, migrations.RunPython.noop),
    ]