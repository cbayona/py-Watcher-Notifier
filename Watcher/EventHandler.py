import pyinotify
import time
import logging


class Handler(pyinotify.ProcessEvent):

   def __init__(self, logging):
      self.logging = logging

   def process_IN_CREATE(self, event):

      self.write(event, "CREATED")

   def process_IN_DELETE(self, event):
      
      self.write(event, "DELETED")

   def process_IN_MODIFY(self, event):
      
      self.write(event, "EDITED")

   def process_IN_MOVED_FROM(self, event):
      
      self.write(event, "RENAMED-FROM")

   def process_IN_MOVED_TO(self, event):
      
      self.write(event, "RENAMED-TO")

   def write(self, event, label):

      t = time.strftime("%Y-%m-%d %H:%M:%S %Z")
      x = "[" + t + "] " + label + " -> " + event.pathname

      self.logging.debug(x)
