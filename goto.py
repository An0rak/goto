#!/usr/bin/env python
import os
import argparse
import subprocess
import string


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--folder", help="Choose folder to open", type=str)
parser.add_argument("-d", "--document", help="Choose a document to open, default editor is vim", type=str)
parser.add_argument("-e", "--editor", help="Choose an editor, vim, gedit", type=str)

args = parser.parse_args()

def check_args(args):
	if args.folder:
		print "Folder Specified: " + args.folder
	else:
		print "No Folder Specified"
	if args.document:
		print "Document Specified: " + args.document
	else:
		print "No Document Specified"
	if args.editor:
		print "Editor Specified: " + args.editor
	else:
		print "No Editor Specified"

def locate_folder(folder):
	print folder
	proc = subprocess.Popen(["locate " + folder], stdout=subprocess.PIPE, shell=True)
	folder_path = (out, err) = proc.communicate()
	print folder_path
	folder_path = str(folder_path)
	folder_path = folder_path.split()
	folder_path = folder_path[0]
	folder_path = string.split(folder_path[0], '\n')
	print '\n'
	print folder_path[0]
	

def main(args):
	check_args(args)
	locate_folder(args.folder)
main(args)
