import os

# 当前目录
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# LLM_MODEL_PATH = r"D:\Project\ChatPdf\chatglm2-6b-int4"  
LLM_MODEL_PATH = "THUDM/chatglm2-6b" # 对话模型

# EMBEDDING_MODEL_PATH = r'D:\Project\ChatPdf\text2vec-base-chinese' 
EMBEDDING_MODEL_PATH = 'maidalun1020/bce-embedding-base_v1'  # 检索模型文件 or huggingface远程仓库

PDF_FILE_PATH = r""
KNOWLEDGE_FILE_PATH = "/Users/lucien/PdfReader-LangChian-LLM/cache"
