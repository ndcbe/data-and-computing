# Project 2: Data Analysis

## Introduction

In teams of two, you will leverage several skills from CBE 60258 to analyze a dataset of your choosing.

Specific deliverables include:
1. A self-contained Jupyter notebook that documents your analysis and acts as a tutorial for others.
2. A 7-minute presentation that explains the problem, your approach, and your findings

The hope is for each person to give their presentation and demonstrate their notebook in their research group meetings during the following semester.

## Learning Objectives

By completing this assignment, you will:
1. Master computing and data analysis skills
2. Practice creating a Jupyter notebook in the style of supporting information often published with a journal article
3. Create publication plots
3. Plan, create, and deliver a brief talk (which is great practice for the 1st year PhD students!)

## Choosing a Good Problem and Data Set

One of the most challenging aspects of this project will be choosing a good problem and data set. Here are some suggestions:
* Each team member asks their research advisor for an already published data set. Read the corresponding paper and look at the data. Using the knowledge for this class, can you analyze the data in a different way? Perhaps your senior group mate performed (non)linear regression. Did they perform regression diagnostics? Did they estimate uncertainty in the regressed parameters? If you choose this route of reanalyzing a data set, you **need to clearly articulate** in your notebook and presentation how your approach **goes beyond the prior analysis**.
* Choose an experimental procedure in your lab and perform a detailed error analysis. Has anyone in your research group (or literature) performed a similar error analysis? If so, how does your analysis go beyond this prior work? Consider comparing multiple error analysis and propagation methods as one way to go beyond prior work.
* Analyze one of the data sets provided by Prof. Victoria Goodrich or other CBE faculty from our undergraduate labratories. You analysis must go beyond an example lab reports or calculations you are provided.
* Analyze a data set from literature or online. This is the most open ended option and has the most opportunities to go wrong. If you go this route, think very carefully about the end goal of your data analysis. What are the questions you want to answer with the data? The other options are easier in a sense because their structure provides a more clear end goal. You **must go beyond an prior analysis** you find in literature or online. Simply redoing analysis you find in a textbook, online forum, or paper is not acceptable.

## Project Proposal

Each team should submit a 1-page project proposal that answers the following questions:
1. What is the end goal of the analysis?
2. Do you have the neccessary data? Please identify the sources will full bibliographic information.
3. How will your project go beyond prior analysis? Tip: write bullet points to clearly articulate all of the differentiating factors
4. What are the anticipated take-away messages from your analysis? (What are your hunches?)
5. How will you organize your notebook in sections (level 2, `##`) and optionally subsections (level 3, `###`)?

## Project Notebook

The project notebook should be self-contained and fully document your analysis. It should be structured similar to supporting information for a paper and serve as a tuturial for a future graduate student. All steps should be explained, add plots should be briefly interpreted, and general conclusions should be summarized. In other words, you are creating the tutorial you wish you had when joining a research group ;)

### Required Content

Each notebook must include the following sections:
1. Introduction or Problem Statement
2. Background (e.g., explaination of the experimental aparatus or models, prior analysis, brief overview of key literature)
2. Analysis (may be split into multiple sections)
4. Conclusions or Take Away Message
5. References

Each notebook must follow the following standards:
1. All references and data sources are acknowledged
2. Link to the appropriate pages (and sections) in the CBE 60258 website
3. All equations are typeset
4. Schematic figures or photographs of the experiment equipment are included as appropriate
5. All figures our publication quality
6. All results and figures are briefly interpretted and discussed
7. In either the introduction or background, you must explain how your project goes beyond prior analysis
8. Be professional formatted and visually appealing.

### Example

Below are a few examples. After each example, we walk though good elements to emulate and missing elements that are needed for this specific project.

Here is [supporting information](https://github.com/dowlinglab/CO2-to-carbs-analysis/blob/main/Watson_supporting_calculations.ipynb) from [Watson et al](https://pubs.acs.org/doi/full/10.1021/acsenergylett.2c01550):
* Good: publication quality plots, commented code, organized into sections and subsections, easy to match code with the paper figures
* Missing: the background, references, discussion, and conclusions are all in the paper. For this project, all of these contents should be self contained in the notebook. (In this way, our project deviates slights from the format of Supporting Information as it requires additional elements.)

Here is [supporting information](https://github.com/dowlinglab/multiscale-adsorption-targets) from [Eugene et al](https://pubs.acs.org/doi/10.1021/acsestengg.0c00046):
* Good: publication quality plots, easy to follow code, notebooks are divided into sections and subsections, repository is well organized with a helpful readme making it easy to match the code with the paper figures
* Missing: Similar to the previous example, elements required for our project like the background, references, discussion, and conclusions are in the companion journal article.

Here is an analysis of the [heat exchanger experiment from our undergraduate laboratory](https://jckantor.github.io/cbe31358-book/notebooks/01/00_hx.html):
* Good: detailed background, easy to follow code, excellent presentation
* Missing: discussion and conclusions, not quite publication quality plots, longer than expected for our project

## Presentation

Each team will give a 7-minute presentation and answer questions for 3 to 4 minutes during our final exam timeslot. Each team member must participate in the presentation. For example, one person can give the talk and the other person can answer questions. Or the team can split the time spent presenting and answering questions approximately equaly. If multiple people are giving the presentation, there should only be one transition between speakers.

Each presentation should include the following:
1. Description of the problem
2. Overview of the data and experimental apartus (as appropriate)
3. Summary of the analysis approach
4. Highlights of one or two key results
5. Conclusions including how this analysis goes beyond prior work

References should be included on the appropriate slides. If you take a figure, data, or model from literature (or the internet), you need to acknolwedge it on your slides in a clear way!
