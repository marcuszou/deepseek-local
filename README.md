# Steamlit DeepSeek-R1 locally

## Tech Stack
- Python
- ollama
- streamlit
- deepseek LLM

## How-to
1. Install ollama app per Windows/Linux/macOS env
    ```shell
    http://ollama.com/download
    ```
2. Download `DeepSeek-R1 7b` model in a terminal/Command-prompt:
    ```shell
    ollama pull deepseek-r1:7b
    ```
3. Create folder and setup venv
    ```shell
    mkdir deepseek-gui
    cd deepseek-gui
    python3 -m venv ds-venv
    source ds-venv/bin/activate ## in Linux/macOS
    ## .\ds-venv\scripts\activate.exe   ## in Windows
    ```
4. Install the python packages
    ```shell
    pip install -r requirements.txt
    ```

4. Prepare the Python3 code.
    - A sample python code has been provided as `main.py`
5. Run the code.
    ```shell
    streamlit run main.py
    ```

## License
- MIT