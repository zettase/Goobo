# GOOBO BOT README

Welcome to the Goobo Bot documentation! Here's a quick guide to get you started on Windows.

## 1. Installing Dependencies

### Setting Up Python and pip

#### a. Install Python

- Download Python for Windows from the official website: [Python Downloads](https://www.python.org/downloads/)
- During installation, ensure you **check** the option that says "Add Python X.X to PATH".
- Verify the installation by opening a command prompt and typing:
  ```
  python --version
  ```

#### b. Install pip

If you don't have `pip` pre-installed:

- Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to a folder on your computer.
- Open a command prompt, navigate to the folder containing `get-pip.py`.
- Run the command:
  ```
  python get-pip.py
  ```

#### c. Verify pip Installation

In the command prompt, type:
  ```
  pip --version
  ```

#### d. Add pip to Windows PATH (if necessary)

If `pip` is not available in the command prompt:

- Right-click on the Windows Start icon and click on 'System'.
- Click on 'Advanced system settings'.
- Select the 'Advanced' tab and click on 'Environment Variables'.
- Find the 'Path' variable, select it, and click 'Edit'.
- Click 'New' and paste:
  ```
  C:\Users\<YourUsername>\AppData\Local\Programs\Python\PythonXX\
  C:\Users\<YourUsername>\AppData\Local\Programs\Python\PythonXX\Scripts\
  ```
  Replace `<YourUsername>` with your username and `PythonXX` with your Python version.

### Installing Goobo Bot Dependencies

In the Command Prompt, execute:
```
pip install -r requirements.txt
```

## 2. Setting up the Environment Variable

Set an environment variable named `GOOBO_BOT_TOKEN`:

In Command Prompt, enter:
```
setx GOOBO_BOT_TOKEN "Your_Discord_Bot_Token"
```

Replace `Your_Discord_Bot_Token` with your token.

## 3. Running the Goobo Bot Script

Run the script by entering:
```
python goobo_bot.py
```

Ensure you're in the directory containing `goobo_bot.py`.

**Enjoy using Goobo Bot!**
