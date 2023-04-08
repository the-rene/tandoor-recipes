from django.db.models import Func, Q


class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 0)'


def str2bool(v):
    if type(v) == bool or v is None:
        return v
    else:
        return v.lower() in ("yes", "true", "1")


def get_duplicate_object_with_plural(model, name):
    if obj := model.objects.filter(Q(name=name) | Q(plural_name=name)).first():
        return obj
    return None
