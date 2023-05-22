import random

class FSM:
    def __init__(self):
        self.start = self._create_start()
        self.sleep = self._sleep()
        self.eat = self._eat()
        self.study = self._study()
        self.cry = self._cry_bcs_of_studying()
        self.alarm = self._air_alarm()

        # setting current state of the system
        self.current_state = self.start

        # stopped flag to denote that iteration is stopped due to bad
        # input against which transition was not defined.
        self.stopped = False

        # Start the generators
        next(self.start)
        next(self.sleep)
        next(self.eat)
        next(self.study)
        next(self.cry)
        next(self.alarm)

    def send(self, time):
        """The function sends the current input to the current state
        It captures the StopIteration exception and marks the stopped flag.
        """
        try:
            self.current_state.send(time)
        except StopIteration:
            self.stopped = True

    def does_match(self):
        """The function at any point in time returns if till the current input
        the string matches the given regular expression.

        It does so by comparing the current state with the end state `study`.
        It also checks for `stopped` flag which sees that due to bad input the iteration of FSM had to be stopped.
        """
        if self.stopped:
            return False
        return self.current_state == self.study

    def _create_start(self):
        while True:
            time = yield
            if time in range(8):
                # sleep
                print("State: Sleep")
                self.current_state = self.sleep
            elif time in range(8, 10):
                # eat
                print("State: Eat")
                self.current_state = self.eat
            elif time in range(10, 14):
                # study
                print("State: Study")
                self.current_state = self.study
            elif time in range(14, 15):
                # cry
                print("State: Cry")
                self.current_state = self.cry
            elif time in range(15, 16):
                # eat
                print("State: Eat")
                self.current_state = self.eat
            elif time in range(16, 21):
                # study
                print("State: Study")
                self.current_state = self.study
            elif time in range(21, 22):
                # eat
                print("State: Eat")
                self.current_state = self.eat
            elif time in range(22, 24):
                # study
                print("State: Study")
                self.current_state = self.study
            else:
                print("Invalid time range. Exiting FSM.")
                break

    def _sleep(self):
        while True:
            time = yield
            if time in range(8):
                if random.random() > 0.3:
                    print("State: Sleep")
                    self.current_state = self.sleep
                else:
                    print("State: Alarm")
                    self.current_state = self.alarm
            else:
                self.current_state = self.eat if time in range(8, 10) else self.study
                yield None

    def _eat(self):
        while True:
            time = yield
            if time in range(8, 10):
                print("State: Eat")
                self.current_state = self.eat
            else:
                self.current_state = self.study if time in range(10, 14) or time in range(16, 21) or time in range(22, 24) else self.sleep
                yield None

    def _study(self):
        while True:
            time = yield
            if time in range(10, 14) or time in range(16, 21) or time in range(22, 24):
                print("State: Study")
                self.current_state = self.study
            else:
                self.current_state = self.eat if time in range(8, 10) else self.sleep
                yield None

    def _cry_bcs_of_studying(self):
        while True:
            time = yield
            if time in range(14, 15):
                self.current_state = self.cry
                print('State: Cry')
            else:
                self.current_state = random.choice([self.eat, self.study])
                print('State:', self.current_state.__name__)
                yield None

    def _air_alarm(self):
        while True:
            if random.random() > 0.9:
                print("Rockets are still flying...")
            else:
                self.current_state = random.choice([self.eat, self.sleep])
                print('State:', self.current_state.__name__)
            yield None

if __name__ == '__main__':
    fsm = FSM()
    time_range = range(24)

    for hour in time_range:
        print(f"Time: {hour}")
        fsm.send(hour)
        print('')
