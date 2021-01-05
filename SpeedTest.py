#!/usr/bin/env python3

import sys
import subprocess
try:
    import speedtest
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'speedtest-cli'])
finally:
    import speedtest
    test = speedtest.Speedtest()
    print("Checking your download speed...")
    down = test.download()   # tests download speed
    print("Done...")
    print("Now checking your upload speed...")
    up = test.upload()       # tests upload speed
    print("Done...")
    print("Download Speed: {:.2f} Mb/s \nUpload Speed: {:.2f} Mb/ss".format(down / 1024 * 0.0009765625, up / 1024 * 0.0009765625))
