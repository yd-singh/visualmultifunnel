Funnel Simulation Project

author: https://www.linkedin.com/in/yashdeepsingh/

Read Me Before You Start

Welcome to the Funnel Simulation Project! This project provides a comprehensive toolset for designing, visualizing, and simulating complex funnels or workflows. It consists of two main components:

	1.	Funnel Configuration Builder (config_builder.py): An interactive Streamlit application that allows you to create and visualize funnel configurations without manually editing YAML files.
	2.	Funnel Simulation Application (main.py): The core application that runs simulations based on the funnel configurations you’ve created, providing insights and analytics on the funnel’s performance.

Brief Introduction

In many industries, workflows and processes can be represented as funnels consisting of multiple stages or modules. Understanding and optimizing these funnels is crucial for improving efficiency, reducing costs, and enhancing user experience. This project aims to simplify the creation and analysis of such funnels by providing intuitive tools for both configuration and simulation.

	•	Funnel Configuration Builder (config_builder.py): This tool lets you design your funnel step by step. You can define modules, set parameters like success rates and costs, and specify the flow between modules. The builder provides real-time visualization and generates a YAML configuration file that can be used by the simulation application.
	•	Funnel Simulation Application (main.py): Using the configurations created with the builder, this application runs simulations to model how entities (e.g., customers, applications) move through the funnel. It helps you analyze metrics like conversion rates, bottlenecks, time to completion, and cost efficiency.

By combining these tools, you can iteratively design, test, and optimize your funnels to achieve better performance and outcomes.

Funnel Configuration Builder

The Funnel Configuration Builder is a Streamlit application that allows users to create and visualize funnel configurations interactively. Users can define modules, set parameters, and specify the flow of their funnel without manually editing YAML files. The app provides real-time updates to the configuration and visualization, making it easy to design complex funnels.

Table of Contents

	•	Features
	•	Installation
	•	Getting Started
	•	Usage
	•	1. Enter Funnel Name
	•	2. Add Modules
	•	3. Define Module Parameters
	•	4. Specify Next Modules
	•	5. View Configuration and Visualization
	•	6. Download Configuration
	•	7. Reset and Start Over
	•	Example Workflow
	•	Notes
	•	Contributing

Features

	•	Interactive Module Definition: Add, edit, and delete modules through an intuitive interface.
	•	Real-Time Visualization: See the funnel structure update in real-time as you make changes.
	•	Automatic Module Handling: New modules referenced in next steps are automatically added for definition.
	•	Standardized Module Names: Module names are standardized to uppercase with underscores to ensure consistency.
	•	Terminal Steps: Use “APPROVED” or “REJECTED” to represent terminal steps in your funnel.
	•	YAML Configuration Export: Download the funnel configuration as a YAML file for use in other applications.

Installation

Prerequisites

	•	Python 3.7 or higher
	•	pip (Python package installer)

Steps

	1.	Clone the Repository

git clone https://github.com/yourusername/funnel-simulation-project.git
cd funnel-simulation-project


	2.	Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate


	3.	Install Dependencies

pip install -r requirements.txt

If requirements.txt is not provided, you can install the necessary packages directly:

pip install streamlit pyyaml



Getting Started

To start the Funnel Configuration Builder app, run:

streamlit run config_builder.py

To start the Funnel Simulation Application, run:

streamlit run app.py

Note: Ensure that you have created a funnel configuration using the builder before running the simulation application.

Usage

1. Enter Funnel Name

	•	Upon launching the Funnel Configuration Builder, you’ll be prompted to enter a Funnel Name.
	•	The name will be sanitized by replacing spaces with underscores and will be used as the filename when downloading the configuration.
	•	Click “Set Funnel Name” after entering the name.

2. Add Modules

	•	Click the “Add Module ➕” button to create a new module form.
	•	You can add as many modules as needed for your funnel.

3. Define Module Parameters

For each module:

	•	Module Name: Enter a unique name for the module. The name will be automatically converted to uppercase and spaces replaced with underscores.
	•	Is Start Module: Check this box if the module is a starting point in your funnel. You can have multiple start modules.
	•	Success Rate: Enter the probability (between 0 and 1) of the module succeeding.
	•	Cost per Transaction: Specify the cost associated with each transaction in this module.
	•	Time to Complete: Enter the time (in seconds) it takes to complete the module.

4. Specify Next Modules

	•	Next Module on Success and Next Module on Failure: Enter the name of the next module to proceed to upon success or failure.
	•	Terminal Steps: Use “APPROVED” or “REJECTED” to represent terminal steps in your funnel.
	•	New Modules: If you enter a module name that hasn’t been defined yet, a new module form will be automatically added for you to define later.

Note: Module names in next steps are standardized just like module names.

5. View Configuration and Visualization

	•	As you save modules, the YAML Configuration and Funnel Visualization sections will update automatically.
	•	YAML Configuration: Displays the current configuration in YAML format.
	•	Funnel Visualization: Shows a graphical representation of your funnel structure using Graphviz.

6. Download Configuration

	•	Once you’re satisfied with your funnel, you can download the configuration file.
	•	Click the “Download YAML” button to save the configuration as a YAML file named after your funnel.

7. Reset and Start Over

	•	If you wish to start over, click the “Reset and Start Over” button.
	•	This will clear all data, and you’ll be prompted to enter a new funnel name.

Example Workflow

	1.	Enter Funnel Name
	•	Funnel Name: Loan Application Process
	2.	Add Start Module
	•	Click “Add Module ➕”.
	•	Module Name: Document Submission
	•	Is Start Module: Checked
	•	Success Rate: 0.9
	•	Cost per Transaction: 5
	•	Time to Complete: 60
	•	Next Module on Success: Credit Check
	•	Next Module on Failure: REJECTED
	•	Click “Save Module”.
	•	A new module form for CREDIT_CHECK is automatically added.
	3.	Define Credit Check Module
	•	Scroll to the new module form for CREDIT_CHECK.
	•	Module Name: Already filled as CREDIT_CHECK.
	•	Is Start Module: Unchecked
	•	Success Rate: 0.85
	•	Cost per Transaction: 10
	•	Time to Complete: 120
	•	Next Module on Success: APPROVED
	•	Next Module on Failure: REJECTED
	•	Click “Save Module”.
	4.	Review Funnel
	•	The YAML Configuration and Funnel Visualization sections display the current state of your funnel.
	•	The visualization shows the flow from DOCUMENT_SUBMISSION to CREDIT_CHECK, leading to APPROVED or REJECTED.
	5.	Download Configuration
	•	Click “Download YAML” to save your funnel configuration for use in your application.

Notes

	•	Module Naming Conventions: Module names are automatically converted to uppercase with underscores to ensure consistency and prevent duplicates.
	•	Deleting Modules: If you need to remove a module, use the “Delete Module” button within its form. This will also clear any references to it in other modules.
	•	Terminal Steps: Use “APPROVED” and “REJECTED” to represent the end points of your funnel.
	•	Automatic Module Addition: When you reference a new module in the next module fields, a new module form will be added automatically.
	•	Editing Modules: You can edit any module at any time by expanding its form, making changes, and clicking “Save Module”.


Onboarding Funnel Simulation

This project simulates customer onboarding funnels, allowing you to model, analyze, and compare different configurations of verification modules. It calculates key metrics such as success rates, costs, and processing times, providing insights into the efficiency and effectiveness of your onboarding processes. Additionally, it offers interactive visualizations and an intuitive web interface for a comprehensive analysis.

Table of Contents

	•	Features
	•	Demo
	•	Getting Started
	•	Prerequisites
	•	Installation
	•	Usage
	•	Running the Streamlit App
	•	Using the Dashboard
	•	Configuration
	•	Modules Configuration (configs/)
	•	Visualizations
	•	Sankey Diagram
	•	Time Distribution Chart
	•	Cost Distribution Chart
	•	Success Distribution Chart
	•	Configuration Flow Graph
	•	Example Output
	•	Customization
	•	Acknowledgments

Features

	•	Simulate customer flow through customizable onboarding funnels.
	•	Calculate success rates, total and average costs, and processing times.
	•	Compare multiple configurations side by side.
	•	Interactive web interface using Streamlit.
	•	Detailed visualizations including Sankey diagrams, bar charts, and configuration flow graphs.
	•	Easy configuration via YAML files.

Demo


Getting Started

Prerequisites

Ensure you have the following installed:

	•	Python 3.6 or higher
	•	pip package manager
	•	Git (optional, for cloning the repository)

Installation

	1.	Clone the repository:

git clone https://github.com/yourusername/onboarding-funnel-simulation.git
cd onboarding-funnel-simulation


	2.	Create a virtual environment:

python -m venv venv


	3.	Activate the virtual environment:
	•	On Windows:

venv\Scripts\activate


	•	On macOS/Linux:

source venv/bin/activate


	4.	Install required Python packages:

pip install -r requirements.txt

If requirements.txt is not provided, install the packages individually:

pip install pandas pyyaml tabulate plotly matplotlib seaborn streamlit



Usage

Running the Streamlit App

	1.	Navigate to the project directory (if not already there):

cd onboarding-funnel-simulation


	2.	Activate your virtual environment (if not already activated):
	•	On Windows:

venv\Scripts\activate


	•	On macOS/Linux:

source venv/bin/activate


	3.	Run the Streamlit app:

streamlit run app.py


	4.	Access the app:
	•	The app will automatically open in your default web browser.
	•	If not, navigate to http://localhost:8501 in your browser.

Using the Dashboard

	•	Select Configurations:
	•	Use the sidebar to select one or more configurations from the dropdown list.
	•	You can select multiple configurations to compare their performance.
	•	Set Number of Customers:
	•	Enter the number of customers to simulate.
	•	The default value is 100.
	•	Run Simulation:
	•	Click the “Run Simulation” button to execute the simulation.
	•	View Results:
	•	Summary Statistics: Displays key metrics for each configuration.
	•	Comparative Analysis: When multiple configurations are selected, shows side-by-side comparisons.
	•	Visualizations: Includes Sankey diagrams, bar charts, and configuration flow graphs.
	•	Detailed Module Results: Provides in-depth data for each module in the funnel.

Configuration

Modules Configuration (configs/)

The simulation uses YAML configuration files stored in the configs/ directory to define the modules in each onboarding funnel.

Example Configuration (configs/config1.yaml):

modules:
  - name: Phone Verification
    is_start: true
    success_rate: 0.97
    cost_per_transaction: 2
    time_to_complete: 30
    next_module_on_success: "PAN Verification"
    next_module_on_failure: "Failed"

  - name: PAN Verification
    success_rate: 0.90
    cost_per_transaction: 1
    time_to_complete: 20
    next_module_on_success: "CKYC Verification"
    next_module_on_failure: "Failed"

  - name: CKYC Verification
    success_rate: 0.75
    cost_per_transaction: 1.75
    time_to_complete: 8
    next_module_on_success: "VCIP"
    next_module_on_failure: "Digilocker Verification"

  - name: Digilocker Verification
    success_rate: 0.70
    cost_per_transaction: 2
    time_to_complete: 15
    next_module_on_success: "VCIP"
    next_module_on_failure: "Failed"

  - name: VCIP
    success_rate: 0.50
    cost_per_transaction: 10
    time_to_complete: 120
    next_module_on_success: "Success"
    next_module_on_failure: "Failed"

Configuration Parameters:

	•	name: The name of the module.
	•	is_start: Indicates if this module is the starting point of the funnel.
	•	success_rate: The probability (between 0 and 1) that a customer passes the module.
	•	cost_per_transaction: The cost incurred per customer processed in the module.
	•	time_to_complete: Time (in seconds) taken to process each customer in the module.
	•	next_module_on_success: The next module if the customer passes. Use "Success" if it leads to final success.
	•	next_module_on_failure: The next module if the customer fails. Use "Failed" if the customer is terminally rejected.

Customizing Modules:

You can add, remove, or modify modules by editing or creating YAML files in the configs/ directory. Ensure that:

	•	There is exactly one module with is_start: true.
	•	The next_module_on_success and next_module_on_failure refer to valid module names, "Success", or "Failed".

Visualizations

The application provides several visualizations to help you understand and analyze the simulation results.

Sankey Diagram

The Sankey diagram illustrates the flow of customers through the modules, showing how many pass or fail at each stage.

Note: Replace ./images/sankey_example.png with the path to an actual Sankey diagram generated by your app.

Time Distribution Chart

Shows the total time spent in each module.

Note: Replace ./images/time_distribution_example.png with the path to an actual time distribution chart.

Cost Distribution Chart

Displays the total cost incurred in each module.

Note: Replace ./images/cost_distribution_example.png with the path to an actual cost distribution chart.

Success Distribution Chart

Illustrates the number of customers who passed or failed in each module.

Note: Replace ./images/success_distribution_example.png with the path to an actual success distribution chart.

Configuration Flow Graph

Visualizes the structure of the funnel as defined in the configuration file.

Note: Replace ./images/config_flow_example.png with the path to an actual configuration flow graph.

Example Output

Summary Statistics

When you run the simulation, the app displays summary statistics for each configuration:

- **Total Success:** 40
- **Total Failures:** 60
- **Success Rate:** 40.00%
- **Total Cost:** ₹1293.25
- **Total Time:** 259.43 minutes
- **Average Cost per Customer:** ₹12.93
- **Average Time per Customer:** 2.59 minutes

Detailed Module Results

A table showing detailed results for each module:

Module	Enter Funnel	Success Rate	Pass	Fail	Final Success	Terminally Rejected	Total Cost	Total Time	Average Cost per Customer	Average Time per Customer
Phone Verification	100	97%	97	3	0	3	200.00	3000.00	2.00	30.00
PAN Verification	97	90%	87	10	0	10	97.00	1940.00	1.00	20.00
CKYC Verification	87	75%	65	22	0	0	152.25	696.00	1.75	8.00
Digilocker Verification	22	70%	15	7	0	7	44.00	330.00	2.00	15.00
VCIP	80	50%	40	40	40	40	800.00	9600.00	10.00	120.00

Comparative Analysis

When multiple configurations are selected, the app displays comparative statistics and visualizations.

Comparative Statistics Table

Configuration	Success Rate (%)	Total Cost (₹)	Total Time (minutes)	Average Cost per Customer (₹)	Average Time per Customer (minutes)
config1	40.0	1293.25	259.43	12.93	2.59
config2	45.0	1145.00	234.67	11.45	2.35

Comparative Visualizations

	•	Success Rate Comparison:

	•	Total Cost Comparison:

	•	Total Time Comparison:

Note: Replace image paths with actual images generated by your app.

Customization

	•	Adding New Configurations:
	•	Create new YAML files in the configs/ directory.
	•	Define the modules and their parameters as per the format.
	•	Modifying Modules:
	•	Adjust the success_rate, cost_per_transaction, time_to_complete, and transitions between modules.
	•	Adjusting Visualizations:
	•	Customize the appearance of charts by modifying the visualization functions in app.py.
	•	Changing Currency Symbol:
	•	The currency symbol is set to ₹ (Indian Rupees). You can change it by replacing ₹ with your desired symbol in the code.


Feel free to contribute to this project by submitting issues or pull requests. Your feedback is highly appreciated!
