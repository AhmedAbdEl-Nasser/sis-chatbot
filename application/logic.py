from application import routes, utilities, app
from fpdf import FPDF
from flask import url_for

# Data authentication
def myQuery(std_id):
    return utilities.Student.query.filter_by(id=std_id).first()

# Define a costume pdf template
class myPDF(FPDF):
    def header(self):
        # Logo
        self.image('application/static/images/FOE.png', 10, 12, 30, 30)
        # Arial bold 15
        self.set_font('Arial', 'B', 18)
        # Move right
        self.cell(65)
        # Title
        self.cell(60, 20, "Ain Shams University", 0, 0, 'C')
        self.ln(8)
        self.cell(65)
        self.set_font('Arial', 'B', 14)
        self.cell(60, 20, "Fuculty of Engineering", 0, 0, 'C')
        self.ln(10)
        self.cell(65)
        self.set_font('Courier', '', 18)
        self.cell(60, 20, "Student Transcript", 0, 0, 'C')
        # Logo
        self.image('application/static/images/AinShamsUniv.png', 170, 8, 30, 30)
        # Line break
        self.ln(30)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 10)
        # Page number
        self.cell(0, 10, 'This document is part of a student project and is not official', 0, 0, 'C')


def GenerateTranscript(std_id):
    pdf =myPDF()
    pdf.add_page()
    pdf.set_font('Times', size = 18)

    std = utilities.Student.query.filter_by(id=std_id).first()

    pdf.cell(200,10, "Student name: " + std.name, ln=1, align='L')
    pdf.cell(200,10, "Student ID: " + std.id, ln=1, align='L')
    pdf.cell(200,10, "Level: " + str(std.level.name), ln=1, align='L')
    pdf.cell(200,10, "Passed hours: " + str(std.ph), ln=1, align='L')
    pdf.cell(200,10, "GPA: " + str(std.gpa), ln=1, align='L')

    pdf.output(name = "application/static/client/pdf/" + std_id + ".pdf", dest = 'F')


def GetPDFURL(std_id):
    return routes.getpdf(std_id + ".pdf")
    #with app.test_request_context():
        #return url_for('getpdf', pdf_id=std_id)