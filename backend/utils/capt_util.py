import os
import random
import subprocess
import tempfile

from captcha.conf import settings

from captcha.views import getsize, makeimg, DISTANCE_FROM_TOP
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404, HttpResponse
from PIL import Image, ImageDraw, ImageFont
from ranged_response import RangedFileResponse

from system.models import CaptchaStore

try:
    from cStringIO import StringIO
except ImportError:
    from io import BytesIO as StringIO


def captcha_image(request, key, scale=1):
    if scale == 2 and not settings.CAPTCHA_2X_IMAGE:
        raise Http404
    try:
        store = CaptchaStore.objects.get(id=key)
    except CaptchaStore.DoesNotExist:
        # HTTP 410 Gone status so that crawlers don't index these expired urls.
        return HttpResponse(status=410)

    random.seed(key)  # Do not generate different images for the same key

    text = store.challenge

    if isinstance(settings.CAPTCHA_FONT_PATH, str):
        fontpath = settings.CAPTCHA_FONT_PATH
    elif isinstance(settings.CAPTCHA_FONT_PATH, (list, tuple)):
        fontpath = random.choice(settings.CAPTCHA_FONT_PATH)
    else:
        raise ImproperlyConfigured(
            "settings.CAPTCHA_FONT_PATH needs to be a path to a font or list of paths to fonts"
        )

    if fontpath.lower().strip().endswith("ttf"):
        font = ImageFont.truetype(fontpath, settings.CAPTCHA_FONT_SIZE * scale)
    else:
        font = ImageFont.load(fontpath)

    if settings.CAPTCHA_IMAGE_SIZE:
        size = settings.CAPTCHA_IMAGE_SIZE
    else:
        size = getsize(font, text)
        size = (size[0] * 2, int(size[1] * 1.4))

    image = makeimg(size)
    xpos = 2

    charlist = []
    for char in text:
        if char in settings.CAPTCHA_PUNCTUATION and len(charlist) >= 1:
            charlist[-1] += char
        else:
            charlist.append(char)
    for char in charlist:
        fgimage = Image.new("RGB", size, settings.CAPTCHA_FOREGROUND_COLOR)
        charimage = Image.new("L", getsize(font, " %s " % char), "#000000")
        chardraw = ImageDraw.Draw(charimage)
        chardraw.text((0, 0), " %s " % char, font=font, fill="#ffffff")
        if settings.CAPTCHA_LETTER_ROTATION:
            charimage = charimage.rotate(
                random.randrange(*settings.CAPTCHA_LETTER_ROTATION),
                expand=0,
                resample=Image.BICUBIC,
            )
        charimage = charimage.crop(charimage.getbbox())
        maskimage = Image.new("L", size)

        maskimage.paste(
            charimage,
            (
                xpos,
                DISTANCE_FROM_TOP,
                xpos + charimage.size[0],
                DISTANCE_FROM_TOP + charimage.size[1],
            ),
        )
        size = maskimage.size
        image = Image.composite(fgimage, image, maskimage)
        xpos = xpos + 2 + charimage.size[0]

    if settings.CAPTCHA_IMAGE_SIZE:
        # centering captcha on the image
        tmpimg = makeimg(size)
        tmpimg.paste(
            image,
            (
                int((size[0] - xpos) / 2),
                int((size[1] - charimage.size[1]) / 2 - DISTANCE_FROM_TOP),
            ),
        )
        image = tmpimg.crop((0, 0, size[0], size[1]))
    else:
        image = image.crop((0, 0, xpos + 1, size[1]))
    draw = ImageDraw.Draw(image)

    for f in settings.noise_functions():
        draw = f(draw, image)
    for f in settings.filter_functions():
        image = f(image)

    out = StringIO()
    image.save(out, "PNG")
    out.seek(0)

    response = HttpResponse(content_type="image/png")
    response.write(out.read())
    response["Content-length"] = out.tell()


    return response