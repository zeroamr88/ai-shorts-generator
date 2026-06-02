# 🎬 منشئ الفيديوهات القصيرة AI Shorts

فيديوهات قصيرة احترافية مع نصوص عربية وموسيقى خلفية تلقائية!

## 📋 المتطلبات

- Python 3.8+
- FFmpeg (مثبت على النظام)

## 🚀 التثبيت

```bash
# تثبيت المكتبات
pip install -r requirements.txt

# تثبيت FFmpeg (إذا لم يكن مثبتاً)
# على Ubuntu/Debian:
sudo apt-get install ffmpeg

# على macOS:
brew install ffmpeg

# على Windows:
choco install ffmpeg
```

## 💻 طرق الاستخدام

### 1️⃣ التشغيل المباشر (بالإعدادات الافتراضية)

```bash
python generate_video.py
```

### 2️⃣ مع تخصيص الخيارات

```bash
python generate_video.py \
    --text "نصك هنا" \
    --duration 20 \
    --output "my_video.mp4" \
    --font-size 50 \
    --fps 60
```

### 3️⃣ كل الخيارات المتاحة

```bash
python generate_video.py \
    --text "النجاح حقيقي" \
    --duration 15                    # مدة الفيديو بالثواني
    --width 1080                     # عرض الفيديو
    --height 1920                    # ارتفاع الفيديو
    --font-size 45                   # حجم الخط
    --fps 30                         # عدد الإطارات في الثانية
    --output "final.mp4"             # اسم الملف الناتج
    --bg-color "15,15,25"            # لون الخلفية (R,G,B)
    --text-color "white"             # لون النص
```

## 📝 الميزات

✅ **إنشاء موسيقى خلفية تلقائياً** - لا تحتاج لملف صوتي منفصل
✅ **دعم كامل اللغة العربية** - نصوص عربية بدون مشاكل
✅ **خيارات متقدمة** - تخصيص كامل للفيديو
✅ **معالجة الأخطاء** - رسائل واضحة وسهلة الفهم
✅ **جودة عالية** - H.264 codec و 30 FPS
✅ **سهل الاستخدام** - يعمل بأمر واحد

## 📂 الملفات المُنتجة

- `final_shorts_video.mp4` - الفيديو النهائي
- `background_audio.mp3` - الموسيقى الخلفية (تُحفظ للاستخدام المستقبلي)
- `temp_background.png` - خلفية مؤقتة (تُحذف تلقائياً)

## 🔧 استكشاف الأخطاء

### المشكلة: "ffmpeg not found"
**الحل:** ثبت FFmpeg على نظامك

### المشكلة: خطأ في الخطوط العربية
**الحل:** السكريبت يختار أفضل خط متاح تلقائياً

### المشكلة: الفيديو بطيء جداً
**الحل:** قلل حجم الفيديو أو قيمة fps:
```bash
python generate_video.py --width 720 --height 1280 --fps 24
```

## 📊 أمثلة الاستخدام

### إنشاء فيديو بنص مختلف:
```bash
python generate_video.py --text "أحلام عظيمة تحتاج إلى عمل عظيم"
```

### فيديو أطول:
```bash
python generate_video.py --duration 30
```

### فيديو بجودة أعلى:
```bash
python generate_video.py --fps 60 --width 1440 --height 2560
```

## 📧 الدعم والمساهمة

شارك ملاحظاتك وتحسيناتك!

---

**صُنع بـ ❤️ لإنشاء محتوى رائع**
