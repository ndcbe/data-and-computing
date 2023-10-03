# Semester Project

## Introduction

You will create and revise teaching material (e.g., class examples, assignments) that use numerical methods and data analysis skills from CBE 60258. These material will be targetted at undergraduate or graduate science and engineering students.

Deliverables:
1. Either (1) individually revise a published numerical methods contributed notebook or (2) with a partner, create a new notebook.
2. With your partner, prepare a new notebook that teaches one or more data analysis topics from CBE 60258 using a science or engineering example.
3. With your partner, give a 7-minute presentation that summarizes your contributions to the class website.

## Learning Objectives

By completing this assignment, you will:
1. Master computing and data analysis skills
2. Practice creating a Jupyter notebook in the style of supporting information often published with a journal article
3. Create publication-quality plots
3. Plan, create, and deliver a brief talk (which is great practice for the 1st year PhD students!)

## Part 1: Revise a Numerical Methods Jupyter Notebook

Please take a few minutes to browse [previously contributed notebooks](../notebooks/contrib/contribute.md). Most students individually revise one of these notebooks.

Many of these notebooks need some minor editing:
* Ensure consistent section numbers
* Fix equations not rendered correctly
* Fix links to other notebooks
* Move all solutions, including discussion solutions, to between `### BEGIN SOLUTION` and `### END SOLUTION` in code block.
* Spelling and grammar checks
* Ensure all images render correctly

Each person will contribute their editted notebook via GitHub following [these instructions](../notebooks/contrib/contribute.md). **Important:** Do NOT edit the notebook using the "Launch Colab" link on the class website. Instead, you need to download the correct file [here](https://github.com/ndcbe/data-and-computing/tree/main/notebooks/contrib-dev). You can then upload this version to Google Colab for editting. If you do not follow these instructions, you will end the wrong version of the file and need to redo your work.

Each person also needs to make at least one substantial intellectual contribution to their assignment notebook. Ideas:
* Add a new sensitivity analysis and discussion question
* Draw a strong connection to linear algebra
* Perform regression in Python instead of Excel in [](../notebooks/contrib/McCabe-Thiele.ipynb)

Alternately, a team of 2 students may decide to contribute a new notebook to the class website. This may be either a new example (hint: look to a textbook for inspiration) or an explanation of an advanced topics. Here are some advanced topics to consider:
* QR factorization
* Line search or trust regions for globalization of Newton's method
* Finite volume or finite element discretization methods
* Shooting methods for boundary value problems

For each topic, Prof. Dowling can provide a recommended textbook chapter to use a basis for the contributed notebook.

### Project Proposal

Please indicate your preferences [here](https://forms.gle/MyLb75GS2RzFd1nm7).

### Submission

Each person (or team) will submit their revisions via GitHub. See [](../notebooks/contrib/contribute.md) for instructions. We are doing this so everyone practices using GitHub.

You will also submit via Gradescope up to 1-page (PDF) highlighting the key revisions you made. In this document, you need to clearly articulate your intellectual contributions.

### Anticipated Time Requirements

**Notebook Editting**
Project Proposal: 1 hour
Complete Activities in Notebook, Verify Answers: 2 hours
Formatting and Edits: 2 hours
Intellectual Contribution: 3 hours
Learning GitHub: 1 hour
Miscellanous: 1 hour

**Create New Notebook** (per person)
Project Proposal: 1 hour
Agree on Project Idea, Coordinate Effort: 1 hour
Review Reference Material: 2 hours
Prepare Notebook (keep it simple): 2 hours
Formatting and Edits: 2 hours
Learning GitHub: 1 hour
Miscellanous: 1 hour

## Part 2: Create a Data Analysis Jupyter Notebook

In teams of 2 or 3 people, you will contribute a Jupyter notebook to the class website demonstrating one or more data analysis skills from CBE 60258.

### Choosing a Good Problem and Data Set

One of the most challenging aspects of this project will be choosing a good problem and data set. Here are some suggestions:
* Each team member asks their research advisor for an **already published data set**. Read the corresponding paper and look at the data. Using the knowledge for this class, can you analyze the data in a different way? Perhaps your senior group mate performed (non)linear regression. Did they perform regression diagnostics? Did they estimate uncertainty in the regressed parameters? If you choose this route of reanalyzing a data set, you **need to clearly articulate** how your approach **goes beyond the prior analysis**.
* Choose an experimental procedure in your lab and perform a detailed error analysis. Has anyone in your research group (or literature) performed a similar error analysis? If so, how does your analysis go beyond this prior work? Consider comparing multiple error analysis and propagation methods as one way to go beyond prior work.
* Analyze one of the data sets provided by Prof. Victoria Goodrich or other CBE faculty from our undergraduate labratories. Your analysis must go beyond example lab reports or calculations provided.
* Analyze a data set from literature or online. This is the most open-ended option and has the most opportunities to go wrong. If you go this route, think very carefully about the end goal of your data analysis. What are the questions you want to answer with the data? The other options are easier in a sense because their structure provides a clearer end goal. You **must go beyond prior analysis** you find in the literature or online. Simply redoing analysis you find in a textbook, online forum, or paper is not acceptable.

**Important** This project is intentioanlly open-ended to help practice the discipline of maintaining a focused project scope. The end goal is a short homework assignment or ~20 minute class activitiy. As you brainstorm and refine ideas in your team, keep asking *how can we simplify and still meet our learning objectives*. Often *less is more*.

### Project Update

Each team should submit a 1-page project update that:
1. Identifies the learning objectives
2. Explains the problem statement
3. Identifies data sources
4. Articulates how your project will go beyond prior analysis. Tip: write bullet points to clearly articulate all of the differentiating factors.
5. Lists anticipated take-away messages from your analysis
6. Lists references (full bibliographic information)

You will also submit a draft of the 

### Project Notebook

The project notebook should be self-contained and fully document your analysis. It should be structured similar to the examples from prior years you revised in Part 1.

### Required Content

Each notebook must include the following sections:
1. Introduction or Problem Statement
2. Background (e.g., explaination of the experimental aparatus or models, prior analysis, brief overview of key literature)
3. Analysis (may be split into multiple sections)
4. Conclusions or Take Away Message
5. References

### Submission

Each person (or team) will submit their revisions via GitHub. See [](../notebooks/contrib/contribute.md) for instructions.

You will also submit via Gradescope up to 1-page (PDF) explaining how this example goes beyond exisiting material. For example, if you reproduced an example from a textbook, what new content did you add (e.g., implemented bootstrap uncertainty estimates, added sensitivity analysis, added discussion questions)

### Anticipated Time Requirements

(per person)
Brainstorm Ideas: 1 hour
Agree on Project Scope: 2 hour
Identify Data Sources and Examples: 2 hour
Prepare Notebook Draft 1: 2 hours
Project Status Update: 1 hour
Prepare Notebook Draft 2: 2 hours
Team Coordination: 2 hours
Formatting and Editting: 2 hours
Submission: 1 hour

## Part 3: Deliver a Final Presentation

Each team will give a 7-minute presentation (focused on Part 2) and answer questions for 3 to 4 minutes during our final exam timeslot. Each team member must participate in the presentation. For example, one person can give the talk and the other person can answer questions. Or the team can split the time spent presenting and answering questions approximately equally. If multiple people are giving the presentation, there should only be one transition between speakers.

Each presentation should include the following:
1. Description of the problem
2. Overview of the data and/ experimental apartus (as appropriate)
3. Summary of the analysis approach
4. Highlights of one or two key results
5. Conclusions including how this analysis goes beyond prior work

References should be included on the appropriate slides. If you take a figure, data, or model from literature (or the internet), you need to acknolwedge it on your slides in a clear way!

## Jupyter Notebook Formatting Guidelines

Each notebook must follow the following standards:
1. All references and data sources are acknowledged
2. Link to the appropriate pages (and sections) in the CBE 60258 website
3. All equations are typeset
4. Schematic figures or photographs of the experiment equipment are included as appropriate
5. All figures are publication-quality
6. All results and figures are briefly interpretted and discussed
7. Be professionally formatted and visually appealing

