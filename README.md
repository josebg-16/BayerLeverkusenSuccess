 # Analyzing BayerLeverkusen Success: Bundesliga Dashboard and Scraping Project

This project provides an automated way to scrape Bundesliga statistics and visualize insights into teams' performances through a dashboard. The scraped data is processed and displayed using Tableau.

![Bundesliga Dashboard](Dashboard%201.png)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dashboard Insights](#dashboard-insights)
- [Acknowledgments](#acknowledgments)

---

## Introduction

This project leverages Python to scrape football data from [FBref](https://fbref.com/) for the Bundesliga 2023/24 season. The data covers various performance metrics such as shooting, passing, goalkeeping, and defensive actions. The processed data is then used to create a visually appealing dashboard in Tableau.

---

## Features

- **Automated Data Scraping:** 
  Extracts data from the Bundesliga stats page, including team performance metrics.
  
- **Custom Calculations:**
  - Shooting efficiency (`Shots per Goal` ratio)
  - Progressive passes and third passes per 90 minutes
  - Defensive and goalkeeper metrics
  
- **Merged Dataset:** Combines data into a single file (`data.csv`) for easy analysis.

- **Interactive Dashboard:** Visualizes:
  - Teams' pass distribution
  - Defensive capabilities
  - Goalkeeper save percentages
  - Rivals' expected goals (xG) and penalties

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/bundesliga-dashboard.git
    cd bundesliga-dashboard
    ```

2. Install the required Python libraries:

    ```bash
    pip install pandas
    ```

3. Ensure you have Tableau or Tableau Public installed to open and edit the `Dashboard.twb` file.

---

## Usage

1. **Run the scraping script:**

    ```bash
    python scrapper.py
    ```

    This script will scrape the required data and save it in `data.csv`.

2. **Open the dashboard:**

    Load the `Dashboard.twb` file in Tableau to visualize the data.

---

## Dashboard Insights

### Pass Distribution
Visualizes the number of progressive passes per 90 minutes against passes in the last third, highlighting top-performing teams like Bayer Leverkusen.

### Teams' Effectiveness
Explores the relationship between goals minus expected goals (G-xG) and the average shots to score a goal.

### Teams' Defensive Capacity
Examines recoveries per 90 minutes against opponent shot-creating actions per 90 minutes.

### Goalkeeper Statistics
Compares save percentages and defensive penalties for all Bundesliga teams.

---

## Acknowledgments

- Data Source: [FBref](https://fbref.com/)
- Visualization: Created using Tableau
- Python Libraries: `pandas`

Feel free to contribute to the project or raise issues by submitting a pull request or opening an issue.
