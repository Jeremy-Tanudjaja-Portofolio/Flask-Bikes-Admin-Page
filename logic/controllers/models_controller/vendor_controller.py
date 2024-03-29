class Vendor_Controller():

    def __init__(self, cursor, oracle):
        """Initialize the Vendor controller"""
        print("connection to Vendor succeeded")
        self.cursor = cursor
        self.oracle = oracle

    def get_vendor_data(self):
        """This Method will grab all the data from the vendor table"""
        data = []
        self.cursor.execute(
            f"select vendor_id, vendor_name, address "
            f"from vVendors")
        for vendor_id, vendor_name, address in self.cursor:
            data.append({"vendor_id": vendor_id,
                         "vendor_name": vendor_name,
                         "address": address})
        # print(data)
        print(len(data))
        return data

    def insert_new_vendor(self, data):
        """Call Insert Department Procedure to Insert Data"""
        # print(data)
        vendor_name = data.get('Vendor_Name')
        vendor_address = data.get('Address')
        try:
            self.cursor.execute(f"CALL NewVendor('{vendor_name}','{vendor_address}')")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Added"

    def delete_vendor(self, id):
        """Delete a Vendor From Reality"""
        vendor_id = id
        try:
            self.cursor.execute(f"Delete from vendors where VENDOR_ID = {vendor_id}")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Deleted"



    def update_vendor(self, id, data):
        vendor_name = data['update_vendor_name']
        vendor_address = data['update_vendor_address']
        vendor_id = id
        try:
            self.cursor.execute(f"Update vendors set vendor_name='{vendor_name}', address ='{vendor_address}'"
                                f"where VENDOR_ID = {vendor_id}")
            self.cursor.execute("commit")
        except self.oracle.DatabaseError as e:
            error_message = f"{e}"
            return error_message
        else:
            return "Data Successfully Updated"







