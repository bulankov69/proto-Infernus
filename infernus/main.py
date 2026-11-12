import webbrowser

class Action:
    def __init__(self, Name, Action, RequestMarkers, ParamMarkers):
        self.Name = Name
        self.Action = Action
        self.RequestMarkers = RequestMarkers
        self.ParamMarkers = ParamMarkers
        self.Probability = 0

def open_Web(WebUrl):
    webbrowser.open(WebUrl)
    print(f"Opening {WebUrl} site")

def open_App(AppName):
    print(f"Opening {AppName} application")

def get_AppList():
    return ["Steam", "Firefox", "VS Code"]

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
            ActionResults.update({Action.Name:int(Action.Probability/(ActionScore/100))})
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

Actions = []

WebAction = Action("Open link", "link {url}", ["открой", "сайт", "ссылка"], [".com", ".ru", ".org"])
Actions.append(WebAction)

AppAction = Action("Launch app", "open_App", ["открой", "запусти"], get_AppList())
Actions.append(AppAction)

VolumeAction = Action("Change volume", "change_Volume {param}", ["увеличь", "прибавь", "уменьши", "убавь"], [""])
Actions.append(VolumeAction)    

if __name__ == "__main__":
    UserRequest = input("Enter request: ")

    ActionProbabilities = suggest_Probabilities(UserRequest, Actions)
    print(ActionProbabilities)
    execute_ByProbability(ActionProbabilities)