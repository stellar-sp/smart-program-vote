from vote import *
import tempfile
import os

state_file = tempfile.mkstemp()

start(os.getcwd() + "/input_file_sample.json", state_file[1])
