from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
my_path='Reciept.pdf' 
#C:\Users\Hp\Desktop\PDF Invoice Generation
from reportlab.lib.pagesizes import letter, A4

##############################################################################################################
c = canvas.Canvas(my_path)#,pagesize=letter)
c.setPageSize((1350,1050))
##############################################################################################################

##############################################################################################################
c.translate(inch,inch)
c.setFillColorRGB(0,0,0.25)
c.rect(0,890,1200,890,fill=1)
##############################################################################################################

##############################################################################################################
#'Ahmed Corrugation Machines'
c.setFillColorRGB(1,1,1) # font colour
c.setFont("Times-Bold", 40)
c.drawCentredString(8.6*inch,(13*inch)-20,'Ahmed Corrugation Machines')
##############################################################################################################
#Date
from  datetime import date
dt = date.today().strftime('%d-%b-%Y')
c.setFillColorRGB(0,0,0)
c.setFont('Times-Bold',22)
c.drawString(3.0*inch,11.2*inch,'Date:')
c.drawString(3.8*inch,11.2*inch,dt)
##############################################################################################################

##############################################################################################################
#Client Name
c.setFillColorRGB(0,0,0)
c.setFont('Times-Bold',22)
c.drawString(7.5*inch,11.2*inch,'Client Name:')
##############################################################################################################

##############################################################################################################
#Reciept Number
c.setFillColorRGB(0,0,0)
c.setFont('Times-Bold',22)
c.drawString(3.0*inch,10.67*inch,'Reciept No:')
##############################################################################################################

##############################################################################################################
#Client Contact No
c.setFillColorRGB(0,0,0)
c.setFont('Times-Bold',22)
c.drawString(7.5*inch,10.67*inch,'Client Contact No:')
##############################################################################################################


##############################################################################################################
#Rectangle Table
c.setFillColorRGB(0,0,0)
c.rect(0,3.2*inch,900,6.85*inch,fill=0)
##############################################################################################################

##############################################################################################################
#Total Rs:
c.setFillColorRGB(0,0,0)
c.setFont('Times-Bold',22)
c.drawString(12.8*inch,9.7*inch,'Total Rs:')

##############################################################################################################


##############################################################################################################
#Total Rs BOX 
c.setFillColorRGB(0,0,0)
c.rect(14.96*inch,9.55*inch,2.12*inch,.5*inch,fill=0)
##############################################################################################################

##############################################################################################################
#Rent Rs:
c.setFillColorRGB(0,0,0)
c.setFont('Times-Bold',22)
c.drawString(12.8*inch,9.1*inch,'Rent Rs:')

##############################################################################################################


##############################################################################################################
#Rent Rs BOX 
c.setFillColorRGB(0,0,0)
c.rect(14.96*inch,9.01*inch,2.12*inch,.5*inch,fill=0)
##############################################################################################################


##############################################################################################################
#Credit Rs:
c.setFillColorRGB(0,0,0)
c.setFont('Times-Bold',22)
c.drawString(12.8*inch,8.4*inch,'Credit Rs:')

##############################################################################################################


##############################################################################################################
#Credit Rs BOX 
c.setFillColorRGB(0,0,0)
c.rect(14.96*inch,8.35*inch,2.12*inch,.5*inch,fill=0)
##############################################################################################################


##############################################################################################################
#Credit Details:
c.setFillColorRGB(0,0,0)
c.setFont('Times-Bold',22)
c.drawString(12.8*inch,7.7*inch,'Credit Details:')

##############################################################################################################


##############################################################################################################
#Credit Details Rs BOX 
c.setFillColorRGB(0,0,0)
c.rect(15.0*inch,7.55*inch,2.12*inch,.5*inch,fill=0)
##############################################################################################################


##############################################################################################################
#Previous Balance:
c.setFillColorRGB(0,0,0)
c.setFont('Times-Bold',22)
c.drawString(12.8*inch,6.89*inch,'Previous Balance:')

##############################################################################################################


##############################################################################################################
#Credit Details Rs BOX 
c.setFillColorRGB(0,0,0)
c.rect(15.23*inch,6.77*inch,2.12*inch,.5*inch,fill=0)
##############################################################################################################

##############################################################################################################
#Previous Bill#:
c.setFillColorRGB(0,0,0)
c.setFont('Times-Bold',22)
c.drawString(12.8*inch,5.42*inch,'Previous Bill#:')

##############################################################################################################


##############################################################################################################
#Previous Bill BOX 
c.setFillColorRGB(0,0,0)
c.rect(15.0*inch,5.37*inch,2.12*inch,.5*inch,fill=0)
##############################################################################################################


##############################################################################################################
#Total Balance
c.setFillColorRGB(0,0,0)
c.setFont('Times-Bold',22)
c.drawString(12.8*inch,4.42*inch,'Total Balance:')

##############################################################################################################


##############################################################################################################
#Total Balance BOX 
c.setFillColorRGB(0,0,0)
c.rect(15.0*inch,4.37*inch,2.12*inch,.5*inch,fill=0)
##############################################################################################################


##############################################################################################################
c.setFont('Times-Bold',25)
c.drawString(9*inch,2.88*inch,'Muhammad Dawood Sheikh:')
c.setFont('Courier',25)
c.drawString(13.5*inch,2.88*inch,'+92-300-4279085')
##############################################################################################################

##############################################################################################################
c.setFont('Times-Bold',25)
c.drawString(9*inch,2.32*inch,'Ahmed Dawood Sheikh:')
c.setFont('Courier',25)
c.drawString(13.5*inch,2.32*inch,'+92-324-4023811')
##############################################################################################################

##############################################################################################################
c.setFont('Times-Bold',25)
c.drawString(9*inch,1.68*inch,'Farooq Mir:')
c.setFont('Courier',25)
c.drawString(13.5*inch,1.68*inch,'+92-321-4966690')
##############################################################################################################

##############################################################################################################
c.setFont('Times-Bold',25)
c.drawString(9*inch,1.12*inch,'Sheikh Muhammad Qasim:')
c.setFont('Courier',25)
c.drawString(13.5*inch,1.12*inch,'+92-305-4129775')
##############################################################################################################
##############################################################################################################
c.setFont('Times-Bold',25)
c.drawString(9*inch,1.68*inch,'Farooq Mir:')
c.setFont('Courier',25)
c.drawString(13.5*inch,1.68*inch,'+92-321-4966690')
##############################################################################################################


##############################################################################################################
c.setFont('Times-Bold',25)
c.drawString(9*inch,0.55*inch,'PTCL:')
c.setFont('Courier',25)
c.drawString(13.5*inch,0.55*inch,'042-37149081')
##############################################################################################################

c.showPage()
c.save()