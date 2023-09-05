from subprocess import call
from ui import demo

def main():
    install_pip = "apt install pip"
    install_cuda = "pip install cupy-cuda115"
    install_gradio = "pip install gradio"

    call(install_pip)

    call([install_cuda,install_gradio])

    print("launching ui")
    demo.launch(share=True)