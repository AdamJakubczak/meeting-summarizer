import re
import json
import logging
from markdown2 import markdown
import pdfkit
from google import genai
from google.genai import types
import time
from prompts import system_prompt, finishing_prompt, html_template

TRANSCRIPT_PATH = 'transcriptions/example.vtt'
CONVERSATION_JSON_PATH = 'output/conversation.json'
PRE_SUMMARY_MD_PATH = 'output/pre_summary.md'
SUMMARY_MD_PATH = 'output/summary.md'
SUMMARY_PDF_PATH = 'output/summary.pdf'
WKHTMLTOPDF_PATH = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def load_transcript(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_conversation(transcript):
    pattern = re.compile(r'<v\s+([^>]+)>(.*?)</v>')
    return [{'speaker': name, 'text': text} for name, text in pattern.findall(transcript)]

def save_json(data, path):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def generate_content(client: genai.Client, prompt, contents):
    return client.models.generate_content(
        model='gemini-2.5-flash',
        config=types.GenerateContentConfig(system_instruction=prompt),
        contents=contents
    )

def save_text(text, path):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)

def convert_md_to_pdf(md_path, pdf_path, wkhtmltopdf_path):
    with open(md_path, 'r', encoding='utf-8') as file:
        md_text = file.read()
    html_text = markdown(md_text)
    html = html_template.format(content=html_text)

    pdfkit.from_string(html, pdf_path, configuration=pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path))

def main():
    start_time = time.time()
                
    try:
        logger.info('📄 Loading transcript...')
        transcript = load_transcript(TRANSCRIPT_PATH)

        logger.info('🗣️ Extracting conversation...')
        conversation = extract_conversation(transcript)
        save_json(conversation, CONVERSATION_JSON_PATH)

        conversation_json = json.dumps(conversation, ensure_ascii=False, indent=4)

        logger.info('🤖 Initializing GenAI client...')
        client = genai.Client()

        logger.info('📝 Generating initial summary...')
        response = generate_content(client, system_prompt, conversation_json)
        save_text(response.text, PRE_SUMMARY_MD_PATH)

        logger.info('✨ Refining summary...')
        summary_text = load_transcript(PRE_SUMMARY_MD_PATH)
        finishing_response = generate_content(client, finishing_prompt, summary_text)
        save_text(finishing_response.text, SUMMARY_MD_PATH)

        logger.info('📑 Converting markdown to PDF...')
        convert_md_to_pdf(SUMMARY_MD_PATH, SUMMARY_PDF_PATH, WKHTMLTOPDF_PATH)

        end_time = time.time()
        elapsed_time = end_time - start_time
        logger.info(f'✅ Process completed successfully. Time taken: {elapsed_time:.5f}')

    except Exception as e:
        logger.error(f'Error: {e}')

if __name__ == '__main__':
    main()