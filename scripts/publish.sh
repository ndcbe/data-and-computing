# Run this script from the root directory of this project

python ./scripts/process_notebooks.py
jb build ../data-and-computing/
ghp-import -n -p -f _build/html 
jb clean ../data-and-computing/
