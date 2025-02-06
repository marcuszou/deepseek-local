# Install Conda and DeepSeek Janus on macOS

per https://docs.conda.io



## Install Miniconda in silent mode

To run the [silent installation](https://docs.conda.io/projects/conda/en/stable/glossary.html#silent-mode-glossary) of Miniconda for macOS or Linux, specify the -b and -p arguments of the bash installer. The following arguments are supported:

- `-b`: Batch mode with no PATH modifications to shell scripts. Assumes that you agree to the license agreement. Does not edit shell scripts such as `.bashrc`, `.bash_profile`, `.zshrc`, etc.
- `-p`: Installation prefix/path.
- `-f`: Force installation even if prefix `-p` already exists.

```shell
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -O ~/miniconda.sh --no-check-certificate

bash ~/miniconda.sh -b -p $HOME/miniconda
```

Then initialize the Conda:

```shell
source ~/miniconda/bin/activate

conda init --all
```



## Install DeepSeek Janus

```shellcd projects
## Create folder
cd projects
mkdir deepseek

## Create venv for Janus
@@ This Python3.10 env has issue with the requirements.txt
## Then do NOT use it.
## conda create -n janus python=3.10 -y
## conda activate janus

## git clone https://github.com/deepseek-ai/janus.git
## cd janus
git clone https://github.com/briankb/deepseek-janus.git
cd deepseek-janus

## Install the dependencies
pip install -e .
```



## Create GUI

```shell
pip install gradio

## Then call up the Janus model
python demo/app_januspro.py
```



## Download Deepseek-ai/janus-pro-7b from hugging face?

to be verified.
