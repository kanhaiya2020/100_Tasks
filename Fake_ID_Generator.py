class Fake:
    def __init__(self):
        self.result=[]
    def get_result(self,text):
        import itertools
        TEXT = text.upper()  
        base_list = []
        super_base_list = []
        result = []
        def special_text_add(text):
            gf = []
            sa = text
            special_list = ['a', 'i', 'o', 's', 'h', 'c', 'O', 'S', 'H', 'C']
            data=['@','!','0','$','#','[','0','$','#','[']
            for var in text:
                if var in special_list:
                    i=special_list.index(var)
                    j=data[i]
                    x=sa.find(var)
                    sa=sa[:x]+j+sa[x+1:]
                    gf.append(sa)
            return gf

        #Create base_list:
        s = 0
        for var in range(len(text)):
            formula = TEXT[s:var + 1] + text[var + 1:len(text)]
            super_base_list.append(formula)
        
        #Add text in super_base_list:
        super_base_list.append(text)
        
        # Add Special in base_list
        for var in super_base_list:
            return_list = special_text_add(var)
            for i in return_list:
                base_list.append(i)

        
        # Add Combination in base_list
        for var in super_base_list:
            base_list.append(var)
        
        #ADD the _._ in base_list1
        base_list1 = base_list.copy()
        for var in base_list:
            base_list1.append(var+'_._')
        #print(base_list)
        #print(base_list1)
        
        #Result through permutation using base_list1:
        for var in base_list1:
            for var1 in itertools.permutations(var):
                temp = ''.join(list(var1))
                result.append(temp)
        result = list(set(result))
        self.result=result
 
    def Numberoffakeaccounts(self,text):
        self.get_result(text)
        count = 0
        for i in range(len(self.result)):
            count +=1
        return count
    
    def Print_allfakeID(self,text):
        self.get_result(text)
        choice = input("'We will show top 100 fake ID So type 'Yes' otherwise you type 'No' then We will save the all fake ID in a file'").lower().strip()
        if choice == 'yes':
            return self.result[:100]
        elif choice == 'no':
            x=datetime.datetime.now()
            x=str(x).split('.')[0]
            fname="date_"+str(x).replace(" ","_").replace(":","_")+".txt"
            #fname="abc.txt"
            f=open(fname,"w")
            f.write('\n'.join(self.result))
            f.close()
        else:
            return "Wrong Input"
    def isfakeID(self,text,match_text):
        self.get_result(text)
        if match_text in self.result:
            return True
        else:
            return False

# To create a Object:
f=Fake()