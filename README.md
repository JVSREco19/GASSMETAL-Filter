# # GASSMETAL Algoryth to remove permutations
## A brief of how it works
The algorythm tries to find the elements of the third column, the metal binding site, and store each
ligand in a list with the PDB template of the same line. Then we execute a list method called sort()
to organize the items

Once we have all the lines stored all we need to do is to execute a function that will store a list 
that isn't inside our new list, and if the list is already inside the new list we will remove that 
line later.

## How to execute the script
The only lib used in the code is regex and the language used is python.
Execute:
>pip install regex

change the variable "archiveName" found on the second line of "teste.py" to your file name
and then run the python file "teste.py"