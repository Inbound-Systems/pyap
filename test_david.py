# -*- coding: utf-8 -*-

""" Test for USA address parser """

import re
import pytest
from pyap import utils, parse
from pyap.packages import six
import pyap.source_US.data as data_us
import pyap.parser
import pyap.api


input = """Find Cupbop

ORDER
ORDER

Cupbop store locations

Utah

AMERICAN FORK

598 W Main St

American Fork UT 84003

385-314-3887

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

BOUNTIFUL (COMING SOON)

325 S 500 W ste d

Bountiful UT 84010

385-399-9930

Mon - Sat  10 30 am - 9 pm

CEDAR CITY

1322 S Providence Center Dr c

Cedar City UT 84721

435-254-7072

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

CEDAR HILLS

9920 N 4800 W Ste B

Cedar Hills UT 84062

801-630-0070

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

DAYBREAK

11259 Kestrel Rise Rd Suite #100

South Jordan UT 84095

385-314-3888

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

DOWNTOWN - SALT LAKE

45 E Broadway

Salt Lake City UT 84111

385-314-3889

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

DRAPER

593 E 12300 S

Draper UT 84020

385-314-3890

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

FASHION PLACE

6191 State St Unit #1995

Murray UT 84107

801-383-0141

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

FOOTHILL

1400 Foothill Dr #156

Salt Lake City UT 84108

801-630-0052

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

FORT UNION

7178 Union Park Ave

Midvale UT 84047

801-618-1024

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

HERRIMAN

5136 13400 S #102

Herriman UT 84096

801-877-8423

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

HILL AFB

5845 E Ave Building 412

Hill AFB UT 84056

Mon - Sat  10 30 am - 9 pm

HUNTER

2662 S 5600 W Ste 102

West Valley City UT 84120

801-618-1025

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

LAYTON

743 King St

Layton UT 84041

385-314-3891

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

LEHI

2851 Club House Dr #150

Lehi UT 84043

801-877-8435

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

LOGAN

1309 N Main St Ste 90

Logan UT 84341

801-877-8415

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

MIDVALE

752 Blue Vista Ln #100

Midvale UT 84047

801-679-0362

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

MILLCREEK

2915 E 3300 S

Salt Lake City UT 84109

801-877-8424

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

OGDEN

141 12st

Ogden UT 84404

801-877-8416

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

OREM

719 E University Pkwy

Orem UT 84097

801-383-0143

Mon - Thu  10 30 am - 9 pm
Fri Sat  10 30 am - 10 pm

Pick upDelivery

PARK CITY

1612 W Ute Blvd Suite 106

Park City UT 84098

801-618-1015

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

PROVO

815 700 E

Provo UT 84606

801-383-0144

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

ROY

6050 S 3500 W

Roy UT 84067

801-630-0069

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

SARATOGA SPRINGS

1080 N Redwood Rd Bld 3 Suite A

Saratoga Springs UT 84045

801-877-8428

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

SLCC

4600 S Redwood Rd

Salt Lake City UT 84123

385-314-3884

Mon - Sat  10 30 am - 9 pm

SPANISH FORK

788 N 800 E

Spanish Fork UT 84660

801-396-7836

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

TOOELE

1024 N Main St Ste B

Tooele UT 84074

801-618-1016

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

UVU CAFETERIA

Student Center 800 W University Pkwy

Orem UT 84058

Mon - Sat  10 30 am - 9 pm

WASHINGTON

875 W Red Cliffs Dr Suite 6

Washington UT 84780

435-417-4385

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

WEST VALLEY

3619 2700 W

West Valley City UT 84119

801-383-0145

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

Idaho

BLUE LAKE BLVD

806 Blue Lakes Blvd N

Twin Falls ID 83301

801-916-8968

Mon - Sat  11 am - 9 pm

Pick upDelivery

DOWNTOWN - BOISE

298 North 8th Street

Boise ID 83702

208-370-8515

Mon - Sat  11 am - 9 pm

Pick upDelivery

EAGLE ISLAND MKTPL

1520 W Chinden Blvd #104

Meridian ID 83646

208-895-9737

Mon - Sat  11 am - 9 pm

Pick upDelivery

KARCHER MALL

1471 Caldwell Blvd

Nampa ID 83651

208-695-0698

Mon - Sat  11 am - 9 pm

Pick upDelivery

REXBURG - MAIN ST

163 W Main Street Ste 100

Rexburg ID 83440

208-760-2301

Mon - Sat  11 am - 9 pm

Pick upDelivery

SUNNYSIDE

3460 S 25th E

Idaho Falls ID 83404

801-916-8968

Mon - Sat  11 am - 9 pm

Pick upDelivery

VILLAGE AT MERIDIAN

3243 E Village Dr STE 110

Meridian ID 83646

208-948-2534

Mon - Sat  11 am - 9 pm

Pick upDelivery

Arizona

44TH & INDIAN SCHOOL

4325 E Indian School Ste 150

Phoenix AZ 85018

602-807-2575

Mon - Sat  11 am - 9 pm

Pick upDelivery

CRISMON & SOUTHERN

1222 S Crismon Rd Ste103

Mesa AZ 85209

602-807-2576

Mon - Sat  11 am - 9 pm

Pick upDelivery

CROSSROADS MALL

4811 E Grant Rd

Tucson AZ 85712

520-635-7218

Mon - Sat  11 am - 9 pm

Pick upDelivery

DESERT RIDGE MKTPL

21001 N Tatum Blvd Suite 34-1130

Phoenix AZ 85050

602-727-7403

Mon - Sat  11 am - 9 pm

Pick upDelivery

DOWNTOWN - BLOCK 23

101 E Washington St

Phoenix AZ 85004

480-875-8557

Mon - Sat  11 am - 9 pm

Pick upDelivery

GILBERT RD & WARNER RD

35 E Warner Rd #101

Gilbert AZ 85296

602-725-2735

Mon - Sat  11 am - 9 pm

Pick upDelivery

KINO PKWY - COMING SOON

3470 S Kino Pkwy

Tucson AZ 85713

Mon - Sat  11 am - 9 pm

TEMPE - MILL AVE

690 S Mill Ave

Tempe AZ 85281

480-875-8807

Mon - Sat  11 am - 9 pm

Pick upDelivery

THE LANDINGS

4764 S Landing Way

Tucson AZ 85714

520-971-1845

Mon - Sat  11 am - 9 pm

Pick upDelivery

WESTGATE

9410 W Hanna ln A101

Glendale AZ 85305

602-860-2713

Mon - Sat  11 am - 9 pm

Pick upDelivery

Colorado

ARVADA

7450 W 52nd Ave Unit C

Arvada CO 80002

720-741-2408

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

AURORA

13700 E Colfax Ave Suite I

Aurora CO 80011

720-741-2409

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

DENVER KIOSK #2

17th St and Wewatta

Denver CO 80202

720-741-2409

Mon - Fri  11 am - 5 pm

HIGHLANDS SQUARE

3453 W 32nd Ave

Denver CO 80211

720-741-2409

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

Nevada

CACTUS & ARVILLE - COMING SOON

4390 W Cactus Ave Ste 110

Las Vegas NV 89141

Mon - Sat  11 am - 9 pm

CHARLESTON

1100 Sourth Fort Apache Road #150

Las Vegas NV 89117

702-861-6023

Mon - Sat  11 am - 9 pm

Pick upDelivery

CRAIG RD & CLAYTON ST

1975 W Craig Rd #100

North Las Vegas NV 89032

702-348-0190

Mon - Sat  11 am - 9 pm

Pick upDelivery

LAS VEGAS - UNLV

4680 S Maryland Pkwy Suite 300

Las Vegas NV 89119

702-415-4578

Mon - Sat  11 am - 9 pm

Pick upDelivery

MONTECITO MKTPL

7150 North Durango Drive #120

Las Vegas NV 89149

702-573-0320

Mon - Sat  11 am - 9 pm

Pick upDelivery

Oklahoma

MOORE

660 SW 19th st Ste D

Moore OK 73160

405-676-7494

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

NORMAN

757 Asp Ave Norman OK 73069

Norman OK 73069

405-504-0670

Mon - Sat  10 30 am - 10 pm

Pick upDelivery

OKLAHOMA CITY

14220 N Pennsylvania Ave STE 1

Oklahoma City OK 73134

405-504-0638

Mon - Sat  10 30 am - 9 pm

Pick upDelivery

Texas

EL PASO - EASTLAKE BLVD

12261 Eastlake Blvd E501

El Paso TX 79928

915-861-2844

Mon - Sat  11 am - 9 pm

Pick upDelivery

EL PASO - ZARAGOSA RD

3565 Zaragoza Rd C-301

El Paso TX 79938

915-861-3643

Mon - Sat  11 am - 9 pm

Pick upDelivery
Our story
Nutrition
Allergen Info
Careers
Franchise
Contact us
FacebookInstagramTiktok
License

  COPYRIGHT 2024 CUPBOP Inc"""

# input = "237 N 2nd E, Rexburg, ID 83440"
# lines = input.split("\n")

# for line in lines:
#   pattern = data_us.full_address
#   match = utils.match(pattern, line, re.VERBOSE)
#   if match:
#     print(match)

response = parse(input, country='US')
for address in response:
  print(address.as_dict())
  print("\n\n")