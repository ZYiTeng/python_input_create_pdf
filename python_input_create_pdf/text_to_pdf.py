from fpdf import FPDF
# coding=utf-8

pdf = FPDF()
pdf.add_page()
pdf.add_font('msjh', '', '微軟正黑體.ttf', uni=True)
pdf.set_font('msjh', '', 16)
pdf.set_margin(0)

product_name = input("產品名稱:")
print("產品:{}".format(product_name))
MD_date = input("輸入製造日期:")
print("生產日:{}".format(MD_date))
EX_date = input("輸入有效日期:")
print("有效日期:{}".format(EX_date))
quantity = input("輸入需要張數:")
print("數量:{}".format(quantity))
quantity = int(quantity)
all_text = product_name + '\n' + '有效日期\n' + EX_date + '\n' + '生產日 ' + MD_date

row = int((quantity/3)+2)
num = 4
col_width = pdf.epw / 3 # distribute content evenly
line_height = 59.3
for i in range(1,row):
    for j in range(1,num):
        if pdf.will_page_break(line_height):
            pdf.cell(0.6,0.6,'') #應付換頁問題
        pdf.multi_cell(col_width, line_height, all_text, border=0, ln=3, align = 'C', max_line_height=pdf.font_size)
    if(quantity-(i*3)<3):
        num = quantity-(i*3)+1
    pdf.ln(line_height)

pdf.output(product_name +'.pdf','F')