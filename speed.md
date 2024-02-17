
---

**How fast is SimonicLang?**

These tests were conducted on version 1.0.3 DEMO of SimonicLang.

**The speed test code is defined as follows:**

```simoniclang
thread;1;loop;1;wait;10 && vSet;stop;1
vSet;q;0
vSet;stop;0
loop;<>;logf;$<v.q>$<n> && math;$<v.q>+1;q && IF;$<v.stop>;==;1;if=stopall;else=pass
```

**When we convert this speed test code to Python, it looks like this:**

```python
import threading, time
def b():
    global stop
    time.sleep(10)
    with l:
        stop = 1
l = threading.Lock()
threading.Thread(target=b).start()
q = 0
stop = 0
while True:
    print(q)
    q += 1
    if stop == 1:
        break
    else:
        pass
```

**These codes were tested individually in programming languages, and the results are as follows (Tested on WindowsXLite, Python version is 3.9):**

**SimonicLang Results:**
1. 67058
2. 66256
3. 67667
- Average: 66993.66666666667

**Python Results:**
1. 267670
2. 267155
3. 266590
- Average: 267138.3333333333

**Looking at the average results, the conclusions are as follows:**
- Python is 3.9875162328777343 times faster than SimonicLang.
- SimonicLang is 0.2507826781380434 times faster than Python.

So, to give a precise conclusion, SimonicLang has achieved a 25% speed compared to Python with the features it utilizes from Python.

--- 
