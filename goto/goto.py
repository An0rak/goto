# -*- coding: utf-8 -*-

"""goto-commandline-tool.goto: provides entry point main()."""

__version__ = "0.1.0"

import os
import argparse
import subprocess
from subprocess import Popen
import string

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--folder", help="Choose folder to open", type=str)
parser.add_argument("-d", "--document", help="Choose a document to open, default editor is vim", type=str)
parser.add_argument("-e", "--editor", help="Choose an editor, vim, gedit", type=str)

args = parser.parse_args()

def check_args(args):
	folder = False
	doc = False
	editor = False
	if args.folder:
		print "Folder Specified: " + args.folder
		folder = True
	else:
		print "No Folder Specified"
	if args.document:
		print "Document Specified: " + args.document
		doc = True
	else:
		print "No Document Specified"
	if args.editor:
		print "Editor Specified: " + args.editor
		editor = True
	else:
		print "No Editor Specified"
	return folder, doc, editor

def get_and_format_path(dir):
	proc = subprocess.Popen(["locate " + dir], stdout=subprocess.PIPE, shell=True)
	dir_path = (out, err) = proc.communicate()
	dir_path = str(dir_path)
	dir_path = dir_path.split()
	dir_path = dir_path[0]
	dir_path = dir_path.strip("('")
	dir_path = dir_path.split("\\n")
	dir_path = dir_path[0]
	dir_path = dir_path.split('/')
	print dir_path
	for x in range(0, 3):
		dir_path.remove(dir_path[0])
	dir_path = '/'.join(dir_path)
	print dir_path
	print '\n'
	path = dir_path
	print path
	print '\n'
	return path

def locate_folder(folder):
	print folder
	path = get_and_format_path(folder)
	#GOTTA MAKE THAT CWD STAY IN CWD

def open_doc(doc, editor):
	path = get_and_format_path(doc)
	os.system(editor + ' ' + path)

def choose_path(folder, doc, editor):
	if folder == True:
		locate_folder(args.folder)
	if editor == True & doc == True:
		open_doc(args.document, args.editor)
	else:
		if doc == True:
			open_doc(args.document, 'vim')

def main(args):
	folder, doc, editor = check_args(args)
	choose_path(folder, doc, editor)

main(args)
