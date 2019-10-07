#!/usr/bin/python
import json
import os


def vote(input_data, state_file):

    candidate_name = input_data["candidate_name"]
    voter = os.environ.get('SENDER')

    if voter == None:
        raise Exception("voter shouldn't be empty")

    if os.stat(state_file).st_size == 0:
        current_state_data = {}
    else:
        with open(state_file, "r") as json_file:
            current_state_data = json.load(json_file)

    if "voters" not in current_state_data:
        current_state_data["voters"] = []
    if "candidates" not in current_state_data:
        current_state_data["candidates"] = {}

    if voter not in current_state_data["voters"]:
        current_state_data["voters"].append(voter)
        if candidate_name not in current_state_data["candidates"]:
            current_state_data["candidates"][candidate_name] = 0
        current_state_data["candidates"][candidate_name] = current_state_data["candidates"][candidate_name] + 1
    else:
        raise Exception("you have already voted!")

    with open(state_file, "w") as json_file:
        json.dump(current_state_data, json_file)


def get_votes(input_data):
    state_file = input_data["state_file"]
    candidate_name = input_data["arguments"][0]

    with open(state_file, "r") as json_file:
        json_data = json.load(json_file)

    print(json_data["candidates"][candidate_name])


def start(input_file, state_file):
    with open(input_file, "r") as f:
        input_data = json.load(f)

    function = input_data["function"]

    if function == "vote":
        vote(input_data, state_file)
    elif function == "get_votes":
        get_votes(input_data)


if __name__ == '__main__':
    start("/input", "/state")
