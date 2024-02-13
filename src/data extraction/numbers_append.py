import re
import json

# Provided list of customer care services and their toll free numbers
customer_care_list_text = """
Airtel – 18001030405

Air India – 1800 22 7722
Go Air – 1800 223 001
Indian Airlines – 1800 180 1407
Indigo Airlines – 1800 180 3838
Jet Airways – 1800 22 5522
KingFisher – 1800 180 0101
SpiceJet – 1800 180 3333

Audi – 1800 103 6800
Bentley – 18001006243
Ford – 1800 209 5556
Honda – 1800 103 3121
Hyundai – 1800 11 4645
Mercedez Benz – 1800 102 9222
Mahindra Scorpio – 1800 22 6006
Maruti Suzuki – 1800 111 515
Mitsubishi – 1800-102 2955
Nissan – 1800-209-4080
Porsche – 1800 1020 911
Tata Motors – 1800 22 5552
Toyota – 1800 425 0001
Windshield Experts – 1800 11 3636

ABN AMRO – 1800 11 2224
Axis Bank Ltd. – 1860 425 8888
Bank of Baroda – 1800 22 4447
Bank of India – 1800 22 00 88
Canara Bank – 1800 44 6000
Citibank – 1800 44 2265
Corporation Bank – 1800 443 555
Development Credit Bank – 1800 22 5769
HDFC Bank – 1800 227 227
ICICI Bank – 1800 333 499
ICICI Bank NRI – 1800 22 4848
IDBI Bank – 1800 11 6999
Indian Bank – 1800 425 1400
Indian Overseas Bank – 1800 4251 230
ING Vysya – 1800 44 9900
Kotak Mahindra Bank – 1800 22 6022
Lord Krishna Bank – 1800 11 2300
Oriental Bank of Commerce – 1800 180 1235
Punjab National Bank – 1800 122 222
State Bank of India 1800 44 1955
State Bank of Patiala – 1800 112 211
Syndicate Bank 1800 44 6655
Union Bank of India – 1800 22 22 44

Apple – 1800 4250 744
BenQ – 1800 22 08 08
Bird CellPhones – 1800 11 7700
Blackberry – 1800 419 0121
HTC – 1800 113 377
LG – 1860 180 9999
Maxx – 1800 22 6299
Micromax – 1860 500 8286
Motorola MotoAssist – 1800 11 1211
Nokia – 3030 3838
Sony Ericsson – 3901 1111
Samsung – 1800 110 011
Tata Indicom – 1800 209 7070
Virgin – 1800 209 4444

Acer – 1800 3000 2237
Adrenalin – 1800 444 445
AMD – 1800 425 6664
Apple Computers – 1800 444 683
Canon – 1800 333 366
Cisco Systems – 1800 221 777
Compaq HP – 1800 444 999
Data One Broadband – 1800 424 1800
Dell – 1800 444 026
Epson – 1800 44 0011
eSys – 3970 0011
Genesis Tally Academy – 1800 444 888
HCL – 1800 180 8080
HP – 1800 425 4999
IBM – 1800 443 333
Infosys – 1800 930 4048
L&T – 1800 419 6666
Lexmark – 1800 22 4477
Marshals Point – 1800 33 4488
Microsoft – 1800 111 100
Microsoft Virus Update – 1901 333 334
Seagate – 1800 180 1104
Symantec – 1800 44 5533
TCS – 1800 200 1221
TVS Electronics – 1800 444 566
WeP Peripherals – 1800 44 6446
Wipro – 1800 333 312
xerox – 1800 180 1225
Zenith – 1800 222 004

ABT Courier – 1800 44 8585
AFL Wizz – 1800 22 9696
Agarwal Packers & Movers – 1800 11 4321
Associated Packers P Ltd – 1800 21 4560
DHL – 1800 111 345
DTDC – 1866 383 6606
First Flight – 1800 225 5345
FedEx – 1800 22 6161
Gati – 1800 180 4284
Goel Packers & Movers – 1800 11 3456
Om deo packers & Movers – 1800 2660 299
Royal Packers & Movers – 1800 11 4321
UPS – 1800 22 7171

Airtel Digital TV – 1800 102 8080
Tata Sky – 1800 180 6633
Sun Direct – 1800 200 7575
Reliance Big TV – 1800 200 9001
D2H – 1800 102 3111
Dish TV – 1800-180-3474

Barclaycard – 1800-233-7878
Bobcards – 1800-22-5110
HDFC Bank Credit Cards – 1800-345-4332
ICICI Credit Cards – 1800-11-2222
SBI Cards – 1800-180-1290
Tata Card – 1800-180-8282
VISA Credit and Debit Gold Cards – 1800-425-4446

Edu Plus – 1800 444 000
Hindustan College – 1800 33 4438
NCERT – 1800 11 1265
Vellore Institute of Technology – 1800 441 555
Amity University NCR Delhi – 1800 110 000

Best on Health – 1800 11 8899
Dr Batras – 1800 11 6767
GlaxoSmithKline – 1800 22 8797
Johnson & Johnson – 1800 22 8111
Kaya Skin Clinic – 1800 22 5292
LifeCell – 1800 44 5323
Manmar Technologies – 1800 33 4420
Pfizer – 1800 442 442
Roche Accu-Chek – 1800 11 45 46
Rudraksha – 1800 21 4708
Varilux Lenses – 1800 44 8383
VLCC – 1800 33 1262

Aiwa/Sony – 1800 11 1188
Anchor Switches – 1800 22 7979
Blue Star – 1800 22 2200
Bose Audio – 1800 11 2673
Bru Coffee Vending Machines – 1800 44 7171
Daikin Air Conditioners – 1800 444 222
DishTV – 1800 12 3474
Faber Chimneys – 1800 21 4595
Godrej – 1800 22 5511
Grundfos Pumps – 1800 33 4555
LG – 1901 180 9999
Philips – 1800 22 4422
Samsung – 1800 113 444
Sanyo – 1800 11 0101
Voltas – 1800 33 4546

Four Seasons – 000 800 650 1418
GRT Grand – 1800 44 5500
InterContinental Hotels Group – 1800 111 000
Le Meridien – 000 800 650 1458
Marriott – 1800 22 0044
Sarovar Park Plaza – 1800 111 222
Taj Holidays – 1800 111 825
The Leela Palace – 1800 222 444
Trident – 1800 11 2122

AMP Sanmar – 1800 44 2200
Aviva – 1800 33 2244
Bajaj Allianz – 1800 22 5858
Chola MS General Insurance – 1800 44 5544
HDFC Standard Life – 1800 227 227
LIC – 1800 33 4433
Max New York Life – 1800 33 5577
Royal Sundaram – 1800 33 8899
SBI Life Insurance – 1800 22 9090

Kurl-on – 1800 44 0404
Sleepwell – 1800 11 2266

CAMS – 1800 44 2267
Chola Mutual Fund – 1800 22 2300
Easy IPOs – 3030 5757
Fidelity Investments – 1800 180 8000
Franklin Templeton Fund – 1800 425 4255
J M Morgan Stanley – 1800 22 0004
Kotak Mutual Fund – 1800 222 626
LIC Housing Finance – 1800 44 0005
SBI Mutual Fund – 1800 22 3040
Sharekhan – 1800 22 7500
Tata Mutual Fund – 1800 22 0101

Asian Paints Home Solutions – 1800 22 5678
Berger Paints Home Decor – 1800 33 8800

Asian Sky Shop – 1800 22 1800
Home shop 18 – 1860 1800 918
Jaipan Teleshoppe – 1800 11 5225
Tele Brands – 1800 11 8000
VMI Teleshopping – 1800 447 777
WWS Teleshopping – 1800 220 777

Club Mahindra Holidays – 1800 33 4539
Cosmos – 1800 11 3211
Cox & Kings – 1800 22 1235
Emirates – 1800 11 5757
God TV Tours – 1800 442 777
Himalaya – 1800 694 6342
Kerala Tourism – 1800 444 747
Kumarakom Lake Resort – 1800 44 5030
Raj Travels & Tours – 1800 22 9900
Sita Tours – 1800 111 911
SOTC Tours – 1800 22 3344

APC – 1800 44 4272
Luminous – 1800 11 3535
Numeric – 1800 44 3266
Sukam – 1800 102 4423

Indian Railway General Enquiry – 131
Indian Railway Railway Reservation Enquiry – 1345
Indian Railway Centralised Railway Enquiry – 1330

Eureka Forbes – 1800 180 1407
Kenstar – 1800 419 4040
Kent RO Water Purifiers – 1800 100 1000
Pureit – 1800 22 8080
TATA Swach Water Purifiers – 1800 258 5858

Aavin – 1800 44 3300
Dominos Pizza – 1800 111 123
Google Local – 1800 419 4444
Consumer Helpline – 1800 11 4000
Loreal garnier – 1800 223 000
Kodak India – 1800 22 8877
KONE Elevator – 1800 444 666
Indane – 1800 44 51 15
Pedigree – 1800 11 2121
Pizza Hut – 3988 3988
Telecom Monitoring Cell – 1800 110 420
World Vision India – 1800 444 550

Police Helpline – 100
Ambulance – 102
Fire & Rescue Service – 101
Cyber Crime Helpline – 1930
"""

# Parse names and numbers from the text
contacts = []
for line in customer_care_list_text.split('\n'):
    if line.strip():  # Skip empty lines
        match = re.match(r"(.+?)\s*–\s*([\d\s]+)$", line)
        if match:
            ContactName, PhoneNumber = match.groups()
            # Remove whitespaces from the phone number
            PhoneNumber = ''.join(PhoneNumber.split())
            contacts.append({"ContactName": ContactName.strip(),
                            "PhoneNumber": PhoneNumber.strip()})

json_file_path = "data/phonebook_data.json"

with open(json_file_path, 'w') as json_file:
    json.dump(contacts, json_file, indent=4)

print(f"The data has been written to {json_file_path}")
