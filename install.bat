@echo off
REM سكريبت التثبيت السريع لنظام Windows

echo =========================================
echo 🎬 منشئ الفيديوهات القصيرة AI Shorts
echo =========================================
echo.

REM التحقق من Python
echo ✅ التحقق من Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python غير مثبت. يرجى تثبيت Python 3.8 أو أحدث
    pause
    exit /b 1
)
echo ✅ Python مثبت

REM التحقق من FFmpeg
echo ✅ التحقق من FFmpeg...
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  FFmpeg غير مثبت
    echo يرجى تثبيت FFmpeg من: https://ffmpeg.org/download.html
    echo أو استخدم: choco install ffmpeg
) else (
    echo ✅ FFmpeg مثبت
)

REM تثبيت المكتبات
echo.
echo 📦 تثبيت المكتبات المطلوبة...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
echo =========================================
echo ✅ تم التثبيت بنجاح!
echo =========================================
echo.
echo 🚀 للبدء، استخدم أحد الأوامر التالية:
echo.
echo   التشغيل الافتراضي:
echo   python generate_video.py
echo.
echo   مع خيارات مخصصة:
echo   python generate_video.py --text "نصك هنا" --duration 20
echo.
echo   للمساعدة:
echo   python generate_video.py --help
echo.
pause
