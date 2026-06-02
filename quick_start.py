#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🎬 دليل الاستخدام السريع - AI Shorts Generator Enhanced
Quick Start Guide for creating professional AI-generated short videos

نسخة سريعة وسهلة لإنشاء فيديوهات احترافية مع جميع الخصائص الجديدة
"""

from generate_video_enhanced import create_shorts_video_enhanced
import sys

# ============================================================================
# أمثلة جاهزة للاستخدام الفوري
# ============================================================================

# مثال 1: فيديو تحفيزي بسيط
def example_motivational():
    """فيديو تحفيزي مع جميع الخصائص"""
    print("🚀 مثال 1: فيديو تحفيزي بسيط\n")
    create_shorts_video_enhanced(
        text_content="النجاح\nليس بالصدفة\nإنه بالاختيار",
        duration=15,
        output_filename="motivational_shorts.mp4",
        enable_voiceover=True,
        enable_animated_bg=True,
        enable_animated_text=True,
        music_style="cinematic"
    )

# مثال 2: حكمة يومية بدون صوت
def example_wisdom_no_voice():
    """حكمة يومية بخلفية متحركة فقط"""
    print("🚀 مثال 2: حكمة يومية بدون صوت\n")
    create_shorts_video_enhanced(
        text_content="الحكمة\nتأتي من التجارب\nوالتجارب تأتي من الأخطاء",
        duration=18,
        output_filename="wisdom_shorts.mp4",
        enable_voiceover=False,  # بدون تعليق صوتي
        enable_animated_bg=True,
        enable_animated_text=True,
        music_style="ambient"
    )

# مثال 3: فيديو احترافي عالي الجودة
def example_professional_hd():
    """فيديو احترافي بجودة عالية جداً"""
    print("🚀 مثال 3: فيديو احترافي عالي الجودة\n")
    create_shorts_video_enhanced(
        text_content="الإبداع\nهو القدرة على الربط\nبين الأشياء التي لا تبدو مرتبطة",
        duration=20,
        output_filename="professional_hd_shorts.mp4",
        fps=60,  # جودة عالية جداً (ملف أكبر)
        enable_voiceover=True,
        enable_animated_bg=True,
        enable_animated_text=True,
        music_style="cinematic"
    )

# مثال 4: فيديو بسيط بدون تأثيرات
def example_simple_static():
    """فيديو بسيط بدون تأثيرات متحركة"""
    print("🚀 مثال 4: فيديو بسيط\n")
    create_shorts_video_enhanced(
        text_content="ابدأ\nمن حيث أنت\nاستخدم ما لديك\nاعمل بما تستطيع",
        duration=15,
        output_filename="simple_shorts.mp4",
        enable_voiceover=False,
        enable_animated_bg=False,  # خلفية ثابتة فقط
        enable_animated_text=False,  # نص ثابت فقط
        music_style="professional"
    )

# مثال 5: فيديو طويل احترافي
def example_long_cinematic():
    """فيديو طويل بتأثيرات سينمائية"""
    print("🚀 مثال 5: فيديو طويل احترافي\n")
    create_shorts_video_enhanced(
        text_content="في طريقك للنجاح\nستواجه تحديات كثيرة\nلكن تذكر دائماً\nأن كل خطوة تقربك من الهدف\nفلا تستسلم",
        duration=30,
        output_filename="cinematic_long_shorts.mp4",
        fps=30,
        enable_voiceover=True,
        enable_animated_bg=True,
        enable_animated_text=True,
        music_style="cinematic"
    )

# ============================================================================
# الخيارات والتخصيص
# ============================================================================

def custom_example():
    """مثال مخصص بالكامل"""
    print("🚀 مثال مخصص\n")
    
    # اكتب نصك الخاص هنا
    my_text = """
    الحب والعمل الشاق
    هما مفتاح السعادة
    جد عملاً تحبه
    وستكون غنياً بالفعل
    """.strip()
    
    create_shorts_video_enhanced(
        text_content=my_text,
        duration=20,
        fps=30,
        output_filename="my_custom_shorts.mp4",
        enable_voiceover=True,
        enable_animated_bg=True,
        enable_animated_text=True,
        music_style="cinematic"
    )

# ============================================================================
# القائمة الرئيسية
# ============================================================================

def main():
    print("""
╔════════════════════════════════════════════════════════════════════════════╗
║          🎬 AI Shorts Generator - دليل الاستخدام السريع               ║
║              Quick Start Guide for Professional Videos                     ║
╚════════════════════════════════════════════════════════════════════════════╝

اختر أحد الأمثلة التالية:

1️⃣  - فيديو تحفيزي بسيط مع جميع الخصائص
2️⃣  - حكمة يومية بدون تعليق صوتي
3️⃣  - فيديو احترافي بجودة عالية جداً (60 FPS)
4️⃣  - فيديو بسيط بدون تأثيرات متحركة
5️⃣  - فيديو طويل احترافي سينمائي
6️⃣  - مثال مخصص (عدّل النص بنفسك)
7️⃣  - تشغيل اختبار سريع

الخيارات:
   --help          : عرض هذه الرسالة
   --text "نصك"    : إنشاء فيديو بنصك الخاص
   --all           : تشغيل جميع الأمثلة

مثال الاستخدام:
   python quick_start.py 1
   python quick_start.py --text "نصي الخاص"
   python quick_start.py --all

    """)
    
    if len(sys.argv) < 2:
        choice = input("📝 اختر رقم المثال (1-7) أو اكتب 'all': ").strip()
    else:
        if sys.argv[1] == "--text" and len(sys.argv) > 2:
            # نص مخصص من سطر الأوامر
            custom_text = " ".join(sys.argv[2:])
            print(f"\n🎬 إنشاء فيديو بنصك: {custom_text}\n")
            create_shorts_video_enhanced(
                text_content=custom_text,
                duration=15,
                output_filename="custom_video.mp4",
                enable_voiceover=True,
                enable_animated_bg=True,
                enable_animated_text=True,
                music_style="cinematic"
            )
            return
        elif sys.argv[1] == "--all":
            choice = "all"
        else:
            choice = sys.argv[1]
    
    print("\n" + "="*80 + "\n")
    
    if choice == "1":
        example_motivational()
    elif choice == "2":
        example_wisdom_no_voice()
    elif choice == "3":
        example_professional_hd()
    elif choice == "4":
        example_simple_static()
    elif choice == "5":
        example_long_cinematic()
    elif choice == "6":
        custom_example()
    elif choice == "7":
        print("⏱️  تشغيل اختبار سريع (5 ثواني فقط)...\n")
        create_shorts_video_enhanced(
            text_content="اختبار سريع",
            duration=5,
            output_filename="test_shorts.mp4",
            fps=24,
            enable_voiceover=False,
            enable_animated_bg=True,
            enable_animated_text=False,
            music_style="professional"
        )
    elif choice.lower() == "all":
        print("🎬 تشغيل جميع الأمثلة...\n")
        example_motivational()
        print("\n" + "="*80 + "\n")
        example_wisdom_no_voice()
        print("\n" + "="*80 + "\n")
        example_professional_hd()
        print("\n" + "="*80 + "\n")
        example_simple_static()
        print("\n" + "="*80 + "\n")
        example_long_cinematic()
    else:
        print("❌ خيار غير صحيح!")
        return
    
    print("\n" + "="*80)
    print("✅ تم إنشاء الفيديو بنجاح!")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
