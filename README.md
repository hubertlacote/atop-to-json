# atop-to-json

**Convert atop text logfiles to JSON.**

Compatible with **Atop 2.5.0**, please use `atopconvert` to convert older raw log files or feel free to send a pull request to add support to a newer version of Atop.

## Introduction to Atop

Atop is a performance monitor for Linux that is capable of reporting the activity of all processes, system and process activity", see atop's [official website](https://www.atoptool.nl/) or [GitHub repository](https://github.com/Atoptool/atop).

When executed without arguments, the output of Atop is similar to `htop`.
Atop can also capture log files in compressed binary format or in text format, useful for long-term analysis on system level and process level.

## Why atop-to-json

Atop's log files can be analysed with the `atopsar` command, e.g. to generate all possible reports from a raw capture:

```bash
atopsar -A -r capture.raw
```

While useful, it doesn't allow to visualise quickly all the information collected by Atop.

JSON format is easily processable by tools like [jq](https://stedolan.github.io/jq/) (command-line JSON processor) and can be used to generate graphs using [Dash](https://plotly.com/dash/) in Python or [D3.js](https://d3js.org/) in JavaScript.

## Installation

No installation required.

## Usage

This repository contains a set of basic tools generating JSON. They can be combined using [jq](https://stedolan.github.io/jq/) to deal with more complex use cases, see example shell scripts in [tools/](tools/).

```bash
./atop-to-json -i capture.txt
```

## Contributing

Please run tests before contributing new code:

```bash
pip install -r requirements-tests.txt
./run-tests
```

## License

MIT (see [LICENSE](LICENSE))
