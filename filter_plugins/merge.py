from collections import defaultdict


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
            merged[key] = sum(flat[key])

    return merged


class FilterModule(object):
    def filters(self):
        return {'merge': merge}
