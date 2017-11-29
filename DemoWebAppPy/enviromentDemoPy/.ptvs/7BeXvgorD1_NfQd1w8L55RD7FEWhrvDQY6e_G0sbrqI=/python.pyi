﻿class __Unknown:
    '<unknown type>'
class __NoneType:
    'the type of the None object'
class object:
    'The most base type'
    __class__ = object
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        pass
    def __dir__():
        '__dir__() -> list\ndefault dir() implementation'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __format__(self, format_spec):
        'default object formatter'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __reduce__(self):
        'helper for pickle'
        pass
    def __reduce_ex__(self, protocol):
        'helper for pickle'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        pass
    def __sizeof__():
        '__sizeof__() -> int\nsize of object in memory, in bytes'
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
__Object = object
class type(object):
    "type(object_or_name, bases, dict)\ntype(object) -> the object's type\ntype(name, bases, dict) -> a new type"
    __base__ = object()
    __bases__ = ()
    __basicsize__ = 864
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    __class__ = type
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        pass
    __dict__ = {}
    __dictoffset__ = 264
    def __dir__():
        '__dir__() -> list\nspecialized __dir__ implementation for types'
        pass
    __flags__ = -2146675712
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __instancecheck__():
        '__instancecheck__() -> bool\ncheck if an object is an instance'
        pass
    __itemsize__ = 40
    __mro__ = ()
    __name__ = 'type'
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __prepare__():
        '__prepare__() -> dict\nused to create the namespace for the class statement'
        pass
    __qualname__ = 'type'
    def __repr__(self):
        'Return repr(self).'
        pass
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        pass
    def __sizeof__():
        '__sizeof__() -> int\nreturn memory consumption of the type object'
        pass
    def __subclasscheck__():
        '__subclasscheck__() -> bool\ncheck if a class is a subclass'
        pass
    def __subclasses__():
        '__subclasses__() -> list of immediate subclasses'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    __text_signature__
    __weakrefoffset__ = 368
    def mro():
        "mro() -> list\nreturn a type's method resolution order"
        pass
__Type = type
class int(object):
    "int(x=0) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    def __abs__(self):
        'abs(self)'
        pass
    def __add__(self, value):
        'Return self+value.'
        pass
    def __and__(self, value):
        'Return self&value.'
        pass
    def __bool__(self):
        'self != 0'
        pass
    def __ceil__(self):
        'Ceiling of an Integral returns itself.'
        pass
    __class__ = int
    def __divmod__(self, value):
        'Return divmod(self, value).'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __float__(self):
        'float(self)'
        pass
    def __floor__(self):
        'Flooring an Integral returns itself.'
        pass
    def __floordiv__(self, value):
        'Return self//value.'
        pass
    def __format__(self, format_spec):
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getnewargs__(self):
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __index__(self):
        'Return self converted to an integer, if self is suitable for use as an index into a list.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __int__(self):
        'int(self)'
        pass
    def __invert__(self):
        '~self'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __lshift__(self, value):
        'Return self<<value.'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __mod__(self, value):
        'Return self%value.'
        pass
    def __mul__(self, value):
        'Return self*value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __neg__(self):
        '-self'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __or__(self, value):
        'Return self|value.'
        pass
    def __pos__(self):
        '+self'
        pass
    def __pow__(self, value, mod=None):
        'Return pow(self, value, mod).'
        pass
    def __radd__(self, value):
        'Return value+self.'
        pass
    def __rand__(self, value):
        'Return value&self.'
        pass
    def __rdivmod__(self, value):
        'Return divmod(value, self).'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __rfloordiv__(self, value):
        'Return value//self.'
        pass
    def __rlshift__(self, value):
        'Return value<<self.'
        pass
    def __rmod__(self, value):
        'Return value%self.'
        pass
    def __rmul__(self, value):
        'Return value*self.'
        pass
    def __ror__(self, value):
        'Return value|self.'
        pass
    def __round__(self, ndigits=0):
        'Rounding an Integral returns itself.\nRounding with an ndigits argument also returns an integer.'
        pass
    def __rpow__(self, value, mod=None):
        'Return pow(value, self, mod).'
        pass
    def __rrshift__(self, value):
        'Return value>>self.'
        pass
    def __rshift__(self, value):
        'Return self>>value.'
        pass
    def __rsub__(self, value):
        'Return value-self.'
        pass
    def __rtruediv__(self, value):
        'Return value/self.'
        pass
    def __rxor__(self, value):
        'Return value^self.'
        pass
    def __sizeof__(self):
        'Returns size in memory, in bytes'
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __sub__(self, value):
        'Return self-value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def __truediv__(self, value):
        'Return self/value.'
        pass
    def __trunc__(self):
        'Truncating an Integral returns itself.'
        pass
    def __xor__(self, value):
        'Return self^value.'
        pass
    def bit_length(self):
        "int.bit_length() -> int\n\nNumber of bits necessary to represent self in binary.\n>>> bin(37)\n'0b100101'\n>>> (37).bit_length()\n6"
        pass
    def conjugate(self):
        'Returns self, the complex conjugate of any int.'
        pass
    denominator = getset_descriptor()
    def from_bytes(self):
        "int.from_bytes(bytes, byteorder, *, signed=False) -> int\n\nReturn the integer represented by the given array of bytes.\n\nThe bytes argument must be a bytes-like object (e.g. bytes or bytearray).\n\nThe byteorder argument determines the byte order used to represent the\ninteger.  If byteorder is 'big', the most significant byte is at the\nbeginning of the byte array.  If byteorder is 'little', the most\nsignificant byte is at the end of the byte array.  To request the native\nbyte order of the host system, use `sys.byteorder' as the byte order value.\n\nThe signed keyword-only argument indicates whether two's complement is\nused to represent the integer."
        pass
    imag = getset_descriptor()
    numerator = getset_descriptor()
    real = getset_descriptor()
    def to_bytes(self):
        "int.to_bytes(length, byteorder, *, signed=False) -> bytes\n\nReturn an array of bytes representing an integer.\n\nThe integer is represented using length bytes.  An OverflowError is\nraised if the integer is not representable with the given number of\nbytes.\n\nThe byteorder argument determines the byte order used to represent the\ninteger.  If byteorder is 'big', the most significant byte is at the\nbeginning of the byte array.  If byteorder is 'little', the most\nsignificant byte is at the end of the byte array.  To request the native\nbyte order of the host system, use `sys.byteorder' as the byte order value.\n\nThe signed keyword-only argument determines whether two's complement is\nused to represent the integer.  If signed is False and a negative integer\nis given, an OverflowError is raised."
        pass
__Int = int
class bool(int):
    'bool(x) -> bool\n\nReturns True when the argument x is true, False otherwise.\nThe builtins True and False are the only two instances of the class bool.\nThe class bool is a subclass of the class int, and cannot be subclassed.'
    def __and__(self, value):
        'Return self&value.'
        pass
    __class__ = bool
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __or__(self, value):
        'Return self|value.'
        pass
    def __rand__(self, value):
        'Return value&self.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __ror__(self, value):
        'Return value|self.'
        pass
    def __rxor__(self, value):
        'Return value^self.'
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def __xor__(self, value):
        'Return self^value.'
        pass
    def from_bytes(self):
        "int.from_bytes(bytes, byteorder, *, signed=False) -> int\n\nReturn the integer represented by the given array of bytes.\n\nThe bytes argument must be a bytes-like object (e.g. bytes or bytearray).\n\nThe byteorder argument determines the byte order used to represent the\ninteger.  If byteorder is 'big', the most significant byte is at the\nbeginning of the byte array.  If byteorder is 'little', the most\nsignificant byte is at the end of the byte array.  To request the native\nbyte order of the host system, use `sys.byteorder' as the byte order value.\n\nThe signed keyword-only argument indicates whether two's complement is\nused to represent the integer."
        pass
__Bool = bool
__Long = __Int
class float(object):
    'float(x) -> floating point number\n\nConvert a string or number to a floating point number, if possible.'
    def __abs__(self):
        'abs(self)'
        pass
    def __add__(self, value):
        'Return self+value.'
        pass
    def __bool__(self):
        'self != 0'
        pass
    __class__ = float
    def __divmod__(self, value):
        'Return divmod(self, value).'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __float__(self):
        'float(self)'
        pass
    def __floordiv__(self, value):
        'Return self//value.'
        pass
    def __format__(self, format_spec):
        'float.__format__(format_spec) -> string\n\nFormats the float according to format_spec.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getformat__(self):
        "float.__getformat__(typestr) -> string\n\nYou probably don't want to use this function.  It exists mainly to be\nused in Python's test suite.\n\ntypestr must be 'double' or 'float'.  This function returns whichever of\n'unknown', 'IEEE, big-endian' or 'IEEE, little-endian' best describes the\nformat of floating point numbers used by the C type named by typestr."
        pass
    def __getnewargs__(self):
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __int__(self):
        'int(self)'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __mod__(self, value):
        'Return self%value.'
        pass
    def __mul__(self, value):
        'Return self*value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __neg__(self):
        '-self'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __pos__(self):
        '+self'
        pass
    def __pow__(self, value, mod=None):
        'Return pow(self, value, mod).'
        pass
    def __radd__(self, value):
        'Return value+self.'
        pass
    def __rdivmod__(self, value):
        'Return divmod(value, self).'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __rfloordiv__(self, value):
        'Return value//self.'
        pass
    def __rmod__(self, value):
        'Return value%self.'
        pass
    def __rmul__(self, value):
        'Return value*self.'
        pass
    def __round__(self, ndigits=0):
        'Return the Integral closest to x, rounding half toward even.\nWhen an argument is passed, work like built-in round(x, ndigits).'
        pass
    def __rpow__(self, value, mod=None):
        'Return pow(value, self, mod).'
        pass
    def __rsub__(self, value):
        'Return value-self.'
        pass
    def __rtruediv__(self, value):
        'Return value/self.'
        pass
    def __setformat__(self):
        "float.__setformat__(typestr, fmt) -> None\n\nYou probably don't want to use this function.  It exists mainly to be\nused in Python's test suite.\n\ntypestr must be 'double' or 'float'.  fmt must be one of 'unknown',\n'IEEE, big-endian' or 'IEEE, little-endian', and in addition can only be\none of the latter two if it appears to match the underlying C reality.\n\nOverride the automatic determination of C-level floating point type.\nThis affects how floats are converted to and from binary strings."
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __sub__(self, value):
        'Return self-value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def __truediv__(self, value):
        'Return self/value.'
        pass
    def __trunc__(self):
        'Return the Integral closest to x between 0 and x.'
        pass
    def as_integer_ratio(self):
        'float.as_integer_ratio() -> (int, int)\n\nReturn a pair of integers, whose ratio is exactly equal to the original\nfloat and with a positive denominator.\nRaise OverflowError on infinities and a ValueError on NaNs.\n\n>>> (10.0).as_integer_ratio()\n(10, 1)\n>>> (0.0).as_integer_ratio()\n(0, 1)\n>>> (-.25).as_integer_ratio()\n(-1, 4)'
        pass
    def conjugate(self):
        'Return self, the complex conjugate of any float.'
        pass
    def fromhex(self):
        "float.fromhex(string) -> float\n\nCreate a floating-point number from a hexadecimal string.\n>>> float.fromhex('0x1.ffffp10')\n2047.984375\n>>> float.fromhex('-0x1p-1074')\n-5e-324"
        pass
    def hex(self):
        "float.hex() -> string\n\nReturn a hexadecimal representation of a floating-point number.\n>>> (-0.1).hex()\n'-0x1.999999999999ap-4'\n>>> 3.14159.hex()\n'0x1.921f9f01b866ep+1'"
        pass
    imag = getset_descriptor()
    def is_integer(self):
        'Return True if the float is an integer.'
        pass
    real = getset_descriptor()
__Float = float
class complex(object):
    'complex(real[, imag]) -> complex number\n\nCreate a complex number from a real part and an optional imaginary part.\nThis is equivalent to (real + imag*1j) where imag defaults to 0.'
    def __abs__(self):
        'abs(self)'
        pass
    def __add__(self, value):
        'Return self+value.'
        pass
    def __bool__(self):
        'self != 0'
        pass
    __class__ = complex
    def __divmod__(self, value):
        'Return divmod(self, value).'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __float__(self):
        'float(self)'
        pass
    def __floordiv__(self, value):
        'Return self//value.'
        pass
    def __format__(self, format_spec):
        'complex.__format__() -> str\n\nConvert to a string according to format_spec.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getnewargs__(self):
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __int__(self):
        'int(self)'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __mod__(self, value):
        'Return self%value.'
        pass
    def __mul__(self, value):
        'Return self*value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __neg__(self):
        '-self'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __pos__(self):
        '+self'
        pass
    def __pow__(self, value, mod=None):
        'Return pow(self, value, mod).'
        pass
    def __radd__(self, value):
        'Return value+self.'
        pass
    def __rdivmod__(self, value):
        'Return divmod(value, self).'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __rfloordiv__(self, value):
        'Return value//self.'
        pass
    def __rmod__(self, value):
        'Return value%self.'
        pass
    def __rmul__(self, value):
        'Return value*self.'
        pass
    def __rpow__(self, value, mod=None):
        'Return pow(value, self, mod).'
        pass
    def __rsub__(self, value):
        'Return value-self.'
        pass
    def __rtruediv__(self, value):
        'Return value/self.'
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __sub__(self, value):
        'Return self-value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def __truediv__(self, value):
        'Return self/value.'
        pass
    def conjugate(self):
        'complex.conjugate() -> complex\n\nReturn the complex conjugate of its argument. (3-4j).conjugate() == 3+4j.'
        pass
    imag = member_descriptor()
    real = member_descriptor()
__Complex = complex
class tuple(object):
    "tuple() -> empty tuple\ntuple(iterable) -> tuple initialized from iterable's items\n\nIf the argument is a tuple, the return value is the same object."
    def __add__(self, value):
        'Return self+value.'
        pass
    __class__ = tuple
    def __contains__(self, key):
        'Return key in self.'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getitem__(self, key):
        'Return self[key].'
        pass
    def __getnewargs__(self):
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __mul__(self, value):
        'Return self*value.n'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __rmul__(self, value):
        'Return self*value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def count(self, x):
        'T.count(value) -> integer -- return number of occurrences of value'
        pass
    def index(self, v):
        'T.index(value, [start, [stop]]) -> integer -- return first index of value.\nRaises ValueError if the value is not present.'
        pass
__Tuple = tuple
class list(object):
    "list() -> new empty list\nlist(iterable) -> new list initialized from iterable's items"
    def __add__(self, value):
        'Return self+value.'
        pass
    __class__ = list
    def __contains__(self, key):
        'Return key in self.'
        pass
    def __delitem__(self, key):
        'Delete self[key].'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getitem__(self, index):
        'x.__getitem__(y) <==> x[y]'
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    __hash__
    def __iadd__(self, value):
        'Implement self+=value.'
        pass
    def __imul__(self, value):
        'Implement self*=value.'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __mul__(self, value):
        'Return self*value.n'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __reversed__(self):
        'L.__reversed__() -- return a reverse iterator over the list'
        pass
    def __rmul__(self, value):
        'Return self*value.'
        pass
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        pass
    def __sizeof__(self):
        'L.__sizeof__() -- size of L in memory, in bytes'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def append(self):
        'L.append(object) -> None -- append object to end'
        pass
    def clear(self):
        'L.clear() -> None -- remove all items from L'
        pass
    def copy(self):
        'L.copy() -> list -- a shallow copy of L'
        pass
    def count(self, x):
        'L.count(value) -> integer -- return number of occurrences of value'
        pass
    def extend(self):
        'L.extend(iterable) -> None -- extend list by appending elements from the iterable'
        pass
    def index(self, v):
        'L.index(value, [start, [stop]]) -> integer -- return first index of value.\nRaises ValueError if the value is not present.'
        pass
    def insert(self):
        'L.insert(index, object) -- insert object before index'
        pass
    def pop(self):
        'L.pop([index]) -> item -- remove and return item at index (default last).\nRaises IndexError if list is empty or index is out of range.'
        pass
    def remove(self):
        'L.remove(value) -> None -- remove first occurrence of value.\nRaises ValueError if the value is not present.'
        pass
    def reverse(self):
        'L.reverse() -- reverse *IN PLACE*'
        pass
    def sort(self):
        'L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*'
        pass
__List = list
class dict(object):
    "dict() -> new empty dictionary\ndict(mapping) -> new dictionary initialized from a mapping object's\n    (key, value) pairs\ndict(iterable) -> new dictionary initialized as if via:\n    d = {}\n    for k, v in iterable:\n        d[k] = v\ndict(**kwargs) -> new dictionary initialized with the name=value pairs\n    in the keyword argument list.  For example:  dict(one=1, two=2)"
    __class__ = dict
    def __contains__(self, key):
        'True if D has a key k, else False.'
        pass
    def __delitem__(self, key):
        'Delete self[key].'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getitem__(self, index):
        'x.__getitem__(y) <==> x[y]'
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    __hash__
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        pass
    def __sizeof__(self):
        'D.__sizeof__() -> size of D in memory, in bytes'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def clear(self):
        'D.clear() -> None.  Remove all items from D.'
        pass
    def copy(self):
        'D.copy() -> a shallow copy of D'
        pass
    def fromkeys(iterable, value=None):
        'Returns a new dict with keys from iterable and values equal to value.'
        pass
    def get(self):
        'D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.'
        pass
    def items(self):
        "D.items() -> a set-like object providing a view on D's items"
        pass
    def keys(self):
        "D.keys() -> a set-like object providing a view on D's keys"
        pass
    def pop(self):
        'D.pop(k[,d]) -> v, remove specified key and return the corresponding value.\nIf key is not found, d is returned if given, otherwise KeyError is raised'
        pass
    def popitem(self):
        'D.popitem() -> (k, v), remove and return some (key, value) pair as a\n2-tuple; but raise KeyError if D is empty.'
        pass
    def setdefault(self):
        'D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D'
        pass
    def update(self):
        'D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.\nIf E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]\nIf E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v\nIn either case, this is followed by: for k in F:  D[k] = F[k]'
        pass
    def values(self):
        "D.values() -> an object providing a view on D's values"
        pass
__Dict = dict
class set(object):
    'set() -> new empty set object\nset(iterable) -> new set object\n\nBuild an unordered collection of unique elements.'
    def __and__(self, value):
        'Return self&value.'
        pass
    __class__ = set
    def __contains__(self, value):
        'x.__contains__(y) <==> y in x.'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    __hash__
    def __iand__(self, value):
        'Return self&=value.'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __ior__(self, value):
        'Return self|=value.'
        pass
    def __isub__(self, value):
        'Return self-=value.'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __ixor__(self, value):
        'Return self^=value.'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __or__(self, value):
        'Return self|value.'
        pass
    def __rand__(self, value):
        'Return value&self.'
        pass
    def __reduce__(self):
        'Return state information for pickling.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __ror__(self, value):
        'Return value|self.'
        pass
    def __rsub__(self, value):
        'Return value-self.'
        pass
    def __rxor__(self, value):
        'Return value^self.'
        pass
    def __sizeof__(self):
        'S.__sizeof__() -> size of S in memory, in bytes'
        pass
    def __sub__(self, value):
        'Return self-value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def __xor__(self, value):
        'Return self^value.'
        pass
    def add(self):
        'Add an element to a set.\n\nThis has no effect if the element is already present.'
        pass
    def clear(self):
        'Remove all elements from this set.'
        pass
    def copy(self):
        'Return a shallow copy of a set.'
        pass
    def difference(self):
        'Return the difference of two or more sets as a new set.\n\n(i.e. all elements that are in this set but not the others.)'
        pass
    def difference_update(self):
        'Remove all elements of another set from this set.'
        pass
    def discard(self):
        'Remove an element from a set if it is a member.\n\nIf the element is not a member, do nothing.'
        pass
    def intersection(self):
        'Return the intersection of two sets as a new set.\n\n(i.e. all elements that are in both sets.)'
        pass
    def intersection_update(self):
        'Update a set with the intersection of itself and another.'
        pass
    def isdisjoint(self):
        'Return True if two sets have a null intersection.'
        pass
    def issubset(self):
        'Report whether another set contains this set.'
        pass
    def issuperset(self):
        'Report whether this set contains another set.'
        pass
    def pop(self):
        'Remove and return an arbitrary set element.\nRaises KeyError if the set is empty.'
        pass
    def remove(self):
        'Remove an element from a set; it must be a member.\n\nIf the element is not a member, raise a KeyError.'
        pass
    def symmetric_difference(self):
        'Return the symmetric difference of two sets as a new set.\n\n(i.e. all elements that are in exactly one of the sets.)'
        pass
    def symmetric_difference_update(self):
        'Update a set with the symmetric difference of itself and another.'
        pass
    def union(self):
        'Return the union of sets as a new set.\n\n(i.e. all elements that are in either set.)'
        pass
    def update(self):
        'Update a set with the union of itself and others.'
        pass
__Set = set
class frozenset(object):
    'frozenset() -> empty frozenset object\nfrozenset(iterable) -> frozenset object\n\nBuild an immutable unordered collection of unique elements.'
    def __and__(self, value):
        'Return self&value.'
        pass
    __class__ = frozenset
    def __contains__(self, value):
        'x.__contains__(y) <==> y in x.'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __or__(self, value):
        'Return self|value.'
        pass
    def __rand__(self, value):
        'Return value&self.'
        pass
    def __reduce__(self):
        'Return state information for pickling.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __ror__(self, value):
        'Return value|self.'
        pass
    def __rsub__(self, value):
        'Return value-self.'
        pass
    def __rxor__(self, value):
        'Return value^self.'
        pass
    def __sizeof__(self):
        'S.__sizeof__() -> size of S in memory, in bytes'
        pass
    def __sub__(self, value):
        'Return self-value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def __xor__(self, value):
        'Return self^value.'
        pass
    def copy(self):
        'Return a shallow copy of a set.'
        pass
    def difference(self):
        'Return the difference of two or more sets as a new set.\n\n(i.e. all elements that are in this set but not the others.)'
        pass
    def intersection(self):
        'Return the intersection of two sets as a new set.\n\n(i.e. all elements that are in both sets.)'
        pass
    def isdisjoint(self):
        'Return True if two sets have a null intersection.'
        pass
    def issubset(self):
        'Report whether another set contains this set.'
        pass
    def issuperset(self):
        'Report whether this set contains another set.'
        pass
    def symmetric_difference(self):
        'Return the symmetric difference of two sets as a new set.\n\n(i.e. all elements that are in exactly one of the sets.)'
        pass
    def union(self):
        'Return the union of sets as a new set.\n\n(i.e. all elements that are in either set.)'
        pass
__FrozenSet = frozenset
class bytes(object):
    'bytes(iterable_of_ints) -> bytes\nbytes(string, encoding[, errors]) -> bytes\nbytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer\nbytes(int) -> bytes object of size given by the parameter initialized with null bytes\nbytes() -> empty bytes object\n\nConstruct an immutable array of bytes from:\n  - an iterable yielding integers in range(256)\n  - a text string encoded using the specified encoding\n  - any object implementing the buffer API.\n  - an integer'
    def __add__(self, value):
        'Return self+value.'
        pass
    __class__ = bytes
    def __contains__(self, key):
        'Return key in self.'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getitem__(self, key):
        'Return self[key].'
        pass
    def __getnewargs__(self):
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __mod__(self, value):
        'Return self%value.'
        pass
    def __mul__(self, value):
        'Return self*value.n'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __rmod__(self, value):
        'Return value%self.'
        pass
    def __rmul__(self, value):
        'Return self*value.'
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def capitalize(self):
        'B.capitalize() -> copy of B\n\nReturn a copy of B with only its first character capitalized (ASCII)\nand the rest lower-cased.'
        pass
    def center(self):
        'B.center(width[, fillchar]) -> copy of B\n\nReturn B centered in a string of length width.  Padding is\ndone using the specified fill character (default is a space).'
        pass
    def count(self, x):
        'B.count(sub[, start[, end]]) -> int\n\nReturn the number of non-overlapping occurrences of subsection sub in\nbytes B[start:end].  Optional arguments start and end are interpreted\nas in slice notation.'
        pass
    def decode(self, encoding='utf-8', errors='strict'):
        "Decode the bytes using the codec registered for encoding.\n\n  encoding\n    The encoding with which to decode the bytes.\n  errors\n    The error handling scheme to use for the handling of decoding errors.\n    The default is 'strict' meaning that decoding errors raise a\n    UnicodeDecodeError. Other possible values are 'ignore' and 'replace'\n    as well as any other name registered with codecs.register_error that\n    can handle UnicodeDecodeErrors."
        pass
    def endswith(self, suffix, start=0, end=-1):
        'B.endswith(suffix[, start[, end]]) -> bool\n\nReturn True if B ends with the specified suffix, False otherwise.\nWith optional start, test B beginning at that position.\nWith optional end, stop comparing B at that position.\nsuffix can also be a tuple of bytes to try.'
        pass
    def expandtabs(self, tabsize=8):
        'B.expandtabs(tabsize=8) -> copy of B\n\nReturn a copy of B where all tab characters are expanded using spaces.\nIf tabsize is not given, a tab size of 8 characters is assumed.'
        pass
    def find(self, sub, start=0, end=-1):
        'B.find(sub[, start[, end]]) -> int\n\nReturn the lowest index in B where subsection sub is found,\nsuch that sub is contained within B[start,end].  Optional\narguments start and end are interpreted as in slice notation.\n\nReturn -1 on failure.'
        pass
    def fromhex(string):
        "Create a bytes object from a string of hexadecimal numbers.\n\nSpaces between two numbers are accepted.\nExample: bytes.fromhex('B9 01EF') -> b'\\\\xb9\\\\x01\\\\xef'."
        pass
    def hex(self):
        "B.hex() -> string\n\nCreate a string of hexadecimal numbers from a bytes object.\nExample: b'\\xb9\\x01\\xef'.hex() -> 'b901ef'."
        pass
    def index(self, v):
        'B.index(sub[, start[, end]]) -> int\n\nReturn the lowest index in B where subsection sub is found,\nsuch that sub is contained within B[start,end].  Optional\narguments start and end are interpreted as in slice notation.\n\nRaises ValueError when the subsection is not found.'
        pass
    def isalnum(self):
        'B.isalnum() -> bool\n\nReturn True if all characters in B are alphanumeric\nand there is at least one character in B, False otherwise.'
        pass
    def isalpha(self):
        'B.isalpha() -> bool\n\nReturn True if all characters in B are alphabetic\nand there is at least one character in B, False otherwise.'
        pass
    def isdigit(self):
        'B.isdigit() -> bool\n\nReturn True if all characters in B are digits\nand there is at least one character in B, False otherwise.'
        pass
    def islower(self):
        'B.islower() -> bool\n\nReturn True if all cased characters in B are lowercase and there is\nat least one cased character in B, False otherwise.'
        pass
    def isspace(self):
        'B.isspace() -> bool\n\nReturn True if all characters in B are whitespace\nand there is at least one character in B, False otherwise.'
        pass
    def istitle(self):
        'B.istitle() -> bool\n\nReturn True if B is a titlecased string and there is at least one\ncharacter in B, i.e. uppercase characters may only follow uncased\ncharacters and lowercase characters only cased ones. Return False\notherwise.'
        pass
    def isupper(self):
        'B.isupper() -> bool\n\nReturn True if all cased characters in B are uppercase and there is\nat least one cased character in B, False otherwise.'
        pass
    def join(self, iterable_of_bytes):
        "Concatenate any number of bytes objects.\n\nThe bytes whose method is called is inserted in between each pair.\n\nThe result is returned as a new bytes object.\n\nExample: b'.'.join([b'ab', b'pq', b'rs']) -> b'ab.pq.rs'."
        pass
    def ljust(self):
        'B.ljust(width[, fillchar]) -> copy of B\n\nReturn B left justified in a string of length width. Padding is\ndone using the specified fill character (default is a space).'
        pass
    def lower(self):
        'B.lower() -> copy of B\n\nReturn a copy of B with all ASCII characters converted to lowercase.'
        pass
    def lstrip(self, bytes=None):
        'Strip leading bytes contained in the argument.\n\nIf the argument is omitted or None, strip leading  ASCII whitespace.'
        pass
    def maketrans(frm, to):
        'Return a translation table useable for the bytes or bytearray translate method.\n\nThe returned table will be one where each byte in frm is mapped to the byte at\nthe same position in to.\n\nThe bytes objects frm and to must be of the same length.'
        pass
    def partition(self, sep):
        'Partition the bytes into three parts using the given separator.\n\nThis will search for the separator sep in the bytes. If the separator is found,\nreturns a 3-tuple containing the part before the separator, the separator\nitself, and the part after it.\n\nIf the separator is not found, returns a 3-tuple containing the original bytes\nobject and two empty bytes objects.'
        pass
    def replace(self, old, new, count=-1):
        'Return a copy with all occurrences of substring old replaced by new.\n\n  count\n    Maximum number of occurrences to replace.\n    -1 (the default value) means replace all occurrences.\n\nIf the optional argument count is given, only the first count occurrences are\nreplaced.'
        pass
    def rfind(self, sub, start=0, end=-1):
        'B.rfind(sub[, start[, end]]) -> int\n\nReturn the highest index in B where subsection sub is found,\nsuch that sub is contained within B[start,end].  Optional\narguments start and end are interpreted as in slice notation.\n\nReturn -1 on failure.'
        pass
    def rindex(self, sub, start=0, end=-1):
        'B.rindex(sub[, start[, end]]) -> int\n\nReturn the highest index in B where subsection sub is found,\nsuch that sub is contained within B[start,end].  Optional\narguments start and end are interpreted as in slice notation.\n\nRaise ValueError when the subsection is not found.'
        pass
    def rjust(self):
        'B.rjust(width[, fillchar]) -> copy of B\n\nReturn B right justified in a string of length width. Padding is\ndone using the specified fill character (default is a space)'
        pass
    def rpartition(self, sep):
        'Partition the bytes into three parts using the given separator.\n\nThis will search for the separator sep in the bytes, starting and the end. If\nthe separator is found, returns a 3-tuple containing the part before the\nseparator, the separator itself, and the part after it.\n\nIf the separator is not found, returns a 3-tuple containing two empty bytes\nobjects and the original bytes object.'
        pass
    def rsplit(self, sep=None, maxsplit=-1):
        'Return a list of the sections in the bytes, using sep as the delimiter.\n\n  sep\n    The delimiter according which to split the bytes.\n    None (the default value) means split on ASCII whitespace characters\n    (space, tab, return, newline, formfeed, vertical tab).\n  maxsplit\n    Maximum number of splits to do.\n    -1 (the default value) means no limit.\n\nSplitting is done starting at the end of the bytes and working to the front.'
        pass
    def rstrip(self, bytes=None):
        'Strip trailing bytes contained in the argument.\n\nIf the argument is omitted or None, strip trailing ASCII whitespace.'
        pass
    def split(self, sep=None, maxsplit=-1):
        'Return a list of the sections in the bytes, using sep as the delimiter.\n\n  sep\n    The delimiter according which to split the bytes.\n    None (the default value) means split on ASCII whitespace characters\n    (space, tab, return, newline, formfeed, vertical tab).\n  maxsplit\n    Maximum number of splits to do.\n    -1 (the default value) means no limit.'
        pass
    def splitlines(self, keepends=False):
        'Return a list of the lines in the bytes, breaking at line boundaries.\n\nLine breaks are not included in the resulting list unless keepends is given and\ntrue.'
        pass
    def startswith(self, prefix, start=0, end=-1):
        'B.startswith(prefix[, start[, end]]) -> bool\n\nReturn True if B starts with the specified prefix, False otherwise.\nWith optional start, test B beginning at that position.\nWith optional end, stop comparing B at that position.\nprefix can also be a tuple of bytes to try.'
        pass
    def strip(self, bytes=None):
        'Strip leading and trailing bytes contained in the argument.\n\nIf the argument is omitted or None, strip leading and trailing ASCII whitespace.'
        pass
    def swapcase(self):
        'B.swapcase() -> copy of B\n\nReturn a copy of B with uppercase ASCII characters converted\nto lowercase ASCII and vice versa.'
        pass
    def title(self):
        'B.title() -> copy of B\n\nReturn a titlecased version of B, i.e. ASCII words start with uppercase\ncharacters, all remaining cased characters have lowercase.'
        pass
    def translate(self, table, delete=b''):
        'Return a copy with each character mapped by the given translation table.\n\n  table\n    Translation table, which must be a bytes object of length 256.\n\nAll characters occurring in the optional argument delete are removed.\nThe remaining characters are mapped through the given translation table.'
        pass
    def upper(self):
        'B.upper() -> copy of B\n\nReturn a copy of B with all ASCII characters converted to uppercase.'
        pass
    def zfill(self, width):
        'B.zfill(width) -> copy of B\n\nPad a numeric string B with zeros on the left, to fill a field\nof the specified width.  B is never truncated.'
        pass
__Bytes = bytes
class bytes_iterator(object):
    __class__ = bytes_iterator
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __length_hint__(self):
        'Private method returning an estimate of len(list(it)).'
        pass
    def __next__(self):
        'Implement next(self).'
        pass
    def __reduce__(self):
        'Return state information for pickling.'
        pass
    def __setstate__(self, state):
        'Set state information for unpickling.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
__BytesIterator = bytes_iterator
class str(object):
    "str(object='') -> str\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\n\nCreate a new string object from the given object. If encoding or\nerrors is specified, then the object must expose a data buffer\nthat will be decoded using the given encoding and error handler.\nOtherwise, returns the result of object.__str__() (if defined)\nor repr(object).\nencoding defaults to sys.getdefaultencoding().\nerrors defaults to 'strict'."
    def __add__(self, value):
        'Return self+value.'
        pass
    __class__ = str
    def __contains__(self, key):
        'Return key in self.'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __format__(self, format_spec):
        'S.__format__(format_spec) -> str\n\nReturn a formatted version of S as described by format_spec.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getitem__(self, key):
        'Return self[key].'
        pass
    def __getnewargs__(self):
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __mod__(self, value):
        'Return self%value.'
        pass
    def __mul__(self, value):
        'Return self*value.n'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __rmod__(self, value):
        'Return value%self.'
        pass
    def __rmul__(self, value):
        'Return self*value.'
        pass
    def __sizeof__(self):
        'S.__sizeof__() -> size of S in memory, in bytes'
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def capitalize(self):
        'S.capitalize() -> str\n\nReturn a capitalized version of S, i.e. make the first character\nhave upper case and the rest lower case.'
        pass
    def casefold(self):
        'S.casefold() -> str\n\nReturn a version of S suitable for caseless comparisons.'
        pass
    def center(self):
        'S.center(width[, fillchar]) -> str\n\nReturn S centered in a string of length width. Padding is\ndone using the specified fill character (default is a space)'
        pass
    def count(self, x):
        'S.count(sub[, start[, end]]) -> int\n\nReturn the number of non-overlapping occurrences of substring sub in\nstring S[start:end].  Optional arguments start and end are\ninterpreted as in slice notation.'
        pass
    def encode(self):
        "S.encode(encoding='utf-8', errors='strict') -> bytes\n\nEncode S using the codec registered for encoding. Default encoding\nis 'utf-8'. errors may be given to set a different error\nhandling scheme. Default is 'strict' meaning that encoding errors raise\na UnicodeEncodeError. Other possible values are 'ignore', 'replace' and\n'xmlcharrefreplace' as well as any other name registered with\ncodecs.register_error that can handle UnicodeEncodeErrors."
        pass
    def endswith(self, suffix, start=0, end=-1):
        'S.endswith(suffix[, start[, end]]) -> bool\n\nReturn True if S ends with the specified suffix, False otherwise.\nWith optional start, test S beginning at that position.\nWith optional end, stop comparing S at that position.\nsuffix can also be a tuple of strings to try.'
        pass
    def expandtabs(self, tabsize=8):
        'S.expandtabs(tabsize=8) -> str\n\nReturn a copy of S where all tab characters are expanded using spaces.\nIf tabsize is not given, a tab size of 8 characters is assumed.'
        pass
    def find(self, sub, start=0, end=-1):
        'S.find(sub[, start[, end]]) -> int\n\nReturn the lowest index in S where substring sub is found,\nsuch that sub is contained within S[start:end].  Optional\narguments start and end are interpreted as in slice notation.\n\nReturn -1 on failure.'
        pass
    def format(self):
        "S.format(*args, **kwargs) -> str\n\nReturn a formatted version of S, using substitutions from args and kwargs.\nThe substitutions are identified by braces ('{' and '}')."
        pass
    def format_map(self):
        "S.format_map(mapping) -> str\n\nReturn a formatted version of S, using substitutions from mapping.\nThe substitutions are identified by braces ('{' and '}')."
        pass
    def index(self, v):
        'S.index(sub[, start[, end]]) -> int\n\nReturn the lowest index in S where substring sub is found, \nsuch that sub is contained within S[start:end].  Optional\narguments start and end are interpreted as in slice notation.\n\nRaises ValueError when the substring is not found.'
        pass
    def isalnum(self):
        'S.isalnum() -> bool\n\nReturn True if all characters in S are alphanumeric\nand there is at least one character in S, False otherwise.'
        pass
    def isalpha(self):
        'S.isalpha() -> bool\n\nReturn True if all characters in S are alphabetic\nand there is at least one character in S, False otherwise.'
        pass
    def isdecimal(self):
        'S.isdecimal() -> bool\n\nReturn True if there are only decimal characters in S,\nFalse otherwise.'
        pass
    def isdigit(self):
        'S.isdigit() -> bool\n\nReturn True if all characters in S are digits\nand there is at least one character in S, False otherwise.'
        pass
    def isidentifier(self):
        'S.isidentifier() -> bool\n\nReturn True if S is a valid identifier according\nto the language definition.\n\nUse keyword.iskeyword() to test for reserved identifiers\nsuch as "def" and "class".\n'
        pass
    def islower(self):
        'S.islower() -> bool\n\nReturn True if all cased characters in S are lowercase and there is\nat least one cased character in S, False otherwise.'
        pass
    def isnumeric(self):
        'S.isnumeric() -> bool\n\nReturn True if there are only numeric characters in S,\nFalse otherwise.'
        pass
    def isprintable(self):
        'S.isprintable() -> bool\n\nReturn True if all characters in S are considered\nprintable in repr() or S is empty, False otherwise.'
        pass
    def isspace(self):
        'S.isspace() -> bool\n\nReturn True if all characters in S are whitespace\nand there is at least one character in S, False otherwise.'
        pass
    def istitle(self):
        'S.istitle() -> bool\n\nReturn True if S is a titlecased string and there is at least one\ncharacter in S, i.e. upper- and titlecase characters may only\nfollow uncased characters and lowercase characters only cased ones.\nReturn False otherwise.'
        pass
    def isupper(self):
        'S.isupper() -> bool\n\nReturn True if all cased characters in S are uppercase and there is\nat least one cased character in S, False otherwise.'
        pass
    def join(self):
        'S.join(iterable) -> str\n\nReturn a string which is the concatenation of the strings in the\niterable.  The separator between elements is S.'
        pass
    def ljust(self):
        'S.ljust(width[, fillchar]) -> str\n\nReturn S left-justified in a Unicode string of length width. Padding is\ndone using the specified fill character (default is a space).'
        pass
    def lower(self):
        'S.lower() -> str\n\nReturn a copy of the string S converted to lowercase.'
        pass
    def lstrip(self, chars):
        'S.lstrip([chars]) -> str\n\nReturn a copy of the string S with leading whitespace removed.\nIf chars is given and not None, remove characters in chars instead.'
        pass
    def maketrans(x, y=None, z=None):
        'Return a translation table usable for str.translate().\n\nIf there is only one argument, it must be a dictionary mapping Unicode\nordinals (integers) or characters to Unicode ordinals, strings or None.\nCharacter keys will be then converted to ordinals.\nIf there are two arguments, they must be strings of equal length, and\nin the resulting dictionary, each character in x will be mapped to the\ncharacter at the same position in y. If there is a third argument, it\nmust be a string, whose characters will be mapped to None in the result.'
        pass
    def partition(self):
        'S.partition(sep) -> (head, sep, tail)\n\nSearch for the separator sep in S, and return the part before it,\nthe separator itself, and the part after it.  If the separator is not\nfound, return S and two empty strings.'
        pass
    def replace(self, old, new, count=-1):
        'S.replace(old, new[, count]) -> str\n\nReturn a copy of S with all occurrences of substring\nold replaced by new.  If the optional argument count is\ngiven, only the first count occurrences are replaced.'
        pass
    def rfind(self, sub, start=0, end=-1):
        'S.rfind(sub[, start[, end]]) -> int\n\nReturn the highest index in S where substring sub is found,\nsuch that sub is contained within S[start:end].  Optional\narguments start and end are interpreted as in slice notation.\n\nReturn -1 on failure.'
        pass
    def rindex(self, sub, start=0, end=-1):
        'S.rindex(sub[, start[, end]]) -> int\n\nReturn the highest index in S where substring sub is found,\nsuch that sub is contained within S[start:end].  Optional\narguments start and end are interpreted as in slice notation.\n\nRaises ValueError when the substring is not found.'
        pass
    def rjust(self):
        'S.rjust(width[, fillchar]) -> str\n\nReturn S right-justified in a string of length width. Padding is\ndone using the specified fill character (default is a space).'
        pass
    def rpartition(self):
        'S.rpartition(sep) -> (head, sep, tail)\n\nSearch for the separator sep in S, starting at the end of S, and return\nthe part before it, the separator itself, and the part after it.  If the\nseparator is not found, return two empty strings and S.'
        pass
    def rsplit(self, sep=None, maxsplit=-1):
        'S.rsplit(sep=None, maxsplit=-1) -> list of strings\n\nReturn a list of the words in S, using sep as the\ndelimiter string, starting at the end of the string and\nworking to the front.  If maxsplit is given, at most maxsplit\nsplits are done. If sep is not specified, any whitespace string\nis a separator.'
        pass
    def rstrip(self, chars=None):
        'S.rstrip([chars]) -> str\n\nReturn a copy of the string S with trailing whitespace removed.\nIf chars is given and not None, remove characters in chars instead.'
        pass
    def split(self, sep=None, maxsplit=-1):
        'S.split(sep=None, maxsplit=-1) -> list of strings\n\nReturn a list of the words in S, using sep as the\ndelimiter string.  If maxsplit is given, at most maxsplit\nsplits are done. If sep is not specified or is None, any\nwhitespace string is a separator and empty strings are\nremoved from the result.'
        pass
    def splitlines(self, keepends=False):
        'S.splitlines([keepends]) -> list of strings\n\nReturn a list of the lines in S, breaking at line boundaries.\nLine breaks are not included in the resulting list unless keepends\nis given and true.'
        pass
    def startswith(self, prefix, start=0, end=-1):
        'S.startswith(prefix[, start[, end]]) -> bool\n\nReturn True if S starts with the specified prefix, False otherwise.\nWith optional start, test S beginning at that position.\nWith optional end, stop comparing S at that position.\nprefix can also be a tuple of strings to try.'
        pass
    def strip(self, chars=None):
        'S.strip([chars]) -> str\n\nReturn a copy of the string S with leading and trailing\nwhitespace removed.\nIf chars is given and not None, remove characters in chars instead.'
        pass
    def swapcase(self):
        'S.swapcase() -> str\n\nReturn a copy of S with uppercase characters converted to lowercase\nand vice versa.'
        pass
    def title(self):
        'S.title() -> str\n\nReturn a titlecased version of S, i.e. words start with title case\ncharacters, all remaining cased characters have lower case.'
        pass
    def translate(self):
        'S.translate(table) -> str\n\nReturn a copy of the string S in which each character has been mapped\nthrough the given translation table. The table must implement\nlookup/indexing via __getitem__, for instance a dictionary or list,\nmapping Unicode ordinals to Unicode ordinals, strings, or None. If\nthis operation raises LookupError, the character is left untouched.\nCharacters mapped to None are deleted.'
        pass
    def upper(self):
        'S.upper() -> str\n\nReturn a copy of S converted to uppercase.'
        pass
    def zfill(self, width):
        'S.zfill(width) -> str\n\nPad a numeric string S with zeros on the left, to fill a field\nof the specified width. The string S is never truncated.'
        pass
__Unicode = str
class str_iterator(object):
    __class__ = str_iterator
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __length_hint__(self):
        'Private method returning an estimate of len(list(it)).'
        pass
    def __next__(self):
        'Implement next(self).'
        pass
    def __reduce__(self):
        'Return state information for pickling.'
        pass
    def __setstate__(self, state):
        'Set state information for unpickling.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
__UnicodeIterator = str_iterator
__Str = __Unicode
__StrIterator = __UnicodeIterator
class module(object):
    'module(name[, doc])\n\nCreate a module object.\nThe name must be a string; the optional doc argument can have any type.'
    __class__ = module
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        pass
    __dict__ = {}
    def __dir__():
        '__dir__() -> list\nspecialized dir() implementation'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
__Module = module
class function(object):
    'function(code, globals[, name[, argdefs[, closure]]])\n\nCreate a function object from a code object and a dictionary.\nThe optional name string overrides the name from the code object.\nThe optional argdefs tuple specifies the default argument values.\nThe optional closure tuple supplies the bindings for free variables.'
    __annotations__ = getset_descriptor()
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    __class__ = function
    __closure__ = member_descriptor()
    __code__ = getset_descriptor()
    __defaults__ = getset_descriptor()
    __dict__ = {}
    def __get__(self, instance, owner):
        'Return an attribute of instance, which is of type owner.'
        pass
    __globals__ = member_descriptor()
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    __kwdefaults__ = getset_descriptor()
    __name__ = 'function'
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    __qualname__ = 'function'
    def __repr__(self):
        'Return repr(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
__Function = function
class wrapper_descriptor(object):
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    __class__ = wrapper_descriptor
    def __get__(self, instance, owner):
        'Return an attribute of instance, which is of type owner.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    __name__ = 'wrapper_descriptor'
    __objclass__ = member_descriptor()
    __qualname__ = 'wrapper_descriptor'
    def __reduce__(self):
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    __text_signature__
__BuiltinMethodDescriptor = wrapper_descriptor
class builtin_function_or_method(object):
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    __class__ = builtin_function_or_method
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    __name__ = 'builtin_function_or_method'
    def __ne__(self, value):
        'Return self!=value.'
        pass
    __qualname__ = 'builtin_function_or_method'
    def __reduce__(self):
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    __self__ = getset_descriptor()
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    __text_signature__
__BuiltinFunction = builtin_function_or_method
class generator(object):
    __class__ = generator
    def __del__(self):
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    __name__ = 'generator'
    def __next__(self):
        'Implement next(self).'
        pass
    __qualname__ = 'generator'
    def __repr__(self):
        'Return repr(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def close():
        'close() -> raise GeneratorExit inside generator.'
        pass
    gi_code = member_descriptor()
    gi_frame = member_descriptor()
    gi_running = member_descriptor()
    gi_yieldfrom = getset_descriptor()
    def send(arg):
        "send(arg) -> send 'arg' into generator,\nreturn next yielded value or raise StopIteration."
        pass
    def throw(typ, val, tb):
        'throw(typ[,val[,tb]]) -> raise exception in generator,\nreturn next yielded value or raise StopIteration.'
        pass
__Generator = generator
class property(object):
    'property(fget=None, fset=None, fdel=None, doc=None) -> property attribute\n\nfget is a function to be used for getting an attribute value, and likewise\nfset is a function for setting, and fdel a function for del\'ing, an\nattribute.  Typical use is to define a managed attribute x:\n\nclass C(object):\n    def getx(self): return self._x\n    def setx(self, value): self._x = value\n    def delx(self): del self._x\n    x = property(getx, setx, delx, "I\'m the \'x\' property.")\n\nDecorators make defining new properties or modifying existing ones easy:\n\nclass C(object):\n    @property\n    def x(self):\n        "I am the \'x\' property."\n        return self._x\n    @x.setter\n    def x(self, value):\n        self._x = value\n    @x.deleter\n    def x(self):\n        del self._x\n'
    __class__ = property
    def __delete__(self, instance):
        'Delete an attribute of instance.'
        pass
    def __get__(self, instance, owner):
        'Return an attribute of instance, which is of type owner.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    __isabstractmethod__ = getset_descriptor()
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __set__(self, instance, value):
        'Set an attribute of instance to value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def deleter(self):
        'Descriptor to change the deleter on a property.'
        pass
    fdel = member_descriptor()
    fget = member_descriptor()
    fset = member_descriptor()
    def getter(self):
        'Descriptor to change the getter on a property.'
        pass
    def setter(self):
        'Descriptor to change the setter on a property.'
        pass
__Property = property
class classmethod(object):
    'classmethod(function) -> method\n\nConvert a function to be a class method.\n\nA class method receives the class as implicit first argument,\njust like an instance method receives the instance.\nTo declare a class method, use this idiom:\n\n  class C:\n      @classmethod\n      def f(cls, arg1, arg2, ...):\n          ...\n\nIt can be called either on the class (e.g. C.f()) or on an instance\n(e.g. C().f()).  The instance is ignored except for its class.\nIf a class method is called for a derived class, the derived class\nobject is passed as the implied first argument.\n\nClass methods are different than C++ or Java static methods.\nIf you want those, see the staticmethod builtin.'
    __class__ = classmethod
    __dict__ = {}
    __func__ = member_descriptor()
    def __get__(self, instance, owner):
        'Return an attribute of instance, which is of type owner.'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    __isabstractmethod__ = getset_descriptor()
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
__ClassMethod = classmethod
class staticmethod(object):
    'staticmethod(function) -> method\n\nConvert a function to be a static method.\n\nA static method does not receive an implicit first argument.\nTo declare a static method, use this idiom:\n\n     class C:\n         @staticmethod\n         def f(arg1, arg2, ...):\n             ...\n\nIt can be called either on the class (e.g. C.f()) or on an instance\n(e.g. C().f()).  The instance is ignored except for its class.\n\nStatic methods in Python are similar to those found in Java or C++.\nFor a more advanced concept, see the classmethod builtin.'
    __class__ = staticmethod
    __dict__ = {}
    __func__ = member_descriptor()
    def __get__(self, instance, owner):
        'Return an attribute of instance, which is of type owner.'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    __isabstractmethod__ = getset_descriptor()
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
__StaticMethod = staticmethod
class ellipsis(object):
    __class__ = ellipsis
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __reduce__(self):
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
__Ellipsis = ellipsis
class tuple_iterator(object):
    __class__ = tuple_iterator
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __length_hint__(self):
        'Private method returning an estimate of len(list(it)).'
        pass
    def __next__(self):
        'Implement next(self).'
        pass
    def __reduce__(self):
        'Return state information for pickling.'
        pass
    def __setstate__(self, state):
        'Set state information for unpickling.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
__TupleIterator = tuple_iterator
class list_iterator(object):
    __class__ = list_iterator
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __length_hint__(self):
        'Private method returning an estimate of len(list(it)).'
        pass
    def __next__(self):
        'Implement next(self).'
        pass
    def __reduce__(self):
        'Return state information for pickling.'
        pass
    def __setstate__(self, state):
        'Set state information for unpickling.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
__ListIterator = list_iterator
class dict_keys(object):
    def __and__(self, value):
        'Return self&value.'
        pass
    __class__ = dict_keys
    def __contains__(self, key):
        'Return key in self.'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    __hash__
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __or__(self, value):
        'Return self|value.'
        pass
    def __rand__(self, value):
        'Return value&self.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __ror__(self, value):
        'Return value|self.'
        pass
    def __rsub__(self, value):
        'Return value-self.'
        pass
    def __rxor__(self, value):
        'Return value^self.'
        pass
    def __sub__(self, value):
        'Return self-value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def __xor__(self, value):
        'Return self^value.'
        pass
    def isdisjoint(self):
        'Return True if the view and the given iterable have a null intersection.'
        pass
__DictKeys = dict_keys
class dict_values(object):
    __class__ = dict_values
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
__DictValues = dict_values
class dict_items(object):
    def __and__(self, value):
        'Return self&value.'
        pass
    __class__ = dict_items
    def __contains__(self, key):
        'Return key in self.'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    __hash__
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __or__(self, value):
        'Return self|value.'
        pass
    def __rand__(self, value):
        'Return value&self.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __ror__(self, value):
        'Return value|self.'
        pass
    def __rsub__(self, value):
        'Return value-self.'
        pass
    def __rxor__(self, value):
        'Return value^self.'
        pass
    def __sub__(self, value):
        'Return self-value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def __xor__(self, value):
        'Return self^value.'
        pass
    def isdisjoint(self):
        'Return True if the view and the given iterable have a null intersection.'
        pass
__DictItems = dict_items
class set_iterator(object):
    __class__ = set_iterator
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __length_hint__(self):
        'Private method returning an estimate of len(list(it)).'
        pass
    def __next__(self):
        'Implement next(self).'
        pass
    def __reduce__(self):
        'Return state information for pickling.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
__SetIterator = set_iterator
class callable_iterator(object):
    __class__ = callable_iterator
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __next__(self):
        'Implement next(self).'
        pass
    def __reduce__(self):
        'Return state information for pickling.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
__CallableIterator = callable_iterator
__builtin_module_names = "_ast,_bisect,_blake2,_codecs,_codecs_cn,_codecs_hk,_codecs_iso2022,_codecs_jp,_codecs_kr,_codecs_tw,_collections,_csv,_datetime,_findvs,_functools,_heapq,_imp,_io,_json,_locale,_lsprof,_md5,_multibytecodec,_opcode,_operator,_pickle,_random,_sha1,_sha256,_sha3,_sha512,_signal,_sre,_stat,_string,_struct,_symtable,_thread,_tracemalloc,_warnings,_weakref,_winapi,array,atexit,audioop,binascii,builtins,cmath,errno,faulthandler,gc,itertools,marshal,math,mmap,msvcrt,nt,parser,sys,time,winreg,xxsubtype,zipimport,zlib"
class ArithmeticError(Exception):
    'Base class for arithmetic errors.'
    __class__ = ArithmeticError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class AssertionError(Exception):
    'Assertion failed.'
    __class__ = AssertionError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class AttributeError(Exception):
    'Attribute not found.'
    __class__ = AttributeError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class BaseException(object):
    'Common base class for all exceptions'
    __cause__ = getset_descriptor()
    __class__ = BaseException
    __context__ = getset_descriptor()
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        pass
    __dict__ = {}
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __reduce__(self):
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        pass
    def __setstate__(self, state):
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    __suppress_context__ = member_descriptor()
    __traceback__ = getset_descriptor()
    args = getset_descriptor()
    def with_traceback(self):
        'Exception.with_traceback(tb) --\n    set self.__traceback__ to tb and return self.'
        pass
class BlockingIOError(OSError):
    'I/O operation would block.'
    __class__ = BlockingIOError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class BrokenPipeError(ConnectionError):
    'Broken pipe.'
    __class__ = BrokenPipeError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class BufferError(Exception):
    'Buffer error.'
    __class__ = BufferError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class BytesWarning(Warning):
    'Base class for warnings about bytes and buffer related problems, mostly\nrelated to conversion from str or comparing to str.'
    __class__ = BytesWarning
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class ChildProcessError(OSError):
    'Child process error.'
    __class__ = ChildProcessError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class ConnectionAbortedError(ConnectionError):
    'Connection aborted.'
    __class__ = ConnectionAbortedError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class ConnectionError(OSError):
    'Connection error.'
    __class__ = ConnectionError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class ConnectionRefusedError(ConnectionError):
    'Connection refused.'
    __class__ = ConnectionRefusedError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class ConnectionResetError(ConnectionError):
    'Connection reset.'
    __class__ = ConnectionResetError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class DeprecationWarning(Warning):
    'Base class for warnings about deprecated features.'
    __class__ = DeprecationWarning
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class EOFError(Exception):
    'Read beyond end of file.'
    __class__ = EOFError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class Ellipsis:
    __class__ = ellipsis
    def __delattr__(name):
        'Implement delattr(self, name).'
        pass
    def __dir__():
        '__dir__() -> list\ndefault dir() implementation'
        pass
    def __eq__(value):
        'Return self==value.'
        pass
    def __format__(self, format_spec):
        'default object formatter'
        pass
    def __ge__(value):
        'Return self>=value.'
        pass
    def __getattribute__(name):
        'Return getattr(self, name).'
        pass
    def __gt__(value):
        'Return self>value.'
        pass
    def __hash__():
        'Return hash(self).'
        pass
    def __init__(*args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __le__(value):
        'Return self<=value.'
        pass
    def __lt__(value):
        'Return self<value.'
        pass
    def __ne__(value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __reduce__(self):
        pass
    def __reduce_ex__(self, protocol):
        'helper for pickle'
        pass
    def __repr__():
        'Return repr(self).'
        pass
    def __setattr__(name, value):
        'Implement setattr(self, name, value).'
        pass
    def __sizeof__():
        '__sizeof__() -> int\nsize of object in memory, in bytes'
        pass
    def __str__():
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class EnvironmentError(Exception):
    'Base class for I/O related errors.'
    __class__ = OSError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __reduce__(self):
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    characters_written = getset_descriptor()
    errno = member_descriptor()
    filename = member_descriptor()
    filename2 = member_descriptor()
    strerror = member_descriptor()
    winerror = member_descriptor()
class Exception(BaseException):
    'Common base class for all non-exit exceptions.'
    __class__ = Exception
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class FileExistsError(OSError):
    'File already exists.'
    __class__ = FileExistsError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class FileNotFoundError(OSError):
    'File not found.'
    __class__ = FileNotFoundError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class FloatingPointError(ArithmeticError):
    'Floating point operation failed.'
    __class__ = FloatingPointError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class FutureWarning(Warning):
    'Base class for warnings about constructs that will change semantically\nin the future.'
    __class__ = FutureWarning
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class GeneratorExit(BaseException):
    'Request that a generator exit.'
    __class__ = GeneratorExit
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class IOError(Exception):
    'Base class for I/O related errors.'
    __class__ = OSError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __reduce__(self):
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    characters_written = getset_descriptor()
    errno = member_descriptor()
    filename = member_descriptor()
    filename2 = member_descriptor()
    strerror = member_descriptor()
    winerror = member_descriptor()
class ImportError(Exception):
    "Import can't find module, or can't find name in module."
    __class__ = ImportError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __reduce__(self):
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    msg = member_descriptor()
    name = member_descriptor()
    path = member_descriptor()
class ImportWarning(Warning):
    'Base class for warnings about probable mistakes in module imports'
    __class__ = ImportWarning
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class IndentationError(SyntaxError):
    'Improper indentation.'
    __class__ = IndentationError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class IndexError(LookupError):
    'Sequence index out of range.'
    __class__ = IndexError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class InterruptedError(OSError):
    'Interrupted by signal.'
    __class__ = InterruptedError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class IsADirectoryError(OSError):
    "Operation doesn't work on directories."
    __class__ = IsADirectoryError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class KeyError(LookupError):
    'Mapping key not found.'
    __class__ = KeyError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class KeyboardInterrupt(BaseException):
    'Program interrupted by user.'
    __class__ = KeyboardInterrupt
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class LookupError(Exception):
    'Base class for lookup errors.'
    __class__ = LookupError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class MemoryError(Exception):
    'Out of memory.'
    __class__ = MemoryError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class ModuleNotFoundError(ImportError):
    'Module not found.'
    __class__ = ModuleNotFoundError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class NameError(Exception):
    'Name not found globally.'
    __class__ = NameError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class NotADirectoryError(OSError):
    'Operation only works on directories.'
    __class__ = NotADirectoryError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class NotImplemented:
    __class__ = NotImplementedType
    def __delattr__(name):
        'Implement delattr(self, name).'
        pass
    def __dir__():
        '__dir__() -> list\ndefault dir() implementation'
        pass
    def __eq__(value):
        'Return self==value.'
        pass
    def __format__(self, format_spec):
        'default object formatter'
        pass
    def __ge__(value):
        'Return self>=value.'
        pass
    def __getattribute__(name):
        'Return getattr(self, name).'
        pass
    def __gt__(value):
        'Return self>value.'
        pass
    def __hash__():
        'Return hash(self).'
        pass
    def __init__(*args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __le__(value):
        'Return self<=value.'
        pass
    def __lt__(value):
        'Return self<value.'
        pass
    def __ne__(value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __reduce__(self):
        pass
    def __reduce_ex__(self, protocol):
        'helper for pickle'
        pass
    def __repr__():
        'Return repr(self).'
        pass
    def __setattr__(name, value):
        'Implement setattr(self, name, value).'
        pass
    def __sizeof__():
        '__sizeof__() -> int\nsize of object in memory, in bytes'
        pass
    def __str__():
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class NotImplementedError(RuntimeError):
    "Method or function hasn't been implemented yet."
    __class__ = NotImplementedError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class OSError(Exception):
    'Base class for I/O related errors.'
    __class__ = OSError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __reduce__(self):
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    characters_written = getset_descriptor()
    errno = member_descriptor()
    filename = member_descriptor()
    filename2 = member_descriptor()
    strerror = member_descriptor()
    winerror = member_descriptor()
class OverflowError(ArithmeticError):
    'Result too large to be represented.'
    __class__ = OverflowError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class PendingDeprecationWarning(Warning):
    'Base class for warnings about features which will be deprecated\nin the future.'
    __class__ = PendingDeprecationWarning
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class PermissionError(OSError):
    'Not enough permissions.'
    __class__ = PermissionError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class ProcessLookupError(OSError):
    'Process not found.'
    __class__ = ProcessLookupError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class RecursionError(RuntimeError):
    'Recursion limit exceeded.'
    __class__ = RecursionError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class ReferenceError(Exception):
    'Weak ref proxy used after referent went away.'
    __class__ = ReferenceError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class ResourceWarning(Warning):
    'Base class for warnings about resource usage.'
    __class__ = ResourceWarning
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class RuntimeError(Exception):
    'Unspecified run-time error.'
    __class__ = RuntimeError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class RuntimeWarning(Warning):
    'Base class for warnings about dubious runtime behavior.'
    __class__ = RuntimeWarning
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class StopAsyncIteration(Exception):
    'Signal the end from iterator.__anext__().'
    __class__ = StopAsyncIteration
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class StopIteration(Exception):
    'Signal the end from iterator.__next__().'
    __class__ = StopIteration
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    value = member_descriptor()
class SyntaxError(Exception):
    'Invalid syntax.'
    __class__ = SyntaxError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    filename = member_descriptor()
    lineno = member_descriptor()
    msg = member_descriptor()
    offset = member_descriptor()
    print_file_and_line = member_descriptor()
    text = member_descriptor()
class SyntaxWarning(Warning):
    'Base class for warnings about dubious syntax.'
    __class__ = SyntaxWarning
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class SystemError(Exception):
    'Internal error in the Python interpreter.\n\nPlease report this to the Python maintainer, along with the traceback,\nthe Python version, and the hardware/OS platform and version.'
    __class__ = SystemError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class SystemExit(BaseException):
    'Request to exit from the interpreter.'
    __class__ = SystemExit
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    code = member_descriptor()
class TabError(IndentationError):
    'Improper mixture of spaces and tabs.'
    __class__ = TabError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class TimeoutError(OSError):
    'Timeout expired.'
    __class__ = TimeoutError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class TypeError(Exception):
    'Inappropriate argument type.'
    __class__ = TypeError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class UnboundLocalError(NameError):
    'Local name referenced but not bound to a value.'
    __class__ = UnboundLocalError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class UnicodeDecodeError(UnicodeError):
    'Unicode decoding error.'
    __class__ = UnicodeDecodeError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    encoding = member_descriptor()
    end = member_descriptor()
    object = member_descriptor()
    reason = member_descriptor()
    start = member_descriptor()
class UnicodeEncodeError(UnicodeError):
    'Unicode encoding error.'
    __class__ = UnicodeEncodeError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    encoding = member_descriptor()
    end = member_descriptor()
    object = member_descriptor()
    reason = member_descriptor()
    start = member_descriptor()
class UnicodeError(ValueError):
    'Unicode related error.'
    __class__ = UnicodeError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class UnicodeTranslateError(UnicodeError):
    'Unicode translation error.'
    __class__ = UnicodeTranslateError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    encoding = member_descriptor()
    end = member_descriptor()
    object = member_descriptor()
    reason = member_descriptor()
    start = member_descriptor()
class UnicodeWarning(Warning):
    'Base class for warnings about Unicode related problems, mostly\nrelated to conversion problems.'
    __class__ = UnicodeWarning
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class UserWarning(Warning):
    'Base class for warnings generated by user code.'
    __class__ = UserWarning
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class ValueError(Exception):
    'Inappropriate argument value (of correct type).'
    __class__ = ValueError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class Warning(Exception):
    'Base class for warning categories.'
    __class__ = Warning
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class WindowsError(Exception):
    'Base class for I/O related errors.'
    __class__ = OSError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __reduce__(self):
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    characters_written = getset_descriptor()
    errno = member_descriptor()
    filename = member_descriptor()
    filename2 = member_descriptor()
    strerror = member_descriptor()
    winerror = member_descriptor()
class ZeroDivisionError(ArithmeticError):
    'Second argument to a division or modulo operation was zero.'
    __class__ = ZeroDivisionError
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
def __build_class__(func, name):
    '__build_class__(func, name, *bases, metaclass=None, **kwds) -> class\n\nInternal helper function used by the class statement.'
    pass
__doc__ = "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
def __import__(name, globals, locals, fromlist, level):
    "__import__(name, globals=None, locals=None, fromlist=(), level=0) -> module\n\nImport a module. Because this function is meant for use by the Python\ninterpreter and not for general use it is better to use\nimportlib.import_module() to programmatically import a module.\n\nThe globals argument is only used to determine the context;\nthey are not modified.  The locals argument is unused.  The fromlist\nshould be a list of names to emulate ``from name import ...'', or an\nempty list to emulate ``import name''.\nWhen importing a module from a package, note that __import__('A.B', ...)\nreturns package A when fromlist is empty, but its submodule B when\nfromlist is not empty.  Level is used to determine whether to perform \nabsolute or relative imports. 0 is absolute while a positive number\nis the number of parent directories to search relative to the current module."
    pass
__name__ = 'builtins'
__package__ = ''
__spec__
def abs(x):
    'Return the absolute value of the argument.'
    pass
def all(iterable):
    'Return True if bool(x) is True for all values x in the iterable.\n\nIf the iterable is empty, return True.'
    pass
def any(iterable):
    'Return True if bool(x) is True for any x in the iterable.\n\nIf the iterable is empty, return False.'
    pass
def ascii(obj):
    'Return an ASCII-only representation of an object.\n\nAs repr(), return a string containing a printable representation of an\nobject, but escape the non-ASCII characters in the string returned by\nrepr() using \\\\x, \\\\u or \\\\U escapes. This generates a string similar\nto that returned by repr() in Python 2.'
    pass
def bin(number):
    "Return the binary representation of an integer.\n\n   >>> bin(2796202)\n   '0b1010101010101010101010'"
    pass
class bool(int):
    'bool(x) -> bool\n\nReturns True when the argument x is true, False otherwise.\nThe builtins True and False are the only two instances of the class bool.\nThe class bool is a subclass of the class int, and cannot be subclassed.'
    def __and__(self, value):
        'Return self&value.'
        pass
    __class__ = bool
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __or__(self, value):
        'Return self|value.'
        pass
    def __rand__(self, value):
        'Return value&self.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __ror__(self, value):
        'Return value|self.'
        pass
    def __rxor__(self, value):
        'Return value^self.'
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def __xor__(self, value):
        'Return self^value.'
        pass
    def from_bytes(self):
        "int.from_bytes(bytes, byteorder, *, signed=False) -> int\n\nReturn the integer represented by the given array of bytes.\n\nThe bytes argument must be a bytes-like object (e.g. bytes or bytearray).\n\nThe byteorder argument determines the byte order used to represent the\ninteger.  If byteorder is 'big', the most significant byte is at the\nbeginning of the byte array.  If byteorder is 'little', the most\nsignificant byte is at the end of the byte array.  To request the native\nbyte order of the host system, use `sys.byteorder' as the byte order value.\n\nThe signed keyword-only argument indicates whether two's complement is\nused to represent the integer."
        pass
class bytearray(object):
    'bytearray(iterable_of_ints) -> bytearray\nbytearray(string, encoding[, errors]) -> bytearray\nbytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer\nbytearray(int) -> bytes array of size given by the parameter initialized with null bytes\nbytearray() -> empty bytes array\n\nConstruct a mutable bytearray object from:\n  - an iterable yielding integers in range(256)\n  - a text string encoded using the specified encoding\n  - a bytes or a buffer object\n  - any object implementing the buffer API.\n  - an integer'
    def __add__(self, value):
        'Return self+value.'
        pass
    def __alloc__(self):
        'B.__alloc__() -> int\n\nReturn the number of bytes actually allocated.'
        pass
    __class__ = bytearray
    def __contains__(self, key):
        'Return key in self.'
        pass
    def __delitem__(self, key):
        'Delete self[key].'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getitem__(self, key):
        'Return self[key].'
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    __hash__
    def __iadd__(self, value):
        'Implement self+=value.'
        pass
    def __imul__(self, value):
        'Implement self*=value.'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __mod__(self, value):
        'Return self%value.'
        pass
    def __mul__(self, value):
        'Return self*value.n'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __reduce__(self):
        'Return state information for pickling.'
        pass
    def __reduce_ex__(self, proto=0):
        'Return state information for pickling.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __rmod__(self, value):
        'Return value%self.'
        pass
    def __rmul__(self, value):
        'Return self*value.'
        pass
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        pass
    def __sizeof__(self):
        'Returns the size of the bytearray object in memory, in bytes.'
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def append(self, item):
        'Append a single item to the end of the bytearray.\n\n  item\n    The item to be appended.'
        pass
    def capitalize(self):
        'B.capitalize() -> copy of B\n\nReturn a copy of B with only its first character capitalized (ASCII)\nand the rest lower-cased.'
        pass
    def center(self):
        'B.center(width[, fillchar]) -> copy of B\n\nReturn B centered in a string of length width.  Padding is\ndone using the specified fill character (default is a space).'
        pass
    def clear(self):
        'Remove all items from the bytearray.'
        pass
    def copy(self):
        'Return a copy of B.'
        pass
    def count(self, x):
        'B.count(sub[, start[, end]]) -> int\n\nReturn the number of non-overlapping occurrences of subsection sub in\nbytes B[start:end].  Optional arguments start and end are interpreted\nas in slice notation.'
        pass
    def decode(self, encoding='utf-8', errors='strict'):
        "Decode the bytearray using the codec registered for encoding.\n\n  encoding\n    The encoding with which to decode the bytearray.\n  errors\n    The error handling scheme to use for the handling of decoding errors.\n    The default is 'strict' meaning that decoding errors raise a\n    UnicodeDecodeError. Other possible values are 'ignore' and 'replace'\n    as well as any other name registered with codecs.register_error that\n    can handle UnicodeDecodeErrors."
        pass
    def endswith(self, suffix, start=0, end=-1):
        'B.endswith(suffix[, start[, end]]) -> bool\n\nReturn True if B ends with the specified suffix, False otherwise.\nWith optional start, test B beginning at that position.\nWith optional end, stop comparing B at that position.\nsuffix can also be a tuple of bytes to try.'
        pass
    def expandtabs(self, tabsize=8):
        'B.expandtabs(tabsize=8) -> copy of B\n\nReturn a copy of B where all tab characters are expanded using spaces.\nIf tabsize is not given, a tab size of 8 characters is assumed.'
        pass
    def extend(self, iterable_of_ints):
        'Append all the items from the iterator or sequence to the end of the bytearray.\n\n  iterable_of_ints\n    The iterable of items to append.'
        pass
    def find(self, sub, start=0, end=-1):
        'B.find(sub[, start[, end]]) -> int\n\nReturn the lowest index in B where subsection sub is found,\nsuch that sub is contained within B[start,end].  Optional\narguments start and end are interpreted as in slice notation.\n\nReturn -1 on failure.'
        pass
    def fromhex(string):
        "Create a bytearray object from a string of hexadecimal numbers.\n\nSpaces between two numbers are accepted.\nExample: bytearray.fromhex('B9 01EF') -> bytearray(b'\\\\xb9\\\\x01\\\\xef')"
        pass
    def hex(self):
        "B.hex() -> string\n\nCreate a string of hexadecimal numbers from a bytearray object.\nExample: bytearray([0xb9, 0x01, 0xef]).hex() -> 'b901ef'."
        pass
    def index(self, v):
        'B.index(sub[, start[, end]]) -> int\n\nReturn the lowest index in B where subsection sub is found,\nsuch that sub is contained within B[start,end].  Optional\narguments start and end are interpreted as in slice notation.\n\nRaises ValueError when the subsection is not found.'
        pass
    def insert(self, index, item):
        'Insert a single item into the bytearray before the given index.\n\n  index\n    The index where the value is to be inserted.\n  item\n    The item to be inserted.'
        pass
    def isalnum(self):
        'B.isalnum() -> bool\n\nReturn True if all characters in B are alphanumeric\nand there is at least one character in B, False otherwise.'
        pass
    def isalpha(self):
        'B.isalpha() -> bool\n\nReturn True if all characters in B are alphabetic\nand there is at least one character in B, False otherwise.'
        pass
    def isdigit(self):
        'B.isdigit() -> bool\n\nReturn True if all characters in B are digits\nand there is at least one character in B, False otherwise.'
        pass
    def islower(self):
        'B.islower() -> bool\n\nReturn True if all cased characters in B are lowercase and there is\nat least one cased character in B, False otherwise.'
        pass
    def isspace(self):
        'B.isspace() -> bool\n\nReturn True if all characters in B are whitespace\nand there is at least one character in B, False otherwise.'
        pass
    def istitle(self):
        'B.istitle() -> bool\n\nReturn True if B is a titlecased string and there is at least one\ncharacter in B, i.e. uppercase characters may only follow uncased\ncharacters and lowercase characters only cased ones. Return False\notherwise.'
        pass
    def isupper(self):
        'B.isupper() -> bool\n\nReturn True if all cased characters in B are uppercase and there is\nat least one cased character in B, False otherwise.'
        pass
    def join(self, iterable_of_bytes):
        'Concatenate any number of bytes/bytearray objects.\n\nThe bytearray whose method is called is inserted in between each pair.\n\nThe result is returned as a new bytearray object.'
        pass
    def ljust(self):
        'B.ljust(width[, fillchar]) -> copy of B\n\nReturn B left justified in a string of length width. Padding is\ndone using the specified fill character (default is a space).'
        pass
    def lower(self):
        'B.lower() -> copy of B\n\nReturn a copy of B with all ASCII characters converted to lowercase.'
        pass
    def lstrip(self, bytes=None):
        'Strip leading bytes contained in the argument.\n\nIf the argument is omitted or None, strip leading ASCII whitespace.'
        pass
    def maketrans(frm, to):
        'Return a translation table useable for the bytes or bytearray translate method.\n\nThe returned table will be one where each byte in frm is mapped to the byte at\nthe same position in to.\n\nThe bytes objects frm and to must be of the same length.'
        pass
    def partition(self, sep):
        'Partition the bytearray into three parts using the given separator.\n\nThis will search for the separator sep in the bytearray. If the separator is\nfound, returns a 3-tuple containing the part before the separator, the\nseparator itself, and the part after it.\n\nIf the separator is not found, returns a 3-tuple containing the original\nbytearray object and two empty bytearray objects.'
        pass
    def pop(self, index=-1):
        'Remove and return a single item from B.\n\n  index\n    The index from where to remove the item.\n    -1 (the default value) means remove the last item.\n\nIf no index argument is given, will pop the last item.'
        pass
    def remove(self, value):
        'Remove the first occurrence of a value in the bytearray.\n\n  value\n    The value to remove.'
        pass
    def replace(self, old, new, count=-1):
        'Return a copy with all occurrences of substring old replaced by new.\n\n  count\n    Maximum number of occurrences to replace.\n    -1 (the default value) means replace all occurrences.\n\nIf the optional argument count is given, only the first count occurrences are\nreplaced.'
        pass
    def reverse(self):
        'Reverse the order of the values in B in place.'
        pass
    def rfind(self, sub, start=0, end=-1):
        'B.rfind(sub[, start[, end]]) -> int\n\nReturn the highest index in B where subsection sub is found,\nsuch that sub is contained within B[start,end].  Optional\narguments start and end are interpreted as in slice notation.\n\nReturn -1 on failure.'
        pass
    def rindex(self, sub, start=0, end=-1):
        'B.rindex(sub[, start[, end]]) -> int\n\nReturn the highest index in B where subsection sub is found,\nsuch that sub is contained within B[start,end].  Optional\narguments start and end are interpreted as in slice notation.\n\nRaise ValueError when the subsection is not found.'
        pass
    def rjust(self):
        'B.rjust(width[, fillchar]) -> copy of B\n\nReturn B right justified in a string of length width. Padding is\ndone using the specified fill character (default is a space)'
        pass
    def rpartition(self, sep):
        'Partition the bytes into three parts using the given separator.\n\nThis will search for the separator sep in the bytearray, starting and the end.\nIf the separator is found, returns a 3-tuple containing the part before the\nseparator, the separator itself, and the part after it.\n\nIf the separator is not found, returns a 3-tuple containing two empty bytearray\nobjects and the original bytearray object.'
        pass
    def rsplit(self, sep=None, maxsplit=-1):
        'Return a list of the sections in the bytearray, using sep as the delimiter.\n\n  sep\n    The delimiter according which to split the bytearray.\n    None (the default value) means split on ASCII whitespace characters\n    (space, tab, return, newline, formfeed, vertical tab).\n  maxsplit\n    Maximum number of splits to do.\n    -1 (the default value) means no limit.\n\nSplitting is done starting at the end of the bytearray and working to the front.'
        pass
    def rstrip(self, bytes=None):
        'Strip trailing bytes contained in the argument.\n\nIf the argument is omitted or None, strip trailing ASCII whitespace.'
        pass
    def split(self, sep=None, maxsplit=-1):
        'Return a list of the sections in the bytearray, using sep as the delimiter.\n\n  sep\n    The delimiter according which to split the bytearray.\n    None (the default value) means split on ASCII whitespace characters\n    (space, tab, return, newline, formfeed, vertical tab).\n  maxsplit\n    Maximum number of splits to do.\n    -1 (the default value) means no limit.'
        pass
    def splitlines(self, keepends=False):
        'Return a list of the lines in the bytearray, breaking at line boundaries.\n\nLine breaks are not included in the resulting list unless keepends is given and\ntrue.'
        pass
    def startswith(self, prefix, start=0, end=-1):
        'B.startswith(prefix[, start[, end]]) -> bool\n\nReturn True if B starts with the specified prefix, False otherwise.\nWith optional start, test B beginning at that position.\nWith optional end, stop comparing B at that position.\nprefix can also be a tuple of bytes to try.'
        pass
    def strip(self, bytes=None):
        'Strip leading and trailing bytes contained in the argument.\n\nIf the argument is omitted or None, strip leading and trailing ASCII whitespace.'
        pass
    def swapcase(self):
        'B.swapcase() -> copy of B\n\nReturn a copy of B with uppercase ASCII characters converted\nto lowercase ASCII and vice versa.'
        pass
    def title(self):
        'B.title() -> copy of B\n\nReturn a titlecased version of B, i.e. ASCII words start with uppercase\ncharacters, all remaining cased characters have lowercase.'
        pass
    def translate(self, table, delete=b''):
        'Return a copy with each character mapped by the given translation table.\n\n  table\n    Translation table, which must be a bytes object of length 256.\n\nAll characters occurring in the optional argument delete are removed.\nThe remaining characters are mapped through the given translation table.'
        pass
    def upper(self):
        'B.upper() -> copy of B\n\nReturn a copy of B with all ASCII characters converted to uppercase.'
        pass
    def zfill(self, width):
        'B.zfill(width) -> copy of B\n\nPad a numeric string B with zeros on the left, to fill a field\nof the specified width.  B is never truncated.'
        pass
class bytes(object):
    'bytes(iterable_of_ints) -> bytes\nbytes(string, encoding[, errors]) -> bytes\nbytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer\nbytes(int) -> bytes object of size given by the parameter initialized with null bytes\nbytes() -> empty bytes object\n\nConstruct an immutable array of bytes from:\n  - an iterable yielding integers in range(256)\n  - a text string encoded using the specified encoding\n  - any object implementing the buffer API.\n  - an integer'
    def __add__(self, value):
        'Return self+value.'
        pass
    __class__ = bytes
    def __contains__(self, key):
        'Return key in self.'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getitem__(self, key):
        'Return self[key].'
        pass
    def __getnewargs__(self):
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __mod__(self, value):
        'Return self%value.'
        pass
    def __mul__(self, value):
        'Return self*value.n'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __rmod__(self, value):
        'Return value%self.'
        pass
    def __rmul__(self, value):
        'Return self*value.'
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def capitalize(self):
        'B.capitalize() -> copy of B\n\nReturn a copy of B with only its first character capitalized (ASCII)\nand the rest lower-cased.'
        pass
    def center(self):
        'B.center(width[, fillchar]) -> copy of B\n\nReturn B centered in a string of length width.  Padding is\ndone using the specified fill character (default is a space).'
        pass
    def count(self, x):
        'B.count(sub[, start[, end]]) -> int\n\nReturn the number of non-overlapping occurrences of subsection sub in\nbytes B[start:end].  Optional arguments start and end are interpreted\nas in slice notation.'
        pass
    def decode(self, encoding='utf-8', errors='strict'):
        "Decode the bytes using the codec registered for encoding.\n\n  encoding\n    The encoding with which to decode the bytes.\n  errors\n    The error handling scheme to use for the handling of decoding errors.\n    The default is 'strict' meaning that decoding errors raise a\n    UnicodeDecodeError. Other possible values are 'ignore' and 'replace'\n    as well as any other name registered with codecs.register_error that\n    can handle UnicodeDecodeErrors."
        pass
    def endswith(self, suffix, start=0, end=-1):
        'B.endswith(suffix[, start[, end]]) -> bool\n\nReturn True if B ends with the specified suffix, False otherwise.\nWith optional start, test B beginning at that position.\nWith optional end, stop comparing B at that position.\nsuffix can also be a tuple of bytes to try.'
        pass
    def expandtabs(self, tabsize=8):
        'B.expandtabs(tabsize=8) -> copy of B\n\nReturn a copy of B where all tab characters are expanded using spaces.\nIf tabsize is not given, a tab size of 8 characters is assumed.'
        pass
    def find(self, sub, start=0, end=-1):
        'B.find(sub[, start[, end]]) -> int\n\nReturn the lowest index in B where subsection sub is found,\nsuch that sub is contained within B[start,end].  Optional\narguments start and end are interpreted as in slice notation.\n\nReturn -1 on failure.'
        pass
    def fromhex(string):
        "Create a bytes object from a string of hexadecimal numbers.\n\nSpaces between two numbers are accepted.\nExample: bytes.fromhex('B9 01EF') -> b'\\\\xb9\\\\x01\\\\xef'."
        pass
    def hex(self):
        "B.hex() -> string\n\nCreate a string of hexadecimal numbers from a bytes object.\nExample: b'\\xb9\\x01\\xef'.hex() -> 'b901ef'."
        pass
    def index(self, v):
        'B.index(sub[, start[, end]]) -> int\n\nReturn the lowest index in B where subsection sub is found,\nsuch that sub is contained within B[start,end].  Optional\narguments start and end are interpreted as in slice notation.\n\nRaises ValueError when the subsection is not found.'
        pass
    def isalnum(self):
        'B.isalnum() -> bool\n\nReturn True if all characters in B are alphanumeric\nand there is at least one character in B, False otherwise.'
        pass
    def isalpha(self):
        'B.isalpha() -> bool\n\nReturn True if all characters in B are alphabetic\nand there is at least one character in B, False otherwise.'
        pass
    def isdigit(self):
        'B.isdigit() -> bool\n\nReturn True if all characters in B are digits\nand there is at least one character in B, False otherwise.'
        pass
    def islower(self):
        'B.islower() -> bool\n\nReturn True if all cased characters in B are lowercase and there is\nat least one cased character in B, False otherwise.'
        pass
    def isspace(self):
        'B.isspace() -> bool\n\nReturn True if all characters in B are whitespace\nand there is at least one character in B, False otherwise.'
        pass
    def istitle(self):
        'B.istitle() -> bool\n\nReturn True if B is a titlecased string and there is at least one\ncharacter in B, i.e. uppercase characters may only follow uncased\ncharacters and lowercase characters only cased ones. Return False\notherwise.'
        pass
    def isupper(self):
        'B.isupper() -> bool\n\nReturn True if all cased characters in B are uppercase and there is\nat least one cased character in B, False otherwise.'
        pass
    def join(self, iterable_of_bytes):
        "Concatenate any number of bytes objects.\n\nThe bytes whose method is called is inserted in between each pair.\n\nThe result is returned as a new bytes object.\n\nExample: b'.'.join([b'ab', b'pq', b'rs']) -> b'ab.pq.rs'."
        pass
    def ljust(self):
        'B.ljust(width[, fillchar]) -> copy of B\n\nReturn B left justified in a string of length width. Padding is\ndone using the specified fill character (default is a space).'
        pass
    def lower(self):
        'B.lower() -> copy of B\n\nReturn a copy of B with all ASCII characters converted to lowercase.'
        pass
    def lstrip(self, bytes=None):
        'Strip leading bytes contained in the argument.\n\nIf the argument is omitted or None, strip leading  ASCII whitespace.'
        pass
    def maketrans(frm, to):
        'Return a translation table useable for the bytes or bytearray translate method.\n\nThe returned table will be one where each byte in frm is mapped to the byte at\nthe same position in to.\n\nThe bytes objects frm and to must be of the same length.'
        pass
    def partition(self, sep):
        'Partition the bytes into three parts using the given separator.\n\nThis will search for the separator sep in the bytes. If the separator is found,\nreturns a 3-tuple containing the part before the separator, the separator\nitself, and the part after it.\n\nIf the separator is not found, returns a 3-tuple containing the original bytes\nobject and two empty bytes objects.'
        pass
    def replace(self, old, new, count=-1):
        'Return a copy with all occurrences of substring old replaced by new.\n\n  count\n    Maximum number of occurrences to replace.\n    -1 (the default value) means replace all occurrences.\n\nIf the optional argument count is given, only the first count occurrences are\nreplaced.'
        pass
    def rfind(self, sub, start=0, end=-1):
        'B.rfind(sub[, start[, end]]) -> int\n\nReturn the highest index in B where subsection sub is found,\nsuch that sub is contained within B[start,end].  Optional\narguments start and end are interpreted as in slice notation.\n\nReturn -1 on failure.'
        pass
    def rindex(self, sub, start=0, end=-1):
        'B.rindex(sub[, start[, end]]) -> int\n\nReturn the highest index in B where subsection sub is found,\nsuch that sub is contained within B[start,end].  Optional\narguments start and end are interpreted as in slice notation.\n\nRaise ValueError when the subsection is not found.'
        pass
    def rjust(self):
        'B.rjust(width[, fillchar]) -> copy of B\n\nReturn B right justified in a string of length width. Padding is\ndone using the specified fill character (default is a space)'
        pass
    def rpartition(self, sep):
        'Partition the bytes into three parts using the given separator.\n\nThis will search for the separator sep in the bytes, starting and the end. If\nthe separator is found, returns a 3-tuple containing the part before the\nseparator, the separator itself, and the part after it.\n\nIf the separator is not found, returns a 3-tuple containing two empty bytes\nobjects and the original bytes object.'
        pass
    def rsplit(self, sep=None, maxsplit=-1):
        'Return a list of the sections in the bytes, using sep as the delimiter.\n\n  sep\n    The delimiter according which to split the bytes.\n    None (the default value) means split on ASCII whitespace characters\n    (space, tab, return, newline, formfeed, vertical tab).\n  maxsplit\n    Maximum number of splits to do.\n    -1 (the default value) means no limit.\n\nSplitting is done starting at the end of the bytes and working to the front.'
        pass
    def rstrip(self, bytes=None):
        'Strip trailing bytes contained in the argument.\n\nIf the argument is omitted or None, strip trailing ASCII whitespace.'
        pass
    def split(self, sep=None, maxsplit=-1):
        'Return a list of the sections in the bytes, using sep as the delimiter.\n\n  sep\n    The delimiter according which to split the bytes.\n    None (the default value) means split on ASCII whitespace characters\n    (space, tab, return, newline, formfeed, vertical tab).\n  maxsplit\n    Maximum number of splits to do.\n    -1 (the default value) means no limit.'
        pass
    def splitlines(self, keepends=False):
        'Return a list of the lines in the bytes, breaking at line boundaries.\n\nLine breaks are not included in the resulting list unless keepends is given and\ntrue.'
        pass
    def startswith(self, prefix, start=0, end=-1):
        'B.startswith(prefix[, start[, end]]) -> bool\n\nReturn True if B starts with the specified prefix, False otherwise.\nWith optional start, test B beginning at that position.\nWith optional end, stop comparing B at that position.\nprefix can also be a tuple of bytes to try.'
        pass
    def strip(self, bytes=None):
        'Strip leading and trailing bytes contained in the argument.\n\nIf the argument is omitted or None, strip leading and trailing ASCII whitespace.'
        pass
    def swapcase(self):
        'B.swapcase() -> copy of B\n\nReturn a copy of B with uppercase ASCII characters converted\nto lowercase ASCII and vice versa.'
        pass
    def title(self):
        'B.title() -> copy of B\n\nReturn a titlecased version of B, i.e. ASCII words start with uppercase\ncharacters, all remaining cased characters have lowercase.'
        pass
    def translate(self, table, delete=b''):
        'Return a copy with each character mapped by the given translation table.\n\n  table\n    Translation table, which must be a bytes object of length 256.\n\nAll characters occurring in the optional argument delete are removed.\nThe remaining characters are mapped through the given translation table.'
        pass
    def upper(self):
        'B.upper() -> copy of B\n\nReturn a copy of B with all ASCII characters converted to uppercase.'
        pass
    def zfill(self, width):
        'B.zfill(width) -> copy of B\n\nPad a numeric string B with zeros on the left, to fill a field\nof the specified width.  B is never truncated.'
        pass
def callable(obj):
    'Return whether the object is callable (i.e., some kind of function).\n\nNote that classes are callable, as are instances of classes with a\n__call__() method.'
    pass
def chr(i):
    'Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.'
    pass
class classmethod(object):
    'classmethod(function) -> method\n\nConvert a function to be a class method.\n\nA class method receives the class as implicit first argument,\njust like an instance method receives the instance.\nTo declare a class method, use this idiom:\n\n  class C:\n      @classmethod\n      def f(cls, arg1, arg2, ...):\n          ...\n\nIt can be called either on the class (e.g. C.f()) or on an instance\n(e.g. C().f()).  The instance is ignored except for its class.\nIf a class method is called for a derived class, the derived class\nobject is passed as the implied first argument.\n\nClass methods are different than C++ or Java static methods.\nIf you want those, see the staticmethod builtin.'
    __class__ = classmethod
    __dict__ = {}
    __func__ = member_descriptor()
    def __get__(self, instance, owner):
        'Return an attribute of instance, which is of type owner.'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    __isabstractmethod__ = getset_descriptor()
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
def compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1):
    "Compile source into a code object that can be executed by exec() or eval().\n\nThe source code may represent a Python module, statement or expression.\nThe filename will be used for run-time error messages.\nThe mode must be 'exec' to compile a module, 'single' to compile a\nsingle (interactive) statement, or 'eval' to compile an expression.\nThe flags argument, if present, controls which future statements influence\nthe compilation of the code.\nThe dont_inherit argument, if true, stops the compilation inheriting\nthe effects of any future statements in effect in the code calling\ncompile; if absent or false these statements do influence the compilation,\nin addition to any features explicitly specified."
    pass
class complex(object):
    'complex(real[, imag]) -> complex number\n\nCreate a complex number from a real part and an optional imaginary part.\nThis is equivalent to (real + imag*1j) where imag defaults to 0.'
    def __abs__(self):
        'abs(self)'
        pass
    def __add__(self, value):
        'Return self+value.'
        pass
    def __bool__(self):
        'self != 0'
        pass
    __class__ = complex
    def __divmod__(self, value):
        'Return divmod(self, value).'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __float__(self):
        'float(self)'
        pass
    def __floordiv__(self, value):
        'Return self//value.'
        pass
    def __format__(self, format_spec):
        'complex.__format__() -> str\n\nConvert to a string according to format_spec.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getnewargs__(self):
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __int__(self):
        'int(self)'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __mod__(self, value):
        'Return self%value.'
        pass
    def __mul__(self, value):
        'Return self*value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __neg__(self):
        '-self'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __pos__(self):
        '+self'
        pass
    def __pow__(self, value, mod=None):
        'Return pow(self, value, mod).'
        pass
    def __radd__(self, value):
        'Return value+self.'
        pass
    def __rdivmod__(self, value):
        'Return divmod(value, self).'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __rfloordiv__(self, value):
        'Return value//self.'
        pass
    def __rmod__(self, value):
        'Return value%self.'
        pass
    def __rmul__(self, value):
        'Return value*self.'
        pass
    def __rpow__(self, value, mod=None):
        'Return pow(value, self, mod).'
        pass
    def __rsub__(self, value):
        'Return value-self.'
        pass
    def __rtruediv__(self, value):
        'Return value/self.'
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __sub__(self, value):
        'Return self-value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def __truediv__(self, value):
        'Return self/value.'
        pass
    def conjugate(self):
        'complex.conjugate() -> complex\n\nReturn the complex conjugate of its argument. (3-4j).conjugate() == 3+4j.'
        pass
    imag = member_descriptor()
    real = member_descriptor()
def copyright():
    'interactive prompt objects for printing the license text, a list of\n    contributors and the copyright notice.'
    pass
def credits():
    'interactive prompt objects for printing the license text, a list of\n    contributors and the copyright notice.'
    pass
def delattr(obj, name):
    "Deletes the named attribute from the given object.\n\ndelattr(x, 'y') is equivalent to ``del x.y''"
    pass
class dict(object):
    "dict() -> new empty dictionary\ndict(mapping) -> new dictionary initialized from a mapping object's\n    (key, value) pairs\ndict(iterable) -> new dictionary initialized as if via:\n    d = {}\n    for k, v in iterable:\n        d[k] = v\ndict(**kwargs) -> new dictionary initialized with the name=value pairs\n    in the keyword argument list.  For example:  dict(one=1, two=2)"
    __class__ = dict
    def __contains__(self, key):
        'True if D has a key k, else False.'
        pass
    def __delitem__(self, key):
        'Delete self[key].'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getitem__(self, index):
        'x.__getitem__(y) <==> x[y]'
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    __hash__
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        pass
    def __sizeof__(self):
        'D.__sizeof__() -> size of D in memory, in bytes'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def clear(self):
        'D.clear() -> None.  Remove all items from D.'
        pass
    def copy(self):
        'D.copy() -> a shallow copy of D'
        pass
    def fromkeys(iterable, value=None):
        'Returns a new dict with keys from iterable and values equal to value.'
        pass
    def get(self):
        'D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.'
        pass
    def items(self):
        "D.items() -> a set-like object providing a view on D's items"
        pass
    def keys(self):
        "D.keys() -> a set-like object providing a view on D's keys"
        pass
    def pop(self):
        'D.pop(k[,d]) -> v, remove specified key and return the corresponding value.\nIf key is not found, d is returned if given, otherwise KeyError is raised'
        pass
    def popitem(self):
        'D.popitem() -> (k, v), remove and return some (key, value) pair as a\n2-tuple; but raise KeyError if D is empty.'
        pass
    def setdefault(self):
        'D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D'
        pass
    def update(self):
        'D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.\nIf E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]\nIf E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v\nIn either case, this is followed by: for k in F:  D[k] = F[k]'
        pass
    def values(self):
        "D.values() -> an object providing a view on D's values"
        pass
def dir(object):
    "dir([object]) -> list of strings\n\nIf called without an argument, return the names in the current scope.\nElse, return an alphabetized list of names comprising (some of) the attributes\nof the given object, and of attributes reachable from it.\nIf the object supplies a method named __dir__, it will be used; otherwise\nthe default dir() logic is used and returns:\n  for a module object: the module's attributes.\n  for a class object:  its attributes, and recursively the attributes\n    of its bases.\n  for any other object: its attributes, its class's attributes, and\n    recursively the attributes of its class's base classes."
    pass
def divmod(x, y):
    'Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.'
    pass
class enumerate(object):
    'enumerate(iterable[, start]) -> iterator for index, value of iterable\n\nReturn an enumerate object.  iterable must be another object that supports\niteration.  The enumerate object yields pairs containing a count (from\nstart, which defaults to zero) and a value yielded by the iterable argument.\nenumerate is useful for obtaining an indexed list:\n    (0, seq[0]), (1, seq[1]), (2, seq[2]), ...'
    __class__ = enumerate
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __next__(self):
        'Implement next(self).'
        pass
    def __reduce__(self):
        'Return state information for pickling.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
def eval(source, globals=None, locals=None):
    'Evaluate the given source in the context of globals and locals.\n\nThe source may be a string representing a Python expression\nor a code object as returned by compile().\nThe globals must be a dictionary and locals can be any mapping,\ndefaulting to the current globals and locals.\nIf only globals is given, locals defaults to it.'
    pass
def exec(source, globals=None, locals=None):
    'Execute the given source in the context of globals and locals.\n\nThe source may be a string representing one or more Python statements\nor a code object as returned by compile().\nThe globals must be a dictionary and locals can be any mapping,\ndefaulting to the current globals and locals.\nIf only globals is given, locals defaults to it.'
    pass
def exit(code=None):
    pass
class filter(object):
    'filter(function or None, iterable) --> filter object\n\nReturn an iterator yielding those items of iterable for which function(item)\nis true. If function is None, return the items that are true.'
    __class__ = filter
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __next__(self):
        'Implement next(self).'
        pass
    def __reduce__(self):
        'Return state information for pickling.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class float(object):
    'float(x) -> floating point number\n\nConvert a string or number to a floating point number, if possible.'
    def __abs__(self):
        'abs(self)'
        pass
    def __add__(self, value):
        'Return self+value.'
        pass
    def __bool__(self):
        'self != 0'
        pass
    __class__ = float
    def __divmod__(self, value):
        'Return divmod(self, value).'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __float__(self):
        'float(self)'
        pass
    def __floordiv__(self, value):
        'Return self//value.'
        pass
    def __format__(self, format_spec):
        'float.__format__(format_spec) -> string\n\nFormats the float according to format_spec.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getformat__(self):
        "float.__getformat__(typestr) -> string\n\nYou probably don't want to use this function.  It exists mainly to be\nused in Python's test suite.\n\ntypestr must be 'double' or 'float'.  This function returns whichever of\n'unknown', 'IEEE, big-endian' or 'IEEE, little-endian' best describes the\nformat of floating point numbers used by the C type named by typestr."
        pass
    def __getnewargs__(self):
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __int__(self):
        'int(self)'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __mod__(self, value):
        'Return self%value.'
        pass
    def __mul__(self, value):
        'Return self*value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __neg__(self):
        '-self'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __pos__(self):
        '+self'
        pass
    def __pow__(self, value, mod=None):
        'Return pow(self, value, mod).'
        pass
    def __radd__(self, value):
        'Return value+self.'
        pass
    def __rdivmod__(self, value):
        'Return divmod(value, self).'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __rfloordiv__(self, value):
        'Return value//self.'
        pass
    def __rmod__(self, value):
        'Return value%self.'
        pass
    def __rmul__(self, value):
        'Return value*self.'
        pass
    def __round__(self, ndigits=0):
        'Return the Integral closest to x, rounding half toward even.\nWhen an argument is passed, work like built-in round(x, ndigits).'
        pass
    def __rpow__(self, value, mod=None):
        'Return pow(value, self, mod).'
        pass
    def __rsub__(self, value):
        'Return value-self.'
        pass
    def __rtruediv__(self, value):
        'Return value/self.'
        pass
    def __setformat__(self):
        "float.__setformat__(typestr, fmt) -> None\n\nYou probably don't want to use this function.  It exists mainly to be\nused in Python's test suite.\n\ntypestr must be 'double' or 'float'.  fmt must be one of 'unknown',\n'IEEE, big-endian' or 'IEEE, little-endian', and in addition can only be\none of the latter two if it appears to match the underlying C reality.\n\nOverride the automatic determination of C-level floating point type.\nThis affects how floats are converted to and from binary strings."
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __sub__(self, value):
        'Return self-value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def __truediv__(self, value):
        'Return self/value.'
        pass
    def __trunc__(self):
        'Return the Integral closest to x between 0 and x.'
        pass
    def as_integer_ratio(self):
        'float.as_integer_ratio() -> (int, int)\n\nReturn a pair of integers, whose ratio is exactly equal to the original\nfloat and with a positive denominator.\nRaise OverflowError on infinities and a ValueError on NaNs.\n\n>>> (10.0).as_integer_ratio()\n(10, 1)\n>>> (0.0).as_integer_ratio()\n(0, 1)\n>>> (-.25).as_integer_ratio()\n(-1, 4)'
        pass
    def conjugate(self):
        'Return self, the complex conjugate of any float.'
        pass
    def fromhex(self):
        "float.fromhex(string) -> float\n\nCreate a floating-point number from a hexadecimal string.\n>>> float.fromhex('0x1.ffffp10')\n2047.984375\n>>> float.fromhex('-0x1p-1074')\n-5e-324"
        pass
    def hex(self):
        "float.hex() -> string\n\nReturn a hexadecimal representation of a floating-point number.\n>>> (-0.1).hex()\n'-0x1.999999999999ap-4'\n>>> 3.14159.hex()\n'0x1.921f9f01b866ep+1'"
        pass
    imag = getset_descriptor()
    def is_integer(self):
        'Return True if the float is an integer.'
        pass
    real = getset_descriptor()
def format(value, format_spec=''):
    "Return value.__format__(format_spec)\n\nformat_spec defaults to the empty string.\nSee the Format Specification Mini-Language section of help('FORMATTING') for\ndetails."
    pass
class frozenset(object):
    'frozenset() -> empty frozenset object\nfrozenset(iterable) -> frozenset object\n\nBuild an immutable unordered collection of unique elements.'
    def __and__(self, value):
        'Return self&value.'
        pass
    __class__ = frozenset
    def __contains__(self, value):
        'x.__contains__(y) <==> y in x.'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __or__(self, value):
        'Return self|value.'
        pass
    def __rand__(self, value):
        'Return value&self.'
        pass
    def __reduce__(self):
        'Return state information for pickling.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __ror__(self, value):
        'Return value|self.'
        pass
    def __rsub__(self, value):
        'Return value-self.'
        pass
    def __rxor__(self, value):
        'Return value^self.'
        pass
    def __sizeof__(self):
        'S.__sizeof__() -> size of S in memory, in bytes'
        pass
    def __sub__(self, value):
        'Return self-value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def __xor__(self, value):
        'Return self^value.'
        pass
    def copy(self):
        'Return a shallow copy of a set.'
        pass
    def difference(self):
        'Return the difference of two or more sets as a new set.\n\n(i.e. all elements that are in this set but not the others.)'
        pass
    def intersection(self):
        'Return the intersection of two sets as a new set.\n\n(i.e. all elements that are in both sets.)'
        pass
    def isdisjoint(self):
        'Return True if two sets have a null intersection.'
        pass
    def issubset(self):
        'Report whether another set contains this set.'
        pass
    def issuperset(self):
        'Report whether this set contains another set.'
        pass
    def symmetric_difference(self):
        'Return the symmetric difference of two sets as a new set.\n\n(i.e. all elements that are in exactly one of the sets.)'
        pass
    def union(self):
        'Return the union of sets as a new set.\n\n(i.e. all elements that are in either set.)'
        pass
def getattr(object, name, default):
    "getattr(object, name[, default]) -> value\n\nGet a named attribute from an object; getattr(x, 'y') is equivalent to x.y.\nWhen a default argument is given, it is returned when the attribute doesn't\nexist; without it, an exception is raised in that case."
    pass
def globals():
    "Return the dictionary containing the current scope's global variables.\n\nNOTE: Updates to this dictionary *will* affect name lookups in the current\nglobal scope and vice-versa."
    pass
def hasattr(obj, name):
    'Return whether the object has an attribute with the given name.\n\nThis is done by calling getattr(obj, name) and catching AttributeError.'
    pass
def hash(obj):
    'Return the hash value for the given object.\n\nTwo objects that compare equal must also have the same hash value, but the\nreverse is not necessarily true.'
    pass
def help(*args, **kwds):
    "Define the builtin 'help'.\n\n    This is a wrapper around pydoc.help that provides a helpful message\n    when 'help' is typed at the Python interactive prompt.\n\n    Calling help() at the Python prompt starts an interactive help session.\n    Calling help(thing) prints help for the python object 'thing'.\n    "
    pass
def hex(number):
    "Return the hexadecimal representation of an integer.\n\n   >>> hex(12648430)\n   '0xc0ffee'"
    pass
def id(obj):
    "Return the identity of an object.\n\nThis is guaranteed to be unique among simultaneously existing objects.\n(CPython uses the object's memory address.)"
    pass
def input(prompt=None):
    'Read a string from standard input.  The trailing newline is stripped.\n\nThe prompt string, if given, is printed to standard output without a\ntrailing newline before reading input.\n\nIf the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.\nOn *nix systems, readline is used if available.'
    pass
class int(object):
    "int(x=0) -> integer\nint(x, base=10) -> integer\n\nConvert a number or string to an integer, or return 0 if no arguments\nare given.  If x is a number, return x.__int__().  For floating point\nnumbers, this truncates towards zero.\n\nIf x is not a number or if base is given, then x must be a string,\nbytes, or bytearray instance representing an integer literal in the\ngiven base.  The literal can be preceded by '+' or '-' and be surrounded\nby whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.\nBase 0 means to interpret the base from the string as an integer literal.\n>>> int('0b100', base=0)\n4"
    def __abs__(self):
        'abs(self)'
        pass
    def __add__(self, value):
        'Return self+value.'
        pass
    def __and__(self, value):
        'Return self&value.'
        pass
    def __bool__(self):
        'self != 0'
        pass
    def __ceil__(self):
        'Ceiling of an Integral returns itself.'
        pass
    __class__ = int
    def __divmod__(self, value):
        'Return divmod(self, value).'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __float__(self):
        'float(self)'
        pass
    def __floor__(self):
        'Flooring an Integral returns itself.'
        pass
    def __floordiv__(self, value):
        'Return self//value.'
        pass
    def __format__(self, format_spec):
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getnewargs__(self):
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __index__(self):
        'Return self converted to an integer, if self is suitable for use as an index into a list.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __int__(self):
        'int(self)'
        pass
    def __invert__(self):
        '~self'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __lshift__(self, value):
        'Return self<<value.'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __mod__(self, value):
        'Return self%value.'
        pass
    def __mul__(self, value):
        'Return self*value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __neg__(self):
        '-self'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __or__(self, value):
        'Return self|value.'
        pass
    def __pos__(self):
        '+self'
        pass
    def __pow__(self, value, mod=None):
        'Return pow(self, value, mod).'
        pass
    def __radd__(self, value):
        'Return value+self.'
        pass
    def __rand__(self, value):
        'Return value&self.'
        pass
    def __rdivmod__(self, value):
        'Return divmod(value, self).'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __rfloordiv__(self, value):
        'Return value//self.'
        pass
    def __rlshift__(self, value):
        'Return value<<self.'
        pass
    def __rmod__(self, value):
        'Return value%self.'
        pass
    def __rmul__(self, value):
        'Return value*self.'
        pass
    def __ror__(self, value):
        'Return value|self.'
        pass
    def __round__(self, ndigits=0):
        'Rounding an Integral returns itself.\nRounding with an ndigits argument also returns an integer.'
        pass
    def __rpow__(self, value, mod=None):
        'Return pow(value, self, mod).'
        pass
    def __rrshift__(self, value):
        'Return value>>self.'
        pass
    def __rshift__(self, value):
        'Return self>>value.'
        pass
    def __rsub__(self, value):
        'Return value-self.'
        pass
    def __rtruediv__(self, value):
        'Return value/self.'
        pass
    def __rxor__(self, value):
        'Return value^self.'
        pass
    def __sizeof__(self):
        'Returns size in memory, in bytes'
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __sub__(self, value):
        'Return self-value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def __truediv__(self, value):
        'Return self/value.'
        pass
    def __trunc__(self):
        'Truncating an Integral returns itself.'
        pass
    def __xor__(self, value):
        'Return self^value.'
        pass
    def bit_length(self):
        "int.bit_length() -> int\n\nNumber of bits necessary to represent self in binary.\n>>> bin(37)\n'0b100101'\n>>> (37).bit_length()\n6"
        pass
    def conjugate(self):
        'Returns self, the complex conjugate of any int.'
        pass
    denominator = getset_descriptor()
    def from_bytes(self):
        "int.from_bytes(bytes, byteorder, *, signed=False) -> int\n\nReturn the integer represented by the given array of bytes.\n\nThe bytes argument must be a bytes-like object (e.g. bytes or bytearray).\n\nThe byteorder argument determines the byte order used to represent the\ninteger.  If byteorder is 'big', the most significant byte is at the\nbeginning of the byte array.  If byteorder is 'little', the most\nsignificant byte is at the end of the byte array.  To request the native\nbyte order of the host system, use `sys.byteorder' as the byte order value.\n\nThe signed keyword-only argument indicates whether two's complement is\nused to represent the integer."
        pass
    imag = getset_descriptor()
    numerator = getset_descriptor()
    real = getset_descriptor()
    def to_bytes(self):
        "int.to_bytes(length, byteorder, *, signed=False) -> bytes\n\nReturn an array of bytes representing an integer.\n\nThe integer is represented using length bytes.  An OverflowError is\nraised if the integer is not representable with the given number of\nbytes.\n\nThe byteorder argument determines the byte order used to represent the\ninteger.  If byteorder is 'big', the most significant byte is at the\nbeginning of the byte array.  If byteorder is 'little', the most\nsignificant byte is at the end of the byte array.  To request the native\nbyte order of the host system, use `sys.byteorder' as the byte order value.\n\nThe signed keyword-only argument determines whether two's complement is\nused to represent the integer.  If signed is False and a negative integer\nis given, an OverflowError is raised."
        pass
def isinstance(obj, class_or_tuple):
    'Return whether an object is an instance of a class or of a subclass thereof.\n\nA tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to\ncheck against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)\nor ...`` etc.'
    pass
def issubclass(cls, class_or_tuple):
    "Return whether 'cls' is a derived from another class or is the same class.\n\nA tuple, as in ``issubclass(x, (A, B, ...))``, may be given as the target to\ncheck against. This is equivalent to ``issubclass(x, A) or issubclass(x, B)\nor ...`` etc."
    pass
def iter(iterable):
    'iter(iterable) -> iterator\niter(callable, sentinel) -> iterator\n\nGet an iterator from an object.  In the first form, the argument must\nsupply its own iterator, or be a sequence.\nIn the second form, the callable is called until it returns the sentinel.'
    pass
def len(obj):
    'Return the number of items in a container.'
    pass
def license():
    'interactive prompt objects for printing the license text, a list of\n    contributors and the copyright notice.'
    pass
class list(object):
    "list() -> new empty list\nlist(iterable) -> new list initialized from iterable's items"
    def __add__(self, value):
        'Return self+value.'
        pass
    __class__ = list
    def __contains__(self, key):
        'Return key in self.'
        pass
    def __delitem__(self, key):
        'Delete self[key].'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getitem__(self, index):
        'x.__getitem__(y) <==> x[y]'
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    __hash__
    def __iadd__(self, value):
        'Implement self+=value.'
        pass
    def __imul__(self, value):
        'Implement self*=value.'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __mul__(self, value):
        'Return self*value.n'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __reversed__(self):
        'L.__reversed__() -- return a reverse iterator over the list'
        pass
    def __rmul__(self, value):
        'Return self*value.'
        pass
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        pass
    def __sizeof__(self):
        'L.__sizeof__() -- size of L in memory, in bytes'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def append(self):
        'L.append(object) -> None -- append object to end'
        pass
    def clear(self):
        'L.clear() -> None -- remove all items from L'
        pass
    def copy(self):
        'L.copy() -> list -- a shallow copy of L'
        pass
    def count(self, x):
        'L.count(value) -> integer -- return number of occurrences of value'
        pass
    def extend(self):
        'L.extend(iterable) -> None -- extend list by appending elements from the iterable'
        pass
    def index(self, v):
        'L.index(value, [start, [stop]]) -> integer -- return first index of value.\nRaises ValueError if the value is not present.'
        pass
    def insert(self):
        'L.insert(index, object) -- insert object before index'
        pass
    def pop(self):
        'L.pop([index]) -> item -- remove and return item at index (default last).\nRaises IndexError if list is empty or index is out of range.'
        pass
    def remove(self):
        'L.remove(value) -> None -- remove first occurrence of value.\nRaises ValueError if the value is not present.'
        pass
    def reverse(self):
        'L.reverse() -- reverse *IN PLACE*'
        pass
    def sort(self):
        'L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*'
        pass
def locals():
    "Return a dictionary containing the current scope's local variables.\n\nNOTE: Whether or not updates to this dictionary will affect name lookups in\nthe local scope and vice-versa is *implementation dependent* and not\ncovered by any backwards compatibility guarantees."
    pass
class map(object):
    'map(func, *iterables) --> map object\n\nMake an iterator that computes the function using arguments from\neach of the iterables.  Stops when the shortest iterable is exhausted.'
    __class__ = map
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __next__(self):
        'Implement next(self).'
        pass
    def __reduce__(self):
        'Return state information for pickling.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
def max(iterable):
    'max(iterable, *[, default=obj, key=func]) -> value\nmax(arg1, arg2, *args, *[, key=func]) -> value\n\nWith a single iterable argument, return its biggest item. The\ndefault keyword-only argument specifies an object to return if\nthe provided iterable is empty.\nWith two or more arguments, return the largest argument.'
    pass
class memoryview(object):
    'Create a new memoryview object which references the given object.'
    __class__ = memoryview
    def __delitem__(self, key):
        'Delete self[key].'
        pass
    def __enter__(self):
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __exit__(self):
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getitem__(self, key):
        'Return self[key].'
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    c_contiguous = getset_descriptor()
    def cast(self, format, *, shape):
        'Cast a memoryview to a new format or shape.'
        pass
    contiguous = getset_descriptor()
    f_contiguous = getset_descriptor()
    format = getset_descriptor()
    def hex(self):
        'Return the data in the buffer as a string of hexadecimal numbers.'
        pass
    itemsize = getset_descriptor()
    nbytes = getset_descriptor()
    ndim = getset_descriptor()
    obj = getset_descriptor()
    readonly = getset_descriptor()
    def release(self):
        'Release the underlying buffer exposed by the memoryview object.'
        pass
    shape = getset_descriptor()
    strides = getset_descriptor()
    suboffsets = getset_descriptor()
    def tobytes(self):
        'Return the data in the buffer as a byte string.'
        pass
    def tolist(self):
        'Return the data in the buffer as a list of elements.'
        pass
def min(iterable):
    'min(iterable, *[, default=obj, key=func]) -> value\nmin(arg1, arg2, *args, *[, key=func]) -> value\n\nWith a single iterable argument, return its smallest item. The\ndefault keyword-only argument specifies an object to return if\nthe provided iterable is empty.\nWith two or more arguments, return the smallest argument.'
    pass
def next(iterator, default):
    'next(iterator[, default])\n\nReturn the next item from the iterator. If default is given and the iterator\nis exhausted, it is returned instead of raising StopIteration.'
    pass
class object:
    'The most base type'
    __class__ = object
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        pass
    def __dir__():
        '__dir__() -> list\ndefault dir() implementation'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __format__(self, format_spec):
        'default object formatter'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __reduce__(self):
        'helper for pickle'
        pass
    def __reduce_ex__(self, protocol):
        'helper for pickle'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        pass
    def __sizeof__():
        '__sizeof__() -> int\nsize of object in memory, in bytes'
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
def oct(number):
    "Return the octal representation of an integer.\n\n   >>> oct(342391)\n   '0o1234567'"
    pass
def open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
    'Open file and return a stream.  Raise IOError upon failure.\n\nfile is either a text or byte string giving the name (and the path\nif the file isn\'t in the current working directory) of the file to\nbe opened or an integer file descriptor of the file to be\nwrapped. (If a file descriptor is given, it is closed when the\nreturned I/O object is closed, unless closefd is set to False.)\n\nmode is an optional string that specifies the mode in which the file\nis opened. It defaults to \'r\' which means open for reading in text\nmode.  Other common values are \'w\' for writing (truncating the file if\nit already exists), \'x\' for creating and writing to a new file, and\n\'a\' for appending (which on some Unix systems, means that all writes\nappend to the end of the file regardless of the current seek position).\nIn text mode, if encoding is not specified the encoding used is platform\ndependent: locale.getpreferredencoding(False) is called to get the\ncurrent locale encoding. (For reading and writing raw bytes use binary\nmode and leave encoding unspecified.) The available modes are:\n\n========= ===============================================================\nCharacter Meaning\n--------- ---------------------------------------------------------------\n\'r\'       open for reading (default)\n\'w\'       open for writing, truncating the file first\n\'x\'       create a new file and open it for writing\n\'a\'       open for writing, appending to the end of the file if it exists\n\'b\'       binary mode\n\'t\'       text mode (default)\n\'+\'       open a disk file for updating (reading and writing)\n\'U\'       universal newline mode (deprecated)\n========= ===============================================================\n\nThe default mode is \'rt\' (open for reading text). For binary random\naccess, the mode \'w+b\' opens and truncates the file to 0 bytes, while\n\'r+b\' opens the file without truncation. The \'x\' mode implies \'w\' and\nraises an `FileExistsError` if the file already exists.\n\nPython distinguishes between files opened in binary and text modes,\neven when the underlying operating system doesn\'t. Files opened in\nbinary mode (appending \'b\' to the mode argument) return contents as\nbytes objects without any decoding. In text mode (the default, or when\n\'t\' is appended to the mode argument), the contents of the file are\nreturned as strings, the bytes having been first decoded using a\nplatform-dependent encoding or using the specified encoding if given.\n\n\'U\' mode is deprecated and will raise an exception in future versions\nof Python.  It has no effect in Python 3.  Use newline to control\nuniversal newlines mode.\n\nbuffering is an optional integer used to set the buffering policy.\nPass 0 to switch buffering off (only allowed in binary mode), 1 to select\nline buffering (only usable in text mode), and an integer > 1 to indicate\nthe size of a fixed-size chunk buffer.  When no buffering argument is\ngiven, the default buffering policy works as follows:\n\n* Binary files are buffered in fixed-size chunks; the size of the buffer\n  is chosen using a heuristic trying to determine the underlying device\'s\n  "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.\n  On many systems, the buffer will typically be 4096 or 8192 bytes long.\n\n* "Interactive" text files (files for which isatty() returns True)\n  use line buffering.  Other text files use the policy described above\n  for binary files.\n\nencoding is the name of the encoding used to decode or encode the\nfile. This should only be used in text mode. The default encoding is\nplatform dependent, but any encoding supported by Python can be\npassed.  See the codecs module for the list of supported encodings.\n\nerrors is an optional string that specifies how encoding errors are to\nbe handled---this argument should not be used in binary mode. Pass\n\'strict\' to raise a ValueError exception if there is an encoding error\n(the default of None has the same effect), or pass \'ignore\' to ignore\nerrors. (Note that ignoring encoding errors can lead to data loss.)\nSee the documentation for codecs.register or run \'help(codecs.Codec)\'\nfor a list of the permitted encoding error strings.\n\nnewline controls how universal newlines works (it only applies to text\nmode). It can be None, \'\', \'\\n\', \'\\r\', and \'\\r\\n\'.  It works as\nfollows:\n\n* On input, if newline is None, universal newlines mode is\n  enabled. Lines in the input can end in \'\\n\', \'\\r\', or \'\\r\\n\', and\n  these are translated into \'\\n\' before being returned to the\n  caller. If it is \'\', universal newline mode is enabled, but line\n  endings are returned to the caller untranslated. If it has any of\n  the other legal values, input lines are only terminated by the given\n  string, and the line ending is returned to the caller untranslated.\n\n* On output, if newline is None, any \'\\n\' characters written are\n  translated to the system default line separator, os.linesep. If\n  newline is \'\' or \'\\n\', no translation takes place. If newline is any\n  of the other legal values, any \'\\n\' characters written are translated\n  to the given string.\n\nIf closefd is False, the underlying file descriptor will be kept open\nwhen the file is closed. This does not work when a file name is given\nand must be True in that case.\n\nA custom opener can be used by passing a callable as *opener*. The\nunderlying file descriptor for the file object is then obtained by\ncalling *opener* with (*file*, *flags*). *opener* must return an open\nfile descriptor (passing os.open as *opener* results in functionality\nsimilar to passing None).\n\nopen() returns a file object whose type depends on the mode, and\nthrough which the standard file operations such as reading and writing\nare performed. When open() is used to open a file in a text mode (\'w\',\n\'r\', \'wt\', \'rt\', etc.), it returns a TextIOWrapper. When used to open\na file in a binary mode, the returned class varies: in read binary\nmode, it returns a BufferedReader; in write binary and append binary\nmodes, it returns a BufferedWriter, and in read/write mode, it returns\na BufferedRandom.\n\nIt is also possible to use a string or bytearray as a file for both\nreading and writing. For strings StringIO can be used like a file\nopened in a text mode, and for bytes a BytesIO can be used like a file\nopened in a binary mode.'
    pass
def ord(c):
    'Return the Unicode code point for a one-character string.'
    pass
def pow(x, y, z=None):
    'Equivalent to x**y (with two arguments) or x**y % z (with three arguments)\n\nSome types, such as ints, are able to use a more efficient algorithm when\ninvoked using the three argument form.'
    pass
def print():
    "print(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)\n\nPrints the values to a stream, or to sys.stdout by default.\nOptional keyword arguments:\nfile:  a file-like object (stream); defaults to the current sys.stdout.\nsep:   string inserted between values, default a space.\nend:   string appended after the last value, default a newline.\nflush: whether to forcibly flush the stream."
    pass
class property(object):
    'property(fget=None, fset=None, fdel=None, doc=None) -> property attribute\n\nfget is a function to be used for getting an attribute value, and likewise\nfset is a function for setting, and fdel a function for del\'ing, an\nattribute.  Typical use is to define a managed attribute x:\n\nclass C(object):\n    def getx(self): return self._x\n    def setx(self, value): self._x = value\n    def delx(self): del self._x\n    x = property(getx, setx, delx, "I\'m the \'x\' property.")\n\nDecorators make defining new properties or modifying existing ones easy:\n\nclass C(object):\n    @property\n    def x(self):\n        "I am the \'x\' property."\n        return self._x\n    @x.setter\n    def x(self, value):\n        self._x = value\n    @x.deleter\n    def x(self):\n        del self._x\n'
    __class__ = property
    def __delete__(self, instance):
        'Delete an attribute of instance.'
        pass
    def __get__(self, instance, owner):
        'Return an attribute of instance, which is of type owner.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    __isabstractmethod__ = getset_descriptor()
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __set__(self, instance, value):
        'Set an attribute of instance to value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def deleter(self):
        'Descriptor to change the deleter on a property.'
        pass
    fdel = member_descriptor()
    fget = member_descriptor()
    fset = member_descriptor()
    def getter(self):
        'Descriptor to change the getter on a property.'
        pass
    def setter(self):
        'Descriptor to change the setter on a property.'
        pass
def quit(code=None):
    pass
class range(object):
    'range(stop) -> range object\nrange(start, stop[, step]) -> range object\n\nReturn an object that produces a sequence of integers from start (inclusive)\nto stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.\nstart defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.\nThese are exactly the valid indices for a list of 4 elements.\nWhen step is given, it specifies the increment (or decrement).'
    def __bool__(self):
        'self != 0'
        pass
    __class__ = range
    def __contains__(self, key):
        'Return key in self.'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getitem__(self, key):
        'Return self[key].'
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __reduce__(self):
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __reversed__(self):
        'Return a reverse iterator.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def count(self, x):
        'rangeobject.count(value) -> integer -- return number of occurrences of value'
        pass
    def index(self, v):
        'rangeobject.index(value, [start, [stop]]) -> integer -- return index of value.\nRaise ValueError if the value is not present.'
        pass
    start = member_descriptor()
    step = member_descriptor()
    stop = member_descriptor()
def repr(obj):
    'Return the canonical string representation of the object.\n\nFor many object types, including most builtins, eval(repr(obj)) == obj.'
    pass
class reversed(object):
    'reversed(sequence) -> reverse iterator over values of the sequence\n\nReturn a reverse iterator'
    __class__ = reversed
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __length_hint__(self):
        'Private method returning an estimate of len(list(it)).'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __next__(self):
        'Implement next(self).'
        pass
    def __reduce__(self):
        'Return state information for pickling.'
        pass
    def __setstate__(self, state):
        'Set state information for unpickling.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
def round(number, ndigits):
    'round(number[, ndigits]) -> number\n\nRound a number to a given precision in decimal digits (default 0 digits).\nThis returns an int when called with one argument, otherwise the\nsame type as the number. ndigits may be negative.'
    pass
class set(object):
    'set() -> new empty set object\nset(iterable) -> new set object\n\nBuild an unordered collection of unique elements.'
    def __and__(self, value):
        'Return self&value.'
        pass
    __class__ = set
    def __contains__(self, value):
        'x.__contains__(y) <==> y in x.'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    __hash__
    def __iand__(self, value):
        'Return self&=value.'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __ior__(self, value):
        'Return self|=value.'
        pass
    def __isub__(self, value):
        'Return self-=value.'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __ixor__(self, value):
        'Return self^=value.'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __or__(self, value):
        'Return self|value.'
        pass
    def __rand__(self, value):
        'Return value&self.'
        pass
    def __reduce__(self):
        'Return state information for pickling.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __ror__(self, value):
        'Return value|self.'
        pass
    def __rsub__(self, value):
        'Return value-self.'
        pass
    def __rxor__(self, value):
        'Return value^self.'
        pass
    def __sizeof__(self):
        'S.__sizeof__() -> size of S in memory, in bytes'
        pass
    def __sub__(self, value):
        'Return self-value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def __xor__(self, value):
        'Return self^value.'
        pass
    def add(self):
        'Add an element to a set.\n\nThis has no effect if the element is already present.'
        pass
    def clear(self):
        'Remove all elements from this set.'
        pass
    def copy(self):
        'Return a shallow copy of a set.'
        pass
    def difference(self):
        'Return the difference of two or more sets as a new set.\n\n(i.e. all elements that are in this set but not the others.)'
        pass
    def difference_update(self):
        'Remove all elements of another set from this set.'
        pass
    def discard(self):
        'Remove an element from a set if it is a member.\n\nIf the element is not a member, do nothing.'
        pass
    def intersection(self):
        'Return the intersection of two sets as a new set.\n\n(i.e. all elements that are in both sets.)'
        pass
    def intersection_update(self):
        'Update a set with the intersection of itself and another.'
        pass
    def isdisjoint(self):
        'Return True if two sets have a null intersection.'
        pass
    def issubset(self):
        'Report whether another set contains this set.'
        pass
    def issuperset(self):
        'Report whether this set contains another set.'
        pass
    def pop(self):
        'Remove and return an arbitrary set element.\nRaises KeyError if the set is empty.'
        pass
    def remove(self):
        'Remove an element from a set; it must be a member.\n\nIf the element is not a member, raise a KeyError.'
        pass
    def symmetric_difference(self):
        'Return the symmetric difference of two sets as a new set.\n\n(i.e. all elements that are in exactly one of the sets.)'
        pass
    def symmetric_difference_update(self):
        'Update a set with the symmetric difference of itself and another.'
        pass
    def union(self):
        'Return the union of sets as a new set.\n\n(i.e. all elements that are in either set.)'
        pass
    def update(self):
        'Update a set with the union of itself and others.'
        pass
def setattr(obj, name, value):
    "Sets the named attribute on the given object to the specified value.\n\nsetattr(x, 'y', v) is equivalent to ``x.y = v''"
    pass
class slice(object):
    'slice(stop)\nslice(start, stop[, step])\n\nCreate a slice object.  This is used for extended slicing (e.g. a[0:10:2]).'
    __class__ = slice
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    __hash__
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __reduce__(self):
        'Return state information for pickling.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def indices(self):
        'S.indices(len) -> (start, stop, stride)\n\nAssuming a sequence of length len, calculate the start and stop\nindices, and the stride length of the extended slice described by\nS. Out of bounds indices are clipped in a manner consistent with the\nhandling of normal slices.'
        pass
    start = member_descriptor()
    step = member_descriptor()
    stop = member_descriptor()
def sorted(iterable, *, key=None, reverse=False):
    'Return a new list containing all items from the iterable in ascending order.\n\nA custom key function can be supplied to customize the sort order, and the\nreverse flag can be set to request the result in descending order.'
    pass
class staticmethod(object):
    'staticmethod(function) -> method\n\nConvert a function to be a static method.\n\nA static method does not receive an implicit first argument.\nTo declare a static method, use this idiom:\n\n     class C:\n         @staticmethod\n         def f(arg1, arg2, ...):\n             ...\n\nIt can be called either on the class (e.g. C.f()) or on an instance\n(e.g. C().f()).  The instance is ignored except for its class.\n\nStatic methods in Python are similar to those found in Java or C++.\nFor a more advanced concept, see the classmethod builtin.'
    __class__ = staticmethod
    __dict__ = {}
    __func__ = member_descriptor()
    def __get__(self, instance, owner):
        'Return an attribute of instance, which is of type owner.'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    __isabstractmethod__ = getset_descriptor()
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
class str(object):
    "str(object='') -> str\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\n\nCreate a new string object from the given object. If encoding or\nerrors is specified, then the object must expose a data buffer\nthat will be decoded using the given encoding and error handler.\nOtherwise, returns the result of object.__str__() (if defined)\nor repr(object).\nencoding defaults to sys.getdefaultencoding().\nerrors defaults to 'strict'."
    def __add__(self, value):
        'Return self+value.'
        pass
    __class__ = str
    def __contains__(self, key):
        'Return key in self.'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __format__(self, format_spec):
        'S.__format__(format_spec) -> str\n\nReturn a formatted version of S as described by format_spec.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getitem__(self, key):
        'Return self[key].'
        pass
    def __getnewargs__(self):
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __mod__(self, value):
        'Return self%value.'
        pass
    def __mul__(self, value):
        'Return self*value.n'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __rmod__(self, value):
        'Return value%self.'
        pass
    def __rmul__(self, value):
        'Return self*value.'
        pass
    def __sizeof__(self):
        'S.__sizeof__() -> size of S in memory, in bytes'
        pass
    def __str__(self):
        'Return str(self).'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def capitalize(self):
        'S.capitalize() -> str\n\nReturn a capitalized version of S, i.e. make the first character\nhave upper case and the rest lower case.'
        pass
    def casefold(self):
        'S.casefold() -> str\n\nReturn a version of S suitable for caseless comparisons.'
        pass
    def center(self):
        'S.center(width[, fillchar]) -> str\n\nReturn S centered in a string of length width. Padding is\ndone using the specified fill character (default is a space)'
        pass
    def count(self, x):
        'S.count(sub[, start[, end]]) -> int\n\nReturn the number of non-overlapping occurrences of substring sub in\nstring S[start:end].  Optional arguments start and end are\ninterpreted as in slice notation.'
        pass
    def encode(self):
        "S.encode(encoding='utf-8', errors='strict') -> bytes\n\nEncode S using the codec registered for encoding. Default encoding\nis 'utf-8'. errors may be given to set a different error\nhandling scheme. Default is 'strict' meaning that encoding errors raise\na UnicodeEncodeError. Other possible values are 'ignore', 'replace' and\n'xmlcharrefreplace' as well as any other name registered with\ncodecs.register_error that can handle UnicodeEncodeErrors."
        pass
    def endswith(self, suffix, start=0, end=-1):
        'S.endswith(suffix[, start[, end]]) -> bool\n\nReturn True if S ends with the specified suffix, False otherwise.\nWith optional start, test S beginning at that position.\nWith optional end, stop comparing S at that position.\nsuffix can also be a tuple of strings to try.'
        pass
    def expandtabs(self, tabsize=8):
        'S.expandtabs(tabsize=8) -> str\n\nReturn a copy of S where all tab characters are expanded using spaces.\nIf tabsize is not given, a tab size of 8 characters is assumed.'
        pass
    def find(self, sub, start=0, end=-1):
        'S.find(sub[, start[, end]]) -> int\n\nReturn the lowest index in S where substring sub is found,\nsuch that sub is contained within S[start:end].  Optional\narguments start and end are interpreted as in slice notation.\n\nReturn -1 on failure.'
        pass
    def format(self):
        "S.format(*args, **kwargs) -> str\n\nReturn a formatted version of S, using substitutions from args and kwargs.\nThe substitutions are identified by braces ('{' and '}')."
        pass
    def format_map(self):
        "S.format_map(mapping) -> str\n\nReturn a formatted version of S, using substitutions from mapping.\nThe substitutions are identified by braces ('{' and '}')."
        pass
    def index(self, v):
        'S.index(sub[, start[, end]]) -> int\n\nReturn the lowest index in S where substring sub is found, \nsuch that sub is contained within S[start:end].  Optional\narguments start and end are interpreted as in slice notation.\n\nRaises ValueError when the substring is not found.'
        pass
    def isalnum(self):
        'S.isalnum() -> bool\n\nReturn True if all characters in S are alphanumeric\nand there is at least one character in S, False otherwise.'
        pass
    def isalpha(self):
        'S.isalpha() -> bool\n\nReturn True if all characters in S are alphabetic\nand there is at least one character in S, False otherwise.'
        pass
    def isdecimal(self):
        'S.isdecimal() -> bool\n\nReturn True if there are only decimal characters in S,\nFalse otherwise.'
        pass
    def isdigit(self):
        'S.isdigit() -> bool\n\nReturn True if all characters in S are digits\nand there is at least one character in S, False otherwise.'
        pass
    def isidentifier(self):
        'S.isidentifier() -> bool\n\nReturn True if S is a valid identifier according\nto the language definition.\n\nUse keyword.iskeyword() to test for reserved identifiers\nsuch as "def" and "class".\n'
        pass
    def islower(self):
        'S.islower() -> bool\n\nReturn True if all cased characters in S are lowercase and there is\nat least one cased character in S, False otherwise.'
        pass
    def isnumeric(self):
        'S.isnumeric() -> bool\n\nReturn True if there are only numeric characters in S,\nFalse otherwise.'
        pass
    def isprintable(self):
        'S.isprintable() -> bool\n\nReturn True if all characters in S are considered\nprintable in repr() or S is empty, False otherwise.'
        pass
    def isspace(self):
        'S.isspace() -> bool\n\nReturn True if all characters in S are whitespace\nand there is at least one character in S, False otherwise.'
        pass
    def istitle(self):
        'S.istitle() -> bool\n\nReturn True if S is a titlecased string and there is at least one\ncharacter in S, i.e. upper- and titlecase characters may only\nfollow uncased characters and lowercase characters only cased ones.\nReturn False otherwise.'
        pass
    def isupper(self):
        'S.isupper() -> bool\n\nReturn True if all cased characters in S are uppercase and there is\nat least one cased character in S, False otherwise.'
        pass
    def join(self):
        'S.join(iterable) -> str\n\nReturn a string which is the concatenation of the strings in the\niterable.  The separator between elements is S.'
        pass
    def ljust(self):
        'S.ljust(width[, fillchar]) -> str\n\nReturn S left-justified in a Unicode string of length width. Padding is\ndone using the specified fill character (default is a space).'
        pass
    def lower(self):
        'S.lower() -> str\n\nReturn a copy of the string S converted to lowercase.'
        pass
    def lstrip(self, chars):
        'S.lstrip([chars]) -> str\n\nReturn a copy of the string S with leading whitespace removed.\nIf chars is given and not None, remove characters in chars instead.'
        pass
    def maketrans(x, y=None, z=None):
        'Return a translation table usable for str.translate().\n\nIf there is only one argument, it must be a dictionary mapping Unicode\nordinals (integers) or characters to Unicode ordinals, strings or None.\nCharacter keys will be then converted to ordinals.\nIf there are two arguments, they must be strings of equal length, and\nin the resulting dictionary, each character in x will be mapped to the\ncharacter at the same position in y. If there is a third argument, it\nmust be a string, whose characters will be mapped to None in the result.'
        pass
    def partition(self):
        'S.partition(sep) -> (head, sep, tail)\n\nSearch for the separator sep in S, and return the part before it,\nthe separator itself, and the part after it.  If the separator is not\nfound, return S and two empty strings.'
        pass
    def replace(self, old, new, count=-1):
        'S.replace(old, new[, count]) -> str\n\nReturn a copy of S with all occurrences of substring\nold replaced by new.  If the optional argument count is\ngiven, only the first count occurrences are replaced.'
        pass
    def rfind(self, sub, start=0, end=-1):
        'S.rfind(sub[, start[, end]]) -> int\n\nReturn the highest index in S where substring sub is found,\nsuch that sub is contained within S[start:end].  Optional\narguments start and end are interpreted as in slice notation.\n\nReturn -1 on failure.'
        pass
    def rindex(self, sub, start=0, end=-1):
        'S.rindex(sub[, start[, end]]) -> int\n\nReturn the highest index in S where substring sub is found,\nsuch that sub is contained within S[start:end].  Optional\narguments start and end are interpreted as in slice notation.\n\nRaises ValueError when the substring is not found.'
        pass
    def rjust(self):
        'S.rjust(width[, fillchar]) -> str\n\nReturn S right-justified in a string of length width. Padding is\ndone using the specified fill character (default is a space).'
        pass
    def rpartition(self):
        'S.rpartition(sep) -> (head, sep, tail)\n\nSearch for the separator sep in S, starting at the end of S, and return\nthe part before it, the separator itself, and the part after it.  If the\nseparator is not found, return two empty strings and S.'
        pass
    def rsplit(self, sep=None, maxsplit=-1):
        'S.rsplit(sep=None, maxsplit=-1) -> list of strings\n\nReturn a list of the words in S, using sep as the\ndelimiter string, starting at the end of the string and\nworking to the front.  If maxsplit is given, at most maxsplit\nsplits are done. If sep is not specified, any whitespace string\nis a separator.'
        pass
    def rstrip(self, chars=None):
        'S.rstrip([chars]) -> str\n\nReturn a copy of the string S with trailing whitespace removed.\nIf chars is given and not None, remove characters in chars instead.'
        pass
    def split(self, sep=None, maxsplit=-1):
        'S.split(sep=None, maxsplit=-1) -> list of strings\n\nReturn a list of the words in S, using sep as the\ndelimiter string.  If maxsplit is given, at most maxsplit\nsplits are done. If sep is not specified or is None, any\nwhitespace string is a separator and empty strings are\nremoved from the result.'
        pass
    def splitlines(self, keepends=False):
        'S.splitlines([keepends]) -> list of strings\n\nReturn a list of the lines in S, breaking at line boundaries.\nLine breaks are not included in the resulting list unless keepends\nis given and true.'
        pass
    def startswith(self, prefix, start=0, end=-1):
        'S.startswith(prefix[, start[, end]]) -> bool\n\nReturn True if S starts with the specified prefix, False otherwise.\nWith optional start, test S beginning at that position.\nWith optional end, stop comparing S at that position.\nprefix can also be a tuple of strings to try.'
        pass
    def strip(self, chars=None):
        'S.strip([chars]) -> str\n\nReturn a copy of the string S with leading and trailing\nwhitespace removed.\nIf chars is given and not None, remove characters in chars instead.'
        pass
    def swapcase(self):
        'S.swapcase() -> str\n\nReturn a copy of S with uppercase characters converted to lowercase\nand vice versa.'
        pass
    def title(self):
        'S.title() -> str\n\nReturn a titlecased version of S, i.e. words start with title case\ncharacters, all remaining cased characters have lower case.'
        pass
    def translate(self):
        'S.translate(table) -> str\n\nReturn a copy of the string S in which each character has been mapped\nthrough the given translation table. The table must implement\nlookup/indexing via __getitem__, for instance a dictionary or list,\nmapping Unicode ordinals to Unicode ordinals, strings, or None. If\nthis operation raises LookupError, the character is left untouched.\nCharacters mapped to None are deleted.'
        pass
    def upper(self):
        'S.upper() -> str\n\nReturn a copy of S converted to uppercase.'
        pass
    def zfill(self, width):
        'S.zfill(width) -> str\n\nPad a numeric string S with zeros on the left, to fill a field\nof the specified width. The string S is never truncated.'
        pass
def sum(iterable, start=0):
    "Return the sum of a 'start' value (default: 0) plus an iterable of numbers\n\nWhen the iterable is empty, return the start value.\nThis function is intended specifically for use with numeric values and may\nreject non-numeric types."
    pass
class super(object):
    'super() -> same as super(__class__, <first argument>)\nsuper(type) -> unbound super object\nsuper(type, obj) -> bound super object; requires isinstance(obj, type)\nsuper(type, type2) -> bound super object; requires issubclass(type2, type)\nTypical use to call a cooperative superclass method:\nclass C(B):\n    def meth(self, arg):\n        super().meth(arg)\nThis works for class methods too:\nclass C(B):\n    @classmethod\n    def cmeth(cls, arg):\n        super().cmeth(arg)\n'
    __class__ = super
    def __get__(self, instance, owner):
        'Return an attribute of instance, which is of type owner.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    __self__ = member_descriptor()
    __self_class__ = member_descriptor()
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    __thisclass__ = member_descriptor()
class tuple(object):
    "tuple() -> empty tuple\ntuple(iterable) -> tuple initialized from iterable's items\n\nIf the argument is a tuple, the return value is the same object."
    def __add__(self, value):
        'Return self+value.'
        pass
    __class__ = tuple
    def __contains__(self, key):
        'Return key in self.'
        pass
    def __eq__(self, value):
        'Return self==value.'
        pass
    def __ge__(self, value):
        'Return self>=value.'
        pass
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __getitem__(self, key):
        'Return self[key].'
        pass
    def __getnewargs__(self):
        pass
    def __gt__(self, value):
        'Return self>value.'
        pass
    def __hash__(self):
        'Return hash(self).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __le__(self, value):
        'Return self<=value.'
        pass
    def __len__(self):
        'Return len(self).'
        pass
    def __lt__(self, value):
        'Return self<value.'
        pass
    def __mul__(self, value):
        'Return self*value.n'
        pass
    def __ne__(self, value):
        'Return self!=value.'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __repr__(self):
        'Return repr(self).'
        pass
    def __rmul__(self, value):
        'Return self*value.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    def count(self, x):
        'T.count(value) -> integer -- return number of occurrences of value'
        pass
    def index(self, v):
        'T.index(value, [start, [stop]]) -> integer -- return first index of value.\nRaises ValueError if the value is not present.'
        pass
class type(object):
    "type(object_or_name, bases, dict)\ntype(object) -> the object's type\ntype(name, bases, dict) -> a new type"
    __base__ = object()
    __bases__ = ()
    __basicsize__ = 864
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    __class__ = type
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        pass
    __dict__ = {}
    __dictoffset__ = 264
    def __dir__():
        '__dir__() -> list\nspecialized __dir__ implementation for types'
        pass
    __flags__ = -2146675712
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init__(self, *args, **kwargs):
        'Initialize self.  See help(type(self)) for accurate signature.'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __instancecheck__():
        '__instancecheck__() -> bool\ncheck if an object is an instance'
        pass
    __itemsize__ = 40
    __mro__ = ()
    __name__ = 'type'
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __prepare__():
        '__prepare__() -> dict\nused to create the namespace for the class statement'
        pass
    __qualname__ = 'type'
    def __repr__(self):
        'Return repr(self).'
        pass
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        pass
    def __sizeof__():
        '__sizeof__() -> int\nreturn memory consumption of the type object'
        pass
    def __subclasscheck__():
        '__subclasscheck__() -> bool\ncheck if a class is a subclass'
        pass
    def __subclasses__():
        '__subclasses__() -> list of immediate subclasses'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass
    __text_signature__
    __weakrefoffset__ = 368
    def mro():
        "mro() -> list\nreturn a type's method resolution order"
        pass
def vars(object):
    'vars([object]) -> dictionary\n\nWithout arguments, equivalent to locals().\nWith an argument, equivalent to object.__dict__.'
    pass
class zip(object):
    'zip(iter1 [,iter2 [...]]) --> zip object\n\nReturn a zip object whose .__next__() method returns a tuple where\nthe i-th element comes from the i-th iterable argument.  The .__next__()\nmethod continues until the shortest iterable in the argument sequence\nis exhausted and then it raises StopIteration.'
    __class__ = zip
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        pass
    def __iter__(self):
        'Implement iter(self).'
        pass
    def __new__(*args, **kwargs):
        'Create and return a new object.  See help(type) for accurate signature.'
        pass
    def __next__(self):
        'Implement next(self).'
        pass
    def __reduce__(self):
        'Return state information for pickling.'
        pass
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        pass