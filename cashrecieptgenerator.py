from reportlab.lib.units import inch
from reportlab.pdfgen import canvas 

from reportlab.lib.pagesizes import letter, A4
import pandas as pd
import math as m
# Other List order
# Rent
# Credit Details
# Credit
# Debit
# Client Name
# Reciept Number
# Contact Number
# Date
# Previous Balance
# Previous Bill Number
# Total Balance

def generate_cash_reciept(df,other_list):
    my_path='Cash_Bills\\'
    my_path = my_path + str(other_list[4]) + "_" + str(other_list[5]) + "_" + str(other_list[6]) + ".pdf"
    ##############################################################################################################
    c = canvas.Canvas(my_path)#,pagesize=letter)

    page_count=m.ceil(df.shape[0]/9)
    
    current_page=1
    while(current_page<=page_count):

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
        dt = other_list[7]
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
        name = str(other_list[4])
        name = name.upper()
        c.drawString(10.67*inch,11.2*inch,name)
        ##############################################################################################################

        ##############################################################################################################
        #Reciept Number
        c.setFillColorRGB(0,0,0)
        c.setFont('Times-Bold',22)
        c.drawString(3.0*inch,10.67*inch,'Reciept No:')
        c.drawString(4.65*inch,10.67*inch,str(other_list[5]))
        ##############################################################################################################

        ##############################################################################################################
        #Client Contact No
        c.setFillColorRGB(0,0,0)
        c.setFont('Times-Bold',22)
        c.drawString(7.5*inch,10.67*inch,'Client Contact No: +')
        c.drawString(10.67*inch,10.67*inch,str(other_list[6]))
        ##############################################################################################################


        ##############################################################################################################
        #Rectangle Table
        c.setFillColorRGB(0,0,0)
        c.rect(0,0*inch,900,9.865*inch,fill=0)
        ##############################################################################################################

        ##############################################################################################################
        #Total Rs:
        c.setFillColorRGB(0,0,0)
        c.setFont('Times-Bold',22)
        c.drawString(12.8*inch,9.7*inch,'Debit Rs:')

        ##############################################################################################################


        ##############################################################################################################
        #Total Rs BOX 
        c.setFillColorRGB(0,0,0)
        c.rect(15.23*inch,9.55*inch,2.12*inch,.5*inch,fill=0)
        c.setFont('Times-Bold',19)
        c.drawString(15.7*inch,9.65*inch,str(other_list[3]))
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
        c.rect(15.23*inch,9.01*inch,2.12*inch,.5*inch,fill=0)
        c.setFont('Times-Bold',19)
        c.drawString(15.7*inch,9.12*inch,str(other_list[0]))
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
        c.rect(15.23*inch,8.35*inch,2.12*inch,.5*inch,fill=0)
        c.setFont('Times-Bold',19)
        c.drawString(15.7*inch,8.39*inch,str(other_list[2]))
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
        c.rect(15.23*inch,7.55*inch,2.12*inch,.5*inch,fill=0)
        c.setFont('Times-Bold',19)
        c.drawString(15.7*inch,7.63*inch,str(other_list[1]))
        ##############################################################################################################


        ##############################################################################################################
        #Previous Balance:
        c.setFillColorRGB(0,0,0)
        c.setFont('Times-Bold',22)
        c.drawString(12.8*inch,6.89*inch,'Previous Balance:')

        ##############################################################################################################
        c.setFillColorRGB(0,0,0)
        c.rect(15.23*inch,7.55*inch,2.12*inch,.5*inch,fill=0)
        c.setFont('Times-Bold',19)
        c.drawString(15.7*inch,6.862*inch,str(other_list[8]))

        ##############################################################################################################
        #Credit Details Rs BOX 
        c.setFillColorRGB(0,0,0)
        c.rect(15.23*inch,6.77*inch,2.12*inch,.5*inch)
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
        c.rect(15.23*inch,5.37*inch,2.12*inch,.5*inch)
        c.setFont('Times-Bold',19)
        c.drawString(15.7*inch,5.44*inch,str(other_list[9]))
        ##############################################################################################################


        ##############################################################################################################
        #Total Balance
        c.setFillColorRGB(0,0,0)
        c.setFont('Times-Bold',22)
        c.drawString(12.8*inch,4.51*inch,'Total Balance:')

        ##############################################################################################################


        ##############################################################################################################
        #Total Balance BOX 
        c.setFillColorRGB(0,0,0)
        c.rect(15.23*inch,4.37*inch,2.12*inch,.5*inch)
        c.setFont('Times-Bold',19)
        c.drawString(15.7*inch,4.4*inch,str(other_list[10]))
        ##############################################################################################################


        ##############################################################################################################
        # c.setFont('Times-Bold',25)
        # c.drawString(9*inch,2.88*inch,'Muhammad Dawood Sheikh:')
        # c.setFont('Courier',25)
        # c.drawString(13.5*inch,2.88*inch,'+92-300-4279085')
        # ##############################################################################################################

        # ##############################################################################################################
        c.setFont('Times-Bold',25)
        c.drawString(13.0*inch,3.0*inch,'Ahmed Dawood Sheikh:')
        c.setFont('Courier',25)
        c.drawString(13.0*inch,2.55*inch,'+92-324-4023811')
        # ##############################################################################################################

        # ##############################################################################################################
        c.setFont('Times-Bold',25)
        c.drawString(13.0*inch,2.0*inch,'Farooq Mir:')
        c.setFont('Courier',25)
        c.drawString(13.0*inch,1.55*inch,'+92-321-4966690')
        # ##############################################################################################################

        # ##############################################################################################################
        # c.setFont('Times-Bold',25)
        # c.drawString(9*inch,1.12*inch,'Sheikh Muhammad Qasim:')
        # c.setFont('Courier',25)
        # c.drawString(13.5*inch,1.12*inch,'+92-305-4129775')
        # ##############################################################################################################
        # ##############################################################################################################
        # c.setFont('Times-Bold',25)
        # c.drawString(9*inch,1.68*inch,'Farooq Mir:')
        # c.setFont('Courier',25)
        # c.drawString(13.5*inch,1.68*inch,'+92-321-4966690')
        # ##############################################################################################################


        # ##############################################################################################################
        c.setFont('Times-Bold',25)
        c.drawString(13.0*inch,1.0*inch,'PTCL:')
        c.setFont('Courier',25)
        c.drawString(13.0*inch,0.55*inch,'042-37149081')
        ##############################################################################################################


        ##############################################################################################################
        c.setFont('Times-Bold',22)
        c.drawString(35,9.56*inch,'Item')
    
        c.drawString(500,9.56*inch,'Price')
        
        ##############################################################################################################

        c.setFont('Times-Bold',25)


        ending_delimiter=(9*current_page)
        if df.shape[0]<(9*current_page):
            ending_delimiter=df.shape[0]

        # for i in range((9*current_page)-9,ending_delimiter):
        #     c.drawString(15.5,9.0*inch-(50*i),str(i+1))

        height=0
        for row in range((9*current_page)-9,ending_delimiter):
            x=0
            for col in df.columns:
                if x==0:
                    c.drawString(35,9.0*inch-(50*height),str(df[col][row]))
                elif x==1:
                    c.drawString(500.2,9.0*inch-(50*height),str(df[col][row]))
                else:
                    c.drawString(1000,9.5*inch-(50*height),str(df[col][row]))

                x=x+1
                #pass
            height=height+1
            ##############################################################################################################    
        current_page=current_page+1
        c.showPage()
    c.save()