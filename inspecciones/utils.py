import base64
from django.core.files.base import ContentFile

def guardar_firma(base64_string, nombre):
    if not base64_string:
        return None

    format, imgstr = base64_string.split(';base64,')
    ext = format.split('/')[-1]

    return ContentFile(
        base64.b64decode(imgstr),
        name=f"{nombre}.{ext}"
    )