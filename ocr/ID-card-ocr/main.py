import easyocr
import os

# 身份证所在文件夹
images = './images'
# 创建OCR的reader对象，识别中英文（使用GPU速度更快）
ocr = easyocr.Reader(['ch_sim', 'en'], gpu=False)
# 识别图片文字
content = ocr.readtext(images, detail=0)
# 遍历所有图片并识别文字，切片提取有效信息
data = []
for image in os.listdir(images):
    content = ocr.readtext(f'{images}/{image}', detail=0)
    print(f"正在识别：{image}")
    name = content[0][4:]
    gender = content[1][-1]
    nation = content[2][-1]
    birth = content[-5]
    if "月" not in birth:
        birth = content[-6] + "月" + content[-5]
    if "日" not in birth:
        birth = birth[:-1] + "日"
    address = content[-4][4:] + content[-3]
    number = content[-1]
    print(f"完成识别: {image}")
    print("-" * 50)
    data.append([name, gender, nation, birth, address, number])