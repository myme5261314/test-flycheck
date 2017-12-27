#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# created at [CST 2017/11/21 (Tue)]
#
# Peng Liu, <myme5261314@gmail.com>
#
# Distributed under terms of the gplv3 license.

"""
This project aims to implement a platform to resign ios app.
"""
from ipa_resign_platform.core import create_app

if __name__ == "__main__":  # pragma: no cover
    app = create_app()
    # logging.basicConfig(level=logging.NOTSET)
    app.run(host=app.config['HOST'], port=app.config['PORT'],
            threaded=True,
            debug=app.config.get('DEBUG', True))
else:
    app = create_app()
