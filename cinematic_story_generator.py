import os
import sys
import re
import asyncio
from pathlib import Path
from moviepy.editor import (
    ImageClip, VideoFileClip, AudioFileClip, CompositeAudioClip,
    CompositeVideoClip, TextClip, concatenate_videoclips, vfx, ColorClip
)
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
import numpy as np
from scipy.io import wavfile
import warnings
warnings.filterwarnings('ignore')

# مكتبات TTS و Voice
try:
    import pyttsx3
    HAS_PYTTSX3 = True
except ImportError:
    HAS_PYTTSX3 = False

try:
    from edge_tts import Communicate
    HAS_EDGE_TTS = True
except ImportError:
    HAS_EDGE_TTS = False


class CinematicShortGenerator:
    """
    منشئ فيديوهات قصيرة احترافية بجودة سينمائية فخمة
    مع تأثيرات انيميشن متقدمة وسيناريوهات قصيرة
    """
    
    def __init__(self):
        self.temp_dir = "temp_cinema"
        os.makedirs(self.temp_dir, exist_ok=True)
        self.frame_count = 0
        
    def cleanup(self):
        """تنظيف الملفات المؤقتة"""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    # ========================================================================
    # المرحلة 1: إنشاء خلفيات سينمائية فخمة
    # ========================================================================
    
    def create_cinematic_background(self, width=1080, height=1920, duration=15, fps=30, style="luxury"):
        """
        إنشاء خلفية سينمائية فخمة مع تأثيرات متقدمة
        Styles: luxury, minimalist, dark, gradient, particle
        """
        print(f"🎬 جاري إنشاء خلفية سينمائية ({style})...")
        
        try:
            frames_dir = os.path.join(self.temp_dir, "bg_frames")
            os.makedirs(frames_dir, exist_ok=True)
            
            total_frames = int(duration * fps)
            
            for frame_idx in range(total_frames):
                progress = frame_idx / total_frames
                
                if style == "luxury":
                    # خلفية فاخرة سوداء مع ذهبي
                    img = self._create_luxury_frame(width, height, progress)
                
                elif style == "minimalist":
                    # خلفية بسيطة مع تدرجات ناعمة
                    img = self._create_minimalist_frame(width, height, progress)
                
                elif style == "dark":
                    # خلفية داكنة دراماتيكية
                    img = self._create_dark_frame(width, height, progress)
                
                elif style == "gradient":
                    # تدرجات لونية متحركة
                    img = self._create_gradient_frame(width, height, progress)
                
                elif style == "particle":
                    # جزيئات متحركة احترافية
                    img = self._create_particle_frame(width, height, progress)
                
                # حفظ الإطار
                frame_path = os.path.join(frames_dir, f"frame_{frame_idx:05d}.png")
                img.save(frame_path)
                
                if (frame_idx + 1) % 10 == 0:
                    print(f"   ✓ {frame_idx + 1}/{total_frames} إطار", end='\r')
            
            print(f"\n✅ تم إنشاء {total_frames} إطار خلفية سينمائية")
            return frames_dir
        
        except Exception as e:
            print(f"❌ خطأ: {e}")
            return None
    
    def _create_luxury_frame(self, width, height, progress):
        """خلفية فاخرة سوداء مع ذهبي"""
        img = Image.new("RGB", (width, height), (10, 10, 15))
        
        # تدرج ذهبي متحرك
        for y in range(height):
            for x in range(width):
                # حساب اللون بناءً على الحركة
                wave = np.sin((x / width - progress) * 3 * np.pi) * 0.5 + 0.5
                
                r = int(20 + wave * 60)
                g = int(10 + wave * 50)
                b = int(5 + wave * 40)
                
                # تدرج عمودي
                brightness = int(255 * (y / height) * 0.2)
                r = min(255, r + brightness)
                g = min(255, g + brightness)
                b = min(255, b + brightness)
                
                img.putpixel((x, y), (r, g, b))
        
        # إضافة أشكال هندسية احترافية
        draw = ImageDraw.Draw(img, 'RGBA')
        
        # خطوط ذهبية عمودية
        for i in range(5):
            x = int(width * (i / 4 + progress * 0.5) % 1)
            alpha = int(50 * (0.5 - abs(0.5 - (x / width))))
            draw.line([(x, 0), (x, height)], fill=(200, 150, 50, alpha), width=2)
        
        # دوائر مركزة
        center_x, center_y = width // 2, height // 2
        for r in range(200, 0, 50):
            alpha = int(30 * (1 - r / 200))
            draw.ellipse(
                [(center_x - r, center_y - r), (center_x + r, center_y + r)],
                outline=(200, 150, 50, alpha),
                width=2
            )
        
        # تطبيق تأثير التمويه الخفيف
        img = img.filter(ImageFilter.GaussianBlur(radius=1))
        
        return img
    
    def _create_minimalist_frame(self, width, height, progress):
        """خلفية بسيطة وأنيقة"""
        img = Image.new("RGB", (width, height), (240, 240, 245))
        draw = ImageDraw.Draw(img)
        
        # تدرج ناعم
        for y in range(height):
            value = int(240 - (y / height) * 40)
            draw.line([(0, y), (width, y)], fill=(value, value, value + 10))
        
        # أشكال هندسية بسيطة
        circle_x = int(width * progress)
        circle_y = height // 2
        draw.ellipse(
            [(circle_x - 30, circle_y - 30), (circle_x + 30, circle_y + 30)],
            outline=(100, 150, 200),
            width=3
        )
        
        return img
    
    def _create_dark_frame(self, width, height, progress):
        """خلفية داكنة دراماتيكية"""
        img = Image.new("RGB", (width, height), (5, 5, 20))
        draw = ImageDraw.Draw(img)
        
        # موجات داكنة
        for x in range(0, width, 10):
            y_offset = int(50 * np.sin((x / width - progress) * 2 * np.pi))
            draw.line([(x, height // 2 + y_offset), (x + 10, height // 2 + y_offset)],
                     fill=(50, 100, 200), width=2)
        
        # شعاع نور
        angle = progress * 2 * np.pi
        for i in range(200):
            x = int(width // 2 + i * np.cos(angle))
            y = int(height // 2 + i * np.sin(angle))
            if 0 <= x < width and 0 <= y < height:
                brightness = int(100 * (1 - i / 200))
                img.putpixel((x, y), (brightness, brightness + 50, brightness + 100))
        
        return img
    
    def _create_gradient_frame(self, width, height, progress):
        """تدرجات لونية متحركة"""
        img = Image.new("RGB", (width, height))
        
        for y in range(height):
            # حساب اللون بناءً على الموضع والوقت
            hue = ((y / height + progress) % 1.0) * 360
            
            # تحويل HSV إلى RGB
            r, g, b = self._hsv_to_rgb(hue, 0.7, 0.5)
            
            for x in range(width):
                # تأثير موجة
                wave = np.sin((x / width) * 2 * np.pi) * 0.1
                factor = 1 + wave
                
                r_adj = max(0, min(255, int(r * factor)))
                g_adj = max(0, min(255, int(g * factor)))
                b_adj = max(0, min(255, int(b * factor)))
                
                img.putpixel((x, y), (r_adj, g_adj, b_adj))
        
        return img
    
    def _create_particle_frame(self, width, height, progress):
        """جزيئات متحركة احترافية"""
        img = Image.new("RGB", (width, height), (15, 15, 30))
        draw = ImageDraw.Draw(img, 'RGBA')
        
        # عدد الجزيئات
        num_particles = 50
        
        for i in range(num_particles):
            # موضع الجزيء
            angle = (i / num_particles) * 2 * np.pi + progress * 2
            radius = 100 + 50 * np.sin(progress * 3)
            
            x = width // 2 + int(radius * np.cos(angle))
            y = height // 2 + int(radius * np.sin(angle))
            
            # الحجم والشفافية
            size = 5 + 5 * np.sin(progress * 5 + i)
            alpha = int(150 * (0.5 + 0.5 * np.cos(progress * 3 + i)))
            
            draw.ellipse(
                [(x - size, y - size), (x + size, y + size)],
                fill=(100 + 100 * np.sin(i), 150 + 100 * np.cos(i), 200, alpha)
            )
        
        return img
    
    def _hsv_to_rgb(self, h, s, v):
        """تحويل HSV إلى RGB"""
        c = v * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = v - c
        
        if h < 60:
            r, g, b = c, x, 0
        elif h < 120:
            r, g, b = x, c, 0
        elif h < 180:
            r, g, b = 0, c, x
        elif h < 240:
            r, g, b = 0, x, c
        elif h < 300:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x
        
        return int((r + m) * 255), int((g + m) * 255), int((b + m) * 255)
    
    # ========================================================================
    # المرحلة 2: تأثيرات انيميشن متقدمة
    # ========================================================================
    
    def create_animated_title(self, title, duration, width=1080, height=1920, style="elegant"):
        """
        إنشاء عنوان متحرك احترافي
        Styles: elegant, bold, typewriter, split, fade
        """
        print(f"✨ جاري إنشاء عنوان متحرك ({style})...")
        
        try:
            # إنشاء إطارات العنوان
            frames_dir = os.path.join(self.temp_dir, "title_frames")
            os.makedirs(frames_dir, exist_ok=True)
            
            fps = 30
            total_frames = int(duration * fps)
            
            for frame_idx in range(total_frames):
                progress = frame_idx / total_frames
                
                img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
                draw = ImageDraw.Draw(img)
                
                # تحميل خط عربي
                font_size = 120
                font = self._load_arabic_font(font_size)
                
                if style == "elegant":
                    img = self._animate_elegant_title(img, title, progress, draw, font)
                elif style == "bold":
                    img = self._animate_bold_title(img, title, progress, draw, font)
                elif style == "typewriter":
                    img = self._animate_typewriter_title(img, title, progress, draw, font)
                elif style == "split":
                    img = self._animate_split_title(img, title, progress, draw, font)
                elif style == "fade":
                    img = self._animate_fade_title(img, title, progress, draw, font)
                
                frame_path = os.path.join(frames_dir, f"title_{frame_idx:05d}.png")
                img.save(frame_path)
                
                if (frame_idx + 1) % 15 == 0:
                    print(f"   ✓ {frame_idx + 1}/{total_frames} إطار", end='\r')
            
            print(f"\n✅ تم إنشاء عنوان متحرك")
            return frames_dir
        
        except Exception as e:
            print(f"❌ خطأ: {e}")
            return None
    
    def _load_arabic_font(self, size):
        """تحميل خط عربي احترافي"""
        font_paths = [
            "/usr/share/fonts/truetype/noto/NotoSansArabic-Bold.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/System/Library/Fonts/Arial.ttf",
            "C:\\Windows\\Fonts\\arial.ttf",
        ]
        
        for font_path in font_paths:
            if os.path.exists(font_path):
                try:
                    return ImageFont.truetype(font_path, size)
                except:
                    continue
        
        return ImageFont.load_default()
    
    def _animate_elegant_title(self, img, title, progress, draw, font):
        """عنوان أنيق مع تأثير الظهور التدريجي"""
        width, height = img.size
        
        # حساب الشفافية والحجم
        alpha = int(255 * min(1, progress * 2))
        scale = 0.8 + 0.2 * progress
        
        font_size = int(120 * scale)
        font = self._load_arabic_font(font_size)
        
        # رسم النص
        bbox = draw.textbbox((0, 0), title, font=font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) // 2
        y = height // 2 - 100
        
        # ظل أنيق
        draw.text((x + 3, y + 3), title, font=font, fill=(0, 0, 0, alpha // 2))
        # النص الأساسي
        draw.text((x, y), title, font=font, fill=(255, 255, 255, alpha))
        
        return img
    
    def _animate_bold_title(self, img, title, progress, draw, font):
        """عنوان جريء مع تأثير الحركة"""
        width, height = img.size
        
        # حركة من اليسار
        x_offset = int(width * (progress - 1) * 0.5)
        alpha = int(255 * min(1, progress * 3))
        
        font_size = 120
        font = self._load_arabic_font(font_size)
        
        bbox = draw.textbbox((0, 0), title, font=font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) // 2 + x_offset
        y = height // 2 - 100
        
        draw.text((x, y), title, font=font, fill=(255, 200, 0, alpha))
        
        return img
    
    def _animate_typewriter_title(self, img, title, progress, draw, font):
        """عنوان مع تأثير الكتابة"""
        width, height = img.size
        
        # حساب عدد الأحرف المرئية
        num_chars = int(len(title) * progress)
        visible_text = title[:num_chars]
        
        font_size = 120
        font = self._load_arabic_font(font_size)
        
        bbox = draw.textbbox((0, 0), visible_text, font=font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) // 2
        y = height // 2 - 100
        
        draw.text((x, y), visible_text, font=font, fill=(255, 255, 255, 255))
        
        # مؤشر الكتابة
        if num_chars < len(title):
            cursor_x = x + text_width + 5
            draw.line([(cursor_x, y), (cursor_x, y + 100)], fill=(255, 255, 255, 255), width=3)
        
        return img
    
    def _animate_split_title(self, img, title, progress, draw, font):
        """عنوان ينقسم إلى قسمين"""
        width, height = img.size
        
        # تقسيم النص
        mid = len(title) // 2
        left_text = title[:mid]
        right_text = title[mid:]
        
        # حركة الأجزاء
        x_offset = int(width * 0.3 * (0.5 - progress))
        alpha = int(255 * min(1, progress * 2))
        
        font_size = 120
        font = self._load_arabic_font(font_size)
        
        # الجزء الأيسر
        bbox_left = draw.textbbox((0, 0), left_text, font=font)
        text_width_left = bbox_left[2] - bbox_left[0]
        x_left = width // 2 - text_width_left - x_offset
        draw.text((x_left, height // 2 - 100), left_text, font=font, fill=(255, 100, 100, alpha))
        
        # الجزء الأيمن
        x_right = width // 2 + x_offset
        draw.text((x_right, height // 2 - 100), right_text, font=font, fill=(100, 150, 255, alpha))
        
        return img
    
    def _animate_fade_title(self, img, title, progress, draw, font):
        """عنوان مع تأثير التلاشي والظهور"""
        width, height = img.size
        
        # تأثير fade in ثم fade out
        if progress < 0.5:
            alpha = int(255 * (progress * 2))
        else:
            alpha = int(255 * (1 - (progress - 0.5) * 2))
        
        # تأثير تكبير وتصغير
        scale = 0.8 + 0.4 * np.sin(progress * np.pi)
        font_size = int(120 * scale)
        font = self._load_arabic_font(font_size)
        
        bbox = draw.textbbox((0, 0), title, font=font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) // 2
        y = height // 2 - 100
        
        draw.text((x, y), title, font=font, fill=(255, 255, 255, alpha))
        
        return img
    
    # ========================================================================
    # المرحلة 3: تأثيرات سينمائية متقدمة
    # ========================================================================
    
    def create_cinematic_effects(self, duration, width=1080, height=1920, effect_type="film_grain"):
        """
        إضافة تأثيرات سينمائية احترافية
        Types: film_grain, vignette, lens_flare, bokeh
        """
        print(f"🎬 جاري إضافة تأثيرات سينمائية ({effect_type})...")
        
        try:
            frames_dir = os.path.join(self.temp_dir, f"effect_{effect_type}")
            os.makedirs(frames_dir, exist_ok=True)
            
            fps = 30
            total_frames = int(duration * fps)
            
            for frame_idx in range(total_frames):
                progress = frame_idx / total_frames
                
                if effect_type == "film_grain":
                    img = self._create_film_grain(width, height, progress)
                elif effect_type == "vignette":
                    img = self._create_vignette(width, height, progress)
                elif effect_type == "lens_flare":
                    img = self._create_lens_flare(width, height, progress)
                elif effect_type == "bokeh":
                    img = self._create_bokeh(width, height, progress)
                
                frame_path = os.path.join(frames_dir, f"effect_{frame_idx:05d}.png")
                img.save(frame_path)
                
                if (frame_idx + 1) % 15 == 0:
                    print(f"   ✓ {frame_idx + 1}/{total_frames}", end='\r')
            
            print(f"\n✅ تم إضافة تأثيرات سينمائية")
            return frames_dir
        
        except Exception as e:
            print(f"❌ خطأ: {e}")
            return None
    
    def _create_film_grain(self, width, height, progress):
        """تأثير حبيبات الفيلم القديم"""
        img = Image.new("RGB", (width, height), (100, 100, 100))
        
        for y in range(height):
            for x in range(width):
                grain = np.random.randint(-30, 30)
                base = 100
                value = max(0, min(255, base + grain))
                img.putpixel((x, y), (value, value, value))
        
        return img
    
    def _create_vignette(self, width, height, progress):
        """تأثير الإطار المظلم على الحواف"""
        img = Image.new("RGB", (width, height), (50, 50, 50))
        
        center_x, center_y = width // 2, height // 2
        max_dist = np.sqrt(center_x**2 + center_y**2)
        
        for y in range(height):
            for x in range(width):
                dist = np.sqrt((x - center_x)**2 + (y - center_y)**2)
                factor = 1 - (dist / max_dist) ** 1.5
                value = int(100 * factor)
                img.putpixel((x, y), (value, value, value))
        
        return img
    
    def _create_lens_flare(self, width, height, progress):
        """تأثير انعكاس الضوء على العدسة"""
        img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # موضع الشعاع يتحرك
        x = int(width * progress)
        y = int(height * 0.3)
        
        # رسم شعاع الضوء
        for i in range(100, 0, -5):
            alpha = int(200 * (1 - i / 100))
            draw.ellipse([(x - i, y - i), (x + i, y + i)], 
                        outline=(255, 255, 200, alpha), width=2)
        
        return img
    
    def _create_bokeh(self, width, height, progress):
        """تأثير الأضواء الضبابية الخارج من التركيز"""
        img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # رسم دوائر bokeh
        for i in range(15):
            angle = (i / 15 + progress) * 2 * np.pi
            x = int(width // 2 + 300 * np.cos(angle))
            y = int(height // 2 + 300 * np.sin(angle))
            
            size = np.random.randint(20, 80)
            brightness = np.random.randint(150, 255)
            
            draw.ellipse([(x - size, y - size), (x + size, y + size)],
                        fill=(brightness, brightness - 50, brightness - 100, 100))
        
        return img
    
    # ========================================================================
    # المرحلة 4: التعليق الصوتي الاحترافي
    # ========================================================================
    
    async def create_professional_voiceover(self, text, output_path="voiceover.mp3", language="ar"):
        """
        إنشاء تعليق صوتي احترافي بجودة عالية
        """
        print(f"🎤 جاري إنشاء التعليق الصوتي (بجودة احترافية)...")
        
        try:
            if HAS_EDGE_TTS:
                # تحديد الصوت الاحترافي
                voices = {
                    "ar": "ar-SA-FadiyahNeural",  # صوت نسائي احترافي
                    "ar-male": "ar-SA-HamedNeural",  # صوت ذكري احترافي
                    "en": "en-US-AriaNeural",
                    "en-male": "en-US-GuyNeural"
                }
                
                voice = voices.get(language, "ar-SA-FadiyahNeural")
                
                # تطبيق معايير احترافية
                communicate = Communicate(
                    text,
                    voice,
                    rate="-5%",  # سرعة أبطأ قليلاً للوضوح
                    volume="+10%"  # مستوى صوت أعلى
                )
                
                await communicate.save(output_path)
                print(f"✅ تم إنشاء التعليق الصوتي: {output_path}")
                return output_path
            
            elif HAS_PYTTSX3:
                engine = pyttsx3.init()
                engine.setProperty('rate', 120)
                engine.setProperty('volume', 0.95)
                engine.save_to_file(text, output_path)
                engine.runAndWait()
                print(f"✅ تم إنشاء التعليق الصوتي: {output_path}")
                return output_path
            
            else:
                print("⚠️ لا توجد مكتبات TTS متاحة")
                return None
        
        except Exception as e:
            print(f"❌ خطأ: {e}")
            return None
    
    # ========================================================================
    # المرحلة 5: موسيقى خلفية احترافية
    # ========================================================================
    
    def create_cinematic_music(self, duration=15, output_path="cinematic_music.mp3", mood="epic"):
        """
        إنشاء موسيقى سينمائية احترافية
        Moods: epic, emotional, mysterious, uplifting
        """
        print(f"🎵 جاري إنشاء موسيقى سينمائية ({mood})...")
        
        try:
            sample_rate = 44100
            t = np.linspace(0, duration, int(sample_rate * duration))
            
            if mood == "epic":
                # موسيقى حماسية درامية
                freq1, freq2, freq3, freq4 = 80, 160, 240, 320
                wave1 = 0.25 * np.sin(2 * np.pi * freq1 * t)
                wave2 = 0.2 * np.sin(2 * np.pi * freq2 * t)
                wave3 = 0.15 * np.sin(2 * np.pi * freq3 * t)
                wave4 = 0.1 * np.sin(2 * np.pi * freq4 * t)
                
            elif mood == "emotional":
                # موسيقى عاطفية حزينة
                freq1, freq2, freq3 = 100, 200, 300
                wave1 = 0.3 * np.sin(2 * np.pi * freq1 * t) * np.cos(2 * np.pi * 0.5 * t)
                wave2 = 0.2 * np.sin(2 * np.pi * freq2 * t)
                wave3 = 0.15 * np.sin(2 * np.pi * freq3 * t)
                wave4 = 0
                
            elif mood == "mysterious":
                # موسيقى غامضة مثيرة
                freq1, freq2, freq3 = 90, 180, 270
                wave1 = 0.2 * np.sin(2 * np.pi * freq1 * t + np.pi * np.sin(2 * np.pi * 0.1 * t))
                wave2 = 0.2 * np.sin(2 * np.pi * freq2 * t)
                wave3 = 0.15 * np.sin(2 * np.pi * freq3 * t)
                wave4 = 0.1 * np.sin(2 * np.pi * 150 * t)
                
            else:  # uplifting
                # موسيقى إيجابية مرفعة للمعنويات
                freq1, freq2, freq3 = 110, 220, 330
                wave1 = 0.25 * np.sin(2 * np.pi * freq1 * t)
                wave2 = 0.2 * np.sin(2 * np.pi * freq2 * t)
                wave3 = 0.15 * np.sin(2 * np.pi * freq3 * t)
                wave4 = 0.1 * np.sin(2 * np.pi * 440 * t)
            
            # Envelope احترافي
            attack = np.linspace(0, 1, len(t) // 6)
            decay = np.linspace(1, 0.7, len(t) // 6)
            sustain = np.ones(len(t) // 3)
            release = np.linspace(0.7, 0, len(t) - len(t) // 6 - len(t) // 6 - len(t) // 3)
            envelope = np.concatenate([attack, decay, sustain, release])
            
            # دمج الموجات
            audio = (wave1 + wave2 + wave3 + wave4) * envelope * 0.3
            
            # تطبيع ومعالجة صوتية احترافية
            audio = audio / np.max(np.abs(audio)) * 0.85
            
            # حفظ الملف
            wav_path = os.path.join(self.temp_dir, "temp_music.wav")
            wavfile.write(wav_path, sample_rate, (audio * 32767).astype(np.int16))
            
            # تحويل إلى MP3
            cmd = f"ffmpeg -i {wav_path} -q:a 6 -n {output_path} 2>/dev/null"
            os.system(cmd)
            
            if os.path.exists(wav_path):
                os.remove(wav_path)
            
            print(f"✅ تم إنشاء الموسيقى: {output_path}")
            return output_path
        
        except Exception as e:
            print(f"❌ خطأ: {e}")
            return None
    
    # ========================================================================
    # المرحلة 6: دمج كل شيء معاً
    # ========================================================================
    
    def create_cinematic_story_video(
        self,
        story_parts,  # قائمة من الأجزاء (عنوان، نص، مدة)
        output_filename="cinematic_story.mp4",
        bg_style="luxury",
        title_style="elegant",
        effect_type="vignette",
        music_mood="epic",
        fps=30
    ):
        """
        إنشاء قصة قصيرة سينمائية كاملة
        story_parts: [
            {"title": "...", "text": "...", "duration": 5},
            {"title": "...", "text": "...", "duration": 5},
        ]
        """
        
        print("\n" + "="*80)
        print("🎬 منشئ القصص السينمائية - Cinematic Story Generator")
        print("="*80 + "\n")
        
        try:
            all_clips = []
            
            # معالجة كل جزء من أجزاء القصة
            for part_idx, part in enumerate(story_parts):
                print(f"\n📖 جاري معالجة الجزء {part_idx + 1}/{len(story_parts)}")
                
                title = part.get("title", "")
                text = part.get("text", "")
                duration = part.get("duration", 5)
                
                # 1. إنشاء الخلفية
                bg_frames = self.create_cinematic_background(
                    duration=duration,
                    style=bg_style,
                    fps=fps
                )
                
                if bg_frames:
                    bg_clip = self._frames_to_clip(bg_frames, duration, fps)
                
                # 2. إنشاء العنوان المتحرك
                if title:
                    title_frames = self.create_animated_title(
                        title,
                        duration=2,
                        style=title_style
                    )
                    
                    if title_frames:
                        title_clip = self._frames_to_clip(title_frames, 2, fps)
                        title_clip = title_clip.set_position("center")
                        bg_clip = CompositeVideoClip(
                            [bg_clip, title_clip.set_start(0)],
                            size=bg_clip.size
                        )
                
                # 3. إضافة النص
                if text:
                    text_clip = TextClip(
                        text,
                        fontsize=60,
                        color='white',
                        method='caption',
                        size=(1000, None),
                        font='Arial-Bold'
                    ).set_duration(duration - 2).set_start(2)
                    
                    text_clip = text_clip.set_position(("center", "bottom"))
                    
                    bg_clip = CompositeVideoClip(
                        [bg_clip, text_clip],
                        size=bg_clip.size
                    )
                
                # 4. إضافة تأثيرات سينمائية
                effect_frames = self.create_cinematic_effects(
                    duration=duration,
                    effect_type=effect_type
                )
                
                if effect_frames:
                    effect_clip = self._frames_to_clip(effect_frames, duration, fps)
                    bg_clip = CompositeVideoClip(
                        [bg_clip, effect_clip.set_opacity(0.3)],
                        size=bg_clip.size
                    )
                
                all_clips.append(bg_clip)
            
            # دمج جميع الأجزاء
            print("\n🎬 جاري دمج أجزاء القصة...")
            final_video = concatenate_videoclips(all_clips)
            
            # إضافة الموسيقى الخلفية
            print("🎵 جاري إضافة الموسيقى الخلفية...")
            total_duration = sum(p.get("duration", 5) for p in story_parts)
            music_path = self.create_cinematic_music(
                duration=total_duration,
                mood=music_mood
            )
            
            if music_path and os.path.exists(music_path):
                music = AudioFileClip(music_path)
                if music.duration > total_duration:
                    music = music.subclip(0, total_duration)
                final_video = final_video.set_audio(music.volumex(0.6))
            
            # تصدير الفيديو
            print("\n💾 جاري تصدير الفيديو النهائي...")
            print(f"📁 الملف: {output_filename}\n")
            
            final_video.write_videofile(
                output_filename,
                fps=fps,
                codec="libx264",
                audio_codec="aac",
                verbose=False,
                logger=None
            )
            
            print("\n✅ تم إنشاء الفيديو بنجاح!")
            print(f"📊 الحجم: {os.path.getsize(output_filename) / (1024*1024):.2f} MB")
            print("="*80 + "\n")
            
            # تنظيف
            self.cleanup()
            
            return output_filename
        
        except Exception as e:
            print(f"❌ خطأ: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def _frames_to_clip(self, frames_dir, duration, fps):
        """تحويل مجلد الإطارات إلى مقطع فيديو"""
        frame_files = sorted(os.listdir(frames_dir))
        if not frame_files:
            return None
        
        frame_clips = [
            ImageClip(os.path.join(frames_dir, f)).set_duration(1/fps)
            for f in frame_files
        ]
        
        return concatenate_videoclips(frame_clips)


# ============================================================================
# واجهة الاستخدام
# ============================================================================

def main():
    """
    أمثلة على استخدام منشئ القصص السينمائية
    """
    
    generator = CinematicShortGenerator()
    
    # مثال 1: قصة قصيرة سينمائية
    story = [
        {
            "title": "البداية",
            "text": "كل نهاية هي بداية جديدة\nكل سقوط يعلمنا الحكمة",
            "duration": 8
        },
        {
            "title": "الرحلة",
            "text": "في طريقنا نجد أنفسنا\nفي الظلام نرى النور",
            "duration": 8
        },
        {
            "title": "النهاية",
            "text": "والآن... بداية جديدة",
            "duration": 6
        }
    ]
    
    generator.create_cinematic_story_video(
        story_parts=story,
        output_filename="cinematic_story.mp4",
        bg_style="luxury",
        title_style="elegant",
        effect_type="vignette",
        music_mood="epic",
        fps=30
    )


if __name__ == "__main__":
    main()
