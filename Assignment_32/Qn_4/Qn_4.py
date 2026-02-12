'''Design automation script which accept directory name and delete all duplicate files from that
directory. Write names of duplicate files from that directory into log file named as Log.txt.
Log.txt file should be created into current directory. Display execution time required for the
script.

Usage : DirectoryDusplicateRemoval.py "Demo"

Demo is name of directory.'''

import os
import sys
import hashlib
import time


def CalculateChecksum(path):
    fobj = open(path, "rb")
    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while len(Buffer) > 0:
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()


def DuplicateRemoval(DirectoryName):
    Border = "-" * 50
    timestamp = time.ctime()

    # Create log file
    logfilename = "ChecksumLog_%s.log" % (timestamp)
    logfilename = logfilename.replace(" ", "_")
    logfilename = logfilename.replace(":", "_")

    fobj = open(logfilename, "w")
    fobj.write(Border + "\n")
    fobj.write("This is a log file created by Mitali\n")
    fobj.write("Duplicate Files Removal Script\n")
    fobj.write(Border + "\n")

    if not os.path.exists(DirectoryName):
        print("There is no such directory")
        fobj.close()
        return

    if not os.path.isdir(DirectoryName):
        print("Unable to scan as it is not a directory")
        fobj.close()
        return

    files_dict = {}

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        for fname in FileName:
            fullpath = os.path.join(FolderName, fname)
            try:
                checksum = CalculateChecksum(fullpath)

                if checksum in files_dict:
                    files_dict[checksum].append(fullpath)
                else:
                    files_dict[checksum] = [fullpath]

            except Exception as e:
                fobj.write(f"Unable to process {fullpath} : {e}\n")

    DeletedCount = 0

    for checksum, filelist in files_dict.items():
        if len(filelist) > 1:
            original = filelist[0]
            fobj.write(f"\nKeeping original: {original}\n")

            for duplicate in filelist[1:]:
                try:
                    os.remove(duplicate)
                    DeletedCount += 1
                    fobj.write(f"Deleted duplicate: {duplicate}\n")
                except Exception:
                    fobj.write(f"Unable to delete: {duplicate}\n")

    if DeletedCount == 0:
        fobj.write("No duplicate files found\n")

    fobj.write(Border + "\n")
    fobj.write(f"Total files deleted: {DeletedCount}\n")
    fobj.write(Border + "\n")

    fobj.close()


def main():
    Border = "-" * 50
    print(Border)
    print("----- Duplicate Files Removal ----")
    print(Border)

    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        return

    start_time = time.time()

    DuplicateRemoval(sys.argv[1])

    end_time = time.time()

    print("Execution Time:", end_time - start_time, "seconds")

    print(Border)
    print("-------------- Thank you --------------")
    print(Border)


if __name__ == "__main__":
    main()
