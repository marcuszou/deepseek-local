# How to Install DeepSeek Janus Pro 7B Locally?

[#deepseek](https://dev.to/t/deepseek)[#opensource](https://dev.to/t/opensource)[#januspro](https://dev.to/t/januspro)[#ai](https://dev.to/t/ai)

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Feldixke6774v427xwqtx.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Feldixke6774v427xwqtx.png)

Janus-Pro, built on the DeepSeek-LLM-7B-base, is an advanced multimodal framework designed to unify understanding and generation tasks. By decoupling visual encoding into separate pathways while maintaining a unified transformer architecture, it resolves conflicts between visual understanding and generation. Equipped with the SigLIP-L vision encoder for image input and an efficient tokenizer for image generation, Janus-Pro delivers high performance across multimodal benchmarks, surpassing unified models and competing effectively with task-specific approaches. Its simplicity, flexibility, and robust design make it a strong contender for next-generation vision-language models.

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fy7yejb8zdanomu4gnyl3.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fy7yejb8zdanomu4gnyl3.png)

### Resource

HuggingFace

Link: https://huggingface.co/deepseek-ai/Janus-Pro-7B

GitHub

Link: https://github.com/deepseek-ai/Janus

Prerequisites for Installing DeepSeek Janus Pro 7B Locally
Make sure you have the following:

GPUs: 1xRTXA6000 (for smooth execution).
Disk Space: 100 GB free.
RAM: 64 GB(48 Also works) but we use 64 for smooth execution
CPU: 64 Cores(48 Also works)but we use 64 for smooth execution
Step-by-Step Process to Install NVIDIA SANA Model Locally
For the purpose of this tutorial, we will use a GPU-powered Virtual Machine offered by NodeShift; however, you can replicate the same steps with any other cloud provider of your choice. NodeShift provides the most affordable Virtual Machines at a scale that meets GDPR, SOC2, and ISO27001 requirements.

### Step 1: Sign Up and Set Up a NodeShift Cloud Account

Visit the [NodeShift Platform](https://nodeshift.com/) and create an account. Once you’ve signed up, log into your account.

Follow the account setup process and provide the necessary details and information.

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fth9ztf8mpkelzeuu1e9d.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fth9ztf8mpkelzeuu1e9d.png)

### Step 2: Create a GPU Node (Virtual Machine)

GPU Nodes are NodeShift’s GPU Virtual Machines, on-demand resources equipped with diverse GPUs ranging from H100s to A100s. These GPU-powered VMs provide enhanced environmental control, allowing configuration adjustments for GPUs, CPUs, RAM, and Storage based on specific requirements.

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2d12hhcwfvoh5hh9kxmd.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2d12hhcwfvoh5hh9kxmd.png)

Navigate to the menu on the left side. Select the GPU Nodes option, create a GPU Node in the Dashboard, click the Create GPU Node button, and create your first Virtual Machine deployment.

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fndt1t1fecn9zjv7k22uu.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fndt1t1fecn9zjv7k22uu.png)

### Step 3: Select a Model, Region, and Storage

In the “GPU Nodes” tab, select a GPU Model and Storage according to your needs and the geographical region where you want to launch your model.

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4doqr25rupx0j39qh3f2.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4doqr25rupx0j39qh3f2.png)

We will use 1x RTX A6000 GPU for this tutorial to achieve the fastest performance. However, you can choose a more affordable GPU with less VRAM if that better suits your requirements.

### Step 4: Select Authentication Method

There are two authentication methods available: Password and SSH Key. SSH keys are a more secure option. To create them, please refer to our [official documentation](https://docs.nodeshift.com/gpus/create-gpu-deployment?ref=blog.nodeshift.com).

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fubqutves5lmcg153l8yp.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fubqutves5lmcg153l8yp.png)

### Step 5: Choose an Image

Next, you will need to choose an image for your Virtual Machine. We will deploy DeepSeek Janus Pro 7B on an NVIDIA Cuda Virtual Machine. This proprietary, closed-source parallel computing platform will allow you to install DeepSeek Janus Pro 7B on your GPU Node.

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5gcxwaq6k0xu6m6hif1v.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F5gcxwaq6k0xu6m6hif1v.png)

After choosing the image, click the ‘Create’ button, and your Virtual Machine will be deployed.

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fpwn3qv0syf56zypfv7mz.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fpwn3qv0syf56zypfv7mz.png)

### Step 6: Virtual Machine Successfully Deployed

You will get visual confirmation that your node is up and running.

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fx9crtj4d39vnu4e9ru9m.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fx9crtj4d39vnu4e9ru9m.png)

### Step 7: Connect to GPUs using SSH

NodeShift GPUs can be connected to and controlled through a terminal using the SSH key provided during GPU creation.

Once your GPU Node deployment is successfully created and has reached the ‘RUNNING’ status, you can navigate to the page of your GPU Deployment Instance. Then, click the ‘Connect’ button in the top right corner.

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F0fqsq2ifo2hzf1bc6qrv.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F0fqsq2ifo2hzf1bc6qrv.png)

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffkc62yk405jsn824ypyg.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffkc62yk405jsn824ypyg.png)

Now open your terminal and paste the proxy SSH IP or direct SSH IP.

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fma1yy0xqqsqu85y68hgj.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fma1yy0xqqsqu85y68hgj.png)

Next, if you want to check the GPU details, run the command below:

```
nvidia-smi
```



[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fx2pmuqvwzc1idgrxt0fc.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fx2pmuqvwzc1idgrxt0fc.png)

### Step 8: Check the Available Python version and Install the new version

Run the following commands to check the available Python version.

If you check the version of the python, system has Python 3.8.1 available by default. To install a higher version of Python, you’ll need to use the deadsnakes PPA.

Run the following commands to add the deadsnakes PPA:

```
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
```



[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fumj8bujltuarbbxa0lld.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fumj8bujltuarbbxa0lld.png)

### Step 9: Install Python 3.11

Now, run the following command to install Python 3.11 or another desired version:

```
sudo apt install -y python3.11 python3.11-distutils python3.11-venv
```



[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fia3y9t88yqb3sacevofh.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fia3y9t88yqb3sacevofh.png)

### Step 10: Update the Default Python3 Version

Now, run the following command to link the new Python version as the default python3:

```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2
sudo update-alternatives --config python3
```



Then, run the following command to verify that the new Python version is active:

```
python3 --version
```



[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F84qr8kkvavz2zvuxlo69.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F84qr8kkvavz2zvuxlo69.png)

### Step 11: Install and Update Pip

Run the following command to install and update the pip:

```
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
```



Then, run the following command to check the version of pip:

```
pip --version
```



[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fm7ci2v9m03si4dk9obz9.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fm7ci2v9m03si4dk9obz9.png)

### Step 12: Clone the Repository

Run the following command to clone the DeepSeek Janus repository:

```
git clone https://github.com/deepseek-ai/Janus.git
cd Janus
```



[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fpi3cqhmmxsxr4qh8bfgc.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fpi3cqhmmxsxr4qh8bfgc.png)

### Step 13: Install the Project Dependencies

Run the following command to install the project dependencies:

```
pip install -e .
```



[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F59kzvw8hwjzj7g2td4ct.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F59kzvw8hwjzj7g2td4ct.png)

### Step 14: Install Gradio

Run the following command to install the gradio:

```
pip install -e .[gradio]
```



[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F43myixulh71kor7mwbiv.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F43myixulh71kor7mwbiv.png)

### Step 15: Run the Server

Execute the following command to run the server:

```
python3 demo/app_januspro.py
```



[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwed5cdhnq5u5vdpzmgc0.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fwed5cdhnq5u5vdpzmgc0.png)

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbtfbaysrvflp8w4badn1.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbtfbaysrvflp8w4badn1.png)

### Step 16: Access the Application

Accessing the application at:

Running on local URL: [http://127.0.0.1:7860](http://127.0.0.1:7860/)

Running on public URL: [https://0fac078df655921b11.gradio.live](https://0fac078df655921b11.gradio.live/)

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fh37vhtdrkzplp1onnav7.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fh37vhtdrkzplp1onnav7.png)

### Step 17: Multimodal Understanding

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fif6vuf9o7zo0b1xi5fb4.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fif6vuf9o7zo0b1xi5fb4.png)

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fzclrubsvahbctgjjkpxp.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fzclrubsvahbctgjjkpxp.png)

### Step 18: Text-to-Image Generation

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4vmezcbff5t12aowdedo.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4vmezcbff5t12aowdedo.png)

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3laqgkiy2g7x2dfyzki0.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F3laqgkiy2g7x2dfyzki0.png)

[![Image description](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvebv3xvofl42t2fd3ytn.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvebv3xvofl42t2fd3ytn.png)

### Conclusion

In conclusion, DeepSeek Janus Pro 7B is a groundbreaking multimodal framework designed to unify and optimize tasks involving multimodal understanding and text-to-image generation. By leveraging its decoupled visual encoding and unified transformer architecture, it surpasses traditional unified models while maintaining the flexibility and simplicity needed for diverse applications. With detailed installation guidelines and compatibility with advanced GPU setups, Janus Pro is well-suited for researchers and developers aiming to explore the next frontier of multimodal capabilities. Its robust performance and innovative design mark it as a promising tool for future advancements in vision-language integration.