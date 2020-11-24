import click
import os
import fnmatch
import multiprocessing as mp
from multiprocessing import Pool

class Search:
    def __init__(self, mask, dir, key, ftype):
        self.__mask = mask
        self.__dir = dir
        self.__key = key
        self.__ftype = ftype

    # task function
    def searchPool(self, file):
        # open file and read lines
        with open (file) as lines:
            for line in lines:
                # if the key is in the line, print the line
                if self.__key in line:
                    # prints filename 
                    click.secho((f"FOUND: {file}"), fg='red')
                    # prints line containing key 
                    print(line.rstrip())
    
    # pool handler
    def pool(self, data):
        # gets cpu core count
        cores = mp.cpu_count()

        # creates pools based on cores
        p = Pool(cores)

        # calls function on all the items (files) in data
        p.map(self.searchPool, data)

    def searchForKey(self):
        dirFiles = []
        try:
            # if dir exists, iterate through files directory
            for file in os.listdir(self.__dir):
                # if file that matches pattern
                if fnmatch.fnmatch(file, '*' + self.__mask + '*.' + self.__ftype):
                    # if file is truely a file
                    if os.path.isfile(file):
                        # add filename to list
                        dirFiles.append(file)

            # sorts directory files by name
            dirFiles.sort()
            
            # passes directory files into pool handler
            self.pool(dirFiles)

        except Exception as e:
            # throws exception
            click.secho((f"SOMETHING WENT WRONG"), fg='red')