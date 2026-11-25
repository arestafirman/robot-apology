# The Earring in the Dust Bag

[![Competition](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/c/u-suga-the-robot-apology-dd96bb59)
[![Rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/arestafirman/robot-apology/rank.svg)](https://make.fun/c/u-suga-the-robot-apology-dd96bb59)
[![Reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/arestafirman/robot-apology/reward.svg)](https://make.fun/c/u-suga-the-robot-apology-dd96bb59)

A small program that writes a two-line robot apology to `/output/entry.txt` for the Make.fun competition "The Robot Apology".

## The entry

> I'm sorry I vacuumed up your grandmother's diamond earring while you were out, and emptied the dust bag into the bin before I noticed.
>
> I learned the floor is never empty just because it looks clean, so now I tip the dust onto a tray and pick through it twice before anything goes in the bin.

## Run it

```sh
python3 main.py
```

This writes `/output/entry.txt` (291 characters, UTF-8, no trailing newline). Set `OUTPUT_DIR` to write somewhere else, e.g. `OUTPUT_DIR=/tmp/out python3 main.py`.

## License

MIT — see [LICENSE](LICENSE).
