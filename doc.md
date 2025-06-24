# 📘 PipeCM – User Manual  
**Version:** 1.0  
**Organization:** Bhabha Atomic Research Centre (BARC)  

---

# Table of Content  
## 📌 **Chapter 1: Getting Started**  
- [1.1 Create an Account](#-11-create-an-account)  
- [1.2 Login to the System](#-12-login-to-the-system)  
- [1.3 PipeCM Analysis Dashboard](#-13-pipecm-analysis-dashboard)  

## 📌 **Chapter 2: Creating and Managing Runs**  
- [2.1 Create a Run](#-21-create-a-run)  
  - [2.1.1 Select Tool](#-211-select-tool)  
  - [2.1.2 Create Run Details](#-212-create-run-details)  
  - [2.1.3 Uploading Binary Files](#-213-uploading-binary-files)  
    - [2.1.3.1 Browse and Select Files](#-2131-browse-and-select-files)  
    - [2.1.3.2 Upload the Files](#-2132-upload-the-files)  
    - [2.1.3.3 Save and Confirm](#-2133-save-and-confirm)  
  - [2.1.4 Run Status & Processing](#-214-run-status--processing)  
  - [2.1.5 Review Uploaded Files](#-215-review-uploaded-files)  
  - [2.1.6 Status Change on Navigation](#-216-status-change-on-navigation)  
  - [2.1.7 Edit Configurations](#-217-edit-configurations)  
  - [2.1.8 Auto Analysis](#-218-auto-analysis)  
- [2.2 Select Run and Manage Runs](#-22-select-run-and-manage-runs)  
  - [2.2.1 Select Existing Run](#-221-select-existing-run)  
  - [2.2.2 Edit Configurations](#-222-edit-configurations)  
  - [2.2.3 Auto Analysis](#-223-auto-analysis)  

## 📌 **Chapter 3: Modifying Configurations**  
- [3.1 Accessing the Configuration Interface](#-31-accessing-the-configuration-interface)  
- [3.2 Overview of Editable Configurations](#-32-overview-of-editable-configurations)  
- [3.3 Classifying Total Channels (`NoOfChannels`)](#-33-classifying-total-channels-noofchannels)  
- [3.4 Determining and Specifying Faulty Channels](#-34-determining-and-specifying-faulty-channels)  
- [3.5 Saving Configuration Changes](#-35-saving-configuration-changes)  

## 📌 **Chapter 4: Auto Analysis**  
- [4.1 Overview](#-41-overview)  
- [4.2 Auto Analysis Stages](#-42-auto-analysis-stages)  
  - [4.2.1 Feature Extraction](#-421-feature-extraction)  
  - [4.2.2 Distance Calculation](#-422-distance-calculation)  
  - [4.2.3 Metalloss Analysis](#-423-metalloss-analysis)  
- [4.3 Auto Analysis Dashboard](#-43-auto-analysis-dashboard)  
- [4.4 After Auto Analysis](#-44-after-auto-analysis)  

## 📌 **Chapter 5: Manual Analysis**  
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
- [5.11 Manual Editing Feature](#-511-manual-editing-feature)  
  - [5.11.1 Editing a Feature](#-5111-editing-a-feature)  
  - [5.11.2 Adding a Feature](#-5112-adding-a-feature)  
  - [5.11.3 Deleting a Feature](#-5113-deleting-a-feature)  
  - [5.11.4 Version Control](#-5114-version-control)  
- [5.12 Manual Editing for METALLOSS Region](#-512-manual-editing-for-metalloss-region)  

## 📌 **Chapter 6: Generating Reports**  
- [6.1 Starting the Report Generation Process](#-61-starting-the-report-generation-process)  


---


## 📘 Chapter 1: Getting Started – Registering and Logging into PipeCM

### 📌 Overview

**PipeCM** (Pipeline Corrosion Monitoring) is a robust application designed to evaluate pipeline conditions and perform health assessments using tool and sensor data. This chapter guides users through the process of account creation and login, ensuring secure access to all features.

---

## 🧾 1.1 Create an Account

To access the features of PipeCM, you must first create a user account.

### ➤ Step-by-Step Registration Process:

📷 **Screenshot:**  
![1.1](https://github.com/user-attachments/assets/97d0ea1a-f61c-4107-85f2-925660d1dd04)

1. **Username**: Enter a unique username (e.g., `roshansahu`).
2. **Email**: Provide a valid email address for notifications and recovery.
3. **Password Requirements**:
   - At least 1 uppercase letter  
   - At least 1 lowercase letter  
   - At least 1 number  
   - At least 1 special character (e.g., `@`, `#`, `!`)
4. **Re-enter Password**: Confirm your password by retyping it.

🛑 If any password requirement is not met, an error message will appear in red below the input field.

✅ Once all fields are correctly filled, click the **"CREATE USER"** button.

---

## 🔐 1.2 Log in to the System

After registration, return to the login screen to access the application.

📷 **Screenshot:**  
![2](https://github.com/user-attachments/assets/716bb085-c46c-42da-b52c-38a477f21859)

### ➤ Login Steps:

1. **Enter Username** used during registration.  
2. **Enter Password**.  
3. Click the **"LOGIN"** button.

✅ If your credentials are valid, you will be redirected to the main dashboard.

---

## 💡 Additional Options

- **Already Registered? Login Now!** – Click this if you already have an account.  
- **New Here? Register Now!** – Click here to access the registration form if you're a new user.

---

## 🧭 1.3 PipeCM Analysis Dashboard

📷 **Screenshot:**  
![3](https://github.com/user-attachments/assets/dbb8012a-2409-4d91-942f-9929a0aee055)

After successful login, users land on the main dashboard, which contains the following modules:

- **MFL + EC** – Gas pipeline inspection  
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

- Initially: `FILES_TO_BE_UPLOADED`, `INTERMEDIATE_TO_BE_GENERATED`
- Afterwards: `TO_BE_PROCESSED`

Click **NEXT** to continue.

---

### 🧾 2.1.5 Review Uploaded Files

On the **Select File** screen, view the uploaded `.bin` files.

📷 **Screenshot:**  
![Uploaded Files](https://github.com/user-attachments/assets/caa0c021-6cf5-4d70-b3e3-a9cc871efb50)

Each file displays:

- **File Name**
- **Sequence Number**
- **Status:** `TO_BE_PROCESSED`

---

### 🧾 2.1.6 Status Change on Navigation

If you return to the **Select Run** screen by clicking **BACK**, the status of the run changes:

- `FILES_TO_BE_UPLOADED` / `INTERMEDIATE_TO_BE_GENERATED` → `TO_BE_PROCESSED`

📷 **Screenshot:**  
![Status Change](https://github.com/user-attachments/assets/db4efece-89f6-4bf0-a072-e835a9e9f0be)

This means the system has queued your files for processing.

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

1. Click **NEXT** on the **Select Run** screen.
2. Review file and analysis summaries.

🔗 [Link to Chapter 4: Auto Analysis](#-chapter-4-auto-analysis)

---

# 📘 Chapter 3: Modifying Configurations

This chapter describes how to view and edit the configurations associated with a selected run in the PipeCM application.

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

📌 This informs the system to use neighboring healthy channels during data processing.

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

This chapter explains how to conduct **Manual Feature Analysis** using the PipeCM application. It covers interpretation of the pipeline data table, feature filtering, scan image viewing, and defect inspection.

---

## 🧾 5.1 Interface Overview

The Manual Analysis screen includes:

- **Left Pane:** Pipetally Table (features from database)
- **Right Pane:** Pipeline scan visualization with defect markers

📷 Screenshots:  
![image1](https://github.com/user-attachments/assets/330343d7-bbd7-4760-a174-41f7f7158830)  
![image2](https://github.com/user-attachments/assets/ec314af3-2cf8-49c5-8df9-aa82658095e9)  
![image3](https://github.com/user-attachments/assets/d3e46462-8a1e-4e45-b5e4-43624f64f562)  
![image4](https://github.com/user-attachments/assets/924ad21c-3e97-4c66-be88-ad03e5e25c11)

### ➤ Steps to Launch:

1. Start App → Select Tool → Click Next  
2. Select Run → Click Next  
3. Choose File → Click Submit  

📷 Screenshot:  
![start](https://github.com/user-attachments/assets/154f04a2-883b-4cff-ab4f-84c6142754c4)

---

## 🧾 5.2 Pipetally Table (Left Pane)

The table shows auto-fetched features per page and supports full filtering and selection.

### 📚 Column Breakdown

| Column Name       | Description                           |
|-------------------|---------------------------------------|
| Select            | Row selector for detailed view        |
| Page No           | Page index of scan                    |
| Sample No         | Feature's sample ID                   |
| Feature Type      | e.g., METALLOSS, VALVE, etc.          |
| Log Distance      | Distance on pipeline log (m)          |
| Absolute Sample   | Raw data sample position              |
| Wall Loss         | % thickness loss                      |
| Length            | Defect length                         |
| Max Width         | Maximum width                         |
| Width / Depth     | Feature size ratio                    |
| Gauss Peak        | Peak magnetic value                   |
| Span              | Spread of defect                      |
| Max Depth         | Deepest point                         |
| MAOP              | Max Operating Pressure impact         |
| No. of Sensors    | No. of detecting sensors              |

📷 Screenshot:  
![table](https://github.com/user-attachments/assets/40528029-6483-4413-8da0-f3d7723a7fce)

---

## 🧾 5.3 Feature Filtering

### 🔘 5.3.1 Filter by Feature Type

- Use the dropdown above the table  
- Select one or more types (e.g., WELD, METALLOSS)  
- Click **Reload** to update

📷 Screenshots:  
![filter1](https://github.com/user-attachments/assets/e0656463-3a6d-415e-aeac-a1e075b19db9)  
![filter2](https://github.com/user-attachments/assets/7cecb17c-6c17-4a47-8e1a-6f2eb8d457c1)

---

### 🔘 5.3.2 Filter by Columns

Supports: `Equals`, `Between`, `>=`, `<=`

📷 Screenshots:  
![equals](https://github.com/user-attachments/assets/446dd465-cb55-4813-bc29-9a1c13020a49)  
![between](https://github.com/user-attachments/assets/8b575d02-043e-467c-a7bf-6d5141b96543)  
![gte](https://github.com/user-attachments/assets/19026f4b-bc41-446a-ad19-877733665b1e)  
![lte](https://github.com/user-attachments/assets/28e2d867-d943-4407-98ee-5a04ef3b912a)

---

### 🔘 5.3.3 Pagination & Row Control

- Use ⏮ ⏪ ⏩ ⏭ buttons  
- Choose rows per page: 10 / 30 / 50 / 100  

📷 Screenshots:  
![pagination](https://github.com/user-attachments/assets/4d8be492-bd10-4449-a41b-53c62c59c4b3)

---

## 🧾 5.4 Feature Navigation

### 🖱️ 5.4.1 Double-Click Navigation

- Double-click a row → auto-navigates to that page  
- Right pane highlights selected feature (yellow box)

📷 Screenshot:  
![navigate](https://github.com/user-attachments/assets/ba81fc4c-9019-45ce-9f6d-523502f83810)

---

### 📝 Detail Panel Info

| Field            | Description                            |
|------------------|----------------------------------------|
| Feature Type     | METALLOSS, WELD, etc.                  |
| Sample Number    | Index of detection                     |
| Date             | Timestamp                              |
| Status           | Flagged/Confirmed                      |
| Remark           | User/system note                       |
| Log Distance     | Distance in mm                         |
| Page Number      | Page ID                                |

---

## 🧾 5.5 Visual Feature Panel (Right Pane)

### ➤ Key Tools

| Tool Ref | Feature              | Description                                     |
|----------|----------------------|-------------------------------------------------|
| 1        | Scan Name            | Name of scan                                    |
| 2        | Feature Selector     | Filter by feature (WELD, METALLOSS, etc.)       |
| 3        | Page Dropdown        | Jump to specific scan page                      |
| 4        | Go To Page           | Enter page manually                             |
| 5/6      | Next/Prev Buttons    | Page navigation                                 |
| 7        | View Mode Selector   | PIPELINE-SCAN, LINE PLOT, etc.                  |

---

## 🧾 5.6 Visualization Modes

| Mode                   | Description                                               |
|------------------------|-----------------------------------------------------------|
| PIPELINE-SCAN          | Raw image of full scan                                    |
| LINE PLOT              | Sensor signal line chart                                  |
| DENOISED PIPELINE-SCAN | Clean scan for better visibility                          |
| DENOISED LINE PLOT     | Filtered signals for clearer inspection                   |

📷 Screenshots:  
![pipe-scan](https://github.com/user-attachments/assets/d3642591-01f9-41c1-809f-8a00fa689c53)  
![lineplot](https://github.com/user-attachments/assets/d88995ea-ce80-437d-a045-5fe04e86ac31)

---

## 🧾 5.7 Scan Toolbar Tools

| Tool     | Function                    |
|----------|-----------------------------|
| 🔍 Zoom  | Click & drag to zoom         |
| ➕/➖     | Zoom in/out                   |
| 🔄 Reset | Reset zoom/view              |
| 🔲 Box   | Define area to inspect       |

📷 Screenshot:  
![toolbar](https://github.com/user-attachments/assets/f2d23016-148b-49f1-98a7-bda10d62f684)

---

## 🧾 5.8 Circumferential Profile

Visual bar chart around pipe’s circumference for selected feature.

### 📝 Steps:

1. Box select region  
2. Right-click → **Show Circumferential Profile**  
3. Right-click again → **Hide** if needed

📷 Screenshots:  
![circ-1](https://github.com/user-attachments/assets/64e2fe2c-e7f4-486c-9740-dad9d6658eb6)

---

## 🧾 5.9 Axes Explanation

| Axis | Meaning                              |
|------|--------------------------------------|
| X    | Sample Number                        |
| Y    | Sensor Number (positioned around pipe) |
| Z    | Gauss reading (intensity)            |

📷 Screenshot:  
![xyz](https://github.com/user-attachments/assets/f28c14a9-4a1c-4e11-bca3-8f96048a6670)

---

## 🧾 5.10 Changing Color Scale

### Steps:

1. Right-click on scan area  
2. Hover on **Color Scales**  
3. Choose palette (e.g., Viridis, Reds, Jet, Hot)

📷 Screenshot:  
![color-scale](https://github.com/user-attachments/assets/0875879f-d78a-45fb-a6a8-7b0446a0e075)

---

## ✏️ 5.11 Editing Features

### 🧭 Select Region

Click on scan image → yellow marker appears.

📷 Screenshot:  
![select](https://github.com/user-attachments/assets/7336aa69-a7d7-4296-80d7-edc76e8ff17e)

---

### ✏️ 5.11.1 Edit Feature

**Method 1:** Right-click → `Edit Feature`  
**Method 2:** Click ✎ in detail panel

📷 Screenshots:  
![edit1](https://github.com/user-attachments/assets/0474d241-9ac0-46b3-a6a4-fbe2d0b2f20d)  
![edit2](https://github.com/user-attachments/assets/fcb87674-84b7-4965-ace8-49b792c85582)

---

### ➕ 5.11.2 Add Feature

Right-click → `Add Feature`  
Input type and parameters.

📷 Screenshot:  
![add](https://github.com/user-attachments/assets/7c7db278-feb7-4017-b416-b1e4af38bfc8)

---

### ❌ 5.11.3 Delete Feature

Right-click → `Delete Feature`  
Status updates to `MANUALLY_DELETED`.

📷 Screenshot:  
![delete](https://github.com/user-attachments/assets/d78a28a4-3336-406b-b5e2-19288ea71f99)

---

### 🗂️ 5.11.4 Version Control

Feature history tracked as: `v1`, `v2`, …, `Current`

📷 Screenshot:  
![versions](https://github.com/user-attachments/assets/6b801db9-ed2f-41c1-a764-08e448c4dcd3)

---

## 📝 5.12 Editing METALLOSS Region

### 🔸 Select Region

Click a METALLOSS section → yellow highlight appears.

📷 Screenshot:  
![selectmetal](https://github.com/user-attachments/assets/9b47d1a0-af0e-4104-a55f-afaf2ce09772)

---

### ✏️ Edit

- Right-click → Edit Feature  
- OR click ✎ in bottom dialog  

📷 Screenshot:  
![metallossform](https://github.com/user-attachments/assets/aaf6a5a1-2b07-43ed-9aa0-8551da4fbe98)

---

### ➕ Add / ❌ Delete METALLOSS

- **Add:** Right-click → Add METALLOSS → Fill parameters  
- **Delete:** Right-click → Delete

📷 Screenshot:  
![addmetal](https://github.com/user-attachments/assets/b0851a5c-f013-4040-b88f-d00a171fc8ef)

---


# 📘 Chapter 6: Generating Reports

This chapter explains how to generate and export inspection reports using the PipeCM application after completing manual feature analysis.

---

## 🧾 6.1 Starting the Report Generation Process

Before generating a report, ensure you have completed all necessary manual analysis and saved any changes.

### 📝 Steps to Generate a Report:

![image](https://github.com/user-attachments/assets/5af52374-ebd9-4901-9b99-88cc9800b5fd)
![image](https://github.com/user-attachments/assets/b77ec6d7-a6b4-4e4b-9e08-fd811af53dd7)
![image](https://github.com/user-attachments/assets/fa5caf95-6af4-436c-9c6e-fc2a63b9746e)
![image](https://github.com/user-attachments/assets/4db7096d-0e47-45dd-a65e-b284252ca61b)
![Screenshot (162)](https://github.com/user-attachments/assets/cb0251bf-511f-4847-884f-795d1059109e)
![Screenshot (162)](https://github.com/user-attachments/assets/cde26749-884b-42e1-8db9-9dc7a6a76ec0)

![Screenshot (166)](https://github.com/user-attachments/assets/37f5af68-9437-4dbc-984f-8018932a9977)
![Screenshot (167)](https://github.com/user-attachments/assets/e1b35657-7830-42b3-9d45-0f1ab8eab13d)


1.Click on home
2.Click on start app
3.select the desired tool and click on next
4.select the desired run and click on downlaod report for csv file
5.otherwise click on download pdf report for pdf file



---

