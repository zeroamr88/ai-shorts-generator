import os
import sys
from moviepy.editor import ImageClip, AudioFileClip, CompositeAudioClip
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from scipy.io import wavfile
from scipy import signal

def create_background_audio(duration=15, output_path="background_audio.mp3"):
    """
    إنشاء موسيقى خلفية هادئة تلقائياً باستخدام موجات صوتية
    """
    print("🎵 جاري إنشاء الموسيقى الخلفية...")
    
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # إنشاء موجات صوتية هادئة وسلسة
    freq1, freq2, freq3 = 140, 280, 420  # تكرارات موسيقية هادئة
    
    # دمج موجات صوتية متعددة للحصول على صوت موسيقي
    wave1 = 0.3 * np.sin(2 * np.pi * freq1 * t)
    wave2 = 0.2 * np.sin(2 * np.pi * freq2 * t)
    wave3 = 0.15 * np.sin(2 * np.pi * freq3 * t)
    
    # إضافة envelope للصوت (يبدأ منخفض وينتهي منخفض)
    envelope = np.linspace(0, 1, len(t) // 2)
    envelope = np.concatenate([envelope, np.linspace(1, 0, len(t) - len(t) // 2)])
    
    # الدمج النهائي
    audio = (wave1 + wave2 + wave3) * envelope * 0.3
    
    # تطبيع الصوت
    audio = audio / np.max(np.abs(audio)) * 0.9
    
    # حفظ كـ WAV ثم تحويله إلى MP3
    wav_path = "temp_audio.wav"
    wavfile.write(wav_path, sample_rate, (audio * 32767).astype(np.int16))
    
    # تحويل WAV إلى MP3
    os.system(f"ffmpeg -i {wav_path} -q:a 9 -n {output_path} 2>/dev/null")
    
    # حذف الملف المؤقت
    if os.path.exists(wav_path):
        os.remove(wav_path)
    
    print(f"✅ تم إنشاء الموسيقى الخلفية: {output_path}")
    return output_path

def load_font(size=45):
    """
    تحميل خط مناسب مع دعم اللغة العربية
    """
    font_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/System/Library/Fonts/Arial.ttf",  # macOS
        "C:\\Windows\\Fonts\\arial.ttf",  # Windows
        "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
    ]
    
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, size)
            except:
                continue
    
    return ImageFont.load_default()

def create_shorts_video(
    text_content="النجاح ليس بمقدار ما تنجزه،\nبل بمقدار التحديات التي تتغلب عليها.",
    width=1080,
    height=1920,
    duration=15,
    bg_color=(15, 15, 25),
    text_color="white",
    font_size=45,
    fps=30,
    output_filename="final_shorts_video.mp4"
):
    """
    إنشاء فيديو قصير احترافي مع جميع الخيارات المتقدمة
    """
    try:
        print("🚀 بدء عملية إنتاج الفيديو القصير...")
        print(f"📐 الأبعاد: {width}x{height}")
        print(f"⏱️ المدة: {duration} ثانية")
        
        # 1. التحقق من الملفات المطلوبة وإنشاء الصوت إن لزم الحال
        audio_file = "background_audio.mp3"
        if not os.path.exists(audio_file):
            print("⚠️ لم يتم العثور على ملف الصوت، جاري إنشاء واحد جديد...")
            create_background_audio(duration, audio_file)
        
        # 2. إنشاء صورة خلفية داكنة
        print("🎨 جاري إنشاء الخلفية...")
        image = Image.new("RGB", (width, height), bg_color)
        draw = ImageDraw.Draw(image)
        
        # 3. تحميل الخط
        font = load_font(font_size)
        
        # 4. كتابة النص في منتصف الصورة
        print("✍️ جاري إضافة النص...")
        text_boxes = [draw.textbbox((0, 0), line, font=font) for line in text_content.split('\n')]
        line_heights = [box[3] - box[1] for box in text_boxes]
        total_height = sum(line_heights) + (len(line_heights) - 1) * 20
        
        current_y = (height - total_height) // 2
        for line in text_content.split('\n'):
            box = draw.textbbox((0, 0), line, font=font)
            w = box[2] - box[0]
            x = (width - w) // 2
            draw.text((x, current_y), line, fill=text_color, font=font)
            current_y += (box[3] - box[1]) + 20
        
        # 5. حفظ الصورة مؤقتاً
        temp_image_path = "temp_background.png"
        image.save(temp_image_path)
        print(f"✅ تم حفظ الخلفية مؤقتاً")
        
        # 6. تحويل الصورة إلى مقطع فيديو
        print("🎬 جاري إنشاء الفيديو...")
        video = ImageClip(temp_image_path).set_duration(duration)
        
        # 7. دمج الصوت
        if os.path.exists(audio_file):
            print(f"🎵 جاري دمج الصوت: {audio_file}")
            try:
                audio = AudioFileClip(audio_file)
                # إذا كان الصوت أطول من المدة المطلوبة
                if audio.duration > duration:
                    audio = audio.subclip(0, duration)
                # إذا كان الصوت أقصر نكرره
                elif audio.duration < duration:
                    num_repeats = int(duration / audio.duration) + 1
                    audio = CompositeAudioClip([audio.set_start(i * audio.duration) 
                                               for i in range(num_repeats)]).set_duration(duration)
                video = video.set_audio(audio)
                print("✅ تم دمج الصوت بنجاح")
            except Exception as e:
                print(f"⚠️ خطأ في دمج الصوت: {e}")
        
        # 8. تصدير الفيديو النهائي
        print(f"💾 جاري تصدير الفيديو: {output_filename}...")
        video.write_videofile(
            output_filename,
            fps=fps,
            codec="libx264",
            audio_codec="aac",
            verbose=False,
            logger=None
        )
        
        # تنظيف الملفات المؤقتة
        if os.path.exists(temp_image_path):
            os.remove(temp_image_path)
        
        print(f"🎉 مبروك! تم إنتاج الفيديو بنجاح: {output_filename}")
        return output_filename
        
    except Exception as e:
        print(f"❌ خطأ أثناء إنتاج الفيديو: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    """
    الدالة الرئيسية مع خيارات سطر الأوامر
    """
    import argparse
    
    parser = argparse.ArgumentParser(description="إنشاء فيديو قصير احترافي مع نصوص وصوت")
    parser.add_argument("--text", type=str, 
                       default="النجاح ليس بمقدار ما تنجزه،\nبل بمقدار التحديات التي تتغلب عليها.",
                       help="النص المراد عرضه")
    parser.add_argument("--duration", type=int, default=15, help="مدة الفيديو بالثواني")
    parser.add_argument("--width", type=int, default=1080, help="عرض الفيديو")
    parser.add_argument("--height", type=int, default=1920, help="ارتفاع الفيديو")
    parser.add_argument("--font-size", type=int, default=45, help="حجم الخط")
    parser.add_argument("--output", type=str, default="final_shorts_video.mp4", help="اسم ملف الإخراج")
    parser.add_argument("--fps", type=int, default=30, help="عدد الإطارات في الثانية")
    parser.add_argument("--bg-color", type=str, default="15,15,25", help="لون الخلفية RGB")
    parser.add_argument("--text-color", type=str, default="white", help="لون النص")
    
    args = parser.parse_args()
    
    # تحويل لون الخلفية
    try:
        bg_color = tuple(map(int, args.bg_color.split(',')))
    except:
        bg_color = (15, 15, 25)
    
    # إنشاء الفيديو
    create_shorts_video(
        text_content=args.text,
        width=args.width,
        height=args.height,
        duration=args.duration,
        bg_color=bg_color,
        text_color=args.text_color,
        font_size=args.font_size,
        fps=args.fps,
        output_filename=args.output
    )

if __name__ == "__main__":
    main()
