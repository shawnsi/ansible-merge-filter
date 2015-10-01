
def merge(a, b):
    for key in b:
        if key in a:
            if isinstance(b[key], dict):
                a[key] = merge(a[key], b[key])
            else:
                a[key] = a[key] + b[key]

        else:
            a[key] = b[key]

    return a


class FilterModule(object):
    def filters(self):
        return {'merge': merge}
