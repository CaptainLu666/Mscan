#!/usr/bin/env python
# encoding: utf-8
import logging

#logging.basicConfig(filename='logger.log',level=logging.INFO)
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s : %(message)s")
message = '"fuck you" "fuck you to"'
logging.debug(message)
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')

