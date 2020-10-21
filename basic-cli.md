# CLI

- Command Line is a faster and more powerful way to maneuver your o.s than by using GUI such as Windows Explore/Mac finder
- \$ sed 's/dude/tejas/g' report.txt > report_new.txt

---

# OS File Structure

- OS organize theire folder in a hierarchical structure (a tree) with parent and children, all relative to base root directory (root ==> /)
- Everything is inside this Root Directory (Mac/Linux)
- Files and directories have absolute paths based on the root, where each additional level down adds a ' /'
  ex: absolute path for vsc : home/tejas/tejas/workspace/vsc/
- The special directory called home which is also known as '~' (This is a default directory upon opening a terminal)
- Generally home directory is inside the Users/home (Users in mac/home in linux) directory which is again inside the root directory eventually
- pwd (Gives the print working directory) ==> provides Absolute Path
- NOTE: / ==> Root directory, ~ ==> Home directory

---

# Navigating Absolute Path

- cd (Change directory) ==> cd followed by the absolute path of the folder will navigate you there
- \$ cd tejas/workspace/vsc
- \$ cd / (root directory)
- \$ cd (or) cd ~ (home directory)

# Navigating Relative Path

- dot (.) stands for current directory and dot-dot (..) stands for parent folder <== This allow for relative navigation
- \$ cd .. (Take back one level)

---

# ls

- list the contents of a directory.
- you can use option such as '-a' to list all files (including hidden onces) or '-l' for longer format
- \$ ls -a
- \$ ls workspace

---

# mkdir

- mkdir followed by the name of the new directory will create a new child directory inside the current directory
- \$ mkdir test/test-child (You cannot create child folder inside another folder)

---

# create file

- touch followed by file name and file-type extension will create a new file of that type
- \$ touch test.py
- \$ touch cat.jpg
- When you touch the previous created file then this command will gently touch the file (update the last modified time of that file)

---

# Moving / Renaming Things

- mv (move) which takes two arguments src and destination (It can be used for move or rename the file)
- \$ mv favs.txt goat.txt (Rename favs file-name to goat since in the same directory)
- \$ mv goat.txt ../ (moving the file to parent directory)

---

# Removing file

- rm (remove file) followed by name of the file
- \$ rm goat.txt

---

# Removing Directories

- rmdir <directory_name> <== Only to remove empty directory
- rm -rf <directory> (options -r --> recursive and -f --> force to prevent warnings) [NOTE: we cannot get-back the fils/folders/sub-folders i.e- undo the delete]
- man rm
- Files are removed with the [ rm ] command while the directories need to have [ rm -r ] flag so it recursively deletes file contents.

---
