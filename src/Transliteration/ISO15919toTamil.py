class ISO15919toTamil:

    def __init__(self):
        # initialization
        self.uy = {
        'k':'க', 
        'ṅ':'ங',
        'c':'ச',
        'ñ':'ஞ',
        'ṭ':'ட',
        'ṇ':'ண',
        't':'த',
        'n':'ந',
        'p':'ப',
        'm':'ம',
        'y':'ய',
        'r':'ர',
        'l':'ல',
        'v':'வ',
        'ḻ':'ழ',
        'ḷ':'ள',
        'ṟ':'ற',
        'ṉ':'ன'
        }
        self.sym = {
        '':'்',
        'a':'',
        'ā':'ா',
        'i':'ி',
        'ī':'ீ',
        'u':'ு',
        'ū':'ூ',
        'e':'ெ',
        'ē':'ே',
        'ai':'ை',
        'o':'ொ',
        'ō':'ோ',
        'au':'ௌ'
        }
        self.iso = {
        'a':'அ',
        'ā':'ஆ',
        'i':'இ',
        'ī':'ஈ',
        'u':'உ',
        'ū':'ஊ',
        'e':'எ',
        'ē':'ஏ',
        'ai':'ஐ',
        'o':'ஒ',
        'ō':'ஓ',
        'au':'ஔ',
        'ḵ':'ஃ'
        }

    def iso15919_to_tamil(self,text):
        self.text= text.casefold()
        
        # converting word to list
        x=list(self.text)
        x.append(0)

        for i in range(len(x)):
            if(len(x)>1):
                if(x[i]=='a' and x[i+1]=='i'):
                    x[i]='ai'
                    x[i+1]=0
                if(x[i]=='a' and x[i+1]=='u'):
                    x[i]='au'
                    x[i+1]=0

        x.append(0)
        
        y=[]
        for i in range(len(x)):
            if x[i] in self.iso:
                y.append(self.iso[x[i]])
            elif x[i] in self.uy:
                if(x[i+1]) in self.sym:
                    y.append(self.uy[x[i]]+self.sym[x[i+1]])
                    x[i+1]=0
                else:
                    y.append(self.uy[x[i]]+self.sym[''])
            if x[i]==' ':
                y.append(" ")
            else:
                continue

        return (''.join(y))
