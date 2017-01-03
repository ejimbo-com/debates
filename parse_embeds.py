# _*_ coding:utf-8 _*_
import logging
import re
import copy
import app_config
import doc_config
import parse_doc
from jinja2 import Environment, FileSystemLoader
from bs4 import BeautifulSoup

logging.basicConfig(format=app_config.LOG_FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(app_config.LOG_LEVEL)

extract_shortcode_items_regex = re.compile(
    ur'^\s*(\w+\S)\s*(.*)', re.UNICODE)
extract_shortcode_contents_regex = re.compile(
    ur'^\s*(\w+\S)\s*.*', re.UNICODE)
extract_list_items_regex = re.compile(
    ur'“(.*?)”', re.UNICODE)

def shortcode_parser(shortcode):
    contents = extract_shortcode_items_regex.match(shortcode)
    embed_type = contents.group(1)
    embed_attributes = contents.group(2)
    try:
        embed = SHORTCODE_DICT[embed_type](embed_attributes)
        return embed
        # need a fail safe in case shortcode embed type isn't found
    except KeyError:
        default()

def create_list(attrs):
    """
    takes list of unicode strings and transforms
    to an html list. sends back markup of list
    """
    items = extract_list_items_regex.findall(attrs)
    list_items = ''
    for item in items:
        list_items += '<li>%s</li>' % item
    embed = '<div class="embed"><ul>%s</ul></div>' % list_items
    return embed
def create_graphic(attrs):
    """
    TKTKTK
    """
    embed = '<div class="embed"><img class="graphic" src="%s" /></div>' % attrs
    return embed

def create_table(attrs):
    """
    TKTKTK
    """
    logger.info('create table')

def create_image(attrs):
    """
    TKTKTK
    """
    embed = '<div class="embed"><img class="image" src="%s" /></div>' % attrs
    return embed

def create_youtube(attrs):
    """
    TKTKTK
    """
    logger.info('create youtube')

def create_tweet(attrs):
    """
    TKTKTK
    """
    logger.info('create tweet')

def create_facebook(attrs):
    """
    TKTKTK
    """
    logger.info('create facebook')

def create_link(attrs):
    """
    TKTKTK
    """
    logger.info('create link')

SHORTCODE_DICT = {
    'list': create_list,
    'table': create_table,
    'graphic': create_graphic,
    'image': create_image,
    'youtube': create_youtube,
    'tweet': create_tweet,
    'facebook': create_facebook,
    'link': create_link
}
