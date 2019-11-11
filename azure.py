########### Python 3.2 #############
import ast, http.client, urllib.request, urllib.parse, urllib.error, base64, json, time

# https://docs.microsoft.com/en-us/azure/cognitive-services/content-moderator/text-moderation-api

body = ["How much longer are we going to wait for them to take care of themselves ?",
        "It's people like this that are the face that represents the filth of Islam .",
        "More black-on-white hate crime videos are posted here : http://ethniccrime.blogspot.com/p/ra...-on-video.html",
        "We need to deport all nonwhites immediately , that or stop letting more in and sterilize the ones here , that will fix the problem .",
        "Let mother nature evolve these people naturally because no amount of money or aid is going to drag these ' things ' into the civilized world where they serve absolutely no purpose .",
        "No doubt they 'll be coming up with chocolate-colored Leprechauns and a Chinese flavored Uncle Sam 's too .",
        "Sardines and anchovies , for example , are basically 100 percent safe ."]


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