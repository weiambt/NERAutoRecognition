import win32com.client as win32
import os
from docx import Document

# win32.gencache.EnsureDispatch这个方法如果放到循环里就会报出：内存超出的错误

def doc_to_docx(doc_path, docx_path):
    # 启动 Word 应用程序
    word = win32.gencache.EnsureDispatch('Word.Application')
    word.Visible = False  # 不显示 Word 界面

    try:
        # 打开 doc 文件
        doc = word.Documents.Open(doc_path)

        # 另存为 docx 格式
        doc.SaveAs(docx_path, FileFormat=16)  # 16 是 Word 2007+ 的 DOCX 格式

        # 关闭文档（不保存更改）
        doc.Close(False)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # 退出 Word 应用程序
        word.Quit()

def doc_to_docx2(word,doc_path, docx_path):
    # 打开 doc 文件
    doc = word.Documents.Open(doc_path)

    # 另存为 docx 格式
    doc.SaveAs(docx_path, FileFormat=16)  # 16 是 Word 2007+ 的 DOCX 格式

    # 关闭文档（不保存更改）
    doc.Close(False)


def read(file_path):
    doc = Document(file_path)
    # 一篇doc文档
    full_text = []
    for para in doc.paragraphs:
        print(para.text)
        # full_text.append(para.text)

def batch_doc_to_docx(old_dir_path,new_dir_path):
    if not os.path.exists(new_dir_path):
        os.makedirs(new_dir_path)
    for filename in os.listdir(old_dir_path):
        if filename.endswith('.doc'):
            doc_path = os.path.join(old_dir_path, filename)
            docx_path = os.path.join(new_dir_path, filename.split('.')[0] + '.docx')
            doc_to_docx(doc_path, docx_path)

def batch_doc_to_docx2(old_dir_path,new_dir_path):
    if not os.path.exists(new_dir_path):
        os.makedirs(new_dir_path)
    # 启动 Word 应用程序
    word = win32.gencache.EnsureDispatch('Word.Application')
    word.Visible = False  # 不显示 Word 界面
    try:
        for filename in os.listdir(old_dir_path):
            if filename.endswith('.doc'):
                doc_path = os.path.join(old_dir_path, filename)
                docx_path = os.path.join(new_dir_path, filename.split('.')[0] + '.docx')
                doc_to_docx2(word,doc_path, docx_path)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # 退出 Word 应用程序
        word.Quit()

if __name__ == '__main__':

    # 使用函数进行转换
    # doc_file = 'D:\\APersonal\\Agraduate\\AinGroup\\AProjects\\NER\\data_process\\上海中石化分公司燃爆事故.doc'
    # docx_file = 'D:\\APersonal\\Agraduate\\AinGroup\\AProjects\\NER\\data_process\\上海中石化分公司燃爆事故.docx'
    # doc_to_docx(doc_file, docx_file)

    # docx_file = 'D:\\APersonal\\Agraduate\\AinGroup\\AProjects\\NER\\data_process\\上海中石化分公司燃爆事故.docx'
    # read(docx_file)

    doc_dir = 'D:\\APersonal\\Agraduate\\AinGroup\\AProjects\\NER\\data_process\\爆炸'
    docx_dir = 'D:\\APersonal\\Agraduate\\AinGroup\\AProjects\\NER\\data_process\\爆炸_docx'
    # batch_doc_to_docx(doc_dir, docx_dir)

    batch_doc_to_docx2(doc_dir, docx_dir)


