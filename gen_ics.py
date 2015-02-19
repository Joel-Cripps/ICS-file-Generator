#!/usr/bin/env

#Creates an ics file named Test.ics with basic calendar events between 2010-2015 Dec 28/
#Inteded to test calendar Migration

#TODO: Ad in random Attachments, groups and other varibles

import os
import random

def main():
    event_count = float(raw_input("How many Events to create? " ))

    i = 0
    list_of_events = []
    while i < event_count:
        x = generate()
        list_of_events.append(x)
        i = i + 1

    writeFile(list_of_events)
    print "Done"
def randomAttendee():
    dictofAttendee = {"joel.cripps@gmail.com":"Joel Cripps", "jcripps@langara.ca":"Joel Cripps", "vsilvalima@langara.ca":"Vitor Silva Lima"}

    listofAttendee = ["joel.cripps@gmail.com","jcripps@langara.ca","gr-fscott2@langara.ca","vsilvalima@langara.ca",
                      """

                      """
                      ]

    randx = random.randint(1,len(dictofAttendee))
    for i,j in dictofAttendee.iteritems():
        print i,j
    #print randx
    #print dictofAttendee.fromkeys()
    #print dictofAttendee.keys()
    #return dictofAttendee.keys()

def randomGroup():
    pass




def randomDate():
    month = random.randint(1,12)
    day = random.randint(1,28)
    year = random.randint(2010,2015)
    #Add 0 to beginning of Number if less than 10
    if day < 10:
        day = str(0)+str(day)
    if month<10:
        month = str(0)+str(month)
    return (str(year)+str(month)+str(day))

def writeFile(data):
    try:
        fics =open('Test.ics', "wb")
    except:
        IOError, "IO ERROR"
    fics.write("""BEGIN:VCALENDAR
PRODID:-//Microsoft Corporation//Outlook 15.0 MIMEDIR//EN
VERSION:2.0
METHOD:PUBLISH
X-CALSTART:20140407T000000
X-CALEND:20150417T153000Z
X-WR-RELCALID:{0000002E-97B3-8E8D-6942-5BA629B5B946}
X-PRIMARY-CALENDAR:TRUE
X-OWNER;CN="Joel Cripps":mailto:jcripps@langara.ca
X-MS-OLK-WKHRSTART;TZID="Pacific Standard Time":080000
X-MS-OLK-WKHREND;TZID="Pacific Standard Time":170000
X-MS-OLK-WKHRDAYS:MO,TU,WE,TH,FR
BEGIN:VTIMEZONE
TZID:Pacific Standard Time
BEGIN:STANDARD
DTSTART:16011104T020000
RRULE:FREQ=YEARLY;BYDAY=1SU;BYMONTH=11
TZOFFSETFROM:-0700
TZOFFSETTO:-0800
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:16010311T020000
RRULE:FREQ=YEARLY;BYDAY=2SU;BYMONTH=3
TZOFFSETFROM:-0800
TZOFFSETTO:-0700
END:DAYLIGHT
END:VTIMEZONE
""")
    for i in data:
        for y in i:
            fics.write("%s\n" % y)

    fics.write("""END:VCALENDAR


    """)
    fics.close()
    
def randomBoolean():
    x = random.randint(1,2)
    return x

#"dtstart:20150121T220000Z",
def generate():
    DT_START = randomDate()
    #DT_END = DT_START
    random_attendee = randomAttendee()
    random_Date = "DTSTART:"+ randomDate() + "T220000Z"
    listA = ["BEGIN:VEVENT",
             """ATTENDEE;CN="Joel Cripps";RSVP=FALSE:mailto:jcripps@langara.bc.ca""",
             "CLASS:PUBLIC",
             "CREATED:"+DT_START+"T213406Z",
             "DESCRIPTION:THIS IS A TEST OF THE AUTOMATICALLY GENERATED ICS FILE",
             """DTEND;DTEND;TZID="Pacific Standard Time":""" + DT_START,
             "DTSTAMP:20150206T192728Z",
             """DTSTART;TZID="Pacific Standard Time":"""+DT_START,
             "LAST-MODIFIED:",
             "ORGANIZER;CN=jcripps@langara.ca:mailto:jcripps@langara.ca",
             "SEQUENCE:0",
             "SUMMARY:TEST OF THE AUTOMATICALLY GENERATED ICS FILE",
             "TRANSP:OPAQUE",
             "X-MICROSOFT-CDO-BUSYSTATUS:BUSY",
             "X-MS-OLK-SENDER;CN=jcripps@langara.ca:mailto:jcripps@langara.ca",
             "END:VEVENT"
            ]
    return listA
    
def list_of():
    pass

main()


