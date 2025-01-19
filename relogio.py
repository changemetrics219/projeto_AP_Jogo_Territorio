import time
import sys

def contador():
    for i in range(0, 1000):
        sys.stdout.write(f"\r{i}")
        sys.stdout.flush()
        time.sleep(1)
    print("\nFim")