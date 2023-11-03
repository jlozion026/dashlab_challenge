# Medical Forms Analyzer
 A program that automatically scans and extract information from the doh medical forms and records submitted by users

## Getting Started
To run this project locally, you'll need to set up a **virtual environment** and install the **required dependencies**. Follow the steps below to get started.

### Prerequisites

- Python (3.10.11 or higher) installed on your system.

 
### Setting up a Virtual Environment

A virtual environment is a way to isolate your project's dependencies. It's a good practice to use one to avoid conflicts with other projects. To set up a virtual environment, follow these steps:

1. Open a terminal in the root directory of your project.

2. Run the following command to create a virtual environment:

   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:

   ```bash
   venv\Scripts\activate
   ```
   You'll now be working within the virtual environment, and you can deactivate it by running `deactivate` in the terminal.

### Installing Dependencies
This project uses a requirements.txt file to specify its dependencies. To install these dependencies, follow these steps:
1. Make sure your virtual environment is activated (as explained in the previous section).

2. Run the following command to install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
### Running the Project
Now that you have set up the virtual environment and installed the dependencies, you can run the project.

Simply run this in the root directory of your project.
```bash
python main.py
```
## How to use 
In this section, you will see a demonstration of how to use the created application for Dashlabs. You can check this video or read through it. 
[Promotional Video](https://drive.google.com/file/d/1VBecVfg7D0_4d54JzKVc0DUHnH0Ug2tc/view?fbclid=IwAR3ZfMSBZ1hW_8s1w0SsnonisSK9tLXL2aNKdq3AJspugkFBwAvmKdU0boM)


### Home Screen
This is our home screen, it has four buttons. Button for uploading a single file, uploading a folder for processing multiple files, inserting the data extracted JSON to main CSV, and View CSV 

![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/7e05350f-0dfc-4973-9bd9-cbc0315a7b37)

### Upload a Single File
1. To process a single file simply click `upload a file` button

   ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/cbc45e97-f4b1-46ab-8614-de91e9929a3b)

3. After clicking the button, a file dialog will pop up. Choose a form you want to process. For this example, I will be processing a landbase_cert_3.jpg file or a Medical Certificate for Landbased Overseas Workers

   ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/fa661f2d-1901-4e2f-8093-fb5a282cddae)

   ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/52adc895-e323-44af-ac74-dcf259415d2c)

4. A new window will pop up that has an empty canvas and a process document button
   ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/1258b17b-e1c9-4c5c-82fa-a619303df320)

   ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/58967fc8-8491-42ac-8496-cef8cdd97410)

   This button will start to process document

6. 
