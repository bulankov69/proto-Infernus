class Activity:
    def __init__(self, Name, Associations):
        self.Name = Name
        self.Associations = Associations
        self.Probability = 0

Activities = []

WebActivity = Activity("Web", ["открой", "сайт", "ссылка"])
Activities.append(WebActivity)

AppActivity = Activity("App", ["открой", "запусти"])
Activities.append(AppActivity)

VolumeActivity = Activity("Volume", ["увеличь", "прибавь", "уменьши", "убавь"])
Activities.append(VolumeActivity)

def open_Web(WebUrl):
    print(f"Opening {WebUrl} site")

def open_App(AppName):
    print(f"Opening {AppName} application")

def get_AppList():
    pass

def change_Volume(Mode, Amount):
    pass

def suggest_ActivityProbabilities(Sentence, ActivitiesList):
    SplitedSentence = Sentence.split()
    for Word in SplitedSentence:
        WordTriplets = break_Word(Word)
        for Triplet in WordTriplets:
            for Activity in ActivitiesList:
                for Association in Activity.Associations:
                    if Triplet in Association:
                        Activity.Probability+=1
    Results = []
    for Activity in ActivitiesList:
        if Activity.Probability == 0:
            pass
        else:
            Results.append(f"{Activity.Name}: {Activity.Probability}")
    return Results


def break_Word(Word):
    if len(Word) <= 3:
        return {Word}
    else:
        TripletsList = []
        for step in range(0, len(Word)-2):
            Triplet = Word[step:len(Word)-3+step]
            TripletsList.append(Triplet)
        return TripletsList
    

if __name__ == "__main__":
    UserRequest = input("Enter request: ")
    print(suggest_ActivityProbabilities(UserRequest, Activities))
