#!/usr/bin/env python3
import os
import sys

if os.environ.get('LC_CTYPE', '') == 'UTF-8':
    os.environ['LC_CTYPE'] = 'en_US.UTF-8'
import jockcli.jockcli


def main():
    return jockcli.jockcli.jock_cli()


if __name__ == '__main__':
    sys.exit(main())
