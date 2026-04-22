import requests
import random
import os
import json
from datetime import datetime
from bs4 import BeautifulSoup

# --- CONFIGURATION ---
CONFIG_FILE = "renaissance_config.json"
API_URL = "https://api.artic.edu/api/v1/artworks"

def initialize_drop_zone():
    """Checks for existing config, or prompts for the vault path."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            vault_path = config.get("vault_path")
            
            if vault_path and os.path.exists(vault_path):
                return vault_path

    print("\n[!] OPERATION RENAISSANCE: Initializing...")
    print("[!] Target drop zone not found in local configuration.")
    vault_path = input("\n[?] Enter the absolute path to your Obsidian destination folder:\n> ").strip()
    vault_path = os.path.expanduser(vault_path)

    if not os.path.exists(vault_path):
        print(f"\n[!] Warning: The path '{vault_path}' does not currently exist.")
        create_dir = input("[?] Would you like to establish this directory now? (y/n): ").strip().lower()
        if create_dir == 'y':
            os.makedirs(vault_path)
            print("[+] Directory established.")
        else:
            print("[-] Operation aborted. Please create the target folder and restart.")
            exit()

    with open(CONFIG_FILE, "w") as f:
        json.dump({"vault_path": vault_path}, f, indent=4)
    
    print(f"[+] Coordinates secured in {CONFIG_FILE}. Commencing extraction...\n")
    return vault_path

def get_random_art():
    print("[*] Intercepting a single random asset...")
    
    # Find the total number of valid pages
    search_params = {"filter[is_public_domain]": "true", "limit": 1}
    response = requests.get(API_URL, params=search_params).json()
    total_pages = response['pagination']['total_pages']
    
    # Target a random page and pull exactly 1 asset
    random_page = random.randint(1, total_pages)
    page_response = requests.get(API_URL, params={
        "filter[is_public_domain]": "true", 
        "page": random_page, 
        "limit": 1
    }).json()
    
    art_data = page_response['data'][0]
    
    # --- HTML Scrubbing ---
    raw_desc = art_data.get('description')
    if raw_desc:
        description = BeautifulSoup(raw_desc, "html.parser").get_text()
    else:
        description = "No description summary available."
    # ----------------------
    
    image_id = art_data.get('image_id')
    img_url = f"https://www.artic.edu/iiif/2/{image_id}/full/843,/0/default.jpg" if image_id else None
    
    return {
        "title": art_data.get('title', 'Unknown Title'),
        "artist": art_data.get('artist_display', 'Unknown Artist'),
        "date": art_data.get('date_display', 'Unknown Date'),
        "medium": art_data.get('medium_display', 'Unknown Medium'),
        "description": description,
        "image": img_url,
        "link": f"https://www.artic.edu/artworks/{art_data['id']}"
    }

def create_obsidian_note(art, vault_path):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"Canvas - {today}.md"
    filepath = os.path.join(vault_path, filename)
    
    # --- YAML Sanitization ---
    safe_title = str(art['title']).replace('\n', ' ').replace('"', '\\"')
    safe_artist = str(art['artist']).replace('\n', ', ').replace('"', '\\"')
    safe_date = str(art['date']).replace('"', '\\"')
    safe_medium = str(art['medium']).replace('\n', ', ').replace('"', '\\"')
    # -------------------------
    
    content = f"""---
title: "{safe_title}"
artist: "{safe_artist}"
date: "{safe_date}"
medium: "{safe_medium}"
source: "{art['link']}"
tags:
  - operation-renaissance
  - daily-canvas
---

# {art['title']}
**Artist:** {safe_artist}  
**Date:** {art['date']}  
**Medium:** {safe_medium}

![{art['title']}]({art['image']})

## Art Summary
{art['description']}

---
[View Asset Source]({art['link']})
"""
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"[+] OPERATION RENAISSANCE: Asset '{art['title']}' secured.")
    print(f"[+] Blind drop to '{filename}' complete.")

if __name__ == "__main__":
    target_path = initialize_drop_zone()
    art_asset = get_random_art()
    create_obsidian_note(art_asset, target_path)