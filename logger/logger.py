import pymongo
import datetime

class MongoOperations:

    def __init__(self):
        try:
            path = "mongodb+srv://test:test@cluster0.8kinx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
            self.client = pymongo.MongoClient(path)
            self.db = self.client['GetToWork']
            self.collection = self.db['logs']
            print("Mongodb Connection Established")
        except Exception as e:
            print(e.__str__)

        
    def insert_logs(self, log_msg):
        print("insertlogs")
        try:
            message_dict = self.log_msg_to_dict(log_msg)
            rec = self.collection.insert_one(message_dict)
            if rec:
                print(rec, 'success')
            else:
                print("failed")
        except Exception as e:
            print(e)

    def log_msg_to_dict(self, log_msg):
        try:
            log_dict = {}
            data = log_msg.split("::")
            log_dict['Timestamp'] = data[0]
            log_dict['Filesource'] = data[1]
            log_dict['Loglevel'] = data[2]
            log_dict['Message'] = data[3]
            return log_dict
        except Exception as e:
            print(e)
    
        def __str__(self):
            return "MongoOperations Class"

class Applogs(MongoOperations):
    def __init__(self, logfile, setlevel):
        global log_levels
        self.logfile = logfile
        self.mongo_db_object = MongoOperations()
        self.setlevel = setlevel
        log_levels = {"NOTSET":0, "DEBUG":10, "INFO":20, "WARNING":30, "ERROR":40, "CRITICAL":50}
        self.sourcefile = ""
    
    def writelog(self, level, message):
        try:
            timestamp = datetime.datetime.now()
            filename = self.sourcefile
            level_ = log_levels[level]
            if  level_ >= log_levels[self.setlevel]:
                log_msg = f"{timestamp}::{filename}::{level}::{message}\n"
                return log_msg
            else:
                return None
        except Exception as e:
            print(e)
      
    def debug(self, message):
        try:
            log_msg = self.writelog("DEBUG", message)
            if log_msg != None:
                self.launchlogs(self.logfile, log_msg)
        except Exception as e:
            print(e)
    
    def info(self, message):
        try:
            log_msg = self.writelog("INFO", message)
            if log_msg != None:
                self.launchlogs(self.logfile, log_msg)
        except Exception as e:
            print(e)

    def warning(self, message):
        try:
            log_msg = self.writelog("WARNING", message)
            if log_msg != None:
                self.launchlogs(self.logfile, log_msg)
        except Exception as e:
            print(e)

    def error(self, message):
        try:
            log_msg = self.writelog("ERROR", message)
            if log_msg != None:
                self.launchlogs(self.logfile, log_msg)
        except Exception as e:
            print(e)

    def critical(self, message):
        try:
            log_msg = self.writelog("CRITICAL", message)
            if log_msg != None:
                self.launchlogs(self.logfile, log_msg)
        except Exception as e:
            print(e)

    def getlogger(self, sourcefilename):
        try:
            self.sourcefile = sourcefilename
        except Exception as e:
            print(e)

    def write_to_logfile(self, filepath, message):
        try:
            with open(filepath, 'a+') as file:
                file.write(message)
        except Exception as e:
            print(e)
    
    def launchlogs(self, logfile, log_msg):
        try:
            self.write_to_logfile(logfile, log_msg)
            self.mongo_db_object.insert_logs(log_msg)
        except Exception as e:
            print(e)

    def __str__(self):
        return "Applogs Class"

