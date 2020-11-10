from .models import Link


def ctx_dict(request):
    links = Link.objects.all()
    return {link.key: link.url for link in links}
