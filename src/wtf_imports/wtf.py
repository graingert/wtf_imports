from __future__ import absolute_import, print_function


def foo():
    try:
        from . import asdfasdfasdf
    except ImportError:
        pass

print(__name__, __package__)
foo()
print(__name__, __package__)
