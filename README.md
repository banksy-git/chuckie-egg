![Chuckie egg logo](./docs/logo.png)

# Chuckie Egg for BBC model B (32k) - with Persistent High Scores

Original game author: A&F Software
Hack author: Paul G. Banks <https://paulbanks.org/>

This is a new hack of the classic Chuckie Egg platform game for the BBC Micro. It adds persistent high-score saving to disk/network storage while remaining compatible with standard filing systems including DFS and NFS (Econet).

This build is derived from the excellent Chuckie Egg reverse-engineering work here: https://github.com/mungre/chuckie

The original BBC Micro release loads at &0900, overwriting ROM workspace and making it unsafe to call filing system routines. This version reorganises the program into overlayed modules so the main code loads at &1B00, leaving the OS workspace area untouched. With the MOS fully functional, the game can safely write its high score table to a file.

Gameplay behaviour is otherwise unaltered. The timing, mechanics, and feel remain identical to the original release. The only visible difference is that high scores now persist between sessions. If you’re using slow storage, you may notice brief pauses when overlay modules load, but these occur outside gameplay. On faster systems, such as Econet backed by modern server hardware, they are effectively imperceptible.

This design also opens the door to future enhancements such as a shared / networked global high-score board with minimal further changes.

# Build instructions

Ensure you have beebasm and GNU Make installed.

Then simply run:

```shell
make
```

from the project's root directory. This will assemble the code and produce an SSD you can load.

