# Steamlit DeepSeek-R1 locally

## Tech Stack
- Python
- ollama
- streamlit
- deepseek LLM

## How-to
1. Install ollama app in Windows/Linux/macOS
```shell
http://ollama.com/download
```
2. Ensure you have Python 3.10+ installed
3. Create folder and setup venv
```shell
mkdir deepseek-gui
cd deepseek-gui
python3 -m venv ds-venv
.\ds-venv\scripts\activate.exe   ## in Windows
## source ds-venv/bin/activate ## in Linux/macOS
pip install -r requirements.txt
```

4. Prepare the Python3 code.
5. Run the code.
```shell
streamlit run main.py
```