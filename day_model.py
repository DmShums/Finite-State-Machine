"""Finite-State-Machine"""

import random

class FSM:
    """
    Model your day in life
    Every hour (you can take smaller time intervals if you wish)
    you can be in one of the states 
    """
    def __init__(self):
        # main events
        self.sleep = self._sleep()
        self.eat = self._eat()
        self.study = self._study()
        self.cry = self._cry_bcs_of_studying()
        self.dog = self._walk_a_dog()

        # random events
        self.alarm = self._air_alarm()
        self.music = self._music()
        self.twitter = self._read_twitter()

        # setting current state of the system
        self.current_state = self.sleep

        # stopped flag to denote that iteration is stopped due to bad
        # input against which transition was not defined.
        self.stopped = False

        # Start the generators
        next(self.sleep)
        next(self.eat)
        next(self.study)
        next(self.cry)
        next(self.dog)
        next(self.alarm)
        next(self.music)
        next(self.twitter)

    def does_match(self):
        """
        The function at any point in time returns if till the current input
        the string matches the given regular expression.

        It does so by comparing the current state with the end state `study`.
        It also checks for `stopped` flag which sees that due to bad input the
        iteration of FSM had to be stopped.
        """
        if self.stopped:
            return False
        return self.current_state == self.study

    def cycle(self):
        """Day cycle"""
        for i in range(24):
            self.current_state.send(i)

    def _sleep(self):
        while True:
            time = yield
            print(f'\nHour {time}')
            print('State: Sleep')
            if time in range(8):
                rand=random.random()
                if rand> 0.8:
                    self.current_state = self.sleep
                else:
                    self.current_state = self.alarm
            else:
                self.current_state = random.choice([self.eat, self.study])

    def _eat(self):
        while True:
            time = yield
            print(f'\nHour {time}')
            print('State: Eat')
            if random.random() > 0.3:
                if time in range(8, 10):
                    self.current_state = self.eat
                else:
                    self.current_state = random.choice([self.study, self.sleep])
            else:
                self.current_state = self.twitter

    def _study(self):
        while True:
            time = yield
            print(f'\nHour {time}')
            print('State: Study')
            if random.random() > 0.3:
                if time in range(10, 14) or time in range(19, 21) or time in range(22, 24):
                    self.current_state = self.study
                else:
                    self.current_state = random.choice([self.eat, self.dog])
            else:
                self.current_state = self.music

    def _cry_bcs_of_studying(self):
        while True:
            time = yield
            print(f'\nHour {time}')
            print('State: Cry')
            if time in range(14, 15):
                self.current_state = self.cry
            else:
                self.current_state = random.choice([self.eat, self.sleep])

    def _walk_a_dog(self):
        while True:
            time = yield
            print(f'\nHour {time}')
            print('State: Walk a dog')
            if time in range(18, 19):
                self.current_state = self.dog
            else:
                self.current_state = self.study


    def _air_alarm(self):
        while True:
            time = yield
            print(f'\nHour {time}')
            print("State: Alarm")
            rand = random.random()
            if rand < 0.2:
                self.current_state = self.eat
            else:
                self.current_state = self.sleep

    def _music(self):
        while True:
            time = yield
            print(f'\nHour {time}')
            print("State: Listen to music")
            rand = random.random()
            if rand < 0.9:
                self.current_state = self.study
            else:
                self.current_state = self.music

    def _read_twitter(self):
        while True:
            time = yield
            print(f'\nHour {time}')
            print("State: Read twitter")
            rand = random.random()
            if rand < 0.9:
                self.current_state = self.eat
            else:
                self.current_state = self.twitter

if __name__ == '__main__':
    fsm = FSM()
    fsm.cycle()
