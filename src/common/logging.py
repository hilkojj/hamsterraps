import sys

class Logger(object):
  def __init__(self, logfile):
    self.terminal = sys.stdout
    self.log = open(logfile, "w")

  def write(self, message):
    self.terminal.write(message)
    self.log.write(message)
    self.log.flush()  # save new contents NOW

  def flush(self):
    self.log.flush()

def log_to(file):
  # todo: write stderr to stderr instead of stdout. Also give it a color?
  sys.stdout = Logger(file)
  sys.stderr = sys.stdout
