import sys
import random
import datetime
import config
from twython import Twython
import random

twitter = Twython("",
                  "",
                  "",
                  "")


def get_line(file_name):
    lines = open(file_name, encoding="utf8").read().splitlines()
    myline =random.choice(lines)
    return myline


def tweet(sentence):
    try:
        sys.stdout.write("{} {}\n".format(len(sentence), sentence))
        twitter.update_status(status=sentence)
    except:
        pass


def do_tweet(file_name):
    line = get_line(file_name)
    tweet(line)

def main(event, context):
    file_name = config.config_vars['text_file_path']
    do_tweet(file_name)
