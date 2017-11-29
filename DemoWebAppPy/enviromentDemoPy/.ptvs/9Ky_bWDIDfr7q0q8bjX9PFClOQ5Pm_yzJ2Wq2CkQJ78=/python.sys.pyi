﻿import _io
import types
def __displayhook__():
    'displayhook(object) -> None\n\nPrint an object to sys.stdout and also save it in builtins._\n'
    pass
__doc__ = "This module provides access to some objects used or maintained by the\ninterpreter and to functions that interact strongly with the interpreter.\n\nDynamic objects:\n\nargv -- command line arguments; argv[0] is the script pathname if known\npath -- module search path; path[0] is the script directory, else ''\nmodules -- dictionary of loaded modules\n\ndisplayhook -- called to show results in an interactive session\nexcepthook -- called to handle any uncaught exception other than SystemExit\n  To customize printing in an interactive session or to install a custom\n  top-level exception handler, assign other functions to replace these.\n\nstdin -- standard input file object; used by input()\nstdout -- standard output file object; used by print()\nstderr -- standard error object; used for error messages\n  By assigning other file objects (or objects that behave like files)\n  to these, it is possible to redirect all of the interpreter's I/O.\n\nlast_type -- type of last uncaught exception\nlast_value -- value of last uncaught exception\nlast_traceback -- traceback of last uncaught exception\n  These three are only available in an interactive session after a\n  traceback has been printed.\n\nStatic objects:\n\nbuiltin_module_names -- tuple of module names built into this interpreter\ncopyright -- copyright notice pertaining to this interpreter\nexec_prefix -- prefix used to find the machine-specific Python library\nexecutable -- absolute path of the executable binary of the Python interpreter\nfloat_info -- a struct sequence with information about the float implementation.\nfloat_repr_style -- string indicating the style of repr() output for floats\nhash_info -- a struct sequence with information about the hash algorithm.\nhexversion -- version information encoded as a single integer\nimplementation -- Python implementation information.\nint_info -- a struct sequence with information about the int implementation.\nmaxsize -- the largest supported length of containers.\nmaxunicode -- the value of the largest Unicode code point\nplatform -- platform identifier\nprefix -- prefix used to find the Python library\nthread_info -- a struct sequence with information about the thread implementation.\nversion -- the version of this interpreter as a string\nversion_info -- version information as a named tuple\ndllhandle -- [Windows only] integer handle of the Python DLL\nwinver -- [Windows only] version number of the Python DLL\n_enablelegacywindowsfsencoding -- [Windows only] \n__stdin__ -- the original stdin; don't touch!\n__stdout__ -- the original stdout; don't touch!\n__stderr__ -- the original stderr; don't touch!\n__displayhook__ -- the original displayhook; don't touch!\n__excepthook__ -- the original excepthook; don't touch!\n\nFunctions:\n\ndisplayhook() -- print an object to the screen, and save it in builtins._\nexcepthook() -- print an exception and its traceback to sys.stderr\nexc_info() -- return thread-safe information about the current exception\nexit() -- exit the interpreter by raising SystemExit\ngetdlopenflags() -- returns flags to be used for dlopen() calls\ngetprofile() -- get the global profiling function\ngetrefcount() -- return the reference count for an object (plus one :-)\ngetrecursionlimit() -- return the max recursion depth for the interpreter\ngetsizeof() -- return the size of an object in bytes\ngettrace() -- get the global debug tracing function\nsetcheckinterval() -- control how often the interpreter checks for events\nsetdlopenflags() -- set the flags to be used for dlopen() calls\nsetprofile() -- set the global profiling function\nsetrecursionlimit() -- set the max recursion depth for the interpreter\nsettrace() -- set the global debug tracing function\n"
def __excepthook__():
    'excepthook(exctype, value, traceback) -> None\n\nHandle an exception by displaying it with a traceback on sys.stderr.\n'
    pass
def __interactivehook__():
    pass
__name__ = 'sys'
__package__ = ''
__spec__
__stderr__ = _io.TextIOWrapper()
__stdin__ = _io.TextIOWrapper()
__stdout__ = _io.TextIOWrapper()
def _clear_type_cache():
    '_clear_type_cache() -> None\nClear the internal type lookup cache.'
    pass
def _current_frames():
    "_current_frames() -> dictionary\n\nReturn a dictionary mapping each current thread T's thread id to T's\ncurrent stack frame.\n\nThis function should be used for specialized purposes only."
    pass
def _debugmallocstats():
    "_debugmallocstats()\n\nPrint summary info to stderr about the state of\npymalloc's structures.\n\nIn Py_DEBUG mode, also perform some expensive internal consistency\nchecks.\n"
    pass
def _enablelegacywindowsfsencoding():
    '_enablelegacywindowsfsencoding()\n\nChanges the default filesystem encoding to mbcs:replace for consistency\nwith earlier versions of Python. See PEP 529 for more information.\n\nThis is equivalent to defining the PYTHONLEGACYWINDOWSFSENCODING \nenvironment variable before launching Python.'
    pass
def _getframe(depth):
    '_getframe([depth]) -> frameobject\n\nReturn a frame object from the call stack.  If optional integer depth is\ngiven, return the frame object that many calls below the top of the stack.\nIf that is deeper than the call stack, ValueError is raised.  The default\nfor depth is zero, returning the frame at the top of the call stack.\n\nThis function should be used for internal and specialized\npurposes only.'
    pass
_git = ('CPython', 'v3.6.3', '2c5fed8')
_home = 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64'
_xoptions = {}
api_version = 1013
argv = ['C:\\Program Files (x86)\\Microsoft Visual Studio\\Preview\\Community\\Common7\\IDE\\Extensions\\Microsoft\\Python\\Core\\scrape_module.py', 'sys']
base_exec_prefix = 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64'
base_prefix = 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64'
builtin_module_names = ('_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections', '_csv', '_datetime', '_findvs', '_functools', '_heapq', '_imp', '_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator', '_pickle', '_random', '_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_sre', '_stat', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', '_winapi', 'array', 'atexit', 'audioop', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 'parser', 'sys', 'time', 'winreg', 'xxsubtype', 'zipimport', 'zlib')
byteorder = 'little'
def call_tracing(func, args):
    'call_tracing(func, args) -> object\n\nCall func(*args), while tracing is enabled.  The tracing state is\nsaved, and restored afterwards.  This is intended to be called from\na debugger from a checkpoint, to recursively debug some other code.'
    pass
def callstats():
    'callstats() -> tuple of integers\n\nReturn a tuple of function call statistics, if CALL_PROFILE was defined\nwhen Python was built.  Otherwise, return None.\n\nWhen enabled, this function returns detailed, implementation-specific\ndetails about the number of function calls executed. The return value is\na 11-tuple where the entries in the tuple are counts of:\n0. all function calls\n1. calls to PyFunction_Type objects\n2. PyFunction calls that do not create an argument tuple\n3. PyFunction calls that do not create an argument tuple\n   and bypass PyEval_EvalCodeEx()\n4. PyMethod calls\n5. PyMethod calls on bound methods\n6. PyType calls\n7. PyCFunction calls\n8. generator calls\n9. All other calls\n10. Number of stack pops performed by call_function()'
    pass
copyright = 'Copyright (c) 2001-2017 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.'
def displayhook(object):
    'displayhook(object) -> None\n\nPrint an object to sys.stdout and also save it in builtins._\n'
    pass
dllhandle = 1474756608
dont_write_bytecode = True
def exc_info():
    'exc_info() -> (type, value, traceback)\n\nReturn information about the most recent exception caught by an except\nclause in the current stack frame or in an older stack frame.'
    pass
def excepthook(exctype, value, traceback):
    'excepthook(exctype, value, traceback) -> None\n\nHandle an exception by displaying it with a traceback on sys.stderr.\n'
    pass
exec_prefix = 'C:\\Repos\\GitHub\\DemoPy_Continous_Integration\\DemoWebAppPy\\enviromentDemoPy'
executable = 'C:\\Repos\\GitHub\\DemoPy_Continous_Integration\\DemoWebAppPy\\enviromentDemoPy\\Scripts\\python.exe'
def exit(status):
    'exit([status])\n\nExit the interpreter by raising SystemExit(status).\nIf the status is omitted or None, it defaults to zero (i.e., success).\nIf the status is an integer, it will be used as the system exit status.\nIf it is another kind of object, it will be printed and the system\nexit status will be one (i.e., failure).'
    pass
class flags:
    'sys.flags\n\nFlags provided through command line arguments or environment vars.'
    def __add__(value):
        'Return self+value.'
        pass
    __class__ = flags
    def __contains__(key):
        'Return key in self.'
        pass
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
    def __getitem__(key):
        'Return self[key].'
        pass
    def __getnewargs__(self):
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
    def __iter__():
        'Implement iter(self).'
        pass
    def __le__(value):
        'Return self<=value.'
        pass
    def __len__():
        'Return len(self).'
        pass
    def __lt__(value):
        'Return self<value.'
        pass
    def __mul__(value):
        'Return self*value.n'
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
    def __rmul__(value):
        'Return self*value.'
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
    bytes_warning = 0
    def count(self):
        'T.count(value) -> integer -- return number of occurrences of value'
        pass
    debug = 0
    dont_write_bytecode = 1
    hash_randomization = 1
    ignore_environment = 1
    def index(self):
        'T.index(value, [start, [stop]]) -> integer -- return first index of value.\nRaises ValueError if the value is not present.'
        pass
    inspect = 0
    interactive = 0
    isolated = 0
    n_fields = 13
    n_sequence_fields = 13
    n_unnamed_fields = 0
    no_site = 0
    no_user_site = 0
    optimize = 0
    quiet = 0
    verbose = 0
class float_info:
    "sys.float_info\n\nA structseq holding information about the float type. It contains low level\ninformation about the precision and internal representation. Please study\nyour system's :file:`float.h` for more information."
    def __add__(value):
        'Return self+value.'
        pass
    __class__ = float_info
    def __contains__(key):
        'Return key in self.'
        pass
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
    def __getitem__(key):
        'Return self[key].'
        pass
    def __getnewargs__(self):
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
    def __iter__():
        'Implement iter(self).'
        pass
    def __le__(value):
        'Return self<=value.'
        pass
    def __len__():
        'Return len(self).'
        pass
    def __lt__(value):
        'Return self<value.'
        pass
    def __mul__(value):
        'Return self*value.n'
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
    def __rmul__(value):
        'Return self*value.'
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
    def count(self):
        'T.count(value) -> integer -- return number of occurrences of value'
        pass
    dig = 15
    epsilon = 2.220446049250313e-16
    def index(self):
        'T.index(value, [start, [stop]]) -> integer -- return first index of value.\nRaises ValueError if the value is not present.'
        pass
    mant_dig = 53
    max = 1.7976931348623157e+308
    max_10_exp = 308
    max_exp = 1024
    min = 2.2250738585072014e-308
    min_10_exp = -307
    min_exp = -1021
    n_fields = 11
    n_sequence_fields = 11
    n_unnamed_fields = 0
    radix = 2
    rounds = 1
float_repr_style = 'short'
def get_asyncgen_hooks():
    'get_asyncgen_hooks()\n\nReturn a namedtuple of installed asynchronous generators hooks (firstiter, finalizer).'
    pass
def get_coroutine_wrapper():
    'get_coroutine_wrapper()\n\nReturn the wrapper for coroutine objects set by sys.set_coroutine_wrapper.'
    pass
def getallocatedblocks():
    'getallocatedblocks() -> integer\n\nReturn the number of memory blocks currently allocated, regardless of their\nsize.'
    pass
def getcheckinterval():
    'getcheckinterval() -> current check interval; see setcheckinterval().'
    pass
def getdefaultencoding():
    'getdefaultencoding() -> string\n\nReturn the current default string encoding used by the Unicode \nimplementation.'
    pass
def getfilesystemencodeerrors():
    'getfilesystemencodeerrors() -> string\n\nReturn the error mode used to convert Unicode filenames in\noperating system filenames.'
    pass
def getfilesystemencoding():
    'getfilesystemencoding() -> string\n\nReturn the encoding used to convert Unicode filenames in\noperating system filenames.'
    pass
def getprofile():
    'getprofile()\n\nReturn the profiling function set with sys.setprofile.\nSee the profiler chapter in the library manual.'
    pass
def getrecursionlimit():
    'getrecursionlimit()\n\nReturn the current value of the recursion limit, the maximum depth\nof the Python interpreter stack.  This limit prevents infinite\nrecursion from causing an overflow of the C stack and crashing Python.'
    pass
def getrefcount(object):
    'getrefcount(object) -> integer\n\nReturn the reference count of object.  The count returned is generally\none higher than you might expect, because it includes the (temporary)\nreference as an argument to getrefcount().'
    pass
def getsizeof(object, default):
    'getsizeof(object, default) -> int\n\nReturn the size of object in bytes.'
    pass
def getswitchinterval():
    'getswitchinterval() -> current thread switch interval; see setswitchinterval().'
    pass
def gettrace():
    'gettrace()\n\nReturn the global debug tracing function set with sys.settrace.\nSee the debugger chapter in the library manual.'
    pass
def getwindowsversion():
    'getwindowsversion()\n\nReturn information about the running version of Windows as a named tuple.\nThe members are named: major, minor, build, platform, service_pack,\nservice_pack_major, service_pack_minor, suite_mask, and product_type. For\nbackward compatibility, only the first 5 items are available by indexing.\nAll elements are numbers, except service_pack and platform_type which are\nstrings, and platform_version which is a 3-tuple. Platform is always 2.\nProduct_type may be 1 for a workstation, 2 for a domain controller, 3 for a\nserver. Platform_version is a 3-tuple containing a version number that is\nintended for identifying the OS rather than feature detection.'
    pass
class hash_info:
    'hash_info\n\nA struct sequence providing parameters used for computing\nhashes. The attributes are read only.'
    def __add__(value):
        'Return self+value.'
        pass
    __class__ = hash_info
    def __contains__(key):
        'Return key in self.'
        pass
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
    def __getitem__(key):
        'Return self[key].'
        pass
    def __getnewargs__(self):
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
    def __iter__():
        'Implement iter(self).'
        pass
    def __le__(value):
        'Return self<=value.'
        pass
    def __len__():
        'Return len(self).'
        pass
    def __lt__(value):
        'Return self<value.'
        pass
    def __mul__(value):
        'Return self*value.n'
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
    def __rmul__(value):
        'Return self*value.'
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
    algorithm = 'siphash24'
    def count(self):
        'T.count(value) -> integer -- return number of occurrences of value'
        pass
    cutoff = 0
    hash_bits = 64
    imag = 1000003
    def index(self):
        'T.index(value, [start, [stop]]) -> integer -- return first index of value.\nRaises ValueError if the value is not present.'
        pass
    inf = 314159
    modulus = 2305843009213693951
    n_fields = 9
    n_sequence_fields = 9
    n_unnamed_fields = 0
    nan = 0
    seed_bits = 128
    width = 64
hexversion = 50725872
implementation = types.SimpleNamespace()
class int_info:
    "sys.int_info\n\nA struct sequence that holds information about Python's\ninternal representation of integers.  The attributes are read only."
    def __add__(value):
        'Return self+value.'
        pass
    __class__ = int_info
    def __contains__(key):
        'Return key in self.'
        pass
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
    def __getitem__(key):
        'Return self[key].'
        pass
    def __getnewargs__(self):
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
    def __iter__():
        'Implement iter(self).'
        pass
    def __le__(value):
        'Return self<=value.'
        pass
    def __len__():
        'Return len(self).'
        pass
    def __lt__(value):
        'Return self<value.'
        pass
    def __mul__(value):
        'Return self*value.n'
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
    def __rmul__(value):
        'Return self*value.'
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
    bits_per_digit = 30
    def count(self):
        'T.count(value) -> integer -- return number of occurrences of value'
        pass
    def index(self):
        'T.index(value, [start, [stop]]) -> integer -- return first index of value.\nRaises ValueError if the value is not present.'
        pass
    n_fields = 2
    n_sequence_fields = 2
    n_unnamed_fields = 0
    sizeof_digit = 4
def intern(string):
    "intern(string) -> string\n\n``Intern'' the given string.  This enters the string in the (global)\ntable of interned strings whose purpose is to speed up dictionary lookups.\nReturn the string itself or the previously interned string object with the\nsame value."
    pass
def is_finalizing():
    'is_finalizing()\nReturn True if Python is exiting.'
    pass
maxsize = 9223372036854775807
maxunicode = 1114111
meta_path = [<class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib_external.PathFinder'>]
modules = {'builtins': <module 'builtins' (built-in)>, 'sys': <module 'sys' (built-in)>, '_frozen_importlib': <module 'importlib._bootstrap' (frozen)>, '_imp': <module '_imp' (built-in)>, '_warnings': <module '_warnings' (built-in)>, '_thread': <module '_thread' (built-in)>, '_weakref': <module '_weakref' (built-in)>, '_frozen_importlib_external': <module 'importlib._bootstrap_external' (frozen)>, '_io': <module 'io' (built-in)>, 'marshal': <module 'marshal' (built-in)>, 'nt': <module 'nt' (built-in)>, 'winreg': <module 'winreg' (built-in)>, 'zipimport': <module 'zipimport' (built-in)>, 'encodings': <module 'encodings' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\encodings\\__init__.py'>, 'codecs': <module 'codecs' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\codecs.py'>, '_codecs': <module '_codecs' (built-in)>, 'encodings.aliases': <module 'encodings.aliases' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\encodings\\aliases.py'>, 'encodings.utf_8': <module 'encodings.utf_8' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\encodings\\utf_8.py'>, '_signal': <module '_signal' (built-in)>, '__main__': <module '__main__' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Preview\\Community\\Common7\\IDE\\Extensions\\Microsoft\\Python\\Core\\scrape_module.py'>, 'encodings.latin_1': <module 'encodings.latin_1' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\encodings\\latin_1.py'>, 'io': <module 'io' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\io.py'>, 'abc': <module 'abc' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\abc.py'>, '_weakrefset': <module '_weakrefset' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\_weakrefset.py'>, '_bootlocale': <module '_bootlocale' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\_bootlocale.py'>, '_locale': <module '_locale' (built-in)>, 'encodings.cp1252': <module 'encodings.cp1252' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\encodings\\cp1252.py'>, 'site': <module 'site' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\site.py'>, 'os': <module 'os' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\os.py'>, 'errno': <module 'errno' (built-in)>, 'stat': <module 'stat' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\stat.py'>, '_stat': <module '_stat' (built-in)>, 'ntpath': <module 'ntpath' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\ntpath.py'>, 'genericpath': <module 'genericpath' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\genericpath.py'>, 'os.path': <module 'ntpath' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\ntpath.py'>, '_collections_abc': <module '_collections_abc' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\_collections_abc.py'>, '_sitebuiltins': <module '_sitebuiltins' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\_sitebuiltins.py'>, 'sysconfig': <module 'sysconfig' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\sysconfig.py'>, '__future__': <module '__future__' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\__future__.py'>, 'ast': <module 'ast' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\ast.py'>, '_ast': <module '_ast' (built-in)>, 'inspect': <module 'inspect' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\inspect.py'>, 'dis': <module 'dis' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\dis.py'>, 'types': <module 'types' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\types.py'>, 'functools': <module 'functools' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\functools.py'>, '_functools': <module '_functools' (built-in)>, 'collections': <module 'collections' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\collections\\__init__.py'>, 'operator': <module 'operator' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\operator.py'>, '_operator': <module '_operator' (built-in)>, 'keyword': <module 'keyword' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\keyword.py'>, 'heapq': <module 'heapq' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\heapq.py'>, '_heapq': <module '_heapq' (built-in)>, 'itertools': <module 'itertools' (built-in)>, 'reprlib': <module 'reprlib' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\reprlib.py'>, '_collections': <module '_collections' (built-in)>, 'weakref': <module 'weakref' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\weakref.py'>, 'collections.abc': <module 'collections.abc' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\collections\\abc.py'>, 'opcode': <module 'opcode' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\opcode.py'>, '_opcode': <module '_opcode' (built-in)>, 'enum': <module 'enum' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\enum.py'>, 'importlib': <module 'importlib' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\importlib\\__init__.py'>, 'importlib._bootstrap': <module 'importlib._bootstrap' (frozen)>, 'importlib._bootstrap_external': <module 'importlib._bootstrap_external' (frozen)>, 'warnings': <module 'warnings' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\warnings.py'>, 'importlib.machinery': <module 'importlib.machinery' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\importlib\\machinery.py'>, 'linecache': <module 'linecache' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\linecache.py'>, 'tokenize': <module 'tokenize' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\tokenize.py'>, 're': <module 're' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\re.py'>, 'sre_compile': <module 'sre_compile' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\sre_compile.py'>, '_sre': <module '_sre' (built-in)>, 'sre_parse': <module 'sre_parse' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\sre_parse.py'>, 'sre_constants': <module 'sre_constants' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\sre_constants.py'>, 'copyreg': <module 'copyreg' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\copyreg.py'>, 'token': <module 'token' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\token.py'>, 'encodings.utf_8_sig': <module 'encodings.utf_8_sig' from 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\encodings\\utf_8_sig.py'>}
path = ['C:\\Program Files (x86)\\Microsoft Visual Studio\\Preview\\Community\\Common7\\IDE\\Extensions\\Microsoft\\Python\\Core', 'C:\\Repos\\GitHub\\DemoPy_Continous_Integration\\DemoWebAppPy\\enviromentDemoPy\\Scripts\\python36.zip', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\DLLs', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib', 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64', 'C:\\Repos\\GitHub\\DemoPy_Continous_Integration\\DemoWebAppPy\\enviromentDemoPy', 'C:\\Repos\\GitHub\\DemoPy_Continous_Integration\\DemoWebAppPy\\enviromentDemoPy\\lib\\site-packages']
path_hooks = [<class 'zipimport.zipimporter'>, <function FileFinder.path_hook.<locals>.path_hook_for_FileFinder at 0x00000162A7B9E6A8>]
path_importer_cache = {'C:\\Repos\\GitHub\\DemoPy_Continous_Integration\\DemoWebAppPy\\enviromentDemoPy\\Scripts\\python36.zip': None, 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\DLLs': FileFinder('C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\DLLs'), 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib': FileFinder('C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib'), 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\encodings': FileFinder('C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\encodings'), 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64': FileFinder('C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64'), 'C:\\Repos\\GitHub\\DemoPy_Continous_Integration\\DemoWebAppPy\\enviromentDemoPy': FileFinder('C:\\Repos\\GitHub\\DemoPy_Continous_Integration\\DemoWebAppPy\\enviromentDemoPy'), 'C:\\Repos\\GitHub\\DemoPy_Continous_Integration\\DemoWebAppPy\\enviromentDemoPy\\lib\\site-packages': FileFinder('C:\\Repos\\GitHub\\DemoPy_Continous_Integration\\DemoWebAppPy\\enviromentDemoPy\\lib\\site-packages'), 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Preview\\Community\\Common7\\IDE\\Extensions\\Microsoft\\Python\\Core\\scrape_module.py': None, 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Preview\\Community\\Common7\\IDE\\Extensions\\Microsoft\\Python\\Core': FileFinder('C:\\Program Files (x86)\\Microsoft Visual Studio\\Preview\\Community\\Common7\\IDE\\Extensions\\Microsoft\\Python\\Core'), 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\collections': FileFinder('C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\collections'), 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\importlib': FileFinder('C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python36_64\\lib\\importlib')}
platform = 'win32'
prefix = 'C:\\Repos\\GitHub\\DemoPy_Continous_Integration\\DemoWebAppPy\\enviromentDemoPy'
def set_asyncgen_hooks():
    'set_asyncgen_hooks(*, firstiter=None, finalizer=None)\n\nSet a finalizer for async generators objects.'
    pass
def set_coroutine_wrapper(wrapper):
    'set_coroutine_wrapper(wrapper)\n\nSet a wrapper for coroutine objects.'
    pass
def setcheckinterval(n):
    'setcheckinterval(n)\n\nTell the Python interpreter to check for asynchronous events every\nn instructions.  This also affects how often thread switches occur.'
    pass
def setprofile(function):
    'setprofile(function)\n\nSet the profiling function.  It will be called on each function call\nand return.  See the profiler chapter in the library manual.'
    pass
def setrecursionlimit(n):
    'setrecursionlimit(n)\n\nSet the maximum depth of the Python interpreter stack to n.  This\nlimit prevents infinite recursion from causing an overflow of the C\nstack and crashing Python.  The highest possible limit is platform-\ndependent.'
    pass
def setswitchinterval(n):
    'setswitchinterval(n)\n\nSet the ideal thread switching delay inside the Python interpreter\nThe actual frequency of switching threads can be lower if the\ninterpreter executes long sequences of uninterruptible code\n(this is implementation-specific and workload-dependent).\n\nThe parameter must represent the desired switching delay in seconds\nA typical value is 0.005 (5 milliseconds).'
    pass
def settrace(function):
    'settrace(function)\n\nSet the global debug tracing function.  It will be called on each\nfunction call.  See the debugger chapter in the library manual.'
    pass
stderr = _io.TextIOWrapper()
stdin = _io.TextIOWrapper()
stdout = _io.TextIOWrapper()
class thread_info:
    'sys.thread_info\n\nA struct sequence holding information about the thread implementation.'
    def __add__(value):
        'Return self+value.'
        pass
    __class__ = thread_info
    def __contains__(key):
        'Return key in self.'
        pass
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
    def __getitem__(key):
        'Return self[key].'
        pass
    def __getnewargs__(self):
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
    def __iter__():
        'Implement iter(self).'
        pass
    def __le__(value):
        'Return self<=value.'
        pass
    def __len__():
        'Return len(self).'
        pass
    def __lt__(value):
        'Return self<value.'
        pass
    def __mul__(value):
        'Return self*value.n'
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
    def __rmul__(value):
        'Return self*value.'
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
    def count(self):
        'T.count(value) -> integer -- return number of occurrences of value'
        pass
    def index(self):
        'T.index(value, [start, [stop]]) -> integer -- return first index of value.\nRaises ValueError if the value is not present.'
        pass
    lock
    n_fields = 3
    n_sequence_fields = 3
    n_unnamed_fields = 0
    name = 'nt'
    version
version = '3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)]'
class version_info:
    'sys.version_info\n\nVersion information as a named tuple.'
    def __add__(value):
        'Return self+value.'
        pass
    __class__ = version_info
    def __contains__(key):
        'Return key in self.'
        pass
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
    def __getitem__(key):
        'Return self[key].'
        pass
    def __getnewargs__(self):
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
    def __iter__():
        'Implement iter(self).'
        pass
    def __le__(value):
        'Return self<=value.'
        pass
    def __len__():
        'Return len(self).'
        pass
    def __lt__(value):
        'Return self<value.'
        pass
    def __mul__(value):
        'Return self*value.n'
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
    def __rmul__(value):
        'Return self*value.'
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
    def count(self):
        'T.count(value) -> integer -- return number of occurrences of value'
        pass
    def index(self):
        'T.index(value, [start, [stop]]) -> integer -- return first index of value.\nRaises ValueError if the value is not present.'
        pass
    major = 3
    micro = 3
    minor = 6
    n_fields = 5
    n_sequence_fields = 5
    n_unnamed_fields = 0
    releaselevel = 'final'
    serial = 0
warnoptions = []
winver = '3.6'