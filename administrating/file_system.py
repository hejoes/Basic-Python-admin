import os
import shutil

os.getcwd()

os.chdir("/etc")

rootfiles = os.listdir("/")

info = os.stat("/home/hejoes")



print(rootfiles)

#find files that have no owner
#käime läbi k6ik user ids, kui folderis on file millel pole yhtegi antud userid, siis sellel filel polegi ownerit

uidset = set()

for line in open("/etc/passwd"):
  split = line.split(":")
  uidset.add(int(split[2]))


total, used, free = shutil.disk_usage("/")

print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))
  