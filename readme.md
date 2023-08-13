# Distance and Address Calculator using Geopy

This repository contains two Python scripts for calculating the distance and retrieving the main address between the user's current location and another specified location using the Geopy library.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

The Distance and Address Calculator is a set of Python scripts that utilize the Geopy library to calculate the distance and retrieve the main address between two locations. One location is determined by `ipinfo.com`, while the other location is specified using latitude and longitude coordinates. This functionality can be useful in various applications, including location-based services, travel planning, and more.

## Installation

Before using the Distance and Address Calculator, ensure you have the required packages installed. You can install them using `pip` by running the following command in your terminal or command prompt:

```bash
pip install -r requirements.txt
```

This will install the necessary packages, including Geopy, which is used for geolocation calculations.

## Usage

1. Clone this repository to your local machine using:

```bash
git clone https://github.com/sodiqlef/distance-calculator.git
```

2. Change to the repository directory:

```bash
cd geolocation-distance-calculator
```

3. Install the required packages as mentioned in the installation section.

4. Run the Distance Calculator script using Python:

```bash
python distance-calculator.py
```

5. Follow the prompts to provide the latitude and longitude of the other location for which you want to calculate the distance.

6. The script will calculate and display the distance in kilometers between the user's current location and the specified location.

7. To use the new functionality in `distance-address.py` that calculates the distance and retrieves the main address, run the script using Python:

```bash
python distance-address.py
```

8. Follow the prompts to provide the latitude and longitude of the other location.

9. The script will calculate and display the distance in kilometers as well as the main address of the specified location.

---

Happy distance and address calculating! If you have any questions or need further assistance, please don't hesitate to contact me.
