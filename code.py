from fpdf import FPDF
import zipfile
from PIL import Image
import os
import shutil

failList = []

path = 'D:\\CIRNO\\zips'
#path = 'test'

def makePdf(zipName, pdfFileName, listPages):
	width = 0
	height = 0
	for page in listPages:
		current = Image.open('temp\\' + page)
		if (width,height) == current.size:
			break
		else:
			width, height = current.size

	pdf = FPDF(unit = "pt", format = [width, height])
	for page in listPages:
		pdf.add_page()
		try:
			pdf.image('temp\\' + page, 0, 0)
		except:
			print(zip + '生成失败\n')
			failList.append(zip)
			return
	pdf.output(pdfFileName, "F")
	print(zip + '生成成功\n')

zipList = os.listdir(path)

for zip in zipList:
	z = zipfile.ZipFile(path + '\\' + zip, "r")
	fileList = z.namelist()
	print(zip + '解压中...\n')
	for f in fileList:
		z.extract(f, 'temp')
	print(zip + '解压完毕\n')
	makePdf(zip, 'result\\' + zip + '.pdf', fileList)
	z.close()
	shutil.rmtree('temp')

print('生成失败的文件：\n')
for fail in failList:
	print(fail + '\n')

os.system('pause')
