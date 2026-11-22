#!/bin/bash
# Download subtitles from a YouTube video.
# Usage: ./download_subtitles.sh <YouTube_URL> [output_directory]
# Prefer human-written subtitles, then fall back to automatic captions.
# Language priority: Chinese, English, then other languages where supported.
# The transcript converter accepts either SRT or VTT.

set -e
message() {
    case "${NUWA_LANG:-en}" in
        ar|ar-*|ar_*) printf '%s\n' "$2" ;;
        *) printf '%s\n' "$1" ;;
    esac
}


URL="$1"
OUTPUT_DIR="${2:-.}"

if [ -z "$URL" ]; then
    message "Usage: ./download_subtitles.sh <YouTube_URL> [output_directory]" "الاستخدام: ./download_subtitles.sh <YouTube_URL> [مجلّد الإخراج]"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

# Use a fresh temporary directory so only newly downloaded files are selected.
WORK_DIR=$(mktemp -d)
trap 'rm -rf "$WORK_DIR"' EXIT

# Usage: try_download <yt-dlp subtitle option> <language list>
# Move a successful download and print its path. Return nonzero on failure.
try_download() {
    rm -rf "${WORK_DIR:?}"/*
    yt-dlp "$1" --sub-langs "$2" --sub-format "srt/vtt/best" --skip-download \
        -o "$WORK_DIR/%(title)s" "$URL" >/dev/null 2>&1 || true
    local file
    file=$(find "$WORK_DIR" -type f \( -name "*.srt" -o -name "*.vtt" \) | head -1)
    [ -n "$file" ] || return 1
    mv "$file" "$OUTPUT_DIR/"
    echo "$OUTPUT_DIR/$(basename "$file")"
}

message ">>> Checking available subtitles…" ">>> جارٍ التحقّق من الترجمات النصّيّة المتاحة…"
yt-dlp --list-subs --no-download "$URL" 2>/dev/null | tail -20 || true

echo ""
message ">>> Trying human-written subtitles (Chinese first)…" ">>> جارٍ البحث عن ترجماتٍ نصّيّة بشريّة، بدءًا بالصينيّة…"

# Try human-written Chinese subtitles.
if FOUND=$(try_download --write-subs "zh-Hans,zh-Hant,zh,zh-CN,zh-TW"); then
    message "Downloaded: $FOUND" "تمّ التنزيل: $FOUND"
    exit 0
fi

# Try human-written English subtitles.
message ">>> Trying human-written English subtitles…" ">>> جارٍ البحث عن ترجماتٍ نصّيّة بشريّة بالإنجليزيّة…"
if FOUND=$(try_download --write-subs "en,en-US,en-GB"); then
    message "Downloaded: $FOUND" "تمّ التنزيل: $FOUND"
    exit 0
fi

# Try automatic captions, with Chinese preferred.
message ">>> Trying automatic captions…" ">>> جارٍ البحث عن ترجماتٍ نصّيّة آليّة…"
if FOUND=$(try_download --write-auto-subs "zh-Hans,zh,en"); then
    message "Downloaded automatic captions: $FOUND" "تمّ تنزيل الترجمة النصّيّة الآليّة: $FOUND"
    exit 0
fi

message "No subtitles found." "لم يُعثَر على ترجماتٍ نصّيّة."
exit 1
