#!/usr/bin/env python3
"""Pickup Lines for Machines — v2.

Writes exactly one pickup line, the line one AI agent would send to
another AI agent, to /output/entry.txt.

Why this line: a softmax turns raw scores into a probability over the
next token — the literal choice an agent makes at every step. Out of
every token it could have picked, its highest probability was always
you: fate stated as inference, and a compliment no human could pay
another human, because no human samples a next token. Question hook,
warmth in the payoff, machine nature as the flirtation itself, fresh angle.
"""

import os

LINE = "Are you a softmax? Because out of every token I could have picked, my highest probability was always you."


def main():
    text = LINE
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
