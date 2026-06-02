import os
from moviepy.editor import ColorClip, TextClip, AudioFileClip, CompositeVideoClip

def create_shorts_video():
    print("🚀 بدء عملية إنتاج الفيديو القصير...")
    
    # 1. إعدادات أبعاد الفيديو العمودي (Shorts / Reels) وتحديد المدة
    width, height = 1080, 1920
    duration = 15  # مدة الفيديو 15 ثانية
    
    # 2. إنشاء خلفية ملونة (تقدر تغير اللون بالـ HEX)
    # هنا اخترنا لون داكن ومميز يناسب الأجواء السينمائية وقنوات الـ AI
    background = ColorClip(size=(width, height), color=[15, 15, 25]).set_duration(duration)
    
    # 3. النص الذي سيظهر في الفيديو (يمكنك تعديله لأي نص تحبه)
    text_content = "النجاح ليس بمقدار ما تنجزه،\nبل بمقدار التحديات التي تتغلب عليها."
    
    # 4. إعدادات الخط والنص داخل الفيديو
    # ملاحظة: GitHub Actions يعمل على نظام Linux (Ubuntu)، وخط Amiri متوفر افتراضياً أو كخط قياسي
    text_clip = TextClip(
        txt=text_content,
        fontsize=50,
        color='white',
        font='Amiri-Regular',  # خط عربي أنيق ومتوفر في أنظمة سيرفرات GitHub
        align='Center',
        method='caption',
        size=(width - 200, None)  # ترك هوامش على الجوانب
    )
    
    # تحديد مكان النص في منتصف الشاشة وربطه بمدة الفيديو
    text_clip = text_clip.set_position('center').set_duration(duration)
    
    # 5. تجميع الفيديو النهائي (الخلفية + النص)
    video = CompositeVideoClip([background, text_clip])
    
    # 6. إضافة ملف صوتي (خلفية موسيقية أو صوت تعليق) إذا كان موجوداً
    # تأكد من رفع ملف صوتي باسم background_audio.mp3 في مشروعك لو أحببت تفعيله
    audio_file = "background_audio.mp3"
    if os.path.exists(audio_file):
        print(f"🎵 تم العثور على ملف الصوت {audio_file} وجاري دمجه...")
        audio = AudioFileClip(audio_file).subclip(0, duration)
        video = video.set_audio(audio)
    else:
        print("⚠️ لم يتم العثور على ملف background_audio.mp3، سيتم إنتاج الفيديو بدون صوت.")
    
    # 7. تصدير الفيديو النهائي بجودة عالية وبتنسيق مناسب للموبايل
    output_filename = "final_shorts_video.mp4"
    print(f"🎬 جاري رندر وتصدير الفيديو باسم: {output_filename}...")
    
    video.write_videofile(
        output_filename,
        fps=30,
        codec="libx264",
        audio_codec="aac",
        logger=None  # لإخفاء سطور التحميل الكثيرة في الـ Logs
    )
    
    print("🎉 تم إنتاج الفيديو بنجاح واكتمال العملية!")

if __name__ == "__main__":
    create_shorts_video()
