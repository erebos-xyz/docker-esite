# Generated by Django 2.2.9 on 2020-06-16 06:08

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinuxdayPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headers', wagtail.core.fields.StreamField([('h_banner', wagtail.core.blocks.StructBlock([('banner_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', help_text='The bold header text at the frontpage slider', null=True)), ('banner_subhead', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', help_text='The content of the frontpage slider element', null=True)), ('banner_image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Big, high resolution slider image', null=True))], blank=False, icon='title', null=True)), ('h_code', wagtail.core.blocks.RawHTMLBlock(blank=True, classname='full', icon='code', null=True))], null=True)),
                ('sections', wagtail.core.fields.StreamField([('s_info', wagtail.core.blocks.StructBlock([('info_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', help_text='The bold header text at the frontpage slider', null=True)), ('info_paragraph', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', help_text='The content of the frontpage slider element', null=True)), ('info_image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Big, high resolution slider image', null=True)), ('info_image_position', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('left', 'left'), ('right', 'right')], icon='cup', null=True))], blank=False, icon='radio-empty', null=True)), ('s_boxes', wagtail.core.blocks.StructBlock([('boxes_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', help_text='Bold header text', null=True)), ('boxes_displayhead', wagtail.core.blocks.BooleanBlock(blank=True, default=True, help_text='Whether or not to display the header', null=True, required=False)), ('boxes_boxes', wagtail.core.blocks.StreamBlock([('boxes_box', wagtail.core.blocks.StructBlock([('box_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', help_text='The bold header text at the frontpage slider', null=True)), ('box_paragraph', wagtail.core.blocks.RichTextBlock(blank=False, classname='full', help_text='Formatted text', null=True))], blank=False, icon='cogs', null=True))], blank=False, null=True))], blank=False, icon='pilcrow', null=True)), ('s_partners', wagtail.core.blocks.StructBlock([('partners_head', wagtail.core.blocks.CharBlock(blank=False, classname='full title', help_text='Bold header text', null=True)), ('partners_displayhead', wagtail.core.blocks.BooleanBlock(blank=True, default=True, help_text='Whether or not to display the header', null=True, required=False)), ('partners_partners', wagtail.core.blocks.StreamBlock([('partners_partner', wagtail.core.blocks.StructBlock([('partner_logo', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Partner logo', null=True)), ('partner_link', wagtail.core.blocks.URLBlock(blank=True, help_text='Important! Format https://www.domain.tld/xyz', null=True))], blank=False, icon='cogs', null=True))], blank=False, null=True))], blank=False, icon='fa-id-badge', null=True)), ('s_code', wagtail.core.blocks.RawHTMLBlock(blank=True, classname='full', icon='code', null=True))], null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]