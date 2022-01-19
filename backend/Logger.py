RED = '\033[93m'
END = '\033[93m'

class Logger:
  @staticmethod
  def red(printable):
    return f"{RED}{printable}{END}"
