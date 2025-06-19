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
- **Forgot Username or Password?** – Click the respective links to recover your credentials.

---

## 🧭 1.3 Post-Login Dashboard

📷 **Screenshot:**  
![3](https://github.com/user-attachments/assets/dbb8012a-2409-4d91-942f-9929a0aee055)




After successful login, users land on the main dashboard containing the following modules:

- **MFL + EC** – Gas pipeline inspection  
- **MFL + UT** – Oil pipeline inspection using ultrasonic and flux leakage data  
- **Health Assessment** – Tool and pipeline data analysis  
- **Settings** – Customize software configurations  

Each section contains a **"Start App"** button to launch its respective module.

---

# 📘 Chapter 2: Creating a Run

**Version:** 1.0  
**Organization:** Bhabha Atomic Research Centre (BARC)

This chapter walks you through the complete process of creating a new pipeline run in PipeCM — including tool selection, run details, file uploads, and confirmation.

---

## 🧾 2.1 Select Tool

The first step is to choose the appropriate inspection tool for the pipeline run.

📷 **Screenshot:** _Insert Select Tool Screenshot_

**Steps:**
- From the **Select Tool** screen, choose a tool by clicking the radio button in the **Select** column.
- **Tool details include:**
  - **Tool Type:** e.g., `MFL_OCTA_GEN1`
  - **Tool Size:** e.g., `12 inch`
- Click **NEXT** to proceed.

---

## 🧾 2.2 Create a Run

Enter run-specific metadata such as source, destination, and date.

📷 **Screenshot:** _Insert Add Run Screenshot_

**Fill the following fields:**
- **Run Source:** e.g., `location1`
- **Run Destination:** e.g., `location2`
- **Run Date:** e.g., `19/06/2025`

Click **ADD** to create the run entry.

---

## 🧾 2.3 Uploading Binary Files

After the run is created, upload sensor data files.

### 📍 2.3.1 Browse and Select Files

- Click **BROWSE FILES**
- Select files from your system (e.g., `TMP0001_AK.bin`, `TMP0002_AK.bin`)

📷 **Screenshot:** _Insert File Browse Screenshot_

### 📍 2.3.2 Upload the Files

- Selected files will show with progress bars.
- Click **UPLOAD** to start the transfer.

📷 **Screenshot:** _Insert Upload Progress Screenshot_

### 📍 2.3.3 Save and Confirm

Once upload completes:

- Click **SAVE**
- A confirmation popup appears:

> _“Do you want to proceed with processing?”_  
> _“If confirmed, you cannot upload files anymore to this Run…”_

📷 **Screenshot:** _Insert Confirmation Popup Screenshot_

- Click **YES, I'M SURE** only when ready to finalize.

⚠️ **Note:** After confirmation, no more files can be added to this run.

---

## 🧾 2.4 Run Status & Processing

After saving, you’re redirected to the **Select Run** screen.

📷 **Screenshot:** _Insert Select Run Screenshot_

**Check the Status column:**
- Initially: `FILES_TO_BE_UPLOADED`
- After confirmation: `TO_BE_PROCESSED`

Click **NEXT** to continue.

---

## 🧾 2.5 Review Uploaded Files

On the **Select File** screen, you can view the uploaded `.bin` files.

📷 **Screenshot:** _Insert Select File Screenshot_

Each file displays:
- **File Name**
- **Sequence Number**
- **Status:** `TO_BE_PROCESSED`

---

## 🧾 2.6 Status Change on Navigation

If you return to the **Select Run** screen by clicking **BACK**, the status of the run changes:

- `FILES_TO_BE_UPLOADED` → `TO_BE_PROCESSED`

📷 **Screenshot:** _Insert Status Update Screenshot_

This means the system has queued your files for processing.

