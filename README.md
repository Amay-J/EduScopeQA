# EduScopeQA Dataset

**A Multi-Subject, Multi-Scope Educational Question-Answering Dataset for RAG System Evaluation**

## Overview

EduScopeQA is a comprehensive question-answering dataset designed to evaluate Retrieval-Augmented Generation (RAG) systems in educational contexts.

## Dataset Composition

### Subjects (3 domains)
- **History**: Historical works including writings by Benjamin Franklin, Thomas Paine, Frederick Douglass, and John Maynard Keynes
- **Literature**: Classic novels including *Moby Dick* and *Little Women*
- **Science**: Full-length OpenStax Microbiology textbook

### 📊 Dataset Composition

| **Subject** | **Source Text** | **Words** | **Specific** | **Sectional** | **Thematic** |
|-------------|----------------|-----------|--------------|---------------|--------------|
| | | | | | |
| **📚 Literature** | | | | | |
| | *Moby-Dick; or, The Whale* by Herman Melville<br/>[📖 Project Gutenberg](https://www.gutenberg.org/cache/epub/2701/pg2701.txt) | 208,465 | 356 | 40 | 20 |
| | *Little Women* by Louisa May Alcott<br/>[📖 Project Gutenberg](https://www.gutenberg.org/cache/epub/37106/pg37106.txt) | 188,683 | 323 | 40 | 20 |
| | ***Literature Subtotal*** | ***397,148*** | ***679*** | ***80*** | ***40*** |
| | | | | | |
| **📜 History** | | | | | |
| | *The North Pole: Its Discovery in 1909* by Robert E. Peary<br/>[📖 Project Gutenberg](https://www.gutenberg.org/cache/epub/18975/pg18975.txt) | 97,980 | 173 | 20 | 10 |
| | *A History of the Philippines* by David P. Barrows<br/>[📖 Project Gutenberg](https://www.gutenberg.org/cache/epub/38269/pg38269.txt) | 77,475 | 173 | 16 | 8 |
| | *Autobiography of Benjamin Franklin* by Benjamin Franklin<br/>[📖 Project Gutenberg](https://www.gutenberg.org/cache/epub/20203/pg20203.txt) | 76,108 | 134 | 15 | 7 |
| | *The Economic Consequences of the Peace* by John Maynard Keynes<br/>[📖 Project Gutenberg](https://www.gutenberg.org/cache/epub/15776/pg15776.txt) | 69,966 | 123 | 14 | 7 |
| | *Narrative of the Life of Frederick Douglass* by Frederick Douglass<br/>[📖 Project Gutenberg](https://www.gutenberg.org/cache/epub/23/pg23.txt) | 40,750 | 72 | 8 | 4 |
| | *Common Sense* by Thomas Paine<br/>[📖 Project Gutenberg](https://www.gutenberg.org/cache/epub/147/pg147.txt) | 21,857 | 38 | 4 | 2 |
| | ***History Subtotal*** | ***384,136*** | ***713*** | ***77*** | ***38*** |
| | | | | | |
| **🔬 Science** | | | | | |
| | *Microbiology* by OpenStax<br/>[📖 OpenStax Textbook](https://openstax.org/books/microbiology) | 397,994 | 678 | 80 | 20 |
| | ***Science Subtotal*** | ***397,994*** | ***678*** | ***80*** | ***20*** |
| | | | | | |
| **🎯 TOTAL DATASET** | | **1,179,278** | **2,070** | **237** | **98** |

> **📈 Summary**: 2,405 total questions across 3 academic domains • 1.18M+ words of university-level content

### Key Features
- **2,405 total question-answer pairs** across three academic domains
- **1.18+ million words** of realistic academic materials
- **Source texts not included** - use provided download script to obtain materials

### Question Types (by scope)

1. **Specific Questions**: Narrow queries answerable from a single paragraph (~500 words)
   - Example: *"Which genera of soil bacteria are involved in the denitrification process?"*

2. **Sectional Questions**: Require information synthesis across multiple paragraphs (~5,000 words)
   - Example: *"How did President Wilson's personality affect the Paris Peace Conference outcome?"*

3. **Thematic Questions**: Broad queries requiring understanding of overarching themes
   - Example: *"What does the Whaleman's Chapel represent in Moby Dick's narrative?"*

## Purpose

This dataset addresses gaps in educational AI evaluation by:

- **Testing pedagogical variations**: Comparing performance across disciplines and question complexity
- **Realistic educational content**: Using actual course materials rather than Wikipedia or news articles
- **Multi-granularity evaluation**: Assessing both factual recall and thematic understanding

## File Structure

```
EduScopeQA/
├── history/
│   └── questions.json  # QA pairs with metadata and source references
├── literature/
│   └── questions.json  # QA pairs with metadata and source references
├── science/
│   └── questions.json  # QA pairs with metadata and source references
└── download_sources.py  # Script to fetch source texts
```

## Obtaining Source Materials

The original source texts are not included in this repository. Instead, we provide a download script (`download_sources.py`) that fetches the publicly available materials from their original sources:

- **History texts**: 6 historical works from Project Gutenberg (public domain)
- **Literature works**: 2 classic novels from Project Gutenberg (public domain)
- **Science textbook**: OpenStax Microbiology textbook (openly licensed)

All Project Gutenberg and OpenStax materials are freely available.

Run the download script to automatically retrieve and organize the source materials:

```bash
# Install required dependencies
pip install requests PyPDF2

# Run the download script
python download_sources.py
```

The script will:
1. Create the appropriate directory structure
2. Download all texts from Project Gutenberg (history and literature)
3. Download the OpenStax Microbiology PDF and convert it to text format
4. Organize all materials into the correct input directories

**Note**: If PDF conversion fails, you can manually download the OpenStax Microbiology textbook and convert it using tools like Adobe Acrobat, online PDF converters, or alternative Python libraries like `pdfplumber`.

## 📄 License & Attribution

### Source Material Licenses

**📚 Literature & History Texts (Project Gutenberg)**
- All texts are in the **public domain** in the United States
- No copyright restrictions - freely usable for any purpose
- Source: [Project Gutenberg](https://www.gutenberg.org/policy/permission.html)

**🔬 Science Textbook (OpenStax)**
- *Microbiology* by OpenStax is licensed under [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
- You are free to: Share, adapt, and use for any purpose (including commercial)
- Attribution required: "Microbiology by OpenStax is licensed under CC BY 4.0"

### EduScopeQA Dataset License

**Question-Answer Pairs & Metadata**
- The questions, answers, and associated metadata created for this dataset are released under [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)