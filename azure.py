########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, json, time

# https://docs.microsoft.com/en-us/azure/cognitive-services/content-moderator/text-moderation-api

body = ["you do know hungarians, czechs, romanians are so , they throw #bananas at black soccer players, don\'t you? @user @user",
    "@user @user @user no, just seen this gay gorilla mindset nonsense, and him touting dershowitz as \"clean\" !",
    "@user the box as pictured contains a single inflatable prep-school-boy sex-doll.",
    "your desire for miscegenation genocide is the very definition of hate &amp; bigotry, @user   @user @user @user",
    "even if trump suppoers were correct that they are the majority, that is still a sad reality to be ashamed of.  #misogynist #america",
    "@user i was into \"\"pimps up hoes down\"\" \"\"hookers at the point\"\" documentaries by brent owens and the cathouse series as a kid lol  ",
    ",i thought the 500 dollar fine was more effective in discouraging people from littering in the higways.",
    "@user totally agree gary as i'm sick of british press blaming our fans to sell their crap papers  !!",
    "#cc   gorilla simulator: you need to do to adapt to the environment. the need to tear the city. material dam",
    "teen girl killed, 3 others injured in downtown oakland shooting. #guns #mentalillness #gangs ð¨ð¦ð¨ð¦ð¨ð¦ is   #orlando ",
    ",just #fucked another one #faggot #asscunt with my big #strapon. we both   ð°  ð±ð  @user @user @user @user @user",
    "rip lvl 93 almost 94 shield charger (~20 ex) | had a ~20 second delay, no mobs around me when the lag staed.   ",
    "@user good morning! hope yours is as happy as mine! extreme #masochist is coming in for a session in a few. i am",
    "i grew interest in a topic, and was promptly told to \"\"shut the fuck up\"\" every time that i decided to show my passion for it.  ",
    "fuck you #alzheimer's for taking my dad from me and turning him into a viual stranger   #heabroken",
    "god damn.. i can't have best friends, because they always leave me. this is realy painfull. #alone #pain   #cry",
    "i am who i am. #single #swagalicious   #pinay #filipina #cute",
    "we can relate! lol! happy #funfriday! #weightloss #healthy #fitness #pizza #fridayfeeling #friday   #weightgain",
    "@user @user + #bread x one million loaves of bread = me. #math #carbs   #lifestyle #blog ",
    "michelle obama âape in heelsâ case is just the beginning #donaldtrump  #america"]

headers = {
    # Request headers
    'Content-Type': 'text/plain',
    'Ocp-Apim-Subscription-Key': 'a5681f57404b4c749f1a38dd00b35e45',
}

params = urllib.parse.urlencode({
    # Request parameters
    'autocorrect': 'False',
    'PII': 'True',
    #'listId': '{list id}',
    'classify': 'True',
    'language': 'eng',
})

with open('azure_twitter_log.txt', 'w+') as log:
    for b in body:
        try:
            conn = http.client.HTTPSConnection('westus2.api.cognitive.microsoft.com')
            conn.request("POST", "/contentmoderator/moderate/v1.0/ProcessText/Screen?%s" % params,
                b, headers)
            response = conn.getresponse()
            data = str(response.read())
            conn.close()
            print(data)
            log.write(data + "\n")
            # = json.loads(data[2:len(data) - 1])

            # if (dj['Classification']['ReviewRecommended'] != False):
            #     line = [dj['OriginalText'], dj['Classification']]
            #     print(line)
            # else:
            #     print("Not flagged for review: " + dj['OriginalText'])
            time.sleep(1)

        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))


