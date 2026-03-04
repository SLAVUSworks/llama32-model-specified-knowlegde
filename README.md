# llama 3.2 Model with Specified Knowlegde Using Wiki Text Assets Indexing as Database

This is a tool that clones text from a specific wiki (such as Wiki Fandom, Wikipedia, etc) and stores it in a Chroma database using LLaMA embeddings.

## 🚀 Features
- Clone Wikipedia text from a specific wiki using the MediaWiki API
- Save the cloned text to a local directory
- Index the cloned text using the Chroma database and LLaMA embeddings
- Clean and preprocess the text data for better indexing and querying
- Split the text into chunks for more efficient indexing and querying
- Display a progress bar during the indexing process
- Support for handling large amounts of text data

## 🛠️ Tech Stack
- Python 3.x
- `requests` library for making HTTP requests to the MediaWiki API
- `os` library for creating directories and writing files to the local file system
- `time` library for introducing a delay between requests to avoid overwhelming the API
- `re` library for sanitizing filenames and extracting data from API responses
- `chromadb` library for interacting with the Chroma database
- `ollama` library for generating LLaMA embeddings
- `tqdm` library for displaying a progress bar during the indexing process

## 📦 Installation
To install the required dependencies, run the following command:
```bash
pip install requests os time re chromadb ollama tqdm
```
Make sure to install the dependencies in the correct order and with the correct versions.

## 💻 Usage
To clone the wiki text and index it, follow these steps:
1. Run the `clone_wiki_text.py` script to clone the wiki text from the specific wiki.
2. Run the `index_wiki.py` script to index the cloned text using the Chroma database and LLaMA embeddings.

## 📂 Project Structure
```markdown
.
├── clone_wiki_text.py
├── index_wiki.py
├── wiki_text
│   ├── page1.txt
│   ├── page2.txt
│   └── ...
├── requirements.txt
└── README.md
```
## 🤝 Contributing
To contribute to this project, please fork the repository and submit a pull request with your changes. Make sure to follow the standard professional guidelines for contributing to open-source projects.

## 📝 License
This project is licensed under the MIT License. See the LICENSE file for more information.
