# Finite-State-Machine

Model your day in life :) Every hour (you can take smaller time intervals if you wish) you can be in one of the states (Sleep, Eat, Work, ...). The transition between these states can occur both deterministically (with each time interval) and as a reaction to some external events (non-deterministically, as a result of a random event).

<pre>
        +---------------------+
        |        Start        |
        +----------+----------+
                   |
            +------+-------+
            |              |
            v              |
   +--------------------+  |        +--------+
   |        Sleep       +--+        |  Alarm |
   +---------+----------+           +---+----+
             |                         |
             |                         |
    +--------+--------+                |
    |       Eat       +<---------------+
    +--------+--------+
             |
             |
    +--------+--------+
    |       Study      |
    +--------+--------+
             |
             |
    +--------+--------+
    |       Cry        |
    +-----------------+

</pre>

Output examples:

<pre>
Time: 0
State: Sleep

Time: 1
State: Sleep

Time: 2
State: Sleep

Time: 3
State: Sleep

Time: 4
State: Alarm

Time: 5

Time: 6
State: _sleep

Time: 7
State: Sleep

Time: 8
State: _study

Time: 9
State: _eat

Time: 10

Time: 11
State: _sleep

Time: 12

Time: 13
State: _eat

Time: 14

Time: 15
State: _sleep

Time: 16

Time: 17
State: _study

Time: 18

Time: 19
State: Study

Time: 20
State: Study

Time: 21
State: _eat

Time: 22

Time: 23
State: _sleep
</pre>

Notes:
1) Some lines are empty because states are not defined in some cases
2) Due to random events states can be present in inappropriate time(for ex. sleep at noon)


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
