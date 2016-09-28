#!/usr/bin/env python
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
	folder = false
	doc = false
	editor = false
	if args.folder:
		print "Folder Specified: " + args.folder
		folder = true;
	else:
		print "No Folder Specified"
	if args.document:
		print "Document Specified: " + args.document
		doc = true;
	else:
		print "No Document Specified"
	if args.editor:
		print "Editor Specified: " + args.editor
		editor = true;
	else:
		print "No Editor Specified"
	return folder, doc, editor

def locate_folder(folder):
	print folder
	proc = subprocess.Popen(["locate " + folder], stdout=subprocess.PIPE, shell=True)
	folder_path = (out, err) = proc.communicate()
	folder_path = str(folder_path)
	folder_path = folder_path.split()
	folder_path = folder_path[0]
	folder_path = folder_path.strip("('")
	folder_path = folder_path.split("\\n")
	folder_path = folder_path[0]
	folder_path = folder_path.split('/')
	print folder_path
	for x in range(0, 3):
		folder_path.remove(folder_path[0])
	folder_path = '/'.join(folder_path)
	print folder_path
	print '\n'
	path = folder_path
	print path
	print '\n'
	//GOTTA MAKE THAT CWD STAY IN CWD

def choose_path(bool folder, doc, editor):
	if folder == true:
		locate_folder(args.folder)
	if editor == true && doc == true:
		open_doc(args.document, args.editor)
	else if doc == true:
		open_doc(args.document, 'vim')

def main(args):
	choose_path(bool folder, doc, editor) = check_args(args)

main(args)
