#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it

# global GST, PST, purchase
PST = 0.05
GST = 0.025
test_item = 100

def get_gst(purchase):
    new_val = purchase * GST
    return new_val


def get_pst(purchase):
    new_val = purchase * PST
    return new_val


# def log_file(data):
#     with open("log.txt", "a") as write_file:
#         write_file.write(data)


def bill_of_sale(purchase):

    # Calculate GST, PST tax values separately; add to original purchase amount
    gst_tax = get_gst(purchase)
    pst_tax = get_pst(purchase)
    total_tax = gst_tax + pst_tax
    taxed_purchase = purchase + total_tax

    with open("log.txt", "a") as log_file:
        log_file.write("Amount of purchase: {0:.2f} \n".format(purchase))
        log_file.write("Provincial tax: {0:.2f} \n".format(pst_tax))
        log_file.write("Federal tax: {0:.2f} \n".format(gst_tax))
        log_file.write("Total tax: {0:.2f} \n".format(total_tax))
        log_file.write("Total sale: {0:.2f} \n".format(taxed_purchase))

    return taxed_purchase


bill_of_sale(test_item)