from python_calamine import CalamineWorkbook
import traceback

filename = "/home/guyga/hasadna/penssion/xlsx-files/bad/512065202_p1560_p221.xlsx"

wb = CalamineWorkbook.from_path(filename)
print(str(wb))
#for name in wb.sheet_names:
#    ws = wb.get_sheet_by_name(name)
#    workarray = ws.to_python(skip_empty_area=True)
#   print("================== "+ws.name+" ==================================")
#   print(str(workarray))

ws = wb.get_sheet_by_name("מזומנים")
#index = wb.sheet_names.index("מזומנים")
#print("index="+str(index)+" name="+ws.name)
workarray = ws.to_python(skip_empty_area=True)
print(str(workarray[6]))
#rows = ws.rows()
#ws.load()
#for row in ws.iter_rows():
#    print(str(row))
##ws1 = wb.get_sheet_by_index(2)
#workarray = ws.to_python(skip_empty_area=True)
#workarray1 = ws1.to_python(skip_empty_area=True)
#print("workarray="+str(ws))
#for row in ws.iter_rows():
#    print(str(row))
print("====================================================")
#print("workarrya1="+str(ws1))
#for row in ws1.iter_rows():
#    print(str(row))