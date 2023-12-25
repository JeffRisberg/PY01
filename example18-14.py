from collections import ChainMap

from typing import Any

Symbol = str

class Environment(ChainMap):
    "A ChainMap that allows changing an item in-place."

    def change(self, key: Symbol, value: Any) -> None:
        "Find where key is defined and change the value there."
        for map in self.maps:
            if key in map:
                map[key] = value  # type: ignore[index]
                return
        raise KeyError(key)

inner_env = {'a': 2}
outer_env = {'a': 0, 'b': 1}
env = Environment(inner_env, outer_env)
print(env['a'])

env['a'] = 111
env['c'] = 222
print(env)
Environment({'a': 111, 'c': 222}, {'a': 0, 'b': 1})
env.change('b', 333)
print(env)
Environment({'a': 111, 'c': 222}, {'a': 0, 'b': 333})
