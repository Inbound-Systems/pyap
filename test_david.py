# -*- coding: utf-8 -*-

""" Test for USA address parser """

import re
import pytest
from pyap import utils
from pyap.packages import six
import pyap.source_US.data as data_us
import pyap.parser
import pyap.api

input = """4329
Skip to content
IDAHO FALLS - (208) 881-9066
REXBURG - (208) 881-5525
Request Appointment
facebook social buttoninstagram social button
(208) 881-5525
Summit Spine and Sport Chiropractic
Rexburg Location
237 N 2nd E Suite 106
Rexburg ID 83440
Phone  (208) 881-5525
Idaho Falls Location
1515 Ashment Ave Suite 2
Idaho Falls ID 83404
Phone  (208) 881-9066
Menu
Home
Idaho Falls
Dr Kimball S Arritt
Erin Balderson
Rachel Adams
Contact Idaho Falls
Rexburg
Dr Travis C Thompson
Dr Kimball S Arritt
Contact Rexburg
Meet the Team
Our Services
Chiropractic Care
Pregnancy Chiropractic
Pediatric Chiropractic
Sports Chiropractic
Class IV Laser Therapy
Vertical Traction Therapy
Auto Accident & Personal Injury
New Patients
Contact Us
Blog
Award-Winning Chiropractor in Idaho Falls and Rexburg

Live the vibrant life you deserve We look forward to helping you achieve your health goals!

Meet Our Team
Our Services
New Patients
Contact Us

Reach  Destination Wellness 
at Summit Spine and Sport Chiropractic

At Summit Spine and Sport Chiropractic  our priority is to get you out of pain get you well and get you back to living life the way you want to Although pain may be what brings you to our practice alleviating that discomfort is only the first step in your overall care We aim to help all of our patients achieve real wellness and get them to our Destination Wellness Wall of Champions

Idaho Falls and Rexburg Chiropractors Dr Kimball Arritt and Dr Travis Thompson strive to help you change how you function so you re in less pain and in pain less often

We treat every member of the family from newborns through great-great-grandparents and everyone in between We also care for athletes including Pee Wee players pros and weekend warriors in virtually every sport

Meet Our Caring Chiropractors

Dr Arritt and Dr Thompson both have extensive advanced education to provide the best care possible for our patients Dr Arritt has a master s degree in sports science and rehabilitation a doctorate in chiropractic and is an International Certificate in Sports Chiropractic Physician Dr Thompson has two master s degrees one in sports science and rehabilitation and one in nutrition and human performance as well as a doctorate in chiropractic and certification as an International Certificate in Sports Chiropractic Physician

Because of their training and experience they offer a more functional approach to movement and rehabilitation to all of our patients whether they re athletes or not

Meet the Doctors
We re in Your Corner

We listen attentively to your concerns take notes and then do an exam tailored to what you ve told us We are in your corner and will do whatever we can to help get you where you want to go with your overall health Our patients are generally looking for a change to help improve their lives rather than taking a pill to mask symptoms

Get Started Today

We offer on-site X-rays at both our Idaho Falls and Rexburg chiropractic clinics and we accept most insurance plans Contact us today to book an appointment

Chiropractic Care
Sports Chiropractic
Classic IV Laser Therapy
Pregnancy Chiropractic
Pediatric Chiropractic
Vertical Traction Therapy
Auto Accident & Personal Injury
Testimonials
I have really appreciated the care I have gotten from Doctor Thompson and Doctor Arritt They know how to treat and explain things so that I can continue to work at home and improve my back for long term benefits My back pain has greatly improved The staff is very kind and helpful and they have been willing to work around my schedule I would recommend Summit Spine and Sport to anyone
- Kare D
So knowledgeable and sensitive to my daughters medical history and issues! Amazing Doctor I highly recommend!!!!
- Bridget S
Great people! Many thanks for helping me!
- Dennis S
Super awesome experience Front desk was very friendly and informative and I was impressed with the professionalism and charisma of the whole staff After one visit my neck already feels so much better Definitely will be going back! 
- Sarah L
I m a new patient of Dr Thompson and I highly recommend him and this facility! After getting in an auto accident and having pretty bad neck and shoulder pain within one adjustment I felt 10x better! The environment is professional and welcoming His assistant and the other girls that work there are also super great!
- Haley V
Dr Arritt was amiable and knowledgeable and was able to provide results with the first appointment I look forward to work with him on improving my posture and future daily comfort!
- Boston S
This office is the best!! Both doctors are fantastic and the staff is so nice to me every time I come in! I can tell they genuinely care about me and how I m doing! If you re thinking of going to a chiropractor I would definitely recommend this office!
- Makayla A
Dr Thompson is amazing! He explained everything very well is very personable and my first adjustment here was amazing! I feel very taken care of and trust him!
- Brynlee O
Walked in with a headache I have had for about two weeks and walked out without it!
- Jayson G
Very good experience after having a bad experience with a different chiropractic office I will definitely be back and have referred family there as well!
- Tyrel W
You guys were amazing! I have had work done before where I have left wondering why even go to a chiropractor But you made me feel at home and what a relief! I look forward to coming back!
- Paul B
Very friendly professional and effective treatment I will definitely be back Next Tuesday in fact!
- Shari B
Dr Thompson and his staff are so great!! So thankful we found them!!
- Emily D
For a first timer I was nervous but the staff and Dr Arritt we re very kind and attentive
- Alyssa M
Great people and great experience!
- Braxton
On my first day as a new patient at Summit Spine and Sport Chiropractic I was impressed with their amazing service Dr Arritt had done a phenomenal job adjusting my spine especially my sacrum and coccyx where I had pain a lot of I went home with a happy feeling and a huge change in my whole body I definitely recommended them to anybody who needs a professional chiropractor
- Mavae J
After the first visit and adjustment I feel better already!
- Jarod W
My chiropractor is amazing ! I am glad I chose him! He was very detail on what was going on and how we can fix the issues going on! Very friendly!
- Nicki P
Everyone was very kind and helpful with getting me back on my feet!
- Linda R
Dr Thompson was amazing! No that is selling it short Both Dr Thompson and the fabulous wonderful beautiful woman at the desk was amazing! They were both extremely comfortable to talk with I am a very anxious person and even I felt immediately comfortable I will gladly continue treatment at the Rexburg office I am even looking forward to it 
- Miranda C
Great Dr! In no time at all he determined what needed adjusting and relieved my pain and greatly improved my flexibility I m very pleased to have found this practice
- Gary D
I didn t have real high expectations when I came in because I have dealt with the same pain for a long time and I m used to it I feel so much better already and Dr Aritt was able to tell me exactly what is going on with my hip and back Thank you!
- Kayla E
Extremely impressed by this facility and also your staff
- Gina S
I always seem to have a tough case to handle Dr Arritt and his team throughly listened to all of my complaints and took the time to know my case personally I feel treatment was personal to me and the office had a great atmosphere All of the staff really made me feel comfortable and I felt like I was in a safe place
- Shannon H
The atmosphere is very inviting and comforting I felt as though I was cared for and not just for my money but for my health and wellbeing It s a great family environment and I felt like I was apart of their family even with only one visit
- Porter K
Lexie was fantastic! She listened to my concerns and was very knowledgeable Down to earth and very friendly
- Erin S
I love going to Summit Spine and Sport The staff members are friendly inviting and very considerate! Travis is very professional and does a great job at his job!
- Jenny R
Dr Ariett is a very strong man! But he has such a gentle touch
- Dakota E
Professional reasonable priced and so far I feel better after my visit I plan on going back!
- Lisa W
I enjoyed being analyzed for posture correctness The feedback and direction given confirmed my current goals and course of action It also pointed me in a new direction Marissa was a good listener and source of information Thank you for your service
- Ron S
I have really appreciated the care I have gotten from Doctor Thompson and Doctor Arritt They know how to treat and explain things so that I can continue to work at home and improve my back for long term benefits My back pain has greatly improved The staff is very kind and helpful and they have been willing to work around my schedule I would recommend Summit Spine and Sport to anyone
- Kare D
So knowledgeable and sensitive to my daughters medical history and issues! Amazing Doctor I highly recommend!!!!
- Bridget S
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
Chiropractor Idaho Falls Rexburg ID   Summit Spine and Sport Chiropractic

Rexburg Location


237 N 2nd E Suite 106
Rexburg ID 83440
Phone  (208) 881-5525

Contact Us

Idaho Falls Location


1515 Ashment Ave Suite 2
Idaho Falls ID 83404
Phone  (208) 881-9066

Contact Us

facebook icon link instagram icon link

Email Summit Spine and Sport Chiropractic
Comments Requests Questions or Suggestions

First Name
Last Name
Respond to me via 
Email
Phone
No Response
Email Address
Phone Number
I agree to refrain from including any personally identifiable information or protected health information in the comment field For more info read disclaimer
Please keep in mind that communications via email over the internet are not secure Although it is unlikely there is a possibility that information you include in an email can be intercepted and read by other parties or unauthorized individuals Please do not include personal identifying information such as your birth date or personal medical information in any emails you send to us Communication via our website cannot replace the relationship you have with a physician or another healthcare practitioner
I consent to having this website store my submitted information so they can respond to my inquiry For more info read our privacy policy
Leave this empty 
Send Message

Request Appointment (pending confirmation)
Patient Type
New Patient
Current Patient
Returning Patient
First Name
Last Name
Email Address
Phone Number
Respond to me via 
Email
Phone
Preferred Day Time 
Date
Appointment Hour 
H
1
2
3
4
5
6
7
8
9
10
11
12
Appointment Minute 
M
00
15
30
45
AM or PM
AM
PM
Comments or Questions
I agree to refrain from including any personally identifiable information or protected health information in the comment field For more info read disclaimer
Please keep in mind that communications via email over the internet are not secure Although it is unlikely there is a possibility that information you include in an email can be intercepted and read by other parties or unauthorized individuals Please do not include personal identifying information such as your birth date or personal medical information in any emails you send to us Communication via our website cannot replace the relationship you have with a physician or another healthcare practitioner
I consent to having this website store my submitted information so they can respond to my inquiry For more info read our privacy policy
Leave this empty 
Send Message

Share on TwitterShare on FacebookShare via Email
Summit Spine and Sport Chiropractic
237 N 2nd E Suite 106
Rexburg ID 83440
Phone  (208) 881-5525
Copyright
Legal
Privacy
Accessibility
Sitemap
Chiropractic Websites by Perfect Patients
PrevNextSlideshow
CloseLog In
Log In
Forgot Account 
Summit Spine and Sport Chiropractic 
759 likes   807 followers
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
Summit Spine and Sport Chiropractic
Intro
 
Voted Readers Choice  Best Chiropractor  in Rexburg Idaho
Page   Chiropractor
237 N 2 E Rexburg ID United States Idaho
(208) 881-5525
frontdeskrex@summitchiropractichealthcom
summitchiropractichealthcom
Opening Soon
Rating   48 (70 Reviews) 
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
Summit Spine and Sport Chiropractic
    rnodSpesto36 949i f2m 6t4t08aA 3226fa73ftyt7091l1a 9gM0fM0i2   
In observance of Memorial Day we will be closed on Monday May 27th We will resume our regular hours on Tuesday May 28th
As we honor and remember those who have served and are currently serving our country we hope you have a safe and reflective holiday
#MemorialDay2024 #HonorAndRemember #ChiropracticCare #SpineHealth #Wellness
mk1vbwPacom
IEWm0EVBCCLBdd51f8ffM
In observance of Memorial Day we will be closed on Monday May 27th We will resume our regular hours on Tuesday May 28th As we honor and remember those who have served and are currently serving our country we hope you have a safe and reflective holiday #MemorialDay2024 #HonorAndRemember #ChiropracticCare #SpineHealth #Wellness
rnodSpesto3 i949iMf2mm6t4108Lut3226fnroftet7091l1al9gerfa0ia
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
Create new accountSomething went wrong
There s an issue and the page could not be loaded
Reload pageFacebook
Log in to use your Facebook account with Vortala
Email or phone 
Password 

Forgot account 

Create new account"""



# input = "237 N 2nd E, Rexburg, ID 83440"
# lines = input.split("\n")

# for line in lines:
#   pattern = data_us.full_address
#   match = utils.match(pattern, line, re.VERBOSE)
#   if match:
#     print(match)

response = pyap.api.parse(input, country='US')
for address in response:
  print(address.as_dict())
  print("\n\n")