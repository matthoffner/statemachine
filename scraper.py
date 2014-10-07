import requests, re, time
from BeautifulSoup import BeautifulSoup
from datetime import date
start = time.time()
year = date.today().year
month = date.today().month
day = date.today().day
#states = []
#for option in BeautifulSoup(requests.get("http://cfpub.epa.gov/flpp/searchrrp_firm.htm").content).find("select", {"name":"state_2"}).findAll("option")[1:]:
#	states.append(option['value'])
#for state in states:
#	print state
#f = open("led_c_%sepa_20140710_000.csv"%"TX-Texas".split("-")[0], "w")
f = open("led_c_%sepa_%s%s%s_000.csv"%("TX-Texas".split("-")[0], str(year), str(month).zfill(2), str(day).zfill(2)), "w")
#f.write("Name, Address, City, State, Zip, Email, Phone, Lead Dust Sampling Technician, Renovation, License Number, Expiration Date\n")
f.write("entity_name, address1, city, state, zip, email, phone, qualifying_individual, primary_specialty, license_number, expiration_date\n")
try:
	for tr in BeautifulSoup(requests.get("http://cfpub.epa.gov/flpp/printRRP.cfm?Applicant_Type=FIRM&Sort_By=&static=false&qlat=&qlong=&Discipline=Renovator&TxtLocation=&distance_1=50&state_2=" +"TX-Texas"+ "&Applicant_Name_Option=1&Applicant_Name=&Certificate_number=&doSearch=Yes&redirect=%2Fflpp%2Fsearchrrp.cfm&print=Yes").content.replace("&nbsp;", "").replace("<br />", "\",\"").replace("<br>", "\",\"")).find("table", {"border":"1"}).findAll("tr")[2:]:
		info = []
		for td in tr.findAll("td"):
			info.append(td.text.strip())
		try:
			info = (re.sub("\s\s*", " ", "\",\"".join(info))).split("\",\"")
			if "(" in info[3]:	
				info.insert(3, "")
			info[2] = "\",\"".join(info[2].strip().replace(",", "").rsplit(" ", 2))
			info = "\",\"".join(info).split("\",\"")
			if len(info) == 11:
				f.write("\"" + "\",\"".join(info) + "\"\n")
		except:
			pass
except Exception, e:
	print str(e)
f.close()
print time.time()-start
