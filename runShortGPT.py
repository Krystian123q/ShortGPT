from gui.gui_gradio import ShortGptUI

app = ShortGptUI(colab=False)
app.launch(
    share=True,         # To jest kluczowe na Railway!
    server_name="0.0.0.0"
)
