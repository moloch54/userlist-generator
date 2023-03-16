#!/usr/bin/python3

import os
import argparse

def parse_arg():

	parser = argparse.ArgumentParser(description="usergen --ul users.txt -o userlist.txt")
	parser.add_argument("--ul", help="path to the userlist, a space between the firstname and the lastname. Ex: John Hammond")
	parser.add_argument("-o", help="output file")
	args = parser.parse_args()	
	#print(args) 
	return args.ul, args.o

ul, o = parse_arg()

separators=[".","","-","_"]
users=[]
userlist=[]
final_list=[]

with open(ul,"r") as fichier:
	users=fichier.readlines()
for user in users:
	user_split= user.split(" ")
	user_split[1]=user_split[1].replace("\n","")
	userlist.append(user_split)

for user in userlist:
	for separator in separators:
		for i in range(1,len(user[0])+1):
			for j in range (1,len(user[1])+1):
		
				final_list.append(user[0][:i]+separator+user[1][:j])		
		

final_list=list(set(final_list))
final_list.sort()
with open(o,"w") as fichier:
	fichier.writelines(line+"\n" for line in final_list)
