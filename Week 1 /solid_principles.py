# Single Responsibility Principle

class Report:
    def get_content(self):
        return "Student Performance Report"


class ReportPrinter:
    def print_report(self, report):
        print(report.get_content())


report = Report()
printer = ReportPrinter()

printer.print_report(report)
