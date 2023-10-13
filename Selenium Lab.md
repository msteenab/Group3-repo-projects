_______________________________________________________________________

	Group 3	SELENIUM LAB	
_______________________________________________________________________


## LAB 01	AUTOMATION WITH SELENIUM

### OBJECTIVES
- Provide details on commands commonly used in Selenium
- Create a Selenium Script
- Automate browser actions for web application testing.
- Understand and utilize Selenium WebDriver using Python.
- Validate web application UI elements and functionalities.

### FAQ (Frequently Asked Questions)
1. My command line is displaying this error message:

![pipError](https://miro.medium.com/v2/resize:fit:1067/1*wyc5U_i45xQ5g-t4e33FUQ.png)
#### This error message is most likely due to:
- Your environment not having the path to your python folder/scripts.
- Your pip version not being in your "scripts" folder.
- Your python is outdated.
#### How do I fix this?:
##### Method 1 (Copy the path into your environment)
1. 


### PREREQUISITE
- Must have a basic level of knowledge of the python language

## BEFORE YOU GET STARTED
You will need the following in order for your tests to perform correctly 

- Install a web browser to run the web application
    - This can be:
        - Firefox (Recommended)
        - Chrome
        - Microsoft Edge
- Create a GitHub account
    - Clone the GitHub repository

### HOW TO CREATE A GITHUB ACCOUNT
- Navigate to this page on how to create a GitHub account: https://docs.github.com/en/get-started/onboarding/getting-started-with-your-github-account

### HOW TO CLONE A GITHUB REPOSITORY
- Navigate to this page on how to clone a GitHub repository: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
### OVERVIEW
Selenium is a great way to automate web interactions and perform automated browser testing. You can use selenium with multiple languages, but in this lab we will only focus on python. The latest version of selenium is selenium 4. The information below is a step-by-step guide on how to help you get started.

### Step 1: Install Python
If you have not, you will need to install Python on your computer. To do so please navigate to Python official website to download the latest version: https://www.python.org/downloads/ 

Note: Make sure to download the right file based on your OS, as well as adding Python to your system's PATH during installation.

The current supported versions for Selenium are:
- 2.7
- 3.5+

#### (IF YOU AlREADY HAVE PIP ON YOUR SYSTEM):
If you already have pip installed on our system, you can upgrade it by using the following command in either the command line or terminal:
![pipUpgrade](file:///C:/Users/aliya/Documents/Classes%20For%20Summer%202023/CSC%20256/Screenshot%202023-10-13%20115546.png)

### Step 2: Install Selenium
You can install Selenium using Python's package manager, pip. Open your command prompt or terminal and run the following command:    
`{ pip install selenium }`

![pipCommand](https://github.com/3osmic/Group3-repo-projects/assets/113747615/e9cf1bf1-cda0-4ff6-83b5-e7f4389c208b)


Once installed, a successfully installed message should be displayed.

### Step 3: Download a Web Driver
Selenium interacts with web browsers using drivers. You will need to download the appropriate driver for the web browser you want to automate. Such as Chrome, Firefox, and Edge.  
Drivers can be found in the following URL's:	

	- ChromeDriver: https://sites.google.com/a/chromium.org/chromedriver/	
	- GeckoDriver (for Firefox): https://github.com/mozilla/geckodriver/releases	
	- EdgeDriver: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/	
 
Note: Download the appropriate driver for your browser and make sure to add the driver exe to your system's PATH.  
For more platform options please visit the selenium official website, and scroll down to browsers.
(https://www.selenium.dev/downloads/)


Once Selenium is installed, you’re ready to create your first Selenium script!
### Step 4: Create Your First Selenium Script 
Here is a simple Python script that opens a browser, navigates to a website and performs some action with expected results:	

![FirstScript](https://github.com/3osmic/Group3-repo-projects/assets/113747615/083e734e-18ca-4787-8228-0384d1085194)

### Class Diagram of Web Application Back-End Functionalities:































