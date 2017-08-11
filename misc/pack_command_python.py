SYM_STAR = b'*'
SYM_DOLLAR = b'$'
SYM_CRLF = b'\r\n'
SYM_LF = b'\n'

def encode(value):
    "Return a bytestring representation of the value"
    if isinstance(value, str):
        return value.encode('utf-8')
    if isinstance(value, float):
        value = repr(value)
    if not isinstance(value, str):
        value = str(value)
    if isinstance(value, str):
        value = value.encode('utf-8', 'strict')
    return value

def pack_command(*args):
    "Pack a series of arguments into a value Redis command"
    output = SYM_STAR + str(len(args)).encode('utf-8') + SYM_CRLF
    for enc_value in map(encode, args):
        output += SYM_DOLLAR
        output += str(len(enc_value)).encode('utf-8')
        output += SYM_CRLF
        output += enc_value
        output += SYM_CRLF
    return [output]
