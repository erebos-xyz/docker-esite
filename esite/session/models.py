import uuid
from django.db import models
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import PageChooserPanel, TabbedInterface, ObjectList, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.core.models import Page
from wagtail.core import blocks

from esite.api.helpers import register_streamfield_block

from esite.api.models import (
    GraphQLForeignKey,
    GraphQLField,
    GraphQLStreamfield,
    GraphQLImage,
    GraphQLString,
    GraphQLCollection,
    GraphQLEmbed,
    GraphQLSnippet,
    GraphQLBoolean,
    GraphQLSnippet,
)

# Create your homepage related models here.

@register_streamfield_block
class _SE_PresentatorBlock(blocks.StructBlock):
    presentator_name = blocks.CharBlock(null=True, required=True, help_text="Name of the presentator")
    presentator_email = blocks.EmailBlock(null=True, required=True, help_text="Important! Format ci@s.co")
    presentator_link = blocks.URLBlock(null=True, required=True, help_text="Important! Format https://www.domain.tld/xyz")

    graphql_fields = [GraphQLString("presentator_name"), GraphQLString("presentator_link"),]

@register_streamfield_block
class _SE_AttendeeBlock(blocks.StructBlock):
    attendee_name = blocks.CharBlock(null=True, required=False, help_text="Name of the attendee")
    attendee_email = blocks.EmailBlock(null=True, required=False, help_text="Important! Format ci@s.co")
    attendee_attendance = blocks.BooleanBlock(null=False, required=False, default=False, help_text="Whether the attendee was attending or not")
    attendee_cache = blocks.TextBlock(null=True, required=False,  help_text="Other information")

    graphql_fields = [GraphQLString("attendee_name"), GraphQLString("attendee_email"), GraphQLBoolean("attendee_attendance"),]


class Session(models.Model):
    session_id = models.CharField(primary_key=True, max_length=36)
    session_name = models.CharField(null=True, blank=True, max_length=32)
    session_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    session_scope = models.CharField(null=True, blank=True, max_length=256)
    session_from = models.DateTimeField(null=True, blank=True)
    session_to = models.DateTimeField(null=True, blank=True)
    session_room = models.CharField(null=True, blank=True, max_length=32)
    session_max_attendees = models.PositiveIntegerField(null=False, blank=False, default=16)
    session_current_attendees = models.PositiveIntegerField(null=False, blank=False, default=0)

    session_presentators = StreamField([
        ('se_presentator', _SE_PresentatorBlock(null=True, icon='fa-id-badge')),
    ], null=True, blank=False)

    session_attendees = StreamField([
        ('se_attendee', _SE_AttendeeBlock(null=True, icon='fa-credit-card')),
    ], null=True, blank=True)

    session_cache = models.TextField(null=True, blank=True)


    graphql_fields = [
        GraphQLString("session_id"),
        GraphQLString("session_name"),
        GraphQLImage('session_image'),
        GraphQLString("session_scope"),
        GraphQLString("session_from"),
        GraphQLString("session_to"),
        GraphQLString("session_room"),
        GraphQLString("session_max_attendees"),
        GraphQLString("session_current_attendees"),
        GraphQLStreamfield("session_presentators"),
        GraphQLStreamfield("session_attendees"),
        GraphQLString("session_cache"),
    ]

    main_content_panels = [
        #FieldPanel('session_id'),
        FieldPanel('session_name'),
        ImageChooserPanel('session_image'),
        FieldPanel('session_scope'),
        FieldPanel('session_from'),
        FieldPanel('session_to'),
        FieldPanel('session_room'),
        FieldPanel('session_max_attendees'),
        FieldPanel('session_current_attendees'),
        StreamFieldPanel('session_presentators'),
        StreamFieldPanel('session_attendees'),
        FieldPanel('session_cache'),
    ]

    
    edit_handler = TabbedInterface([
        ObjectList(main_content_panels, heading='Main'),
    ])

    # custom save function
    def save(self, *args, **kwargs):
        if not self.session_id:
            self.session_id = str(uuid.uuid4())

        super(Session, self).save(*args, **kwargs)

    def __str__(self):
        return self.session_id

#> Linuxdaypage
class SessionPage(Page):
    test = models.CharField(null=True, blank=True, max_length=256)

    main_content_panels = [
        FieldPanel('test'),
    ]

    graphql_fields = [
        GraphQLString("test"),
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels + main_content_panels, heading='Main'),
        ObjectList(Page.promote_panels + Page.settings_panels, heading='Settings', classname="settings")
    ])

