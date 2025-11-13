# Solar Challenge Week 0
## Overview

This project is part of the KAIM 8 Learning Week 0 program. The project analyzes solar radiation and environmental data from Benin, Sierra Leone, and Togo. It focuses on environment setup, profiling, cleaning, and comparison to assess regional solar potential.

## Task 1: Git & Environment Setup
## Objective  
 
 Establish a consistent development environment and apply version control best practices.

## Usage 
 - Create and clone the repository from GitHub.
 - Set up a Python virtual environment and install the required packages. 
 - Add a .gitignore, requirements.txt, and a GitHub Actions workflow for basic CI. 
 - Use feature branches for setup tasks and commit changes with clear messages. 
 - Merge the setup branch into the main branch through a pull request after verifying CI passes.

## Task 2: Data Profiling, Cleaning & EDA
## Objective 

 Profile, clean, and explore solar datasets from Benin, Sierra Leone, and Togo to prepare them for analysis.

## Usage 
 - Create a separate branch and notebook for each country. 
 - Perform summary statistics, missing value checks, and outlier detection. 
 - Clean the datasets by imputing or removing invalid values. 
 - Generate correlation, scatter, and time-series visualizations to identify patterns. 
 - Save cleaned versions of each dataset locally. 
 - Commit and push the updated notebooks for review.

## Task 3: Cross-Country Comparison
## Objective 

 Compare the solar potential of Benin, Sierra Leone, and Togo based on the cleaned datasets.

## Usage 
 - Combine the cleaned datasets and create summary statistics for each country. 
 - Visualize differences in solar indicators such as GHI, DNI, and DHI. 
 - Rank countries based on average solar irradiance.

## Bonus Task:  Solar Data Dashboard
## Objective
An interactive Streamlit dashboard to explore solar radiation insights for Benin, Sierra Leone, and Togo.

## Usage
- Country selector for Benin, Sierra Leone, and Togo
- Interactive GHI, DNI, DHI, ModA & ModB boxplot
- Date range filter
- Top 5 regions 