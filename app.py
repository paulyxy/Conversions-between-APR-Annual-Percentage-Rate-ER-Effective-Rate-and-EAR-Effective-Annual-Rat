# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 16:09:42 2023

@author: pyan
"""

import numpy as np
import streamlit as st


st.set_page_config(layout="wide")
st.title("APR (Annual Percentage Rate), ER (Effective Rate), and EAR (Effective Annual Rate)") 
st.write("By Dr. Yan, v1.0, 2/5/2023")

a1=f"##### For a pair of given APR (Annual Percentage Rate) and its compounding frequency (n1), we calculate:"
a2=f" ##### .... a) Effective Rate."
a3=f" ##### .... b) EAR (Effective Annual Rate)."
a4=f"##### With more information: the second compounding frequency (n2), we calculate:"
a5=f" ##### ...  c) equivalent effective rate (for n2), and"
a6=f" ##### ...  d) equivalent APR2 (for n2)."


with st.expander("Click here to see the explanation. After that, click here again to hide it."):
    st.write(a1)
    st.write(a2)
    st.write(a3)
    st.write(a4)
    st.write(a5)
    st.write(a6)
#
col1, col2 =st.columns([1,1])

APR1= col1.number_input('Step 1: Input your APR (Annual Percentage Rate), such as 0.1')
a=" Step2: choose from a list for the given compounding frequency (1000 is for continuously compounded)"
n1= col1.selectbox(a,(1,2,4,12,365,1000))

if n1==1000:
    EAR=np.exp(APR1)-1
else:
    EAR=(1+APR1/n1)**n1-1
    

if n1==1000:
    EAR1=APR1
else:
    EAR1=APR1/n1


if n1==1:
    k="annual"
elif n1==2:
    k="semi-annual"
elif n1==4:
    k="quarterly"
elif n1==12:
    k="monthly"
elif n1==365:
     k="daily"
else:
     k="continuously compounded"
x="The effective "+k+" rate is:"

with col1.expander("Click here to see the Effective Rate for frequency n1"):
    st.write(x)
    st.write(round(EAR1,6))
    
with col1.expander("Click here to see the corresponding EAR (Effective Annual Rate):"):
    st.write(round(EAR,6))

b=" Step 3: choose from a list for the second compounding frequency (1000 is for continuously compounded)"
n2= col2.selectbox(b,(1,2,4,12,365,1000))
#
if n2==1:
    k2="annual"
elif n2==2:
    k2="semi-annual"
elif n2==4:
    k2="quarterly"
elif n2==12:
    k2="monthly"
elif n2==365:
     k2="daily"
else:
     k2="continuously compounded"
x2="The equivalent Effective "+k2+" Rate is:"
x3="The equivalent APR2 compounded "+k2+" is:"    

#
if n2==1000:
    ER2=np.log(1+EAR)
    APR2=ER2
    x2="The equivalent continuously compounded rate is:"
    x3=x2
else:
    ER2=(1+EAR)**(1/n2)-1
    APR2=ER2*n2

    
with col2.expander("Click here to see the equivalent ER2 (effective rate 2):"):
    st.write(x2)
    st.write(round(ER2,8))
with col2.expander("Click here to see the equivalent APR2:"):
    st.write(x3)
    st.write(round(APR2,8))
      
        
        
        
        