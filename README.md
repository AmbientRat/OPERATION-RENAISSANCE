# OPERATION RENAISSANCE
Extracts art from MET and AIC to a "daily note" vault note for obsidian, for your local muse inspiration

How this deployment works:

   - The Handshake: On the very first run, it prompts you for the path where you want your output files to go for your obsidian vault. You can feed it an absolute path (e.g., C:\Users\Name\Documents\Obsidian Vaults\Vault\<folder within the vault> or /Users/Name/Documents/...).

   - The Failsafe: It checks if the folder actually exists. If you made a typo or the folder isn't there, it asks if you want to create it on the spot.

   - The Config File: It writes the finalized path to renaissance_config.json. If you ever reorganize your Obsidian Vault and move the folder, simply delete that .json file, and the script will ask you for the new coordinates the next time it runs.

## Dependencies
- need beautifulsoup4 see commands below to install:

```Bash
pip install beautifulsoup4
pip install beautifulsoup4 requests
```

## Usage

Automated Extraction (Windows Task Scheduler)

To ensure **OPERATION RENAISSANCE** runs automatically every morning, you can configure Windows Task Scheduler to act as the handler for the script. 

**Note:** Before automating, run the script manually at least once so you can establish your local drop zone configuration (`renaissance_config.json`).

1. Open the Windows Start Menu, type **Task Scheduler**, and hit Enter.
2. In the right-hand "Actions" pane, click **Create Basic Task...**
3. **Name:** `OPERATION RENAISSANCE - Daily Extraction` (or whatever you prefer) and click **Next**.
4. **Trigger:** Select **Daily** and set your preferred file creation time (e.g., `6:00 AM`).
5. **Action:** Select **Start a program**.
6. **Program/Script Configuration (Crucial Step):**
   - **Program/script:** Type `python` (or see the Ghost Mode tip below).
   - **Add arguments:** Type the name of your script (e.g., `renaissance.py`).
   - **Start in:** Paste the **absolute path** to the folder where your script and config file live (e.g., `C:\Users\YourName\Documents\operation-renaissance`). *Do not put quotes around this path.*
7. Click **Next**, review your parameters, and click **Finish**.

Your system will now automatically run the exfiltration protocol every morning, dropping the random art piece directly into your Obsidian vault.

> **Tip: "Ghost Mode" (Silent Execution)**
> By default, Task Scheduler might briefly flash a black Python terminal window on your screen when it runs. To make the execution completely silent and invisible, change the **Program/script** box in Step 6 from `python` to `pythonw`. The 'w' tells Windows to run the script in the background without launching a console UI.