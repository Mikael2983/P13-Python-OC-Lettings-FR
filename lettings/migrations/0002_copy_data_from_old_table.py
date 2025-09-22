from django.db import migrations


def copy_data(apps, schema_editor):
    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')

    old_addresses = OldAddress.objects.all()
    new_addresses = [
        NewAddress(
            id=old_addr.id,
            number=old_addr.number,
            street=old_addr.street,
            city=old_addr.city,
            state=old_addr.state,
            zip_code=old_addr.zip_code,
            country_iso_code=old_addr.country_iso_code,
        )
        for old_addr in old_addresses
    ]
    NewAddress.objects.bulk_create(new_addresses)

    old_lettings = OldLetting.objects.all()
    new_lettings = [
        NewLetting(
            id=old_let.id,
            title=old_let.title,
            address_id=old_let.address_id,
        )
        for old_let in old_lettings
    ]
    NewLetting.objects.bulk_create(new_lettings)


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_data, migrations.RunPython.noop),
    ]