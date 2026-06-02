## 🎬 AI Shorts Generator - النسخة المحسّنة

منشئ فيديوهات قصيرة احترافية مع دعم العربية والعديد من الخصائص المتقدمة.

---

## ✨ الخصائص الرئيسية

### 🎨 خصائص الفيديو المحسّنة

#### 1️⃣ **خلفية متحركة احترافية** (Animated Backgrounds)
- بدلاً من اللون الأزرق الثابت، الآن لديك خلفية متحركة **سينمائية**
- تدرجات لونية ديناميكية تتحرك بسلاسة طوال الفيديو
- تأثيرات موجية وحركة احترافية
- دعم أنماط مختلفة (Cinematic, Ambient, Professional)

#### 2️⃣ **نصوص متحركة مع تأثيرات** (Animated Text)
- النص يظهر **كلمة بكلمة** بدلاً من البقاء ثابتاً
- تأثيرات **Fade-in** و **Fade-out** احترافية
- تحديد أسود للخط (stroke) لوضوح أفضل
- خطوط عربية واحترافية بحجم كبير

#### 3️⃣ **تعليق صوتي ذكي** (AI Voiceover)
- تحويل النص إلى **صوت احترافي بصوت بشري**
- دعم **اللغة العربية** بشكل احترافي
- استخدام `edge-tts` للأصوات الطبيعية والسلسة
- المزج التلقائي بين التعليق الصوتي والموسيقى الخلفية

#### 4️⃣ **موسيقى خلفية احترافية**
- موسيقى **سينمائية هادئة** (Cinematic)
- موسيقى **محيطة هادئة** (Ambient)
- دعم أنماط متعددة مع تأثيرات صوتية احترافية
- خفض تلقائي للموسيقى عند وجود تعليق صوتي

---

## 🚀 البدء السريع

### التثبيت

```bash
# 1. استنساخ المشروع
git clone https://github.com/zeroamr88/ai-shorts-generator.git
cd ai-shorts-generator

# 2. تثبيت المتطلبات
pip install -r requirements.txt

# 3. تثبيت ffmpeg (مطلوب)
# على Ubuntu/Debian:
sudo apt-get install ffmpeg

# على macOS:
brew install ffmpeg

# على Windows:
# اتبع: https://ffmpeg.org/download.html
```

### الاستخدام الأساسي

```bash
# إنشاء فيديو بالإعدادات الافتراضية
python generate_video_enhanced.py

# إنشاء فيديو بنص مخصص
python generate_video_enhanced.py --text "حكمتك اليوم\nستكون قوتك غداً"

# إنشاء فيديو بمدة أطول
python generate_video_enhanced.py --text "نصك" --duration 20

# تخصيص شامل
python generate_video_enhanced.py \
  --text "النجاح\nهو المثابرة" \
  --duration 20 \
  --output my_shorts.mp4 \
  --fps 60 \
  --music-style cinematic \
  --enable-animated-text
```

---

## 📋 خيارات سطر الأوامر

### الخيارات الأساسية

| الخيار | الوصف | القيمة الافتراضية |
|--------|-------|------------------|
| `--text` | النص المراد عرضه | "النجاح ليس بمقدار..." |
| `--duration` | مدة الفيديو بالثواني | 15 |
| `--output` | اسم ملف الإخراج | final_shorts_video.mp4 |
| `--fps` | عدد الإطارات في الثانية | 30 |

### خيارات التأثيرات

| الخيار | الوصف |
|--------|-------|
| `--no-animated-bg` | تعطيل الخلفية المتحركة |
| `--no-voiceover` | تعطيل التعليق الصوتي |
| `--no-animated-text` | تعطيل النصوص المتحركة |
| `--music-style` | نمط الموسيقى: `cinematic`, `ambient`, `professional` |

---

## 💡 أمثلة الاستخدام

### مثال 1: فيديو تحفيزي بسيط
```bash
python generate_video_enhanced.py \
  --text "لا تستسلم\nالحلم يحتاج صبر" \
  --duration 15 \
  --music-style cinematic
```

### مثال 2: فيديو طويل بدون صوت
```bash
python generate_video_enhanced.py \
  --text "حكمة اليوم" \
  --duration 30 \
  --no-voiceover \
  --fps 60
```

### مثال 3: فيديو بخلفية ثابتة فقط
```bash
python generate_video_enhanced.py \
  --text "نصك هنا" \
  --no-animated-bg \
  --no-animated-text
```

### مثال 4: فيديو احترافي كامل
```bash
python generate_video_enhanced.py \
  --text "النجاح\nليس بالصدفة\nإنه بالاختيار" \
  --duration 20 \
  --output professional_shorts.mp4 \
  --fps 60 \
  --music-style cinematic
```

---

## 🎯 الميزات المتقدمة

### الخلفية المتحركة

```python
from generate_video_enhanced import create_shorts_video_enhanced

# إنشاء فيديو مع خلفية متحركة كاملة
create_shorts_video_enhanced(
    text_content="نصك هنا",
    enable_animated_bg=True,  # ✅ تفعيل الخلفية المتحركة
    duration=15
)
```

### التعليق الصوتي

```python
# إنشاء فيديو مع تعليق صوتي بالعربية
create_shorts_video_enhanced(
    text_content="مرحباً بك في عالم الإمكانيات",
    enable_voiceover=True,  # ✅ تفعيل التعليق الصوتي
    duration=15
)
```

### النصوص المتحركة

```python
# إنشاء فيديو بنصوص تظهر بتأثيرات احترافية
create_shorts_video_enhanced(
    text_content="النجاح\nهو الهدف",
    enable_animated_text=True,  # ✅ تفعيل النصوص المتحركة
    duration=15
)
```

---

## 🔧 البنية الداخلية للملفات

```
generate_video_enhanced.py
├── create_animated_background()      # إنشاء خلفية متحركة
├── create_voiceover()                # تحويل النص إلى صوت
├── create_background_music()         # إنشاء موسيقى خلفية
├── create_animated_text_clips()      # إنشاء نصوص متحركة
└── create_shorts_video_enhanced()    # الدالة الرئيسية
```

---

## 📊 المتطلبات

### البرامج المطلوبة
- ✅ Python 3.8+
- ✅ FFmpeg (للمعالجة الصوتية والفيديو)

### مكتبات Python
```
moviepy==1.0.3          # معالجة الفيديو
pillow==10.1.0          # معالجة الصور
numpy==1.24.3           # الحسابات الرياضية
scipy==1.11.4           # معالجة الصوت
edge-tts==6.1.9         # تحويل النص إلى صوت (عربي)
pyttsx3==2.90           # بديل TTS
```

---

## 🎨 نصائح للحصول على أفضل النتائج

### 1. النصوص
- استخدم **جملاً قصيرة وواضحة**
- فصل الجمل بـ `\n` للظهور على أسطر منفصلة
- **تجنب النصوص الطويلة جداً**

### 2. المدة
- **15-20 ثانية**: مثالية لمنصات التواصل
- **30-45 ثانية**: للمحتوى الأكثر تفصيلاً
- **استخدم --fps 60** للجودة الأعلى (ملفات أكبر)

### 3. الموسيقى
- **cinematic**: موسيقى سينمائية احترافية (الأفضل للحكم والاقتباسات)
- **ambient**: موسيقى هادئة ومحيطة (جيدة للتأمل)
- **professional**: موسيقى احترافية عامة

### 4. التأثيرات
- استخدم **--enable-animated-text** مع نصوص قصيرة فقط
- استخدم **--no-voiceover** إذا كنت ستضيف صوتاً خارجياً
- جرّب **--no-animated-bg** للنتائج الأسرع

---

## 🐛 استكشاف الأخطاء

### المشكلة: "ffmpeg not found"
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg

# Windows - اتبع التعليمات من: https://ffmpeg.org/download.html
```

### المشكلة: "Edge-TTS not working"
```bash
# تأكد من الاتصال بالإنترنت
# أعد تثبيت المكتبة
pip install --upgrade edge-tts
```

### المشكلة: "الفيديو بطيء في الإنشاء"
```bash
# استخدم FPS أقل
python generate_video_enhanced.py --fps 24

# أو عطّل الخلفية المتحركة
python generate_video_enhanced.py --no-animated-bg
```

---

## 📈 مقارنة النسخ

| الميزة | النسخة الأصلية | النسخة المحسّنة |
|-------|----------------|-----------------|
| خلفية متحركة | ❌ | ✅ |
| تعليق صوتي | ❌ | ✅ |
| نصوص متحركة | ❌ | ✅ |
| موسيقى احترافية | ✅ | ✅ محسّنة |
| خيارات متقدمة | ❌ | ✅ |
| دعم عربي | ✅ | ✅ محسّن |

---

## 📁 الملفات المُنتجة

عند تشغيل السكريبت، سيتم إنشاء:

```
📦 المشروع
├── final_shorts_video.mp4       # الفيديو النهائي
├── voiceover.mp3                # التعليق الصوتي (إن وجد)
├── background_music.mp3         # الموسيقى الخلفية
└── temp_frames/                 # إطارات مؤقتة (يتم حذفها تلقائياً)
```

---

## 📝 الترخيص

هذا المشروع مرخص تحت [MIT License](LICENSE)

---

## 🙏 المساهمة

نرحب بالمساهمات! يرجى:

1. Fork المشروع
2. إنشاء فرع جديد (`git checkout -b feature/amazing-feature`)
3. Commit التغييرات (`git commit -m 'Add amazing feature'`)
4. Push إلى الفرع (`git push origin feature/amazing-feature`)
5. فتح Pull Request

---

## 📧 الدعم

للمزيد من المساعدة أو الإبلاغ عن أخطاء، يرجى فتح [Issue](https://github.com/zeroamr88/ai-shorts-generator/issues) على GitHub.

---

## 🌟 استمتع بإنشاء الفيديوهات الاحترافية!

**Made with ❤️ by zeroamr88**
