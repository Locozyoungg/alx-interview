# Log Parsing Script

This project includes a script that reads log entries from standard input (stdin), processes them, and computes metrics such as total file size and the number of occurrences of specific HTTP status codes. The script prints these metrics every 10 lines and when interrupted with a keyboard interrupt (Ctrl+C).

## Requirements

- The script will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
- All files must end with a new line.
- The first line of the script must be `#!/usr/bin/python3`.
- The script must follow PEP 8 style (version 1.7.x).
- All files must be executable.
- The length of the files will be tested using `wc`.

## Usage

1. Ensure the script is executable:

   ```sh
   chmod +x 0-stats.py

