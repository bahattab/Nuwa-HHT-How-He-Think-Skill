#!/usr/bin/env python3
"""
Convert SRT/VTT subtitles to a plain-text transcript.
Remove timestamps, cue numbers, duplicate lines, and HTML tags.

Usage:
    python3 srt_to_transcript.py input.srt [output.txt]
    python3 srt_to_transcript.py input.vtt [output.txt]

When no output path is specified, write to input_transcript.txt.
"""

import sys
import os
import re
from pathlib import Path

# Use UTF-8 for console output on Windows.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass


def clean_srt(content: str) -> str:
    """Clean subtitles in SRT format."""
    lines = content.strip().split('\n')
    texts = []

    for line in lines:
        line = line.strip()
        # Skip numeric cue identifiers.
        if re.match(r'^\d+$', line):
            continue
        # Skip timestamp lines.
        if re.match(r'\d{2}:\d{2}:\d{2}', line):
            continue
        # Skip blank lines.
        if not line:
            continue
        # Strip HTML tags.
        line = re.sub(r'<[^>]+>', '', line)
        # Remove VTT position markers.
        line = re.sub(r'align:.*$|position:.*$', '', line).strip()
        if line:
            texts.append(line)

    # Remove consecutive duplicates found in automatic captions.
    deduped = []
    for text in texts:
        if not deduped or text != deduped[-1]:
            deduped.append(text)

    # Merge short lines into paragraphs.
    result = []
    current = []

    for text in deduped:
        current.append(text)
        # Flush the paragraph at the length threshold or sentence punctuation.
        joined = ' '.join(current)
        if len(joined) > 200 or re.search(r'[。！？.!?]$', text):
            result.append(joined)
            current = []

    if current:
        result.append(' '.join(current))

    return '\n\n'.join(result)


def clean_vtt(content: str) -> str:
    """Remove the VTT header, then clean cues with the SRT parser."""
    # Remove the WEBVTT header.
    content = re.sub(r'^WEBVTT.*?\n\n', '', content, flags=re.DOTALL)
    # Remove NOTE blocks.
    content = re.sub(r'NOTE.*?\n\n', '', content, flags=re.DOTALL)
    return clean_srt(content)


def main():
    arabic = os.environ.get("NUWA_LANG", "").lower().replace("_", "-").split("-")[0] == "ar"
    if len(sys.argv) < 2:
        print(("الاستخدام" if arabic else "Usage") + ": python3 srt_to_transcript.py <input.srt|input.vtt> [output.txt]")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"{'الملفّ غير موجود' if arabic else 'File not found'}: {input_path}")
        sys.exit(1)

    # Choose the default output filename.
    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.parent / f"{input_path.stem}_transcript.txt"

    # Read the input and detect its format.
    content = input_path.read_text(encoding='utf-8')

    if input_path.suffix.lower() == '.vtt' or content.startswith('WEBVTT'):
        transcript = clean_vtt(content)
    else:
        transcript = clean_srt(content)

    output_path.write_text(transcript, encoding='utf-8')

    # Count words and paragraphs.
    word_count = len(transcript)
    line_count = transcript.count('\n') + 1
    print(f"{'اكتمل التحويل' if arabic else 'Conversion complete'}: {output_path}")
    print(f"   {'الكلمات' if arabic else 'Words'}: {word_count}  {'الفقرات' if arabic else 'Paragraphs'}: {line_count}")


if __name__ == '__main__':
    main()
