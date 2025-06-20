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

**Version:** 1.0  
**Organization:** Bhabha Atomic Research Centre (BARC)  

This chapter walks you through the complete process of creating a new pipeline run in PipeCM — including tool selection, run details, file uploads, and confirmation, and then managing existing runs.

---

## 🧾 2.1 Create a Run

### 🧾 2.1.1 Select Tool

The first step is to choose the appropriate inspection tool for the pipeline run.

**Screenshot:** *(Insert relevant screenshot)*

**Steps:**

- From the **Select Tool** screen, choose a tool by clicking the radio button in the **Select** column.
- **Before Selecting Tool Click on Plus Button in Bottom Right to Add A Run**
- **Tool details include:**
  - **Tool Type:** e.g., `MFL_OCTA_GEN1`
  - **Tool Size:** e.g., `12 inch`
- Click **NEXT** to proceed.

### 🧾 2.1.2 Create Run Details

Enter run-specific metadata such as source, destination, and date.

**Screenshot:** *(Insert relevant screenshot)*

**Fill the following fields:**

- **Run Source:** e.g., `location1`
- **Run Destination:** e.g., `location2`
- **Run Date:** e.g., `19/06/2025`

Click **ADD** to create the run entry.

### 🧾 2.1.3 Uploading Binary Files

After the run is created, upload sensor data files.

#### 2.1.3.1 Browse and Select Files

- Click **BROWSE FILES**
- Select files from your system (e.g., `TMP0001_AK.bin`, `TMP0002_AK.bin`)

**Screenshot:** *(Insert relevant screenshot)*

#### 2.1.3.2 Upload the Files

- Selected files will show with progress bars.
- Click **UPLOAD** to start the transfer.

**Screenshot:** *(Insert relevant screenshot)*

#### 2.1.3.3 Save and Confirm

Once upload completes:

- Click **SAVE**
- A confirmation popup appears:

> *“Do you want to proceed with processing?”*  
> *“If confirmed, you cannot upload files anymore to this Run…”*

**Screenshot:** *(Insert relevant screenshot)*

- Click **YES, I'M SURE** only when ready to finalize.

⚠️ **Note:** After confirmation, no more files can be added to this run.

### 🧾 2.1.4 Run Status & Processing

After saving, you’re redirected to the **Select Run** screen.

📷 **Screenshot:**
![11](https://github.com/user-attachments/assets/02675c3f-efaf-458e-9041-bc2b399e3b57)


**Check the Status column:**
- Initially: `FILES_TO_BE_UPLOADED`
- After confirmation: `TO_BE_PROCESSED`

Click **NEXT** to continue.

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

- `FILES_TO_BE_UPLOADED` → `TO_BE_PROCESSED`

📷 **Screenshot:**
![13](https://github.com/user-attachments/assets/db4efece-89f6-4bf0-a072-e835a9e9f0be)


This means the system has queued your files for processing.
### 🧾 2.1.7 Edit Configurations

To modify the configurations associated with a selected run:

- Go to the **Select Run** screen.
- Locate the desired run from the table.
- In the top right corner of the table, click the **pencil icon (edit icon)**.

**Screenshot:** *(Insert 16.PNG here)*

This action will navigate you to the **Configure** screen for the selected run, where you can modify parameters related to the run's data processing.

[Link to Chapter 3: Modifying Configurations](#-chapter-3-modifying-configurations)

---

## 🧾 2.1.8 Auto Analysis

This section will cover the steps for initiating and reviewing auto-analysis of the run data.

[Link to Chapter 4: Auto Analysis](#-chapter-4-auto-analysis)


---

---

## 🧾 2.2 Select Run and Manage Runs



### 2.2.2 Edit Configurations

To modify the configurations associated with a selected run:

- Go to the **Select Run** screen.
- Locate the desired run from the table.
- In the top right corner of the table, click the **pencil icon (edit icon)**.

**Screenshot:** *(Insert 16.PNG here)*

This action will navigate you to the **Configure** screen for the selected run, where you can modify parameters related to the run's data processing.

[Link to Chapter 3: Modifying Configurations](https://www.google.com/search?q=%23chapter-4-modifying-configurations)

---

### 2.2.3 Auto Analysis

This section will cover the steps for initiating and reviewing auto-analysis of the run data.

[Link to Chapter 4: Auto Analysis](https://www.google.com/search?q=%23chapter-4-auto-analysis)


# 📘 Chapter 3: Modifying Configurations

**Version:** 1.0  
**Organization:** Bhabha Atomic Research Centre (BARC)

This chapter describes how to view and edit the configurations associated with a selected run in the PipeCM application.

---

## 🧾 3.1 Accessing the Configuration Interface

To modify the configurations:

- Go to the **Select Run** screen.
- Locate the desired run from the table.
- In the top right corner of the table, click the **pencil icon (edit icon)**.

📷 **Screenshot:** _Insert 16.PNG_

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

- Locate the field labeled `NoOfChannels`.
![15](https://github.com/user-attachments/assets/8e49e647-4c0d-4afd-850a-288284e8bdfa)



- Input the total number of channels in this field.  
  Example: For 128 channels, enter:



---

## 🧾 3.4 Determining and Specifying Faulty Channels

In the **Faulty Channels** section:
- If there are no faulty sensors, leave the fields for `HALL` and `EDDY` empty.

- To specify faulty channels, use:
  - **Comma-separated values** for individual channels
  - **Hyphenated ranges** for sequences
  - Or a **combination of both**

### ✅ Examples:

- Faulty individual channels:


> This tells the system to ignore channels 1 through 24 and 34 through 45 during processing.

---

## 🧾 3.5 Saving Configuration Changes

Once all changes are made:

- Click the **SAVE** button at the bottom right of the screen to apply the changes.

- If you want to revert to the original/default configuration, click the **SET DEFAULT** button.

---

✅ **Note:** Saving incorrect configuration settings can impact the data analysis. Always double-check values and faulty channel entries before confirming changes.




