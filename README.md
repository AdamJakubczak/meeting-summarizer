## Meeting Summarizer

This project automatically summarizes meeting transcripts (original language: Polish) using Gemini AI and exports the results as Markdown and PDF files.

---

## Features

- Extracts speaker contributions from `.vtt` transcript files
- Summarizes meetings using Gemini AI (Google Generative AI)
- Refines summaries for clarity and conciseness
- Outputs results in Markdown and PDF formats
- Customizable HTML template for PDF export

---

## Prerequisites

- Python 3.12+
- [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) (required for PDF export)
  - Download and install from the official site
  - Update the `WKHTMLTOPDF_PATH` variable in main.py to match your installation path (e.g. `C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe`)
- Google Generative AI Python SDK (`google-genai`), Get Your API key and store it in Your PATH. Otherwise specify it in:

```python
client = genai.Client(api_key="YOUR_API_KEY")
```
- Other dependencies listed in requirements.txt

---

## Installation

```sh
pip install -r requirements.txt
```

---

## Usage

1. Place your meeting transcript in the transcriptions folder (e.g. example.vtt).
2. Adjust paths in main.py if needed.
3. Run the summarizer:

```sh
python main.py
```

4. Find the outputs in the output folder:
   - `conversation.json` – extracted speaker turns
   - `pre_summary.md` – initial summary
   - `summary.md` – refined summary
   - `summary.pdf` – final PDF

---

## Configuration

- Prompts and HTML template are defined in prompts.py.
- Change transcript and output paths in main.py as needed.

---

## License

MIT License

---

## Troubleshooting

- If PDF export fails, ensure `wkhtmltopdf` is installed and the path is correct.
- For Google Generative AI, ensure you have valid credentials and access.

---
