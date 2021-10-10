#! /usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph


def generate_report(attachment, title, paragraph):
    report = SimpleDocTemplate(attachment)

    styles = getSampleStyleSheet()

    report_title = Paragraph(title,styles['h1'])
    report_paragraph = Paragraph(paragraph)

    report.build([report_title, report_paragraph])


