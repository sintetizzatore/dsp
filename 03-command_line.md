# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

>> less/more (view a file)

>> ls *.txt (wildcard matching)

>> grep, select-string (typing text into a file quickly)

>> apropros, help (help)

>> pushd, popd (switch between directories)

>> ls (list directory)

>> mv (move file)

>> rm (remove file)

>> cat (stream file)

>> find, dir -r (find file)


---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

>> 'ls' lists out the contents of whichever directory you've pointed to using the 'cd' command.

>> 'ls -a' lists out hidden files

>> 'ls -l' lists out directory contents in long format

>> 'ls -lh' lists the file size/s in easy to read (human readable format)

---


---

What does `xargs` do? Give an example of how to use it.

>> 'xargs' is a command you can use alongside other commands to ease or simplify the output. 

>> Example: find tif files in a directory and get a list, -print0 required if any filenames have whitespace

>>  find ./images -name "*.tif" -print0 | xargs -0 ls

---

