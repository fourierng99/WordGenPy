import numpy as np
import pandas as pd
import random

ENG_INPUT_PATH = 'eng\English Wordlist.csv'
DEU_INPUT_PATH = 'deu\GoetheA1.csv'
JAP_INPUT_PATH = 'eng\AdvanceIELTS.csv'
file_lst = ['eng\English Wordlist.csv','deu\GoetheA1.csv','eng\AdvanceIELTS.csv', 'deu\Duolingo.csv']
class WordGenerator:
    input_df = ''
    input_path = ''
    def __init__(self, input):
        try:
            self.input_df = pd.DataFrame()
            self.input_df = pd.read_csv(input, header=0,encoding='latin-1')
            self.input_path= input
        except:
            print('Error when parsing input to dataframe')

# This function generate k unlearned words from the list

    def GeneratedWord(self, k):
        valid_df = self.input_df[self.input_df['Checked'] == 0]
        r_choices = valid_df.sample(n = k)
        print(self.input_path)
        print('')
        print(r_choices.head(k).sort_index())
        self.SaveLearnedWord(r_choices.index)

# This function save generated words

    def SaveLearnedWord(self, ids):
        next_val = self.input_df['Checked'].max() + 1
        for id in  ids:
            self.input_df.loc[id,'Checked'] = next_val
        self.SaveToFile()

# This function Reset all generated words

    def ResetWords(self):
        self.input_df.loc[:,'Checked'] = np.zeros(self.input_df.shape[0])
        self.SaveToFile()

# This function reset last words generated by GenerateWords

    def ResetLasLearnedtWords(self):
        max_val = self.input_df['Checked'].max()
        if max_val == 0:
            return
        last_ids = self.input_df[self.input_df['Checked'] == max_val ].index
        for id in last_ids:
            self.input_df.loc[id, 'Checked'] = 0
            print(str(id) + ' ' + str(self.input_df.loc[id, 'Checked']))
        self.SaveToFile()

# This function reroll the generated results if you don't like it 

    def RerollWords(self, k):
        self.ResetLasLearnedtWords()
        self.GeneratedWord(k)

# This function show your last generated words:
    def ShowLastGeneratedWords(self):
        max_val = self.input_df['Checked'].max()
        if max_val == 0:
            print('You have not take any words')
            return
        print('You generated time(s): ' + str(max_val))
        print(self.input_df[self.input_df['Checked'] == max_val])

# This function save to file

    def SaveToFile(self):
        self.input_df.to_csv(self.input_path, index = False)
    
# This function give statistics for your learning

    def Stats(self):
        uncheck = self.input_df[self.input_df['Checked'] == 0].shape[0]
        total = self.input_df.shape[0]
        print('Total: ' + str(total))
        print('Words remaining: ' + str(uncheck))

WordGen = WordGenerator(ENG_INPUT_PATH)
while True:
    print('1. Take words')
    print('2. Reroll Words')
    print('3. Reset Last Learned Words')
    print('4. Reset words')
    print('5. Stats')
    print('6. Show your newest words')
    print('7. ChangeList')
    print('Other.Quit')
    x = input()
    if (int(x) == 1):
        WordGen.GeneratedWord(15)
    elif (int(x) == 2):
        WordGen.RerollWords(15)
    elif(int(x) ==3):
        WordGen.ResetLasLearnedtWords()
    elif(int(x) == 4):
        WordGen.ResetWords()
    elif(int(x) == 5):
        WordGen.Stats()
    elif(int(x) == 6):
        WordGen.ShowLastGeneratedWords()
    elif(int(x) == 7):
        print('Chooose File:')
        l = len(file_lst)
        for i in range (0,l):
            print(str(i + 1) + '. ' +file_lst[i])
    
        print(str(l + 1) + '. Return')
        y = input()
        if int(y) <= l and int(y) > 0:
            WordGen = WordGenerator(file_lst[int(y)-1])
        else:
                print('Oki back to the last')
    else:
        break