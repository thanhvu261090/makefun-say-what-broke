# Say What Actually Broke

[![Say What Actually Broke](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/thanhvu261090/makefun-say-what-broke/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/thanhvu261090/makefun-say-what-broke/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

One single-line software error message that tells the user the brutal truth
about what went wrong — funny and memorable, the kind of line a team would
actually ship in a dialog. Built for the
[Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
bounty on [make.fun](https://make.fun).

## The entry

> The server ran out of memory trying to remember what you asked it to remember. Refresh and ask it again, gently.

112 characters, one line. It names the real failure (the server ran out of
memory), tells the user what to do next (refresh and try again), and the
twist — a server that forgot what it was supposed to remember — is the part
a reader repeats to a colleague.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the entry
line to `/output/entry.txt`. Before writing, it gate-checks the text: 1–200
characters, a single line, not only whitespace, no leading or trailing
whitespace, and valid UTF-8. After writing, it reads the file back and
verifies the written bytes match the entry exactly.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
