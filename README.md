# Stack Overflow Data Pipeline using Airflow

This repository contains a data engineering project demonstrating how to build a data pipeline using Apache Airflow to extract data from Stack Overflow. The focus is on extracting and moving the data of the tag 'cloud', as I was personally curious to analyse the frequency and other data related to different cloud provides (AWS, Azure, Google). 

## Project Overview

The pipeline involves:

Extract: Fetch questions from Stack Overflow using the StackAPI.
Transform: Process the data for analysis.
Load: Store the processed data in a database.

## Prerequisites

* Python 3.6+
* Apache Airflow
* Stack Overflow Developer API Key

## Installation

1. Clone the repository:

   ```bash
   git clone [https://github.com/ondrejmlynarc/stackoverflow-data-pipeline.git](https://github.com/ondrejmlynarc/stackoverflow-data-pipeline.git)
   cd stackoverflow-data-pipeline
