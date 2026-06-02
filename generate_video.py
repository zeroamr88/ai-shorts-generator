from moviepy.editor import TextClip, CompositeVideoClip

text = "Hello from AI Video Bot"

clip = TextClip(
    text, 
    fontsize=70, 
    color='white', 
    bg_color='black', 
    size=(1280, 720),
    font='DejaVu-Sans-Bold'
)
clip = clip.set_duration(5)

clip.write_videofile("output.mp4", fps=24, verbose=False, logger=None)
