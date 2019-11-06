from vote import *
import tempfile
import os

os.environ["SENDER"] = "test_user"

input_file = os.getcwd() + "/sample_setter_input_file.json"
state_file = tempfile.mkstemp()
start(input_file, state_file[1])

input_file = os.getcwd() + "/sample_getter_input_file.json"
start(input_file, state_file[1])
