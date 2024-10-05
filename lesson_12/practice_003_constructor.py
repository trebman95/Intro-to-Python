"""
Now that you can use a constructor, modify your Printer class so you can
pass the brand, model and paper capacity. Create an instance for each
of the following models:

   Brand       Model       Capacity
   HP          7955e       125 sheets
   Brother     HL-L2310D   250 sheets
   Canon       G4270       100 sheets

Add a print_document() instance method that receives a string and prints
it out. The printout should include the brand and model of the printer.
"""

class Printer: #class
    def __init__(self, brand, model, capacity): #constructor
        self.brand = brand #instance
        self.model = model #instance
        self.capacity = capacity # instance

    def print_document(self, document): #instance method
        print(f'{self.brand} {self.model} Printing: {document}')


hp = Printer('HP', '7955e', 125)
brother = Printer('Brother', '7HL-2310D', 250)
canon = Printer('Canon', 'G2470', 100)

hp.print_document('Hello HP!')
brother.print_document('Hello Brother!')
canon.print_document('Hello Canon!')

