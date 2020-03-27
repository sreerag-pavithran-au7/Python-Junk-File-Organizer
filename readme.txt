Junk File Organizer : 
It is a python program that runs as a command-line tool. Basically, as a lazy programmer, my desktop or any directory is full of files.
Due to a large number of files, it is a daunting task to sit and organize each and every file. It is a Python script that comes in handy 
and returns a folder “Organiser” where all the files are organized in a well-manner within seconds. It organizes by size(size), last modified 
date(date), extensions(exte) or alphabetically(alph).


It creates a parent folder Organiser inside the current directory

First take user input,
If the user input is ext
      
The program checks for each file extension of each file .Then according to the category in which it falls creates the folder  
inside parent folder ex: if pdf file it creates PDF directory,copies file there and delete old file. In the same manner it checks for every 
file inside that directory.

If the user input is size
The programs calculates the size of each file.Then according to the category in which it falls creates the folder inside parent folder 
ex: if file size 3kb, it creates a folder LARGE if not created and copies contents there and deletes old file.
File size 1-10 falls under SMALL,  
File size 10-100 falls under MEDIUM ,  
File size 100-1000 falls under LARGE
 File size 1001-16000 falls under HUGE
 File size 16000 above falls under GIGANTIC

if date, programs gets the date of each file and present date.Then according to the category in which it falls creates the folder 
like today,yesterday, this month,last_month gets copied there.
if the user input is size alpha, gets the starting alphabet of each file.Then according to the category in which it falls creates 
the folder like A ,B,C .. gets copied there and deletes the old file.

Steps to follow:
Requirements:
1.Python 3.6
Steps:
In the terminal, navigate to the folder where you need to arrange files
1.git clone “”
2.python organize.py size (instead of size can be alpha,ext or date)
It will produce the “organizer” folder.