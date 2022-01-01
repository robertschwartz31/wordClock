from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from datetime import datetime
from datetime import timedelta
from kivy.uix.label import Label


#These are all the objects that I deem to be required by the entire app

gridDefinition = {

    1 : [str(i) + ', ' + '1' for i in range(0, 13)],
    2 : [str(i) + ', ' + '2' for i in range(0, 13)],
    3 : [str(i) + ', ' + '3' for i in range(0, 13)],
    4 : [str(i) + ', ' + '4' for i in range(0, 13)],
    5 : [str(i) + ', ' + '5' for i in range(0, 13)],
    6 : [str(i) + ', ' + '6' for i in range(0, 13)],
    7 : [str(i) + ', ' + '7' for i in range(0, 13)],
    8 : [str(i) + ', ' + '8' for i in range(0, 13)],
    9 : [str(i) + ', ' + '9' for i in range(0, 13)],
}

display = {

    1 : ["I", "T", "'", "S", "O", "T", "E", "N", "A", "H", "A", "L", "F"],
    2 : ["T", "W", "E", "N", "T", "Y", "Q", "U", "A", "R", "T", "E", "R"],
    3 : ["A", "F", "I", "V", "E", "R", "M", "I", "N", "U", "T", "E", "S"],
    4 : ["P", "A", "S", "T", "T", "O", "Z", "O", "N", "E", "T", "W", "O"],
    5 : ["T", "H", "R", "E", "E", "F", "O", "U", "R", "F", "I", "V", "E"],
    6 : ["S", "I", "X", "S", "E", "V", "E", "N", "E", "I", "G", "H", "T"],
    7 : ["N", "I", "N", "E", "T", "E", "N", "E", "L", "E", "V", "E", "N"],
    8 : ["T", "W", "E", "L", "V", "E", "O", "'", "C", "L", "O", "C", "K"],
    9 : ["M", "R", "O", "B", "P", "S", "C", "H", "W", "A", "R", "T", "Z"],
    # 9 : ["M", "N", "I", "C", "K", "S", "B", "A", "K", "E", "R", "T", "Z"],
    # 9 : ["D", "E", "B", "O", "R", "A", "H", "H", "R", "E", "I", "D", "Z"],
    # 9 : ["D", "E", "V", "A", "N", "A", "E", "W", "A", "L", "D", "D", "Z"],

}

wordDict = {

    'its' : [str(i) + ', ' + '1' for i in range(0, 4)],
    'ten1' : [str(i) + ', ' + '1' for i in range(5, 8)],
    'half' : [str(i) + ', ' + '1' for i in range(9, 13)],
    'twenty' : [str(i) + ', ' + '2' for i in range(0, 6)],
    'quarter' : [str(i) + ', ' + '2' for i in range(6, 13)],
    'five1' : [str(i) + ', ' + '3' for i in range(1, 5)],
    'minutes' : [str(i) + ', ' + '3' for i in range(6, 13)],
    'past' : [str(i) + ', ' + '4' for i in range(0, 4)],
    'to' : [str(i) + ', ' + '4' for i in range(4, 6)],
    'one' : [str(i) + ', ' + '4' for i in range(7, 10)],
    'two' : [str(i) + ', ' + '4' for i in range(10, 13)],
    'three' : [str(i) + ', ' + '5' for i in range(0, 5)],
    'four' : [str(i) + ', ' + '5' for i in range(5, 9)],
    'five2' : [str(i) + ', ' + '5' for i in range(9, 13)],
    'six' : [str(i) + ', ' + '6' for i in range(0, 3)],
    'seven' : [str(i) + ', ' + '6' for i in range(3, 8)],
    'eight' : [str(i) + ', ' + '6' for i in range(8, 13)],
    'nine' : [str(i) + ', ' + '7' for i in range(0, 4)],
    'ten2' : [str(i) + ', ' + '7' for i in range(4, 7)],
    'eleven' : [str(i) + ', ' + '7' for i in range(7, 13)],
    'twelve' : [str(i) + ', ' + '8' for i in range(0, 6)],
    'oClock' : [str(i) + ', ' + '8' for i in range(6, 13)],
    'rob' : [str(i) + ', ' + '9' for i in range(1, 4)],
    'schwartz' : [str(i) + ', ' + '9' for i in range(5, 13)],
    # 'nick' : [str(i) + ', ' + '9' for i in range(1, 5)],
    # 'baker' : [str(i) + ', ' + '9' for i in range(6, 11)],
    # 'deborah' : [str(i) + ', ' + '9' for i in range(0, 7)],
    # 'reid' : [str(i) + ', ' + '9' for i in range(8, 12)],
    # 'evan' : [str(i) + ', ' + '9' for i in range(1, 5)],
    # 'ewald' : [str(i) + ', ' + '9' for i in range(6, 11)],

}

wordNames = ['its', 'ten', 'half', 'twenty', 'quarter', 'five1', 'minutes',
             'past', 'to']

hourList = ['one', 'two', 'three', 'four', 'five2',
            'six', 'seven', 'eight', 'nine', 'ten2',
            'eleven', 'twelve']

wordNames.extend(hourList)
wordNames.extend(['rob', 'schwartz'])
# wordNames.extend(['nick', 'baker'])
# wordNames.extend(['deborah', 'reid'])
# wordNames.extend(['evan', 'ewald'])

displayItems = display.items()

class wordClock(App):

    def build(self):

        currentTime = datetime.now()
        Clock.schedule_interval(self.update_clock, 1)
        currentTimeFormat = currentTime.strftime('%H:%M:%S')

        main_layout = BoxLayout(orientation="vertical")

        self.buttons = {}

        for key, items in displayItems:

            h_layout = BoxLayout()

            for label in range(len(items)):

                button = ToggleButton(
                    text= items[label],
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    background_color="black",
                    background_normal='',
                    color='black',
                    font_size=40,
                    bold=True

                )

                self.buttons[str(label) + ', ' + str(key)] = button

                h_layout.add_widget(button)

            main_layout.add_widget(h_layout)

        return main_layout

    def getWordTime(self):

        clockTime = datetime.now()
        fullTime = clockTime.strftime('%I:%M:%S')
        hour = int(clockTime.strftime('%I')) % 12
        minute = int(clockTime.strftime('%M'))
        second = int(clockTime.strftime('%S'))

        if int(round(minute / 5, 0)) > 6:
            hour = hour + 1

        if second > 30:
            minute = minute + 1

        hourList = ['one', 'two', 'three', 'four', 'five2',
                'six', 'seven', 'eight', 'nine', 'ten2',
                'eleven', 'twelve']

        minuteApprox = int(round(minute / 5, 0))

        def wordList(minApprox, hr):

            if minApprox == 0:
                time = [hourList[hr - 1], 'oClock']
                return time

            elif minApprox == 1:
                time = ['five1', 'past', hourList[hr - 1]]
                return time

            elif  minApprox == 2:
                time = ['ten1', 'past', hourList[hr - 1]]
                return time

            elif minApprox == 3:
                time = ['quarter', 'past', hourList[hr - 1]]
                return time

            elif minApprox == 4:
                time = ['twenty', 'past', hourList[hr - 1]]
                return time

            elif minApprox == 5:
                time = ['twenty', 'five1', 'past', hourList[hr - 1]]
                return time

            elif minApprox == 6:
                time = ['half', 'past', hourList[hr - 1]]
                return time

            elif minApprox == 7:
                time = ['twenty', 'five1', 'to', hourList[hr - 1]]
                return time

            elif minApprox == 8:
                time = ['twenty', 'to', hourList[hr - 1]]
                return time

            elif minApprox == 9:
                time = ['quarter', 'to', hourList[hr - 1]]
                return time

            elif minApprox == 10:
                time = ['ten1', 'to', hourList[hr - 1]]
                return time

            elif minApprox == 11:
                time = ['five1', 'to', hourList[hr - 1]]
                return time

            else:
                time = [hourList[hr - 1], 'oClock']
                return time

        selectedWordList = wordList(minuteApprox, hour)

        fullVariableList = ['its']

        for word in range(len(selectedWordList)):
            fullVariableList.append(selectedWordList[word])

        fullVariableList.extend(['rob', 'schwartz'])
        # fullVariableList.extend(['nick', 'baker'])
        # fullVariableList.extend(['deborah', 'reid'])
        # fullVariableList.extend(['evan', 'ewald'])
        return fullVariableList

    def update_clock(self, *args):

        wordList = self.getWordTime()
        buttonList = self.buttons

        currentTime = datetime.now()
        currentTime = currentTime + timedelta(seconds = 1)

        gridList = []
        for row in gridDefinition:
            gridList.extend(gridDefinition[row])

        activeCoordinates = []
        for word in wordList:
            activeCoordinates.extend(wordDict[word])

        inactiveCoordinates = gridList
        for coordinate in activeCoordinates:
            gridList.remove(coordinate)

        for box in activeCoordinates:
            buttonList[box].background_normal = 'atlas://data/images/defaulttheme/button'
            buttonList[box].background_color = 'white'
            buttonList[box].color = 'black'
            buttonList[box].border = (16, 16, 16, 16)

        for box in inactiveCoordinates:
            buttonList[box].background_normal = ''
            buttonList[box].background_color = 'black'
            buttonList[box].color = 'black'
            buttonList[box].border = (16, 16, 16, 16)

if __name__ == "__main__":
    app = wordClock()
    app.run()
