from textual.app import App, ComposeResult
from textual.widgets import Static

class KonsoleConnect(App):
    CSS_PATH = "app.tcss"

    def compose(self) -> ComposeResult:
        yield Static("hello")

if __name__ == "__main__":
    KonsoleConnect().run()