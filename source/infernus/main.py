import webbrowser
import httpx

class Action:
    def __init__(self, Action, Server, Body, RequestMarkers, ParamMarkers):
        self.Action = Action
        self.Server = Server
        self.Body = Body
        self.RequestMarkers = RequestMarkers
        self.ParamMarkers = ParamMarkers
        self.Probability = 0

def parse_DocsFile(Path):
    with open(Path, "r") as f:
        Content = f.read()

    Content = Content.split("## ")

    ItemServer = (Content[1].split("\n"))[1].split("URL: ")[1]

    List = []

    for i in range(2, len(Content)):
        Lines = Content[i].split("\n")
        Method = ""
        Body = ""
        RequestMarkers = ""
        ParamMarkers = ""
        for Line in Lines:
            if "METHOD:" in Line: Method = Line.split("METHOD: ")[1]
            if "BODY:" in Line: Body = Line.split("BODY: ")[1]
            if "REQUEST_MARKERS:" in Line: RequestMarkers = (Line.split("REQUEST_MARKERS:")[1]).split(", ")
            if "PARAM_MARKERS:" in Line: ParamMarkers = (Line.split("PARAM_MARKERS:")[1]).split(",")
        List.append(Action(Method, ItemServer, Body, RequestMarkers, ParamMarkers))

    return List

def break_WordToTriplets(Word):
    if len(Word) <= 3:
        return [Word]
    else:
        TripletsList = []
        for step in range(0, len(Word)-2):
            Triplet = Word[step:3+step]
            TripletsList.append(Triplet)
        return TripletsList

def suggest_Probabilities(Sentence, ActionsList):
    ActionScore = 0
    ActionResults = dict()

    ParamScore = 0
    ParamResults = dict()

    SplitedSentence = Sentence.split()

    for Word in SplitedSentence:
        WordTriplets = break_WordToTriplets(Word)
        ParamProbability = 0

        for Triplet in WordTriplets:
            for Action in ActionsList:
                for Association in Action.RequestMarkers:
                    if Triplet in Association:
                        ActionScore+=1
                        Action.Probability+=1
                for Association in Action.ParamMarkers:
                    if Triplet in Association:
                        ActionScore+=10
                        Action.Probability+=10

                        ParamScore+=1
                        ParamProbability+=1
        
        if ParamProbability != 0: ParamResults.update({Word:int(ParamProbability/(ParamScore/100))})

    for Action in ActionsList:
        if Action.Probability != 0:
            ActionResults.update({Action:int(Action.Probability/(ActionScore/100))})

    return [dict(sorted(ActionResults.items(), key=lambda item: item[1], reverse=True)),
        dict(sorted(ParamResults.items(), key=lambda item: item[1], reverse=True))]

def make_POST(URL, json):
    response = httpx.request('POST', URL, json=json)
    return response.status_code

def execute_ByProbability(ActionProbabilities):
    Action = next(iter(ActionProbabilities[0]))
    Method = (Action.Action.split(" "))[0]

    Endpoint = "http://"+Action.Server+(Action.Action.split(" "))[1]

    Param = next(iter(ActionProbabilities[1]))
    Body = dict({Action.Body:Param})

    if Method == "POST":
        make_POST(Endpoint, Body)

Actions = []

for i in parse_DocsFile("infernus/Tools.md"):
    Actions.append(i)

if __name__ == "__main__":
    UserRequest = input("Enter request: ")
    
    ActionProbabilities = suggest_Probabilities(UserRequest, Actions)
    execute_ByProbability(ActionProbabilities)