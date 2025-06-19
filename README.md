# Cyrillic Normalizer

A Python library for normalizing text containing mixed Cyrillic and Latin homoglyphs (visually similar characters).

## Overview

The Cyrillic Normalizer solves a common problem in text processing: handling visually identical characters from different alphabets. Many Cyrillic and Latin characters look exactly the same (like А/A, О/O, Р/P) but have different Unicode codepoints, which can cause issues in text processing, search, and data consistency.

## Features

- **Cyrillic Normalization**: Convert Latin homoglyphs to their Cyrillic equivalents
- **Latin Normalization**: Convert Cyrillic homoglyphs to their Latin equivalents
- **Simple API**: Two main functions for bidirectional conversion
- **Zero Dependencies**: Lightweight implementation using only Python standard library

## Supported Character Mappings

The library handles the following homoglyph pairs:

| Latin | Cyrillic | Description |
|-------|----------|-------------|
| A/a   | А/а      | Capital/lowercase A |
| B     | В        | Capital B |
| E/e   | Е/е      | Capital/lowercase E |
| K/k   | К/к      | Capital/lowercase K |
| M     | М        | Capital M |
| O/o   | О/о      | Capital/lowercase O |
| P/p   | Р/р      | Capital/lowercase P |
| C/c   | С/с      | Capital/lowercase C |
| T     | Т        | Capital T |
| X/x   | Х/х      | Capital/lowercase X |

## Installation

```bash
pip install git+https://github.com/sth-v/cyrillic-normalizer
```

## Usage

### Converting to Cyrillic

```python
from cyrillic_normalizer.homoglyphs import fix_homoglyphs_cyrillic

# Input contains Latin 'c' that looks like Cyrillic 'с'
mixed_text = "Веc"  # "Вес" with Latin 'c'
normalized = fix_homoglyphs_cyrillic(mixed_text)
print(normalized)  # "Вес" (all Cyrillic)
```

### Converting to Latin

```python
from cyrillic_normalizer.homoglyphs import fix_homoglyphs_latin

# Input contains Cyrillic 'А' that looks like Latin 'A'
mixed_text = "Аrea"  # "Area" with Cyrillic 'А'
normalized = fix_homoglyphs_latin(mixed_text)
print(normalized)  # "Area" (all Latin)
```

## Use Cases

- **Data Cleaning**: Normalize user input that may contain mixed scripts
- **Search Optimization**: Ensure consistent character encoding for search functionality
- **Text Processing**: Standardize text before analysis or comparison
- **Database Consistency**: Clean data before storage to avoid encoding issues
- **Internationalization**: Handle text from users with different keyboard layouts

## Requirements

- Python >= 2.7
- No external dependencies

## License

This project is open source. See the project files for license details.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Author

- Andrew Astakhov (sth-v) - sthv.developer@gmail.com