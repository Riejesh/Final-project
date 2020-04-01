#!/usr/bin/env python3

import json
import locale
import sys
import os
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_revenue = {"revenue": 0}
  max_sales = {"sales": 0}
  max_yearly_sale = {}

  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item


    # TODO: also handle max sales
    item_sales = item["total_sales"]
    if item_sales > max_sales["sales"]:
      item["sales"] = item_sales
      max_sales = item

    # TODO: also handle most popular car_year
    item_year = item["car"]["car_year"]
    per_item_sales = item["total_sales"]

    if not item_year in max_yearly_sale:
      max_yearly_sale[item_year] = 0
    max_yearly_sale[item_year] += per_item_sales
  """Maximum value calculation. The value of the corresponding entry is obtained in summary"""
  Max_year = max(max_yearly_sale , key = max_yearly_sale.get)

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(format_car(max_sales["car"]), max_sales["total_sales"]),
    "The most popular year was {} with {} sales ".format((Max_year),max_yearly_sale[Max_year])
  ]
  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  os.getcwd()
  os.chdir("../")
  data = load_data("car_sales.json")
  summary = process_data(data)
  print(summary)
  # TODO: turn this into a PDF report

  report = SimpleDocTemplate("cars.pdf")
  styles = getSampleStyleSheet()
  report_title = Paragraph("Sales summary for last month", styles["h1"])
  report_blank = Paragraph("<br />" , styles["Normal"])
  report_line1 = Paragraph(summary[0], styles["Normal"])
  report_line2 = Paragraph(summary[1], styles["Normal"])
  report_line3 = Paragraph(summary[2], styles["Normal"])
  report_blank = Paragraph("<br />" , styles["Normal"])
  table_data=cars_dict_to_table(data)
  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
  report_blank = Paragraph("<br />" , styles["Normal"])
  
  report.build([report_title,report_blank,report_line1,report_line2,report_line3,report_blank,report_table])
  
  # TODO: send the PDF report as an email attachment


if __name__ == "__main__":
  main(sys.argv)


