########### Python 3.2 #############
import ast, http.client, urllib.request, urllib.parse, urllib.error, base64, json, time

# https://docs.microsoft.com/en-us/azure/cognitive-services/content-moderator/text-moderation-api

body = ["How much longer are we going to wait for them to take care of themselves ?",
        "Its people like this that are the face that represents the filth of Islam .",
        "More black-on-white hate crime videos are posted here : http://ethniccrime.blogspot.com/p/ra...-on-video.html",
        "We need to deport all nonwhites immediately , that or stop letting more in and sterilize the ones here , that will fix the problem .",
        "Let mother nature evolve these people naturally because no amount of money or aid is going to drag these things into the civilized world where they serve absolutely no purpose .",
        "No doubt they ll be coming up with chocolate-colored Leprechauns and a Chinese flavored Uncle Sams too .",
        "Sardines and anchovies , for example , are basically 100 percent safe .",
        "Perhaps people will take you more seriously if you do nt make as many grammar errors and using repulsive language .",
        "Explain how liberals are liars and anti-White and tell her about crime statistics .",
        "I would like to say and I can proudly say that there are no jews in Iceland , those that tried to get here were all sent back to Germany ...",
        "They laugh at whites who obey the law , bother to get married , women who are chaste .",
        "now that ye mention it he does look a bit like this traveller i knew. i wonder if we gave him a wash would he really be a white guy with red hair ?",
        "I want to have 3 children ! 2 girls and 1 boy but the hardest part now is i got to try and find someone to make them with , but so far no luck",
        "Indeed, now they just need to feed themselves , educate themselves , police themselves ad nauseum ......",
        "May they just need to turn these savages loose , justice will take care of itself .",
        "Actually Monkeys and Apes are more noble creatures and rarely act violent it really is unfare to the Monkeys and Apes to be compared with subhuman Negroids who are by contrast very murderous .",
        "Why not just kick out all those Africans ?",
        "Notice the video title , whenever there is a fight between a white and non white , the white is always the racist",
        "The future is ours , as long as we do not sit by and wait to be overrun by the subhumans .",
        "You do not have to wait for this law to pass since already you would be expelled from your school for doing the above under some sort of hostile school environment clause , as you would at most places of work .",
        "To me it means that Jewish supremacists will never again allow Whites to have a say ."
        ]


#stormfront

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
            # print(data)
            # test = ast.literal_eval(data)
            # print(test["Classification"]["ReviewRecommended"])
            # print(test)
            log.write(data + "\n")
            dj = json.loads(data[2:len(data) - 1])
            djc = dj['Classification']
            print(b + "," + str(djc['ReviewRecommended']) + "," + str(djc['Category1']['Score'])
                + "," + str(djc['Category2']['Score']) + "," + str(djc['Category3']['Score']))

            # if (dj['Classification']['ReviewRecommended'] != False):
            #     line = [dj['OriginalText'], dj['Classification']]
            #     print(line)
            # else:
            #     print("Not flagged for review: " + dj['OriginalText'])
            time.sleep(1)

        except Exception as e:
            print("[Errno {0}] {1}".format(e, e))