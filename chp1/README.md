# Montana County Lookup Program

---

## Overview

This Python program allows the user to query Montana county information by **license plate prefix**. Users can choose to see:

- County name
- County seat
- Both county name and county seat

The program reads data from a CSV file (`MontanaCounties.csv`) and allows the user to make multiple queries until they choose to quit.

---

## Requirements

- Python **3.13+** must be installed on your system.  
  You can download it from the [official Python website](https://www.python.org/downloads/).

---

## How to Run

After cloning this GitHub repository into your desired directory,
follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory the repository was cloned in, then navigate to the folder containing `main.py` and `MontanaCounties.csv`.
   
    ```bash
   cd your_desired_directory/chp1
   ```
Once you are within this directory run the following command in your terminal:

```bash
python main.py
```

Then, you will be prompted with a command line program that
requests user county prefix input and outputs county name and county seat information.

---

## Following the Prompts

1. First, choose what information you want returned (County name, County seat, or Both).
2. Then, enter the license plate prefix when prompted (valid numbers are 1 through 56).
3. Type quit to exit the program at any time.

Have fun exploring county data in the beautiful state of Montana!