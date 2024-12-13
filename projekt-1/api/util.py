from functools import reduce

def compose(*funcs):
    return lambda *args: reduce(lambda acc, f: f(*acc) if isinstance(acc, tuple) else f(acc), reversed(funcs), args)

def validate_uploaded_file(file):
    if not file:
        raise ValueError("No file uploaded")
    return file