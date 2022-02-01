from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel,InlinePanel
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from modelcluster.fields import ParentalKey

class HomePage(Page):
  body = RichTextField(blank=True)
  titleHome = models.CharField(max_length=255)
    
  content_panels = Page.content_panels + [
    FieldPanel('body', classname="full"),
    FieldPanel('titleHome'),
    InlinePanel('aboutUs_placements', label="AboutUs"),
  ]

@register_snippet
class AboutUs(models.Model):
  date = models.DateField("About date")
  title = models.CharField(max_length=255)
  body = RichTextField(blank=True)
  image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
  )

  panels = [
    ImageChooserPanel('image'),
    FieldPanel('date'),
    FieldPanel('title'),
    FieldPanel('body'),
  ]

  def __str__(self):
    return self.title
  

class HomePageAboutUsPlacement(Orderable, models.Model):
    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='aboutUs_placements')
    aboutUs = models.ForeignKey('home.AboutUs', on_delete=models.CASCADE, related_name='+')  

    class Meta(Orderable.Meta):
        verbose_name = "aboutUs placement"
        verbose_name_plural = "aboutUs placements"

    panels = [
        SnippetChooserPanel('aboutUs'),
    ]

    def __str__(self):
        return self.page.titleHome + " -> " + self.aboutUs.title   
