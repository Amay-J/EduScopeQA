#!/usr/bin/env python3
"""
Download script for EduScopeQA source materials

This script fetches publicly available source texts used in the EduScopeQA dataset
from their original sources, respecting copyright and licensing terms.
"""

import os
import requests
from urllib.parse import urlparse
from pathlib import Path

try:
    import PyPDF2
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

def create_directories():
    """Create necessary directory structure"""
    dirs = [
        "history/input",
        "literature/input",
        "science/input"
    ]

    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
    print("Created directory structure")

def download_file(url, filepath):
    """Download a file from URL to filepath"""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Downloaded: {filepath}")
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

def download_history_texts():
    """Download historical texts from Project Gutenberg"""
    history_sources = {
        "economic_peace.txt": "https://www.gutenberg.org/cache/epub/15776/pg15776.txt",
        "philippines_history.txt": "https://www.gutenberg.org/cache/epub/38269/pg38269.txt",
        "frederick_douglass.txt": "https://www.gutenberg.org/cache/epub/23/pg23.txt",
        "common_sense.txt": "https://www.gutenberg.org/cache/epub/147/pg147.txt",
        "benjamin_franklin.txt": "https://www.gutenberg.org/cache/epub/20203/pg20203.txt",
        "north_pole.txt": "https://www.gutenberg.org/cache/epub/18975/pg18975.txt"
    }

    print("Downloading history texts...")
    for filename, url in history_sources.items():
        download_file(url, f"history/input/{filename}")

def download_literature_texts():
    """Download literature texts from Project Gutenberg"""
    literature_sources = {
        "moby_dick.txt": "https://www.gutenberg.org/cache/epub/2701/pg2701.txt",
        "little_women.txt": "https://www.gutenberg.org/cache/epub/37106/pg37106.txt"
    }

    print("Downloading literature texts...")
    for filename, url in literature_sources.items():
        download_file(url, f"literature/input/{filename}")

def convert_pdf_to_txt(pdf_path, txt_path):
    """Convert PDF file to text file"""
    if not PDF_AVAILABLE:
        print("PyPDF2 not available. Please install with: pip install PyPDF2")
        return False

    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text_content = []

            print(f"Converting PDF with {len(pdf_reader.pages)} pages...")
            for page_num, page in enumerate(pdf_reader.pages):
                if page_num % 50 == 0:  # Progress indicator
                    print(f"Processing page {page_num + 1}...")
                text_content.append(page.extract_text())

            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write('\n'.join(text_content))

            print(f"Successfully converted PDF to text: {txt_path}")
            return True
    except Exception as e:
        print(f"Error converting PDF to text: {e}")
        return False

def download_science_texts():
    """Download OpenStax science textbook"""
    print("Downloading science texts...")

    # OpenStax Microbiology PDF download URL
    microbiology_pdf_url = "https://assets.openstax.org/oscms-prodcms/media/documents/Microbiology-WEB_7dhpGAK.pdf"
    pdf_path = "science/input/Microbiology.pdf"
    txt_path = "science/input/Microbiology-WEB.txt"

    print("Downloading OpenStax Microbiology textbook PDF...")
    if download_file(microbiology_pdf_url, pdf_path):
        print("Converting PDF to text format...")
        if convert_pdf_to_txt(pdf_path, txt_path):
            # Clean up PDF file after conversion
            try:
                os.remove(pdf_path)
                print("Cleaned up temporary PDF file")
            except:
                print("Note: You may want to manually delete the PDF file")
        else:
            print(f"PDF downloaded to: {pdf_path}")
            print("Please manually convert to text or install PyPDF2")
    else:
        print("Failed to download OpenStax Microbiology textbook")
        print("Please visit: https://openstax.org/books/microbiology")
        print("Download the PDF and save as: science/input/Microbiology-WEB.txt")

def main():
    """Main function to download all source materials"""
    print("EduScopeQA Source Material Download Script")
    print("==========================================")

    if not PDF_AVAILABLE:
        print("WARNING: PyPDF2 not found. Install with 'pip install PyPDF2' for automatic PDF conversion.")
        print("Science textbook will require manual conversion.\n")

    create_directories()
    download_history_texts()
    download_literature_texts()
    download_science_texts()

    print("\nDownload complete! Source materials are now available in their respective input directories.")
    if PDF_AVAILABLE:
        print("All texts have been automatically downloaded and converted to the correct format.")
    else:
        print("Note: OpenStax PDF may require manual conversion to text format.")

if __name__ == "__main__":
    main()