import importer
from importer import models
import openpyxl
from openpyxl import load_workbook
import os
import datetime
import traceback
import argparse
import json
import datetime
from dateutil import parser

MAPPING_FILE = "./importer/field_mapping.json"

class xls_ingester(object):
    file = None
    wb = None
    with open(MAPPING_FILE) as json_data:
            mapping = json.load(json_data)
    reference_objects = dict()        

    def __init__(self):
        super().__init__()
        
	
    def find_sn(self, wb):
        sheet_name_array = wb.sheetnames
        for sn in sheet_name_array:
            # ignore dynamic pick lists that exists in some of the reports
            if sn.startswith("{PL}PickLst"):
                sheet_name_array.remove(sn)           
        for tab in self.mapping:
            sn = tab["tab_name"]
            if sn != "any":
                self.parse_first_tab(wb, sn, tab)
                sheet_name_array.remove(sn)
                ws = wb[sn]
                fields = tab["fields"]
                for field in fields:
               	    if field["type"] == "generated":
                        continue
                        #print(field["column_title"])   
            #print(tab)
        return sheet_name_array, tab

    def find_title_row(self, ws, field_name):
     	#print(field_name)
        for row in ws.iter_rows():
            for cell1 in row:
                if cell1.value is not None:
                    if cell1.value in field_name:
                   		#print("cell="+cell1.value)
                        return cell1.row
                
    def get_value_for(self, ws, field_name):
        for row in ws.iter_rows():
            for cell in row:
                if cell1.value is not None:
               	    if cell.value == field_name:
                        if ws.cell(row=cell1.row+1,column=cell1.column).value is not None:
                        	#print(ws.cell(row=cell1.row+1,column=cell1.column).value)
                            return ws.cell(row=cell1.row+1,column=cell1.column).value

    def put_header_fields(self, reference_objects):
        # special treatment - on report put the kupa, filename and ingestion date
        field = {"class_name": "importer.models.Kupot",
					"field_name": "kupa",
					"column_title": ["kupa"],
					"type": "extracted",
					"ref_name":"kupa"}
        self.reference_objects = self.put_in_model(self.reference_objects, field, None)             
        field = {"class_name": "importer.models.Reports",
					"field_name": "file_name",
					"column_title": ["file_name"],
					"type": "extracted",
					"ref_name":"reports"}
        val = self.file
        self.reference_objects = self.put_in_model(self.reference_objects, field, val)
        field = {"class_name": "importer.models.Reports",
					"field_name": "ingested_at",
					"column_title": ["ingested_at"],
					"type": "extracted",
					"ref_name":"reports"}
        val = datetime.datetime.now()
        self.reference_objects = self.put_in_model(self.reference_objects, field, val) 
       
    def parse_first_tab(self, wb, sn, tab):
		# from first tab get report date, company, track name and trach code
		# optinally get report summary as well
        self.put_header_fields(self.reference_objects)           
        for field in tab["fields"]:
            if field["type"] ==  'generated':
                continue
            else:
                for row in wb[sn].iter_rows(min_row=1, max_row=4, max_col=4,values_only=False):	
                   for cell in row:
                    found = False
                    if cell.value is not None:
                        if str(cell.value).startswith("{PL}PickLst"):
                            break
                        stripped = str(cell.value).replace('*','').replace(":","").strip()
                        for field in tab["fields"]:
                       		#in some of the reports there are multiple * characters of column titles as pointers to comments
                            if stripped in field["column_title"]:
                                found = True
                                i = 1
                                for i in range(1,4):
                                    val = wb[sn].cell(row=cell.row,column=cell.column+i).value
                                    if val is not None:
                                        self.reference_objects = self.put_in_model(self.reference_objects, field, val)
                                        break
                                break
                            elif field["type"] == "reference":
                                self.reference_objects = self.put_in_model(self.reference_objects, field, None)
                        break
                for o in self.reference_objects.values():
                    try:
                        o.save()
                    except Exception as e:
                        traceback.print_exc()      
                return

    def put_in_model(self, objects, field, value):
        o = obj = None
        try:
            if field["ref_name"] in objects:
                obj = objects[field["ref_name"]]
            if obj is not None and str(type(obj)) == "<class '"+field["class_name"]+"'>":
                o = obj
            if o is None:        
                o = eval(field["class_name"]+"()")
                objects[field["ref_name"]] = o
            if field["type"] == "reference":
                value = objects[field["field_name"]]
            if value is not None and value != "None" and value != '':   
                if("date" in field["field_name"]):
                    value = parser.parse(value).date() 
                setattr(o,field["field_name"],value)
        except Exception as e:
            traceback.print_exc()           
        return objects



    def parse_spreadsheet(self, wb):
        sheet_name_array , tab = self.find_sn(wb)
        for sh in sheet_name_array:
            titles = list()
            column_idxs = list()
       	    column_list = []
            title_row = 0
            # find title row in tab    
            for field in tab["fields"]:
                if field["type"] ==  'generated':
                    continue
                if field["type"] ==  'extracted':
                    if title_row == 0 :
                        tr = self.find_title_row(wb[sh], field["column_title"])
                        if tr is not None:
                            title_row = tr
                            break
            # find row of values 
            for row in wb[sh].iter_rows(min_row=title_row, max_row=title_row,values_only=False):
                for cell in row:
                    found = 0
                    if cell.value is not None:
                        if str(cell.value).startswith("{PL}PickLst"):
                            break
                        #in some of the reports there are multiple * characters of column titles as pointers to comments
                        stripped = str(cell.value).replace('*','').strip()
                        for field in tab["fields"]:
                            if field["type"] ==  'reference':
                                found += 1
                                column_idxs.append(found)
                                column_list.append(field)
                            if field["field_name"] == "category":
                                found += 1
                                column_idxs.append(found)
                                column_list.append(field)
                            if stripped in field["column_title"]:
                                found += 1
                                column_idxs.append(cell.column)
                                column_list.append(field)
                            if found == 3:    
                                 break
                        if found > 3:    
                            # filed not found in mapping - log
                            uf = importer.models.UnmappedFields()
                            uf.file_name = self.file
                            uf.tab_name = sh
                            uf.field = str(cell.value)
                            uf.save()
            done = False            
            for row in wb[sh].iter_rows(min_row=title_row+1):
                skip = False   
                # clear details object as each row is a new details record
                if "details" in self.reference_objects:
                    del self.reference_objects["details"]
                # put data in details object 
                for i in range(len(column_idxs)):
                    field = column_list[i]
                    if field["type"] ==  'reference':
                        value = None
                    elif field["field_name"] == "category":
                        value = sh
                    else:
                        value = str(row[column_idxs[i]-1].value)
                    # special treatment - stock_name must be populated or row is not a data row    
                    if "stock_name" == field["field_name"] and (value is None or value == 'None' or value == ''):
                           skip = True
                           break 
                    # special treatment - row starting with * signals end of data     
                    if '*' in str(value):
                        done = True    
                    else:   
                        self.reference_objects = self.put_in_model(self.reference_objects, field, value)
                    if done:
                        break
                if not skip:
                    for o in self.reference_objects.values():
                        try:
                            o.save()
                        except Exception as e:
                            traceback.print_exc()      
                if done: 
           	        break
    
    def ingest(self, file):
        try:
            self.file = file
            wb = load_workbook(file)
            wb.calculation.calcOnLoad = True
            self.parse_spreadsheet(wb)
            self.reference_objects.clear()
        except Exception as e:
            # log failed files
            traceback.print_exc()
            fni = importer.models.FilesNotIngested()
            fni.file_name = file
            fni.info = str(e)
            fni.save()

def xls_import(path, file):
    if path is None:
        ingester = xls_ingester()
        ingester.ingest(file)
    else:
        files = os.listdir(path)
        files = [os.path.join(path, f) for f in files if not f.startswith(".")]
        for f in files:
            ingester = xls_ingester()
            ingester.ingest(f)


def main():  # Main
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--full_file_name', type=str)
    parser.add_argument('-d', '--path', type=str)
    args = parser.parse_args()
    if args.path is None and args.full_file_name is None:
        print("specify either single file or directory")
        return
    if args.path is not None and args.full_file_name is not None:
        print("specify either single file or directory")
        return
    xls_import(args.path, args.full_file_name)


if __name__ == '__main__':
    main()           
