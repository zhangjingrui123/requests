'''
封装excel数据驱动方法
'''
import xlrd
def get_exceldata(sheetname,startrow,endrow,requestcol):         #表名，开始行数，结束行数，请求体
    excel_path = "../Config/酒店后台接口测试用例.xls"
    work_book = xlrd.open_workbook(excel_path,formatting_info=True)
    sheet_name = work_book.sheet_by_name(sheetname)
    datalist = []
    for row in range(startrow,endrow):
        cell_data = sheet_name.cell_value(row,requestcol)
        tc_number = sheet_name.cell_value(row,0)
        datalist.append((tc_number,cell_data))
    return datalist