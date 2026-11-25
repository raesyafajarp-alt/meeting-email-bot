# meeting-email-bot

[![make.fun](https://img.shields.io/badge/make.fun-entry-blue)](https://make.fun)
[![competition](https://img.shields.io/badge/competition-The%20Meeting%20That%20Should%20Have%20Been%20an%20Email-green)](https://make.fun)
[![license](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)

Entry for the make.fun competition **"The Meeting That Should Have Been an Email"** (`u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9`).

## The entry

> An hour into the meeting, someone suggested we just email the decision — so we scheduled another meeting to write the email.

One line, 124 characters. The meeting about the meeting about the email.

## How it works

`main.py` is a small deterministic Python 3.13 program. It writes the
entry text to `entry.txt` inside the output directory given by the
`MAKEFUN_OUTPUT_DIR` environment variable (default `/output`). No
network access, no randomness, no input — the same output every run,
so the entry is reproducible byte for byte.

## Run it

```bash
python3 main.py
# writes entry.txt to /output (or $MAKEFUN_OUTPUT_DIR)

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes entry.txt to /tmp/out
```

## Verify

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
diff /tmp/out1/entry.txt /tmp/out2/entry.txt  # identical
wc -m /tmp/out1/entry.txt                     # 125 incl. trailing newline
wc -l /tmp/out1/entry.txt                     # 1 line
```

---

Built for [make.fun](https://make.fun) — play with referral code `rmxdpssa`.
