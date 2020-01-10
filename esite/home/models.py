from django.http import HttpResponse
from django.db import models
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.admin.edit_handlers import PageChooserPanel, TabbedInterface, ObjectList, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from modelcluster.fields import ParentalKey

from esite.colorfield.fields import ColorField, ColorAlphaField
from esite.colorfield.blocks import ColorBlock, ColorAlphaBlock, GradientColorBlock

#from grapple.models import (
#    GraphQLField,
#    GraphQLString,
#    GraphQLStreamfield,
#)

# Create your homepage related models here.

@register_snippet
class Button(models.Model):
    button_title = models.CharField(null=True, blank=False, max_length=255)
    #button_id = models.CharField(null=True, blank=True, max_length=255)
    #button_class = models.CharField(null=True, blank=True, max_length=255)
    button_embed = models.CharField(null=True, blank=True, max_length=255)
    button_link = models.URLField(null=True, blank=True)
    button_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        FieldPanel('button_title'),
        FieldPanel('button_embed'),
        FieldPanel('button_link'),
        PageChooserPanel('button_page')
    ]

    def __str__(self):
        return self.button_title


#> Header
class _H_HeroBlock(blocks.StructBlock):
    slide_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="The bold header text at the frontpage slider")
    slide_subhead = blocks.RichTextBlock(null=True, blank=False, help_text="The content of the frontpage slider element", classname="full")
    slide_image = ImageChooserBlock(null=True, blank=False, help_text="Big, high resolution slider image")
    slide_button = SnippetChooserBlock(Button, null=True, blank=True, required=False, help_text="The button displayed at the frontpage slider")

#> Why Section
class Why_CollumBlock(blocks.StructBlock):
    collum_image = ImageChooserBlock(null=True, blank=False, help_text="Icon representating the below content")
    collum_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="The bold header text at the frontpage slider")
    collum_subhead = blocks.RichTextBlock(null=True, blank=False, help_text="The content of the frontpage slider element", classname="full")
    collum_paragraph = blocks.RichTextBlock(null=True, blank=False, help_text="Formatted text", classname="full")

class _S_WhyBlock(blocks.StructBlock):
    why_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="Bold header text")
    why_displayhead = blocks.BooleanBlock(null=True, blank=True, default=True, required=False, help_text="Whether or not to display the header")
    #why_collum1 = Why_CollumBlock(null=True, blank=False, icon='cogs', help_text="Left block")
    #why_collum2 = Why_CollumBlock(null=True, blank=False, icon='cogs', help_text="Middle block")
    #why_collum3 = Why_CollumBlock(null=True, blank=False, icon='cogs', help_text="Right block")
    why_collums = blocks.StreamBlock([
        ('why_collum', Why_CollumBlock(null=True, blank=False, icon='cogs'))
    ], null=True, blank=False, max_num=8)

#> About Shop
class Shop_PricingcardBlock(blocks.StructBlock):
    shopcard_background = ColorBlock(null=True, blank=False, help_text="Select background color that contrasts text")
    shopcard_title = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="Title of pricing card")
    shopcard_description = blocks.RichTextBlock(null=True, blank=False, help_text="Description of offer", classname="full")
    shopcard_price = blocks.DecimalBlock(null=True, blank=False, decimal_places=2, help="Price of the offer")
    shopcard_sucessmsg = blocks.RichTextBlock(null=True, blank=False, help_text="Success message", classname="full")
    shopcard_button = SnippetChooserBlock(Button, null=True, blank=True, required=False, help_text="Button displayed at the pricing-section")

class _S_ShopBlock(blocks.StructBlock):
    #shop_background = ColorBlock(null=True, blank=False, help_text="Select background color that contrasts text")
    shop_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="Bold header text")
    shop_displayhead = blocks.BooleanBlock(null=True, blank=True, default=True, required=False, help_text="Whether or not to display the header")
    #pshop_pricingcards = blocks.StreamBlock([
    #    ('shopcard', Shop_PricingcardBlock(null=True, blank=False))
    #], null=True, blank=False, max_num=3)

#> About Section
class About_CardBlock(blocks.StructBlock):
    card_image = ImageChooserBlock(null=True, blank=False, help_text="Office-fitting image")
    card_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="The bold header text at the frontpage slider")
    card_paragraph = blocks.RichTextBlock(null=True, blank=False, help_text="Formatted text", classname="full")

class _S_AboutBlock(blocks.StructBlock):
    about_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="Bold header text")
    about_displayhead = blocks.BooleanBlock(null=True, blank=True, default=True, required=False, help_text="Whether or not to display the header")
    #about_card1 = About_CardBlock(null=True, blank=False, icon='cogs', help_text="Upper Left")
    #about_card2 = About_CardBlock(null=True, blank=False, icon='cogs', help_text="Upper Right")
    #about_card3 = About_CardBlock(null=True, blank=False, icon='cogs', help_text="Lower Left")
    #about_card4 = About_CardBlock(null=True, blank=False, icon='cogs', help_text="Lower Right")
    about_cards = blocks.StreamBlock([
        ('aboutcard', About_CardBlock(null=True, blank=False, icon='cogs'))
    ], null=True, blank=False, max_num=6)

#> Instagram Section
class _S_InstagramBlock(blocks.StructBlock):
    instagram_id = blocks.URLBlock(null=True, blank=False, classname="full", help_text="URL to Instagram-Post")
    instagram_pc = blocks.CharBlock(null=True, blank=False, classname="full", help_text="Instagram-Post count")

#> Steps Section
class Steps_StepBlock(blocks.StructBlock):
    step_image = ImageChooserBlock(null=True, blank=False, help_text="Image fitting this step")
    step_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="Bold header text")
    step_subhead = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="Bold header text")
    step_paragraph = blocks.RichTextBlock(null=True, blank=False, help_text="Step paragraph", classname="full")

class _S_StepsBlock(blocks.StructBlock):
    steps_head = blocks.CharBlock(null=True, blank=False, classname="full title", help_text="Bold header text")
    steps_displayhead = blocks.BooleanBlock(null=True, blank=True, default=True, required=False, help_text="Whether or not to display the header")
    steps_steps = blocks.StreamBlock([
        ('step', Steps_StepBlock(null=True, blank=False))
    ], null=True, blank=False, max_num=4)

#> Homepage
class HomePage(Page):
    header = StreamField([
      ('hbanner', blocks.StructBlock([
        ('banner', blocks.CharBlock(blank=True, classname="full title", icon='title'))
      ], required=False, icon='bold')),

      ('hfull', blocks.StructBlock([
        ('full', blocks.CharBlock(blank=True, classname="full title", icon='title'))
      ], required=False, icon='placeholder')),

      ('hcode', blocks.StructBlock([
        ('code', blocks.RawHTMLBlock(blank=True, classname="full"))
      ], icon='code'))
    ], blank=True)

    article = StreamField([
      ('aabout', blocks.StructBlock([
        ('about_pages', blocks.StreamBlock([
          ('about', blocks.StructBlock([
            ('blink', blocks.CharBlock(blank=True, classname="full")),
            ('use_image', blocks.BooleanBlock(default=False, help_text="Use picture instead of blink", required=False, classname="full")),
            ('image', ImageChooserBlock(required=False, classname="full")),
            ('boxes', blocks.StreamBlock([
              ('title', blocks.CharBlock(blank=True, classname="full title", icon='title')),
              ('content', blocks.RichTextBlock(blank=True, features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full"))
            ]))
          ], icon='doc-full'))
        ], icon='cogs')),
      ], icon='radio-empty')),

      ('amotd', blocks.StructBlock([
        ('modt', blocks.CharBlock(max_length=16, default="Sky's The Limit", classname="full")),
      ], icon='pilcrow')),

      ('asharingan', blocks.StructBlock([
        ('sharingan', blocks.StructBlock([
          ('show_projects', blocks.BooleanBlock(default=True, help_text="Whether sh1, sh2, sh3 will be shown on this block", required=False, classname="full")),
          ('sharingan_1', blocks.RichTextBlock(default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
          ('sharingan_2', blocks.RichTextBlock(default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
          ('sharingan_3', blocks.RichTextBlock(default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", features=['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'hr', 'embed', 'link', 'document-link', 'image'], classname="full")),
        ])),
        ('team', blocks.StructBlock([
          ('show_team', blocks.BooleanBlock(default=False, help_text="Whether the team will be shown on this block", required=False, classname="full")),
          ('nyan_titel', blocks.CharBlock(max_length=16, default="The Team", classname="full")),
          ('members', blocks.StreamBlock([
            ('member', blocks.StructBlock([
              ('pic', ImageChooserBlock(blank=True, classname="full")),
              ('name', blocks.CharBlock(blank=True, max_length=16, default="", classname="full")),
              ('description', blocks.CharBlock(max_length=128, default="", classname="full"))
            ], icon='user'))
          ], required=False))
        ]))
      ], icon='view')),

      ('acommunity', blocks.StructBlock([
        ('admins', blocks.StructBlock([
          ('show_admins', blocks.BooleanBlock(default=True, help_text="Whether the admins will be shown on this block", required=False, classname="full")),
          ('admins_titel', blocks.CharBlock(max_length=16, default="Admins", classname="full")),
          ('members', blocks.StreamBlock([
            ('mrow', blocks.StreamBlock([
              ('member', blocks.StructBlock([
                ('pic', ImageChooserBlock(blank=True, classname="full")),
                ('name', blocks.CharBlock(blank=True, max_length=16, default="", classname="full")),
                ('description', blocks.CharBlock(max_length=128, default="", classname="full"))
              ], icon='user'))
            ], icon='group'))
          ], required=False))
        ])),
        ('mods', blocks.StructBlock([
          ('show_mods', blocks.BooleanBlock(default=True, help_text="Whether the mods will be shown on this block", required=False, classname="full")),
          ('mods_titel', blocks.CharBlock(max_length=16, default="Mods", classname="full")),
          ('members', blocks.StreamBlock([
            ('mrow', blocks.StreamBlock([
              ('member', blocks.StructBlock([
                ('pic', ImageChooserBlock(blank=True, classname="full")),
                ('name', blocks.CharBlock(blank=True, max_length=16, default="", classname="full"))
              ], icon='user'))
            ], icon='group'))
          ], required=False))
        ]))
      ], icon='group')),

      ('aspaceship', blocks.StructBlock([
      ], icon='pick')),

      ('agallery', blocks.StructBlock([
        ('title', blocks.CharBlock(blank=True, classname="full")),
        ('gallery', blocks.StreamBlock([
          ('image', ImageChooserBlock(blank=True, classname="full")),
        ]))
      ], icon='grip')),

      ('acode', blocks.StructBlock([
        ('code', blocks.RawHTMLBlock(blank=True, classname="full"))
      ], icon='code'))
    ], blank=True)


    main_content_panels = [
      StreamFieldPanel('header'),
      StreamFieldPanel('article')
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels + main_content_panels, heading='Main'),
        ObjectList(Page.promote_panels + Page.settings_panels, heading='Settings', classname="settings")
    ])
