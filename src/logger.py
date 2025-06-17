#logger purpose 
# any exceution is  happenng we should be log all the information and exceution even the error or customeexception error


import logging
import os 
from datetime import datetime 

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # filename will be create  dattime 
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) # whatever the log will created it will be respect to the working directory log folder will be created  every folder will be created log 
os.makedirs(logs_path,exist_ok=True) # even there is a log file keep on appending the  file or folder 


LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(

    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO,
    #format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s",

)

if __name__=="__main__":
    logging.info("Logging has started")

#with respect with the logging we really need to set up the basic config



# what we will doo whenever we get the excetion we will take that exception  with the logging into the logger file and use login.info()
# to put it inside the file night so in such we will getthe folder also