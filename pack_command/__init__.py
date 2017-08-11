try:
    from ._speedups import pack_command
except ImportError as e:
    print(e)
    from ._backup import pack_command
