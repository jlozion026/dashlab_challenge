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

### Processing Document
4. A new window will pop up that has an empty canvas and a process document button
   ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/1258b17b-e1c9-4c5c-82fa-a619303df320)

   ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/58967fc8-8491-42ac-8496-cef8cdd97410)

   This button will start to process document

6. During the processing of document, a print diagnostic will be shown.
   ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/2ff4c622-e91a-4ce4-93b6-81f2b6190192)
  
   File Information
   - File being processed: landbase_cert_3.jpg - Tells what file is under the process
   - MIME Type: image/jpeg - Tells the content of the file which a jpeg file
  
   Document Classifier Status - This tells the status of Document Classifier 
   - Document Classifier Status (1): running 
   - Document Classifier Status (2): succeeded

   Document Information 
   - Document Type: Landbase Certificate - This tells that the Landbase Certificate is the model being processed
   - Accuracy: 23.7% - Please note that the accuracy of 23.7% suggests that the document classifier may have identified the document type with a relatively low confidence level. Further review and validation may be required, depending on the specific use case.

    Processing Steps
    1. Processing Document... - The system initiated the processing of the document.

    2. Request Successful - The initial request to process the document was successful.

    3. Creating JSON file - The system generated a JSON file, possibly containing the extracted information.

    4. Text extraction successful to landbase_cert_3.jpg - The text extraction process from the document (landbase_cert_3.jpg) was successful.

    Processing Result
    - Processing Successful! - The document processing was completed successfully, and the extracted text in json file is ready for insert

### Upload a Multiple File by uploading a folder
7. In your file explorer add the files you want to process. For this example I will be uploading for upload forms folder with the following content

   ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/a540bdd1-8e16-4776-a820-3e16066e3b3c) ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/a3e7dd4c-7487-4888-bf4f-08bb3ced7987).

9. Click the `Upload a Folder` button

   ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/a2219acd-f76a-4093-bbba-3918b9200b1e)

10. Choose the for upload forms folder. Do step 4 for processing document and see the printing status. Please be noted that the window screen will freeze when it starts to process the form. To see live status refrain from touching the window screen. 

 
    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/8db51f01-fcd4-4dc7-b1a7-abada764cfcb)
 
    HIV Certificate Processed 
   
    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/71053f14-63de-4d6c-9dfb-97849749855e)
 
    Medical Certificate for Landbase Overseas Workers
   
    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/b0aa1df9-a85c-4e3d-bfe8-e2d4535aecd1)
 
    Medical Certificate for Service at Sea
   
    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/aa385b0e-92f8-4a00-903e-b46e3caa3b70)
 
    Pyschological Evaluation Form
   
    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/f15a4ea7-ea5f-4061-97d6-05af746ee302)
 
    Medical Examination Report for Landbased Overseas Workers
   
    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/c37789ed-d3e7-480e-8201-a68df7de2a15)
 
    Medical Examination Report for Seafarers

    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/145285a8-8aa8-4a6d-bf16-5b1d916b1aa1)

### Insert Data to CSV
11. In the home screen there is a `insert data` button. The purpose of this button was to actually use the json data extracted from processing the document, convert it to a dataframe, and then insert it to a dedicated csv file for storage. 

    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/9e023171-0c05-4be2-bac2-be05e1ea7822)

12. After click the `insert data` button, a window will pop up telling the result of insertion
    
    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/108fcaf7-40ab-456f-ae7b-9c7bb9d51271)

13. When you clicked the `insert data` button data again, a new message will show telling No dataframes to concatenate. Upload a form. This is just common since we successfully inserted the data in csv and the json files are move to new folder.

    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/48eb4439-ad46-4347-be87-ee0d16d88f2a)


### Viewing of CSV
14. To view the stored data, simply click the `View CSV` button.
    
    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/802f3e6a-904c-4360-9a60-c4a515654035)

15. After clicking the `View CSV` button, a new window will pop up displaying different buttons dedicated for each form.
    
    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/56921244-dd4b-422f-86ab-b2399d00afc8)

16. As an example, let us view the `Medical Examination Report for Overseas Workers`.

    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/35f9dc92-a0b2-4d78-b646-6f7ca2fdf138)

17. It will automatically open the csv file holding the extracted data. You can edit and fix the wrongly extracted data

    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/aeca90d1-af3e-4898-8437-d3750b83ef03)

### ZIP and Encrypt All CSV Files

18. Click the button `ZIP and Encrypt All CSV Files`.

    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/12044b76-19f8-4cc3-a13a-d70bb22c3edd)

19. After clicking the `ZIP and Encrypt All CSV Files` a pop up will show asking you to enter the name of your zip file.

    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/e997fb86-88ad-478a-b308-99e7a9b9d3f0)

20. After entering your name a pop up will show asking you to add a password to your zip file
 
    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/974eda9b-9506-4568-ae1a-83f1fbdd4d6a)

21. After setting the password a filedialog will pop up. This will help you navigate where to put your zip file

    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/151d5bbf-4d36-4250-8555-9ed8031db1c9)

22. You can now access the downloaded zipped file. Note that use winrar to open and extract the files.

    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/c37a3429-9741-4ca4-9522-e3af1d47636a)

    ![image](https://github.com/jlozion026/dashlab_challenge/assets/82523427/6bc3ebf4-e81a-4a14-af71-20831e93af44)



    
