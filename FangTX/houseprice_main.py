# -*- coding: utf-8 -*-
from scrapy import cmdline


cmdline.execute("scrapy crawl houseprice -s LOG_FILE=scrapy.log".split())