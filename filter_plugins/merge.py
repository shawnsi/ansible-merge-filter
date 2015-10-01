from collections import defaultdict


def merge_sum(iterable):
    start = 0

    if isinstance(iterable[0], list):
        start = []

    return sum(iterable, start)

def merge(*args):
    flat = defaultdict(list)

    for hash in args:
        for key in hash:
            flat[key].append(hash[key])

    merged = {}

    for key in flat:
        dict_instances = [isinstance(v, dict) for v in flat[key]]

        if any(dict_instances):
            merged[key] = merge(*flat[key])
        else:
            merged[key] = merge_sum(flat[key])

    return merged


class FilterModule(object):
    def filters(self):
        return {'merge': merge}
