# 📘 PipeCM – User Manual  
**Version:** 1.0  
**Organization:** Bhabha Atomic Research Centre (BARC)  

# 📚 PipeCM User Manual – Table of Contents

## 📘 Chapter 1: Getting Started – Registering and Logging into PipeCM
- [1.1 Log in to the System](#-11-log-in-to-the-system)
- [1.2 Create an Account](#-12-create-an-account)
- [1.3 PipeCM Analysis Dashboard](#-13-pipecm-analysis-dashboard)

## 📘 Chapter 2: Creating and Managing Runs
- [2.1 Create a Run](#-21-create-a-run)
  - [2.1.1 Select Tool](#-211-select-tool)
  - [2.1.2 Create Run Details](#-212-create-run-details)
  - [2.1.3 Uploading Binary Files](#-213-uploading-binary-files)
  - [2.1.4 Run Status & Processing](#-214-run-status--processing)
  - [2.1.5 Review Uploaded Files](#-215-review-uploaded-files)
  - [2.1.6 Status Change on Navigation](#-216-status-change-on-navigation)
  - [2.1.7 Edit Configurations](#-217-edit-configurations)
  - [2.1.8 Auto Analysis](#-218-auto-analysis)
  - [2.1.9 Manual Analysis](#-219-manual-analysis)
- [2.2 Select Run and Manage Runs](#-22-select-run-and-manage-runs)
  - [2.2.1 Select Existing Run](#-221-select-existing-run)
  - [2.2.2 Edit Configurations](#-222-edit-configurations)
  - [2.2.3 Auto Analysis](#-223-auto-analysis)
  - [2.2.4 Manual Analysis](#-224-manual-analysis)

## 📘 Chapter 3: Modifying Configurations
- [3.1 Accessing the Configuration Interface](#-31-accessing-the-configuration-interface)
- [3.2 Overview of Editable Configurations](#-32-overview-of-editable-configurations)
- [3.3 Classifying Total Channels (`NoOfChannels`)](#-33-classifying-total-channels-noofchannels)
- [3.4 Determining and Specifying Faulty Channels](#-34-determining-and-specifying-faulty-channels)
- [3.5 Saving Configuration Changes](#-35-saving-configuration-changes)

## 📘 Chapter 4: Auto Analysis
- [4.1 Overview](#-41-overview)
- [4.2 Auto Analysis Stages](#-42-auto-analysis-stages)
  - [4.2.1 Feature Extraction](#-421-feature-extraction)
  - [4.2.2 Distance Calculation](#-422-distance-calculation)
  - [4.2.3 Metalloss Analysis](#-423-metalloss-analysis)
- [4.3 Auto Analysis Dashboard](#-43-auto-analysis-dashboard)
- [4.4 After Auto Analysis](#-44-after-auto-analysis)

## 📘 Chapter 5: Manual Analysis
- [5.1 Interface Overview](#-51-interface-overview)
- [5.2 Pipetally Table (Left Pane)](#-52-pipetally-table-left-pane)
- [5.3 Filter Features](#-53-filter-features)
  - [5.3.1 Filter by Feature Type](#-531-filter-by-feature-type)
  - [5.3.2 Filter by Individual Columns](#-532-filter-by-individual-columns)
  - [5.3.3 Pagination and Row Control](#-533-pagination-and-row-control)
- [5.4 Feature Selection & Navigation](#-54-feature-selection--navigation)
- [5.5 Visual Feature Navigation & Tools](#-55-visual-feature-navigation--tools)
- [5.6 Visualization Modes](#-56-visualization-modes)
- [5.7 Scan Interaction Tools](#-57-scan-interaction-tools)
- [5.8 Lineplot Visualization (Circumferential Profile)](#-58-lineplot-visualization-circumferential-profile)
- [5.9 Understanding the Axes and Values](#-59-understanding-the-axes-and-values)
- [5.10 Changing the Color Scale](#-510-changing-the-color-scale)
- [5.11 PipeCM Manual Editing Feature](#-511-pipecm-manual-editing-feature)
  - [5.11.1 Editing a Feature](#-5111-editing-a-feature)
  - [5.11.2 Adding a Feature](#-5112-adding-a-feature)
  - [5.11.3 Deleting a Feature](#-5113-deleting-a-feature)
  - [5.11.4 Version Control](#-5114-version-control)
- [5.12 Manual Editing for METALLOSS Region](#-512-manual-editing-for-metalloss-region)

## 📘 Chapter 6: Generating Reports
- [6.1 Starting the Report Generation Process](#-61-starting-the-report-generation-process)

---


## 📘 Chapter 1: Getting Started – Logging and Registering on PipeCM

### 📌 Overview

**PipeCM** (Pipeline Corrosion Monitoring) is a powerful application designed to assess pipeline conditions and perform health diagnostics using tool and sensor data. This chapter walks you through the login process and registering a new account.

---

## 🔐 1.1 Log in to the System

Upon launching the application, the **Login Page** appears first.

📷 **Screenshot:** - Login page
![2](https://github.com/user-attachments/assets/716bb085-c46c-42da-b52c-38a477f21859)

### ➤ Login Steps:

1. **Enter Username** used during registration.  
2. **Enter Password**.  
3. Click the **"LOGIN"** button.

✅ If your credentials are correct, you will be redirected to the main dashboard.

---

## 🧾 1.2 Create an Account

If you're a new user, click **"Register Now!"** on the login screen to access the registration form.

📷 **Screenshot:**  - Register Page
![1.1](https://github.com/user-attachments/assets/97d0ea1a-f61c-4107-85f2-925660d1dd04)

### ➤ Step-by-Step Registration Process:

1. **Username**: Enter a unique username (e.g., `roshansahu`).  
2. **Email**: Provide a valid email address for notifications and password recovery.  
3. **Password Requirements**:
   - At least 1 uppercase letter  
   - At least 1 lowercase letter  
   - At least 1 number  
   - At least 1 special character (e.g., `@`, `#`, `!`)
4. **Re-enter Password**: Confirm your password by retyping it.

🛑 If any password rule is not met, an error message will appear below the field in red.

✅ Once all fields are valid, click the **"CREATE USER"** button.

---

## 💡 Tips & Navigation

- **New Here? Register Now!** – Click this on the login screen to create a new account.  
- **Already Registered? Login Now!** – Use this to return to the login page.


## 🧭 1.3 PipeCM Analysis Dashboard

📷 **Screenshot:**  
![3](https://github.com/user-attachments/assets/dbb8012a-2409-4d91-942f-9929a0aee055)

After successful login, users land on the main dashboard, which contains the following modules:

- **MFL + EC** – Oil/Gas pipeline inspection  
- **MFL + UT** – Oil pipeline inspection using ultrasonic and magnetic flux leakage data  
- **Health Assessment** – Analyzes tool and pipeline data  
- **Settings** – Customize software configurations

Each section includes a **"Start App"** button to launch its respective module.

---

# 📘 Chapter 2: Creating and Managing Runs

This chapter walks you through the complete process of creating a new pipeline run in PipeCM — including tool selection, run details, file uploads, confirmation, and managing existing runs.

---

## 🧾 2.1 Create a Run

### 🧾 2.1.1 Select Tool

The first step is to choose the appropriate inspection tool for the pipeline run.  
Click on **Start App** to begin.

📷 **Screenshots:**  
![Tool Selection 1](https://github.com/user-attachments/assets/330343d7-bbd7-4760-a174-41f7f7158830)  
![Tool Selection 2](https://github.com/user-attachments/assets/6cd7482b-918a-417c-97a7-149880f981a3)

**Steps:**

1. On the **Select Tool** screen, choose a tool by clicking the radio button in the **Select** column.
2. Before selecting the tool, click on the **plus (+)** button at the bottom right to add a run.
3. Tool details include:
   - **Tool Type:** e.g., `MFL_OCTA_GEN1`
   - **Tool Size:** e.g., `12 inch`
4. Click **NEXT** to proceed.

---

### 🧾 2.1.2 Create Run Details

Enter run-specific metadata such as source, destination, and date.

📷 **Screenshot:**  
![Run Details](https://github.com/user-attachments/assets/92c60686-0dd2-49c1-a728-37ba472e5abb)

**Fill the following fields:**

1. **Run Source:** e.g., `location1`  
2. **Run Destination:** e.g., `location2`  
3. **Run Date:** e.g., `19/06/2025`  
4. Click **ADD** to create the run entry.

---

### 🧾 2.1.3 Uploading Binary Files

#### 2.1.3.1 Browse and Select Files

1. Click on the desired run.
2. Click **Upload Data Files**.
3. Click **BROWSE FILES**.
4. Select files (e.g., `TMP0001_AK.bin`, `TMP0002_AK.bin`).

📷 **Screenshots:**  
![Browse Files 1](https://github.com/user-attachments/assets/b200fe67-155e-4887-b6ec-ef3d1ae393c6)  
![Browse Files 2](https://github.com/user-attachments/assets/31f8e5f3-f696-4157-bda1-aa3498ed0813)  
![Browse Files 3](https://github.com/user-attachments/assets/0a67e097-2ee5-411a-8f28-31885ade7be0)

#### 2.1.3.2 Upload the Files

1. Selected files appear with progress bars.
2. Click **UPLOAD** to start the transfer.

📷 **Screenshots:**  
![Upload Progress 1](https://github.com/user-attachments/assets/1a741dd3-a22a-4306-b3a6-e942f9a78ca9)  
![Upload Progress 2](https://github.com/user-attachments/assets/1d7b4a38-f49a-4756-91b2-27b00427535f)

#### 2.1.3.3 Save and Confirm

Once upload completes:

1. Click **SAVE**
2. A confirmation popup appears:

> *“Do you want to proceed with processing?”*  
> *“If confirmed, you cannot upload files anymore to this Run…”*

📷 **Screenshots:**  
![Confirm Popup 1](https://github.com/user-attachments/assets/0ffd966f-5440-47c4-953c-9347be1ab38a)  
![Confirm Popup 2](https://github.com/user-attachments/assets/312189d9-8cfe-4d0b-8d0e-3f2a18564a88)

3. Click **YES, I'M SURE** only when ready to finalize.

⚠️ **Note:** After confirmation, no more files can be added to this run.

---

### 🧾 2.1.4 Run Status & Processing

After saving, you're redirected to the **Select Run** screen.

📷 **Screenshot:**  
![Run Status](https://github.com/user-attachments/assets/02675c3f-efaf-458e-9041-bc2b399e3b57)

**Check the Status column:**

- Initially: `FILES_TO_BE_UPLOADED`
- Afterwards: `TO_BE_PROCESSED`,`INTERMEDIATE_TO_BE_GENERATED`

Click **NEXT** to continue.

---

### 🧾 2.1.5 Review Uploaded Files

On the **Select File** screen, view the uploaded `.bin` files.

📷 **Screenshot:**  
![Uploaded Files](https://github.com/user-attachments/assets/caa0c021-6cf5-4d70-b3e3-a9cc871efb50)

Each file displays:

- **File Name** `Name of file`
- **Sequence Number** `Represents order in which file is processed`
- **Status:** `TO_BE_PROCESSED`,`INTERMEDIATE_TO_BE_GENERATED`

---

### 🧾 2.1.6 Status Change on Navigation

If you return to the **Select Run** screen by clicking **BACK**, the status of the run changes:

- `FILES_TO_BE_UPLOADED`  → `TO_BE_PROCESSED` / `INTERMEDIATE_TO_BE_GENERATED`

📷 **Screenshot:**  
![Status Change](https://github.com/user-attachments/assets/db4efece-89f6-4bf0-a072-e835a9e9f0be)

Files are uploaded successfully and run is ready for processing.

---

### 🧾 2.1.7 Edit Configurations

To modify configurations for a selected run:

1. Go to the **Select Run** screen.
2. Locate the desired run.
3. Click the **settings (edit) icon** in the top-right corner.

You will be redirected to the **Configure** screen for that run.

🔗 [Link to Chapter 3: Modifying Configurations](#-chapter-3-modifying-configurations)

---

### 🧾 2.1.8 Auto Analysis

This section introduces auto-analysis steps after file upload.

🔗 [Link to Chapter 4: Auto Analysis](#-chapter-4-auto-analysis)

---

### 🧾 2.1.9 Manual Analysis

This section introduces Manual-analysis steps after file upload.

🔗 [Link to Chapter 5: Manual Analysis](#-chapter-5-manual-analysis)

---

## 🧾 2.2 Select Run and Manage Runs

### 🧾 2.2.1 Select Existing Run

To manage or analyze an existing run:

1. Click **Start App**
2. Select the desired tool
3. Proceed to the **Select Run** screen
4. Click **NEXT** on the **Select Tool** screen
5. Select a run by clicking the row
6. Choose one of the following:
   - Click **Settings icon** (top right) to edit configurations
   - Click Auto Analysis

📷 **Screenshots:**  
![Run Select 1](https://github.com/user-attachments/assets/330343d7-bbd7-4760-a174-41f7f7158830)  
![image](https://github.com/user-attachments/assets/cf351362-0510-4701-a7a6-578e8c343912)
![Run Select 2](https://github.com/user-attachments/assets/de49338d-2201-43ef-bafb-89affb60f060)

---

### 🧾 2.2.2 Edit Configurations

To change configurations for a selected run:

1. On the **Select Run** screen, click the **Settings icon** beside the run.

This redirects to the **Configure** screen.

🔗 [Link to Chapter 3: Modifying Configurations](#-chapter-3-modifying-configurations)

---

### 🧾 2.2.3 Auto Analysis

Once a run is selected and configured:

1. Click on Auto Analysis Button on bottom right.
2. Review file and analysis summaries.

🔗 [Link to Chapter 4: Auto Analysis](#-chapter-4-auto-analysis)

---

### 🧾 2.2.4 Manual Analysis

This section introduces Manual-analysis steps after file upload.

🔗 [Link to Chapter 5: Manual Analysis](#-chapter-5-manual-analysis)

---

# 📘 Chapter 3: Modifying Configurations

This chapter describes how to view and edit the configurations associated with a selected run in the PipeCM application.

![Run Select 1](https://github.com/user-attachments/assets/330343d7-bbd7-4760-a174-41f7f7158830)  
![image](https://github.com/user-attachments/assets/cf351362-0510-4701-a7a6-578e8c343912)

---

## 🧾 3.1 Accessing the Configuration Interface

To modify the configurations:

1. Go to the **Select Run** screen.
2. Locate the desired run from the table.
3. Click the **pencil icon (edit icon)** in the top-right corner.

📷 **Screenshot:**  
![Edit Config](https://github.com/user-attachments/assets/2fd33b04-db7c-4b98-9109-a96ed16169b4)

> This action will navigate you to the **Configure** screen for the selected run.

---

## 🧾 3.2 Overview of Editable Configurations

The **Configure** screen allows modification of parameters related to the run's data processing.

📷 **Screenshot:**  
![Configure Screen](https://github.com/user-attachments/assets/5264e5f9-0e00-4f2c-b539-82364eb7df7d)

### 🔧 Key Editable Sections:

- **Thresholds**
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

- **Tool Config**
  - `Word Size`
  - `Packet Size`
  - `NoOfChannels`

- **SensorCountMap**
  - `HALL`

- **Faulty Channels**
  - `HALL`
  - `EDDY`

- **Odometer Diameter**
  - `Odometer[0]`, `Odometer[1]`, `Odometer[2]`

---

## 🧾 3.3 Classifying Total Channels (`NoOfChannels`)

In the **Tool Config** section:

1. Locate the field labeled `NoOfChannels`.

📷 **Screenshot:**  
![NoOfChannels](https://github.com/user-attachments/assets/8e49e647-4c0d-4afd-850a-288284e8bdfa)

2. Input the total number of channels.  
   Example: If there are 128 channels, enter `128`.

---

## 🧾 3.4 Determining and Specifying Faulty Channels

In the **Faulty Channels** section:

1. If no faulty sensors are present, leave the `HALL` and `EDDY` fields empty.
2. To define faulty channels, use:
   - **Comma-separated values** (e.g., `5,12,30`)
   - **Hyphenated ranges** (e.g., `1-24`)
   - **Combination of both** (e.g., `1-24,34-45`)

📌 *"This setting informs the system to utilize neighboring healthy channels during data processing, using interpolated values for automatic analysis."*


---

## 🧾 3.5 Saving Configuration Changes

After making changes:

1. Click **SAVE** (bottom-right) to apply the changes.
2. To revert to system defaults, click **SET DEFAULT**.

✅ **Note:** Incorrect values may affect processing accuracy. Double-check all entries before saving.

---

# 📘 Chapter 4: Auto Analysis

This chapter explains how to perform Auto Analysis in PipeCM after a run has been created and files have been uploaded. The Auto Analysis process consists of three major stages:

1. **Feature Extraction**  
2. **Distance Calculation**  
3. **Metalloss Analysis**

![Run Select 1](https://github.com/user-attachments/assets/330343d7-bbd7-4760-a174-41f7f7158830)  
![image](https://github.com/user-attachments/assets/cf351362-0510-4701-a7a6-578e8c343912)
![image](https://github.com/user-attachments/assets/0acf313c-05bc-46c2-9889-bb00f08eac77)


---

## 🧪 4.1 Overview

Auto Analysis transforms raw pipeline sensor data into meaningful insights using sequential data processing and signal interpretation techniques.  
The screen displays real-time progress for each stage and provides run metadata for reference.

---

## 🔁 4.2 Auto Analysis Stages

### ✅ 4.2.1 Feature Extraction

- This is the **first step** in the analysis pipeline.
- Extracts characteristics from raw sensor data such as:
  - Signal spikes  
  - Amplitude  
  - Waveform shapes  
- Converts raw binary input into interpretable signal features.
- Once completed:
  - A **green checkmark** appears  
  - Status updates to **COMPLETED**

📷 **Screenshot:**  
![Feature Extraction](https://github.com/user-attachments/assets/05ba0df0-03b4-4959-bced-1063493eeecd)

---

### 📏 4.2.2 Distance Calculation

- Uses **odometer data** to assign physical distances to features.
- Maps anomalies along the pipeline in meters.
- This stage must be started manually by clicking the **START** button.
- Progress is displayed as a percentage (`0%`, `50%`, `100%`, etc.).

📷 **Screenshot:**  
![Distance Calculation](https://github.com/user-attachments/assets/0df105ba-ec4b-4b9c-805a-ca3fd5279812)

---

### ⚙️ 4.2.3 Metalloss Analysis

- Final stage in the Auto Analysis process.
- Analyzes features and distances to detect **metal loss** (e.g., corrosion, thinning).
- Identifies defect locations and severity using built-in algorithms.
- Requires manual initiation via the **START** button.
- Can be started only after both previous stages are marked **COMPLETED**.

📷 **Screenshot:**  
![Metalloss Analysis](https://github.com/user-attachments/assets/bbabf363-4b15-4cd1-9bbc-e611354e5265)

---

## 📊 4.3 Auto Analysis Dashboard

The dashboard includes:

- A **circular progress indicator** (e.g., `33%`, `100%`)
- Real-time indicators for each stage
- A **Run Details panel** with metadata:

| Property         | Value         |
|------------------|---------------|
| Run Source       | location1     |
| Run Destination  | location2     |
| Run Date         | 19/06/2025    |
| Tool Size        | 12            |
| Tool Type        | MFL_OCTA_GEN1 |

---

## 📌 4.4 After Auto Analysis

After all stages are completed:

- Results become available in reporting modules.
- You can proceed with:
  - **Defect classification**
  - **Data visualization**
  - **Defect review**

➡️ These are discussed in subsequent chapters.

---

# 📘 Chapter 5: Manual Analysis

This chapter explains the process of conducting **Manual Feature Analysis** using the PipeCM application. It includes how to interpret the left-hand pipeline data table, filter features, view scan images, and analyze defects.

---

## 🧾 5.1 Interface Overview

![image](https://github.com/user-attachments/assets/330343d7-bbd7-4760-a174-41f7f7158830)  
![image](https://github.com/user-attachments/assets/ec314af3-2cf8-49c5-8df9-aa82658095e9)  
![image](https://github.com/user-attachments/assets/d3e46462-8a1e-4e45-b5e4-43624f64f562)  
![image](https://github.com/user-attachments/assets/924ad21c-3e97-4c66-be88-ad03e5e25c11)

### ➤ Steps:

1. Click on **Start App**  
2. Select tool  
3. Click on **Next**  
4. Select the desired run  
5. Click on **Next**  
6. **Select** the desired file  
7. **Click on Submit**

📷 **Screenshot:**  
![Capture](https://github.com/user-attachments/assets/154f04a2-883b-4cff-ab4f-84c6142754c4)

> The Manual Analysis screen is split into two main sections:
- **Left Pane:** Pipetally table (fetched from database)  
- **Right Pane:** Visualization of pipeline scan with defects/pipe features

---

## 🧾 5.2 Pipetally Table (Left Pane)

The table on the left is auto-populated from PipeCM’s database and shows features detected in the pipeline.

### 🔹 Key Features of the Table:

- Organized by **Page Number (ascending)** with manual control
- Supports **filtering** and **sorting** on all columns
- Apply a filter and click the **Reload** button (🔄)
- New filters will be reflected in real-time

📷 **Screenshot:**  
![image](https://github.com/user-attachments/assets/abc6e666-ac84-43d0-bc07-baa539fb78d5)

### ➤ Guide:

- Click 🔳 for fullscreen  
- Click 🔄 for reload

### 📚 Column Breakdown:

| Column Name        | Description                                           |
|--------------------|-------------------------------------------------------|
| **Select**         | Choose a row for detailed inspection                  |
| **Page No**        | Page number in the pipeline scan                      |
| **Sample No**      | Sample number of feature                              |
| **Feature Type**   | Feature classification (e.g., METALLOSS, WELD)       |
| **Log Distance**   | Distance on pipeline log (in m)                       |
| **Absolute Sample**| Absolute sample                                    |
| **Wall Loss**      | % wall thickness loss                                 |
| **Length**         | Length of defect                                      |
| **Max Width**      | Maximum width of the defect                           |
| **Width / Depth**  | Actual size of defect                                 |
| **Gauss Peak**     | Magnetic peak value                                   |
| **Span**           | Width spread                                          |
| **Max Depth**      | Critical depth data                                   |
| **MAOP**           | Max allowable operating pressure impact              |
| **No. of Sensors** | Number of sensors that picked up metal loss          |

📷 **Screenshot (Table in Action):**  
![3](https://github.com/user-attachments/assets/40528029-6483-4413-8da0-f3d7723a7fce)

---

## 🧾 5.3 Filter Features

You can **filter by Feature Type** using the dropdown above the table.

### 🔘 5.3.1 Filter by Feature Type

### ✅ Available Feature Types:

- WELD  
- METALLOSS  
- FLANGE  
- VALVE  
- MARKER  
- SLEEVE_START / END  
- AREA_START / END  
- ATTACHMENT  
- TAP  
- CLAMP  
- SUPPORT_START / END  
- REDUCER_START / END  
- UNKNOWN  
- KICKER_LINE_CENTRE  
- LIMIT_VALVE  
- BARREL_ISOLATION_VALVE

📷 **Feature List Screenshot:**  
![image](https://github.com/user-attachments/assets/e0656463-3a6d-415e-aeac-a1e075b19db9)  
![Screenshot (19)](https://github.com/user-attachments/assets/7cecb17c-6c17-4a47-8e1a-6f2eb8d457c1)  
![Screenshot (20)](https://github.com/user-attachments/assets/e18966f2-928f-4130-be2b-d7d22086e6b9)  
![image](https://github.com/user-attachments/assets/4f583222-f2a8-4913-a36c-3f6e1383a0a1)
![7](https://github.com/user-attachments/assets/a1bca99a-8ce0-4de3-8343-a9f480853433)

#### 📝 Steps:

1. Click the **Select a feature** dropdown  
2. Choose one or more feature types  
3. Click **Reload (🔄)** to update the table

---

### 🔘 5.3.2 Filter by Individual Columns

| Filter Type              | Description                  |
|--------------------------|------------------------------|
| Equals                   | Match exact values           |
| Between                  | Range filtering              |
| Greater Than or Equal to | Filter values ≥ input        |
| Less Than or Equal to    | Filter values ≤ input        |

#### 📝 Steps:

1. Click the **filter icon** (🔽) next to any column  
2. Choose a filter condition  
3. Enter filter values  
4. Click **Refresh (🔄)**

## 📷 Column Filter UI  
![Screenshot (22)](https://github.com/user-attachments/assets/a3cdcac0-d4be-49de-9d5e-ee205622c284)

---

## 📷 Equals Filter  
- Select **Equal**, enter the desired value, and click on the **Reload** button.  
- This will display only the rows that exactly match the entered value.

![image](https://github.com/user-attachments/assets/446dd465-cb55-4813-bc29-9a1c13020a49)  
![image](https://github.com/user-attachments/assets/33e90ae9-3e52-4d66-8923-0ea99475f7bb)

---

## 📷 Between Filter  
- Select **Between**, enter the **Start** and **End** values, and click on the **Reload** button.  
- This will show only the rows where the value falls within the specified range.

![Screenshot (157)](https://github.com/user-attachments/assets/8b575d02-043e-467c-a7bf-6d5141b96543)  
![Screenshot (158)](https://github.com/user-attachments/assets/f8fdaef7-d3d7-41c7-b9b1-c16a293eeed0)

---

## 📷 Greater Than or Equal Filter  
- Select **Greater Than or Equal**, enter the desired value, and click on the **Reload** button.  
- This filters and displays all rows with values **greater than or equal to** the entered number.

![image](https://github.com/user-attachments/assets/19026f4b-bc41-446a-ad19-877733665b1e)  
![image](https://github.com/user-attachments/assets/1c4e09f5-69ba-4816-befa-d527fcd6de48)

---

## 📷 Less Than or Equal Filter  
- Select **Less Than or Equal**, input the value, and click on the **Reload** button.  
- This will filter and show rows with values **less than or equal to** the specified number.

![image](https://github.com/user-attachments/assets/28e2d867-d943-4407-98ee-5a04ef3b912a)  
![image](https://github.com/user-attachments/assets/87c27f38-c91c-47f9-a1ff-bec7f878cf60)

---

### 🔘 5.3.3 Pagination and Row Control

The table supports pagination for handling large datasets.

#### 📌 Features:

- Navigate pages:
  - ⏮ First
  - ⏪ Previous
  - ⏩ Next
  - ⏭ Last

- **Rows per page:** Choose from:
  - 10
  - 30
  - 50
  - 100

📷 **Pagination Controls:**  
![image](https://github.com/user-attachments/assets/4d8be492-bd10-4449-a41b-53c62c59c4b3)  
![image](https://github.com/user-attachments/assets/75974860-0f19-46e4-a7ac-bd5335db72d9)

---


## 🧾 5.4 Feature Selection & Navigation

The Manual Analysis module allows users to interact with the pipeline feature table for deeper inspection and analysis.

### 🖱️ 5.4.1 Double Click Navigation

You can **double-click** any row in the feature table to automatically navigate to the corresponding location in the pipeline scan.

📷 *Screenshot – Double Click to Navigate*  
![Screenshot (21)](https://github.com/user-attachments/assets/ba81fc4c-9019-45ce-9f6d-523502f83810)

#### 🎯 Feature Highlight and Detailed View

1. When a page is double-clicked, its navigation is shown on the right side.
2. When a row is **selected** (single-click or via radio button):
   - ✅ **Highlighted** in yellow on the pipeline scan.
   - 📄 **Detailed information** is displayed below the table or scan area.

#### 📋 Details Typically Include:

| Field            | Description                                           |
|------------------|-------------------------------------------------------|
| Feature Type     | Classification (e.g., WELD, METALLOSS)                |
| Sample Number    | Sample index of detection                             |
| Date             | Detection or data recording date                      |
| Status           | e.g., Confirmed, Flagged                              |
| Remark           | Notes or system-generated remarks                     |
| Log Distance     | Distance along pipeline (mm)                          |
| Absolute Sample  | Raw sensor sample                                     |
| Page Number      | Related page in scan data                             |

---

## 🧾 5.5 Visual Feature Navigation & Tools

The right-hand pane offers a visual interface to examine pipeline scans.

📷 *Screenshot – Feature View Panel*  
![a1](https://github.com/user-attachments/assets/1b5e4fd7-b13e-4dbb-90ff-5ae2f99b38c0)

### ➤ Key Components:

| Ref | Feature                  | Description                                                                 |
|-----|--------------------------|-----------------------------------------------------------------------------|
| 1   | Scan Name                | Identifies the current pipeline scan section                                |
| 2   | Feature Type Selector    | Switch between detected feature types                                       |
| 3   | Page Navigation Dropdown | Jump to a specific page from dropdown                                       |
| 4   | Goto Page Input          | Type page number and press Enter                                            |
| 5   | Next Page Button         | Go to the next scan page                                                    |
| 6   | Previous Page Button     | Return to previous page                                                     |
| 7   | View Mode Selector       | Choose: PIPELINE-SCAN, LINE PLOT, DENOISED                        |

---

## 🧾 5.6 Visualization Modes

### 🎯 Available Modes:

| Mode Name               | Description                                   |
|------------------------|------------------------------------------------|
| PIPELINE-SCAN          | Raw scan of pipeline                           |
| LINE PLOT              | Sensor signal graphs                           |
| DENOISED PIPELINE-SCAN | Filtered scan                                  |
| DENOISED LINE PLOT     | Noise-reduced signal graphs for better insights|

### 📝 Steps:

1. Right-click on 3 dots
2. Select desired mode  

📷 **Screenshots**:

- **PIPELINE-SCAN**
> Displays the raw pipeline scan image with visible signal traces and feature positions.
![b](https://github.com/user-attachments/assets/d3642591-01f9-41c1-809f-8a00fa689c53)

- **LINE PLOT**
> Shows the raw amplitude waveform across the pipeline length, highlighting signal anomalies.
![c](https://github.com/user-attachments/assets/d88995ea-ce80-437d-a045-5fe04e86ac31)

- **DENOISED PIPELINE-SCAN**
> Provides a cleaner version of the pipeline scan with noise reduction for better visual analysis.
![a](https://github.com/user-attachments/assets/5361f10d-2f4e-41d5-bb80-1c7bd23098c3)

- **DENOISED LINE PLOT**
> Presents the filtered line plot with minimized signal noise, helping isolate critical features.
![d](https://github.com/user-attachments/assets/d6466620-2857-4b7b-be56-4899c6e35f1c)

---

## 🧾 5.7 Scan Interaction Tools

Located at the top-right of the scan viewer.

📷 *Screenshot – Toolbar*  
![a3](https://github.com/user-attachments/assets/f2d23016-148b-49f1-98a7-bda10d62f684)

### 🧰 Toolbar Features:

| Ref | Tool         | Description                                               |
|-----|--------------|-----------------------------------------------------------|
| 1   | 🔍 Zoom Tool | Click + drag to zoom into a region                         |
| 2   | ➕ Zoom In   | Step zoom-in                                               |
| 3   | ➖ Zoom Out  | Step zoom-out                                              |
| 4   | 🔄 Reset View| Resets zoom and pan                                        |
| 5   | 🔲 Box Select| Draw box to zoom/select                                    |

---

## 🧾 5.8 Lineplot Visualization (Circumferential Profile)

Shows how defects spread around the pipe’s circumference using bar charts.

### 📝 Steps:

1. Click **Box Select**
2. Drag a region
3. Right-click → **Show Circumferential Profile**
4. Bar chart appears
5. To close: right-click → **Hide Circumferential Profile**

📷 **Screenshots**  

>select the box select option
![a7](https://github.com/user-attachments/assets/d9da373b-98e9-4cb1-a9e9-21938d8cc8fb)  
![a8](https://github.com/user-attachments/assets/d60242f0-98da-48f2-a3cd-2e0888cd392b)  
![a9](https://github.com/user-attachments/assets/aaa82c81-ca20-4cff-89e2-9ca03eb01d44)
![a10](https://github.com/user-attachments/assets/64e2fe2c-e7f4-486c-9740-dad9d6658eb6)
![a11](https://github.com/user-attachments/assets/629846da-5aa9-4abb-bd59-c5c9d03eaa6d)

---

## 🧾 5.9 Understanding the Axes and Values

| Axis / Value | Meaning                                           |
|--------------|--------------------------------------------------|
| X-Axis       | Sample Number                                    |
| Y-Axis       | Sensor Index (starts from 0)                     |
| Z-Axis       | Magnetic Field Intensity (Gauss level)           |

📷 *Screenshot*  
![a12](https://github.com/user-attachments/assets/f28c14a9-4a1c-4e11-bca3-8f96048a6670)

---

## 🧾 5.10 Changing the Color Scale

### 🪄 Steps:

1. Right-click on scan area  
2. Hover on **Color Scales**
3. Choose one of:

- Blues
- Reds
- Greys
- Jet
- Hot
- Cool
- Viridis
- Spring
- Oranges

📷 *Screenshot*  
![a13](https://github.com/user-attachments/assets/0875879f-d78a-45fb-a6a8-7b0446a0e075)

---

## 📝 5.11 PipeCM Manual Editing Feature

### 🔍 Selecting a Region

To select a region on the pipeline scan:
- Click anywhere inside the scan image (gray area with vertical patterns).
- A **yellow marker (bounding box)** will appear, highlighting the selected feature (e.g., **WELD**, **METALLOSS**).

📷 *Screenshot* - selecting a region  
![Screenshot (132)](https://github.com/user-attachments/assets/7336aa69-a7d7-4296-80d7-edc76e8ff17e)

---

### ✏️ 5.11.1 Editing a Feature

#### Method 1: Right-Click

- **Right-click** on the yellow-highlighted region in the scan view.
- A **context menu** appears with the following options:
  - **Edit Feature**: Opens the feature’s editable form.
  - **Delete Feature**
  - **Add Feature**
  - **Navigation options** (Previous Page, Next Page)
  - **View tools** (Hide Shape, Show Circumferential Profile, Color Scales)

📷 *Screenshot* -Right click for selecting edit feature 
![Screenshot (133)](https://github.com/user-attachments/assets/0474d241-9ac0-46b3-a6a4-fbe2d0b2f20d)

---

#### Method 2: Pencil Icon in Detail Panel

- Click the pencil icon ✎ in the **feature detail panel** at the bottom right corner of the screen.
- This opens an **editing dialog**, where you can:
  - Modify fields like `Sample`, `Log Distance`, `Feature Type`, etc.
  - Add or update a **Remark**.
  - Set the **Status** (e.g., `test1`).
  - A **new version** of the feature is created and stored in the version history.

📷 *Screenshot* -Pencil icon in bottom right panel 
![Screenshot (135)](https://github.com/user-attachments/assets/7c089bd3-a642-4c77-a962-8dac76db9c66)  
![Screenshot (134)](https://github.com/user-attachments/assets/fcb87674-84b7-4965-ace8-49b792c85582)

---

### ➕ 5.11.2 Adding a Feature

From the **right-click menu** → `Add Feature`, you can insert:
- `WELD`, `METALLOSS`, `FLANGE`, `VALVE`, `MARKER`, etc.
Configure its parameters and **save**.

📷 *Screenshot* -Adding a feature
![Screenshot (156)](https://github.com/user-attachments/assets/7c7db278-feb7-4017-b416-b1e4af38bfc8)

---

### ❌ 5.11.3 Deleting a Feature

- Right-click → **Delete Feature**
- Status is set to `MANUALLY_DELETED`

📷 *Screenshot* -deleting a feature  
![Screenshot (142)](https://github.com/user-attachments/assets/2bb12dbc-47d1-4c98-9711-90cb6fba2a0b)  
![Screenshot (143)](https://github.com/user-attachments/assets/d78a28a4-3336-406b-b5e2-19288ea71f99)

---

### 🗂️ 5.11.4 Version Control

- Feature edits are tracked with **versions**
- Feature versioning tracked: e.g., `WELD | v1`, `v2`  
- Accessible from the version dropdown

📷 *Screenshot* -Version control
![Screenshot (145)](https://github.com/user-attachments/assets/6b801db9-ed2f-41c1-a764-08e448c4dcd3)

---

## 🗃️ Data Fields Available

Each feature may include the following fields:

- **Feature Type** (e.g., WELD, METALLOSS)
- **Sample Number**
- **Log Distance**
- **Absolute Sample**
- **Date**
- **Status**
- **Remarks**
- **Page No.**

---

## 📝 5.12 Manual Editing for METALLOSS Region 

### 🔸 Selecting a METALLOSS Region

1. Click on the pipeline scan to select a **METALLOSS** region.
- The selected region is highlighted in **yellow**, indicating it's active for editing.

📷 *Screenshot* -Selecting metalloss region 
![Screenshot (136)](https://github.com/user-attachments/assets/9b47d1a0-af0e-4104-a55f-afaf2ce09772)

---

### ✏️ 5.12.1 Editing METALLOSS

#### 🔹 Right-Click Method

Right-click → **Edit Feature**

📷 *Screenshot* -Right click to select edit feature  
![Screenshot (137)](https://github.com/user-attachments/assets/621e1228-a628-4a9b-bb71-d6c093c2c887)

---

#### 🔹 Bottom Dialog Method

1. Select the METALLOSS region (yellow box).
2. In the **bottom dialog**, click the **“Edit”** button.
3. A form opens with **all parameters pre-calculated and prefilled**, including:
  - Log Distance
  - Depth
  - Length
  - Width
  - Orientation
  - Clock Position
  - Absolute Sample
  - Date
  - Status
  - Max Length
  - Page Number
  - Gauss Value
  - Center Sensor
  - Max Span
  - span
  - Feature Type
  - Number of Sensors
  - Sample

📷 *Screenshot* -Click edit button on bottom right Dialog box
![Screenshot (137)](https://github.com/user-attachments/assets/aaf6a5a1-2b07-43ed-9aa0-8551da4fbe98)  
![Screenshot (139)](https://github.com/user-attachments/assets/f8b90bc5-2c6c-4241-8fc3-8cd0cb20d6ce)  
![Screenshot (140)](https://github.com/user-attachments/assets/f59875ca-7f71-4f44-97af-b02831d52b2a)

---

### ➕ 5.12.2 Add/Delete METALLOSS

#### ✅ Add:

Right-click → **Add METALLOSS**, enter values, Save

📷 *Screenshot* -Add feature 
![Screenshot (141)](https://github.com/user-attachments/assets/b0851a5c-f013-4040-b88f-d00a171fc8ef)

#### 🗑️ Delete:

Right-click → **Delete METALLOSS**

Status: `MANUALLY_DELETED`

---



# 📘 Chapter 6: Generating Reports

This chapter explains how to generate and export inspection reports using the PipeCM application after completing Auto  analysis.

---

## 🧾 6.1 Starting the Report Generation Process

Before generating a report, ensure you have completed all necessary manual analysis and saved any changes.

### 📝 Steps to Generate a Report:

![image](https://github.com/user-attachments/assets/5af52374-ebd9-4901-9b99-88cc9800b5fd)
![image](https://github.com/user-attachments/assets/b77ec6d7-a6b4-4e4b-9e08-fd811af53dd7)
![image](https://github.com/user-attachments/assets/fa5caf95-6af4-436c-9c6e-fc2a63b9746e)
![image](https://github.com/user-attachments/assets/4db7096d-0e47-45dd-a65e-b284252ca61b)
![Screenshot (162)](https://github.com/user-attachments/assets/cb0251bf-511f-4847-884f-795d1059109e)
![Screenshot (165)](https://github.com/user-attachments/assets/8519aa93-3f4e-4f65-b60f-e9aa60d96c76)
![Screenshot (183)](https://github.com/user-attachments/assets/7a5ab5fa-4e3a-45e5-b258-43c3707b20ad)

![Screenshot (166)](https://github.com/user-attachments/assets/d8fa4cb0-dbeb-438c-89ca-347ef463741c)
![Screenshot (167)](https://github.com/user-attachments/assets/6aa3f080-bbb9-45c0-a106-6a62007f3aef)

![Screenshot (184)](https://github.com/user-attachments/assets/e3f9a231-b0cf-49b5-831e-bf8fa75edcd8)
![Screenshot (185)](https://github.com/user-attachments/assets/31723ba6-9892-4127-9a0e-7a6f844c87f2)
![Screenshot (186)](https://github.com/user-attachments/assets/a99487b5-f5de-4d51-9b00-b5a5f0565c1a)




1. Click on **Home**
2. Click on **Start App**
3. Select the desired tool and click on **Next**
4. Select the desired run and click on **Download Report** for the CSV file  
5. Otherwise, click on **Download PDF Report** for the PDF file




---

