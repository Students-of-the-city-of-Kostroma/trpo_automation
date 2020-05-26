import inspect 
import logging 
logging.basicConfig(filename="log2.txt", level = logging.DEBUG) 
name = None
arg=arg1=arg2=arg3=None
class Logs:
    def __init__(self):
        pass

    
        
    
    def Infor (self,name, *args, **kwargs):
        self.name = name
        try:
            logging.info("Program started")
            logging.info("Вызвана функция %s " % name)
            
            if(args.__len__()==1):
                arg1=args[0]
                
                logging.debug('Параметр %s', arg1)
                
            if(args.__len__()==2):
                arg1=args[0]
                arg2=args[1]
                
                logging.debug('Параметры: %s, %s', arg1, arg2) 
                

            if(args.__len__()==3):
                arg1=args[0]
                arg2=args[1]
                arg3=args[2]
                logging.debug('Параметры: %s, %s, %s ', arg1, arg2, arg3)

            if(args.__len__()==4):
                arg1=args[0]
                arg2=args[1]
                arg3=args[2]
                arg4=args[3]

                logging.debug('Параметры: %s, %s, %s, %s',arg1, arg2, arg3, arg4)

               
        
        except Exception as e: 
            logging.error(str(e)) 
         

        finally: 
            logging.info("Program end")
  
