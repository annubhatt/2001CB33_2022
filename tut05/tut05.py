try:
    import pandas as pd
    import math
    def octant_range_names(mod=5000):
     try:
        df = pd.read_excel("octant_input.xlsx")  #  input file reading
        df.head()
        df["U_Average"] = df["U"].mean()     #Making average for coloumns U,V,W 
        df["V_Average"] = df["V"].mean()
        df["W_Average"] = df["W"].mean()
        df["U1"] = df["U"]-df["U_Average"]  # Making new columns for U1,V2,W3 
        df["V2"] = df["V"]-df["V_Average"] 
        df["W3"] = df["W"]-df["W_Average"] 
        
        df.loc[((df.U1 > 0) & (df.V2 > 0) & (df.W3 >0)), "Octant"] = "+1" 
        df.loc[((df.U1 > 0) &(df.V2 > 0) & (df.W3 <0)), "Octant" ] = "-1"
        df.loc[((df.U1 < 0) &(df.V2 > 0) & (df.W3 >0)), "Octant" ] = "+2"
        df.loc[((df.U1 < 0) &(df.V2 > 0) & (df.W3 <0)), "Octant" ] = "-2"    #Mkaing octant column plus  integers assignment for each octant 
        df.loc[((df.U1 < 0) &(df.V2 < 0) & (df.W3 >0)), "Octant" ] = "+3"
        df.loc[((df.U1 < 0) &(df.V2 < 0) & (df.W3 <0)), "Octant" ] = "-3"
        df.loc[((df.U1 > 0) &(df.V2 < 0) & (df.W3 >0)), "Octant" ] = "+4"
        df.loc[((df.U1 > 0) &(df.V2 < 0) & (df.W3 <0)), "Octant" ] = "-4"
        
        X =df['Octant'].value_counts() #  this is the total count of number of values for each octant

        df.loc[0,"octant id"]="overall count"  # making octant id column and assignmnt of octant count under that.
        df.loc[0,"+1"]=X["+1"]      # assigning octant count under all octants(+1,-1,+2,-2,+3,-3,+4,-4)             
        df.loc[0,"-1"]=X["-1"]
        df.loc[0,"+2"]=X["+2"] 
        df.loc[0,"-2"]=X["-2"]
        df.loc[0,"+3"]=X["+3"]
        df.loc[0,"-3"]=X["-3"]
        df.loc[0,"+4"]=X["+4"]
        df.loc[0,"-4"]=X["-4"]
        Y=str(mod)
        df.loc[1,"octant id"]="mod"+" "+Y # assignment of input label based on the user
        try: 
          _d=math.ceil(29745/mod) # greatest integer function used 
          _l=0000
          _m=mod-1
          A=str(_l)
          B=str(_m)
          for j in range(_d) :
             if int(B)>=29744:
                df.loc[j+2,"octant id"]= A+"-"+"29744"
                _l=_m+1
                _m=_m+mod
                A=str(_l)
                B=str(_m)
             else:
                df.loc[j+2,"octant id"]= A+"-"+B
                _l=_m+1
                _m=_m+mod
                A=str(_l)
                B=str(_m)
          
          C=0 
          T=0
          P=2
          for j in range(_d) : # number of coloumns in the output for each octant 
              for i in range(mod) : #running at each 5000 iterations (0-5000,5001-10000,......25000-30000)
                  if df["Octant"][T]=="+4" : # counting number of +4 octant in range of 0-30000
                     C+=1
                  T+=1
                  if T== 29745 : #break loop at T=29745 
                    break
              df.loc[P,"+4"]=C #assignment of count of +4 in each coloumn by iterating P
              P=P+1
              C=0
              j=7
          C=0
          T=0
          P=2
          for j in range(_d) :# count of coloumns in the output for each octant
              for i in range(mod) :
                  if df["Octant"][T]=="-4" :# cFrequency of number of -4 octant in range of 0-30000
                     C =C+1
                  T=T+1
                  if T== 29745 :
                    break
              df.loc[P,"-4"]=C #assigning count of -4 in each coloumn by iterating P
              P=P+1
              C=0
              j=7
          C=0
          T=0
          P=2
          for j in range(_d) :# no of coloumns in the output for each octant
              for i in range(mod) :
                  if df["Octant"][T]=="+3" :# counting number of +3 octant in range of 0-30000
                     C =C+1
                  T=T+1
                  if T== 29745 :
                    break
              df.loc[P,"+3"]=C #assignment of count of +3 in each coloumn by iterating P
              P=P+1
              C=0
              j=7
          C=0
          T=0
          P=2
          for j in range(_d) :# count of coloumns in the output for each octant
              for i in range(mod) :
                  if df["Octant"][T]=="-3" :# frequency of number of -3 octant in range of 0-30000
                     C =C+1
                  T=T+1
                  if T== 29745 :
                    break
              df.loc[P,"-3"]=C #assignment of count of -3 in each coloumn by iterating P
              P=P+1
              C=0
              j=7
          C=0
          T=0
          P=2
          for j in range(_d) :# count of coloumns in the output for each octant
              for i in range(mod) :
                  if df["Octant"][T]=="+2" :# frequency of number of +2 octant in range of 0-30000
                     C =C+1
                  T=T+1
                  if T== 29745 :
                    break
              df.loc[P,"+2"]=C #assignment of count of +2 in each coloumn by iterating P
              P=P+1
              C=0
              j=7 
          C=0
          T=0
          P=2
          for j in range(_d) :# no of coloumns in the output for each octant
              for i in range(mod) :
                  if df["Octant"][T]=="-2" :# counting number of -2 octant in range of 0-30000
                     C =C+1
                  T=T+1
                  if T== 29745 :
                    break
              df.loc[P,"-2"]=C #assigning count of -2 in each coloumn by iterating P
              P=P+1
              C=0
              j=7
          C=0
          T=0
          P=2
          for j in range(_d) :# no of coloumns in the output for each octant
              for i in range(mod) :
                  if df["Octant"][T]=="+1" :# counting number of +1 octant in range of 0-30000
                     C =C+1
                  T=T+1
                  if T== 29745 :
                    break
              df.loc[P,"+1"]=C#assigning count of +1 in each coloumn by iterating P
              P=P+1
              C=0
              j=7    
          C=0
          T=0
          P=2
          for j in range(_d) :# count of coloumns in the output for each octant
              for i in range(mod) :
                  if df["Octant"][T]=="-1" :# frequency of number of -1 octant in range of 0-30000
                     C =C+1
                  T=T+1
                  if T== 29745 :
                    break
              df.loc[P,"-1"]=C #assignment of count of -1 in each coloumn by iterating P
              P=P+1
              C=0
              j=7
          A=[]
          B=[]
          C=[]
          for i in range(8) :  
              C.append(0)
          A.append(df["+1"][0])
          A.append(df["-1"][0])
          A.append(df["+2"][0])
          A.append(df["-2"][0])
          A.append(df["+3"][0])
          A.append(df["-3"][0])
          A.append(df["+4"][0])
          A.append(df["-4"][0])
          B.append(df["+1"][0])
          B.append(df["-1"][0])
          B.append(df["+2"][0])
          B.append(df["-2"][0])
          B.append(df["+3"][0])
          B.append(df["-3"][0])
          B.append(df["+4"][0])
          B.append(df["-4"][0])
          B.sort(reverse = True)
          for i in range(8) : 
              for j in range(8) : 
                  if A[j]==B[i] :
                      C[j]=i+1
                      j=9
          df.loc[0,"rank of +1"]=C[0]                 
          df.loc[0,"rank of -1"]=C[1]                 
          df.loc[0,"rank of +2"]=C[2]
          df.loc[0,"rank of -2"]=C[3]
          df.loc[0,"rank of +3"]=C[4]
          df.loc[0,"rank of -3"]=C[5]
          df.loc[0,"rank of +4"]=C[6]
          df.loc[0,"rank of -4"]=C[7]
          for v in range(_d) :
           e=[]
           f=[]
           g=[]
           for q in range(8) : 
            g.append(0)
           e.append(df["+1"][v+2])
           e.append(df["-1"][v+2])
           e.append(df["+2"][v+2])
           e.append(df["-2"][v+2])
           e.append(df["+3"][v+2])
           e.append(df["-3"][v+2])
           e.append(df["+4"][v+2])
           e.append(df["-4"][v+2])
           f.append(df["+1"][v+2])
           f.append(df["-1"][v+2])
           f.append(df["+2"][v+2])
           f.append(df["-2"][v+2])
           f.append(df["+3"][v+2])
           f.append(df["-3"][v+2])
           f.append(df["+4"][v+2])
           f.append(df["-4"][v+2])
           f.sort(reverse = True)
           for i in range(8) : 
                for j in range(8) : 
                    if e[j]==f[i] :
                        g[j]=i+1
                        j=9
           df.loc[v+2,"The rank of +1"]=g[0]                 
           df.loc[v+2,"The rank of -1"]=g[1]                 
           df.loc[v+2,"The rank of +2"]=g[2]
           df.loc[v+2,"The rank of -2"]=g[3]
           df.loc[v+2,"The rank of +3"]=g[4]
           df.loc[v+2,"The rank of -3"]=g[5]
           df.loc[v+2,"The rank of +4"]=g[6]
           df.loc[v+2,"The rank of -4"]=g[7]
           W_=[]
           C=0
           W_.append(df["The rank of +1"][0])
           W_.append(df["The rank of -1"][0])
           W_.append(df["The rank of +2"][0])
           W_.append(df["The rank of -2"][0])
           W_.append(df["The rank of +3"][0])
           W_.append(df["The rank of -3"][0])
           W_.append(df["The rank of +4"][0])
           W_.append(df["The rank of -4"][0])
          
           for j in range(8) :
               if W_[j]==1 :
                   C=j
                   if(C==0) :
                      C=1
                      df.loc[0,"Rank1 Octant ID is"]=C
                      j=8
                   if(C==1) :
                      C=-1
                      df.loc[0,"Rank1 Octant ID is"]=C
                      j=8
                   if(C==2) :
                      C=2
                      df.loc[0,"Rank1 Octant ID is"]=C
                      j=8
                   if(C==3) :
                      C=-2
                      df.loc[0,"Rank1 Octant  is"]=C
                      j=8
                   if(C==4) :
                       C=3
                       df.loc[0,"Rank1 Octant ID is"]=C
                       j=8
                   if(C==5) :
                       C=-3
                       df.loc[0,"Rank1 Octant ID is"]=C
                       j=8
                   if(C==6) :
                       C=4
                       df.loc[0,"Rank1 Octant ID is"]=C
                       j=8
                   if(C==7) :
                      C=-4
                      df.loc[0,"Rank1 Octant ID is"]=C
                      j=8
           for i in range(_d) :
              Y=[]
              C=0
              Y.append(df["rank of +1"][i+2])
              Y.append(df["rank of -1"][i+2])
              Y.append(df["rank of +2"][i+2])
              Y.append(df["rank of -2"][i+2])
              Y.append(df["rank of +3"][i+2])
              Y.append(df["rank of -3"][i+2])
              Y.append(df["rank of +4"][i+2])
              Y.append(df["rank of -4"][i+2])
              for j in range(8) :
                  if Y[j]==1 :
                      C=j
                      if(C==0) :
                         C=1
                         df.loc[i+2,"Rank1 Octant ID"]=C
                         j=8
                      if(C==1) :
                         C=-1
                         df.loc[i+2,"Rank1 Octant ID"]=C
                         j=8
                      if(C==2) :
                         C=2
                         df.loc[i+2,"Rank1 Octant ID"]=C
                         j=8
                      if(C==3) :
                         C=-2
                         df.loc[i+2,"Rank1 Octant ID"]=C
                         j=8
                      if(C==4) :
                          C=3
                          df.loc[i+2,"Rank1 Octant ID"]=C
                          j=8
                      if(C==5) :
                          C=-3
                          df.loc[i+2,"Rank1 Octant ID"]=C
                          j=8
                      if(C==6) :
                          C=4
                          df.loc[i+2,"Rank1 Octant ID"]=C
                          j=8
                      if(C==7) :
                         C=-4
                         df.loc[i+2,"Rank1 Octant ID"]=C
                         j=8
          
          df.loc[_d+5,"+1"]=" Octant ID"
          _k=0
          _o=0
          _n=_d+6
          for i in range(8) :
              if(i%2==0) :
                  _k=_k+1
                  df.loc[_n,"+1"]=_k
                  _n=_n+1
              else :
                  _o=_o-1
                  df.loc[_n,"+1"]=_o
                  _n=_n+1
                  
          octant_name_id_mapping = {"1": "Internal outward interaction", "-1": "External outward interaction", "2": "External Ejection",
                                        "-2": "Internal Ejection", "3": "External inward interaction", "-3": "Internal inward interaction", "4": "Internal sweep", "-4": "External sweep"}      
          df.loc[_d+5,"-1"]="Octant Name "
          df.loc[_d+5,"+3"]="Count of Rank 1 Mod Values"
          _k=0
          _o=0
          _n=_d+6
          for i in range(8) :
              if(i%2==0) :
                  _k=_k+1
                  df.loc[_n,"-1"]=octant_name_id_mapping[str(_k)]
                  _n=_n+1
              else :
                  _o=_o-1
                  df.loc[_n,"-1"]=octant_name_id_mapping[str(_o)]
                  _n=_n+1
          df.loc[0,"Rank1 Octant Name"]=octant_name_id_mapping[str(int(df.loc[0,"Rank1 Octant ID"]))]
          for i in range(_d) :
              df.loc[i+2,"Rank1 Octant Name"]=octant_name_id_mapping[str(int(df.loc[i+2,"Rank1 Octant ID"]))]
          P=df['Rank1 Octant ID'].value_counts()
          h=[]
          for i in range(_d) :
              h.append(int(df["Rank1 Octant ID"][i+2]))
          _k=0
          for i in range(_d) :
              if(h[i]==1)  :
                  _k=_k+1
          df.loc[_d+6,"+3"]=_k
          _k=0
          for i in range(_d) :
              if(h[i]==-1)  :
                  _k=_k+1
          df.loc[_d+7,"+3"]=_k
          _k=0
          for i in range(_d) :
              if(h[i]==2)  :
                  _k=_k+1
          df.loc[_d+8,"+3"]=_k
          _k=0
          for i in range(_d) :
              if(h[i]==-2)  :
                  _k=_k+1
          df.loc[_d+9,"+3"]=_k
          _k=0
          for i in range(_d) :
              if(h[i]==3)  :
                  _k=_k+1
          df.loc[_d+10,"+3"]=_k
          _k=0
          for i in range(_d) :
              if(h[i]==-3)  :
                  _k=_k+1
          df.loc[_d+11,"+3"]=_k
          _k=0
          for i in range(_d) :
              if(h[i]==4)  :
                  _k=_k+1
          df.loc[_d+12,"+3"]=_k
          _k=0
          for i in range(_d) :
              if(h[i]==-4)  :
                  _k=_k+1
          df.loc[_d+13,"+3"]=_k
        
          df.to_excel('octant_output_ranking_excel.xlsx')
        except:
             print("Enter mod value which is greater than 0")    
     except :
      print("The input file does not exist or any error")    
    mod=5000 
    octant_range_names(mod)  
except:
    print(" Please install pandas,math and import it.")