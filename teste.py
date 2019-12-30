import time as t
import datetime
from datetime import datetime


now= datetime.now()
today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)


print (now)
print (today8am)
print(today8am <= now or today8am <=  today8am )