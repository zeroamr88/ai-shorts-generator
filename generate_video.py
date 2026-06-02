import os
from moviepy.editor import ImageClip, AudioFileClip
from PIL import Image, ImageDraw, ImageFont

def create_shorts_video():
    print("🚀 بدء عملية إنتاج الفيديو القصير باستخدام Pillow البديلة...")
    
    width, height = 1080, 1920
    duration = 15
    
    # 1. إنشاء صورة خلفية داكنة تناسب "Dreamy ai Shorts" باستخدام Pillow
    bg_color = (15, 15, 25)
    image = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(image)
    
    # 2. تحديد النص
    text_content = "النجاح ليس بمقدار ما تنجزه،\nبل بمقدار التحديات التي تتغلب عليها."
    
    # 3. محاولة تحميل خط مناسب، وإذا لم يتوفر نستخدم الخط الافتراضي
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    if os.path.exists(font_path):
        font = ImageFont.truetype(font_path, 45)
    else:
        font = ImageFont.load_default()
        
    # 4. كتابة النص في منتصف الصورة
    # حساب أبعاد النص لتوسيطه
    text_boxes = [draw.textbbox((0, 0), line, font=font) for line in text_content.split('\n')]
    line_heights = [box[3] - box[1] for box in text_boxes]
    total_height = sum(line_heights) + (len(line_heights) - 1) * 20
    
    current_y = (height - total_height) // 2
    for line in text_content.split('\n'):
        box = draw.textbbox((0, 0), line, font=font)
        w = box[2] - box[0]
        x = (width - w) // 2
        draw.text((x, current_y), line, fill="white", font=font)
        current_y += (box[3] - box[1]) + 20
        
    # 5. حفظ الصورة مؤقتاً
    temp_image_path = "temp_background.png"
    image.save(temp_image_path)
    
    # 6. تحويل الصورة إلى مقطع فيديو باستخدام MoviePy بدون استخدام TextClip نهائياً!
    video = ImageClip(temp_image_path).set_duration(duration)
    
    # 7. دمج الصوت لو متاح
    audio_file = "background_audio.mp3"
    if os.path.exists(audio_file):
        print(f"🎵 تم دمج الصوت: {audio_file}")
        audio = AudioFileClip(audio_file).subclip(0, duration)
        video = video.set_audio(audio)
        
    # 8. تصدير الفيديو النهائي
    output_filename = "final_shorts_video.mp4"
    print(f"🎬 جاري رندر وتصدير الفيديو: {output_filename}...")
    video.write_videofile(output_filename, fps=30, codec="libx264", audio_codec="aac", logger=None)
    
    # تنظيف الملف المؤقت
    if os.path.exists(temp_image_path):
        os.remove(temp_image_path)
        
    print("🎉 مبروك! تم إنتاج الفيديو بنجاح واكتمال العملية بدون أي أخطاء!")

if __name__ == "__main__":
    create_shorts_video()
