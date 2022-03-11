from flask import Flask, url_for, render_template, request, redirect
import math
from math import e

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

colleges = {
"Stanford" : 95,
"Yale": 93,
"UCLA": 93,
"MIT" : 91,
"Princeton": 97,
"Harvard": 95,
"Emory": 89,
"Berkely": 89,
"UCSD": 84,
"University of Virginia": 83,
"Georgia Tech": 80,
"UC Davis": 77,
"Tulane": 82,
"Gonzaga": 75,
"TCU": 70,
"Temple": 69,
"RIT": 70,
"Seton Hall": 67,
"George Mason": 64,
"University of Idaho": 61,
"University of New Mexico": 58,
"Pace": 54,
"Gannon": 51,
"Harding": 50,
"Montana State": 48,
"Florida Atlantic": 46,
"South Dakota State University": 42,
"Husson": 40,
"Kieser": 40,
"Oakland University": 37,
"Tennessee State": 36,
"University of Alaska": 35,
"University of Toledo": 34,
"Wingate University": 31,
"Brandman University": 30,
"Valdosta": 28,
"Western Kentucky University": 26,
"William Woods": 25,
"University of the Cumberlands": 23,
"Wichita State": 21,
"William Carey": 20,
"University of Southern Mississippi": 18,
"Jackson State": 16,
"Grand Canyon University": 15,
"Ferris State": 13,
"Lindenwood": 11,
"Missouri State": 10,
"Morgan State": 7,
"SBCC": 0
}

collegeLinks = {
"Stanford" : "https://www.usnews.com/best-colleges/stanford-university-1305",
"Yale": "https://www.usnews.com/best-colleges/yale-university-1426",
"UCLA": "https://www.usnews.com/best-colleges/university-of-california-los-angeles-1315",
"MIT" : "https://www.usnews.com/best-colleges/massachusetts-institute-of-technology-2178",
"Princeton": "https://www.usnews.com/best-colleges/princeton-university-2627",
"Harvard": "https://www.usnews.com/best-colleges/harvard-university-2155",
"Emory": "https://www.usnews.com/best-colleges/emory-university-1564",
"Berkely": "https://www.usnews.com/best-colleges/university-of-california-berkeley-1312",
"UCSD": "https://www.usnews.com/best-colleges/university-of-california-san-diego-1317",
"University of Virginia": "https://www.usnews.com/best-colleges/uva-6968",
"Georgia Tech": "https://www.usnews.com/best-colleges/georgia-institute-of-technology-1569",
"UC Davis": "https://www.usnews.com/best-colleges/university-of-california-davis-1313",
"Tulane": "https://www.usnews.com/best-colleges/tulane-university-2029",
"Gonzaga": "https://www.usnews.com/best-colleges/gonzaga-university-3778",
"TCU": "https://www.usnews.com/best-colleges/tcu-3636",
"Temple": "https://www.usnews.com/education/online-education/temple-university-216339",
"RIT": "https://www.usnews.com/best-colleges/rit-2806",
"Seton Hall": "https://www.usnews.com/best-colleges/seton-hall-university-new-jersey-2632",
"George Mason": "https://www.usnews.com/best-colleges/gmu-3749",
"University of Idaho": "https://www.usnews.com/best-colleges/university-of-idaho-1626",
"University of New Mexico": "https://www.usnews.com/best-colleges/university-of-new-mexico-10313",
"Pace": "https://www.usnews.com/best-colleges/pace-university-2791",
"Gannon": "https://www.usnews.com/best-colleges/gannon-university-3266",
"Harding": "https://www.usnews.com/best-colleges/harding-university-10311",
"Montana State": "https://www.usnews.com/best-colleges/montana-state-billings-2530",
"Florida Atlantic": "https://www.usnews.com/best-colleges/florida-atlantic-university-1481",
"South Dakota State University": "https://www.usnews.com/best-colleges/south-dakota-state-3471",
"Husson": "https://www.usnews.com/best-colleges/husson-university-2043",
"Kieser": "https://www.usnews.com/best-colleges/keiser-university-21519",
"Oakland University": "https://www.usnews.com/best-colleges/oakland-university-2307",
"Tennessee State": "https://www.usnews.com/best-colleges/tennessee-state-3522",
"University of Alaska": "https://www.usnews.com/best-colleges/university-of-alaska-fairbanks-1063",
"University of Toledo": "https://www.usnews.com/best-colleges/university-of-toledo-3131",
"Wingate University": "https://www.usnews.com/best-colleges/wingate-university-2985",
"Brandman University": "https://www.usnews.com/best-colleges/brandman-university-262086",
"Valdosta": "https://www.usnews.com/best-colleges/valdosta-state-university-1599",
"Western Kentucky University": "https://www.usnews.com/best-colleges/western-kentucky-university-2002",
"William Woods": "https://www.usnews.com/best-colleges/william-woods-university-2525",
"University of the Cumberlands": "https://www.usnews.com/best-colleges/university-of-the-cumberlands-1962",
"Wichita State": "https://www.usnews.com/best-colleges/wichita-state-university-1950",
"William Carey": "https://www.usnews.com/best-colleges/william-carey-university-2447",
"University of Southern Mississippi": "https://www.usnews.com/best-colleges/university-of-southern-mississippi-2441",
"Jackson State": "https://www.usnews.com/best-colleges/jackson-state-2410",
"Grand Canyon University": "https://www.usnews.com/best-colleges/grand-canyon-university-1074",
"Ferris State": "https://www.usnews.com/best-colleges/ferris-state-university-2260",
"Lindenwood": "https://www.usnews.com/best-colleges/lindenwood-2480",
"Missouri State": "https://www.usnews.com/best-colleges/southeast-missouri-state-2501",
"Morgan State": "https://www.usnews.com/best-colleges/morgan-state-2083",
"SBCC": "https://www.usnews.com/education/community-colleges/santa-barbara-city-college-CC07599"
}

def get_gpa_index(GPA):
    if GPA == 5:
        return 0
    else:
        return (190*e**GPA)/(e**(2*GPA)+1)+5

def get_volunteer_index(hours):
    if hours <= 100:
        return .25*(-hours + 100)
    else:
        return -1*(hours-100)**(1/3)

def get_asb_index(asb):
    if asb == "Yes":
        return 0
    if asb == "No":
        return 15

def get_ap_index(p, t):
    diff = 5*(t - p)
    if t < 3:
        diff+=20
    elif t >= 3 and t < 6:
        diff+=10
    return diff

def college_index(gpa, pTaken, pPassed, vHours, ASB):
    index = math.floor(100-get_gpa_index(gpa)-get_volunteer_index(vHours)-get_asb_index(ASB)-get_ap_index(pPassed, pTaken))
    if isStretch == "stretch":
        index+=15
    if index > 100:
        index = 100
    elif index < 13:
        index = 13
    return index

def get_colleges(cIndex):
    global collegesIn
    collegesIn = []
    keyList = list(colleges.keys())
    valueList = list(colleges.values())
    for x in range(len(colleges)):
        if len(collegesIn) == 5:
            return collegesIn
        if cIndex >= valueList[x]:
            collegesIn.append(keyList[x])


def get_widths(num):
    num = 4-num
    if isStretch == "stretch":
        w = math.floor(((colleges[collegesIn[num]])/(cinDex+30))*100)
    else:
        w = math.floor(((colleges[collegesIn[num]])/(cinDex))*100)
    if w >=100:
        w=99
    return w

def send_results(width, cNum, num, w):
    return "Your " + cNum + " " + isStretch + " school is " + collegesIn[num] + "! You are " + str(w) + "% likely to get in."

def process_name(name):
    if name == "":
        return " "
    else:
        return "Hello " + name + "! Here are your top five most likely to get into:"

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/form")
def render_form():
    return render_template('form.html')

@app.route("/results")
def render_results():
    global isStretch
    gpa = float(request.args['uGPA'])
    pTaken = int(request.args['uAPTaken'])
    pPassed = int(request.args['uAPpassed'])
    vHours = int(request.args['uvHours'])
    ASB = request.args['ASB']
    name = request.args['uname']
    isStretch = request.args['stretch']


    global cinDex
    cinDex = college_index(gpa,pTaken, pPassed, vHours, ASB)
    c = get_colleges(cinDex)
    w1 = get_widths(0)
    w2 = get_widths(1)
    w3 = get_widths(2)
    w4 = get_widths(3)
    w5 = get_widths(4)

    return render_template('results.html', width1 = w1, width2 = w2, width3 = w3, width4 = w4, width5 = w5, collegeTop = send_results(w1, "top", 0, w1), collegeSecond = send_results(w2, "second", 1, w2), collegeThird = send_results(w3, "third", 2, w3), collegeFourth = send_results(w4, "fourth", 3, w4), collegeFifth = send_results(w5, "fifth", 4, w5), link1 = collegeLinks[collegesIn[0]], link2 = collegeLinks[collegesIn[1]], link3 = collegeLinks[collegesIn[2]], link4 = collegeLinks[collegesIn[3]], link5 = collegeLinks[collegesIn[4]], img1 = collegesIn[0], img2 = collegesIn[1], img3 = collegesIn[2], img4 = collegesIn[3], img5 = collegesIn[4], rName = process_name(name))

if __name__=="__main__":
    app.run(debug=True)
