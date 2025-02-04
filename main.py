import time
f=open(f"{time.time()}.txt","w")
f.write(f"{time.ctime()} by {__file__}")
f.close()
