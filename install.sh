#!/bin/bash

# سكريبت التثبيت السريع لمنشئ الفيديوهات القصيرة

echo "========================================="
echo "🎬 منشئ الفيديوهات القصيرة AI Shorts"
echo "========================================="
echo ""

# التحقق من Python
echo "✅ التحقق من Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 غير مثبت. يرجى تثبيت Python 3.8 أو أحدث"
    exit 1
fi
echo "✅ Python مثبت"

# التحقق من FFmpeg
echo "✅ التحقق من FFmpeg..."
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  FFmpeg غير مثبت. سيتم محاولة التثبيت..."
    
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get update
        sudo apt-get install -y ffmpeg
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install ffmpeg
    else
        echo "⚠️  يرجى تثبيت FFmpeg يدويًا من: https://ffmpeg.org/download.html"
    fi
else
    echo "✅ FFmpeg مثبت"
fi

# تثبيت المكتبات
echo ""
echo "📦 تثبيت المكتبات المطلوبة..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo ""
echo "========================================="
echo "✅ تم التثبيت بنجاح!"
echo "========================================="
echo ""
echo "🚀 للبدء، استخدم أحد الأوامر التالية:"
echo ""
echo "  التشغيل الافتراضي:"
echo "  python3 generate_video.py"
echo ""
echo "  مع خيارات مخصصة:"
echo "  python3 generate_video.py --text \"نصك هنا\" --duration 20"
echo ""
echo "  للمساعدة:"
echo "  python3 generate_video.py --help"
echo ""
