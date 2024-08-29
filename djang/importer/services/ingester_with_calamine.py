
from python_calamine import CalamineWorkbook
from importer.services import xsls_ingester
import traceback

class Ingester_whith_calamine(xsls_ingester.xls_ingester):
    

    def __init__(self):
        super().__init__()

    def get_sheetnames(self, wb):
        return wb.sheet_names
    
    def getSheet(self, wb, sn):
            for sn1 in sn:
                ws = wb.get_sheet_by_name(sn1)
                if ws != None:
                    return ws
            return None   

    def parse_first_tab(self, wb, sn, tab):
        # from first tab get report date, company, track name and track code
        # optinally get report summary as well
        self.put_header_fields(self.reference_objects)
        for field in tab["fields"]:
            if field["type"] == 'generated':
                continue
            else:
                worksheet = self.getSheet(wb, sn)
                if worksheet is not None:    
                    workarray = worksheet.to_python(skip_empty_area=False)

                    for row in workarray[0:3]:
                        i = -1
                        for cell in row:
                            i += 1
                            found = False
                            if cell is not None and cell != '':
                                if str(cell).startswith("{PL}PickLst"):
                                    break
                                stripped = str(cell).replace(
                                    '*', '').replace(":", "").strip()
                                for field1 in tab["fields"]:
                                    # in some of the reports there are multiple * characters of column titles as pointers to comments
                                    if stripped in field1["column_title"]:
                                        found = True
                                        #j = 1
                                        #for i in range(1, 4):
                                        val = row[i + 1]
                                        if val is not None:
                                            self.reference_objects = self.put_in_model(
                                               self.reference_objects, field1, val)
                                            break
                                        break
                                    elif field1["type"] == "reference":
                                        self.reference_objects = self.put_in_model(
                                            self.reference_objects, field1, None)
                                break
                self.save_first_tab()        
               
                return        

    def ingest(self, filename, file_stream):
        try:
            self.file = filename  
            wb = CalamineWorkbook.from_path(filename)
            self.parse_spreadsheet(wb)
            return True
        except ValueError: 
            
            #traceback.print_exc()
            print("report already exists")
            return False

        except Exception as e:
            # log failed files
            traceback.print_exc()
            fni = importer.models.FilesNotIngested()
            fni.file_name = filename
            fni.info = "Failed to read workbook\n\r"+str(e)
            fni.save()
            return False