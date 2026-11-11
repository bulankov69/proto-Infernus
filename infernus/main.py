class Activity:
    def __init__(self, Name, Associations):
        self.Name = Name
        self.Associations = Associations

WebActivity = Activity("Web", {"открой"})
AppActivity = Activity("App", {"открой", "запусти"})
VolumeActivity = Activity("Volume", {"увеличь", "прибавь", "уменьши", "убавь"})

def open_Web(WebUrl):
    pass

def open_App(AppName):
    pass

def get_AppList():
    pass

def change_Volume(Mode, Amount):
    pass

def resolve_Task(Sentence):
    pass

def break_Word(Word):
    pass

if __name__ == "__main__":  
    print(WebActivity.Name)
