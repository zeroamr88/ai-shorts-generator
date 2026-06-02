import os
import sys
import re
from moviepy.editor import (
    ImageClip, VideoFileClip, AudioFileClip, CompositeAudioClip, 
    CompositeVideoClip, TextClip, concatenate_videoclips, vfx
)
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
from scipy.io import wavfile
import warnings
warnings.filterwarnings('ignore')

# مكتبات اختيارية للتعليق الصوتي
try:
    import pyttsx3
    HAS_PYTTSX3 = True
except ImportError:
    HAS_PYTTSX3 = False

try:
    from edge_tts import *
    HAS_EDGE_TTS = True
except ImportError:
    HAS_EDGE_TTS = False


def create_animated_background(width=1080, height=1920, duration=15, fps=30):
    """
    إنشاء خلفية متحركة احترافية بتدرجات لونية وحركة سلسة
    """
    print("🎬 جاري إنشاء خلفية متحركة احترافية...")
    
    try:
        frames = []
        total_frames = int(duration * fps)
        
        for frame_idx in range(total_frames):
            # إنشاء تدرج لوني يتحرك بناءً على الوقت
            progress = frame_idx / total_frames
            
            # تغيير الألوان بشكل ديناميكي (من أزرق داكن إلى بنفسجي)
            r_base = int(15 + (50 * np.sin(progress * 2 * np.pi)))
            g_base = int(15 + (30 * np.sin(progress * 2 * np.pi + np.pi/3)))
            b_base = int(50 + (100 * np.cos(progress * 2 * np.pi)))
            
            img = Image.new("RGB", (width, height))
            pixels = img.load()
            
            # إنشاء تدرج لوني مع حركة
            for y in range(height):
                for x in range(width):
                    # تأثير الموجات المتحركة
                    wave_effect = np.sin((x / width - progress) * 4 * np.pi) * 0.2
                    
                    r = max(0, min(255, int(r_base + wave_effect * 50)))
                    g = max(0, min(255, int(g_base + wave_effect * 30)))
                    b = max(0, min(255, int(b_base + wave_effect * 80)))
                    
                    # إضافة تدرج عمودي
                    vertical_gradient = int(255 * (y / height) * 0.3)
                    b = max(0, min(255, b + vertical_gradient))
                    
                    pixels[x, y] = (r, g, b)
            
            # تطبيق تأثير التمويه الخفيف لسلاسة أكثر
            img = img.filter(ImageFilter.GaussianBlur(radius=2))
            
            # حفظ الإطار مؤقتاً
            frame_path = f"temp_frames/frame_{frame_idx:04d}.png"
            os.makedirs("temp_frames", exist_ok=True)
            img.save(frame_path)
            frames.append(frame_path)
        
        print(f"✅ تم إنشاء {total_frames} إطار للخلفية المتحركة")
        return frames
    
    except Exception as e:
        print(f"⚠️ خطأ في إنشاء الخلفية المتحركة: {e}")
        return None


def create_voiceover(text_content, language="ar", output_path="voiceover.mp3"):
    """
    إنشاء تعليق صوتي من النص باستخدام Text-to-Speech
    يدعم العربية واللغات الأخرى
    """
    print(f"🎤 جاري إنشاء التعليق الصوتي بـ {language}...")
    
    try:
        # محاولة استخدام Edge TTS (أفضل للعربية)
        if HAS_EDGE_TTS:
            import asyncio
            
            # تحديد الصوت بناءً على اللغة
            voice_map = {
                "ar": "ar-SA-FadiyahNeural",  # صوت عربي أنثوي
                "en": "en-US-AriaNeural",
                "fr": "fr-FR-DeniseNeural"
            }
            
            voice = voice_map.get(language, "ar-SA-FadiyahNeural")
            
            async def generate_speech():
                communicate = Communicate(text_content, voice)
                await communicate.save(output_path)
            
            asyncio.run(generate_speech())
            print(f"✅ تم إنشاء التعليق الصوتي: {output_path}")
            return output_path
        
        # بديل: استخدام pyttsx3
        elif HAS_PYTTSX3:
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)  # سرعة الكلام
            engine.setProperty('volume', 0.9)
            engine.save_to_file(text_content, output_path)
            engine.runAndWait()
            print(f"✅ تم إنشاء التعليق الصوتي: {output_path}")
            return output_path
        
        else:
            print("⚠️ لم يتم العثور على مكتبات TTS، سيتم استخدام موسيقى خلفية فقط")
            return None
    
    except Exception as e:
        print(f"⚠️ خطأ في إنشاء التعليق الصوتي: {e}")
        return None


def create_background_music(duration=15, output_path="background_music.mp3", style="cinematic"):
    """
    إنشاء موسيقى خلفية احترافية بأنماط مختلفة
    """
    print(f"🎵 جاري إنشاء موسيقى خلفية ({style})...")
    
    try:
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration))
        
        if style == "cinematic":
            # موسيقى سينمائية هادئة
            freq1, freq2, freq3 = 110, 220, 330  # نغمات منخفضة هادئة
            wave1 = 0.2 * np.sin(2 * np.pi * freq1 * t)
            wave2 = 0.15 * np.sin(2 * np.pi * freq2 * t)
            wave3 = 0.1 * np.sin(2 * np.pi * freq3 * t)
        
        elif style == "ambient":
            # موسيقى محيطة هادئة
            freq1, freq2, freq3 = 100, 250, 400
            wave1 = 0.25 * np.sin(2 * np.pi * freq1 * t)
            wave2 = 0.15 * np.sin(2 * np.pi * freq2 * t)
            wave3 = 0.1 * np.sin(2 * np.pi * freq3 * t)
        
        else:
            # موسيقى احترافية عامة
            freq1, freq2, freq3 = 140, 280, 420
            wave1 = 0.3 * np.sin(2 * np.pi * freq1 * t)
            wave2 = 0.2 * np.sin(2 * np.pi * freq2 * t)
            wave3 = 0.15 * np.sin(2 * np.pi * freq3 * t)
        
        # إضافة Envelope (يبدأ تدريجياً وينتهي تدريجياً)
        envelope = np.linspace(0, 1, len(t) // 4)
        envelope = np.concatenate([
            envelope,
            np.ones(len(t) // 2),
            np.linspace(1, 0, len(t) - len(t) // 4 - len(t) // 2)
        ])
        
        # الدمج النهائي مع تأثير FX
        audio = (wave1 + wave2 + wave3) * envelope * 0.3
        audio = audio / np.max(np.abs(audio)) * 0.8  # تطبيع
        
        # حفظ كـ WAV
        wav_path = "temp_music.wav"
        wavfile.write(wav_path, sample_rate, (audio * 32767).astype(np.int16))
        
        # تحويل إلى MP3
        cmd = f"ffmpeg -i {wav_path} -q:a 9 -n {output_path} 2>/dev/null"
        os.system(cmd)
        
        if os.path.exists(wav_path):
            os.remove(wav_path)
        
        print(f"✅ تم إنشاء الموسيقى الخلفية: {output_path}")
        return output_path
    
    except Exception as e:
        print(f"⚠️ خطأ في إنشاء الموسيقى: {e}")
        return None


def create_animated_text_clips(text_content, duration, width=1080, height=1920, fps=30):
    """
    إنشاء نصوص متحركة تظهر كلمة بكلمة مع تأثيرات احترافية
    """
    print("✨ جاري إنشاء نصوص متحركة...")
    
    try:
        # تقسيم النص إلى جمل
        sentences = [s.strip() for s in text_content.split('\n') if s.strip()]
        
        # توزيع الجمل على مدة الفيديو
        time_per_sentence = duration / len(sentences) if sentences else duration
        
        text_clips = []
        
        for idx, sentence in enumerate(sentences):
            start_time = idx * time_per_sentence
            end_time = (idx + 1) * time_per_sentence
            
            # إنشاء TextClip مع تأثيرات
            txt_clip = TextClip(
                sentence,
                fontsize=80,
                font="Arial-Bold",
                color="white",
                method="caption",
                size=(width - 100, None),
                align="center",
                stroke_color="black",
                stroke_width=3
            ).set_duration(time_per_sentence).set_start(start_time)
            
            # إضافة تأثير Fade-in و Fade-out
            txt_clip = txt_clip.crossfadeout(0.3).crossfadein(0.3)
            
            # وضع النص في منتصف الشاشة
            txt_clip = txt_clip.set_position("center")
            
            text_clips.append(txt_clip)
        
        print(f"✅ تم إنشاء {len(text_clips)} مقاطع نصية متحركة")
        return text_clips
    
    except Exception as e:
        print(f"⚠️ خطأ في إنشاء النصوص المتحركة: {e}")
        return []


def load_font(size=45):
    """
    تحميل خط عربي احترافي
    """
    font_paths = [
        "/usr/share/fonts/truetype/noto/NotoSansBold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/System/Library/Fonts/Arial.ttf",  # macOS
        "C:\\Windows\\Fonts\\arial.ttf",  # Windows
    ]
    
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, size)
            except:
                continue
    
    return ImageFont.load_default()


def create_shorts_video_enhanced(
    text_content="النجاح ليس بمقدار ما تنجزه،\nبل بمقدار التحديات التي تتغلب عليها.",
    width=1080,
    height=1920,
    duration=15,
    fps=30,
    output_filename="final_shorts_video.mp4",
    enable_voiceover=True,
    enable_animated_bg=True,
    enable_animated_text=True,
    music_style="cinematic"
):
    """
    إنشاء فيديو قصير احترافي مع جميع الخصائص المتقدمة
    """
    try:
        print("\n" + "="*70)
        print("🎬 منشئ الفيديوهات القصيرة AI Shorts - النسخة المتقدمة")
        print("="*70)
        print(f"📐 الأبعاد: {width}x{height}")
        print(f"⏱️ المدة: {duration} ثانية")
        print(f"🎨 خلفية متحركة: {'✅' if enable_animated_bg else '❌'}")
        print(f"✨ نصوص متحركة: {'✅' if enable_animated_text else '❌'}")
        print(f"🎤 تعليق صوتي: {'✅' if enable_voiceover else '❌'}")
        print("="*70 + "\n")
        
        # 1. إنشاء الخلفية (متحركة أو ثابتة)
        if enable_animated_bg:
            print("🎨 جاري إنشاء خلفية متحركة احترافية...")
            background_clip = None  # سيتم إنشاؤها لاحقاً
        else:
            print("🎨 جاري إنشاء خلفية ثابتة...")
            bg_color = (15, 15, 50)
            img = Image.new("RGB", (width, height), bg_color)
            img.save("temp_bg.png")
            background_clip = ImageClip("temp_bg.png").set_duration(duration)
        
        # 2. إنشاء الموسيقى الخلفية
        background_music_path = create_background_music(
            duration=duration,
            output_path="background_music.mp3",
            style=music_style
        )
        
        # 3. إنشاء التعليق الصوتي (اختياري)
        voiceover_path = None
        if enable_voiceover:
            voiceover_path = create_voiceover(text_content, language="ar", output_path="voiceover.mp3")
        
        # 4. إنشاء النصوص المتحركة
        text_clips = []
        if enable_animated_text:
            text_clips = create_animated_text_clips(text_content, duration, width, height, fps)
        
        # 5. دمج الفيديو والصوت والنصوص
        print("\n💾 جاري دمج جميع العناصر...")
        
        # إنشاء الفيديو الأساسي
        if background_clip is None:
            # استخدام الخلفية المتحركة
            print("🔄 جاري دمج الإطارات...")
            frame_files = sorted([f for f in os.listdir("temp_frames") if f.endswith(".png")])
            if frame_files:
                frame_clips = [
                    ImageClip(f"temp_frames/{f}").set_duration(1/fps)
                    for f in frame_files
                ]
                background_clip = concatenate_videoclips(frame_clips)
        
        # إضافة النصوص المتحركة
        if text_clips:
            final_video = CompositeVideoClip(
                [background_clip] + text_clips,
                size=(width, height)
            )
        else:
            final_video = background_clip
        
        # دمج الصوت
        audio_clips = []
        
        if background_music_path and os.path.exists(background_music_path):
            bg_audio = AudioFileClip(background_music_path)
            if bg_audio.duration > duration:
                bg_audio = bg_audio.subclip(0, duration)
            audio_clips.append(bg_audio.volumex(0.5))  # خفض الموسيقى قليلاً
        
        if voiceover_path and os.path.exists(voiceover_path):
            voiceover_audio = AudioFileClip(voiceover_path)
            if voiceover_audio.duration > duration:
                voiceover_audio = voiceover_audio.subclip(0, duration)
            audio_clips.append(voiceover_audio.volumex(1.0))  # مستوى عادي للتعليق
        
        if audio_clips:
            final_audio = CompositeAudioClip(audio_clips)
            final_video = final_video.set_audio(final_audio)
        
        # 6. تصدير الفيديو النهائي
        print(f"\n🎬 جاري تصدير الفيديو النهائي...")
        print(f"📁 الملف: {output_filename}")
        print(f"⏳ جاري المعالجة (قد يستغرق عدة دقائق)...\n")
        
        final_video.write_videofile(
            output_filename,
            fps=fps,
            codec="libx264",
            audio_codec="aac",
            verbose=False,
            logger=None
        )
        
        # 7. تنظيف الملفات المؤقتة
        print("\n🗑️ جاري تنظيف الملفات المؤقتة...")
        import shutil
        
        temp_files = ["temp_bg.png", "background_music.mp3", "voiceover.mp3", "temp_music.wav"]
        for f in temp_files:
            if os.path.exists(f):
                os.remove(f)
        
        if os.path.exists("temp_frames"):
            shutil.rmtree("temp_frames")
        
        print("✅ تم التنظيف")
        
        # 8. عرض النتائج
        print("\n" + "="*70)
        print(f"🎉 مبروك! تم إنتاج الفيديو بنجاح!")
        print(f"="*70)
        print(f"📊 معلومات الملف:")
        print(f"   📁 الاسم: {output_filename}")
        print(f"   💾 الحجم: {os.path.getsize(output_filename) / (1024*1024):.2f} MB")
        print(f"   📐 الدقة: {width}x{height}")
        print(f"   🎬 معدل الإطارات: {fps} FPS")
        print(f"   ⏱️ المدة: {duration} ثانية")
        print("="*70 + "\n")
        
        return output_filename
    
    except Exception as e:
        print(f"❌ خطأ أثناء إنتاج الفيديو: {e}")
        import traceback
        traceback.print_exc()
        return None


def main():
    """
    الدالة الرئيسية مع خيارات متقدمة
    """
    import argparse
    
    parser = argparse.ArgumentParser(
        description="إنشاء فيديو قصير احترافي مع خصائص متقدمة",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
أمثلة الاستخدام:
  python generate_video_enhanced.py
  python generate_video_enhanced.py --text "نص مختلف" --duration 20
  python generate_video_enhanced.py --text "النجاح" --output "my_video.mp4" --no-voiceover
  python generate_video_enhanced.py --text "حكمة" --music-style cinematic --enable-animated-text
        """
    )
    
    parser.add_argument("--text", type=str,
                       default="النجاح ليس بمقدار ما تنجزه،\nبل بمقدار التحديات التي تتغلب عليها.",
                       help="النص المراد عرضه")
    parser.add_argument("--duration", type=int, default=15,
                       help="مدة الفيديو بالثواني (افتراضي: 15)")
    parser.add_argument("--output", type=str, default="final_shorts_video.mp4",
                       help="اسم ملف الإخراج")
    parser.add_argument("--fps", type=int, default=30,
                       help="عدد الإطارات في الثانية")
    parser.add_argument("--no-animated-bg", action="store_true",
                       help="تعطيل الخلفية المتحركة")
    parser.add_argument("--no-voiceover", action="store_true",
                       help="تعطيل التعليق الصوتي")
    parser.add_argument("--no-animated-text", action="store_true",
                       help="تعطيل النصوص المتحركة")
    parser.add_argument("--music-style", type=str, default="cinematic",
                       choices=["cinematic", "ambient", "professional"],
                       help="نمط الموسيقى الخلفية")
    
    args = parser.parse_args()
    
    create_shorts_video_enhanced(
        text_content=args.text,
        duration=args.duration,
        output_filename=args.output,
        fps=args.fps,
        enable_animated_bg=not args.no_animated_bg,
        enable_voiceover=not args.no_voiceover,
        enable_animated_text=not args.no_animated_text,
        music_style=args.music_style
    )


if __name__ == "__main__":
    main()
