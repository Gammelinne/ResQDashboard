# Shiny Python Web Application

## Overview

This repository contains the code for an interactive web application developed using the Shiny framework for Python. The application includes a "Dashboard" and a "Custom Dashboard" with specific tabs for visualizing and analyzing hospital data.

## Features

### Dashboard Tab

- **User Interface (UI):** The UI is designed for a rich and convenient visual experience, featuring informative cards and accordion sections.
- **Reactive Updates:** The server logic coordinates data processing and updates the UI reactively in response to user interactions.
- **Shiny Modules:** Overcame the challenge of creating unique graphs for each category using Shiny modules, enhancing code modularity and reusability.

### Custom Dashboard Tab

#### Timeline Tab

- **Temporal Visualization:** Users can dynamically choose the Y-axis based on Quality Indicators (QI) and activate features such as error or trend display.
- **Interactive Graphs:** The `timeline_dashboard_server` function efficiently extracts relevant data and generates interactive temporal graphs.

#### Distribution Tab

- **Understanding Data Distributions:** Users can customize the X-axis, choose to display median or mean lines, and explore specific details for each data point.
- **Informative Visualizations:** The `distribution_dashboard_server` function translates user choices into informative distribution visualizations.

#### Correlation Tab

- **Exploring Relationships:** Users can select X and Y axes, with the option to add a comparison factor.
- **Detailed Correlation Graphs:** The `correlation_dashboard_server` function generates detailed correlation graphs to identify trends and links between variables.

#### Sub-group Comparison Tab

- **Comparing Data Subgroups:** Users can compare various aspects, such as gender, mRS score, or completion of imaging exams.
- **Detailed Comparative View:** The `comparison_dashboard_server` function generates comparison graphs offering a detailed view of the data.