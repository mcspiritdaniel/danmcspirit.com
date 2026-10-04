#!/usr/bin/env python3
"""
Update PDF metadata titles based on filenames.
Converts filenames like 'sbet-return-contribution.pdf' to 'SBET Return Contribution'
"""

import os
import re
from pathlib import Path

try:
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    print("PyPDF2 not installed. Install with: pip install PyPDF2")
    exit(1)


def filename_to_title(filename):
    """Convert filename to readable title."""
    # Remove .pdf extension
    name = filename.replace('.pdf', '')

    # Split on hyphens and capitalize each word
    words = name.split('-')

    # Handle common abbreviations
    abbreviations = {'eth', 'sbet', 'iren', 'linea', 'spcx', 'crwv', 'nbis', 'ai'}

    title_words = []
    for word in words:
        if word.lower() in abbreviations:
            title_words.append(word.upper())
        else:
            title_words.append(word.capitalize())

    return ' '.join(title_words)


def update_pdf_title(filepath, title):
    """Update PDF title metadata."""
    try:
        reader = PdfReader(filepath)
        writer = PdfWriter()

        # Copy all pages
        for page in reader.pages:
            writer.add_page(page)

        # Add metadata
        writer.add_metadata({
            "/Title": title,
        })

        # Write back to file
        with open(filepath, 'wb') as f:
            writer.write(f)

        return True
    except Exception as e:
        print(f"Error updating {filepath}: {e}")
        return False


def main():
    pdf_dir = Path('public')

    if not pdf_dir.exists():
        print(f"Error: {pdf_dir} directory not found")
        exit(1)

    pdf_files = sorted(pdf_dir.glob('*.pdf'))

    if not pdf_files:
        print(f"No PDF files found in {pdf_dir}")
        exit(1)

    print(f"Found {len(pdf_files)} PDF files\n")

    updated = 0
    for pdf_file in pdf_files:
        title = filename_to_title(pdf_file.name)
        print(f"Updating: {pdf_file.name}")
        print(f"   Title: {title}")

        if update_pdf_title(str(pdf_file), title):
            updated += 1
            print("   ✓ Success\n")
        else:
            print("   ✗ Failed\n")

    print(f"\nUpdated {updated}/{len(pdf_files)} PDF titles")


if __name__ == '__main__':
    main()
