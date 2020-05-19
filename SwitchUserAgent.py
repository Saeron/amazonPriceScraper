import linecache
import random


class SwitchUserAgent:

    def __init__(self, file_name):
        self.file_name = file_name
        self.num = 0

    def next_user_agent(self):
        user_agent = linecache.getline(self.file_name, self.num)
        self.num += 1
        return user_agent

    def random_user_agent(self, num_lines):
        rnd = random.randrange(num_lines)
        return linecache.getline(self.file_name, rnd)


