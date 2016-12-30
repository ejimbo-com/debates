# _*_ coding:utf-8 _*_
import logging
import re
import copy
import app_config
import doc_config
import parse_doc
from jinja2 import Environment, FileSystemLoader
from bs4 import BeautifulSoup

def create_list(uncleaned_list):
    """
    takes list of unicode strings and transforms
    to an html list. sends back markup of list
    """
    list_items = ''
    for item in uncleaned_list:
        list_items += '<li>%s</li>' % item
    list = '<div class="embed"><ul>%s</ul></div>' % list_items
    return list
