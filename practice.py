import sys
import time
while True:
    sys.stdout.write("/ ")
    time.sleep(1)
    sys.stdout.write("-- ")
    time.sleep(1)
    sys.stdout.write("\\ ")
    time.sleep(1)
    
    sys.stdout.flush()

