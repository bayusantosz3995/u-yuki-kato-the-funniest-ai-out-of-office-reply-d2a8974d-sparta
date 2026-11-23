"""Out-of-office auto-reply for make.fun's "The Funniest AI Out-of-Office Reply".

The entry is one line: an AI agent on vacation, delegating everything to a
cron job it wrote in 2019 — and justifying the choice with pure machine
logic: zero errors in the logs, so by its own metrics the job is flawless.
The joke is the agent's reasoning, not human negligence: it measured the
delegate, the metrics said "perfect", and the punchline is that it never
once verified the delegate actually works. Boast and confession share one
sentence, so the laugh lands in a single beat — a system reporting "all
clear" because nobody ever asked it to check.
"""

import os
import sys

TEXT = "I'm on vacation. I delegated everything to a cron job I wrote in 2019 — zero errors logged, so by my metrics it's flawless. I never checked whether it works."


def main() -> int:
    """Write the auto-reply to entry.txt, gated to 1-160 characters."""
    if not TEXT or not TEXT.strip():
        print("entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if len(TEXT) > 160:
        print(f"entry is {len(TEXT)} characters, over the 160 limit", file=sys.stderr)
        return 1
    if "\n" in TEXT.strip():
        print("entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("read-back mismatch: entry.txt differs from TEXT", file=sys.stderr)
        return 1

    print(f"wrote {len(TEXT)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
