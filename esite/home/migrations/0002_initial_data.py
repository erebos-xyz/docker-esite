# -*- coding: utf-8 -*-
from django.db import migrations


def create_homepage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model('contenttypes.ContentType')
    Page = apps.get_model('wagtailcore.Page')
    Site = apps.get_model('wagtailcore.Site')
    Image = apps.get_model('wagtailimages.Image')
    HomePage = apps.get_model('home.HomePage')

    # Delete the default homepage
    # If migration is run multiple times, it may have already been deleted
    Page.objects.filter(id=2).delete()

    # Create initial images
    Image.objects.create(
        id=1,
        title='linuxday.jpg',
        file='init_images/linuxday.jpg',
        width=1100,
        height=592,
        file_size=125764,
        collection_id=1,
        file_hash='81451a6dc48a63a55a18f695a12bfe7754d5bb42',
    )

    Image.objects.create(
        id=2,
        title='LinmuxWochen.png',
        file='init_images/LinmuxWochen.png',
        width=336,
        height=160,
        file_size=20499,
        collection_id=1,
        file_hash='50b32f7f8b80aa22cbaabd666b14ce65ff142581',
    )

    Image.objects.create(
        id=3,
        title='csm_STRABAGLOGO_rot_7a4706104f.jpg',
        file='init_images/csm_STRABAGLOGO_rot_7a4706104f.jpg',
        width=263,
        height=109,
        file_size=8302,
        collection_id=1,
        file_hash='357290a3aa638d77f5f38641d117e8bbc4373af6',
    )

    Image.objects.create(
        id=4,
        title='csm_red-hat-social-share_0e49d6c4fc.jpg',
        file='init_images/csm_red-hat-social-share_0e49d6c4fc.jpg',
        width=263,
        height=148,
        file_size=4874,
        collection_id=1,
        file_hash='8d4903eb67f8ee69b50a6e076baf0e110cd410f9',
    )

    Image.objects.create(
        id=5,
        title='csm_Plakat_Entwurf1_8fc59a4401.png',
        file='init_images/csm_Plakat_Entwurf1_8fc59a4401.png',
        width=530,
        height=702,
        file_size=121723,
        collection_id=1,
        file_hash='c6aa5e4142523f04bbe5c50596baba967f84b5eb',
    )

    Image.objects.create(
        id=6,
        title='csm_OSEG-Logos-4501476_738c67d026.jpg',
        file='init_images/csm_OSEG-Logos-4501476_738c67d026.jpg',
        width=263,
        height=161,
        file_size=15878,
        collection_id=1,
        file_hash='306ce3f5a554a51bcb9850430ee1ddf19566664d',
    )

    Image.objects.create(
        id=7,
        title='csm_hqdefault_da22db267d.jpg',
        file='init_images/csm_hqdefault_da22db267d.jpg',
        width=263,
        height=198,
        file_size=3867,
        collection_id=1,
        file_hash='25b2b789df85e408a0c5eac7b71f29bf16a9ad91',
    )

    Image.objects.create(
        id=8,
        title='csm_anexia_607859e049.png',
        file='init_images/csm_anexia_607859e049.png',
        width=263,
        height=152,
        file_size=6581,
        collection_id=1,
        file_hash='8422ae61c4ccfc50ea1934376249c9d796f0496d',
    )

    Image.objects.create(
        id=9,
        title='csm_alturos-destinations-logo-2017_c2694ef669.png',
        file='init_images/csm_alturos-destinations-logo-2017_c2694ef669.png',
        width=263,
        height=127,
        file_size=7306,
        collection_id=1,
        file_hash='b25745a7bdc0f71d82afda1f85ef2c4f19ad88c3',
    )

    # Create content type for homepage model
    homepage_content_type, __ = ContentType.objects.get_or_create(
        model='homepage', app_label='home')

    # Create a initial homepage
    homepage = HomePage.objects.create(
        title="Linuxday",
        draft_title="Linuxday",
        slug='home',
        content_type=homepage_content_type,
        path='00010001',
        depth=2,
        numchild=0,
        url_path='/home/',
        headers='''[
  {
    "type":"h_banner",
    "value":{
      "banner_head":"Open Source and Linux Day 2020",
      "banner_subhead":"<p>Das Motto des heurigen Jahres ist &quot;DevOps &amp; Security&quot;. In zahlreichen Vortr\u00e4gen und Workshops m\u00f6chten wir unser Wissen zu diesem Themenkomplex austauschen und vertiefen. In gem\u00fctlichem Ambiente finden wir Zeit f\u00fcr Diskussionen und das Kn\u00fcpfen von neuen Netzwerken finden.</p>",
      "banner_image":1
    },
    "id":"8d272b27-fbe2-4b2e-81fa-0b89ea4a84a8"
  }
]''',
        sections='''[
  {
    "type":"s_info",
    "value":{
      "info_head":"Open Source & Linux Day",
      "info_paragraph":"<p>Nach dem erfolgreichen Start im vorigen Jahr\u00a0findet auch heuer ein Open Source &amp; Linux Day an der HTL Villach statt.</p><p><b>Aufgrund der Hygienebestimmungen f\u00fcr Schulen musste der Open Source &amp; Linux Day f\u00fcr 2020 leider abgesagt werden!</b></p><p>Im Zuge der Linuxwochen \u00d6sterreich Tour (<a href=\\\"https://www.linuxwochen.at/\\\"><b>https://www.linuxwochen.at/</b></a>) veranstalten wir gemeinsam mit</p><ul><li>Red Hat DACH (<a href=\\\"https://www.redhat.com/de/global/dach\\\"><b>https://www.redhat.com/de/global/dach</b></a>) und\u00a0 der</li><li>Open Source Experts Group (<a href=\\\"https://www.oseg.at/\\\"><b>https://www.oseg.at</b></a>) diesen Event.</li></ul><p>Neben dem geplanten Rahmenprogramm, wie zum Beispiel der Preisverleihung zur 1. Villacher Hacking-Challenge, wollen wir einen diesen Tag mit Vortr\u00e4gen und Workshops f\u00fcr alle Teilnehmer zu einem besonderen Erlebnis werden lassen.</p><p>An alle, die Interesse haben, den Tag mitzugestalten, ergeht ein <a href=\\\"https://osslinuxday.htl-villach.at/anmeldung\\\"><b>Call for Participation</b></a>, wir freuen uns schon auf Sie.</p>",
      "info_image":5,
      "info_image_position":"right"
    },
    "id":"accfb65f-f54a-4e2d-90de-81819a8edf17"
  },
  {
    "type":"s_info",
    "value":{
      "info_head":"Linux Wochen",
      "info_paragraph":"<h3>Tux on Tour</h3><p>Der Pinguin macht 2020\u00a0wieder die \u00d6sterreich Rundfahrt. Wie in den letzten Jahren sind die Linuxwochen eine Veranstaltung, die weit \u00fcber Linux hinaus geht und den Open Source Gedanken in all seinen Facetten repr\u00e4sentiert.</p><p><b>DevOps und Security</b></p><p>Unter diesem Motto treffen sich Vertreter aus Wirtschaft, Bildung und der Linux-Gemeinde zum Wissensaustausch und kn\u00fcpfen neue Netzwerke.</p>",
      "info_image":2,
      "info_image_position":"right"
    },
    "id":"473a04c2-ef8e-46e0-98c6-4fd5cdccaa38"
  },
  {
    "type":"s_boxes",
    "value":{
      "boxes_head":"Updates",
      "boxes_displayhead":false,
      "boxes_boxes":[
        {
          "type":"boxes_box",
          "value":{
            "box_head":"Open Source and Linuxday",
            "box_paragraph":"<h2> abgesagt!</h2>"
          },
          "id":"4afff67f-0c57-4e54-81a6-66cd18686abc"
        },
        {
          "type":"boxes_box",
          "value":{
            "box_head":"Termine",
            "box_paragraph":"<p> 15.01.2020: Start des CfP</p><p>29.02.2020: Ende des CfP</p><p>01.04.2020: Bekanntgabe des Programms</p>"
          },
          "id":"70ab8eb9-7014-4325-b9f7-486e44dbea43"
        },
        {
          "type":"boxes_box",
          "value":{
            "box_head":"Highlights",
            "box_paragraph":"<p>Vortr\u00e4ge und Workshops</p><p>Siegerehrung der 1. Villacher Hacking-Challenge</p><p>Networking Lounge - treffen Sie Ihre zuk\u00fcnftigen Mitarbeiter</p>"
          },
          "id":"99a42e94-9549-4eff-9f0d-1971d4f67739"
        }
      ]
    },
    "id":"46f22701-6984-4cee-9ecc-9946a290e1c3"
  },
  {
    "type":"s_partners",
    "value":{
      "partners_head":"Featuring",
      "partners_displayhead":false,
      "partners_partners":[
        {
          "type":"partners_partner",
          "value":{
            "partner_logo":8,
            "partner_link":"https://anexia.com/"
          },
          "id":"2c96f8fa-de56-4368-9147-6fe9891ac410"
        },
        {
          "type":"partners_partner",
          "value":{
            "partner_logo":4,
            "partner_link":"https://www.redhat.com/"
          },
          "id":"eee0dab6-4807-4727-af1a-2d93d3feb2c3"
        },
        {
          "type":"partners_partner",
          "value":{
            "partner_logo":3,
            "partner_link":"https://www.strabag.com/"
          },
          "id":"55333aff-7e9f-499e-8117-3e9e72232bc5"
        },
        {
          "type":"partners_partner",
          "value":{
            "partner_logo":7,
            "partner_link":"https://www.htl-villach.at/"
          },
          "id":"b6ce5911-cc58-4bd9-908e-31a118163bd8"
        },
        {
          "type":"partners_partner",
          "value":{
            "partner_logo":9,
            "partner_link":"https://www.alturos.com/"
          },
          "id":"e8441b81-6c53-4db4-90e7-43115e04d504"
        },
        {
          "type":"partners_partner",
          "value":{
            "partner_logo":2,
            "partner_link":"https://osslinuxday.htl-villach.at/"
          },
          "id":"56f3372a-aa3e-42fb-b259-73e586033749"
        },
        {
          "type":"partners_partner",
          "value":{
            "partner_logo":6,
            "partner_link":"http://oseg.at/"
          },
          "id":"ba642bfb-20d0-4180-8d92-d8700d3434a7"
        }
      ]
    },
    "id":"df2b2a2c-a42c-470b-8bdc-bcbb7dd96cf6"
  }
]''',
    )

    # Create a site with the new homepage set as the root
    Site.objects.create(
        hostname='localhost', root_page=homepage, is_default_site=True)


def remove_homepage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model('contenttypes.ContentType')
    HomePage = apps.get_model('home.HomePage')

    # Delete the default homepage
    # Page and Site objects CASCADE
    HomePage.objects.filter(slug='home', depth=2).delete()

    # Delete content type for homepage model
    ContentType.objects.filter(model='homepage', app_label='home').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_homepage, remove_homepage),
    ]