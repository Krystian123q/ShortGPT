from gui.gui_gradio import ShortGptUI

app = ShortGptUI(colab=False)
app.launch(
    server_port=31415,
    height=1000,
    allowed_paths=["public/", "videos/", "fonts/"],
    share=True,        # <-- TO JEST NAJWAŻNIEJSZE!
    server_name="0.0.0.0"
)
