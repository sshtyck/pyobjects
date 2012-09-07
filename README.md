pyobjects
=========

Script that prints all the variables, classes, class methods and functions from a python module.

`Usage: ./pyobjects.py </usr/lib/python2.7/module.py>`

For example:
```
debian@debian:/mnt/docs/dev/git/pyobjects$ ./pyobjects.py /usr/lib/python2.7/email/message.py
message.__all__
message.SEMISPACE
message.tspecials
message.Message
    message.Message.__init__(self)
    message.Message.__str__(self)
    message.Message.as_string(self, unixfrom=False)
    message.Message.is_multipart(self)
    message.Message.set_unixfrom(self, unixfrom)
    message.Message.get_unixfrom(self)
    message.Message.attach(self, payload)
    message.Message.get_payload(self, i=None, decode=False)
    message.Message.set_payload(self, payload, charset=None)
    message.Message.set_charset(self, charset)
    message.Message.get_charset(self)
    message.Message.__len__(self)
    message.Message.__getitem__(self, name)
    message.Message.__setitem__(self, name, val)
    message.Message.__delitem__(self, name)
    message.Message.__contains__(self, name)
    message.Message.has_key(self, name)
    message.Message.keys(self)
    message.Message.values(self)
    message.Message.items(self)
    message.Message.get(self, name, failobj=None)
    message.Message.get_all(self, name, failobj=None)
    message.Message.add_header(self, _name, _value, **_params)
    message.Message.replace_header(self, _name, _value)
    message.Message.get_content_type(self)
    message.Message.get_content_maintype(self)
    message.Message.get_content_subtype(self)
    message.Message.get_default_type(self)
    message.Message.set_default_type(self, ctype)
    message.Message._get_params_preserve(self, failobj, header)
    message.Message.get_params(self, failobj=None, header='content-type', unquote=True)
    message.Message.get_param(self, param, failobj=None, header='content-type', unquote=True)
    message.Message.set_param(self, param, value, header='Content-Type', requote=True, charset=None, language='')
    message.Message.del_param(self, param, header='content-type', requote=True)
    message.Message.set_type(self, type, header='Content-Type', requote=True)
    message.Message.get_filename(self, failobj=None)
    message.Message.get_boundary(self, failobj=None)
    message.Message.set_boundary(self, boundary)
    message.Message.get_content_charset(self, failobj=None)
    message.Message.get_charsets(self, failobj=None)
message._splitparam(param)
message._formatparam(param, value=None, quote=True)
message._parseparam(s)
message._unquotevalue(value)
```