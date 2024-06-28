# -*- coding: utf-8 -*-

""" Test for USA address parser """

import re
import pytest
from pyap import utils, parse
from pyap.packages import six
import pyap.source_US.data as data_us
import pyap.parser
import pyap.api


input = """http://lotusskininstitute.com
Skip to content
Home
Programs
Services
Shop
Go To Class
Continuing Education
About
Blog
Menu
Home
Programs
Services
Shop
Go To Class
Continuing Education
About
Blog
Welcome to
Lotus Skin Institute

Esthetics Hands-on Skills Training

Apply Now
About Us
Growing Skin Professionals

The Lotus Skin Institute was created to provide
hands-on skilled training that leads to direct employment in the vast industry of Esthetics

Read More
Our
Programs
Esthetician
Our Esthetician program offers a comprehensive in depth training on the rejuvenation and care of the skin
learn more
Instructor

With Lotus Skin Institute Esthetics Instructor program you become an instructor in the field of esthetics with focusing on advanced and medical esthetic treatments

learn more
Apply Now
Facilities
Lorem ipsum dolor sit amet cons ectetur adip aring elit selld dllao the or eiusmod tempo incint the off ullamco
All Facilities
Gain Access to premier products
Shop

Visit our shop to purchase the latest gear products & more 

Shop
We walk you through the process
Hands on Classes

Quality education resources and support throughout your educational journey

Go to class
Announcements
 Lorem Ipsum is simply dummy text of the printing and typesetting industry 
Client NameCity State
 Lorem Ipsum is simply dummy text of the printing and typesetting industry 
Client NameCity State
 Lorem Ipsum is simply dummy text of the printing and typesetting industry 
Client NameCity State
 Lorem Ipsum is simply dummy text of the printing and typesetting industry 
Client NameCity State
 Lorem Ipsum is simply dummy text of the printing and typesetting industry 
Client NameCity State
sign up for the latest on events & specials
Name
Email
phone
Submit
hands-on skills training that leads to direct employment in the vast industry of Esthetics
Lotus Skin Institute

Growing Skin Professionals

Address

1800 Water Place SE
Ste 100
Atlanta Ga 30339

Opening Hours

Monday   Friday
8 00 AM   9 00 PM

Saturday & Sunday
10 00 AM   6 00 PM

Contact Us
info@thelotuscorporationcom
Local (770) 299-3904
Toll Free (844) 368-9007
Fax (770) 450-8565
  2024 Lotus Skin Institute - All Rights Reserved
Facebook-f Instagram Twitter

https://lotusskininstitute.com/aboutus/
Skip to content
Home
Programs
Services
Shop
Go To Class
Continuing Education
About
Blog
Menu
Home
Programs
Services
Shop
Go To Class
Continuing Education
About
Blog
Home
Programs
Services
Shop
Go To Class
Continuing Education
About
Blog
About us
Lotus Skin Institute

The Lotus Skin Institute was created to provide hands-on skills training that can lead to direct employment in the vast industry of Esthetics Our highly innovative and revolving curriculum allows students to enroll all year-round never missing an opportunity to follow your career dreams

Our Mission

Our mission is to be the best in our field by providing quality education resources and support throughout your educational journey 

We are invested in developing a personal connection with each one of our students In addition to the standardized curriculum we provide courses in CPR medical terminology accounting business marketing advanced esthetics and continuing education courses for licensed nurses 

With our advanced courses our students will have the ability to bridge their education directly into the medical field We strive to produce the highest qualifying newly licensed professionals in the industry

Our Goal

Our goal is to help eliminate hurdles that some students may face while in school and upon completion by offering ongoing mentorships for students to help keep up their enthusiasm and morale 

Our students transition from our program with the skills they need to pass their state board exam and excel in the world of business whether they choose to start their own business work in a medical spa or in a physician s office

Virtual Tour

View Our Virtual Tour

sign up for the latest on events & specials
Name
Email
phone
Submit
hands-on skills training that leads to direct employment in the vast industry of Esthetics
Lotus Skin Institute

Growing Skin Professionals

Address

1800 Water Place SE
Ste 100
Atlanta Ga 30339

Opening Hours

Monday   Friday
8 00 AM   9 00 PM

Saturday & Sunday
10 00 AM   6 00 PM

Contact Us
info@thelotuscorporationcom
Local (770) 299-3904
Toll Free (844) 368-9007
Fax (770) 450-8565
  2024 Lotus Skin Institute - All Rights Reserved
Facebook-f Instagram Twitter

https://lotusskininstitute.com/aboutus/#content
Skip to content
Home
Programs
Services
Shop
Go To Class
Continuing Education
About
Blog
Menu
Home
Programs
Services
Shop
Go To Class
Continuing Education
About
Blog
Home
Programs
Services
Shop
Go To Class
Continuing Education
About
Blog
About us
Lotus Skin Institute

The Lotus Skin Institute was created to provide hands-on skills training that can lead to direct employment in the vast industry of Esthetics Our highly innovative and revolving curriculum allows students to enroll all year-round never missing an opportunity to follow your career dreams

Our Mission

Our mission is to be the best in our field by providing quality education resources and support throughout your educational journey 

We are invested in developing a personal connection with each one of our students In addition to the standardized curriculum we provide courses in CPR medical terminology accounting business marketing advanced esthetics and continuing education courses for licensed nurses 

With our advanced courses our students will have the ability to bridge their education directly into the medical field We strive to produce the highest qualifying newly licensed professionals in the industry

Our Goal

Our goal is to help eliminate hurdles that some students may face while in school and upon completion by offering ongoing mentorships for students to help keep up their enthusiasm and morale 

Our students transition from our program with the skills they need to pass their state board exam and excel in the world of business whether they choose to start their own business work in a medical spa or in a physician s office

Virtual Tour

View Our Virtual Tour

sign up for the latest on events & specials
Name
Email
phone
Submit
hands-on skills training that leads to direct employment in the vast industry of Esthetics
Lotus Skin Institute

Growing Skin Professionals

Address

1800 Water Place SE
Ste 100
Atlanta Ga 30339

Opening Hours

Monday   Friday
8 00 AM   9 00 PM

Saturday & Sunday
10 00 AM   6 00 PM

Contact Us
info@thelotuscorporationcom
Local (770) 299-3904
Toll Free (844) 368-9007
Fax (770) 450-8565
  2024 Lotus Skin Institute - All Rights Reserved
Facebook-f Instagram Twitter

https://lotusskininstitute.com/aboutus
Skip to content
Home
Programs
Services
Shop
Go To Class
Continuing Education
About
Blog
Menu
Home
Programs
Services
Shop
Go To Class
Continuing Education
About
Blog
Home
Programs
Services
Shop
Go To Class
Continuing Education
About
Blog
About us
Lotus Skin Institute

The Lotus Skin Institute was created to provide hands-on skills training that can lead to direct employment in the vast industry of Esthetics Our highly innovative and revolving curriculum allows students to enroll all year-round never missing an opportunity to follow your career dreams

Our Mission

Our mission is to be the best in our field by providing quality education resources and support throughout your educational journey 

We are invested in developing a personal connection with each one of our students In addition to the standardized curriculum we provide courses in CPR medical terminology accounting business marketing advanced esthetics and continuing education courses for licensed nurses 

With our advanced courses our students will have the ability to bridge their education directly into the medical field We strive to produce the highest qualifying newly licensed professionals in the industry

Our Goal

Our goal is to help eliminate hurdles that some students may face while in school and upon completion by offering ongoing mentorships for students to help keep up their enthusiasm and morale 

Our students transition from our program with the skills they need to pass their state board exam and excel in the world of business whether they choose to start their own business work in a medical spa or in a physician s office

Virtual Tour

View Our Virtual Tour

sign up for the latest on events & specials
Name
Email
phone
Submit
hands-on skills training that leads to direct employment in the vast industry of Esthetics
Lotus Skin Institute

Growing Skin Professionals

Address

1800 Water Place SE
Ste 100
Atlanta Ga 30339

Opening Hours

Monday   Friday
8 00 AM   9 00 PM

Saturday & Sunday
10 00 AM   6 00 PM

Contact Us
info@thelotuscorporationcom
Local (770) 299-3904
Toll Free (844) 368-9007
Fax (770) 450-8565
  2024 Lotus Skin Institute - All Rights Reserved
Facebook-f Instagram Twitter

https://www.facebook.com/lotusskininstitute
Log In
Log In
Forgot Account 
Lotus Skin Institute 
173 likes   201 followers
Posts
About
Reels
Photos
Videos
More
Posts
About
Reels
Photos
Videos
Lotus Skin Institute
Intro
 
Lotus Skin Institute Atlanta s #1 institution for advanced and medical esthetics education
Page   Day Spa
1800 Water Pl SE Unit 100 Marietta GA 30339 Atlanta GA United States Georgia
(770) 299-3904
contact@thelotuscorporationcom
lotusskini
lotusskininstitutecom
Price Range   $
Not yet rated (4 Reviews) 
Photos
 
See all photos
Privacy   
Consumer Health Privacy   
Terms   
Advertising   
Ad Choices    
Cookies   
More
   
Meta   2024
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Lotus Skin Institute
    dSeoontsrp0tm0ufA1 M9 0242t1c2ue3hgia3h4a650 48m 651i 30Jin9   
Congrats Class of 2024 graduation
Sorry we re having trouble playing this video
Learn more
1YcQ7com
Aw0xHkBgT2EYMlAUpstZz3AXoF30kmYZRcsn
25ez9vEavSIYa73AZfrZbAeHcHUMlpzCTIIIDA4mNdvOEv1QKaa6QJEOSfdASL91hv
dSeoontsrp0tmaufrofe9r0242 9c2ef3hgin3h4ai50848mi651iM00Lii9
Like
Comment
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
Facebook
See more on Facebook
See more on Facebook
Email or phone number
Password
Log In
Forgot password 
or
Create new account
"""

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