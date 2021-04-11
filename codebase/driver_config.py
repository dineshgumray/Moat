import os

PARENT_DIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
DRIVER_PATH = r"{}\driver\chromedriver.exe".format(PARENT_DIR)
OUTPUT_FILENAME = "result.txt"
OUTPUT_PATH = r"{}\result\{}".format(PARENT_DIR, OUTPUT_FILENAME)