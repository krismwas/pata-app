from django import template

from ..models import Profile, profile_pic_thumbnails

register = template.Library()

@register.filter
def get_thumbnails(obj, arg):
    """
    obj = profile instance
    """
    arg = arg.lower()
    if not isinstance(obj, Profile):
        raise TypeError("This is not a valid product model")
    choices = dict(profile_pic_thumbnails.dr_profile_thumb_choices)
    # print(choices)
    if not choices.get(arg):
        raise TypeError("This is not a valid type for this model")
    return obj.profile_pic_thumbnails_set.filter(type=arg).first().photo.url