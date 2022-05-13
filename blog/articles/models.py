from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _
from .managers import PostManager
from django.urls import reverse
from django.shortcuts import  redirect

User = get_user_model()

# ? Blog-Post Categories
class Category(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=50, help_text=_("Unique title for each category of post"), default="", blank=False, null=False,unique=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title

    

# ? Blog Post Table
class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=250, verbose_name=_("Title"), help_text=_("Identify post uniquely"), default="", blank=False, null=False, unique=True)
    slug = models.SlugField(verbose_name=_("Slugify Title"), max_length=300, help_text=_("URL for this blog post"), default="", blank=False, null=False)
    tags = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Tags"), help_text = _("Keywords for a post"))
    banner = models.ImageField(verbose_name=_("Post Banner Image"), upload_to="posts/", blank=False, null=True)
    content = RichTextField()
    publish = models.BooleanField(
        verbose_name=_('Publish'),
        default=True,
        help_text=_('Will this post be published?')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager() # ?  The default manager.
    publish_objects = PostManager() # ? The publish post manager.

    # def save(self, *args, **kwargs):
    #     if self.banner:
    #         self.banner = get_thumbnail(self.banner, '728x380', quality=99, format='JPEG')
    #     super(Post, self).save(*args, **kwargs)


    class Meta:
        verbose_name=_("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'title': self.slug})

