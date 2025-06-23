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
![3](https://github.com/user-attachments/assets/815ec30b-44b4-478b-8def-71ff615621d7)

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
![Edit Icon](https://github.com/user-attachments/assets/34b317e9-3665-4e2a-9721-bec8bc4a3924)

> This action will navigate you to the **Configure** screen for the selected run.

---

## 🧾 3.2 Overview of Editable Configurations

The **Configure** screen allows modification of parameters related to the run's data processing.

📷 **Screenshot:**  
![Configure Screen](https://github.com/user-attachments/assets/5264e5f9-0e00-4f2c-b539-82364eb7df7d)

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

📷 **Screenshot:**  
![NoOfChannels Example](https://github.com/user-attachments/assets/8e49e647-4c0d-4afd-850a-288284e8bdfa)

2. Input the total number of channels in this field.  
   Example: For 128 channels, enter `128`.

---

## 🧾 3.4 Determining and Specifying Faulty Channels

In the **Faulty Channels** section:

1. If there are no faulty sensors, leave the fields for `HALL` and `EDDY` empty.

2. To specify faulty channels, use:
   - **Comma-separated values** for individual channels
   - **Hyphenated ranges** for sequences
   - Or a **combination of both**

📷 **Example Configuration Screenshot:**  
![Faulty Channels Example](attachment)

### ✅ Examples:

- `1-24,34-45`: Indicates channels 1 to 24 and 34 to 45 are faulty.

> This tells the system to use nearby healthy channels during processing.

---

## 🧾 3.5 Saving Configuration Changes

Once all changes are made:

1. Click the **SAVE** button at the bottom right of the screen to apply the changes.
2. To revert to system defaults, click the **SET DEFAULT** button.

✅ **Note:** Incorrect configuration values can affect data analysis. Always double-check your entries before saving.



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

# 📘 Chapter 5: Manual Analysis

This chapter explains the process of conducting **Manual Feature Analysis** using the PipeCM application. It includes how to interpret the left-hand pipeline data table, filter features, view scan images, and analyze defects.

---

## 🧾 5.1 Interface Overview

![1](https://github.com/user-attachments/assets/2df50d69-992f-4c51-a794-021ca9dbec85)

### ➤Steps:

1. **Select** the desired file.  
2. **Click on submit**.  

📷 **Screenshot:**  
![Screenshot (84)](https://github.com/user-attachments/assets/098258cc-6c75-4e85-94bf-6c2920f01a1a)

The Manual Analysis screen is split into two main sections:

- **Left Pane:** Pipetally table (fetched from database)  
- **Right Pane:** Visualization of pipeline scan with defect markers


---

## 🧾 5.2 Pipetally Table (Left Pane)

The table on the left is auto-populated from PipeCM’s database and shows features detected in the pipeline.

### 🔹 Key Features of the Table:

- Displays **n** entries by default  
- Organized by **Page Number** (ascending) also we can control them 
- Supports **filtering** and **sorting** on all columns  
- Select the feature and click the **Reload** button (🔄)
- Any new feature added will be also get reflected


📷 **Screenshot:**
![2](https://github.com/user-attachments/assets/2bce2c71-ae7b-4a3f-840b-17328c630efa)

### ➤Guide:

1. **Click** for fullscreen.  
2. **Click** for reload table.

### 📚 Column Breakdown:

| Column Name       | Description                             |
|------------------|-----------------------------------------|
| **Select**        | Choose a row for detailed inspection    |
| **Page No**       | Page number in the pipeline scan        |
| **Sample No**     | Sample number of feature                |
| **Feature Type**  | Feature classification (e.g., METALLOSS, WELD, VALVE) |
| **Log Distance**  | Distance on pipeline log (in m)        |
| **Absolute Sample** | Absolute Sample                       |
| **Wall Loss**     | % wall thickness loss                   |
| **Length**        | Length of defect                        |
| **Max Width**     | Maximum width            |
| **Width / Depth** | Actual size of defect                   |
| **Gauss Peak**    | Magnetic peak value                     |
| **Span**          | Width spread                            |
| **Max Depth**     | Critical depth data                     |
| **MAOP**          | Max allowable operating pressure impact |
| **No. of Sensors**| Number of sensors that picked metal loss       |


📷 **Screenshot (Table in Action):**  
![3](https://github.com/user-attachments/assets/40528029-6483-4413-8da0-f3d7723a7fce)

---

## 🧾 5.3 Filter Features

You can **filter by Feature Type** using the dropdown above the table.

📷 **Screenshot (Feature Selection Dropdown):**  

### ✅ Available Feature Types:

- **WELD**  
- **METALLOSS**  
- **FLANGE**  
- **VALVE**  
- **MARKER**  
- **SLEEVE_START / END**  
- **AREA_START / END**  
- **ATTACHMENT**  
- **TAP**  
- **CLAMP**  
- **SUPPORT_START / END**  
- **REDUCER_START / END**  
- **UNKNOWN**
- **KICKER_LINE_CENTRE**
- **LIMIT_VALVE**
- **BARREL_ISOLATION_VALVE**  


📷 **Extended Feature List Screenshot:**  
![5](https://github.com/user-attachments/assets/74d75a2f-78d5-4fc0-ac1a-191216680e79)
![Screenshot (19)](https://github.com/user-attachments/assets/7cecb17c-6c17-4a47-8e1a-6f2eb8d457c1)
![Screenshot (20)](https://github.com/user-attachments/assets/e18966f2-928f-4130-be2b-d7d22086e6b9)
![6](https://github.com/user-attachments/assets/e136ea2b-c768-40d7-a9e2-1e308bba570c)
![7](https://github.com/user-attachments/assets/a1bca99a-8ce0-4de3-8343-a9f480853433)





### 🔘 Filter by Feature Type

You can filter the data table to display only selected types of pipeline features.

#### 📝 Steps to Filter by Feature Type:

1. Click the **Select a feature** dropdown.
2. Choose one or more feature types (e.g., **WELD**, **METALLOSS**, **VALVE**, etc.).
3. Click the **Reload** button (🔄) to update the table with filtered results.
 
---

### 🔘 Filter by Individual Columns

Each column allows advanced filtering to refine the displayed data:

| Filter Type              | Description                              |
|--------------------------|------------------------------------------|
| Equals / Not Equals      | Match specific values                    |
| Contains / Starts With   | Match string patterns                    |
| Greater / Less Than      | Compare numerical values                 |
| Between / Inclusive      | Filter within a range                    |
| Empty / Not Empty        | Check for missing or present values      |

#### 📝 Steps to Use Column Filters:

1. Click the **filter icon** (🔽) next to the column header.
2. Select the desired condition from the dropdown.
3. Enter filter values.
4. The table updates automatically with matching rows.

📷 *Screenshot – Column Filter Options*
![Screenshot (22)](https://github.com/user-attachments/assets/a3cdcac0-d4be-49de-9d5e-ee205622c284)


---

### 🔘 Pagination and Row Control

The table supports pagination, making it easier to navigate through thousands of rows.

#### 📌 Key Features:

- Navigate using:
  - First (⏮)
  - Previous (⏪)
  - Next (⏩)
  - Last (⏭) buttons
- **Rows per page** selector at the bottom lets you choose how many entries to show:
  - Options typically include: **10**, **30**, **50**, **100**

📷 *Screenshot – Rows Per Page and Pagination Controls*
![image](https://github.com/user-attachments/assets/13257f0d-1cfb-4e33-b5d0-59dcfd8ad556)

![image](https://github.com/user-attachments/assets/8d75d98e-432b-479b-92ee-37f2f873b8fe)





---

## 🧾 5.4 Feature Selection & Navigation

The Manual Analysis module allows users to interact with the pipeline feature table for deeper inspection and analysis.

---

### 🖱️ Double Click Navigation

You can **double-click** any row in the feature table to automatically navigate to the corresponding location in the pipeline scan.

#### 📌 Functionality:

- Helps quickly correlate feature data with its visual representation in the scan.

📷 *Screenshot – Double Click to Navigate*
![Screenshot (21)](https://github.com/user-attachments/assets/ba81fc4c-9019-45ce-9f6d-523502f83810)


---

### 🎯 Feature Highlight and Detailed View

When a row is **selected** (via single click or radio button), the corresponding feature is:

- ✅ **Highlighted** on the pipeline scan (right pane) with a colored marker.
- 📄 **Detailed information** is displayed below the table or scan area (depending on layout).

#### 📋 Details Typically Include:
| Field            | Description                                           |
|------------------|-------------------------------------------------------|
| Feature Type     | Classification of the feature (e.g., WELD, METALLOSS) |
| Sample Number    | Sample index where the feature was detected           |
| Date             | Date of feature detection or data recording           |
| Status           | Current status of the feature (e.g., Confirmed, Flagged) |
| Remark           | User notes or system-generated remarks                |
| Log Distance     | Distance along the pipeline in millimeters            |
| Absolute Sample  | Raw sample number from the sensor dataset             |
| Page Number      | Corresponding page in the scan data                   |


---
## 🧾 5.5 Visual Feature Navigation & Tools

The right-hand pane provides a powerful visual interface for examining pipeline scans. Each feature selected from the left pane is shown here with high-resolution scan overlays.

📷 *Screenshot – Feature View Panel*
![a1](https://github.com/user-attachments/assets/1b5e4fd7-b13e-4dbb-90ff-5ae2f99b38c0)


### ➤ Key Components:

| Ref | Feature                 | Description                                                                 |
|-----|-------------------------|-----------------------------------------------------------------------------|
|  1 | Scan Name              | Displays the name of the scan section (e.g., Pipeline-Scan1, Pipeline-Scan2). Useful for identifying which log section is being analyzed. |
|  2 | Feature Type Selector  | Dropdown menu to switch between detected features such as WELD, METALLOSS, etc. This updates the view to show the selected feature in the scan. |
|  3 | Page Navigation Dropdown | Selects a specific page from the pipeline scan to jump to it instantly.   |
|  4 | Goto Page Input        | Directly type in a page number and press enter to navigate to that exact page. |
|  5 | Next Page Button    | Advances to the next page in the scan for quicker browsing.                |
|  6 | Previous Page Button  | Returns to the previous scan page.                                         |
|  7 | View Mode Selector     | Allows switching between visualization modes:<br>✔️ PIPELINE-SCAN<br>✔️ LINE PLOT<br>✔️ DENOISED PIPELINE-SCAN<br>✔️ DENOISED LINE PLOT |


---

## 🧾 5.6 Visualization Modes

The PipeCM Manual Analysis module supports four visualization types, each suited for different inspection needs.

### 🎯 Available Modes:

| Mode Name               | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| PIPELINE-SCAN          | Displays raw scan image of the pipeline along its length. Good for identifying physical patterns and defects visually. |
| LINE PLOT              | Plots signal data from sensors as line graphs. Useful for analyzing signal intensity, patterns, and detecting inconsistencies. |
| DENOISED PIPELINE-SCAN | A filtered version of the pipeline scan that removes background noise and helps focus on actual defects. |
| DENOISED LINE PLOT     | Cleaned signal graph with noise reduction for better clarity during signal analysis. |

![a2](https://github.com/user-attachments/assets/9e382722-5404-4d0c-830a-c37d7fe07a7f)

### 📝 Steps:

1. Right-click on 3 dots.
2. Select the desired modes.  

📷 *Screenshot – PIPELINE-SCAN*  

📷 *Screenshot – LINE PLOT*  

📷 *Screenshot – DENOISED PIPELINE-SCAN* 

📷 *Screenshot – DENOISED LINE PLOT*


---

## 🧾 5.6  Scan Interaction Tools

The top-right corner of the Pipeline Scan Viewer provides essential tools to help users explore and analyze scan images interactively.

📷 *Screenshot – Scan Toolbar Buttons*
![a3](https://github.com/user-attachments/assets/f2d23016-148b-49f1-98a7-bda10d62f684)


### 🧰 Toolbar Functionality Breakdown

| Ref | Tool        | Description                                                         |
|-----|-------------|---------------------------------------------------------------------|
| 🔍 1 | Zoom Tool   | Activates zoom mode — click and drag to zoom into a specific section. |
| ➕ 2 | Zoom In     | Click to incrementally zoom in for more detail.                    |
| ➖ 3 | Zoom Out    | Click to zoom out to see a wider area of the scan.                 |
| 🔄 4 | Reset View  | Returns the scan to its original zoom and position.               |
| 🔲 5 | Box Select  | Lets users draw a rectangle around a region — can be used with Zoom. |

### 📝 Zoom into a Specific Area:

1. Click the **Box Select** tool  
2. Drag to define a rectangular area  
3. Click the **Zoom** icon  



---

## 🧾 5.7 Lineplot Visualization (Circumferential Profile)

The circumferential profile provides a bar chart view of the magnetic response captured by the sensors around the pipe. It helps analysts understand how defects spread around the pipe's circumference.

### 📝 Steps to View the Lineplot:

![a7](https://github.com/user-attachments/assets/d9da373b-98e9-4cb1-a9e9-21938d8cc8fb)
![a8](https://github.com/user-attachments/assets/d60242f0-98da-48f2-a3cd-2e0888cd392b)
![a9](https://github.com/user-attachments/assets/aaa82c81-ca20-4cff-89e2-9ca03eb01d44)
![a10](https://github.com/user-attachments/assets/64e2fe2c-e7f4-486c-9740-dad9d6658eb6)
![a11](https://github.com/user-attachments/assets/629846da-5aa9-4abb-bd59-c5c9d03eaa6d)

### 📝 Steps:

1. Click on box select.
2. Select a region by holding left click of mouse
3. Right click and click on  **"Show Circumferential Profile"** from the context menu.  
4. A bar chart appears below the pipeline scan view.  
5. To hide it again, right-click and select **"Hide Circumferential Profile."**  


### 📊 Understanding the Axes and Values

| Axis / Value   | Represents                                                   |
|----------------|--------------------------------------------------------------|
| **X-Axis**     | Sample Number    |
| **Y-Axis**     | Sensor Number - Each sensor around the pipe (starts at 0).|
| **Z-Axis**     | Gauss Level     |


📷 *Screenshot – X, Y, Z value meaning (Sample no, Sensor no, Gauss value)*

![a12](https://github.com/user-attachments/assets/f28c14a9-4a1c-4e11-bca3-8f96048a6670)

---

## 🎨 5.8 Changing the Color Scale

To enhance contrast or tailor the view to your analysis preferences, you can change the **color scale** of the pipeline scan view.

### 🪄 Steps to Change the Color Scheme:

1. Right-click on the scan area.
2. Hover over **Color Scales** in the context menu.
3. Select from the following color palettes:
   - Blues  
   - Greens  
   - Reds  
   - Greys  
   - Viridis  
   - Oranges  
   - Jet  
   - Hot  
   - Cool  
   - Spring
  

Different palettes help improve visual detection based on lighting and contrast needs.

📷 *Screenshot – Choosing Color Scale*
![a13](https://github.com/user-attachments/assets/0875879f-d78a-45fb-a6a8-7b0446a0e075)





---









