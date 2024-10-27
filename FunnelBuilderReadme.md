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
	•	License

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

git clone https://github.com/yourusername/funnel-configuration-builder.git
cd funnel-configuration-builder


	2.	Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate


	3.	Install Dependencies

pip install -r requirements.txt

If requirements.txt is not provided, you can install the necessary packages directly:

pip install streamlit pyyaml



Getting Started

To start the Funnel Configuration Builder app, run:

streamlit run funnel_builder.py

This will open the app in your default web browser at http://localhost:8501.

Usage

1. Enter Funnel Name

	•	Upon launching the app, you’ll be prompted to enter a Funnel Name.
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

Contributing

Contributions are welcome! If you’d like to improve this project, please follow these steps:

	1.	Fork the Repository

git clone https://github.com/yourusername/funnel-configuration-builder.git


	2.	Create a New Branch

git checkout -b feature/your-feature-name


	3.	Make Changes
	•	Implement your feature or bug fix.
	•	Ensure code quality and consistency.
	4.	Commit Changes

git commit -am 'Add your commit message here'


	5.	Push to the Branch

git push origin feature/your-feature-name


	6.	Create a Pull Request
	•	Submit a pull request detailing your changes.
