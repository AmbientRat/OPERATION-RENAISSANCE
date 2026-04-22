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
