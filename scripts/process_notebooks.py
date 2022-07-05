import nbformat
from nbformat.v4.nbbase import new_code_cell, new_markdown_cell, new_notebook
import re
import os

def process_notebook(folder,filename,verbose=1):

    ''' Remove nbgrader content from notebooks and save updated version
    
    '''

    ## Setup

    # read notebook file
    input_notebook = folder + "/" + filename
    with open(input_notebook, "r") as fp:
        if verbose >= 1:
            print("\nOpening ",input_notebook)
        nb = nbformat.read(fp, as_version=4)

    # display file metadata
    if verbose >= 2:
        print(f"nbformat = {nb.nbformat}.{nb.nbformat_minor}")
        display(nb.metadata)
        
    ## Remove code elements with specific tag
    def replace_code(pattern, replacement):
        ''' Replace content in code by applying regular expression
        
        '''
        
        if verbose >= 1:
            print("Removing following expression: ", pattern)
        
        count = 0
    
        regex = re.compile(pattern, re.DOTALL)
        for cell in nb.cells:
            if cell.cell_type == "code" and regex.findall(cell.source):
                cell.source = regex.sub(replacement, cell.source)
                count += 1
                if verbose >= 2:
                    print(f" - {pattern} removed")
                
        if verbose >= 1:
            print("  ",count," cells processed")

    SOLUTION_CODE = "### BEGIN SOLUTION(.*?)### END SOLUTION"
    HIDDEN_TESTS = "### BEGIN HIDDEN TESTS(.*?)### END HIDDEN TESTS"
    replace_code(SOLUTION_CODE, "# Add your solution here")
    replace_code(HIDDEN_TESTS, "# Removed autograder test. You may delete this cell.")

    ## Save new notebook
    output_notebook = folder + "-publish/" + filename
    
    with open(output_notebook, "w") as fp:
        if verbose >= 1:
            print("Saving ",output_notebook)
        nbformat.write(nb, fp)
    

def replace_code(pattern, replacement, verbose):
    ''' Replace content in code by applying regular expression
    
    '''
    
    if verbose >= 1:
        print("Removing following expression: ", pattern)
    
    count = 0
    
    regex = re.compile(pattern, re.DOTALL)
    for cell in nb.cells:
        if cell.cell_type == "code" and regex.findall(cell.source):
            cell.source = regex.sub(replacement, cell.source)
            count += 1
            if verbose >= 2:
                print(f" - {pattern} removed")
                
    if verbose >= 1:
        print("\t",count," cells processed")

# Testing
#process_notebook("./notebooks/01","03-Flow-control.ipynb")

#folders = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14"]


folders = ["01","02","03","04","05","06","07","08","09","10","11","12","13"]

for fld in folders:
    
    # Loop over filenames
    full_folder_name = "./notebooks/"+fld
    
    print("Processing files in ",full_folder_name)
    
    for file in os.listdir(full_folder_name):
        
        # Check if file is a notebook using ending
        if re.match("(.*?)\.ipynb$",file):
            
            # process the notebook!
            process_notebook(full_folder_name,file,verbose=1)