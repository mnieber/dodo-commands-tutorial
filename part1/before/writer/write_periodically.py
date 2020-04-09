import time

while True:
    with open("../time.log", "a") as ofs:
        ofs.write("%f\n" % time.time())
    time.sleep(1)
