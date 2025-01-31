# LLM Demo

## 简介
这是一个用于展示LLM模型的demo

## 安装
```bash
git clone https://github.com/your-repo/project-name.git
cd project-name
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## deepspeek rag demo
 
### 启动ollama

```bash
ollama start
```
```bash
ollama pull deepseek-r1:1.5b
ollama run deepseek-r1:1.5b
```
 
```bash
streamlit run deepspeek_rag.py
```