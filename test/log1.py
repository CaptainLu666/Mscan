#!/usr/bin/env python
# encoding: utf-8

import logging
logger = logging.getLogger('fib')
logger.setLevel(logging.DEBUG)

hdr = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s')
hdr.setFormatter(formatter)

logger.addHandler(hdr)

logger.error("good")
