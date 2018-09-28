"""
Create metaclass that generates properties automatically.
"""


class AutoPropertyMeta(type):
    parse_methods = ['get_', 'set_', 'del_']

    @classmethod
    def put_method(mcs, param, elem, callable_params):
        for parse_method in mcs.parse_methods:
            if param.startswith(parse_method):
                prop_name = param.replace(parse_method, '')
                if not callable_params.get(prop_name, None):
                    callable_params[prop_name] = {}
                callable_params[prop_name][parse_method] = elem[param]
        return callable_params

    def __new__(mcs, *args, **kwargs):
        new_class = super().__new__(mcs, *args, **kwargs)
        callable_params = {}
        for elem in args:
            if isinstance(elem, dict):
                for param in elem:
                    if callable(elem[param]):
                        callable_params = mcs.put_method(param,
                                                         elem,
                                                         callable_params)
        for callable_param in callable_params:
            setattr(
                new_class,
                callable_param,
                property(
                    fget=callable_params[callable_param].get('get_', None),
                    fset=callable_params[callable_param].get('set_', None),
                    fdel=callable_params[callable_param].get('del_', None)
                )
            )
        return new_class


class Example(metaclass=AutoPropertyMeta):
    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return 'yyy'

    def del_x(self):
        del self._x


ex = Example()
ex.x = 25 + 65
print(ex.x)
del ex.x

print(ex.y)
