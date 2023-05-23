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
Hour 0
State: Sleep

Hour 1
State: Alarm

Hour 2
State: Eat

Hour 3
State: Sleep

Hour 4
State: Sleep

Hour 5
State: Alarm

Hour 6
State: Sleep

Hour 7
State: Alarm

Hour 8
State: Eat

Hour 9
State: Eat

Hour 10
State: Eat

Hour 11
State: Study

Hour 12
State: Study

Hour 13
State: Study

Hour 14
State: Study

Hour 15
State: Sleep

Hour 16
State: Study

Hour 17
State: Study

Hour 18
State: Study

Hour 19
State: Study

Hour 20
State: Study

Hour 21
State: Study

Hour 22
State: Sleep

Hour 23
State: Study
</pre>

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
