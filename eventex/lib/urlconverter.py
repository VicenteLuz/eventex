from django.conf import settings


def mask(n):
    return n ^ settings.MASK


class MaskConverter:
    regex = r'\d+'

    def to_python(self, value):
        return mask(int(value))

    def to_url(self, value):
        return '{}'.format(mask(value))