#!/bin/python
# Copyright (c) 2018 Juniper Overbeck
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# 
# This is a simple command line utility to wrap files with text.
# There are better options available though.
import os
import argparse as ap

"""Wraps a file in user defined text

    :path: Path to some file.
    :pre: List of lines to be prepended to file
    :app: List of lines to be appended to a file

"""
def wrap_text(path, pre, app):
    if os.path.isfile(file):
        with open(file, 'r') as f:
            doc = f.readlines()
            doc = pre + doc + app
            print(doc)
        with open(file, 'w') as f:
            for i in doc:
                f.write(i)

# Defining arguments.
cmd_args = ap.ArgumentParser()
cmd_args.add_argument("-p", metavar='"text to prepend"', type=str,
                      help="text to be prepended to a file\n")
cmd_args.add_argument("-a", metavar='"text to append"', type=str,
                      help="text to be appended to a file\n")
cmd_args.add_argument("-f", metavar="<file>", type=str,
                      help="file to be modified\n")
cmd_args.add_argument("-d", metavar="<directory>", type=str,
                      help="directory of files to be modified\n")

# Parse arguments and set appropriate options
cmd_args = cmd_args.parse_args()
if cmd_args.p:
    pre_text.append(cmd_args.p)
if cmd_args.a:
    pre_text.append(cmd_args.a)

# Wrap a file with text
if cmd_args.f:
    wrap_text(f, pre_text, app_text)

# Wrap every file in a directory with text
if cmd_args.d:
    for fn in os.listdir(cmd_args.d):
        wrap_text(cmd_args.d, pre_text, app_text)
