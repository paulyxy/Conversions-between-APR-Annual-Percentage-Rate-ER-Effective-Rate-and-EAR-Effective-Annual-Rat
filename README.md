# Conversions between APR (Annual Percentage Rate), ER (Effective Rate), and EAR (Effective Annual Rate) 

# Part I---------------------------------------------------------------
# For a pair of given APR1 (Annual Percentage Rate) and its compounding frequency (n1),
#  we calculate:
#    a) Effective Rate for n1 period
#    b) EAR (Effective Annual Rate)


# Part II---------------------------------------------------------------
# With more information: the second compounding frequency (n2), we calculate:
#   c) equivalent effective rate (for n2), and
#   d) equivalent APR2 (for n2).

# /////////////////////////////////////////////////////////////
# Formulae used
#
# For a given APR1 and n1
# -------------------------------------
   # 1) its effective rate is ER1=(APR1/n1)
   # 2) its EAR = (1+APR1/n1)^n1-1

# For a continuously compounded rate (APR1)
# -------------------------------------
   # 3) EAR = exp(APR1)-1
   # Note 1000 is a place holder indicating this rate is a continuously 
   # compounded rate.

# For a given n2
# -------------------------------------
   # 4) EA2 = (1+APR1/n1)*(n1/n2)-1
   # 5) APR2 = EA2*n2

## Two papers

##  A 2-step approach to estimate an effective ra
##      http://datayyy.com/doc_pdf/A_2step_approach_effective_rate.pdf
##
##  They are all equal 
##     http://datayyy.com/doc_pdf/they_are_all_equal.pdf
##
## Yan, v1.0, 2/5/2023
##  email paulyxy@gmail.com



