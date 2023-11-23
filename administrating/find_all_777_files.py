import os


#kustutab kõik 777 failid pathis ära 

path = "/home/hejoes/test"  

files = os.listdir(path)

for file in files:
    
    # os.chmod(path + "/" + file, 0o777)
    
    mask = oct(os.stat(path + "/" + file).st_mode)[-3:]
    
    if int(mask) == 777:
      os.remove(path + "/" + file)

