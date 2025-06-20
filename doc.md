# 📘 PipeCM – User Manual  
**Version:** 1.0  
**Organization:** Bhabha Atomic Research Centre (BARC)  

---

## Chapter 1: Getting Started – Registering and Logging into PipeCM

### 📌 Overview

**PipeCM** (Pipeline Corrosion Monitoring) is a robust application designed to evaluate pipeline conditions and perform health assessments based on tool and sensor data. This chapter guides the user through the process of account creation and login, ensuring secure access to the features.

---

## 🧾 1.1 Create an Account

To access the features of PipeCM, you must first create a user account.

### ➤ Step-by-Step Registration Process:

📷 **Screenshot:**  
![1 1](https://github.com/user-attachments/assets/97d0ea1a-f61c-4107-85f2-925660d1dd04)
1. **Username**: Enter a unique username (e.g., `roshansahu`).
2. **Email**: Provide a valid email address for notifications and recovery.
3. **Password Requirements**:
    - At least 1 uppercase letter  
    - At least 1 lowercase letter  
    - At least 1 number  
    - At least 1 special character (e.g., `@`, `#`, `!`)
4. **Re-enter Password**: Type your password again to confirm.

🛑 If any password condition fails, an error message in red will be shown below the input field.

✅ Once all fields are correctly filled, click on the **"CREATE USER"** button.

---

## 🔐 1.2 Login to the System

After registering, return to the login screen to access the application.

📷 **Screenshot:**  
![2](https://github.com/user-attachments/assets/716bb085-c46c-42da-b52c-38a477f21859)



### ➤ Login Steps:

1. **Enter Username** used at the time of registration.  
2. **Enter Password**.  
3. Click the **"LOGIN"** button.

If your credentials are valid, you will be redirected to the home/dashboard screen.

---

## 💡 Additional Options

- **Already Registered? Login Now!** – Click this if you already have an account.  
- **New Here? Register Now!** – New users should click here to open the registration form.  

---

## 🧭 1.3 Pipecm Analysis Dashboard

📷 **Screenshot:**  
![3](https://github.com/user-attachments/assets/dbb8012a-2409-4d91-942f-9929a0aee055)




After successful login, users land on the main dashboard containing the following modules:

- **MFL + EC** – Gas pipeline inspection  
- **MFL + UT** – Oil pipeline inspection using ultrasonic and flux leakage data  
- **Health Assessment** – Tool and pipeline data analysis  
- **Settings** – Customize software configurations  

Each section contains a **"Start App"** button to launch its respective module.

---

# 📘 Chapter 2: Creating and Managing Runs 

This chapter walks you through the complete process of creating a new pipeline run in PipeCM — including tool selection, run details, file uploads, and confirmation, and then managing existing runs.

---

## 🧾 2.1 Create a Run

### 🧾 2.1.1 Select Tool

The first step is to choose the appropriate inspection tool for the pipeline run,**click on Start App**

**Screenshot:**
![Uploading 3.PNG…]()

![4](https://github.com/user-attachments/assets/9cf1496f-40d7-42da-91c9-8b5970f44356)

**Steps:**

1. From the **Select Tool** screen, choose a tool by clicking the radio button in the **Select** column.
2. **Before selecting tool click on plus button in bottom right to add a run**
- **Tool details include:**
  - **Tool Type:** e.g., `MFL_OCTA_GEN1`
  - **Tool Size:** e.g., `12 inch`
3.Click **NEXT** to proceed.

### 🧾 2.1.2 Create Run Details

Enter run-specific metadata such as source, destination, and date.

**Screenshot:**

![5](https://github.com/user-attachments/assets/92c60686-0dd2-49c1-a728-37ba472e5abb)

**For Example: Fill the following fields-**

1. **Run Source:** e.g., `location1`
2. **Run Destination:** e.g., `location2`
3. **Run Date:** e.g., `19/06/2025`

4. Click **ADD** to create the run entry.

### 🧾 2.1.3 Uploading Binary Files

After the run is created, upload sensor data files.

#### 2.1.3.1 Browse and Select Files

1. Click **BROWSE FILES**
2. Select files from your system (e.g., `TMP0001_AK.bin`, `TMP0002_AK.bin`)

**Screenshot:**
![11](https://github.com/user-attachments/assets/19dc3bcb-9696-4d55-a5dd-642a17ec29d2)
![8](https://github.com/user-attachments/assets/d1d2e933-a088-4721-a57d-a59770885910)
![Screenshot (81)](https://github.com/user-attachments/assets/0a67e097-2ee5-411a-8f28-31885ade7be0)


#### 2.1.3.2 Upload the Files

1. Selected files will show with progress bars.
2. Click **UPLOAD** to start the transfer.

**Screenshot:** 
![9](https://github.com/user-attachments/assets/1a741dd3-a22a-4306-b3a6-e942f9a78ca9)
![Screenshot (82)](https://github.com/user-attachments/assets/1d7b4a38-f49a-4756-91b2-27b00427535f)


#### 2.1.3.3 Save and Confirm

Once upload completes:

1. Click **SAVE**
2. A confirmation popup appears:

> *“Do you want to proceed with processing?”*  
> *“If confirmed, you cannot upload files anymore to this Run…”*

**Screenshot:** 
![10](https://github.com/user-attachments/assets/0ffd966f-5440-47c4-953c-9347be1ab38a)
![Screenshot (83)](https://github.com/user-attachments/assets/312189d9-8cfe-4d0b-8d0e-3f2a18564a88)


3.Click **YES, I'M SURE** only when ready to finalize.

⚠️ **Note:** After confirmation, no more files can be added to this run.

### 🧾 2.1.4 Run Status & Processing

After saving, you’re redirected to the **Select Run** screen.

📷 **Screenshot:**
![11](https://github.com/user-attachments/assets/02675c3f-efaf-458e-9041-bc2b399e3b57)


**Check the Status column:**
- Initially: `FILES_TO_BE_UPLOADED`,`INTERMIDIATE_TO_BE_GENERATED`
- Afterwards: `TO_BE_PROCESSED`

1.Click **NEXT** to continue.

---

### 🧾 2.1.5 Review Uploaded Files

On the **Select File** screen, you can view the uploaded `.bin` files.

📷 **Screenshot:**
![12](https://github.com/user-attachments/assets/caa0c021-6cf5-4d70-b3e3-a9cc871efb50)


Each file displays:
- **File Name**
- **Sequence Number**
- **Status:** `TO_BE_PROCESSED`

---

### 🧾 2.1.6 Status Change on Navigation

If you return to the **Select Run** screen by clicking **BACK**, the status of the run changes:

- `FILES_TO_BE_UPLOADED`/`INTERMIDIATE_TO_BE_GENERATED` → `TO_BE_PROCESSED`

📷 **Screenshot:**
![13](https://github.com/user-attachments/assets/db4efece-89f6-4bf0-a072-e835a9e9f0be)


This means the system has queued your files for processing.
### 🧾 2.1.7 Edit Configurations

To modify the configurations associated with a selected run:

1. Go to the **Select Run** screen.
2. Locate the desired run from the table.
3. In the top right corner of the table, click the **setting icon (edit icon)**.


This action will navigate you to the **Configure** screen for the selected run, where you can modify parameters related to the run's data processing.

[Link to Chapter 3: Modifying Configurations](#-chapter-3-modifying-configurations)

---

## 🧾 2.1.8 Auto Analysis

This section will cover the steps for initiating and reviewing auto-analysis of the run data.

[Link to Chapter 4: Auto Analysis](#-chapter-4-auto-analysis)


---

---
## 🧾 2.2 Select Run and Manage Runs

### 2.2.1 Select Existing Run

To manage or analyze an existing run, follow these steps:

1. Navigate to the **Select Run** screen.
2. Click **NEXT** on the **Select Tool** screen to proceed.
3. From the list of existing runs, choose your desired run by clicking on the row.
4. After selecting a run, you have two options:
  - Click the **Settings icon** (top right) to edit configuration settings.
  - Click **NEXT** again to proceed directly to **Auto Analysis** (if configurations are already set).

**Screenshot:** 
![7](https://github.com/user-attachments/assets/de49338d-2201-43ef-bafb-89affb60f060)


---

### 2.2.2 Edit Configurations

To modify the configurations associated with a selected run:

1. From the **Select Run** screen, after choosing the run,
2. Click the **settings icon (edit icon)** in the top right corner of the run table.

This will take you to the **Configure** screen, where parameters related to the run's data processing can be modified.

[Link to Chapter 3: Modifying Configurations](#-chapter-3-modifying-configurations)

---

### 2.2.3 Auto Analysis

Once the run is selected and optionally configured, you can proceed with automatic analysis of the uploaded data.

1. From the **Select Run** screen, after selecting a run, click **NEXT** to begin analysis.
2. Review the file and analysis summary on the next screen.

[Link to Chapter 4: Auto Analysis](#-chapter-4-auto-analysis)


# 📘 Chapter 3: Modifying Configurations

This chapter describes how to view and edit the configurations associated with a selected run in the PipeCM application.

---

## 🧾 3.1 Accessing the Configuration Interface

To modify the configurations:

1. Go to the **Select Run** screen.
2. Locate the desired run from the table.
3. In the top right corner of the table, click the **pencil icon (edit icon)**.

📷 **Screenshot:**
![11](https://github.com/user-attachments/assets/34b317e9-3665-4e2a-9721-bec8bc4a3924)


> This action will navigate you to the **Configure** screen for the selected run.

---

## 🧾 3.2 Overview of Editable Configurations

The **Configure** screen allows modification of parameters related to the run's data processing.

📷 **Screenshot:**
![14](https://github.com/user-attachments/assets/5264e5f9-0e00-4f2c-b539-82364eb7df7d)


### Key Editable Sections:

- **Thresholds:**
  - `WedThreshold`
  - `Sleeve Threshold`
  - `Flange Threshold`
  - `Marker Threshold`
  - `Valve Threshold`
  - `Feature Peak Distance`
  - `Contour Threshold`
  - `Overlap Cnfl`
  - `Max Db Peaks`
  - `Gauss Sensitivity`

- **Tool Config:**
  - `Word Size`
  - `Packet Size`
  - `NoOfChannels`

- **SensorCountMap:**
  - `HALL`

- **Faulty Channels:**
  - `HALL`
  - `EDDY`

- **Odometer Diameter:**
  - `Odometer[0]`, `Odometer[1]`, `Odometer[2]`

---

## 🧾 3.3 Classifying Total Channels (NoOfChannels)

In the **Tool Config** section:

1. Locate the field labeled `NoOfChannels`.
![15](https://github.com/user-attachments/assets/8e49e647-4c0d-4afd-850a-288284e8bdfa)



2. Input the total number of channels in this field.  
  Example: For 128 channels, enter:



---

## 🧾 3.4 Determining and Specifying Faulty Channels

In the **Faulty Channels** section:
1. If there are no faulty sensors, leave the fields for `HALL` and `EDDY` empty.

2. To specify faulty channels, use:
  - **Comma-separated values** for individual channels
  - **Hyphenated ranges** for sequences
  - Or a **combination of both**

### ✅ Examples:

- Faulty individual channels:


> This tells the system to use nearby healthy channels during processing.

---

## 🧾 3.5 Saving Configuration Changes

Once all changes are made:

1. Click the **SAVE** button at the bottom right of the screen to apply the changes.

2. If you want to revert to the original/default configuration, click the **SET DEFAULT** button.

---

✅ **Note:** Saving incorrect configuration settings can impact the data analysis. Always double-check values and faulty channel entries before confirming changes.


# 📘 Chapter 4: Auto Analysis

This chapter explains how to perform Auto Analysis in PipeCM after a run has been created and files have been uploaded. The Auto Analysis process consists of three major stages: Feature Extraction, Distance Calculation, and Metalloss Analysis.

---

## 🧪 4.1 Overview

Auto Analysis transforms raw pipeline sensor data into meaningful insights by applying sequential data processing and signal interpretation techniques. The screen displays real-time progress of each stage and provides run metadata for reference.

---

## 🔁 4.2 Auto Analysis Stages

### ✅ 4.2.1 Feature Extraction

- This is the **first step** in the analysis pipeline.
- It extracts characteristics from raw sensor data such as signal spikes, amplitude, waveform shapes, etc.
- The purpose is to convert raw binary input into interpretable signal features.
- Once complete, this section displays a **green checkmark** and status as **COMPLETED**.
 ![17](https://github.com/user-attachments/assets/05ba0df0-03b4-4959-bced-1063493eeecd)


---

### 📏 4.2.2 Distance Calculation

- Uses **odometer data** to assign physical distance values to extracted features.
- Calculates position in meters to map anomalies along the pipeline.
- This step must be started manually by clicking the **START** button.
- Progress is shown as a percentage (e.g., `0%`, `50%`, `100%`).
 ![Screenshot (78)](https://github.com/user-attachments/assets/0df105ba-ec4b-4b9c-805a-ca3fd5279812)


---

### ⚙️ 4.2.3 Metalloss Analysis

- Final step in the auto analysis process.
- Analyzes extracted features and calculated distances to detect **metal loss**, such as corrosion or thinning.
- Identifies potential defects and their severity using embedded algorithms.
- This also requires a manual **START**.
- Runs only after **Feature Extraction** and **Distance Calculation** are complete.
  ![Screenshot (80)](https://github.com/user-attachments/assets/bbabf363-4b15-4cd1-9bbc-e611354e5265)


---

## 📊 4.3 Auto Analysis Dashboard
The dashboard includes:

- A **circular progress indicator** displaying overall analysis status (e.g., `33%`)
- Real-time stage indicators for each process step
- A **Run Details panel** listing key run metadata:

| Property         | Value         |
|------------------|---------------|
| Run Source       | location1     |
| Run Destination  | location2     |
| Run Date         | 19/6/2025     |
| Tool Size        | 12            |
| Tool Type        | MFL_OCTA_GEN1 |

---

## 📌 4.4 After Auto Analysis

Once all stages are complete:

- Results can be viewed through the reporting modules.
- Further actions such as classification, visualization, or defect review may follow (covered in later chapters).





