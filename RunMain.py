from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from watchlisttable import Ui_WatchList
from listwindow import Ui_HomeWindow
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from operator import itemgetter
import urllib.request, json
import requests
import sys
import csv
import time


class BuildList(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_HomeWindow()
		self.ui.setupUi(self)
		self.ui.AddButton.clicked.connect(self.addToList)
		self.ui.RemoveButton.clicked.connect(self.removeFromList)
		self.ui.SaveButton.clicked.connect(self.saveAndClose)


########################################################################
# Full company list and watch list are read in from csv, sorted, 
# and written into their appropriate list widget gui
########################################################################
	
	def fillLists(self):
		
		companyInfo = []	# hold list of companies from csv
		watchListInfo = []	# hold list of companies selected for watch list
		
		# read all companies into list
		try:
			with open('Sectors/TechCompanyList.csv') as csvCompany:
				csvReader = csv.reader(csvCompany)
				for row in csvReader:
					companyInfo.append(row)
		except:
			print("error reading in company csv")

		# read companies previously selected into watch list
		try:
			with open('WatchList/WatchList.csv') as csvWatch:
				csvReader = csv.reader(csvWatch)
				for row in csvReader:
					watchListInfo.append(row)
		except:
			print("error reading in watch list csv")
			
		# sort both lists
		try:
			companyInfo = sorted(companyInfo, key=itemgetter(1))
		except:
			print("error in sorting company")
		try:
			watchListInfo = sorted(watchListInfo, key=itemgetter(1))
		except:
			print("error sorting watchlist")
		
		# populate main list, skip company if it's in watchlist
		try:	
			for company in companyInfo:
				if company not in watchListInfo:
					self.ui.MainList.addItem(company[0] + " | " + company[1])
		except:
			print("error adding to MainList")
		
		# populate watch list
		try:	
			for company in watchListInfo:
				self.ui.UserList.addItem(company[0] + " | " + company[1])
		except:
			print("error adding to UserList")
			
########################################################################
# All items from user list are written to csv and program is closed
########################################################################

	def saveAndClose(self):
		print("save and close")
		items = []
		for index in range(0, self.ui.UserList.count()):
			lineInList = self.ui.UserList.item(index).text()
			lineInList = lineInList.split('|')
			items.append([lineInList[0].strip(), lineInList[1].strip()])
			
		with open('WatchList/WatchList.csv', mode='w') as watchList_csv:
			wr = csv.writer(watchList_csv, lineterminator = '\n')
			for line in items:
				wr.writerow(line)
		self.hide()

########################################################################
# Add selected item to user list and remove from main list	
########################################################################
	def addToList(self):
		try:
			itemIndex = self.ui.MainList.currentRow()
			item = self.ui.MainList.takeItem(itemIndex)
			item = item.text()
			self.ui.UserList.addItem(item)
			
		except:
			print("error moving from main to user")
		
########################################################################
# Remove selected item from user list and insert back to main list	
########################################################################	
	def removeFromList(self):
		try:
			itemIndex = self.ui.UserList.currentRow()
			item = self.ui.UserList.takeItem(itemIndex)
			item = item.text()
			self.ui.MainList.addItem(item)
			
		except:
			print("error moving from main to user")

########################################################################
########################################################################
# CreateWatchList Class
########################################################################
########################################################################

class CreateWatchList(QtWidgets.QMainWindow):
	def __init__(self):
		super(CreateWatchList, self).__init__()
		self.ui = Ui_WatchList()
		self.ui.setupUi(self)
		self.ui.RefreshButton.clicked.connect(self.pullDataStream)
		
		# make table cells not editable
		self.ui.WatchTableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
		
		self.ui.AddRemoveButton.clicked.connect(self.openWatchListBuilder)
		self.ui.bl = BuildList()
		self.ui.bl.fillLists()
		
########################################################################
# Pull the companies from the user-created csv file
########################################################################

	def getWatchListCSV(self):
		watchListInfo = []
		
		# read companies previously selected into watch list
		try:
			with open('WatchList/WatchList.csv') as csvWatch:
				csvReader = csv.reader(csvWatch)
				for row in csvReader:
					watchListInfo.append(row)
		except:
			print("error reading in watch list csv")
			
		wlSize = len(watchListInfo)
		
		watchListInfo = sorted(watchListInfo, key=itemgetter(1))
		
		self.ui.WatchTableWidget.setColumnCount(4)
		
		self.ui.WatchTableWidget.setRowCount(wlSize)
		
		self.ui.WatchTableWidget.setHorizontalHeaderLabels([
			'Symbol',
			'Company',
			'Change ($)',
			'Price'
		])
		
		wlSize = len(watchListInfo)
		for i in range(0, wlSize):
				lineSize = len(watchListInfo[i])
				for j in range(0, lineSize):
					self.ui.WatchTableWidget.setItem(i, j, QTableWidgetItem(watchListInfo[i][j]))

				
########################################################################
# Use the API to get the data for the companies in the list
########################################################################	

	def pullDataStream(self):
		self.getWatchListCSV()
		start = time.time()
		urlStart = "https://cloud.iexapis.com/beta/stock/"
		urlEnd = "/quote?token=<API KEY>"
		
		latestPrice = 0
		changeDollar = 0
		
		rowCounter = self.ui.WatchTableWidget.rowCount()
		
		for i in range(0, rowCounter):
			companySymbol = self.ui.WatchTableWidget.item(i, 0).text()
			print(companySymbol)
			
			# Combine the two parts of the URL with the company symbol
			# for the API call
			fullUrl = urlStart + companySymbol + urlEnd
			
			# API call to pull current data for company by symbol
			try:
				with urllib.request.urlopen(fullUrl) as url:
					data = json.loads(url.read().decode())
					getLatestPrice = round(float(data['latestPrice']), 3)
					
					# Get latest price
					latestPrice = QTableWidgetItem(str(getLatestPrice))
					latestPrice.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
					
					# Round values of amount changed
					getChange = round(float(data['change']), 3)
					change = QTableWidgetItem(str(getChange))
					
					# Color the positive/negative values
					if getChange < 0:
						change.setForeground(QBrush(QColor(255,0,0)))
					if getChange > 0:
						change.setForeground(QBrush(QColor(0,153,51)))
					
					# Fix alignment within table cells
					change.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
					self.ui.WatchTableWidget.setItem(i, 3, QTableWidgetItem(latestPrice))
					self.ui.WatchTableWidget.setItem(i, 2, QTableWidgetItem(change))

			except:
				print('error with updating price')
			
		end = time.time()
		print(end - start)
########################################################################
# Use to open the list builder from add/remove button
########################################################################		
	def openWatchListBuilder(self):
		self.ui.bl.show()

	
########################################################################
# Main
########################################################################
def main():
	
	app = QtWidgets.QApplication([])
	bList = BuildList()
	wList = CreateWatchList()
	wList.getWatchListCSV()
	wList.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
