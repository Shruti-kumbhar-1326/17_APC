class Report:
    def generate(self):
        print("Generating report")


class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel Report")


class HTMLReport(Report):
    def generate(self):
        print("Generating HTML Report")


# Function that accepts any report object
def create_report(report):
    report.generate()


# Create objects
pdf = PDFReport()
excel = ExcelReport()
html = HTMLReport()

# Call function
create_report(pdf)
create_report(excel)
create_report(html)