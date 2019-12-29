# Copyright (C) 2015 Optiv, Inc. (brad.spengler@optiv.com)
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import os

from lib.common.abstracts import Package

class Extraction_JS(Package):
    """JavaScript analysis package."""
    PATHS = [
        ("SystemRoot", "system32", "wscript.exe"),
    ]

    def __init__(self, options={}, config=None):
        """@param options: options dict."""
        self.config = config
        self.options = options
        self.options["dll"] = "Extraction.dll"
        self.options["dll_64"] = "Extraction_x64.dll"

    def start(self, path):
        wscript = self.get_path("wscript.exe")
        args = "\"%s\"" % path
        ext = os.path.splitext(path)[-1].lower()
        if ext != ".js" and ext != ".jse":
            if os.path.isfile(path) and "#@~^" in open(path, "rb").read(100):
                os.rename(path,path + ".jse")
                path = path + ".jse"
            else:
                os.rename(path,path + ".js")
                path = path + ".js"
        args = "\"%s\"" % path
        return self.execute(wscript, args, path)
