# The python script adds the list of banks and their url as key-value pairs in a .json file as it will be quite a tedioud task to write it all down manually.
import re
import json

# Provided bank list
bank_list_text = """
Abhyudaya Co-op Bank	www.abhyudaya.com
Abu Dhabi Commercial Bank	www.adcb.com
Ahmedabad Mercantile Co-op Bank	www.amco-bank.com
Akola District Central Co-op Bank	akoladcc.com
Akola Janata Commercial Co-op Bank	www.akolajanatabank.com
Allahabad Bank	www.allahabadbank.com
Almora Urban Co-op Bank	almoraurbanbank.com
Andhra Bank	www.andhrabank.in
Andhra pradesh State Co-Op Bank	www.apcob.org
Andhra Pragathi Grameena Bank	www.apgb.co.in
Apna Sahakari Bank	www.apnabank.co.in
Australia and New Zealand Banking Group	www.anz.com
Axis Bank	www.axisbank.com
Bank of America	www.bankofamerica.com
Bank of Bahrain and Kuwait	www.bbkonline.com
Bank of Baroda	www.bankofbaroda.com
Bank of Ceylon	www.boc.lk
Bank of India	www.bankofindia.com
Bank of Maharashtra	www.bankofmaharashtra.in
Bank of Nova Scotia	www.scotiabank.com
Bank of Tokyo Mitsubishi UFJ	www.bk.mufg.jp/global/globalnetwork/asiaoceania/#India
Barclays Bank	www.barclays.in
Bassein Catholic Co-op Bank	www.bccb.co.in
Bharat Co-op Bank (Mumbai)	www.bharatbank.com
BNP Paribas	www.bnpparibas.com
Canara Bank	www.canarabank.com
Capital Local Area Bank	www.capitalbank.co.in
Catholic Syrian Bank	www.csb.co.in
Central Bank of India	www.centralbankofindia.co.in
China Trust Commercial Bank	www.chinatrustindia.com
Citi Bank	www.citibank.com
Citizen Credit Co-op Bank	www.citizencreditbank.com
City Union Bank	www.cityunionbank.com
Commonwealth Bank of Australia	www.commbank.co.in
Corporation Bank	www.corpbank.com
Cosmos Co-op Bank	www.cosmosbank.com
Credit Agricole Corporate and Investment Bank	www.ca-cib.com
Credit Suisse	www.credit-suisse.com
Delhi State Co-op Bank	plus.google.com/107903992827578686784/about?hl=en
Dena Bank	www.denabank.com
Deposit Insurance and Credit Guarantee Corporation	www.dicgc.org.in
Deutsche Bank	www.db.com
Development Bank of Singapore (DBS)	www.dbs.com
Development Credit Bank (DCB)	www.dcbbank.com
Dhanlaxmi Bank	www.dhanbank.com
Dombivli Nagari Sahakari Bank	www.dnsb.co.in
Federal Bank	www.federalbank.co.in
Firstrand Bank	firstrand.co.in
Gadchiroli District Central Co-op Bank	www.gdccbank.com
Gopinath Patil Parsik Janata Sahakari Bank	www.gpparsikbank.com
Greater Bombay Co-op Bank	www.greaterbank.com
Gujarat State Co-op Bank	www.gscbank.co.in
Gurgaon Gramin Bank	plus.google.com/115047032409973911708/about?hl=en
HDFC Bank	www.hdfcbank.com
HSBC	www.hsbc.co.in
ICICI Bank	www.icicibank.com
IDBI Bank	www.idbi.com
Indian Bank	www.indianbank.in
Indian Overseas Bank (IOB)	www.iob.in
Indonesia International Bank	www.bankbii.co.in
Indusind Bank	www.indusind.com
Industrial and Commercial Bank of China	www.icbc-ltd.com/icbcltd/en/
ING Vysya Bank	www.ingvysyabank.com
Jalgaon Janata Sahkari Bank (JJSB) Ltd	www.jjsbl.com
Jalgaon Peoples Co-op Bank	www.jpcbank.com
Jammu and Kashmir Bank	www.jkbank.net
Janakalyan Sahakari Bank Ltd	www.jksbl.com
Janaseva Sahakari Bank (Borivali)	janasevabank.in
Janaseva Sahakari Bank (Pune)	janasevabankpune.net
JP Morgan Chase Bank	www.jpmorgan.com
Kallappanna Awade Ichalkaranji Janata Sahakari (KAIJS) Bank	www.ijsbank.com
Kalupur Commercial Co-op Bank	www.kalupurbank.com
Kalyan Janata Sahakari Bank	kalyanjanata.in
Kangra Central Co-op Bank	www.kccb.in
Kapole Co-op Bank	www.kapolbank.com
Karad Urban Co-op Bank	www.karadurbanbank.com
Karnataka Bank	www.karnatakabank.com
Karnataka State Co-op Apex Bank	www.karnatakaapex.com
Karnataka Vikas Grameena Bank	www.kvgbank.com
Karur Vysya Bank (KVB)	www.kvb.co.in
Kotak Mahindra Bank	www.kotak.com
Kurmanchal Nagar Sahkari Bank	www.kurmanchalbank.com
Lakshmi Vilas Bank (LVB)	www.lvbank.com
Mahanagar Co-op Bank	www.mahanagarbank.com
Maharashtra State Co-op Bank	www.mscbank.com
Malabar Gramin Bank	keralagbank.com
Mashreq Bank	www.mashreqbank.com
Mizuho Co-op Bank	www.mizuhobank.com
Mumbai District Central Co-op Bank	www.mumbaidistrictbank.com
Municipal Co-op Bank (Mumbai)	www.municipalbankmumbai.com
Nagar Urban Co-op Bank	plus.google.com/118254408225094337228/about?gl=in&hl=en
Nagpur Nagrik Sahakari Bank	www.nnsbank.co.in
Nainital Bank	www.nainitalbank.co.in
Nasik Merchants Co-op Bank	www.nasikonline.com
National Australia Bank	nabasia.in
New India Co-op Bank	www.newindiabank.in
North Kanara GSB (NKGSB) Co-op Bank	www.nkgsb-bank.com
Nutan Nagarik Sahakari Bank	www.nutanbank.com
Oman International Bank	www.oib.co.om
Oriental Bank of Commerce	www.obcindia.co.in
Prathama Bank	www.prathamabank.org
Prime Co-op Bank	primebankindia.com
Punjab and Maharashtra Co-op Bank	www.pmcbank.com
Punjab and Sind Bank	www.psbindia.com
Punjab National Bank	www.pnbindia.in
RABO Bank International	www.rabobank.com
Rajaguru nagar Sahakari Bank	rajgurunagarbank.com
Rajasthan State Co-op Bank	www.rscb.org.in
Rajkot Nagarik Sahakari Bank	www.rnsbindia.com
Ratnakar Bank	ratnakarbank.co.in
Reserve Bank of India	www.rbi.org.in
Royal Bank of Scotland	www.rbs.in
Sahebrao Deshmukh Co-op Bank	sdcbankct.in
Saraswat Co-op Bank	www.saraswatbank.com
Sberbank of Russia	sberbank.ru
Seva Vikas Co-op Bank	www.sevavikasbank.com
Shamrao Vithal Co-op Bank	www.svcbank.com
Shinhan Bank	www.shinhanbankindia.com
Shri Chhatrapathi Rajarshi Shahu Urban Co-op Bank	www.shahubank.com
Societe Generale	www.sgcib.com
Solapur Janata Sahkari Bank	sjsbbank.com
South Indian Bank	www.southindianbank.com
Standard Chartered Bank	www.standardchartered.co.in
State Bank of Bikaner and Jaipur	www.sbbjbank.com
State Bank of Hyderabad	www.sbhyd.com
State Bank of India (SBI)	www.sbi.co.in
State Bank of Mauritius	www.sbmgroup.mu
State Bank of Mysore	www.statebankofmysore.co.in
State Bank of Patiala	www.sbp.co.in
State Bank of Travancore (SBT)	www.statebankoftravancore.com
Sumitomo Mitsui Banking Corporation	www.smbc.co.jp/global
Surat District Co-op Bank	www.sudicobank.com
Surat Peoples Co-op Bank	www.spcbl.in
Sutex Co-op Bank	www.sutexbank.in
Syndicate Bank	www.syndicatebank.in
Tamilnad Mercantile Bank (TMB)	www.tmb.in
Tamilnadu State Apex Co-op Bank	www.tnscbank.com
Thane Bharat Sahakari Bank	www.thanebharatbank.com
Thane District Central Co-op Bank	thanedistrictbank.com
Thane Janata Sahakari Bank (TJSB)	www.thanejanata.co.in
Tumkur Grain Merchants Co-op Bank	tgmcbank.com
UCO Bank	www.ucobank.com
Union Bank of India	www.unionbankofindia.co.in
United Bank of India	www.unitedbankofindia.com
United Overseas Bank	www.uobgroup.com/in
Varachha Co-op Bank	www.varachhabank.com
Vasai Vikas Sahakari Bank	vasaivikasbank.com
Vijaya Bank	www.vijayabank.com
Vishweshwar Sahakari Bank	vishweshwarbank.com
West Bengal State Co-op Bank	www.wbscb.com
Westpac Banking Corporation	http://www.westpac.com.au/about-westpac/global-locations/westpac-in-asia/india-website/
Woori Bank	in.wooribank.com
Yes Bank	www.yesbank.in
"""

# Parse bank names and URLs from the text
banks = []
for line in bank_list_text.split('\n'):
    if line.strip():  # Skip empty lines
        match = re.match(r"(.+?)\s+(www\..+)$", line)
        if match:
            name, url = match.groups()
            # Add "https://" before "www." in the URL
            url = f"https://{url}"
            banks.append({"name": name.strip(), "url": url.strip()})

# Creates a JSON file and mention path
json_file_path = "data/bank_data.json"

# Writes data to JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(banks, json_file, indent=4)

print(f"Bank data has been written to {json_file_path}")
