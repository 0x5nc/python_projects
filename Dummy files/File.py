"""
This is a dummy file 
"""
import datetime

filename = datetime.datetime.now()
def manip():
    """This is my manipulation function"""
    with open(filename.strftime("%Y-%m-%d-%H-%M-%S-%f"),'w+') as file :
        file.write(str(datetime.datetime.now()))

manip()