import webbrowser

class Action:
    def __init__(self, Action, Server, RequestMarkers, ParamMarkers):
        self.Action = Action
        self.Server = Server
        self.RequestMarkers = RequestMarkers
        self.ParamMarkers = ParamMarkers
        self.Probability = 0

def open_Web(WebUrl):
    webbrowser.open(WebUrl)
    print(f"Opening {WebUrl} site")

def open_App(AppName):
    print(f"Opening {AppName} application")

def change_Volume(Mode, Amount):
    pass

def suggest_Probabilities(Sentence, ActionsList):
    ActionScore = 0
    ActionResults = dict()

    ParamScore = 0
    ParamResults = dict()

    SplitedSentence = Sentence.split()

    for Word in SplitedSentence:
        WordTriplets = break_Word(Word)
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
            ActionResults.update({Action.Action:int(Action.Probability/(ActionScore/100))})
    return [dict(sorted(ActionResults.items(), key=lambda item: item[1], reverse=True)),
        dict(sorted(ParamResults.items(), key=lambda item: item[1], reverse=True))]

def execute_ByProbability(ActionProbabilities):
    Action = next(iter(ActionProbabilities[0]))
    Param = next(iter(ActionProbabilities[1]))
    if Action == "Open link":
        open_Web(Param)
    if Action == "Launch app":
        open_App(Param)
    if Action == "Change Volume":
        change_Volume("+", 15)

def break_Word(Word):
    if len(Word) <= 3:
        return {Word}
    else:
        TripletsList = []
        for step in range(0, len(Word)-2):
            Triplet = Word[step:len(Word)-3+step]
            TripletsList.append(Triplet)
        return TripletsList

def parse_DocsFile(Path):
    with open(Path, "r") as f:
        Content = f.read()

    Content = Content.split("## ")

    ItemServer = (Content[1].split("\n"))[1].split("URL:")[1]

    List = []

    for i in range(2, len(Content)):
        Lines = Content[i].split("\n")
        Method = ""
        RequestMarkers = ""
        ParamMarkers = ""
        for Line in Lines:
            if "METHOD:" in Line: Method = Line.split("METHOD: ")[1]
            if "REQUEST_MARKERS:" in Line: RequestMarkers = (Line.split("REQUEST_MARKERS:")[1]).split(", ")
            if "PARAM_MARKERS:" in Line: ParamMarkers = (Line.split("PARAM_MARKERS:")[1]).split(",")
        List.append(Action(Method, ItemServer, RequestMarkers, ParamMarkers))
    
    return List

Actions = []

for i in parse_DocsFile("infernus/Tools.md"):
    Actions.append(i)
  
if __name__ == "__main__":
    UserRequest = input("Enter request: ")
    
    ActionProbabilities = suggest_Probabilities(UserRequest, Actions)
    print(ActionProbabilities)
    execute_ByProbability(ActionProbabilities)
else:
    for i in parse_DocsFile("infernus/Tools.md"):
        print("----")
        print(i.Action)
        print(i.Server)
        print(i.RequestMarkers)
        print(i.ParamMarkers)