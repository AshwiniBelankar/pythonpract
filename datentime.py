from datetime import datetime as dt
if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):
    print("Working hours....")
else:
    print("fun hours")