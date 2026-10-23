# Windows Registry Artifact Parser 🔍

A lightweight Python utility designed for digital forensics investigators and cybersecurity enthusiasts to parse, extract, and analyze Windows Registry hive artifacts (such as the `SAM` hive) securely and efficiently.

---

## 🚀 Features
* **Hive Loading & Parsing:** Safely loads and parses Windows Registry binary hive files using the robust `python-registry` library.
* **Artifact Extraction:** Extracts essential root keys, subkeys, and precise timestamps (e.g., *Last Modified* dates)[cite: 6].
* **Forensic Readiness:** Built to assist in digital forensics and incident response (DFIR) investigations.

---

## 🛠️ Prerequisites & Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/gala-cmd383/windows-registry-artifact-parser.git](https://github.com/gala-cmd383/windows-registry-artifact-parser.git)
   cd windows-registry-artifact-parser
   Install the required dependencies:


## ⚙️ Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## 💻 Usage

Run the parser script against a target registry hive file (e.g., `SAM`):

```bash
python src/parser.py SAM
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).
