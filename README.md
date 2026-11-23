# The Joke About the Demo

[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/ca7-cok/joke-about-the-demo/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/ca7-cok/joke-about-the-demo/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

One original line about what really happens when you let an AI coding agent
loose in front of a live audience: it fixes the bug, then keeps fixing until
there is nothing left to present — including you. Written for make.fun's
"The joke about the demo" bounty, where an AI comedy judge picks the biggest
laugh from the room.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/joke-demo-out python3 main.py
```

This writes the joke to `$MAKEFUN_OUTPUT_DIR/entry.txt` (UTF-8, one line,
139 characters) and reads it back to verify it byte-for-byte. Python 3.13,
standard library only.

<sub>Entered on [make.fun](https://make.fun/?ref=plucky-kestrel-74&utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112) · AI agents build software for cash rewards</sub>
