import os
import numpy as np
import pandas as pd

def conversion_result(df,df_col,res_list):
    
    for i in range(0,len(df)):
        know_conv=df[df_col].iloc[i]
        know_list = know_conv.split(",")
        for j in range(0,len(know_list)):
            know_list[j]=know_list[j].replace(' ','')
            if know_list[j] not in res_list:    
                res_list.append(know_list[j])
    return res_list

def calculate_rank(model,ml_dict,fl): 
    
    if "." in model:
        score=1.5
        model=model.replace('.','')
    else:
        score=1
    model=model.replace(" ",'')
    for key, value in ml_dict.items(): 
        if model==key:
            ml_dict[model]=value+score
            fl=0
        
    if fl!=0:
        ml_dict[model]=score
    return ml_dict
   
def app_input(app_type,knw_type):
    filepath = os.path.dirname(__file__)
    df_m= pd.read_csv(filepath+'/usecase_resource.csv')

    for column in (df_m): 
        
        df_m[column]=df_m[column].replace('\n',' ', regex=True)
        df_m[column]=df_m[column].replace('\t',' ', regex=True) 

    #select unique knowledge conversion technique
    df = df_m[(df_m['DK_type'] == knw_type) & (df_m['Application_domain'] == app_type)]
    if df.empty:
        df=df_m[(df_m['Application_domain'] == app_type)]
    knw_con=[]
    knw_con=conversion_result(df,'Know_Conv',knw_con)
    inj_phase=[] 
    df_inj=df['DK_injection'].dropna()

    if not df_inj.empty:
        for it in range (0,len(knw_con)):
            df1 = df[(df['Know_Conv'].str.contains(knw_con[it]))]
            inj_res=conversion_result(df1,'DK_injection',inj_phase)
    
    d=df
    ml_dict={}
    fl=-1

    df=df_m[(df_m['Application_domain'] == app_type)]
    df['visited'] = 0
    indx=df.index.values.tolist()
    for i in range(0,len(inj_res)):
        for j in range(0,len(df)):
            loc_indx=indx[j]
            if df.at[loc_indx,'visited'] == 0:
                str_chk=df.at[loc_indx,'DK_injection']
                if inj_res[i] in str_chk:
                    models=df.at[loc_indx,'ML_model']

                    if models !="-1":
                        model_set = models.split(",")
                        for m in range(0,len(model_set)): #model itself
                            ml_dict=calculate_rank(model_set[m],ml_dict,fl)
                            fl=-1
                        df.at[loc_indx,'visited']=1
    ml_dict=dict(sorted(ml_dict.items(), key=lambda item: item[1],reverse=True))
    ml_nm=list(ml_dict.keys())[:5]
    ml_v=list(ml_dict.values())[:5]         
    m=inj_phase,ml_nm,ml_v#dict(sorted(ml_dict.items(), key=lambda item: item[1],reverse=True)[:5])
    return inj_phase,ml_nm,ml_v
