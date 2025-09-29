def set_nested(d, path, value):
    if d is None:
        d = {}
    ns = dict(d)  # shallow copy
    parts = path.split(".")
    target = ns
    for p in parts[:-1]:
        if p not in target or not isinstance(target[p], dict):
            target[p] = {}
        target = target[p]
    target[parts[-1]] = value
    return ns

class FilterModule(object):
    def filters(self):
        return {
            'set_nested': set_nested
        }