# Run this script from the root directory of this project

python ./scripts/process_notebooks.py
jb build ../data-and-computing/
#git add ./_build/html/_images/
#git commit -m "Adding images from build"
ghp-import -n -p -f _build/html 
jb clean ../data-and-computing/