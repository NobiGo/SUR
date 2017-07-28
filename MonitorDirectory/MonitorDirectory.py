# coding:utf-8
import sys
import time
import logging
import os
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from ChangeJsonToTable import TransJsonToHtml
from  CreateJsonFile import ReadFileToDict

# 文件被创建时，触发的内容
from watchdog.events import FileCreatedEvent


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == "..\AndoridServer\patientInfo":  # 监控指定文件内容、权限等变化
            print "log file %s changed!" % event.src_path

class HandlerFile(FileSystemEventHandler):
    def on_modified(self, event):
        print "patient file be modified!" + event.src_path
        filePath = str(event.src_path).replace("\\", "/")
        fileName = open(filePath, "a+").readline()
        #print  filePath
        #print filePath.split("/")[3]
        print  os.path.dirname(__file__)
        #print  fileName.split("：")[1] + ".json"
        ReadFileToDict.ReadFileToDict(filePath.split("/")[3])
        fileName = fileName.split("：")[1].replace("\n", "")+".json"
        print  fileName
        TransJsonToHtml.createHtmlTable(u"../病历/"+fileName,os.path.dirname(__file__))
        # print
        # with event.src_path as fileInfor:
        # print fileInfor.read()
    def on_created(self, event):
        print "patient file be created" + event.src_path

    def on_deleted(self, event):
        print "patient file be deleted" + event.src_path

    def on_moved(self, event):
        print "patient file be movesd" + event.src_path


if __name__ == "__main__":
    # 当指定目录发生任何辩护，都会打印消息到终端
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    # 监控特定目录内容变化
    path = "..\AndoridServer\patientFile"
    # event_handler = LoggingEventHandler()
    handler = HandlerFile()
    observer = Observer()
    # observer.schedule(event_handler, path, recursive=False)
    observer.schedule(handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
