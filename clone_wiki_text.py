import requests
import os
import time
import re

API_URL = "https://worldwitches.fandom.com/api.php"

def get_all_pages():
    pages = []
    apcontinue = ""

    while True:
        params = {
            "action": "query",
            "list": "allpages",
            "aplimit": "500",
            "apnamespace": "0",
            "format": "json"
        }

        if apcontinue:
            params["apcontinue"] = apcontinue

        r = requests.get(API_URL, params=params)
        data = r.json()

        pages.extend(data["query"]["allpages"])

        if "continue" in data:
            apcontinue = data["continue"]["apcontinue"]
        else:
            break

    return pages

def get_page_wikitext(title):
    params = {
        "action": "query",
        "prop": "revisions",
        "rvprop": "content",
        "rvslots": "main",
        "titles": title,
        "format": "json"
    }

    r = requests.get(API_URL, params=params)
    data = r.json()

    pages = data["query"]["pages"]
    for page_id in pages:
        revisions = pages[page_id].get("revisions")
        if revisions:
            return revisions[0]["slots"]["main"]["*"]
    return ""

def main():
    os.makedirs("wiki_text", exist_ok=True)
    pages = get_all_pages()

    print(f"Found {len(pages)} articles")

    saved = 0

    for page in pages:
        title = page["title"]
        content = get_page_wikitext(title)

        if not content.strip():
            continue

        def safe_filename(name):
            return re.sub(r'[<>:"/\\|?*]', '_', name)

        filename = safe_filename(title) + ".txt"

        filepath = os.path.join("wiki_text", filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        saved += 1
        print(f"[{saved}] Saved: {title}")
        time.sleep(0.5)

    print(f"\nDone. Saved {saved} files.")

if __name__ == "__main__":
    main()