#coding=utf-8

import xlrd
import xlwt
def read_tables():
    xlsx = xlrd.open_workbook('/Users/ph/desktop/testcases.xlsx')  # 打开表格 testcases.xlsx
    print xlsx.sheet_names()  # 打印表格中所有的sheet名
    sheet1_name = xlsx.sheet_names()[0]  # 获取第一个sheet名
    sheet2_name = xlsx.sheet_names()[1]  # 获取第二个sheet名
    print sheet1_name, sheet2_name

    sheet2 = xlsx.sheet_by_index(1)  # 根据sheet索引获取sheet内容
    sheet2 = xlsx.sheet_by_name('pay_by_wechat')  # 根据名称获取sheet内容

    print sheet2.name
    print 'sheet2的行数：' + str(sheet2.nrows)
    print 'sheet2的列数：' + str(sheet2.ncols)

    # 获取单元格内容的三种方式 ()里两个数字分别代表行和列的索引
    print sheet2.cell(0, 0).value.encode('utf-8')
    print sheet2.cell_value(0, 1).encode('utf-8')
    print sheet2.row(1)[1].value.encode('utf-8')

    print sheet2.cell(0, 1).ctype  # 获取值得数据类型 返回数字意义： 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error

    # 获取Excel表格值得步骤
    table = xlrd.open_workbook('/users/ph/desktop/testcases1.xlsx')
    sheet1 = table.sheet_by_index(0)
    print sheet1.cell(0, 0).value.encode('utf-8')
    for i in range(7):
        for j in range(13):
            print sheet1.cell_value(j, i).encode('utf-8')

def set_style(name,height,bold=False):
    style=xlwt.XFStyle() #初始化样式
    font=xlwt.Font() #为样式创建字体
    font.name=name
    font.bold=bold
    font.color_index=4
    font.height=height
    style.font=font

    return style

def write_table(): #可能是Excel版本有问题，创建的表格打开后看不到内容。
    table=xlwt.Workbook() # 创建工作簿
    sheet1=table.add_sheet('sheet1',cell_overwrite_ok=True)
    row0=[u'id',u'姓名',u'年龄',u'性别',u'分数',u'合计']
    clumn0=['1','2','3','4','5']

    # 生成第一行
    for i in range(len(row0)-1):
        sheet1.write(0,i,row0[i],set_style(u'微软雅黑',12,True))


    for i in range(len(clumn0)-1):
        sheet1.write(i+1,0,clumn0[i],set_style(u'微软雅黑',12,True))

    table.save('/users/ph/desktop/w.xls')
    sheet1.write(1,1,'hello')


if __name__ =='__main__':
    read_tables()
    write_table()
    print('change')








