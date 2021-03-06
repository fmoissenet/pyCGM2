# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info as _swig_python_version_info
# if _swig_python_version_info >= (2, 7, 0):
#     def swig_import_helper():
#         import importlib
#         pkg = __name__.rpartition('.')[0]
#         mname = '.'.join((pkg, '_ma')).lstrip('.')
#         try:
#             return importlib.import_module(mname)
#         except ImportError:
#             return importlib.import_module('_ma')
#     _ma = swig_import_helper()
#     del swig_import_helper
# elif _swig_python_version_info >= (2, 6, 0):
if _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ma', [dirname(__file__)])
        except ImportError:
            import _ma
            return _ma
        if fp is not None:
            try:
                _mod = imp.load_module('_ma', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ma = swig_import_helper()
    del swig_import_helper
else:
    import _ma
del _swig_python_version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

Sex_Unknown = _ma.Sex_Unknown
Sex_Male = _ma.Sex_Male
Sex_Female = _ma.Sex_Female
class Any(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Any, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Any, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _ma.new_Any(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ma.delete_Any
    __del__ = lambda self: None

    def dimensions(self):
        return _ma.Any_dimensions(self)

    def size(self):
        return _ma.Any_size(self)

    def isValid(self):
        return _ma.Any_isValid(self)

    def isEmpty(self):
        return _ma.Any_isEmpty(self)

    def swap(self, other):
        return _ma.Any_swap(self, other)

    def cast(self, *args):
        return _ma.Any_cast(self, *args)

    def assign(self, value):
        return _ma.Any_assign(self, value)
Any_swigregister = _ma.Any_swigregister
Any_swigregister(Any)

class Object(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Object, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Object, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _ma.delete_Object
    __del__ = lambda self: None

    def timestamp(self):
        return _ma.Object_timestamp(self)

    def modified(self):
        return _ma.Object_modified(self)
Object_swigregister = _ma.Object_swigregister
Object_swigregister(Object)

T_Node = _ma.T_Node
class Node(Object):
    __swig_setmethods__ = {}
    for _s in [Object]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Node, name, value)
    __swig_getmethods__ = {}
    for _s in [Object]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Node, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _ma.new_Node(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ma.delete_Node
    __del__ = lambda self: None

    def name(self):
        return _ma.Node_name(self)

    def setName(self, value):
        return _ma.Node_setName(self, value)

    def description(self):
        return _ma.Node_description(self)

    def setDescription(self, value):
        return _ma.Node_setDescription(self, value)

    def property(self, key):
        return _ma.Node_property(self, key)

    def setProperty(self, key, value):
        return _ma.Node_setProperty(self, key, value)

    def dynamicProperties(self):
        return _ma.Node_dynamicProperties(self)

    def child(self, index):
        return _ma.Node_child(self, index)

    def findChild(self, *args):
        return _ma.Node_findChild(self, *args)

    def findChildren(self, *args):
        return _ma.Node_findChildren(self, *args)

    def clear(self):
        return _ma.Node_clear(self)

    def children(self):
        return _ma.Node_children(self)

    def hasChildren(self):
        return _ma.Node_hasChildren(self)

    def parents(self):
        return _ma.Node_parents(self)

    def hasParents(self):
        return _ma.Node_hasParents(self)

    def addParent(self, node):
        return _ma.Node_addParent(self, node)

    def removeParent(self, node):
        return _ma.Node_removeParent(self, node)

    def copy(self, source):
        return _ma.Node_copy(self, source)

    def clone(self, parent=None):
        return _ma.Node_clone(self, parent)

    def modified(self):
        return _ma.Node_modified(self)
Node_swigregister = _ma.Node_swigregister
Node_swigregister(Node)

T_Event = _ma.T_Event
class Event(Node):
    __swig_setmethods__ = {}
    for _s in [Node]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Event, name, value)
    __swig_getmethods__ = {}
    for _s in [Node]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Event, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _ma.new_Event(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ma.delete_Event
    __del__ = lambda self: None

    def time(self):
        return _ma.Event_time(self)

    def setTime(self, value):
        return _ma.Event_setTime(self, value)

    def context(self):
        return _ma.Event_context(self)

    def setContext(self, value):
        return _ma.Event_setContext(self, value)

    def subject(self):
        return _ma.Event_subject(self)

    def setSubject(self, value):
        return _ma.Event_setSubject(self, value)
Event_swigregister = _ma.Event_swigregister
Event_swigregister(Event)

T_Subject = _ma.T_Subject
class Subject(Node):
    __swig_setmethods__ = {}
    for _s in [Node]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Subject, name, value)
    __swig_getmethods__ = {}
    for _s in [Node]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Subject, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _ma.new_Subject(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ma.delete_Subject
    __del__ = lambda self: None
Subject_swigregister = _ma.Subject_swigregister
Subject_swigregister(Subject)

T_TimeSequence = _ma.T_TimeSequence
class TimeSequence(Node):
    __swig_setmethods__ = {}
    for _s in [Node]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, TimeSequence, name, value)
    __swig_getmethods__ = {}
    for _s in [Node]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, TimeSequence, name)
    __repr__ = _swig_repr
    Type_Unknown = _ma.TimeSequence_Type_Unknown
    Type_Reconstructed = _ma.TimeSequence_Type_Reconstructed
    Type_Marker = _ma.TimeSequence_Type_Marker
    Type_Angle = _ma.TimeSequence_Type_Angle
    Type_Force = _ma.TimeSequence_Type_Force
    Type_Moment = _ma.TimeSequence_Type_Moment
    Type_Power = _ma.TimeSequence_Type_Power
    Type_Scalar = _ma.TimeSequence_Type_Scalar
    Type_Pose = _ma.TimeSequence_Type_Pose
    Type_Analog = _ma.TimeSequence_Type_Analog
    Type_Other = _ma.TimeSequence_Type_Other

    def __init__(self, *args):
        this = _ma.new_TimeSequence(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ma.delete_TimeSequence
    __del__ = lambda self: None

    def sampleRate(self):
        return _ma.TimeSequence_sampleRate(self)

    def setSampleRate(self, value):
        return _ma.TimeSequence_setSampleRate(self, value)

    def dimensions(self):
        return _ma.TimeSequence_dimensions(self)

    def samples(self):
        return _ma.TimeSequence_samples(self)

    def components(self):
        return _ma.TimeSequence_components(self)

    def elements(self):
        return _ma.TimeSequence_elements(self)

    def duration(self):
        return _ma.TimeSequence_duration(self)

    def type(self):
        return _ma.TimeSequence_type(self)

    def setType(self, value):
        return _ma.TimeSequence_setType(self, value)

    def unit(self):
        return _ma.TimeSequence_unit(self)

    def setUnit(self, value):
        return _ma.TimeSequence_setUnit(self, value)

    def startTime(self):
        return _ma.TimeSequence_startTime(self)

    def setStartTime(self, value):
        return _ma.TimeSequence_setStartTime(self, value)

    def scale(self):
        return _ma.TimeSequence_scale(self)

    def setScale(self, value):
        return _ma.TimeSequence_setScale(self, value)

    def offset(self):
        return _ma.TimeSequence_offset(self)

    def setOffset(self, value):
        return _ma.TimeSequence_setOffset(self, value)

    def range(self):
        return _ma.TimeSequence_range(self)

    def setRange(self, value):
        return _ma.TimeSequence_setRange(self, value)

    def data(self):
        return _ma.TimeSequence_data(self)

    def setData(self, data):
        return _ma.TimeSequence_setData(self, data)

    def resize(self, samples):
        return _ma.TimeSequence_resize(self, samples)
TimeSequence_swigregister = _ma.TimeSequence_swigregister
TimeSequence_swigregister(TimeSequence)
cvar = _ma.cvar
TimeSequence.InfinityRange = _ma.cvar.TimeSequence_InfinityRange

T_Trial = _ma.T_Trial
class Trial(Node):
    __swig_setmethods__ = {}
    for _s in [Node]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Trial, name, value)
    __swig_getmethods__ = {}
    for _s in [Node]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Trial, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _ma.new_Trial(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ma.delete_Trial
    __del__ = lambda self: None

    def timeSequences(self):
        return _ma.Trial_timeSequences(self)

    def events(self):
        return _ma.Trial_events(self)

    def timeSequence(self, idx):
        return _ma.Trial_timeSequence(self, idx)

    def event(self, idx):
        return _ma.Trial_event(self, idx)
Trial_swigregister = _ma.Trial_swigregister
Trial_swigregister(Trial)

class Logger(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Logger, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Logger, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        mute = staticmethod(_ma.Logger_mute)
    else:
        mute = _ma.Logger_mute
    __swig_destroy__ = _ma.delete_Logger
    __del__ = lambda self: None
Logger_swigregister = _ma.Logger_swigregister
Logger_swigregister(Logger)

def Logger_mute(active):
    return _ma.Logger_mute(active)
Logger_mute = _ma.Logger_mute

T_Hardware = _ma.T_Hardware
class Hardware(Node):
    __swig_setmethods__ = {}
    for _s in [Node]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Hardware, name, value)
    __swig_getmethods__ = {}
    for _s in [Node]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Hardware, name)
    __repr__ = _swig_repr

    def __init__(self, other):
        this = _ma.new_Hardware(other)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def channels(self):
        return _ma.Hardware_channels(self)

    def channelsNumberRequired(self):
        return _ma.Hardware_channelsNumberRequired(self)

    def outputs(self):
        return _ma.Hardware_outputs(self)

    def channel(self, *args):
        return _ma.Hardware_channel(self, *args)

    def setChannel(self, *args):
        return _ma.Hardware_setChannel(self, *args)
    __swig_destroy__ = _ma.delete_Hardware
    __del__ = lambda self: None
Hardware_swigregister = _ma.Hardware_swigregister
Hardware_swigregister(Hardware)

# This file is compatible with both classic and new-style classes.
